import os, re, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

OUT = r'C:\Users\Toks\Documents\AYM\website'
pages = sorted(glob.glob(os.path.join(OUT, '*.html')))
def read(n): return open(os.path.join(OUT, n), encoding='utf-8').read()

def anchors(html):
    return re.findall(r'<a\s+[^>]*href="([^"]*)"[^>]*>(.*?)</a>', html, re.S)

def text(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

print('=== 1. DONATE CTA routing (every link mentioning donate) ===')
bad = 0
for p in pages:
    h = read(p)
    for href, inner in anchors(h):
        t = text(inner)
        if re.search(r'donat', t, re.I) and not re.search(r'donate\.html|#give', href):
            if re.match(r'donate\b.*\bwith\b', t, re.I):
                continue  # the payment-method CTA is data-driven; href set by JS
            print(f'  {os.path.basename(p)}: "{t}" -> {href}')
            bad += 1
print('  violations:', bad)

print('=== 2. YouTube links ===')
seen = set()
for p in pages:
    for m in re.findall(r'href="(https?://[^"]*youtu[^"]*)"', read(p)):
        if m not in seen:
            seen.add(m); print('  ', m)

print('=== 3. Dead href="#" links (non-method) ===')
for p in pages:
    h = read(p)
    for href, inner in anchors(h):
        if href == '#' and not re.match(r'donate\b.*\bwith\b', text(inner), re.I):
            print(f'  {os.path.basename(p)}: "{text(inner)[:50]}"')

print('=== 4. "Click / Click here" link text ===')
hits = 0
for p in pages:
    for href, inner in anchors(read(p)):
        t = text(inner)
        if re.fullmatch(r'click(\s+here)?', t, re.I) or re.fullmatch(r'here', t, re.I):
            print(f'  {os.path.basename(p)}: "{t}" -> {href}'); hits += 1
print('  hits:', hits)

print('=== 5. Button casing (lowercase words that should be capitalised) ===')
ALLOW = {'a','an','the','of','to','and','in','your','with','for','at','by','our','we','per','on','is','as','into','over','it','its','from','or'}
flags = 0
for p in pages:
    h = read(p)
    for m in re.finditer(r'<a\s+[^>]*class="btn[^"]*"[^>]*>(.*?)</a>', h, re.S):
        t = text(m.group(1))
        words = t.replace('→', '').split()
        bad_w = [w for w in words[1:]
                 if (w[:1].islower() and w.lower() not in ALLOW) or
                    (w.islower() and w.lower() not in ALLOW)]
        if bad_w:
            print(f'  {os.path.basename(p)}: "{t}"  -> {bad_w}'); flags += 1
print('  flagged:', flags)

print('=== 6. Hero uses container (side margins) ===')
for p in pages:
    h = read(p)
    hero = h[h.find('<section class="hero'):h.find('</section>')]
    if hero and 'class="container hero__inner"' not in hero:
        print('  MISSING container:', os.path.basename(p))

print('=== 7. Founder link on About ===')
a = read('about.html')
print('  about -> about-team.html present:', 'about-team.html' in a)

print('=== 8. Volunteer: roles, filters, eligibility ===')
v = read('volunteer.html')
print('  role cards:', v.count('class="card" data-role='))
print('  filter UI:', bool(re.search(r'data-filter', v)))
print('  eligibility mention:', bool(re.search(r'eligib', v, re.I)))
print('  skills metadata:', 'Skills' in v)

print('=== 9. Ecotourism activity images ===')
e = read('focus-ecotourism.html')
acts = re.findall(r'<article class="card">(.*?)</article>', e, re.S)
print('  activity cards:', len(acts), '| with <img>:', sum(1 for c in acts if '<img' in c))

print('=== 10. Donate: areas linked + post-donation path ===')
d = read('donate.html')
print('  links to focus pages:', len(re.findall(r'focus-[\w-]+\.html', d)))
print('  post-donation/confirmation:', bool(re.search(r'receipt|confirmation|next step|after you', d, re.I)))
print('  hero amount picker:', 'hero-widget' in d or 'tier--sm' in d)

print('=== 11. Store dead links / load more ===')
s = read('store.html')
print('  Add to Cart buttons:', s.count('data-demo-msg'), '| href="#":', s.count('href="#"'))
print('  product cards:', s.count('data-role="'))

print('=== 12. Volunteer application form (multi-step) ===')
ap = read('volunteer-apply.html')
js = open(os.path.join(OUT, 'assets', 'js', 'main.js'), encoding='utf-8').read()
print('  steps:', len(re.findall(r'data-step="\d"', ap)))
print('  step indicators:', len(re.findall(r'data-step-indicator', ap)))
print('  required fields:', len(re.findall(r'\brequired\b', ap)))
print('  nav hooks (back/next/submit):',
      all(x in ap for x in ['data-apply-back', 'data-apply-next', 'data-apply-submit']))
print('  review + success panels:', 'data-review' in ap and 'data-apply-done' in ap)
print('  validation logic in JS:', 'validatePanel' in js)
print('  draft autosave in JS:', 'localStorage' in js)
print('  no external form action:', 'action=' not in ap)
print('  role cards link to apply:', read('volunteer.html').count('volunteer-apply.html'))
