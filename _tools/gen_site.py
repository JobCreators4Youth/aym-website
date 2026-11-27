# -*- coding: utf-8 -*-
"""Builds the AYM static website (redesign matching the Figma file)."""
import os

OUT = os.environ.get("AYM_SITE_DIR") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(OUT, exist_ok=True)

# ------------------------------------------------------------------ helpers
def write(name, html):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name)

def head(title, desc, active=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Twenty-First Century African Youth Movement (AYM)</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
<link rel="icon" type="image/png" href="assets/img/logo.png">
</head>
<body>
<a class="skip" href="#main" style="position:absolute;left:-999px">Skip to content</a>
<header class="site-header">
  <div class="container site-header__inner">
    <a class="brand" href="index.html" aria-label="AYM home">
      <img src="assets/img/logo.png" alt="AYM logo">
      <span class="brand__name">AYM<span>African Youth Movement</span></span>
    </a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false">&#9776;</button>
    <nav class="nav" aria-label="Primary">
      <a class="navlink" href="index.html">Home</a>
      <div class="has-drop"><a class="navlink" href="about.html">About</a>
        <div class="dropdown">
          <a href="about.html">About AYM</a>
          <a href="about.html#mission">Mission</a>
          <a href="about.html#history">History</a>
          <a href="about-team.html">About the Team</a>
        </div>
      </div>
      <div class="has-drop"><a class="navlink" href="blog.html">Voices &amp; Stories</a>
        <div class="dropdown">
          <a href="blog.html">Stories</a>
          <a href="events.html">Events &amp; Replays</a>
          <a href="https://www.youtube.com/channel/UCU1VXmeMoxZuPC2lvL8-RIw/videos" target="_blank" rel="noopener noreferrer">Videos ↗</a>
        </div>
      </div>
      <div class="has-drop"><a class="navlink" href="opportunity-sectors.html">Sectors</a>
        <div class="dropdown">
          <a href="opportunity-sectors.html">All Sectors</a>
          <a href="focus-art.html">Creative Economy</a>
          <a href="focus-agriculture.html">Agriculture &amp; Food Systems</a>
          <a href="focus-education.html">Learning &amp; Future Careers</a>
          <a href="focus-entrepreneurship.html">Enterprise &amp; Youth Employment</a>
          <a href="focus-ecotourism.html">Heritage &amp; Sustainability</a>
          <a href="focus-ecotourism-forest-safari.html" class="dropdown__sub">Forest Safari</a>
          <a href="focus-health.html">Health &amp; Wellbeing</a>
          <a href="focus-technology.html">Technology &amp; Digital Inclusion</a>
        </div>
      </div>
      <div class="has-drop"><a class="navlink" href="projects.html">Impact</a>
        <div class="dropdown">
          <a href="projects.html">Projects</a>
          <a href="events.html">Events</a>
          <a href="where-we-work.html">Where We Work</a>
        </div>
      </div>
      <div class="has-drop"><a class="navlink" href="volunteer.html">Get Involved</a>
        <div class="dropdown">
          <a href="share-your-story.html">Share Your Story</a>
          <a href="volunteer.html">Volunteer</a>
          <a href="volunteer-apply.html" class="dropdown__sub">Volunteer Application</a>
          <a href="volunteer-fellowship.html" class="dropdown__sub">AYM Youth Fellowship</a>
          <a href="chapter.html">Build a Team</a>
          <a href="donate.html#fundraise">Support the Mission</a>
        </div>
      </div>
      <div class="has-drop"><a class="navlink" href="chapter.html">Chapters</a>
        <div class="dropdown">
          <a href="chapter.html">Start an AYM Chapter</a>
          <a href="where-we-work.html">Where We Work</a>
          <a href="contact.html">Partner With Us</a>
        </div>
      </div>
      <a class="btn btn--accent header__cta" href="donate.html">Donate</a>
    </nav>
  </div>
</header>
<main id="main">
"""

FOOTER = """
</main>
<footer class="site-footer">
  <div class="footer__cta">
    <div class="container">
      <h3>Join us in our mission</h3>
      <div class="flex">
        <a class="btn btn--brand" href="donate.html">Donate</a>
        <a class="btn btn--ghost" href="volunteer.html">Volunteer</a>
        <a class="btn btn--ghost" href="store.html">Shop</a>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="footer__grid">
      <div class="footer__brand">
        <img src="assets/img/logo.png" alt="AYM logo">
        <p class="small" style="margin-top:1rem">Twenty-First Century African Youth Movement (AYM) amplifies African youth voices, develops skills, and creates opportunities.</p>
        <p class="small">P.O.Box 90152<br>
        Alexandria, VA 22309<br>
        USA</p>
        <div class="social">
          <a href="https://x.com/AYMOVEMENT" aria-label="Twitter">X</a>
          <a href="https://www.facebook.com/africanyouthmovement/" aria-label="Facebook">f</a>
          <a href="https://www.youtube.com/c/Aym-incOrg" aria-label="YouTube">&#9654;</a>
          <a href="https://www.linkedin.com/company/twenty-first-century-african-youth-movement/" aria-label="LinkedIn">in</a>
          <a href="https://www.instagram.com/aymovement/" aria-label="Instagram">ig</a>
        </div>
      </div>
      <div>
        <h4>Where We Work</h4>
        <ul>
          <li><a href="where-we-work.html">Africa</a></li>
          <li><a href="where-we-work.html">Sierra Leone</a></li>
          <li><a href="where-we-work.html">United Kingdom</a></li>
          <li><a href="where-we-work.html">USA</a></li>
        </ul>
      </div>
      <div>
        <h4>About Us</h4>
        <ul>
          <li><a href="about.html">About AYM</a></li>
          <li><a href="about.html#mission">Mission</a></li>
          <li><a href="about.html#history">History</a></li>
          <li><a href="about-team.html">Leadership</a></li>
        </ul>
      </div>
      <div>
        <h4>Focus Areas</h4>
        <ul>
          <li><a href="opportunity-sectors.html">Opportunity Sectors</a></li>
          <li><a href="focus-art.html">Art</a></li>
          <li><a href="focus-agriculture.html">Agriculture</a></li>
          <li><a href="focus-education.html">Education</a></li>
          <li><a href="focus-entrepreneurship.html">Entrepreneurship</a></li>
          <li><a href="focus-ecotourism.html">Ecotourism</a></li>
          <li><a href="focus-health.html">Healthcare</a></li>
          <li><a href="focus-technology.html">Technology</a></li>
        </ul>
      </div>
      <div>
        <h4>Quick Links</h4>
        <ul>
          <li><a href="share-your-story.html">Share Your Story</a></li>
          <li><a href="about.html">About Us</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="projects.html">Our Work</a></li>
          <li><a href="volunteer.html">Get Involved</a></li>
          <li><a href="store.html">Impact Store</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>&copy; <span data-year>2026</span> Twenty-First Century African Youth Movement (AYM), Inc., USA. All rights reserved.</span>
      <span>AYM is a 501(C)(3) Nonprofit Organization, EIN 39-1742519.</span>
      <span class="footer__policies"><a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a> · <a href="accessibility.html">Accessibility</a></span>
    </div>
  </div>
</footer>
<script src="assets/js/main.js?v=20261111-web3forms"></script>
<script src="assets/js/chat.js" defer></script>
</body>
</html>
"""

def clean_html(html):
    return "\n".join(line.rstrip() for line in html.splitlines()) + "\n"

def page(name, title, desc, body, active=""):
    write(name, clean_html(head(title, desc, active) + body + FOOTER))

def hero_page(eyebrow, title, sub, image, crumb, actions="", extra="", cls="", post=""):
    return f"""
<section class="hero hero--page{cls}">
  <img class="hero__bg" src="{image}" alt="">
  <div class="container hero__inner">
    <div class="breadcrumb"><a href="index.html">Home</a> / {crumb}</div>
    <span class="eyebrow eyebrow--brand" style="color:var(--brand)">{eyebrow}</span>
    <h1 class="hero__title">{title}</h1>
    <p class="hero__sub">{sub}</p>
    {f'<div class="hero__actions">{actions}</div>' if actions else ''}
    {extra}
  </div>
  {post}
</section>
"""

CONTACT_CTA = """
<section class="section section--cream">
  <div class="container center">
    <h2>Still have questions?</h2>
    <p class="lead">Can't find the answer you're looking for? Please chat to our friendly team.</p>
    <p><a class="btn btn--accent" href="contact.html">Contact Us</a></p>
  </div>
</section>
"""

def cta_trio():
    return """
<section class="section">
  <div class="container">
    <div class="grid grid-3">
      <div class="card card--flat">
        <div class="card__body">
          <h3 class="card__title">Want to join us and connect with individuals globally together?</h3>
          <p class="card__text">Lend your skills to empower local communities and shape sustainable youth-led futures.</p>
          <a class="card__link" href="volunteer.html">Become a Volunteer →</a>
        </div>
      </div>
      <div class="card card--flat">
        <div class="card__body">
          <h3 class="card__title">Want to become a part of our AYM chapters?</h3>
          <p class="card__text">Bring the movement to your city or country and lead grassroots change.</p>
          <a class="card__link" href="chapter.html">Start an AYM Chapter →</a>
        </div>
      </div>
      <div class="card card--flat">
        <div class="card__body">
          <h3 class="card__title">Want to explore our extensive array of products?</h3>
          <p class="card__text">Each purchase gives purpose and supports youth-led programs.</p>
          <a class="card__link" href="store.html">Explore Store →</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""

def faq(items):
    rows = "".join(
        f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items
    )
    return f"""
<section class="section">
  <div class="container">
    <div class="section__head center">
      <span class="eyebrow">FAQs</span>
      <h2>Frequently asked questions</h2>
    </div>
    <div class="faq">{rows}</div>
  </div>
</section>
"""

def statrow(cells):
    inner = "".join(f'<div class="statcell"><strong>{a}</strong><span>{b}</span></div>' for a, b in cells)
    return f'<div class="statrow">{inner}</div>'

def cards_grid(cards, cols=3):
    out = []
    for c in cards:
        img = f'<img class="card__img" src="{c["img"]}" alt="">' if c.get("img") else ""
        tag = f'<div class="card__tag">{c["tag"]}</div>' if c.get("tag") else ""
        link = f'<a class="card__link" href="{c["href"]}">{c["cta"]} →</a>' if c.get("cta") else ""
        out.append(f"""<article class="card">{img}<div class="card__body">{tag}
          <h3 class="card__title">{c['title']}</h3>
          <p class="card__text">{c['text']}</p>{link}</div></article>""")
    return f'<div class="grid grid-{cols}">' + "".join(out) + "</div>"

# ==========================================================================
# PAGE: LANDING
# ==========================================================================
FOCUS = {
  "art": ("Creative Economy &amp; Culture",
     "Promote African creativity, cultural identity, and creative enterprises.",
    "focus-art.html"),
  "agriculture": ("Agriculture &amp; Food Systems",
    "Advance food security, agribusiness, and rural employment.",
    "focus-agriculture.html"),
  "education": ("Education &amp; Skills",
    "Expand access to learning, professional development, and career opportunities.",
    "focus-education.html"),
  "entrepreneurship": ("Entrepreneurship &amp; Employment",
    "Support youth-led enterprises, innovation, and job creation.",
    "focus-entrepreneurship.html"),
  "ecotourism": ("Tourism, Heritage &amp; Environment",
    "Promote cultural heritage, sustainable tourism, and environmental responsibility.",
    "focus-ecotourism.html"),
  "health": ("Health &amp; Community Wellbeing",
    "Promote health education, awareness, and community resilience.",
    "focus-health.html"),
  "technology": ("Technology &amp; Digital Innovation",
    "Advance digital literacy, artificial intelligence, and technology-driven solutions.",
    "focus-technology.html"),
}
FOCUS_ORDER = [("Creative Economy &amp; Culture","art"),("Agriculture &amp; Food Systems","agriculture"),
  ("Education &amp; Skills","education"),("Entrepreneurship &amp; Employment","entrepreneurship"),
  ("Tourism, Heritage &amp; Environment","ecotourism"),("Health &amp; Community Wellbeing","health"),
  ("Technology &amp; Digital Innovation","technology")]

chips = "".join(
    f'<button class="chip{" is-active" if k=="art" else ""}" data-focus="{k}">{lbl}</button>'
    for lbl, k in FOCUS_ORDER)
panels = "".join(
    f'<div data-focus-panel="{k}"{" hidden" if k!="art" else ""}><h3 class="mt-1">{v[0]}</h3>'
    f'<p class="lead">{v[1]}</p><a class="btn btn--outline" href="{v[2]}">Check {lbl} →</a></div>'
    for lbl, k in FOCUS_ORDER for v in [FOCUS[k]])

SECTOR_CARDS = [
  {"title": "Creative Economy &amp; Culture", "text": "Promote African creativity, cultural identity, and creative enterprises.", "cta": "Explore sector", "href": "focus-art.html"},
  {"title": "Agriculture &amp; Food Systems", "text": "Advance food security, agribusiness, and rural employment.", "cta": "Explore sector", "href": "focus-agriculture.html"},
  {"title": "Education &amp; Skills", "text": "Expand access to learning, professional development, and career opportunities.", "cta": "Explore sector", "href": "focus-education.html"},
  {"title": "Entrepreneurship &amp; Employment", "text": "Support youth-led enterprises, innovation, and job creation.", "cta": "Explore sector", "href": "focus-entrepreneurship.html"},
  {"title": "Tourism, Heritage &amp; Environment", "text": "Promote cultural heritage, sustainable tourism, and environmental responsibility.", "cta": "Explore sector", "href": "focus-ecotourism.html"},
  {"title": "Health &amp; Community Wellbeing", "text": "Promote health education, awareness, and community resilience.", "cta": "Explore sector", "href": "focus-health.html"},
  {"title": "Technology &amp; Digital Innovation", "text": "Advance digital literacy, artificial intelligence, and technology-driven solutions.", "cta": "Explore sector", "href": "focus-technology.html"},
]
SECTOR_HUB = hero_page(
  "Opportunity Sectors",
  "Explore Africa’s Opportunity Sectors.",
  "Its seven original priorities serve as Opportunity Sectors that support this mission. Each sector follows the same five-part path: the challenge, African voices, opportunities and solutions, projects and evidence, and ways to get involved.",
  "assets/img/landing-page01-1.png", "Opportunity Sectors",
  actions='<a class="btn btn--accent" href="blog.html">Explore Stories</a>'
          '<a class="btn btn--ghost" href="volunteer.html">Join the Movement</a>'
) + f"""
<section class="section">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Seven areas of opportunity</span><h2>Voices, evidence, opportunities and action</h2></div>
    {cards_grid(SECTOR_CARDS, 3)}
  </div>
</section>
""" + CONTACT_CTA
page("opportunity-sectors.html", "Opportunity Sectors", "Explore the seven Opportunity Sectors covered by VOTE Africa and AYM.", SECTOR_HUB, "focus")

print("opportunity sectors done")

CURRENT_PROJECTS = [
  {"title":"Building Artistic Bridges Through Perception","tag":"Ongoing · Africa / Art","text":"Connecting artists and audiences across continents to reshape global perceptions of Africa.","cta":"Learn More","href":"focus-art.html","img":"assets/img/projects-2.png"},
  {"title":"Mattru Jong Project Pioneer Summit","tag":"In planning · Ecotourism","text":"A community-led summit connecting local knowledge, enterprise ideas and ecotourism in Mattru Jong.","cta":"Learn More","href":"focus-ecotourism.html"},
]

HOME_PROJECTS = [
  {"title":"Building Artistic Bridges Through Perception","tag":"Africa / Art","text":"Connecting artists and audiences across continents to reshape global perceptions of Africa.","cta":"Learn More","href":"focus-art.html","img":"assets/img/projects-2.png"},
  {"title":"Mattru Jong Project Summit","tag":"Ecotourism","text":"Developing 100+ acres along the Jong River into an ecotourism and enterprise hub.","cta":"Watch Videos","href":"focus-ecotourism.html"},
  {"title":"Brick Making","tag":"Art","text":"A youth-led brick-making enterprise producing building materials and practical learning locally.","cta":"Learn More","href":"focus-entrepreneurship.html","img":"assets/img/projects-3.png"},
]

HERO_QUICK_NAV = """
  <nav class="hero-quick-nav" aria-label="Homepage quick links">
    <a class="hero-quick-nav__item" href="donate.html">
      <span class="hero-quick-nav__bullet" aria-hidden="true"></span>
      <span class="hero-quick-nav__copy"><span class="hero-quick-nav__title">Donate Now</span><span class="hero-quick-nav__desc">Back youth-led ideas</span></span>
      <span class="hero-quick-nav__arrow" aria-hidden="true">↗</span>
    </a>
    <a class="hero-quick-nav__item" href="volunteer-apply.html">
      <span class="hero-quick-nav__bullet" aria-hidden="true"></span>
      <span class="hero-quick-nav__copy"><span class="hero-quick-nav__title">Apply as a Volunteer</span><span class="hero-quick-nav__desc">Share time and skills</span></span>
      <span class="hero-quick-nav__arrow" aria-hidden="true">↗</span>
    </a>
    <a class="hero-quick-nav__item" href="chapter.html">
      <span class="hero-quick-nav__bullet" aria-hidden="true"></span>
      <span class="hero-quick-nav__copy"><span class="hero-quick-nav__title">Start a Chapter</span><span class="hero-quick-nav__desc">Lead in your community</span></span>
      <span class="hero-quick-nav__arrow" aria-hidden="true">↗</span>
    </a>
    <a class="hero-quick-nav__item" href="store.html">
      <span class="hero-quick-nav__bullet" aria-hidden="true"></span>
      <span class="hero-quick-nav__copy"><span class="hero-quick-nav__title">Impact Shop</span><span class="hero-quick-nav__desc">Wear the movement</span></span>
      <span class="hero-quick-nav__arrow" aria-hidden="true">↗</span>
    </a>
  </nav>
"""

LANDING = hero_page(
  "VOTE Africa",
  "Africa Speaks. The World Listens.",
  "Voices of the Emerging Africa is a global media and engagement initiative of the Twenty-First Century African Youth Movement, Inc. (AYM), a U.S.-registered nonprofit organization.",
  "assets/img/landing-page01-3.png", "Home",
  actions='<a class="btn btn--accent btn--lg" href="blog.html">Watch Our Stories</a>'
          '<a class="btn btn--ghost btn--lg" href="share-your-story.html">Share Your Voice</a>'
          '<a class="btn btn--ghost btn--lg" href="volunteer.html">Join the Movement</a>',
  cls=" hero--home-nav",
  post=HERO_QUICK_NAV,
) + f"""
<section class="section">
  <div class="container">
    <div class="section__head center">
      <span class="eyebrow">Our Objectives</span>
      <h2>Change-makers rebuilding rural communities</h2>
      <p class="lead">AYM engages youth as change-makers in rebuilding and developing rural communities through innovative and progressive local-driven programs and enterprises. AYM facilitates increased access to critical resources and opportunities for rural youth.</p>
    </div>
    <div class="grid grid-4">
      <div class="feature"><div class="feature__ico">1</div><h3>Extinguish rural poverty</h3><p class="muted">Help people acquire the right skills that will help them improve their livelihood.</p></div>
      <div class="feature"><div class="feature__ico">2</div><h3>Skill Development</h3><p class="muted">Provide youth with job training to acquire employable skills valuable for their future.</p></div>
      <div class="feature"><div class="feature__ico">3</div><h3>Youth Empowerment</h3><p class="muted">Shrink the share of youth most at risk of being left behind in the labor market.</p></div>
      <div class="feature"><div class="feature__ico">4</div><h3>African Intervention</h3><p class="muted">Promote youth self-employment in Sierra Leone as a model for our African intervention.</p></div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="section__head center">
      <span class="eyebrow" style="color:var(--brand)">Where we are stationed</span>
      <h2>Mobilize local youth around pressing regional issues</h2>
      <p class="lead" style="color:rgba(255,255,255,.85)">From environmental sustainability to tech education and policy advocacy.</p>
    </div>
    <div class="grid grid-2">
      <div class="card"><div class="card__body">
        <div class="card__tag">Sierra Leone</div>
        <h3 class="card__title">Contribute to our fundraising</h3>
        <p class="card__text">Mobilize local youth around pressing regional issues—from environmental sustainability to tech education and policy advocacy.</p>
        <a class="card__link" href="donate.html">Donate Now →</a></div></div>
      <div class="card"><div class="card__body">
        <div class="card__tag">United States</div>
        <h3 class="card__title">Apply as a Volunteer</h3>
        <p class="card__text">Propose local campaigns for approval. Any fundraising or institutional funding activity must follow AYM's governance, authorization and written terms.</p>
        <a class="card__link" href="volunteer.html">Apply as a Volunteer →</a></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Current projects</span><h2>What we're working on right now</h2><p class="lead">Where your support goes today &mdash; live projects across art, ecotourism and youth enterprise.</p></div>
    {cards_grid(HOME_PROJECTS, 3)}
    <div class="center mt-3"><a class="btn btn--outline" href="projects.html">View All Projects →</a></div>
  </div>
</section>

<section class="section section--dark">
  <div class="container center">
    <span class="eyebrow" style="color:var(--brand)">Results</span>
    <h2>What our work has achieved so far</h2>
    <div class="stats stats--dark" style="justify-content:center">
      <div class="stat"><div class="stat__num">5000+</div><div class="stat__label">Lives Changed</div></div>
      <div class="stat"><div class="stat__num">50+</div><div class="stat__label">Enterprises Created</div></div>
      <div class="stat"><div class="stat__num">$100K</div><div class="stat__label">Funds Raised</div></div>
      <div class="stat"><div class="stat__num">10K+</div><div class="stat__label">Members Worldwide</div></div>
    </div>
    <p class="small" style="color:rgba(255,255,255,.7)">Figures pending final verification with AYM's finance team.</p>
  </div>
</section>
""" + cta_trio() + f"""
<section class="section section--cream">
  <div class="container">
    <div class="section__head">
      <span class="eyebrow">Opportunity Sectors</span>
      <h2>Explore Africa’s Opportunity Sectors.</h2>
      <p class="lead">AYM revitalizes youth potentials in rural communities for social and political stability through education, technology, agribusiness, eco-tourism, entrepreneurship, and the creative arts.</p>
    </div>
    <div class="chips mb-2">{chips}</div>
    <div class="focus-panels">{panels}</div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">Our Approach</span>
      <h2>Extinguishing Poverty through Innovative Strategies</h2>
      <p class="lead">Twenty-First Century African Youth Movement works with rural youth through technology programs that build practical skills for work, enterprise and community leadership.</p>
      <div class="grid grid-2 mt-2">
        <div><h3>Start a Chapter at AYM</h3><p class="muted">Move from volunteering to proposing community-led enterprise ideas. Any hiring, revenue activity or funding requires approved plans and governance.</p><a class="btn--link" href="chapter.html">Start a Chapter →</a></div>
        <div><h3>Contribute by buying goods</h3><p class="muted">Host local events, participate in the African Lecture Series, and collaborate on continent-wide initiatives with leaders across Africa.</p><a class="btn--link" href="store.html">View Store →</a></div>
      </div>
    </div>
    <div class="split__media"><img src="assets/img/landing-page01-1.png" alt="AYM youth at work"></div>
  </div>
</section>

<section class="section section--cream">
  <div class="container center">
    <span class="eyebrow">Our Sponsors</span>
    <h2>Partners who make our work possible</h2>
    <div class="logos mt-2">
      <div class="logo-ph">Google</div>
      <div class="logo-ph">Wisconsin Humanities</div>
      <div class="logo-ph">Dane Arts</div>
      <div class="logo-ph">DreamHost</div>
      <div class="logo-ph">Madwraps</div>
      <div class="logo-ph">Wisconsin Union</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Blog</span><h2>The latest from our blog</h2></div>
    <div class="grid grid-3">
      <article class="card"><div class="card__body"><div class="card__tag">News</div><h3 class="card__title"><a href="https://www.aym-inc.org/the-sierra-leone-paramount-chief-who-bridged-worlds/">The Sierra Leone Paramount Chief Who Bridged Worlds</a></h3><p class="card__text">Paramount Chief Alhaji Alie Badara Sheriff III died on January...</p><div class="meta mt-1"><span>Abu-Hassan Koroma</span><span>Feb 12, 2026</span></div></div></article>
      <article class="card"><div class="card__body"><div class="card__tag">Programs</div><h3 class="card__title"><a href="https://www.aym-inc.org/rwandan-youth-in-african-youth-movement/">Rwandan Youth in African Youth Movement</a></h3><p class="card__text">The African Youth Movement (AYM) trains Rwandan youth in leadership...</p><div class="meta mt-1"><span>Abu-Hassan Koroma</span><span>Apr 4, 2025</span></div></div></article>
      <article class="card"><div class="card__body"><div class="card__tag">Stories</div><h3 class="card__title"><a href="https://www.aym-inc.org/empowering-african-youth-through-web-design/">Empowering African Youth Through Web Design</a></h3><p class="card__text">The journey of a volunteer using digital skills to empower African youth...</p><div class="meta mt-1"><span>Abu-Hassan Koroma</span><span>Dec 22, 2024</span></div></div></article>
    </div>
    <div class="center mt-3"><a class="btn btn--outline" href="https://www.aym-inc.org/aym-blog/" target="_blank" rel="noopener">View All Posts →</a></div>
  </div>
</section>
""" + CONTACT_CTA

page("index.html", "Young People. Real Power. A Thriving Africa.", "AYM works with young people to build skills, create enterprises, and strengthen communities.", LANDING, "home")

print("landing done")

# ==========================================================================
# PAGE: ABOUT
# ==========================================================================
ABOUT = hero_page(
  "About AYM",
  "A Movement Led by the Youth",
  "Mobilizing Africa's unemployed and underemployed youth as active drivers of economic growth, stability, and lasting social change.",
  "assets/img/about-1.png", "About",
  actions='<a class="btn btn--accent" href="donate.html">Donate Now</a>'
          '<a class="btn btn--ghost" href="about-team.html">Meet the Team</a>'
) + statrow([("2000", "Founded"), ("Youth-led", "Program design"), ("Sierra Leone", "Operational base"), ("Local", "Community roots")]) + f"""
<section class="section" id="vision">
  <div class="container grid grid-2">
    <div>
      <span class="eyebrow">VISION</span>
      <h2>An Africa where every young person has the voice, knowledge, skills, and economic opportunities to shape their future and contribute to the sustainable development of their community and continent.</h2>
    </div>
    <div class="split__media"><img src="assets/img/about-2.png" alt="AYM community"></div>
  </div>
</section>

<section class="section section--cream" id="mission">
  <div class="container">
    <div class="section__head center">
      <span class="eyebrow">MISSION</span>
      <p class="lead">To empower African youth through digital media, education, entrepreneurship, civic engagement, and global collaboration by amplifying their voices, developing their skills, connecting them to opportunities, and transforming their ideas into sustainable economic and social impact.</p>
    </div>
  </div>
</section>

<section class="section" id="delivery">
  <div class="container">
    <div class="section__head">
      <span class="eyebrow">Mission delivery</span>
      <h2>How AYM Will Deliver Its Mission</h2>
      <p class="lead">Through Voices of the Emerging Africa (VOE Africa), AYM will use digital storytelling, media production, research, education, global partnerships, and volunteer engagement to advance its mission.</p>
      <p class="lead">Its seven original priorities will serve as Opportunity Sectors that support this mission:</p>
    </div>
    {cards_grid(SECTOR_CARDS, 3)}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head"><span class="eyebrow">What we do</span><h2>What we do to take action</h2></div>
    <div class="grid grid-4">
      <div class="feature"><div class="feature__ico">&#9733;</div><h3>Skills and Enterprise</h3><p class="muted">We support skill-building workshops and supervised project experience connected to approved mission activities.</p></div>
      <div class="feature"><div class="feature__ico">&#9733;</div><h3>Youth Training</h3><p class="muted">We offer courses and mentorships in various sectors, including technology, entrepreneurship, agribusiness, and creative arts.</p></div>
      <div class="feature"><div class="feature__ico">&#9733;</div><h3>Community Projects</h3><p class="muted">Our initiatives connect youth with real-world projects that promote development and social impact.</p></div>
      <div class="feature"><div class="feature__ico">&#9733;</div><h3>Strategic Partnerships</h3><p class="muted">We collaborate with NGOs, educational institutions, and private sector partners to expand opportunities for youth.</p></div>
    </div>
  </div>
</section>

<section class="section section--cream" id="vote-africa">
  <div class="container split">
    <div>
      <span class="eyebrow">VOTE Africa</span>
      <h2>Voices of the Emerging Africa</h2>
      <p class="lead">VOTE Africa is a global media and engagement initiative of the Twenty-First Century African Youth Movement, Inc. (AYM), a U.S.-registered nonprofit organization. It shares African voices, perspectives and practical information about opportunity sectors across the continent.</p>
      <p class="muted">VOTE Africa is not a separate nonprofit, political party, fundraising vehicle or employer. Stories are published for learning and dialogue. Programs, grants and enterprise activity take place only under approved AYM governance and written authorization.</p>
      <p class="mt-2"><a class="btn btn--outline" href="opportunity-sectors.html">Explore Opportunity Sectors →</a></p>
    </div>
    <div class="split__media"><img src="assets/img/landing-page01-3.png" alt="VOTE Africa"></div>
  </div>
</section>

<section class="section section--dark" id="history">
  <div class="container split">
    <div>
      <span class="eyebrow" style="color:var(--brand)">Our Story</span>
      <h2>The History and Story of AYM</h2>
      <p class="lead" style="color:rgba(255,255,255,.85)">Abu-Hassan Koroma migrated to the United States in 1991, immediately after the start of the Sierra Leone Civil War. The war (1991–2002) left an estimated 60% of young people economically and socially abandoned. At the end of the war, training alone was not enough—creating long-term alternatives for self-reliance required a broader coalition and practical pathways to work and enterprise.</p>
      <div class="tabs mt-2" data-tabs>
        <div class="tabs__nav">
          <button class="chip is-active" data-tab="roots">Roots</button>
          <button class="chip" data-tab="founding">Founding</button>
          <button class="chip" data-tab="impact">Impact</button>
          <button class="chip" data-tab="expansion">Expansion</button>
        </div>
        <div class="tabs__panel" data-tab-panel="roots"><p>Born out of the tragedy of a decade-long civil war that displaced and abandoned an entire generation of youth.</p></div>
        <div class="tabs__panel" data-tab-panel="founding" hidden><p>Founded in 2000 in Wisconsin, US to give rural Sierra Leonean youth a path to self-reliance.</p></div>
        <div class="tabs__panel" data-tab-panel="impact" hidden><p>From 7 staff to a growing team, AYM created enterprises, trained youth, and built the Mattru Jong project.</p></div>
        <div class="tabs__panel" data-tab-panel="expansion" hidden><p>A growing Pan-African network of chapters across West, East, and Southern Africa.</p></div>
      </div>
      <p class="mt-2"><a class="btn btn--brand" href="about-team.html">Learn More →</a></p>
    </div>
    <div class="split__media"><img src="assets/img/about-0.png" alt="AYM history"></div>
  </div>
</section>
""" + cta_trio() + CONTACT_CTA

page("about.html", "About AYM", "Our vision, mission, solution and the history of the Twenty-First Century African Youth Movement.", ABOUT, "about")

# ==========================================================================
# PAGE: ABOUT-TEAM (founder / leadership)
# ==========================================================================
TEAM = hero_page(
  "Our Team",
  "Inspired by History. <em>Led by Youth.</em>",
  "Rooted in the visionary governance of African history, driven today by young leaders transforming communities across the continent.",
  "assets/img/about2-1.png", "About / Team"
) + f"""
<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">Our Founder</span>
      <h2>The Legacy of Askia the Great</h2>
      <p class="lead">Abu-Hassan Koroma named the Twenty-First Century African Youth Movement after Askia the Great (Askia Mohammad I), the 15th-century ruler of the Songhai Empire whose reign brought education, trade, and prosperity across West Africa.</p>
      <p class="muted">Askia the Great expanded the empire's territory and organized its administration into provinces headed by governors. He standardized trade, weights and measures, and established a system of central taxation. He was a devout Muslim and a patron of education, opening schools and encouraging learning; the University of Sankore at Timbuktu flourished under his reign, becoming a center of scholarship.</p>
      <p class="muted">By drawing on this legacy, AYM treats African youth as active leaders today—capable of driving immediate social and economic progress.</p>
      <div class="pullquote">"AYM is a movement to harness the energy, creativity, and determination of African youth, treating them as active leaders today who can drive immediate social and economic progress."</div>
    </div>
    <div class="split__media"><img src="assets/img/about2-0.png" alt="Abu-Hassan Koroma, Founder"></div>
  </div>
</section>

<section class="section section--cream">
  <div class="container center"><span class="eyebrow">Get Involved</span><h2>Feel like getting into the whole process?</h2><p class="mt-2"><a class="btn btn--brand" href="volunteer.html">Get Involved →</a></p></div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Leadership</span><h2>Meet the rest of the team behind everything</h2></div>
    <div class="grid grid-4">
      <div class="person"><div class="person__avatar">AK</div><h3>Abu-Hassan Koroma</h3><span class="person__role">Founder &amp; CEO</span></div>
      <div class="person"><div class="person__avatar">DG</div><h3>Dennis Charles Glover</h3><span class="person__role">Executive Senior Vice President &amp; COO</span></div>
      <div class="person"><div class="person__avatar">CF</div><h3>Chief Financial Officer</h3><span class="person__role">Finance</span></div>
      <div class="person"><div class="person__avatar">PH</div><h3>Philanthropy Lead</h3><span class="person__role">Development</span></div>
      <div class="person"><div class="person__avatar">ED</div><h3>Executive Director</h3><span class="person__role">Programs</span></div>
      <div class="person"><div class="person__avatar">BM</div><h3>Board Member</h3><span class="person__role">Governance</span></div>
      <div class="person"><div class="person__avatar">SL</div><h3>Sierra Leone Team</h3><span class="person__role">Local Operations</span></div>
      <div class="person"><div class="person__avatar">+</div><h3>Join the team</h3><span class="person__role"><a href="volunteer.html">Volunteer with us →</a></span></div>
    </div>
  </div>
</section>
""" + CONTACT_CTA

page("about-team.html", "About the Team", "Meet the founder and leadership behind the Twenty-First Century African Youth Movement.", TEAM, "about")

# ==========================================================================
# PAGE: CONTACT
# ==========================================================================
CONTACT = hero_page(
  "Contact",
  "Get In Touch",
  "Our friendly team would love to hear from you.",
  "assets/img/contact-2.png", "Contact"
) + f"""
<section class="section">
  <div class="container grid grid-2">
    <div>
      <h2>Send us a message</h2>
      <form class="form" action="https://api.web3forms.com/submit" method="POST" data-web3forms>
        <input type="hidden" name="access_key" value="1afd7c99-a77e-4aab-9fac-111a25871653">
        <input type="hidden" name="from_name" value="AYM Website">
        <input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off" style="display:none" aria-hidden="true">
        <div class="grid grid-2">
          <label>First name<input type="text" name="first" placeholder="First name" required></label>
          <label>Last name<input type="text" name="last" placeholder="Last name" required></label>
        </div>
        <label>Email<input type="email" name="email" placeholder="you@company.com" required></label>
        <label>Subject<input type="text" name="subject" placeholder="How can we help?"></label>
        <label>Message<textarea name="message" rows="5" placeholder="Leave us a message..." required></textarea></label>
        <label class="checkbox"><input type="checkbox" required> You agree to our friendly privacy policy.</label>
        <button class="btn btn--accent" type="submit">Send Form</button>
        <p class="form__note" data-form-note role="status" aria-live="polite" hidden></p>
      </form>
    </div>
    <div>
      <h2>Contact information</h2>
      <div class="info">
        <div><strong>Contact us</strong><p class="muted">Use the form on this page, the WhatsApp button, or AYM Assistant.</p></div>
        <div><strong>Office</strong><p class="muted">P.O.Box 90152<br>Alexandria, VA 22309<br>USA</p></div>
      </div>
      <div class="split__media mt-2"><img src="assets/img/contact-1.png" alt="Contact AYM"></div>
    </div>
  </div>
</section>
"""
page("contact.html", "Contact", "Get in touch with the Twenty-First Century African Youth Movement.", CONTACT, "contact")

print("about/team/contact done")

# ==========================================================================
# PAGE: VOLUNTEER
# ==========================================================================
# (title, filter tags, location, commitment, skills, eligibility, description)
VOL_ROLES = [
  ("Web Designer", "remote flexible", "Remote", "Flexible Â· 4+ hrs/week",
   "HTML/CSS, Figma, basic JavaScript", "Beginner to intermediate",
   "Build and maintain pages for AYM's global programs."),
  ("Digital Marketer", "remote flexible", "Remote", "Flexible Â· 6+ hrs/week",
   "SEO, email, social advertising", "Beginner to advanced",
   "Run campaigns that grow awareness and donations."),
  ("Content Writer", "remote flexible", "Remote", "Flexible Â· 4+ hrs/week",
   "Writing, interviewing, editing", "No experience required",
   "Tell the stories of the youth we serve."),
  ("Data & Analytics", "remote part-time", "Remote", "Part-time Â· 10+ hrs/week",
   "Excel, SQL, dashboards", "Intermediate",
   "Measure impact and improve our programs."),
  ("Researcher", "remote part-time", "Remote", "Part-time Â· 8+ hrs/week",
   "Research, synthesis, citations", "Intermediate",
   "Research policy, funding, and best practice."),
  ("Project Manager", "remote on-site", "Remote / Sierra Leone", "Part-time Â· 10+ hrs/week",
   "Planning, coordination, reporting", "Experienced",
   "Coordinate volunteers and deliverables."),
  ("Video Editor", "remote flexible", "Remote", "Flexible · 4+ hrs/week",
   "Video editing, captions, visual storytelling", "Intermediate",
   "Shape VOTE Africa story videos and short clips."),
  ("Interview Host", "remote flexible", "Remote", "Flexible · 4+ hrs/week",
   "Interviewing, facilitation, careful listening", "Beginner to intermediate",
   "Host conversations with young leaders and community voices."),
  ("Correspondent", "remote on-site", "Remote / Sierra Leone", "Part-time · 8+ hrs/week",
   "Field reporting, photography, accurate notes", "Intermediate",
   "Document community-led stories from the field."),
  ("Producer", "remote part-time", "Remote", "Part-time · 10+ hrs/week",
   "Planning, coordination, editorial judgment", "Experienced",
   "Coordinate story production from pitch to publication."),
  ("Translator", "remote flexible", "Remote", "Flexible · 4+ hrs/week",
   "English and local-language fluency", "Intermediate",
   "Support subtitles and accurate community-language access."),
  ("Channel Manager", "remote part-time", "Remote", "Part-time · 6+ hrs/week",
   "YouTube, scheduling, analytics", "Intermediate",
   "Maintain the AYM video library and publishing calendar."),
]
role_cards = "".join(
  f'<article class="card" data-role="{tags}"><div class="card__body">'
  f'<div class="card__tag">{loc}</div>'
  f'<h3 class="card__title">{title}</h3>'
  f'<p class="card__text">{desc}</p>'
  f'<dl class="spec">'
  f'<div><dt>Commitment</dt><dd>{commit}</dd></div>'
  f'<div><dt>Skills</dt><dd>{skills}</dd></div>'
  f'<div><dt>Eligibility</dt><dd>{elig}</dd></div>'
  f'</dl>'
  f'<a class="card__link" href="volunteer-apply.html">Apply for this role →</a>'
  f'</div></article>'
  for title, tags, loc, commit, skills, elig, desc in VOL_ROLES
)
VOL = hero_page(
  "Volunteer",
  "Drive Real Impact <em>Across Africa</em>",
  "Lend your skills to empower local communities and shape sustainable youth-led futures.",
  "assets/img/volunteer-1.png", "Get Involved / Volunteer",
  actions='<a class="btn btn--accent" href="volunteer-apply.html">Apply to Volunteer</a><a class="btn btn--ghost" href="#roles">See Open Roles</a>'
) + f"""
<section class="section" id="roles">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Open Opportunities</span><h2>Find a role that fits you</h2><p class="lead">Filter by location or time commitment &mdash; roles show the skills and eligibility you need before you apply.</p></div>
    <div class="chips mb-2" data-filters>
      <button class="chip is-active" data-filter="all">All roles</button>
      <button class="chip" data-filter="remote">Remote</button>
      <button class="chip" data-filter="on-site">On-site</button>
      <button class="chip" data-filter="flexible">Flexible hours</button>
      <button class="chip" data-filter="part-time">Part-time</button>
    </div>
    <div class="grid grid-3" data-filter-list>{role_cards}</div>

    <div class="grid grid-2 mt-3">
      <div class="card card--flat"><div class="card__body">
        <span class="eyebrow">Eligibility</span>
        <h3 class="card__title">Am I eligible?</h3>
        <ul class="ticks">
          <li>You're 16 or older and can commit to your chosen hours.</li>
          <li>You're comfortable working in English (written and spoken).</li>
          <li>You can pass a basic background check.</li>
          <li>Most roles need no prior professional experience.</li>
        </ul>
        <a class="card__link" href="contact.html">Not sure? Ask us →</a>
      </div></div>
      <div class="card card--flat"><div class="card__body">
        <span class="eyebrow">Not ready to commit?</span>
        <h3 class="card__title">Other ways to help</h3>
        <p class="card__text">Give once or monthly, start a chapter in your city, or take on the one-year AYM Youth Fellowship for school leavers.</p>
        <a class="card__link" href="donate.html">Donate →</a>
        <a class="card__link" href="chapter.html">Start a Chapter →</a>
      </div></div>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">How it works</span><h2>From application to your first project</h2></div>
    <div class="grid grid-4">
      <div class="step"><div class="step__num">1</div><h3>Submit Your Application</h3><p class="muted">Tell us your skills, interests, and availability.</p></div>
      <div class="step"><div class="step__num">2</div><h3>Fill Background Check</h3><p class="muted">A quick screening helps keep our community safe.</p></div>
      <div class="step"><div class="step__num">3</div><h3>Receive Role Acceptance</h3><p class="muted">We match you with the team that needs you most.</p></div>
      <div class="step"><div class="step__num">4</div><h3>Start Your First Project</h3><p class="muted">Get onboarded and make an impact from day one.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="split__media"><img src="assets/img/volunteer-2.png" alt="AYM volunteer"></div>
    <div>
      <span class="eyebrow">Fellowship</span>
      <h2>1-Year School Leaver Fellowship</h2>
      <p class="lead">A proposed one-year, supervised volunteer learning pathway for emerging African leaders. Participation does not guarantee employment, payment, travel or placement.</p>
      <p><a class="btn btn--brand" href="volunteer-fellowship.html">Explore the Fellowship →</a></p>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Volunteer Experience</span><h2>How volunteers contribute</h2></div>
    <p class="lead center">Volunteers receive defined assignments, supervision and portfolio-building opportunities. Media support may include video editors, interview hosts, correspondents, producers, translators and channel managers. Roles begin on a voluntary basis and do not guarantee employment, payment, travel or placement.</p>
  </div>
</section>

<section class="section section--dark">
  <div class="container center">
    <span class="eyebrow" style="color:var(--brand)">Ready to start?</span>
    <h2>The application takes about 10 minutes</h2>
    <p class="lead" style="color:rgba(255,255,255,.85);max-width:60ch;margin:0 auto 1.4rem">Five short steps, saved as you go. Tell us your skills and availability and we'll match you with the team that needs you most.</p>
    <a class="btn btn--accent btn--lg" href="volunteer-apply.html">Start Your Application</a>
  </div>
</section>
""" + faq([
  ("What are the eligibility requirements?", "You must be 16 or older, able to work in English, and comfortable passing a basic background check. Most roles need no prior professional experience."),
  ("How do I apply?", 'Complete the <a href="volunteer-apply.html">five-step application form</a>. Your progress is saved as you go, so you can pause and return at any time.'),
  ("Do I need experience?", "Roles range from entry-level to specialist. We match your skills with a need."),
  ("How much time is required?", "It's flexible—from a few hours a week to scheduled project work. Roles begin on a voluntary basis."),
  ("Can I volunteer remotely?", "Yes. Many of our roles are fully remote, joining a global network of volunteers."),
  ("What happens after I apply?", "Application → background check → role acceptance → start your first project."),
]) + CONTACT_CTA
page("volunteer.html", "Volunteer", "Volunteer with AYM and drive real impact across Africa.", VOL, "volunteer")

# ==========================================================================
# PAGE: VOLUNTEER-APPLY  (robust, multi-step application form)
# ==========================================================================
_role_opts = "".join(f'<option>{t}</option>' for t, *_ in VOL_ROLES)
_role_opts += '<option>Not sure yet &mdash; help me choose</option>'
_country_opts = "".join(
  f'<option>{c}</option>'
  for c in ["Sierra Leone", "United States", "United Kingdom", "Kenya",
            "Rwanda", "Uganda", "Nigeria", "South Africa", "Canada", "Other"]
)
_tz_opts = "".join(
  f'<option>{t}</option>'
  for t in ["UTC-08:00 Pacific", "UTC-05:00 Eastern", "UTC+00:00 GMT/London",
            "UTC+01:00 Central Europe / West Africa", "UTC+02:00 Central/Southern Africa",
            "UTC+03:00 East Africa", "Other"]
)
_exp_opts = "".join(f'<option>{e}</option>' for e in
  ["No prior experience", "Beginner", "Intermediate", "Advanced", "Professional"])
_comm_opts = "".join(
  f'<label class="choice"><input type="radio" name="commitment" value="{v}" required> <span><strong>{v}</strong> &middot; {d}</span></label>'
  for v, d in [("2&ndash;4 hrs/week", "a light but steady commitment"),
               ("4&ndash;8 hrs/week", "a meaningful weekly contribution"),
               ("8&ndash;16 hrs/week", "a significant role in a team"),
               ("16+ hrs/week", "near full-time dedication")]
)
_skill_opts = "".join(
  f'<label class="check-inline"><input type="checkbox" name="skills" value="{s}"> {s}</label>'
  for s in ["Web / design", "Writing / editing", "Marketing / social", "Data / analytics",
            "Project management", "Translation", "Teaching / tutoring", "Fundraising", "Other"]
)
_mode_opts = "".join(
  f'<label class="choice"><input type="radio" name="mode" value="{m}" required> <span>{m}</span></label>'
  for m in ["Remote", "On-site", "Either"]
)
_heard_opts = "".join(
  f'<option>{h}</option>'
  for h in ["Search engine", "Social media", "A friend or colleague", "An AYM event",
            "Newsletter or email", "Other"]
)

APPLY = hero_page(
  "Volunteer Application",
  "Submit Your <em>Application</em>",
  "Five short steps. Your progress is saved as you go, so you can pause and come back at any time.",
  "assets/img/volunteer-0.png", "Get Involved / Volunteer / Apply",
  actions='<a class="btn btn--ghost btn--lg" href="#apply">Start Application</a>'
) + f"""
<section class="section" id="apply">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Application</span><h2>Volunteer application form</h2>
      <p class="lead">Fields marked <span class="req">*</span> are required. Nothing is submitted until the final step.</p>
    </div>

    <noscript>
      <p class="cta-note">JavaScript is turned off, so all five steps are shown together below. Please complete every field marked <span class="req">*</span>, or email your application to <a href="mailto:info@aym-inc.org">info@aym-inc.org</a>.</p>
      <style>
        .apply__steps,.apply__progress{{display:none}}
        .apply__panel[hidden]{{display:block}}
        .apply__panel[data-step="5"]{{display:none}}
        .apply__nav [data-apply-back],.apply__nav [data-apply-next]{{display:none}}
        .apply__nav [data-apply-submit]{{display:inline-flex;margin-left:0}}
      </style>
    </noscript>

    <form class="apply" action="https://api.web3forms.com/submit" method="POST" data-apply novalidate>
      <input type="hidden" name="access_key" value="1afd7c99-a77e-4aab-9fac-111a25871653">
      <input type="hidden" name="from_name" value="AYM Website">
      <input type="hidden" name="subject" value="Volunteer application from AYM website">
      <input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off" style="display:none" aria-hidden="true">
      <ol class="apply__steps" data-apply-steps aria-label="Application progress">
        <li class="apply__step is-active" data-step-indicator="1"><span class="apply__dot">1</span><span class="apply__label">About you</span></li>
        <li class="apply__step" data-step-indicator="2"><span class="apply__dot">2</span><span class="apply__label">Role &amp; skills</span></li>
        <li class="apply__step" data-step-indicator="3"><span class="apply__dot">3</span><span class="apply__label">Availability</span></li>
        <li class="apply__step" data-step-indicator="4"><span class="apply__dot">4</span><span class="apply__label">Motivation</span></li>
        <li class="apply__step" data-step-indicator="5"><span class="apply__dot">5</span><span class="apply__label">Review</span></li>
      </ol>
      <div class="apply__progress"><span data-apply-bar style="width:20%"></span></div>

      <div class="apply__panels">
        <fieldset class="apply__panel is-active" data-step="1" aria-label="About you">
          <legend class="apply__legend">Tell us about you</legend>
          <div class="grid grid-2">
            <label>First name <span class="req">*</span><input type="text" name="first" placeholder="First name" autocomplete="given-name" required></label>
            <label>Last name <span class="req">*</span><input type="text" name="last" placeholder="Last name" autocomplete="family-name" required></label>
          </div>
          <div class="grid grid-2">
            <label>Email <span class="req">*</span><input type="email" name="email" placeholder="you@example.com" autocomplete="email" required></label>
            <label>Phone <span class="small muted">(optional)</span><input type="tel" name="phone" placeholder="+1 555 000 0000" autocomplete="tel"></label>
          </div>
          <div class="grid grid-2">
            <label>Country <span class="req">*</span><select name="country" required><option value="">Select a country</option>{_country_opts}</select></label>
            <label>City / region<input type="text" name="city" placeholder="City or region"></label>
          </div>
          <label>Date of birth <span class="req">*</span>
            <input type="date" name="dob" required data-minage="16" data-error="You must be at least 16 to volunteer with AYM.">
            <span class="small muted">You must be 16 or older to apply.</span>
          </label>
        </fieldset>

        <fieldset class="apply__panel" data-step="2" aria-label="Role and skills" hidden>
          <legend class="apply__legend">Choose your role and skills</legend>
          <label>Which role interests you most? <span class="req">*</span>
            <select name="role" required><option value="">Select a role</option>{_role_opts}</select>
          </label>
          <fieldset class="choice-group"><legend>Your top skills <span class="small muted">(select any)</span></legend>{_skill_opts}</fieldset>
          <div class="grid grid-2">
            <label>Experience level<select name="experience"><option value="">Select</option>{_exp_opts}</select></label>
            <label>Portfolio / LinkedIn / website <span class="small muted">(optional)</span><input type="url" name="portfolio" placeholder="https://"></label>
          </div>
        </fieldset>

        <fieldset class="apply__panel" data-step="3" aria-label="Availability" hidden>
          <legend class="apply__legend">Your availability</legend>
          <fieldset class="choice-group"><legend>How much time can you commit? <span class="req">*</span></legend>{_comm_opts}</fieldset>
          <fieldset class="choice-group"><legend>How would you like to volunteer? <span class="req">*</span></legend>{_mode_opts}</fieldset>
          <div class="grid grid-2">
            <label>Preferred start date<input type="date" name="start"></label>
            <label>Time zone<select name="timezone"><option value="">Select a time zone</option>{_tz_opts}</select></label>
          </div>
        </fieldset>

        <fieldset class="apply__panel" data-step="4" aria-label="Motivation and background" hidden>
          <legend class="apply__legend">Motivation &amp; background</legend>
          <label>Why do you want to volunteer with AYM? <span class="req">*</span>
            <textarea name="why" rows="5" placeholder="Tell us what motivates you (at least a few sentences)..." required data-minchars="40" data-error="Please write at least 40 characters so we can get to know you."></textarea>
            <span class="small muted" data-count-for="why">0 characters</span>
          </label>
          <div class="grid grid-2">
            <label>How did you hear about us?<select name="heard"><option value="">Select</option>{_heard_opts}</select></label>
            <label>Reference name <span class="small muted">(optional)</span><input type="text" name="refname" placeholder="Name of a reference"></label>
          </div>
          <label>Reference email <span class="small muted">(optional)</span><input type="email" name="refemail" placeholder="reference@example.com"></label>
          <label class="checkbox"><input type="checkbox" name="consent_bg" required> I understand a basic background check is part of onboarding. <span class="req">*</span></label>
          <label class="checkbox"><input type="checkbox" name="consent_coc" required> I agree to AYM's code of conduct and privacy policy. <span class="req">*</span></label>
        </fieldset>

        <fieldset class="apply__panel" data-step="5" aria-label="Review and submit" hidden>
          <legend class="apply__legend">Review your application</legend>
          <p class="lead">Please check everything below. Use <strong>Back</strong> to make changes.</p>
          <div class="review" data-review></div>
          <label class="checkbox"><input type="checkbox" name="confirm" required> I confirm the information above is accurate and complete. <span class="req">*</span></label>
        </fieldset>
      </div>

      <p class="apply__error" data-apply-error hidden role="alert"></p>

      <div class="apply__nav">
        <button type="button" class="btn btn--outline" data-apply-back hidden>&larr; Back</button>
        <span class="small muted apply__saved" data-apply-saved hidden></span>
        <button type="button" class="btn btn--accent" data-apply-next>Next step &rarr;</button>
        <button type="submit" class="btn btn--accent" data-apply-submit hidden>Submit application</button>
      </div>
    </form>

    <div class="success" data-apply-done hidden>
      <div class="success__ico">&#10003;</div>
      <h2>Application received</h2>
      <p>Thank you, <strong data-apply-name>friend</strong>. We've recorded your interest and our volunteer team will be in touch.</p>
      <p class="small muted">Your application has been delivered to AYM's volunteer team. We'll be in touch at <strong data-apply-email></strong>. Your reference is <code data-apply-ref></code>.</p>
      <div class="flex"><a class="btn btn--brand" href="focus-ecotourism.html">Explore Our Work</a><a class="btn btn--outline" href="donate.html">Donate Instead</a></div>
    </div>
  </div>
</section>
"""
page("volunteer-apply.html", "Volunteer Application",
     "Apply to volunteer with the Twenty-First Century African Youth Movement using our five-step application form.",
     APPLY, "volunteer")

# ==========================================================================
# PAGE: VOLUNTEER-FELLOWSHIP
# ==========================================================================
FELLOW = hero_page(
  "AYM Global Youth Leadership Fellowship",
  "AYM Global Youth Leadership Fellowship (Proposed)",
  "A proposed one-year, supervised volunteer learning pathway for emerging African leaders. Participation does not guarantee employment, payment, travel or placement.",
  "assets/img/volunteer--special-0.png", "Get Involved / Fellowship",
  actions='<a class="btn btn--accent" href="#program">Read Program Outline</a>'
) + f"""
<section class="section" id="program">
  <div class="container split">
    <div>
      <span class="eyebrow">The Program</span>
      <h2>Step Into Leadership From Day One</h2>
      <p class="lead">The proposed fellowship is a supervised volunteer learning pathway for young people finishing school. Fellows may support media production, research, digital operations, partnerships and approved project development while building documented experience.</p>
      <h3 class="mt-2">Apply if you are a:</h3>
      <ul class="ticks">
        <li>Recent secondary school leaver ready to learn by doing.</li>
        <li>Self-starter who wants real responsibility, fast.</li>
        <li>Young person eager to build a career in Africa's growing economy.</li>
      </ul>
    </div>
    <div class="split__media"><img src="assets/img/volunteer--special-3.png" alt="AYM fellow"></div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">What you'll gain</span><h2>Experience that opens doors</h2></div>
    <div class="grid grid-3">
      <div class="feature"><div class="feature__ico">&#10003;</div><h3>Direct Mentorship</h3><p class="muted">Work alongside AYM leadership and experienced professionals.</p></div>
      <div class="feature"><div class="feature__ico">&#10003;</div><h3>Verified Work Experience</h3><p class="muted">Build a portfolio and a reference you can prove.</p></div>
      <div class="feature"><div class="feature__ico">&#10003;</div><h3>Documented Experience</h3><p class="muted">Fellows may build portfolios and request references based on completed work.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Program Tracks</span><h2>Choose your track</h2></div>
    {cards_grid([
      {"title":"Tech & Digital Operations","text":"Support websites, data, and digital campaigns across the organisation.","cta":"Apply","href":"volunteer-apply.html"},
      {"title":"Agribusiness & Sustainability","text":"Work in the field on short-duration crops and livestock enterprises.","cta":"Apply","href":"volunteer-apply.html"},
      {"title":"Project Management & Admin","text":"Coordinate projects, budgets, and reporting.","cta":"Apply","href":"volunteer-apply.html"},
      {"title":"Ecotourism & Community Development","text":"Help develop sustainable travel and community programs.","cta":"Apply","href":"volunteer-apply.html"},
    ], 4)}
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="section__head center"><span class="eyebrow" style="color:var(--brand)">Timeline</span><h2>Your fellowship year</h2></div>
    <div class="grid grid-4">
      <div class="step"><div class="step__num">1-3</div><h3>Orientation &amp; Shadowing</h3><p style="color:rgba(255,255,255,.8)">Learn the mission, systems and teams.</p></div>
      <div class="step"><div class="step__num">4-8</div><h3>Core Execution</h3><p style="color:rgba(255,255,255,.8)">Own your first real deliverables.</p></div>
      <div class="step"><div class="step__num">9-11</div><h3>Leadership &amp; Mentoring</h3><p style="color:rgba(255,255,255,.8)">Lead a project and mentor newer fellows.</p></div>
      <div class="step"><div class="step__num">12</div><h3>Career Transition</h3><p style="color:rgba(255,255,255,.8)">Graduate with a portfolio and references.</p></div>
    </div>
  </div>
</section>
""" + faq([
  ("Who is eligible?", "Recent secondary school leavers ready for a one-year, full-time commitment."),
  ("What will I work on?", "One of four tracks: Tech & Digital, Agribusiness, Project Management, or Ecotourism."),
  ("Is it remote?", "Tracks combine on-site work in Sierra Leone with online collaboration."),
  ("What happens at the end?", "You graduate with a formal reference, a portfolio, and career-pathway support."),
]) + CONTACT_CTA
page("volunteer-fellowship.html", "AYM Global Youth Leadership Fellowship", "A proposed one-year, supervised volunteer learning pathway for emerging African leaders.", FELLOW, "volunteer")

# ==========================================================================
# PAGE: DONATE (Fundraising)
# ==========================================================================
TIERS = [
  ("10","Contributes to locally purchased supplies for a youth-led activity.","$10"),
  ("25","Helps provide learning materials, internet access, or training resources.","$25"),
  ("50","Supports practical skills training or essential tools for a participant.","$50"),
  ("100","Helps equip a youth-led agricultural or small-enterprise activity.","$100"),
  ("250","Supports group training, mentorship, or a community project milestone.","$250"),
  ("500","Helps launch or expand a small youth-led pilot enterprise.","$500"),
  ("1000","Provides substantial support for training, equipment, or project implementation.","$1,000"),
  ("monthly","Provides recurring support that helps AYM plan and sustain approved programs.","Monthly"),
]
tier_buttons = "".join(
  f'<button class="tier{" is-active" if v=="100" else ""}" data-tier data-amount="{v}">{"$"+t if t!="monthly" else "Monthly"}<span>{d}</span></button>'
  for t,d,v in TIERS
) + '<div class="tier__custom"><label>Other amount<input type="number" min="1" placeholder="Enter amount" data-tier-input></label></div>'

# (id, short name used in the CT one-line subtitle, detail panel copy, href)
PAY_METHODS = [
  ("zeffy", "Zeffy", "Secure credit card donations",
   "You'll be taken to Zeffy's secure donation form to complete your gift. You can review or change the amount there before giving.", "https://www.zeffy.com/en-US/donation-form/donate-to-change-lives-21909"),
  ("paypal", "PayPal", "Give with your PayPal balance or card",
   "You'll be taken to PayPal's secure donation page. You can review or change the amount there before giving.", "https://www.paypal.com/donate/?hosted_button_id=VFN9CU8SVZ6ZE"),
  ("crypto", "Bitcoin", "Send BTC directly to AYM",
   "Send Bitcoin on the Bitcoin network to AYM. The wallet address is bc1qetqdrsm33xqg8ks24gtzczqk0p6z0jxesac7lu. Email info@aym-inc.org with your transaction ID for a receipt.", "bitcoin:bc1qetqdrsm33xqg8ks24gtzczqk0p6z0jxesac7lu"),
  ("cashapp", "Cash App", "$C21stAYM &middot; fast and fee-free in the US",
   "Send your gift to <strong>$C21stAYM</strong> and include your email so we can issue a receipt.", "https://cash.app/$C21stAYM"),
  ("bank", "Network for Good", "Bank transfer, stock &amp; donor-advised funds",
   "Use Network for Good's donation form for ACH transfers, appreciated stock, and donor-advised funds. AYM's EIN is 39-1742519.", "https://www.networkforgood.org/donation/ExpressDonation.aspx?ORGID2=+391742519"),
  ("ebay", "eBay for Charity", "Shop or sell on eBay and support AYM",
   "Visit AYM's eBay for Charity page to support AYM while shopping or selling.", "https://charity.ebay.com/charity/i/Twenty-First-Century-African-Youth-Movement/190751"),
  ("match", "Employer Match", "Double your gift at no cost",
   "Many employers match charitable gifts and volunteer hours. Search your employer's matching-gift system or ask your HR team, and name <strong>Twenty-First Century African Youth Movement</strong>.", "#"),
]
pay_buttons = "".join(
  f'<button type="button" class="method{" is-active" if i==0 else ""}" data-method="{mid}" data-name="{nm}" data-href="{href}">'
  f'<span class="method__name">{nm}</span><span class="method__desc">{sub}</span></button>'
  for i, (mid, nm, sub, _detail, href) in enumerate(PAY_METHODS)
)
pay_panels = "".join(
  f'<div class="method-panel" data-method-panel="{mid}"{" hidden" if i>0 else ""}>{detail}</div>'
  for i, (mid, _nm, _sub, detail, _href) in enumerate(PAY_METHODS)
)
# Suggested amounts shown directly in the hero (kept in sync with the full list)
hero_amounts = "".join(
  f'<a class="tier tier--sm{" is-active" if v=="100" else ""}" href="#give" data-tier data-amount="{v}">'
  f'{"$" + t if t != "monthly" else "Monthly"}</a>'
  for t, _d, v in TIERS[:6]
)

DONATE = hero_page(
  "Fundraising",
  "Invest directly in <em>Africa's youth-led future</em>",
  "Equip young leaders with skills and resources to explore enterprises, build livelihoods, and strengthen local economic independence across rural communities.",
  "assets/img/fundraising-2.png", "Get Involved / Donate",
  actions='<a class="btn btn--accent" href="#give">Donate Now</a>',
  extra=(f'<div class="hero-widget">'
         f'<span class="hero-widget__label">Suggested amounts</span>'
         f'<div class="hero-widget__amounts">{hero_amounts}</div>'
         f'<span class="hero-widget__hint">Pick an amount, then choose how you\u2019d like to pay.</span>'
         f'</div>')
) + f"""
<section class="section" id="give">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Make a gift</span><h2>Choose an amount</h2><p class="lead">Choose a secure giving option. Donations may support approved programs and reasonable operating costs in accordance with donor restrictions and AYM policy. For project-restricted gifts, use only campaigns that AYM has approved and can administer.</p></div>
    <div class="tiers">{tier_buttons}</div>

    <div class="divider"></div>

    <div class="section__head center"><span class="eyebrow">Payment method</span><h2>How would you like to pay?</h2><p class="lead">Choose a method to see its details and next steps.</p></div>
    <div class="methods" data-methods>{pay_buttons}</div>
    <div class="method-panels" data-method-panels>{pay_panels}</div>

    <div class="center mt-3">
      <button class="btn btn--accent btn--lg" data-method-cta type="button">Donate $100 with Zeffy</button>
      <p class="cta-note" data-cta-note hidden></p>
      <p class="small muted mt-1">Payments are processed by third-party providers. AYM does not store your full card details.</p>
    </div>
    <dialog class="payment-dialog" data-payment-dialog aria-labelledby="payment-dialog-title">
      <div class="payment-dialog__head"><div><span class="eyebrow">AYM donations</span><h2 id="payment-dialog-title" data-payment-title>Payment details</h2></div><button class="payment-dialog__close" type="button" data-payment-close aria-label="Close">&times;</button></div>
      <div class="payment-dialog__body" data-payment-body></div>
      <div class="payment-dialog__actions"><button class="btn btn--outline" type="button" data-payment-close>Close</button><a class="btn btn--accent" data-payment-action href="#" target="_blank" rel="noopener" hidden>Continue</a></div>
    </dialog>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Your impact</span><h2>What your donation supports</h2></div>
    <div class="grid grid-3">
      <div class="feature"><h3>Skills and Learning</h3><p class="muted">Practical learning and supervised project experience connected to approved mission activities.</p></div>
      <div class="feature"><h3>Youth Enterprises</h3><p class="muted">Seed support for small, youth-led ventures that generate income.</p></div>
      <div class="feature"><h3>Community Projects</h3><p class="muted">Education, agriculture, health, and tech initiatives in rural communities.</p></div>
    </div>

    <div class="divider"></div>

    <div class="section__head center"><span class="eyebrow">Charitable gifts and other support</span><h2>How support is accounted for</h2><p class="lead">Charitable donations fund approved mission activities. Sponsorships support identified media or events under written terms. Advertising, licensing and merchandise generate earned revenue that AYM accounts for separately.</p></div>
    <div class="grid grid-3">
      <div class="feature"><h3>Charitable donations</h3><p class="muted">Support approved mission activities and reasonable operating costs in line with donor restrictions and AYM policy.</p></div>
      <div class="feature"><h3>Sponsorships</h3><p class="muted">Support identified media or events under written terms agreed with AYM.</p></div>
      <div class="feature"><h3>Earned revenue</h3><p class="muted">Advertising, licensing and merchandise are accounted for separately from charitable gifts.</p></div>
    </div>

    <div class="divider"></div>

    <div class="section__head center"><span class="eyebrow">Opportunity Sectors</span><h2>Topics connected to AYM's work</h2><p class="lead">Explore the sectors covered by VOTE Africa. Project-restricted gifts are accepted only for campaigns AYM has approved and can administer.</p></div>
    <div class="chips chips--lg">
      <a class="chip" href="opportunity-sectors.html">All sectors</a>
      <a class="chip" href="focus-art.html">Creative Economy &amp; Culture</a>
      <a class="chip" href="focus-agriculture.html">Agriculture &amp; Food Systems</a>
      <a class="chip" href="focus-education.html">Education &amp; Skills</a>
      <a class="chip" href="focus-entrepreneurship.html">Entrepreneurship &amp; Employment</a>
      <a class="chip" href="focus-ecotourism.html">Tourism, Heritage &amp; Environment</a>
      <a class="chip" href="focus-health.html">Health &amp; Community Wellbeing</a>
      <a class="chip" href="focus-technology.html">Technology &amp; Digital Innovation</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">After you give</span><h2>What happens next</h2></div>
    <div class="grid grid-3">
      <div class="step"><div class="step__num">1</div><h3>Instant confirmation</h3><p class="muted">You\u2019ll see a confirmation on screen the moment your gift goes through.</p></div>
      <div class="step"><div class="step__num">2</div><h3>Your receipt</h3><p class="muted">An emailed receipt with the amount, date, and AYM\u2019s EIN for your records.</p></div>
      <div class="step"><div class="step__num">3</div><h3>Impact updates</h3><p class="muted">We follow up with news of the programs and youth your gift supports.</p></div>
    </div>
    <p class="small muted center mt-2">Gifts are processed by third-party payment providers. AYM does not store your card details.</p>
  </div>
</section>

<section class="section">
  <div class="container grid grid-2">
    <div class="card card--flat"><div class="card__body">
      <span class="eyebrow">Trust &amp; Transparency</span>
      <h3 class="card__title">Your gift is handled with care</h3>
      <p class="card__text">AYM is committed to ethical stewardship and transparent reporting. We provide clear information on our leadership, finances, and programs so donors can see how their support is directed to approved programs and community development.</p>
      <p class="small muted">AYM is a 501(C)(3) Nonprofit Organization.<br>EIN: 39-1742519. Donations are tax-deductible to the extent allowed by law.</p>
    </div></div>
    <div class="card card--flat"><div class="card__body">
      <span class="eyebrow">Need a hand?</span>
      <h3 class="card__title">Giving by cheque, stock or wire?</h3>
      <p class="card__text">For gifts by cheque, wire transfer, appreciated stock, planned giving, or anything the buttons above don't cover, our team will set it up with you and send a tax receipt.</p>
      <a class="card__link" href="contact.html">Talk to our team →</a>
    </div></div>
  </div>
</section>

<section class="section section--dark">
  <div class="container center">
    <span class="eyebrow" style="color:var(--brand)">Our impact so far</span>
    <h2>Together we've built momentum</h2>
    <div class="stats stats--dark" style="justify-content:center">
      <div class="stat"><div class="stat__num">Local</div><div class="stat__label">Community-rooted programs</div></div>
      <div class="stat"><div class="stat__num">Learning</div><div class="stat__label">Skills and practical experience</div></div>
      <div class="stat"><div class="stat__num">Enterprise</div><div class="stat__label">Approved local pilots</div></div>
      <div class="stat"><div class="stat__num">Verified</div><div class="stat__label">Updates published after review</div></div>
    </div>
    <p class="small" style="color:rgba(255,255,255,.7)">AYM publishes numeric impact figures only after program and finance verification.</p>
  </div>
</section>
""" + faq([
  ("Is my donation tax-deductible?", "AYM is a U.S. 501(c)(3) nonprofit organization. Donations are generally tax-deductible to the extent allowed by law. Donors should retain their receipts and consult a tax adviser about their circumstances."),
  ("How will AYM use my donation?", "Donations support approved programs, operations, and organizational needs connected to AYM's mission. Donors may select a program when available, or allow AYM to direct the gift where it is most needed."),
  ("Can I make a monthly gift?", "Yes. Monthly donations provide reliable support and help AYM plan projects, training, and youth-enterprise activities more effectively."),
  ("Will I receive a receipt?", "Donors who provide valid contact information should receive an electronic or written acknowledgement stating the amount, date, and whether goods or services were received in exchange."),
  ("Can I donate to a particular project?", "Yes, when a designated option is available. AYM explains how it handles gifts when a project is completed, fully funded, postponed, or no longer feasible."),
  ("Can my employer match my donation?", "Some employers match charitable contributions or volunteer hours. Search your employer's matching-gift system or contact your human-resources department."),
  ("Can I donate equipment or supplies?", "AYM may accept approved gifts that meet a documented program need. Contact AYM before purchasing or shipping materials because transportation, customs, storage and distribution costs may exceed the item's value."),
  ("Is online giving secure?", "Payments are processed through third-party services. AYM does not collect or store complete card information directly on its website. Check the provider's checkout page for its current security details."),
  ("Can I donate anonymously?", "Yes, where the payment system permits it. AYM may still need limited information to process the contribution and comply with legal or financial requirements."),
]) + CONTACT_CTA
page("donate.html", "Donate", "Invest directly in Africa's youth-led future. Choose a one-time or monthly gift to support youth skills and enterprise activities.", DONATE, "donate")

print("volunteer/fellowship/donate done")

# ==========================================================================
# PAGE: CHAPTER
# ==========================================================================
CHAPTER = hero_page(
  "AYM Chapter",
  "Mobilize Your Community. <em>Lead an AYM Chapter.</em>",
  "Bring the African Youth Movement to your city or country. Document community stories, develop practical ideas and collaborate under approved standards. Participation does not create an AYM legal chapter or authorize fundraising in AYM's name; independent community groups may partner without becoming official chapters.",
  "assets/img/aym-chapter-0.png", "About / Chapter",
  actions='<a class="btn btn--ghost" href="#network">Find an Existing Chapter</a>'
          '<a class="btn btn--accent" href="contact.html">Apply to Start a Chapter</a>'
) + f"""
<section class="section">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Why start a chapter</span><h2>Why Start a Local Chapter?</h2></div>
    <div class="grid grid-4">
      <div class="feature"><div class="feature__ico">&#9733;</div><h3>Global Credibility &amp; Fundraising</h3><p class="muted">Approved local teams may collaborate under AYM's governance on grant and institutional-funding proposals, subject to written authorization.</p></div>
      <div class="feature"><div class="feature__ico">&#9733;</div><h3>Turnkey Resource Infrastructure</h3><p class="muted">Approved teams may use AYM's campaign tools only under written authorization and reporting rules.</p></div>
      <div class="feature"><div class="feature__ico">&#9733;</div><h3>Centralized Pan-African Network</h3><p class="muted">Approved chapters and independent partners can coordinate shared activities without merging legal entities.</p></div>
      <div class="feature"><div class="feature__ico">&#9733;</div><h3>Leadership Development</h3><p class="muted">Connect members to cross-border conferences, leadership training and the African Lecture Series.</p></div>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">How it works</span><h2>How Chapters Drive Impact</h2></div>
    <div class="grid grid-4">
      <div class="step"><div class="step__num">1</div><h3>Local Grassroots Organizing</h3><p class="muted">Bring people together around the issues that matter in your community.</p></div>
      <div class="step"><div class="step__num">2</div><h3>Resource Mobilization &amp; Grants</h3><p class="muted">Approved teams may mobilize resources and apply for grants only with written authorization.</p></div>
      <div class="step"><div class="step__num">3</div><h3>Creating Sustainable Employment</h3><p class="muted">Develop locally led enterprise ideas; hiring depends on approved plans and funding.</p></div>
      <div class="step"><div class="step__num">4</div><h3>Knowledge Sharing</h3><p class="muted">Share lessons across the Pan-African chapter network.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">Your role</span>
      <h2>Your role as a coordinator</h2>
      <div class="grid grid-1 mt-2">
        <div><h3>Recruit and Inspire</h3><p class="muted">Grow a team of passionate young leaders in your area.</p></div>
        <div><h3>Collaborate</h3><p class="muted">Work with the global AYM team and other chapters.</p></div>
        <div><h3>Grow the Movement</h3><p class="muted">Champion AYM's mission locally and across borders.</p></div>
      </div>
    </div>
    <div class="split__media"><img src="assets/img/aym-chapter-6.png" alt="AYM chapter"></div>
  </div>
</section>

<section class="section section--dark" id="network">
  <div class="container">
    <div class="section__head center"><span class="eyebrow" style="color:var(--brand)">Our network</span><h2>Active &amp; Emerging Chapter Network</h2></div>
    <div class="grid grid-3">
      <div class="card"><div class="card__body"><div class="card__tag">West Africa</div><img class="card__img" src="assets/img/aym-chapter-8.png" alt=""><h3 class="card__title">Ghana Â· Nigeria Â· Sierra Leone Â· Senegal</h3></div></div>
      <div class="card"><div class="card__body"><div class="card__tag">East Africa</div><h3 class="card__title">Kenya Â· Uganda Â· Rwanda Â· Tanzania</h3></div></div>
      <div class="card"><div class="card__body"><div class="card__tag">Southern Africa</div><h3 class="card__title">South Africa Â· Zambia Â· Zimbabwe</h3></div></div>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Resources</span><h2>Resources Provided to Chapter Leaders</h2></div>
    <div class="grid grid-3">
      <div class="feature"><h3>Fundraising &amp; Tech Toolkit</h3><p class="muted">Payment integrations, campaign templates and guides.</p></div>
      <div class="feature"><h3>Legal &amp; Governance Support</h3><p class="muted">Approved teams receive guidance on operating within AYM's framework; other groups remain independent.</p></div>
      <div class="feature"><h3>Program &amp; Event Playbooks</h3><p class="muted">Proven templates for launching programs and local events.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Onboarding</span><h2>Chapter Onboarding Process</h2></div>
    <div class="grid grid-4">
      <div class="step"><div class="step__num">1</div><h3>Submit Your Application</h3><p class="muted">Tell us about your community and vision.</p></div>
      <div class="step"><div class="step__num">2</div><h3>Fill Background Check</h3><p class="muted">A screening step to keep our network safe.</p></div>
      <div class="step"><div class="step__num">3</div><h3>Receive Role Acceptance</h3><p class="muted">We confirm your chapter and connect you with mentors.</p></div>
      <div class="step"><div class="step__num">4</div><h3>Pilot a Documented Activity</h3><p class="muted">Run a small activity under agreed roles, brand permissions and reporting.</p></div>
    </div>
  </div>
</section>
""" + faq([
  ("Who can start a chapter?", "Anyone committed to youth empowerment—individuals or small groups—can apply. Approval is required before a group may describe itself as an approved AYM chapter or use AYM's name and marks."),
  ("Are all local groups official AYM chapters?", "No. Only groups that complete AYM's application, screening and written acceptance are recognized as approved AYM chapters. Other groups may be partners or emerging teams and should not imply formal status or tax-exempt status."),
  ("Is there a cost to start a chapter?", "No. Local teams may use public resources and templates where permitted."),
  ("What support do I receive?", "Orientation, role guidance, reporting expectations and approved templates where applicable."),
  ("How long does onboarding take?", "Submit application → background check → acceptance → start your first project."),
  ("Do chapters handle their own finances?", "Approved AYM chapters do not become separate 501(c)(3) organizations by joining the network. Financial activity must follow AYM's governance, reporting and written authorization; independent groups remain legally and financially separate."),
]) + CONTACT_CTA
page("chapter.html", "Start an AYM Chapter", "Bring the African Youth Movement to your city or country and lead grassroots change.", CHAPTER, "chapter")

# ==========================================================================
# PAGE: STORE
# ==========================================================================
PRODUCTS = [
  ("AYM Heritage Collegiate T-Shirt — Est. 2000","From $23.50","assets/img/store-1.png","Clothing",False),
  ("AYM Logo Cap — Est. 2000","$20.00","assets/img/store-0.png","Clothing",True),
  ("AYM Mission Mug","$12.00","assets/img/image-36-0.png","Mugs",True),
  ("AYM Spirit Tote Bag","$18.00","assets/img/image-38-0.png","Bags",True),
  ("AYM Pin Button Set","$8.00","","Accessories",True),
  ("AYM Sticker Pack","$5.00","","Accessories",True),
  ("AYM Laptop Sleeve","$28.00","","Accessories",True),
  ("AYM Water Bottle","$16.00","","Accessories",True),
  ("AYM Spiral Notebook","$10.00","","Stationery",True),
  ("AYM Tapestry","$30.00","","Home",True),
]
cart_msg = ("Demo store \u2014 the shopping cart isn\u2019t connected yet. "
            "Link this button to your eCommerce provider (WooCommerce, Shopify Buy Button or Snipcart) to take real orders.")
product_cards = "".join(
  f'<article class="card" data-role="{c.lower()}">'
  + (f'<img class="card__img" src="{img}" alt="{t}" loading="lazy">' if img
     else '<div class="card__img card__img--placeholder" aria-hidden="true"></div>')
  + f'<div class="card__body"><div class="card__tag">{c}{" · Sample listing" if sample else ""}</div>'
  f'<h3 class="card__title">{t}</h3><p class="price">{p}</p>'
  f'<button type="button" class="btn btn--outline btn--block" data-demo-msg="{cart_msg}">Add to Cart</button>'
  f'</div></article>'
  for t, p, img, c, sample in PRODUCTS
)
STORE = hero_page(
  "Impact Store",
  "Each Purchase <em>Gives Purpose</em>",
  "Every item you buy supports youth-led programs, enterprises, and community projects across Africa.",
  "assets/img/store-0.png", "Store",
  actions='<a class="btn btn--accent" href="#shop">Shop Now</a>'
) + f"""
<section class="section" id="shop">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Shop by category</span><h2>Clothing Â· Mugs Â· Bags Â· More</h2></div>
    <div class="chips mb-2" data-filters>
      <button class="chip is-active" data-filter="all">All</button>
      <button class="chip" data-filter="clothing">Clothing</button>
      <button class="chip" data-filter="mugs">Mugs</button>
      <button class="chip" data-filter="bags">Bags</button>
      <button class="chip" data-filter="accessories">Accessories</button>
      <button class="chip" data-filter="stationery">Stationery</button>
      <button class="chip" data-filter="home">Home</button>
    </div>
    <div class="grid grid-4" data-filter-list>{product_cards}</div>
    <div class="center mt-3"><button class="btn btn--outline" data-demo-msg="All available items are already shown.">Load More</button></div>
    <p class="cta-note" data-demo-note hidden></p>
    <p class="small muted center mt-1">Sample listings are shown for design review only. The live shop currently lists the AYM Heritage Collegiate T-Shirt at $23.50–$27.50.</p>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Inspirations</span><h2>See how the movement looks</h2></div>
    <div class="grid grid-4">
      <img class="gallery__img" src="assets/img/section-1-0.png" alt="">
      <img class="gallery__img" src="assets/img/section-1-1.png" alt="">
      <img class="gallery__img" src="assets/img/section-1-2.png" alt="">
      <img class="gallery__img" src="assets/img/section-1-3.png" alt="">
    </div>
  </div>
</section>
""" + faq([
  ("How do my purchases help?", "Proceeds from the Impact Store support youth-led programs and enterprises."),
  ("What payment methods are accepted?", "Secure checkout supports major cards and digital wallets."),
  ("When will my order ship?", "Shipping times and rates are confirmed at checkout. Items ship from the United States."),
  ("Can I return an item?", "Contact us within 30 days and we'll help arrange a return or exchange."),
]) + CONTACT_CTA
page("store.html", "Impact Store", "Shop AYM merchandise. Each purchase gives purpose and supports youth-led programs.", STORE, "store")

print("chapter/store done")

# ==========================================================================
# FOCUS PAGES
# ==========================================================================
def focus_hero(title, sub, img, actions):
    return hero_page("Opportunity Sector", title, sub, img, "Opportunity Sectors", actions)

SECTOR_FRAMEWORK = {
  "art": (
    "Creative talent is often treated as culture only, with limited access to skills, markets and fair recognition.",
    "Artists, filmmakers, designers and cultural workers explain how they build value while preserving heritage.",
    "Portfolio skills, mentorship, market access and partnerships can turn creative practice into livelihoods.",
    "AYM presents verified exhibitions, profiles and learning resources separately from future ambitions.",
    "Propose a creator profile, volunteer your skills or support an approved creative-learning activity."
  ),
  "agriculture": (
    "Young farmers face limited land access, finance, storage and reliable routes to market.",
    "Farmers, processors and agribusiness innovators share what works in local conditions.",
    "Short-duration crops, small livestock, training and buyer links can support practical enterprise pilots.",
    "AYM separates documented pilots from proposals and publishes figures only after verification.",
    "Suggest a farmer story, propose an enterprise pilot or support an approved training activity."
  ),
  "education": (
    "Rural learners often lack consistent access to teachers, digital tools and practical career pathways.",
    "Students, mentors and local educators describe the barriers they face and the solutions they are testing.",
    "Hybrid learning, hands-on science, mobile access and mentorship connect education with real opportunities.",
    "AYM reports verified learning activities and avoids promising outcomes that cannot be evidenced.",
    "Volunteer as a mentor, share a learning story or support an approved education activity."
  ),
  "entrepreneurship": (
    "Young people with viable ideas often lack business basics, mentorship, seed support and market access.",
    "Founders explain how they identify problems, serve customers and build value in their communities.",
    "Feasibility support, basic training, peer networks and responsible resource mobilization can help pilots start.",
    "AYM states clearly that funding, placement and success are not guaranteed.",
    "Submit an idea, volunteer your business skills or support an approved enterprise pilot."
  ),
  "ecotourism": (
    "Natural places and cultural heritage need protection while local communities need reliable livelihoods.",
    "Guides, hosts and community leaders share how tourism can respect heritage and distribute benefits locally.",
    "Hospitality skills, local guiding, conservation and transparent visitor arrangements can support community-led income.",
    "AYM presents verified destinations and approved arrangements separately from future plans.",
    "Suggest a community feature, enquire about visits or support an approved conservation activity."
  ),
  "health": (
    "Communities face gaps in reliable health information, qualified local support and practical prevention resources.",
    "Qualified practitioners and community health workers explain needs and locally appropriate responses.",
    "Needs assessment, stakeholder collaboration and carefully sourced resources can strengthen community-led action.",
    "AYM does not provide clinical advice and publishes health information only from responsible sources.",
    "Suggest a carefully sourced health story or support an approved community activity."
  ),
  "technology": (
    "Rural communities are often cut off from connectivity, devices and the skills needed for the digital economy.",
    "Students, creators and local enterprises show how practical tools solve everyday problems.",
    "Computer education, sustainable connectivity, supervised digital projects and shared infrastructure can widen access.",
    "AYM documents verified access projects and separates them from planned infrastructure work.",
    "Share an innovation, volunteer technical skills or support an approved digital-inclusion activity."
  ),
}

def sector_framework(key):
    challenge, voices, opportunities, evidence, involve = SECTOR_FRAMEWORK[key]
    items = [
        ("The Challenge", challenge),
        ("African Voices", voices),
        ("Opportunities and Solutions", opportunities),
        ("Projects and Evidence", evidence),
        ("Get Involved", involve),
    ]
    cards = "".join(
        f'<div class="feature"><h3>{title}</h3><p class="muted">{text}</p></div>'
        for title, text in items
    )
    return f"""
<section class="section">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Sector framework</span><h2>From voices to opportunity</h2><p class="lead">Every sector follows the same path so stories, evidence and action stay connected.</p></div>
    <div class="grid grid-3">{cards}</div>
  </div>
</section>
"""

# ---- ART ----
ART = focus_hero(
  "Creative Economy &amp; Culture",
  "Promote African creativity, cultural identity, and creative enterprises.",
  "assets/img/art-2.png",
  '<a class="btn btn--accent" href="contact.html">Profile a Creator</a><a class="btn btn--ghost" href="opportunity-sectors.html">Explore Skills and Markets</a>'
) + statrow([("All genres","Music, visual, film, design"),("Youth-led","Creator profiles"),("Heritage","Cultural preservation"),("Global","Perception & dialogue")]) + f"""
<section class="section">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Core Strategy</span><h2>Our approach to the creative economy</h2></div>
    <div class="grid grid-3">
      <div class="feature"><h3>Unlocking Potential</h3><p class="muted">Give young creatives the skills, tools and market access to turn talent into income.</p></div>
      <div class="feature"><h3>Amplifying Heritage</h3><p class="muted">Celebrate and preserve Sierra Leone's masking traditions and cultural identity.</p></div>
      <div class="feature"><h3>Economic Viability</h3><p class="muted">Build a Creative Industry that supports creative livelihoods across every genre.</p></div>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="container split">
    <div class="split__media"><img src="assets/img/art-0.png" alt="Representations of Violence"></div>
    <div>
      <span class="eyebrow">Groundbreaking Impact</span>
      <h2>Representations of Violence</h2>
      <p class="lead">Between 1991 and 2001, Sierra Leone's civil war claimed an estimated 50,000 lives. Through 38 paintings and accompanying narrative, young artists gave form to a national trauma and opened a global conversation.</p>
      <p><a class="btn btn--outline" href="events.html">See the Exhibition →</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">Global Perception</span>
      <h2>Imagining Africa: Building Artistic Bridges Through Perception</h2>
      <p class="lead">A program that challenges one-dimensional narratives of Africa by connecting artists and audiences across continents.</p>
      <div class="tags mt-2">
        <span class="pill">Global Perception &amp; Dialogue</span>
        <span class="pill">Sierra Leone Masking Traditions</span>
      </div>
      <p class="mt-2"><a class="btn btn--outline" href="projects.html">View the Project →</a></p>
    </div>
    <div class="split__media"><img src="assets/img/art-1.png" alt="Imagining Africa"></div>
  </div>
</section>
""" + sector_framework("art") + CONTACT_CTA
page("focus-art.html", "Creative Economy &amp; Culture", "Promote African creativity, cultural identity, and creative enterprises.", ART)

# ---- AGRICULTURE ----
AGRI = focus_hero(
  "Agriculture &amp; Food Systems",
  "Advance food security, agribusiness, and rural employment.",
  "assets/img/agri-0.png",
  '<a class="btn btn--accent" href="blog.html">Watch Farmer Stories</a><a class="btn btn--ghost" href="contact.html">Propose an Enterprise Pilot</a>'
) + statrow([("Short-duration","crops for rapid returns"),("6+","livestock varieties"),("Fast-turnover","harvesting"),("Local","enterprise pilots")]) + f"""
<section class="section">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Sector Focus</span><h2>High-value, youth-led agriculture</h2></div>
    <div class="grid grid-3">
      <div class="feature"><h3>High Profitability</h3><p class="muted">Rapid-harvest, fast-turnover crops that generate income quickly.</p></div>
      <div class="feature"><h3>Skill Building</h3><p class="muted">Comprehensive agricultural mentorship and hands-on training.</p></div>
      <div class="feature"><h3>Self-Sustainability</h3><p class="muted">Community-driven economic growth that funds itself.</p></div>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="container split">
    <div>
      <span class="eyebrow">Crops &amp; Livestock</span>
      <h2>Crop &amp; Livestock Focus</h2>
      <div class="grid grid-1 mt-2">
        <div><h3>Spices &amp; Vegetables</h3><p class="muted">High-value, short-duration horticulture for local and regional markets.</p></div>
        <div><h3>Small Livestock</h3><p class="muted">Poultry and small ruminants that produce rapid, repeatable returns.</p></div>
        <div><h3>Cattle &amp; Small Ruminants</h3><p class="muted">Larger livestock enterprises for long-term community wealth.</p></div>
      </div>
    </div>
    <div class="split__media"><img src="assets/img/agri-2.png" alt="AYM agriculture"></div>
  </div>
</section>
""" + sector_framework("agriculture") + CONTACT_CTA
page("focus-agriculture.html", "Agriculture &amp; Food Systems", "Advance food security, agribusiness, and rural employment.", AGRI)

# ---- EDUCATION ----
EDU = focus_hero(
  "Education &amp; Skills",
  "Expand access to learning, professional development, and career opportunities.",
  "assets/img/education-1.png",
  '<a class="btn btn--accent" href="blog.html">Explore Learning Stories</a><a class="btn btn--ghost" href="volunteer.html">Volunteer as a Mentor</a>'
) + f"""
<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">Join the Movement</span>
      <h2>Join the Rural Education Revolution</h2>
      <p class="lead">Access to quality education transforms communities. AYM brings learning to remote areas through a flexible, technology-enabled hybrid model.</p>
      <p><a class="btn btn--outline" href="projects.html">Learn More →</a></p>
    </div>
    <div class="split__media"><img src="assets/img/education-0.png" alt="AYM education"></div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Our Approach</span><h2>A hybrid learning model</h2></div>
    <div class="grid grid-2">
      <div class="feature"><h3>In-Person Learning Hubs</h3><p class="muted">Community-based hubs with mentors and hands-on science.</p></div>
      <div class="feature"><h3>Mobile &amp; E-Learning</h3><p class="muted">Digital lessons that reach students wherever they are.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Impact</span><h2>Student Benefits</h2></div>
    <div class="grid grid-4">
      <div class="feature"><h3>Flexible Learning</h3><p class="muted">Study that adapts to rural life and work.</p></div>
      <div class="feature"><h3>STEM Preparedness</h3><p class="muted">Science, technology and math skills for the modern economy.</p></div>
      <div class="feature"><h3>Critical Thinking</h3><p class="muted">Problem-solving for real community challenges.</p></div>
      <div class="feature"><h3>Community Support</h3><p class="muted">Families and local leaders engaged throughout.</p></div>
    </div>
    <div class="tags mt-3 center">
      <span class="pill">#AYMEducation</span><span class="pill">#RuralLearning</span><span class="pill">#SkillsForLife</span>
    </div>
  </div>
</section>
""" + sector_framework("education") + CONTACT_CTA
page("focus-education.html", "Education &amp; Skills", "Expand access to learning, professional development, and career opportunities.", EDU)

print("art/agri/edu done")

# ---- ENTREPRENEURSHIP ----
ENTRE = focus_hero(
  "Entrepreneurship &amp; Employment",
  "Support youth-led enterprises, innovation, and job creation.",
  "assets/img/entre-1.png",
  '<a class="btn btn--accent" href="contact.html">Submit an Idea</a><a class="btn btn--ghost" href="blog.html">Watch Enterprise Stories</a>'
) + f"""
<section class="section">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Three Pillars</span><h2>How we build entrepreneurs</h2></div>
    <div class="grid grid-3">
      <div class="feature"><div class="feature__ico">&#9733;</div><h3>Endless Avenues of Exploration</h3><p class="muted">From technology to agribusiness, we help young people discover and pursue opportunity.</p></div>
      <div class="feature"><div class="feature__ico">&#9733;</div><h3>Empowering Local Communities</h3><p class="muted">Ventures are rooted in local needs and designed to strengthen community livelihoods.</p></div>
      <div class="feature"><div class="feature__ico">&#9733;</div><h3>Driving Social Change</h3><p class="muted">Enterprise becomes a tool for stability, dignity and lasting progress.</p></div>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="container split">
    <div class="split__media"><img src="assets/img/entre-0.png" alt="AYM entrepreneurship"></div>
    <div>
      <span class="eyebrow">Strategic Framework</span>
      <h2>Empowerment Through Entrepreneurship</h2>
      <p class="lead">We walk with young founders from an idea to a working venture—training, mentorship, seed support and market connections.</p>
      <h3 class="mt-2">Embarking on the Journey</h3>
      <ul class="ticks">
        <li>Idea development and business basics.</li>
        <li>Hands-on mentorship from real operators.</li>
        <li>Seed support to launch a pilot enterprise.</li>
        <li>Access to markets and a peer founder network.</li>
      </ul>
    </div>
  </div>
</section>
""" + sector_framework("entrepreneurship") + CONTACT_CTA
page("focus-entrepreneurship.html", "Entrepreneurship &amp; Employment", "Support youth-led enterprises, innovation, and job creation.", ENTRE)

# ---- HEALTHCARE ----
HEALTH = focus_hero(
  "Health &amp; Community Wellbeing",
  "Promote health education, awareness, and community resilience.",
  "assets/img/health-0.png",
  '<a class="btn btn--accent" href="contact.html">Suggest a Health Story</a><a class="btn btn--ghost" href="blog.html">Explore Verified Resources</a>'
) + f"""
<section class="section">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Strategy &amp; Implementation</span><h2>How we improve community health</h2></div>
    <div class="grid grid-4">
      <div class="step"><div class="step__num">1</div><h3>In-depth Needs Assessment</h3><p class="muted">We start by understanding the real health gaps in each community.</p></div>
      <div class="step"><div class="step__num">2</div><h3>Stakeholder Collaboration</h3><p class="muted">We partner with local clinics, leaders and health workers.</p></div>
      <div class="step"><div class="step__num">3</div><h3>Community-Led Support</h3><p class="muted">Medical supplies and community-led solutions where needs are verified.</p></div>
      <div class="step"><div class="step__num">4</div><h3>Continuous Evaluation</h3><p class="muted">We measure outcomes and improve programs over time.</p></div>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="container split">
    <div>
      <span class="eyebrow">Impact Goals</span>
      <h2>Healthier, stronger communities</h2>
      <p class="lead">By connecting youth-led energy with real medical needs, AYM helps reduce preventable illness and build trust between communities and health services.</p>
    </div>
    <div class="split__media"><img src="assets/img/health-1.png" alt="AYM healthcare"></div>
  </div>
</section>
""" + sector_framework("health") + CONTACT_CTA
page("focus-health.html", "Health &amp; Community Wellbeing", "Promote health education, awareness, and community resilience.", HEALTH)

# ---- ECOTOURISM ----
# (title, description, image, optional detail href)
ACTIVITIES = [
  ("Fishing", "Enjoy traditional and sport fishing along Sierra Leone's rivers and coast.",
   "assets/img/ecotourism-1.png", None),
  ("Waterfalls", "Discover hidden waterfalls set in lush tropical forest.",
   "assets/img/ecotourism-2.png", None),
  ("Forest Safari", "Journey into the wild to see the forests of Sierra Leone and their wildlife.",
   "assets/img/ecotourism-3.png", "focus-ecotourism-forest-safari.html"),
  ("Sailing", "Sail calm coastal waters on community-run boat trips.",
   "assets/img/ecotourism-4.png", None),
  ("Beaches", "Relax on pristine, uncrowded Atlantic beaches \u2014 including Moselle Beach.",
   "assets/img/ecotourism-5.png", None),
  ("Culture", "Experience local music, dance and masking traditions.",
   "assets/img/ecotourism-1.png", None),
  ("Culinary", "Taste authentic Sierra Leonean cuisine prepared by local hosts.",
   "assets/img/ecotourism-4.png", None),
  ("Excursions", "Join guided excursions to historic and natural landmarks.",
   "assets/img/ecotourism-3.png", None),
]
eco_cards = "".join(
  f'<article class="card">'
  f'<img class="card__img" src="{img}" alt="{t}" loading="lazy">'
  f'<div class="card__body"><div class="card__tag">Activity</div>'
  f'<h3 class="card__title">{t}</h3><p class="card__text">{d}</p>'
  + (f'<a class="card__link" href="{href}">Learn More →</a>' if href else "")
  + f'</div></article>'
  for t, d, img, href in ACTIVITIES
)
ECO = focus_hero(
  "Tourism, Heritage &amp; Environment",
  "Promote cultural heritage, sustainable tourism, and environmental responsibility.",
  "assets/img/ecotourism-0.png",
  '<a class="btn btn--accent" href="blog.html">Explore Heritage Stories</a><a class="btn btn--ghost" href="contact.html">Suggest a Community Feature</a>'
) + f"""
<section class="section">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Endless Activities</span><h2>Things to do</h2></div>
    <div class="grid grid-4">{eco_cards}</div>
    <div class="center mt-3">
      <p class="lead">Want to know about these adventures?</p>
      <a class="btn btn--brand" href="contact.html">Contact Us →</a>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="container split">
    <div class="split__media"><img src="assets/img/ecotourism-2.png" alt="Moselle Beach"></div>
    <div>
      <span class="eyebrow">Featured Destination</span>
      <h2>Sustainable Travel &amp; Community Development</h2>
      <p class="lead">Discover Moselle Beach, Sierra Leone. Visits may support local livelihoods, conservation and community projects under approved arrangements.</p>
    </div>
  </div>
</section>

<section class="section" id="packages">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Transparent Pricing</span><h2>Package Options</h2>
      <p class="lead">All daily activities include food and drinks (featuring a traditional African dish and an optional traditional Poyo beverage). Knowledgeable local guides organize, manage, and serve you throughout the tour. <strong>Note:</strong> transportation to and from Moselle Beach is the visitor's responsibility.</p>
    </div>
    <div class="grid grid-3">
      <div class="card card--flat"><div class="card__body"><div class="card__tag">Tier 1</div><h3 class="card__title">Solo &amp; Pairs</h3><p class="price">$50.00 <span class="muted">/ person</span></p><p class="small muted">1 to 2 guests</p><p class="card__text">Daily individual guided tour to Moselle Beach.</p></div></div>
      <div class="card card--flat"><div class="card__body"><div class="card__tag">Tier 2</div><h3 class="card__title">Small Groups (3+)</h3><p class="price">$45.00 <span class="muted">/ person</span></p><p class="small muted">3 or more guests</p><p class="card__text">Daily group tour discount to Moselle Beach.</p></div></div>
      <div class="card card--flat"><div class="card__body"><div class="card__tag">Tier 3</div><h3 class="card__title">Custom &amp; Large Groups</h3><p class="price">Contact for pricing</p><p class="small muted">Custom packages</p><p class="card__text">Customized camping programs, larger group itineraries, and special excursions (e.g. Bonthe Island).</p></div></div>
    </div>
    <div class="center mt-3">
      <a class="btn btn--accent" href="mailto:infosl@aym-inc.org">Inquire About Packages</a>
      <p class="small muted mt-1">Questions? Email <a href="mailto:infosl@aym-inc.org">infosl@aym-inc.org</a></p>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">No hidden costs</span><h2>Plan your eco-trip today</h2><p class="lead">We are committed to complete pricing transparency with zero hidden charges beyond the listed costs.</p></div>
    <div class="grid grid-3">
      <div class="feature"><h3>Guides included</h3><p class="muted">Local guides organize and serve every day of your tour.</p></div>
      <div class="feature"><h3>Meals included</h3><p class="muted">Food and drinks are covered, including an optional traditional Poyo.</p></div>
      <div class="feature"><h3>Nothing added later</h3><p class="muted">No surprise charges beyond the published tier price.</p></div>
    </div>
  </div>
</section>
""" + sector_framework("ecotourism") + CONTACT_CTA
page("focus-ecotourism.html", "Tourism, Heritage &amp; Environment", "Promote cultural heritage, sustainable tourism, and environmental responsibility.", ECO)

# ---- ECOTOURISM > FOREST SAFARI (inner sub-page from the Figma menu) ----
SAFARI = hero_page(
  "Tourism, Heritage &amp; Environment / Forest Safari",
  "A Journey Into <em>the Wild</em>",
  "Walk Sierra Leone's protected forests with a local guide and see the wildlife, rivers and canopy that make the country's interior so extraordinary.",
  "assets/img/ecotourism-3.png", "Opportunity Sectors / Tourism, Heritage &amp; Environment / Forest Safari",
  actions='<a class="btn btn--accent" href="focus-ecotourism.html#packages">Book Your Experience</a> '
          '<a class="btn btn--ghost btn--lg" href="contact.html">Ask a Question</a>'
) + f"""
<section class="section">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">The Experience</span><h2>What you'll do in the forest</h2></div>
    <div class="grid grid-3">
      <div class="feature"><h3>Guided forest walk</h3><p class="muted">A knowledgeable local guide leads you along established trails through primary and secondary forest.</p></div>
      <div class="feature"><h3>Wildlife &amp; birdwatching</h3><p class="muted">Spot monkeys, forest birds and a wide range of plant life along the trail.</p></div>
      <div class="feature"><h3>Rivers &amp; clearings</h3><p class="muted">Rest at streams and forest clearings, with time for photos and questions along the way.</p></div>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="container split">
    <div class="split__media"><img src="assets/img/ecotourism-1.png" alt="Forest safari"></div>
    <div>
      <span class="eyebrow">Good to know</span>
      <h2>What's included</h2>
      <ul class="ticks">
        <li>A professional local guide for the full walk.</li>
        <li>Food and drinks, including a traditional African dish.</li>
        <li>Booking, planning and on-the-ground support.</li>
      </ul>
      <ul class="ticks mt-2">
        <li><strong>Not included:</strong> transport to and from the trailhead.</li>
        <li>Wear closed shoes and bring water and sun protection.</li>
        <li>Tours run in small groups so the forest stays undisturbed.</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Along the way</span><h2>Scenes from the trail</h2></div>
    <div class="gallery">
      <img class="gallery__img" src="assets/img/ecotourism-3.png" alt="Forest canopy">
      <img class="gallery__img" src="assets/img/ecotourism-5.png" alt="Forest trail">
      <img class="gallery__img" src="assets/img/ecotourism-2.png" alt="Waterfall in the forest">
      <img class="gallery__img" src="assets/img/ecotourism-4.png" alt="River crossing">
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Plan your visit</span><h2>Forest Safari at a glance</h2></div>
    <div class="grid grid-3">
      <div class="card card--flat"><div class="card__body"><div class="card__tag">Group size</div><h3 class="card__title">Small groups</h3><p class="card__text">Solo travellers, pairs and groups are all welcome.</p></div></div>
      <div class="card card--flat"><div class="card__body"><div class="card__tag">Duration</div><h3 class="card__title">Indicative: half or full day</h3><p class="card__text">Confirm the available route with AYM Sierra Leone before booking.</p></div></div>
      <div class="card card--flat"><div class="card__body"><div class="card__tag">Price</div><h3 class="card__title">Indicative: from $45.00</h3><p class="card__text">Group rates shown for guidance only; confirm current pricing before booking.</p></div></div>
    </div>
    <div class="center mt-3">
      <a class="btn btn--accent" href="focus-ecotourism.html#packages">See Package Pricing</a>
      <a class="btn btn--brand" href="mailto:infosl@aym-inc.org">Email to Book</a>
    </div>
  </div>
</section>
""" + CONTACT_CTA
page("focus-ecotourism-forest-safari.html", "Forest Safari",
     "A guided journey into Sierra Leone's forests with AYM ecotourism \u2014 wildlife, rivers and local guides.", SAFARI)

# ---- TECHNOLOGY ----
TECH = focus_hero(
  "Technology &amp; Digital Innovation",
  "Advance digital literacy, artificial intelligence, and technology-driven solutions.",
  "assets/img/tech-0.png",
  '<a class="btn btn--accent" href="contact.html">Share an Innovation</a><a class="btn btn--ghost" href="volunteer.html">Volunteer Technical Skills</a>'
) + f"""
<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">The Challenge</span>
      <h2>Connecting Mattru Jong to the Digital Economy</h2>
      <p class="lead">Rural communities are cut off from the digital economy. Without reliable internet and computer skills, youth cannot access education, jobs or markets. AYM's Project Mattru Jong is changing that.</p>
    </div>
    <div class="split__media"><img src="assets/img/tech-1.png" alt="Project Mattru Jong"></div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Our Approach</span><h2>Vision &amp; tech grants</h2></div>
    <div class="grid grid-3">
      <div class="feature"><h3>Founding Roots</h3><p class="muted">Technology has been core to AYM's model since its founding in 2000.</p></div>
      <div class="feature"><h3>Google Grants Integration</h3><p class="muted">We leverage nonprofit technology grants to fund our digital infrastructure.</p></div>
      <div class="feature"><h3>Distance Learning Delivery</h3><p class="muted">Broadband and devices that bring education to the last mile.</p></div>
    </div>
    <div class="grid grid-2 mt-3">
      <div class="feature"><h3>Micro-Donations &amp; Hardware</h3><p class="muted">Small gifts add up to computers, routers and solar power.</p></div>
      <div class="feature"><h3>Social Media &amp; Campaign Volunteers</h3><p class="muted">Remote volunteers power our outreach and digital campaigns.</p></div>
    </div>
  </div>
</section>
""" + sector_framework("technology") + CONTACT_CTA
page("focus-technology.html", "Technology &amp; Digital Innovation", "Advance digital literacy, artificial intelligence, and technology-driven solutions.", TECH)

print("entre/health/eco/tech done")

# ==========================================================================
# PAGE: PROJECTS
# ==========================================================================
PROJECTS = hero_page(
  "Our Work",
  "Ideas Into Action",
  "From grassroots community building to Pan-African intellectual dialogue—explore approved projects, their current status and the pillars behind AYM's work.",
  "assets/img/projects-0.png", "Our Work / Projects",
  actions='<a class="btn btn--accent" href="donate.html">Support Ongoing Projects</a>'
) + f"""
<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">Featured Initiative</span>
      <h2>African Youth Movement Lecture Series</h2>
      <p class="lead">A platform for dialogue connecting youth, leaders and thinkers across the continent and diaspora.</p>
      <div class="grid grid-1 mt-2">
        <div><h3>Online Webinars</h3><p class="muted">Expert-led sessions accessible from anywhere.</p></div>
        <div><h3>Interactive Q&amp;A</h3><p class="muted">Direct conversation with speakers and leaders.</p></div>
        <div><h3>In-Person Sessions (Later)</h3><p class="muted">Expanding to physical gatherings as the program grows.</p></div>
      </div>
    </div>
    <div class="split__media"><img src="assets/img/projects-1.png" alt="Lecture Series"></div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Current Projects</span><h2>Projects we're building now</h2></div>
    {cards_grid(CURRENT_PROJECTS, 2)}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Completed and Pillars</span><h2>Completed projects and foundations</h2></div>
    <div class="grid grid-4">
      <div class="feature"><h3>Global Perception &amp; Dialogue</h3><p class="muted">International exhibitions and conversations on Africa's image.</p></div>
      <div class="feature"><h3>Travelling Art</h3><p class="muted">Taking Sierra Leonean art to audiences abroad.</p></div>
      <div class="feature"><h3>Artist Appreciation Gala</h3><p class="muted">Celebrating and supporting local creative talent.</p></div>
      <div class="feature"><h3>Sierra Leone's Own Musical Talent</h3><p class="muted">Supported The Mixing Crew and the Young Sisters, whose first album was released in 2001.</p></div>
    </div>
    <div class="center mt-3"><a class="btn btn--outline" href="about.html">Learn More →</a></div>
  </div>
</section>
""" + CONTACT_CTA
page("projects.html", "Projects", "Explore AYM's projects, from the African Youth Movement Lecture Series to community enterprises.", PROJECTS, "projects")

# ==========================================================================
# PAGE: EVENTS
# ==========================================================================
EVENTS = hero_page(
  "Our Work",
  "Our Events &amp; <em>Global Initiatives</em>",
  "Virtual conferences, cultural exhibitions and gatherings that connect the movement worldwide.",
  "assets/img/events-0.png", "Our Work / Events",
  actions='<a class="btn btn--accent" href="contact.html">Register Interest</a>'
) + f"""
<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">Upcoming</span>
      <h2>Virtual Conference on Youth, Employment, and Righteous Rage</h2>
      <p class="lead">Our First Annual Virtual Conference brings together youth, employers, policymakers and activists to tackle youth unemployment across Africa.</p>
      <div class="tags mt-2">
        <span class="pill">Date: TBA</span><span class="pill">Location: Virtual / Zoom</span><span class="pill">Free Registration</span>
      </div>
      <p class="mt-2"><a class="btn btn--brand" href="contact.html">Contact Us</a></p>
    </div>
    <div class="split__media"><img src="assets/img/events-1.png" alt="Virtual conference"></div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section__head"><span class="eyebrow">Past Events</span><h2>Past Events &amp; Cultural Exhibitions</h2></div>
    {cards_grid([
      {"title":"Representations of Violence: Art about the Sierra Leone Civil War","tag":"Art","text":"An exhibition using 38 paintings to process and communicate the trauma of war.","cta":"Explore the Gallery","href":"projects.html","img":"assets/img/events-2.png"},
      {"title":"Masking Spirits Across the Seas","tag":"Art","text":"A cultural exhibition celebrating Sierra Leone's masking traditions.","cta":"View Exhibition","href":"projects.html","img":"assets/img/events-3.png"},
    ], 2)}
    <div class="card card--flat mt-3"><div class="card__body">
      <h3 class="card__title">Dates &amp; Locations</h3>
      <p class="card__text">Representations of Violence ran March 1–30, 2003. Exhibition archives are available on request.</p>
      <a class="card__link" href="contact.html">View Exhibition Archive →</a>
    </div></div>
  </div>
</section>
""" + CONTACT_CTA
page("events.html", "Events", "AYM events including the Virtual Conference on Youth, Employment, and Righteous Rage and cultural exhibitions.", EVENTS, "events")

# ==========================================================================
# PAGE: WHERE WE WORK
# ==========================================================================
WORK = hero_page(
  "Where We Work",
  "Global Coordination. <em>Local Operations.</em>",
  "Anchored in the United States for global support; rooted in Sierra Leone for community transformation.",
  "assets/img/work-0.png", "Our Work / Where We Work"
) + f"""
<section class="section">
  <div class="container split">
    <div>
      <span class="eyebrow">Primary Operational Hub</span>
      <h2>Sierra Leone</h2>
      <p class="lead">Our on-the-ground hub is in Mattru Jong, where AYM's Global Assembly and the Global Assembly of Founders Circle coordinate national and international programs.</p>
      <ul class="ticks">
        <li>GLASE partnership advancing local entrepreneurship.</li>
        <li>Staff grew from 7 to a growing team of employees.</li>
        <li>Youth enterprises from power services to agriculture.</li>
        <li>Continued community response, including support during the Ebola outbreak.</li>
      </ul>
    </div>
    <div class="split__media"><img src="assets/img/work-1.png" alt="Sierra Leone operations"></div>
  </div>
</section>

<section class="section section--cream">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">Grassroots Ventures</span><h2>Micro-enterprises building local livelihoods</h2></div>
    <div class="grid grid-2">
      <div class="feature"><h3>Power &amp; Charging Services</h3><p class="muted">Youth-run power and phone-charging micro-enterprises generating reliable income.</p></div>
      <div class="feature"><h3>Mattru Jong Collaboration</h3><p class="muted">Community-led enterprise and ecotourism activity connected to local priorities.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head center"><span class="eyebrow">The Mattru Jong Project</span><h2>Our goals for the site</h2></div>
    <div class="grid grid-3">
      <div class="feature"><h3>Social Enterprise &amp; Ecotourism Base</h3><p class="muted">An incubator for youth-led ventures and sustainable tourism.</p></div>
      <div class="feature"><h3>Educational &amp; Cultural Hub</h3><p class="muted">A center for training, learning and cultural exchange.</p></div>
      <div class="feature"><h3>Developing Land Along the Jong River</h3><p class="muted">Land-use plans for agriculture, enterprise and conservation under approved local arrangements.</p></div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="container split">
    <div>
      <span class="eyebrow" style="color:var(--brand)">United States</span>
      <h2>AYM in the United States</h2>
      <p class="lead" style="color:rgba(255,255,255,.85)">Incorporated in Wisconsin, our U.S. office provides the legal, fundraising and coordination backbone for chapters worldwide.</p>
    </div>
    <div>
      <h3 style="color:#fff">Chapter Responsibilities</h3>
      <div class="grid grid-1 mt-2">
        <div><h4 style="color:var(--brand)">Resource Mobilization</h4><p style="color:rgba(255,255,255,.8)">Raise funds and secure grants to power programs.</p></div>
        <div><h4 style="color:var(--brand)">Volunteer Management</h4><p style="color:rgba(255,255,255,.8)">Recruit, onboard and support local volunteers.</p></div>
        <div><h4 style="color:var(--brand)">Chapter Expansion</h4><p style="color:rgba(255,255,255,.8)">Grow the Pan-African network city by city.</p></div>
      </div>
    </div>
  </div>
</section>
""" + cta_trio() + CONTACT_CTA
page("where-we-work.html", "Where We Work", "AYM operates from Sierra Leone with a global coordination hub in the United States.", WORK, "work")

# ==========================================================================
# PAGE: SHARE YOUR STORY
# ==========================================================================
STORY_FORM_URL = "https://forms.gle/5ziFYCgoBE9tDStc9"
STORY_HERO_ACTION = (
  f'<a class="btn btn--accent btn--lg" href="{STORY_FORM_URL}" target="_blank" rel="noopener noreferrer">SHARE YOUR STORY</a>'
)
STORY_FORM_BLOCK = f"""
<section class="section section--cream">
  <div class="container split">
    <div>
      <span class="eyebrow">VOICES OF THE EMERGING AFRICA</span>
      <h2>Your Story. Your Voice. Your Africa.</h2>
      <p class="lead">Every experience has the power to inspire, educate, and create change. Share your journey, your challenges, your achievements, and your ideas with the world.</p>
      <p class="mt-2"><a class="btn btn--accent btn--lg" href="{STORY_FORM_URL}" target="_blank" rel="noopener noreferrer">SHARE YOUR STORY</a></p>
      <p class="small muted">The questionnaire opens in a new tab. It is the first step in sharing your story with VOE Africa.</p>
    </div>
    <div class="split__media"><img src="assets/img/aym-health-community.jpg" alt="Community members gathered together in Africa"></div>
  </div>
</section>

<section class="section" id="submit-story">
  <div class="container grid grid-2">
    <div>
      <span class="eyebrow">Share Your Story</span>
      <h2>Tell the world what Africa looks like through your eyes</h2>
      <p class="muted">VOE Africa welcomes stories from across the continent and diaspora?entrepreneurial journeys, community impact, creative work, challenges overcome, and ideas for Africa?s future.</p>
      <p class="mt-2"><a class="btn btn--accent btn--lg" href="{STORY_FORM_URL}" target="_blank" rel="noopener noreferrer">SHARE YOUR STORY</a></p>
      <div class="card card--flat mt-2">
        <div class="card__body">
          <h3 class="card__title">Before you submit</h3>
          <ul class="ticks">
            <li>Share only information you have the right to share.</li>
            <li>Do not include passwords, identity numbers, medical records, or other sensitive personal information.</li>
            <li>If your story includes other people, make sure you have their permission.</li>
            <li>Submitting the questionnaire does not automatically publish your story.</li>
          </ul>
        </div>
      </div>
    </div>
    <div>
      <h2>What happens next</h2>
      <div class="info mt-2">
        <div><strong>1. Review</strong><p class="muted">The AYM/VOE Africa team reviews submissions for clarity, accuracy, safeguarding, and fit with the movement?s mission.</p></div>
        <div><strong>2. Verification</strong><p class="muted">We may contact you to verify details, request context, or discuss how your story could be shared responsibly.</p></div>
        <div><strong>3. Separate permission</strong><p class="muted">If your story moves forward, AYM will request separate, clear approval before publication, distribution, or other use.</p></div>
      </div>
      <div class="card card--flat mt-2">
        <div class="card__body">
          <h3 class="card__title">Publishing framework</h3>
          <p class="card__text">The initial questionnaire supports content acquisition, global talent identification, and opportunity development. Before publication, AYM will integrate the Media Release Agreement, Editorial Standards, and safeguarding procedures. The Media Release Agreement will address editing, international distribution, copyright, platform monetization, compensation arrangements, and the use of a contributor?s name, image, and voice.</p>
        </div>
      </div>
      <div class="card card--flat mt-2">
        <div class="card__body">
          <h3 class="card__title">Need help?</h3>
          <p class="card__text">Use the WhatsApp button, AYM Assistant, or our <a href="contact.html">contact page</a> if you have questions before submitting your story.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

SHARE_STORY = hero_page(
  "VOICES OF THE EMERGING AFRICA",
  "Your Story. Your Voice. <em>Your Africa.</em>",
  "Every experience has the power to inspire, educate, and create change. Share your journey, your challenges, your achievements, and your ideas with the world.",
  "assets/img/aym-art-youth-creatives.jpg", "Get Involved / Share Your Story",
  actions=STORY_HERO_ACTION
) + STORY_FORM_BLOCK
page("share-your-story.html", "Share Your Story | Voices of the Emerging Africa", "Share your African story, entrepreneurial journey, achievements, challenges, and ideas with a global audience through VOE Africa.", SHARE_STORY, "story")

# PAGE: PRIVACY POLICY
# ==========================================================================
PRIVACY = hero_page(
  "Policies",
  "Privacy Policy",
  "How AYM handles information submitted through this website.",
  "assets/img/about-2.png", "Policies / Privacy"
) + f"""
<section class="section">
  <div class="container policy">
    <p class="lead">Last updated: 25 November 2026.</p>
    <p>The Twenty-First Century African Youth Movement, Inc. (AYM) respects your privacy. This summary explains what information this website may receive, how it is used and how you can ask questions about it.</p>

    <h2>Information we receive</h2>
    <ul>
      <li><strong>Information you provide:</strong> details you enter in contact, volunteer, story submission and other forms, such as your name, email, location, submitted text and consent choices.</li>
      <li><strong>Story submissions:</strong> information submitted through <a href="share-your-story.html">Share Your Story</a> and its questionnaire is treated as review material, not published content.</li>
      <li><strong>Browser storage:</strong> some features may use local browser storage to keep draft text or interface preferences on your device.</li>
      <li><strong>Service data:</strong> form and hosting providers may process technical information needed to deliver and secure the site.</li>
    </ul>

    <h2>How we use information</h2>
    <ul>
      <li>To respond to enquiries and review forms you submit.</li>
      <li>To verify story submissions and assess safeguarding permissions.</li>
      <li>To operate approved programs and keep records of consent where needed.</li>
      <li>To improve the website and protect it from misuse.</li>
      <li>To meet legal or governance requirements where applicable.</li>
    </ul>

    <h2>Sharing and service providers</h2>
    <p>AYM does not sell personal information. We may share limited information with service providers that help operate this site, such as form delivery, email, hosting and payment providers. Information may also be shared where required by law or where needed to protect people and property.</p>

    <h2>Stories and publication</h2>
    <p>Submitting a story or questionnaire through this website does not automatically publish it and does not grant AYM permission to publish. If a submission moves forward, AYM asks for separate, clear approval about how the story may be used, including any applicable Media Release Agreement, Editorial Standards, and safeguarding procedures. You may withdraw permission by contacting us, subject to material already published or shared under prior approval.</p>

    <h2>Children and safeguarding</h2>
    <p>We do not knowingly collect information from children through this website without appropriate parent or guardian involvement. The story form asks submitters to confirm their age or guardian permission and to confirm they have the right to share details about other people.</p>

    <h2>Retention and your choices</h2>
    <p>We keep information only for as long as it is needed for the purpose it was collected, unless a longer period is required for legal, safety or recordkeeping reasons. You may ask to access, correct or delete information you submitted by contacting <a href="mailto:info@aym-inc.org">info@aym-inc.org</a>.</p>

    <h2>Updates</h2>
    <p>We may update this page as our practices change. The date at the top shows the latest version.</p>

    <h2>Contact</h2>
    <p>Questions about this policy can be sent to <a href="mailto:info@aym-inc.org">info@aym-inc.org</a> or through our <a href="contact.html">contact page</a>. See also our <a href="terms.html">Terms of Use</a> and <a href="accessibility.html">Accessibility</a> pages.</p>
  </div>
</section>
"""
page("privacy.html", "Privacy Policy", "How AYM handles information submitted through this website.", PRIVACY, "policy")

# ==========================================================================
# PAGE: TERMS OF USE
# ==========================================================================
TERMS = hero_page(
  "Policies",
  "Terms of Use",
  "Plain-language terms for using this website and submitting material to AYM.",
  "assets/img/about-1.png", "Policies / Terms"
) + f"""
<section class="section">
  <div class="container policy">
    <p class="lead">Last updated: 25 November 2026.</p>
    <p>These terms explain the basic rules for using the AYM website. By using the site or submitting material, you agree to the points below.</p>

    <h2>Using this website</h2>
    <p>You may browse, share and link to pages on this site for lawful purposes. Do not use the site to harass people, spread false information, attempt unauthorized access, interfere with its operation or submit unlawful content.</p>

    <h2>Website content</h2>
    <p>Text, images, branding and other materials on this site belong to AYM or its contributors. You may quote or link to material with clear attribution, but do not present it as your own or imply endorsement without written permission.</p>

    <h2>Story submissions</h2>
    <ul>
      <li>You keep ownership of what you write.</li>
      <li>Sending a story through <a href="share-your-story.html">Share Your Story</a> or its questionnaire gives AYM permission to review it only.</li>
      <li>Nothing is published automatically, and no publication permission is assumed.</li>
      <li>If AYM wishes to use a story, it will ask for separate, clear approval first.</li>
      <li>You confirm that you have the right to share the material and any details about other people.</li>
    </ul>
    <p>Submissions that are incomplete, unsafe, defamatory, privacy-invasive or submitted without required safeguarding consent may not be reviewed further.</p>

    <h2>Donations and third-party services</h2>
    <p>Donations, purchases and form submissions may be handled by third-party providers. Their terms and privacy practices apply to those transactions. Details about giving are described on the <a href="donate.html">donate page</a>, and handling of submitted information is described in our <a href="privacy.html">Privacy Policy</a>.</p>

    <h2>Accuracy and availability</h2>
    <p>AYM aims to keep site information accurate and useful, but content may change or contain errors. The site is provided for general information and is not professional, legal, medical or financial advice.</p>

    <h2>Changes to these terms</h2>
    <p>We may update these terms to reflect changes to the site or our work. The date at the top shows the latest version.</p>

    <h2>Contact</h2>
    <p>Questions about these terms can be sent to <a href="mailto:info@aym-inc.org">info@aym-inc.org</a> or through our <a href="contact.html">contact page</a>.</p>
  </div>
</section>
"""
page("terms.html", "Terms of Use", "Plain-language terms for using this website and submitting material to AYM.", TERMS, "policy")

# ==========================================================================
# PAGE: ACCESSIBILITY
# ==========================================================================
ACCESSIBILITY = hero_page(
  "Policies",
  "Accessibility",
  "Our approach to making this website easier to use for more people.",
  "assets/img/contact-0.png", "Policies / Accessibility"
) + f"""
<section class="section">
  <div class="container policy">
    <p class="lead">Last updated: 25 November 2026.</p>
    <p>AYM wants this website to be usable by as many people as possible, including people who use keyboards, screen readers, magnification, captions or reduced motion settings.</p>

    <h2>Our approach</h2>
    <p>We aim to meet recognized web accessibility guidance, including WCAG 2.1 AA where practical. Accessibility is reviewed as pages are added and updated, rather than treated as a one-time task.</p>

    <h2>What we work on</h2>
    <ul>
      <li>Clear page structure, headings and descriptive link text.</li>
      <li>Keyboard access to navigation, forms and interactive controls.</li>
      <li>Visible focus styles and labels for form fields.</li>
      <li>Alternative text for meaningful images.</li>
      <li>Readable text, sufficient contrast and responsive layouts.</li>
      <li>Reduced motion options for animation and transitions where supported.</li>
      <li>Status messages for form outcomes where supported.</li>
    </ul>

    <h2>Known limitations</h2>
    <p>Some media, archived articles or embedded third-party content may not yet meet the same standard. If you find something difficult to use, we want to know so we can improve it.</p>

    <h2>Give feedback</h2>
    <p>If a page, form or feature is hard to access, email <a href="mailto:info@aym-inc.org">info@aym-inc.org</a> with the page address and a short description of the issue. You can also use our <a href="contact.html">contact page</a>.</p>

    <h2>Related policies</h2>
    <p>See our <a href="privacy.html">Privacy Policy</a> and <a href="terms.html">Terms of Use</a>.</p>
  </div>
</section>
"""
page("accessibility.html", "Accessibility", "AYM's approach to website accessibility and how to report an issue.", ACCESSIBILITY, "policy")

print("ALL PAGES DONE")

