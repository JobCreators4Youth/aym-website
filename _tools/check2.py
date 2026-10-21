import os, glob
OUT = r'C:\Users\Toks\Documents\AYM\website'
css = open(os.path.join(OUT, 'assets/css/styles.css'), encoding='utf-8').read()
print('css braces:', css.count('{'), css.count('}'))
ok = True
for p in sorted(glob.glob(os.path.join(OUT, '*.html'))):
    h = open(p, encoding='utf-8').read()
    name = os.path.basename(p)
    problems = []
    if '<header class="site-header">' not in h: problems.append('no header')
    if 'site-footer' not in h: problems.append('no footer')
    if '</html>' not in h: problems.append('no </html>')
    if h.count('<main') != 1: problems.append('main count')
    if '<title>' not in h: problems.append('no title')
    if problems:
        ok = False
        print(name, '->', problems)
print('all good' if ok else 'ISSUES FOUND')
