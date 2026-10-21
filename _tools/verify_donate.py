import re
h = open(r'C:\Users\Toks\Documents\AYM\website\donate.html', encoding='utf-8').read()
print('method buttons:', len(re.findall(r'<button type="button" class="method', h)))
print('method panels:', len(re.findall(r'data-method-panel=', h)))
print('cta:', re.search(r'data-method-cta href="[^"]*">([^<]*)', h).group(1))
print('old every.org removed:', 'every.org' not in h)
print('old alt-ways removed:', 'Alternative ways to give' not in h)
print('names:', re.findall(r'data-name="([^"]+)"', h))
