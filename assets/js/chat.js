(function () {
  "use strict";

  var STORE_KEY = "aym-chat-history";
  var MAX_HISTORY = 12;
  var history = [];
  var pending = false;
  var greeted = false;

  try {
    var saved = JSON.parse(sessionStorage.getItem(STORE_KEY) || "[]");
    if (Array.isArray(saved)) {
      history = saved.filter(function (m) {
        return m && (m.role === "user" || m.role === "assistant") && typeof m.content === "string";
      }).slice(-MAX_HISTORY);
    }
  } catch (err) {
    history = [];
  }

  var root = document.createElement("div");
  root.className = "aym-chat";
  root.innerHTML =
    '<button type="button" class="aym-chat__launcher" aria-expanded="false" aria-controls="aym-chat-panel" aria-label="Open AYM Assistant">' +
      '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 4h16a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H9l-4.6 3.45A1 1 0 0 1 3 19.6V6a2 2 0 0 1 1-2z"/></svg>' +
    "</button>" +
    '<section class="aym-chat__panel" id="aym-chat-panel" role="dialog" aria-modal="false" aria-labelledby="aym-chat-title" hidden>' +
      '<header class="aym-chat__head">' +
        '<div class="aym-chat__brand">' +
          '<span class="aym-chat__avatar" aria-hidden="true">AYM</span>' +
          "<div><h2 id=\"aym-chat-title\">AYM Assistant</h2><p>Ask about our programs</p></div>" +
        "</div>" +
        '<button type="button" class="aym-chat__close" aria-label="Close assistant">' +
          '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18"/></svg>' +
        "</button>" +
      "</header>" +
      '<div class="aym-chat__log" data-log role="log" aria-live="polite" aria-relevant="additions"></div>' +
      '<div class="aym-chat__suggest" data-suggest>' +
        '<button type="button" data-q="What does AYM do?">What does AYM do?</button>' +
        '<button type="button" data-q="How can I volunteer?">How can I volunteer?</button>' +
        '<button type="button" data-q="Where does AYM work?">Where does AYM work?</button>' +
        '<button type="button" data-q="How do I donate?">How do I donate?</button>' +
      "</div>" +
      '<form class="aym-chat__form" data-form>' +
        '<label class="aym-chat__sr" for="aym-chat-input">Your question</label>' +
        '<textarea id="aym-chat-input" rows="1" maxlength="1000" placeholder="Ask a question" enterkeyhint="send"></textarea>' +
        '<button type="submit" class="aym-chat__send" aria-label="Send message">' +
          '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12l16-8-6 16-2.6-6.4L4 12z"/></svg>' +
        "</button>" +
      "</form>" +
      '<p class="aym-chat__note">Answers use AYM website information and may be incomplete. Email <a href="mailto:info@aym-inc.org">info@aym-inc.org</a> for official answers.</p>' +
    "</section>";

  document.body.appendChild(root);

  var launcher = root.querySelector(".aym-chat__launcher");
  var panel = root.querySelector(".aym-chat__panel");
  var log = root.querySelector("[data-log]");
  var suggest = root.querySelector("[data-suggest]");
  var form = root.querySelector("[data-form]");
  var input = root.querySelector("#aym-chat-input");
  var sendBtn = root.querySelector(".aym-chat__send");
  var closeBtn = root.querySelector(".aym-chat__close");

  function scroll() {
    log.scrollTop = log.scrollHeight;
  }

  function bubble(role, text) {
    var row = document.createElement("div");
    row.className = "aym-chat__msg aym-chat__msg--" + role;
    var el = document.createElement("div");
    el.className = "aym-chat__bubble";
    if (text && role === "bot") {
      var routes = /\b(index|about|about-team|where-we-work|focus-art|focus-agriculture|focus-education|focus-entrepreneurship|focus-ecotourism|focus-ecotourism-forest-safari|focus-health|focus-technology|projects|events|volunteer|volunteer-apply|volunteer-fellowship|chapter|donate|store|contact)\.html\b/g;
      var cursor = 0;
      var match;
      while ((match = routes.exec(text))) {
        el.appendChild(document.createTextNode(text.slice(cursor, match.index)));
        var link = document.createElement("a");
        link.href = match[0];
        link.textContent = match[0];
        el.appendChild(link);
        cursor = match.index + match[0].length;
      }
      el.appendChild(document.createTextNode(text.slice(cursor)));
    } else if (text) {
      el.textContent = text;
    }
    row.appendChild(el);
    log.appendChild(row);
    scroll();
    return el;
  }

  function setPending(value) {
    pending = value;
    sendBtn.disabled = value;
    input.disabled = value;
    if (!value) input.focus();
  }

  function save() {
    try {
      sessionStorage.setItem(STORE_KEY, JSON.stringify(history.slice(-MAX_HISTORY)));
    } catch (err) {}
  }

  function hideSuggest() {
    if (suggest) suggest.hidden = true;
  }

  function addUser(text) {
    history.push({ role: "user", content: text });
    history = history.slice(-MAX_HISTORY);
    bubble("user", text);
    save();
  }

  function addAssistant(text) {
    history.push({ role: "assistant", content: text });
    history = history.slice(-MAX_HISTORY);
    save();
  }

  // This lightweight, offline knowledge matcher keeps the assistant useful
  // on static hosting without an API key, server, or network request.
  var answers = [
    { keys: ["mission", "what does aym", "about aym", "what is aym", "organization", "employment", "income", "earn money", "economic independence"], text: "AYM mobilizes and provides employment for Africa's unemployed and underemployed youth through education and work in technology, agribusiness, ecotourism, entrepreneurship, and the creative arts. Learn more on about.html." },
    { keys: ["stand for", "full name", "aym meaning", "what is the full name"], text: "AYM stands for the Twenty-First Century African Youth Movement. It is a U.S. 501(c)(3) nonprofit. See about.html." },
    { keys: ["volunteer", "volunteering", "volunteer role", "volunteer work", "get involved", "join aym"], text: "AYM welcomes volunteers in web design, digital marketing, writing, data and analytics, research, and project management. Many roles can be remote. See volunteer.html or apply at volunteer-apply.html." },
    { keys: ["apply", "application", "how to join", "sign up"], text: "You can apply for a volunteer role through volunteer-apply.html. The form asks about your interests, availability, and experience. For help with an application, contact info@aym-inc.org." },
    { keys: ["age", "eligibility", "requirements", "background check"], text: "Most AYM volunteer roles are open to people aged 16 or older who can work in English and pass a basic background check. Most roles do not require prior professional experience. See volunteer.html." },
    { keys: ["fellowship", "fellow"], text: "The AYM Youth Fellowship is a one-year placement for recent secondary-school leavers, with tracks in technology, agribusiness, project management, and ecotourism. Details are on volunteer-fellowship.html." },
    { keys: ["chapter", "start a chapter", "new chapter"], text: "Committed individuals or small groups can apply to start an AYM chapter. AYM provides a toolkit, governance support, and program guidance. See chapter.html." },
    { keys: ["fellowship track", "fellowship tracks", "fellowship program"], text: "The one-year AYM Youth Fellowship has four tracks: Tech and Digital Operations; Agribusiness and Sustainability; Project Management and Admin; and Ecotourism and Community Development. See volunteer-fellowship.html." },
    { keys: ["where", "country", "countries", "location", "mattru jong", "sierra leone", "kenya", "rwanda", "uganda"], text: "AYM's core chapter network includes Sierra Leone, Kenya, Rwanda, Uganda, the United Kingdom, and the United States, with additional chapters across Africa. Operations in Sierra Leone are centered in Mattru Jong. See where-we-work.html." },
    { keys: ["donate", "donation", "give", "giving", "payment"], text: "You can give through PayPal, Bitcoin, Cash App, Network for Good, or eBay for Charity on donate.html. Select a method there to see its details. For cheque, wire, stock, or planned gifts, contact info@aym-inc.org." },
    { keys: ["bitcoin", "crypto", "wallet"], text: "AYM accepts Bitcoin donations on the Bitcoin network. Open donate.html and choose Bitcoin to view the QR code, wallet address, and copy option. For a receipt, email info@aym-inc.org with your transaction ID." },
    { keys: ["cash app", "cashapp"], text: "AYM's Cash App is $C21stAYM. The donation details and link are on donate.html. Include your email in the payment note so AYM can send a receipt." },
    { keys: ["paypal"], text: "Choose PayPal on donate.html to open AYM's secure donation page. You can review or change the amount there." },
    { keys: ["card", "credit card", "visa", "mastercard"], text: "The current donation page does not have a card processor connected yet. You can use PayPal, Cash App, Bitcoin, Network for Good, or eBay for Charity on donate.html, or email info@aym-inc.org for help." },
    { keys: ["program", "focus area", "agriculture", "agribusiness", "education", "health", "healthcare", "technology", "ecotourism", "art", "entrepreneurship"], text: "AYM's focus areas are art, agriculture, education, entrepreneurship, ecotourism, healthcare, and technology. Explore the program pages from the Focus Areas menu." },
    { keys: ["forest safari", "safari", "guided forest", "birdwatching"], text: "AYM's Forest Safari offers guided forest walks, wildlife and birdwatching, rivers, and clearings. The site lists half-day and full-day options starting at $45. See focus-ecotourism-forest-safari.html." },
    { keys: ["mattru jong project", "jong river", "brick making", "one dollar campaign", "projects"], text: "AYM projects include the Mattru Jong ecotourism and enterprise hub, youth-led brick making, the One Dollar Campaign, and the African Youth Movement Lecture Series. See projects.html." },
    { keys: ["event", "conference", "webinar"], text: "AYM runs lectures, webinars, and community events. Check events.html for current information; dates that are not confirmed are not listed as definite." },
    { keys: ["store", "shop", "merchandise", "shirt", "product"], text: "The Impact Store is at store.html. The catalog is being updated; contact info@aym-inc.org if you need help with an order." },
    { keys: ["contact", "email", "phone", "address", "reach", "talk to"], text: "You can reach AYM at info@aym-inc.org or +1 (608) 879-5487. The U.S. office is at 6811 North Ave., Middleton, WI 53562. See contact.html." },
    { keys: ["tax", "tax deductible", "ein", "501", "receipt"], text: "AYM is a U.S. 501(c)(3) nonprofit; its EIN is 39-1742519. Donations are tax-deductible to the extent allowed by law. Keep your receipt and consult a qualified tax adviser about your circumstances." },
    { keys: ["impact", "lives", "enterprise", "members", "raised"], text: "AYM's website reports 5,000+ lives impacted, 50+ enterprises supported, 10K+ members, and $100K raised. See projects.html for more about the work." },
    { keys: ["history", "founded", "founder", "abu hassan", "abu-hassan"], text: "AYM was founded in 2000 in Wisconsin by Abu-Hassan Koroma to support rural Sierra Leonean youth. Learn more on about.html." },
    { keys: ["leadership", "ceo", "president", "board", "team"], text: "AYM's leadership includes founder and CEO Abu-Hassan Koroma, COO Dennis Charles Glover, CFO Mariama Stacy Koroma, and philanthropy director Erin Summers. See about-team.html for team information." },
    { keys: ["vision", "mission statement"], text: "AYM's vision is an Africa where young people are empowered and active drivers of change, and where communities are stable and economically self-sustaining. The mission and history are on about.html." },
  ];

  function normalizeQuestion(value) {
    var q = String(value || "").toLowerCase()
      .replace(/&/g, " and ")
      .replace(/[^a-z0-9 ]/g, " ")
      .replace(/\s+/g, " ").trim();
    var aliases = [
      [/\b(jobs?|career|livelihoods?)\b/g, " employment "],
      [/\b(internships?|placement)\b/g, " fellowship "],
      [/\b(chapter network|local group|branch)\b/g, " chapter "],
      [/\b(give money|giving|contribute|contribution|fundraising)\b/g, " donate "],
      [/\b(crypto|btc)\b/g, " bitcoin "],
      [/\b(merch|merchandise|products)\b/g, " store "],
      [/\b(health care)\b/g, " healthcare "],
      [/\b(volunteering|volunteer role|volunteer work)\b/g, " volunteer "]
    ];
    aliases.forEach(function (entry) { q = q.replace(entry[0], entry[1]); });
    return q.replace(/\s+/g, " ").trim();
  }

  function editDistanceOne(a, b) {
    if (Math.abs(a.length - b.length) > 1 || a === b) return false;
    var i = 0, j = 0, edits = 0;
    while (i < a.length && j < b.length) {
      if (a.charAt(i) === b.charAt(j)) { i++; j++; continue; }
      edits++;
      if (edits > 1) return false;
      if (a.length > b.length) i++;
      else if (b.length > a.length) j++;
      else { i++; j++; }
    }
    if (i < a.length || j < b.length) edits++;
    return edits === 1;
  }

  function answerLocally(question) {
    var q = normalizeQuestion(question);
    if (/^(hi|hello|hey|good morning|good afternoon|good evening)$/.test(q)) return "Hello! I can help with AYM's programs, volunteering, chapters, donations, events, and contact details. What would you like to know?";
    if (/^(thanks|thank you|thank you so much)$/.test(q)) return "You're welcome! If you need anything else about AYM, just ask.";
    if (/^(bye|goodbye|see you)$/.test(q)) return "Goodbye! You can come back any time with another question about AYM.";
    if (/^(who are you|what are you|are you a bot)$/.test(q)) return "I'm the AYM Assistant. I answer from information published on AYM's website, and I work locally without an API key.";

    // Use the previous topic to understand short follow-ups such as “How do I apply?”
    if (/\b(apply|qualify|it|that|them|those|more|there|same)\b/.test(q) && !/\b(volunteer|fellowship|chapter|donat|store|bitcoin|paypal|program|event|country|location)\b/.test(q)) {
      for (var h = history.length - 2; h >= 0; h--) {
        if (history[h].role === "user") {
          var previous = normalizeQuestion(history[h].content);
          if (/volunteer|fellowship|chapter|donat|store/.test(previous)) { q += " " + previous; }
          break;
        }
      }
    }

    var ignored = { a:1, an:1, and:1, are:1, can:1, does:1, do:1, for:1, how:1, i:1, in:1, is:1, it:1, me:1, of:1, on:1, or:1, the:1, to:1, what:1, when:1, where:1, which:1, who:1, with:1, you:1, your:1, tell:1, about:1, please:1 };
    var words = q.split(" ").filter(function (word) { return word.length > 2 && !ignored[word]; });
    var ranked = answers.map(function (item) {
      var score = 0;
      item.keys.forEach(function (key) {
        var phrase = normalizeQuestion(key);
        var keyWords = phrase.split(" ").filter(function (word) { return word.length > 2; });
        if (phrase.length > 3 && q.indexOf(phrase) !== -1) score = Math.max(score, 2.5 + Math.min(2, keyWords.length * 0.35));
        var overlaps = 0;
        words.forEach(function (word) {
          if (keyWords.indexOf(word) !== -1) overlaps++;
          else if (word.length >= 5 && keyWords.some(function (candidate) { return editDistanceOne(word, candidate); })) overlaps += 0.75;
        });
        score = Math.max(score, overlaps * 1.35 + (overlaps > 1 ? 0.5 : 0));
      });
      return { item: item, score: score };
    }).filter(function (entry) { return entry.score >= 2.2; })
      .sort(function (a, b) { return b.score - a.score; });

    if (ranked.length) {
      var selected = [ranked[0]];
      var asksSeveral = /\b(and|also|plus|as well as)\b/.test(q);
      if (asksSeveral) {
        ranked.slice(1).some(function (candidate) {
          if (candidate.score >= 2.2 && candidate.item !== selected[0].item) { selected.push(candidate); return true; }
          return false;
        });
      }
      return selected.map(function (entry) { return entry.item.text; }).join("\n\n");
    }
    return "I don't have that detail in AYM's website information. I can help with programs, volunteering, chapters, donations, locations, events, and contact details. For anything else, email info@aym-inc.org or call +1 (608) 879-5487.";
  }

  async function send(text) {
    text = String(text || "").trim();
    if (!text || pending) return;

    hideSuggest();
    addUser(text);
    input.value = "";
    input.style.height = "auto";
    setPending(true);

    var typing = bubble("bot", "");
    typing.classList.add("aym-chat__typing");
    typing.innerHTML = "<span></span><span></span><span></span>";
    window.setTimeout(function () {
      if (typing.parentNode) typing.parentNode.remove();
      var answer = answerLocally(text);
      bubble("bot", answer);
      addAssistant(answer);
      setPending(false);
      scroll();
    }, 280);
  }

  function greeting() {
    if (greeted) return;
    greeted = true;
    bubble("bot", "Hi, I am the AYM Assistant. Ask me about our programs, volunteering, chapters, donations, events, or the Impact Store.");
  }

  function open() {
    panel.hidden = false;
    launcher.setAttribute("aria-expanded", "true");
    if (!history.length) {
      greeting();
    } else {
      hideSuggest();
    }
    setTimeout(function () { input.focus(); }, 60);
  }

  function close() {
    panel.hidden = true;
    launcher.setAttribute("aria-expanded", "false");
    launcher.focus();
  }

  launcher.addEventListener("click", function () {
    if (panel.hidden) open();
    else close();
  });
  closeBtn.addEventListener("click", close);

  panel.addEventListener("keydown", function (event) {
    if (event.key === "Escape") close();
  });

  if (suggest) {
    suggest.addEventListener("click", function (event) {
      var btn = event.target.closest("button[data-q]");
      if (btn) send(btn.getAttribute("data-q"));
    });
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    send(input.value);
  });

  input.addEventListener("keydown", function (event) {
    if (event.key === "Enter" && !event.shiftKey && !event.isComposing) {
      event.preventDefault();
      form.requestSubmit();
    }
  });

  input.addEventListener("input", function () {
    input.style.height = "auto";
    input.style.height = Math.min(input.scrollHeight, 96) + "px";
  });

  history.forEach(function (message) {
    bubble(message.role === "user" ? "user" : "bot", message.content);
  });
  if (history.length) hideSuggest();
  scroll();
})();
