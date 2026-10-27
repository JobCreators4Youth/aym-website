// AYM site — small progressive enhancements (no dependencies)
(function () {
  "use strict";

  // Mobile navigation toggle
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Focus-area chips -> switch the displayed focus panel (landing page)
  var chips = document.querySelectorAll("[data-focus]");
  if (chips.length) {
    var panels = document.querySelectorAll("[data-focus-panel]");
    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        var key = chip.getAttribute("data-focus");
        chips.forEach(function (c) { c.classList.remove("is-active"); });
        chip.classList.add("is-active");
        panels.forEach(function (p) {
          p.hidden = p.getAttribute("data-focus-panel") !== key;
        });
      });
    });
  }

  // ---- Donation: amount + payment method -------------------------------
  var tierInput = document.querySelector("[data-tier-input]");
  var methodCta = document.querySelector("[data-method-cta]");
  var ctaNote = document.querySelector("[data-cta-note]");
  var tiers = document.querySelectorAll("[data-tier]");

  function selectedAmount() {
    if (tierInput && tierInput.value) {
      return { label: "$" + tierInput.value, isMonthly: false };
    }
    var sel = document.querySelector("[data-tier].is-active");
    if (!sel) return { label: "", isMonthly: false };
    var a = sel.getAttribute("data-amount") || "";
    if (a === "monthly") return { label: "", isMonthly: true };
    if (!a) return { label: "", isMonthly: false };
    return { label: a.charAt(0) === "$" ? a : "$" + a, isMonthly: false };
  }

  function refreshCta() {
    if (!methodCta) return;
    var m = document.querySelector("[data-method].is-active");
    var name = m ? m.getAttribute("data-name") : "";
    var amt = selectedAmount();
    var part = amt.isMonthly ? "monthly " : (amt.label ? amt.label + " " : "");
    methodCta.textContent = ("Donate " + part + "with " + name).replace(/\s+/g, " ").trim();
    methodCta.setAttribute("href", m ? (m.getAttribute("data-href") || "#") : "#");
    if (ctaNote) ctaNote.hidden = true;
  }

  tiers.forEach(function (t) {
    t.addEventListener("click", function () {
      var a = t.getAttribute("data-amount") || "";
      // Keep every tier with the same amount highlighted (hero picker + full list)
      tiers.forEach(function (x) {
        x.classList.toggle("is-active", x.getAttribute("data-amount") === a);
      });
      if (tierInput) tierInput.value = (a === "monthly") ? "" : a.replace(/[^0-9.]/g, "");
      refreshCta();
    });
  });

  if (tierInput) {
    tierInput.addEventListener("input", function () {
      if (tierInput.value) {
        tiers.forEach(function (x) { x.classList.remove("is-active"); });
      }
      refreshCta();
    });
  }

  var methodBtns = document.querySelectorAll("[data-method]");
  if (methodBtns.length) {
    var methodPanels = document.querySelectorAll("[data-method-panel]");
    methodBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var key = btn.getAttribute("data-method");
        methodBtns.forEach(function (b) { b.classList.remove("is-active"); });
        btn.classList.add("is-active");
        methodPanels.forEach(function (p) {
          p.hidden = p.getAttribute("data-method-panel") !== key;
        });
        refreshCta();
      });
    });
  }

  if (methodCta) {
    methodCta.addEventListener("click", function (e) {
      var href = methodCta.getAttribute("href");
      if (href && href !== "#") return;
      e.preventDefault();
      if (ctaNote) {
        var m = document.querySelector("[data-method].is-active");
        ctaNote.hidden = false;
        ctaNote.textContent = "Demo build — connect this button to AYM\u2019s " +
          (m ? m.getAttribute("data-name") : "") + " link (set data-href on that option).";
      }
    });
  }

  refreshCta();

  // Tabs (generic) — group defaults to the ungrouped set
  var tabButtons = document.querySelectorAll("[data-tab]");
  if (tabButtons.length) {
    tabButtons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var group = btn.getAttribute("data-tab-group");
        var btns = group
          ? document.querySelectorAll('[data-tab][data-tab-group="' + group + '"]')
          : document.querySelectorAll("[data-tab]:not([data-tab-group])");
        var pnls = group
          ? document.querySelectorAll('[data-tab-panel][data-tab-group="' + group + '"]')
          : document.querySelectorAll("[data-tab-panel]:not([data-tab-group])");
        btns.forEach(function (b) { b.classList.remove("is-active"); });
        pnls.forEach(function (p) {
          p.hidden = p.getAttribute("data-tab-panel") !== btn.getAttribute("data-tab");
        });
        btn.classList.add("is-active");
      });
    });
  }

  // Demo forms: prevent real submission, show a friendly confirmation
  document.querySelectorAll("form[data-demo]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var note = form.querySelector("[data-form-note]");
      if (note) {
        note.hidden = false;
        note.textContent = "Thanks — this is a demo form. In the live build this sends through your chosen form service.";
      }
    });
  });

  // Chip filters: reveal cards whose data-role tag matches the chosen filter
  document.querySelectorAll("[data-filters]").forEach(function (group) {
    var scope = group.closest("section") || document;
    var list = scope.querySelector("[data-filter-list]");
    var btns = group.querySelectorAll("[data-filter]");
    btns.forEach(function (b) {
      b.addEventListener("click", function () {
        btns.forEach(function (x) { x.classList.remove("is-active"); });
        b.classList.add("is-active");
        var f = b.getAttribute("data-filter");
        if (!list) return;
        list.querySelectorAll("[data-role]").forEach(function (card) {
          var tags = (card.getAttribute("data-role") || "").split(/\s+/);
          card.hidden = !(f === "all" || tags.indexOf(f) !== -1);
        });
      });
    });
  });

  // Demo actions (store cart / load-more): explain instead of a dead click
  document.querySelectorAll("[data-demo-msg]").forEach(function (b) {
    b.addEventListener("click", function () {
      var scope = b.closest("section") || document;
      var note = scope.querySelector("[data-demo-note]");
      if (note) {
        note.hidden = false;
        note.textContent = b.getAttribute("data-demo-msg");
      }
    });
  });

  // ---- Multi-step application form (volunteer) --------------------------
  document.querySelectorAll("form[data-apply]").forEach(function (form) {
    var panels = Array.prototype.slice.call(form.querySelectorAll(".apply__panel[data-step]"));
    var indicators = Array.prototype.slice.call(form.querySelectorAll("[data-step-indicator]"));
    var bar = form.querySelector("[data-apply-bar]");
    var back = form.querySelector("[data-apply-back]");
    var next = form.querySelector("[data-apply-next]");
    var submit = form.querySelector("[data-apply-submit]");
    var errorBox = form.querySelector("[data-apply-error]");
    var saved = form.querySelector("[data-apply-saved]");
    var review = form.querySelector("[data-review]");
    var done = document.querySelector("[data-apply-done]");
    var card = form.closest(".container") || document;
    var total = panels.length;
    var current = 0;
    var storeKey = "aym-volunteer-application";
    var saveTimer = null;

    if (!total) return;

    function escapeHtml(s) {
      return String(s).replace(/[&<>"']/g, function (c) {
        return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
      });
    }

    function ageFrom(v) {
      var d = new Date(v);
      if (isNaN(d)) return null;
      var t = new Date();
      var age = t.getFullYear() - d.getFullYear();
      var m = t.getMonth() - d.getMonth();
      if (m < 0 || (m === 0 && t.getDate() < d.getDate())) age--;
      return age;
    }

    function clearError(wrapper) {
      wrapper.classList.remove("is-invalid");
      var e = wrapper.querySelector(".field__error");
      if (e) e.remove();
    }

    function appendError(wrapper, msg) {
      if (wrapper.querySelector(".field__error")) return;
      var span = document.createElement("span");
      span.className = "field__error";
      span.textContent = msg;
      wrapper.appendChild(span);
    }

    function validatePanel(panel) {
      var ok = true;
      var firstBad = null;
      var nodes = panel.querySelectorAll("input, select, textarea");
      Array.prototype.forEach.call(nodes, function (el) {
        var wrapper = el.closest("label") || el.closest(".choice-group") || el.parentNode;
        if (el.type !== "radio") clearError(wrapper);
        if (el.type === "radio") return;
        var val = (el.value || "").trim();
        var msg = "";
        if (el.type === "checkbox") {
          if (el.required && !el.checked) msg = "This box is required.";
        } else if (el.required && !val) {
          msg = "This field is required.";
        } else if (val && el.type === "email" && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val)) {
          msg = "Enter a valid email address.";
        } else if (val && el.type === "url" && !/^https?:\/\/.+/i.test(val)) {
          msg = "Enter a valid URL starting with http:// or https://.";
        } else if (val && el.getAttribute("data-minchars") && val.length < (+el.getAttribute("data-minchars"))) {
          msg = el.getAttribute("data-error") || ("Please write at least " + el.getAttribute("data-minchars") + " characters.");
        } else if (val && el.getAttribute("data-minage") && ageFrom(val) < (+el.getAttribute("data-minage"))) {
          msg = el.getAttribute("data-error") || ("You must be at least " + el.getAttribute("data-minage") + " years old.");
        }
        if (msg) { wrapper.classList.add("is-invalid"); appendError(wrapper, msg); ok = false; firstBad = firstBad || el; }
      });
      // required radio groups
      Array.prototype.forEach.call(panel.querySelectorAll(".choice-group"), function (grp) {
        var radios = grp.querySelectorAll('input[type="radio"]');
        if (!radios.length) return;
        var required = Array.prototype.some.call(radios, function (r) { return r.required; });
        if (!required) return;
        var checked = Array.prototype.some.call(radios, function (r) { return r.checked; });
        if (!checked) { grp.classList.add("is-invalid"); appendError(grp, "Please choose an option."); ok = false; firstBad = firstBad || radios[0]; }
      });
      if (firstBad && !firstBad.closest("[hidden]")) firstBad.focus();
      return ok;
    }

    function show(index, opts) {
      opts = opts || {};
      current = Math.max(0, Math.min(total - 1, index));
      panels.forEach(function (p, i) { p.hidden = i !== current; p.classList.toggle("is-active", i === current); });
      indicators.forEach(function (ind, i) {
        ind.classList.toggle("is-active", i === current);
        ind.classList.toggle("is-done", i < current);
      });
      if (bar) bar.style.width = Math.round(((current + 1) / total) * 100) + "%";
      if (back) back.hidden = current === 0;
      if (next) next.hidden = current === total - 1;
      if (submit) submit.hidden = current !== total - 1;
      if (errorBox) errorBox.hidden = true;
      if (current === total - 1) buildReview();
      if (opts.scroll !== false) {
        var top = form.getBoundingClientRect().top + window.pageYOffset - 90;
        window.scrollTo({ top: top, behavior: "smooth" });
      }
    }

    function updateCounts() {
      Array.prototype.forEach.call(form.querySelectorAll("textarea[data-minchars]"), function (t) {
        var out = form.querySelector('[data-count-for="' + t.name + '"]');
        if (out) out.textContent = t.value.length + " characters";
      });
    }

    function collect() {
      var data = {};
      Array.prototype.forEach.call(form.querySelectorAll("input, select, textarea"), function (el) {
        if (!el.name) return;
        if (el.type === "checkbox") {
          if (form.querySelectorAll('[name="' + el.name + '"]').length > 1) {
            if (!Array.isArray(data[el.name])) data[el.name] = [];
            if (el.checked) data[el.name].push(el.value);
          } else {
            data[el.name] = el.checked;
          }
        } else if (el.type === "radio") {
          if (el.checked) data[el.name] = el.value;
        } else {
          data[el.name] = el.value;
        }
      });
      return data;
    }

    function buildReview() {
      if (!review) return;
      var data = collect();
      var map = {
        first: "First name", last: "Last name", email: "Email", phone: "Phone",
        country: "Country", city: "City / region", dob: "Date of birth",
        role: "Preferred role", experience: "Experience", portfolio: "Portfolio",
        commitment: "Time commitment", mode: "Volunteer type", start: "Start date", timezone: "Time zone",
        why: "Motivation", heard: "Heard about us", refname: "Reference name", refemail: "Reference email"
      };
      var html = "";
      Object.keys(map).forEach(function (k) {
        var v = data[k];
        if (v === undefined || v === "" || v === false) return;
        html += '<div class="review__row"><dt>' + escapeHtml(map[k]) + "</dt><dd>" + escapeHtml(String(v)) + "</dd></div>";
      });
      var skills = Array.prototype.slice.call(form.querySelectorAll('[name="skills"]:checked')).map(function (c) { return c.value; });
      if (skills.length) html += '<div class="review__row"><dt>Skills</dt><dd>' + escapeHtml(skills.join(", ")) + "</dd></div>";
      html += '<div class="review__row"><dt>Consents</dt><dd>' +
        (data.consent_bg && data.consent_coc ? "Background check &amp; code of conduct accepted" : "Not yet accepted") +
        "</dd></div>";
      review.innerHTML = html;
    }

    function persist() {
      try { localStorage.setItem(storeKey, JSON.stringify(collect())); } catch (e) { return; }
      if (saved) { saved.hidden = false; saved.textContent = "Draft saved"; }
    }

    function restore() {
      var raw = null;
      try { raw = localStorage.getItem(storeKey); } catch (e) { return; }
      if (!raw) return;
      var data;
      try { data = JSON.parse(raw); } catch (e) { return; }
      Object.keys(data).forEach(function (k) {
        var el = form.querySelector('[name="' + k + '"]');
        if (!el) return;
        if (el.type === "checkbox") {
          if (Array.isArray(data[k])) {
            Array.prototype.forEach.call(form.querySelectorAll('[name="' + k + '"]'), function (c) {
              c.checked = data[k].indexOf(c.value) !== -1;
            });
          } else {
            el.checked = !!data[k];
          }
        } else if (el.type === "radio") {
          var val = data[k];
          Array.prototype.forEach.call(form.querySelectorAll('[name="' + k + '"]'), function (rr) {
            if (rr.value === val) rr.checked = true;
          });
        } else { el.value = data[k]; }
      });
      if (saved) { saved.hidden = false; saved.textContent = "Draft restored"; }
      updateCounts();
    }

    function schedulePersist() {
      if (saveTimer) clearTimeout(saveTimer);
      saveTimer = setTimeout(persist, 350);
    }

    // events
    if (next) next.addEventListener("click", function () {
      if (validatePanel(panels[current])) show(current + 1);
      else if (errorBox) { errorBox.hidden = false; errorBox.textContent = "Please fix the highlighted fields before continuing."; }
    });
    if (back) back.addEventListener("click", function () { show(current - 1); });
    indicators.forEach(function (ind, i) {
      ind.addEventListener("click", function () { if (i < current) show(i); });
    });

    form.addEventListener("input", function (e) {
      if (e.target.tagName === "TEXTAREA") updateCounts();
      schedulePersist();
    });
    form.addEventListener("change", schedulePersist);
    form.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && e.target.tagName !== "TEXTAREA" && current < total - 1) {
        e.preventDefault();
        if (next) next.click();
      }
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var badIndex = -1;
      for (var i = 0; i < total; i++) {
        if (!validatePanel(panels[i])) { badIndex = i; break; }
      }
      if (badIndex > -1) {
        show(badIndex, { scroll: true });
        if (errorBox) { errorBox.hidden = false; errorBox.textContent = "Please fix the highlighted fields before submitting."; }
        var bad = panels[badIndex].querySelector(".is-invalid input, .is-invalid select, .is-invalid textarea");
        if (bad) bad.focus();
        return;
      }
      var data = collect();
      if (submit) submit.disabled = true;
      try { localStorage.removeItem(storeKey); } catch (err) {}
      if (done) {
        form.hidden = true;
        done.hidden = false;
        var nameEl = done.querySelector("[data-apply-name]");
        if (nameEl) nameEl.textContent = data.first || "friend";
        var emailEl = done.querySelector("[data-apply-email]");
        if (emailEl) emailEl.textContent = data.email || "your email";
        var refEl = done.querySelector("[data-apply-ref]");
        if (refEl) refEl.textContent = "AYM-VOL-" + Date.now().toString(36).toUpperCase();
        var top = done.getBoundingClientRect().top + window.pageYOffset - 90;
        window.scrollTo({ top: top, behavior: "smooth" });
      }
    });

    restore();
    updateCounts();
    show(0, { scroll: false });
  });

  // Year in footer
  var y = document.querySelector("[data-year]");
  if (y) { y.textContent = new Date().getFullYear(); }
})();
