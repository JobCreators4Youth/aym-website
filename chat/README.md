# AYM Assistant

The site-wide assistant works offline with a built-in AYM topic matcher in `assets/js/chat.js`. It makes no API requests and needs no API key or deployment. Answers are limited to known AYM topics; unknown questions are referred to AYM's contact details.

An optional Cloudflare Worker implementation is included for a future hosted language model. The website does not depend on that worker, and the widget does not call it.

## Files

- `chat/worker.js` — Optional Cloudflare Worker: CORS, input limits, rate limiting, streaming, OpenAI-compatible proxy.
- `chat/knowledge.js` — AYM facts and guardrails injected as the system prompt. Edit this to update answers.
- `chat/wrangler.toml` — worker name, allowed origins, model.
- `assets/js/chat.js` — the widget and offline AYM topic answers, loaded on every page.
- `assets/js/chat-config.js` — legacy optional worker endpoint setting; not needed by the offline widget.
- Widget styles live at the end of `assets/css/styles.css`.

## Deploy

```powershell
cd chat
npx wrangler login
npx wrangler secret put OPENAI_API_KEY
npx wrangler deploy
```

Copy the printed URL (for example `https://aym-chat.your-name.workers.dev`) into `assets/js/chat-config.js`:

```js
window.AYM_CHAT_ENDPOINT = "https://aym-chat.your-name.workers.dev";
```

Redeploy after editing `knowledge.js` with `npx wrangler deploy`.

## Origins

Edit `ALLOWED_ORIGINS` in `wrangler.toml` to match every domain the widget runs on. Multiple origins are comma-separated. The default includes the live site, GitHub Pages, and localhost. For local testing:

```powershell
python -m http.server 8000
```

Open `http://localhost:8000`. Requests from `file://` are blocked by CORS.

## Providers

The worker speaks the OpenAI chat-completions API, so any compatible provider works:

| Provider | `OPENAI_BASE_URL` | `OPENAI_MODEL` |
| --- | --- | --- |
| OpenAI | `https://api.openai.com/v1` (default) | `gpt-4o-mini` |
| OpenRouter | `https://openrouter.ai/api/v1` | `openai/gpt-4o-mini` |
| Groq | `https://api.groq.com/openai/v1` | `llama-3.3-70b-versatile` |

Set overrides as secrets:

```powershell
npx wrangler secret put OPENAI_BASE_URL
npx wrangler secret put OPENAI_MODEL
```

## Test

```powershell
curl.exe -X POST "https://aym-chat.your-name.workers.dev" `
  -H "Content-Type: application/json" `
  -H "Origin: https://www.aym-inc.org" `
  -d "{\"messages\":[{\"role\":\"user\",\"content\":\"What does AYM do?\"}]}"
```

Without a matching `Origin` header the worker returns `403`, which is expected.

## Limits and costs

- Max 12 messages, 2,000 characters each, 12,000 characters total per request.
- 40 requests per IP per 10 minutes, using in-memory counters. This is best-effort protection; add Cloudflare rate-limiting rules for stricter control.
- `gpt-4o-mini` costs roughly $0.15 per 1M input tokens and $0.60 per 1M output tokens. Each conversation is typically a fraction of a cent.

## Answer quality

The assistant only knows what is in `knowledge.js`. When AYM adds a product, program, event date, or staff member, add it there and redeploy. Keep the "IMPORTANT LIMITS" section so the model declines unknown questions instead of inventing answers.
