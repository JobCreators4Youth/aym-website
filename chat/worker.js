import knowledge from "./knowledge.js";

const SYSTEM_PROMPT = [
  "You are the AYM Assistant, the official website assistant for the Twenty-First Century African Youth Movement (AYM), a U.S. 501(c)(3) nonprofit.",
  "Answer questions about AYM using only the knowledge base below.",
  "Be warm, concise, and practical. Use short paragraphs or a few bullets.",
  "If a question is outside the knowledge base, say you do not have that detail and point to info@aym-inc.org or the Contact page.",
  "Never invent names, programs, prices, dates, partners, or impact numbers.",
  "Never ask for or repeat sensitive personal, financial, or medical information.",
  "Do not give legal, tax, medical, or immigration advice; recommend a qualified professional.",
  "Use relative website links such as donate.html, volunteer.html, store.html, chapter.html, and contact.html when they help.",
  "",
  "KNOWLEDGE BASE:",
  knowledge,
].join("\n");

const MAX_MESSAGES = 12;
const MAX_CONTENT = 2000;
const MAX_TOTAL = 12000;
const WINDOW_MS = 10 * 60 * 1000;
const MAX_REQUESTS = 40;
const hits = new Map();

function corsHeaders(origin, allowed) {
  const allow = allowed.length === 0 ? origin || "*" : allowed.includes(origin) ? origin : "";
  if (!allow) return null;
  return {
    "Access-Control-Allow-Origin": allow,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "86400",
    Vary: "Origin",
  };
}

function json(body, status, headers) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...headers, "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" },
  });
}

function limited(ip) {
  const now = Date.now();
  const recent = (hits.get(ip) || []).filter((t) => now - t < WINDOW_MS);
  if (recent.length >= MAX_REQUESTS) {
    hits.set(ip, recent);
    return true;
  }
  recent.push(now);
  hits.set(ip, recent);
  if (hits.size > 5000) {
    for (const [key, times] of hits) {
      if (!times.length || now - times[times.length - 1] > WINDOW_MS) hits.delete(key);
    }
  }
  return false;
}

function cleanMessages(input) {
  if (!Array.isArray(input)) return null;
  const messages = input
    .slice(-MAX_MESSAGES)
    .filter((m) => m && (m.role === "user" || m.role === "assistant"))
    .map((m) => ({ role: m.role, content: String(m.content || "").slice(0, MAX_CONTENT).trim() }))
    .filter((m) => m.content.length > 0);
  if (!messages.length) return null;
  const total = messages.reduce((n, m) => n + m.content.length, 0);
  if (total > MAX_TOTAL) return null;
  return messages;
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    const allowed = (env.ALLOWED_ORIGINS || "")
      .split(",")
      .map((s) => s.trim())
      .filter(Boolean);
    const cors = corsHeaders(origin, allowed);

    if (request.method === "OPTIONS") {
      if (!cors) return new Response("Origin not allowed", { status: 403 });
      return new Response(null, { status: 204, headers: cors });
    }

    if (request.method !== "POST") {
      return json({ error: "Method not allowed" }, 405, cors || {});
    }

    if (!cors) {
      return json({ error: "Origin not allowed" }, 403, {});
    }

    const ip = request.headers.get("CF-Connecting-IP") || "unknown";
    if (limited(ip)) {
      return json({ error: "Too many messages. Please wait a few minutes and try again." }, 429, cors);
    }

    if (!env.OPENAI_API_KEY) {
      return json({ error: "The assistant is not configured yet. Please contact info@aym-inc.org." }, 503, cors);
    }

    let payload;
    try {
      payload = await request.json();
    } catch (err) {
      return json({ error: "Invalid JSON body." }, 400, cors);
    }

    const messages = cleanMessages(payload && payload.messages);
    if (!messages) {
      return json({ error: "Please send a short question." }, 400, cors);
    }

    const base = (env.OPENAI_BASE_URL || "https://api.openai.com/v1").replace(/\/+$/, "");
    const model = env.OPENAI_MODEL || "gpt-4o-mini";
    const upstreamBody = {
      model,
      temperature: 0.3,
      max_tokens: 700,
      stream: true,
      messages: [{ role: "system", content: SYSTEM_PROMPT }, ...messages],
    };

    let upstream;
    try {
      upstream = await fetch(base + "/chat/completions", {
        method: "POST",
        headers: {
          Authorization: "Bearer " + env.OPENAI_API_KEY,
          "Content-Type": "application/json",
          Accept: "text/event-stream",
        },
        body: JSON.stringify(upstreamBody),
        signal: request.signal,
      });
    } catch (err) {
      return json({ error: "The assistant is unavailable right now. Please try again." }, 502, cors);
    }

    if (!upstream.ok) {
      const detail = await upstream.text().catch(() => "");
      console.error("LLM error", upstream.status, detail.slice(0, 500));
      return json({ error: "The assistant is unavailable right now. Please try again." }, 502, cors);
    }

    const type = upstream.headers.get("Content-Type") || "";
    if (type.includes("text/event-stream")) {
      return new Response(upstream.body, {
        status: 200,
        headers: {
          ...cors,
          "Content-Type": "text/event-stream; charset=utf-8",
          "Cache-Control": "no-store",
          Connection: "keep-alive",
        },
      });
    }

    let data;
    try {
      data = await upstream.json();
    } catch (err) {
      return json({ error: "The assistant sent an unreadable response. Please try again." }, 502, cors);
    }
    const reply =
      (data.choices && data.choices[0] && data.choices[0].message && data.choices[0].message.content) || "";
    if (!reply) {
      return json({ error: "The assistant sent an empty response. Please try again." }, 502, cors);
    }
    return json({ reply }, 200, cors);
  },
};
