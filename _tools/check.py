import os, re, glob
OUT = r'C:\Users\Toks\Documents\AYM\website'
pages = [os.path.basename(p) for p in glob.glob(os.path.join(OUT, '*.html'))]
print('PAGES:', len(pages))
missing = set()
for p in pages:
    html = open(os.path.join(OUT, p), encoding='utf-8').read()
    for m in re.findall(r'(?:href|src)="([^"]+)"', html):
        if m.startswith(('http', 'mailto', '#', 'tel:')):
            continue
        path = m.split('#')[0]
        if not path:
            continue
        if not os.path.exists(os.path.join(OUT, path)):
            missing.add((p, m))
print('MISSING refs:')
for p, m in sorted(missing):
    print('  ', p, '->', m)
print('total missing', len(missing))
