   var cta = function () {
    var cards = [
      ["Contribute to our fundraising", "Back youth-led ideas", "donate.html", "Donate Now"],
      ["Start an AYM Chapter Today", "Lead change in your community", "chapter.html", "Start Now"],
      ["Apply as a Volunteer today!", "Share your time and skills", "volunteer.html", "Volunteer Now"],
      ["Contribute by buying goods", "Every purchase supports youth programs", "store.html", "Explore Now"]
    ].map(function (c) {
      return '<article class="cta-card"><h3>' + c[0] + '</h3><p>' + c[1] + '</p><a class="btn btn--brand" href="' + c[2] + '">' + c[3] + '</a></article>';
    }).join("");
    return '' +
'<section class="site-cta">' +
'  <img class="site-cta__bg" src="assets/img/volunteers/aym-community-work.jpg" alt="">' +
'  <div class="container">' +
'    <div class="site-cta__head">' +
'      <h1>Extinguishing Poverty through Innovative Strategies</h1>' +
'      <a class="btn btn--ghost" href="contact.html">Contact Us</a>' +
'    </div>' +
'    <div class="cta-cards">' + cards + '</div>' +
'  </div>' +
'</section>';
  };

  var links = function (items) {
    return '<ul>' + items.map(function (i) {
      return '<li><a href="' + i[1] + '">' + i[0] + '</a></li>';
    }).join("") + '</ul>';
  };

  var footer = function (variant) {
    return (variant === "nocta" ? "" : cta()) +
'<footer class="site-footer">' +
'  <div class="container">' +
'    <div class="footer-main">' +
'      <div class="footer-pitch">' +
'        <span class="footer-pitch__eyebrow">The next move is yours</span>' +
'        <p class="footer-pitch__title">Young People.<br><em>Real Power.</em><br>A Thriving Africa.</p>' +
'        <a class="btn btn--brand" href="volunteer.html">Get Involved</a>' +
'        <div class="social">' +
'          <a href="https://x.com/AYMOVEMENT" aria-label="Twitter">X</a>' +
'          <a href="https://www.facebook.com/africanyouthmovement/" aria-label="Facebook">f</a>' +
'          <a href="https://www.youtube.com/c/Aym-incOrg" aria-label="YouTube">&#9654;</a>' +
'          <a href="https://za.pinterest.com/aymovement/" aria-label="Pinterest">P</a>' +
'          <a href="https://www.linkedin.com/company/twenty-first-century-african-youth-movement/" aria-label="LinkedIn">in</a>' +
'          <a href="https://www.instagram.com/aymovement/" aria-label="Instagram">ig</a>' +
'        </div>' +
'      </div>' +
'      <div class="footer-cols">' +
'        <div><h4>Quick Links</h4>' + links([["About Us","about.html"],["Contact","contact.html"],["Projects","projects.html"],["Events","events.html"],["Take Action","index.html#pathways"]]) + '</div>' +
'        <div><h4>Priorities</h4>' + links([["Art","focus-art.html"],["Agriculture","focus-agriculture.html"],["Education","focus-education.html"],["Entrepreneurship","focus-entrepreneurship.html"],["Ecotourism","focus-ecotourism.html"],["Healthcare","focus-health.html"],["Technology","focus-technology.html"]]) + '</div>' +
'      </div>' +
'    </div>' +
'    <div class="footer-legal">' +
'      <p>&copy; <span data-year>2026</span> Twenty-First Century African Youth Movement (AYM), Inc., USA. All rights reserved.</p>' +
'      <p>AYM is a 501(C)(3) Nonprofit Organization, EIN 39-1742519. Our mission is to Create Jobs and Employment for Youths in Africa!</p>' +
'      <p><a href="https://www.aym-inc.org/privacy-policy/">Privacy Policy</a> | <a href="https://www.aym-inc.org/cookie-policy/">Cookie Policy</a> | <a href="https://www.aym-inc.org/terms-and-conditions/">Terms &amp; Conditions</a></p>' +
'    </div>' +
'  </div>' +
'</footer>';
  };

(function () {
  "use strict";

  var header = function (variant) {
    var overlay = variant === "overlay";
    return '' +
'<header class="site-header' + (overlay ? ' site-header--overlay' : '') + '">' +
'  <div class="container' + (overlay ? ' container--wide' : '') + ' site-header__inner">' +
'    <a class="brand" href="index.html" aria-label="AYM home">' +
'      <img src="assets/img/logo.png" alt="AYM logo">' +
'      <span class="brand__name">AYM<span>African Youth Movement</span></span>' +
'    </a>' +
'    <button class="nav-toggle" aria-label="Menu" aria-expanded="false">&#9776;</button>' +
'    <nav class="nav" aria-label="Primary">' +
'      <div class="has-drop"><a class="navlink" href="volunteer.html">Get Involved</a>' +
'        <div class="dropdown">' +
'          <a href="volunteer.html">Volunteer</a>' +
'          <a href="volunteer-apply.html" class="dropdown__sub">Volunteer Application</a>' +
'          <a href="volunteer-fellowship.html" class="dropdown__sub">AYM Youth Fellowship</a>' +
'          <a href="donate.html#fundraise">Fundraise</a>' +
'          <a href="chapter.html">Start an AYM Chapter</a>' +
'        </div>' +
'      </div>' +
'      <div class="has-drop"><a class="navlink" href="about.html">About</a>' +
'        <div class="dropdown">' +
'          <a href="about.html">About AYM</a>' +
'          <a href="about-team.html">About the Team</a>' +
'          <a href="where-we-work.html">Where We Work</a>' +
'        </div>' +
'      </div>' +
'      <div class="has-drop"><a class="navlink" href="focus-art.html">Focus Areas</a>' +
'        <div class="dropdown">' +
'          <a href="focus-art.html">Art</a>' +
'          <a href="focus-agriculture.html">Agriculture</a>' +
'          <a href="focus-education.html">Education</a>' +
'          <a href="focus-entrepreneurship.html">Entrepreneurship</a>' +
'          <a href="focus-ecotourism.html">Ecotourism</a>' +
'          <a href="focus-ecotourism-forest-safari.html" class="dropdown__sub">Forest Safari</a>' +
'          <a href="focus-health.html">Healthcare</a>' +
'          <a href="focus-technology.html">Technology</a>' +
'        </div>' +
'      </div>' +
'      <div class="has-drop"><a class="navlink" href="projects.html">Our Work</a>' +
'        <div class="dropdown">' +
'          <a href="projects.html">Projects</a>' +
'          <a href="events.html">Events</a>' +
'          <a href="where-we-work.html">Where We Work</a>' +
'        </div>' +
'      </div>' +
'      <a class="navlink" href="blog.html">Blog</a>' +
'      <a class="navlink" href="contact.html">Contact</a>' +
'      <a class="btn ' + (overlay ? 'btn--brand' : 'btn--accent') + ' header__cta" href="donate.html">Donate Now</a>' +
'    </nav>' +
'  </div>' +
'</header>';
  };

var parts = { header: header, cta: cta, footer: footer };

    document.querySelectorAll("[data-component]").forEach(function (slot) {
    var build = parts[slot.getAttribute("data-component")];
    if (build) slot.outerHTML = build(slot.getAttribute("data-variant"));
  });

  var siteHeader = document.querySelector(".site-header--overlay");
  if (siteHeader) {
    var hero = document.querySelector(".hero");
    var onScroll = function () {
      var limit = hero ? hero.offsetHeight - siteHeader.offsetHeight : 50;
      siteHeader.classList.toggle("is-scrolled", window.scrollY > limit);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }
})();