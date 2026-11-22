"""Search index for the site: assets/search-index.json.

Reads only this repo: the article data on the top page (window.<PREF>_PINS in index.html: titles, leads, thumbs, pins with
place names, areas and categories) and the article lists of the prefecture guides (articles/<pref>/index.html, the
<!-- <pref>-articles --> block: the group heading of every article). The site's JavaScript (assets/search.js) does the
matching, including spelling variants (Нисеко / Нисэко / Niseko), so the index holds plain text only.

Run from the repo root: python3 tools/search_build.py  (pref_map_build.py runs it too). Idempotent.
"""
import os, re, json, html, importlib.util

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, 'assets', 'search-index.json')
CAT_RU = {'see': 'Посмотреть', 'stay': 'Где остановиться', 'eat': 'Поесть', 'shop': 'Купить',
          'art': 'История и искусство', 'craft': 'Ремёсла и опыт'}


def text(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()


def short(s, n=140):
    s = re.sub(r'\s+', ' ', s or '').strip()
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0].rstrip(' ,.;:—') + '…'


def build():
    top = open(os.path.join(REPO, 'index.html'), encoding='utf-8').read()
    m = re.search(r'var PREF_RU = (\{.*?\});', top)
    pref_ru = {int(k): v for k, v in re.findall(r"(\d+):'([^']+)'", m.group(1))}
    code = {v: int(c) for v, c in re.findall(r'\[window\.([A-Z]+)_PINS, (\d+),', top)}
    sets = {v: json.loads(d) for v, d in re.findall(r'window\.([A-Z]+)_PINS=(\{.*?\});</script>', top)}
    keys = {}
    for f in sorted(os.listdir(os.path.join(REPO, 'tools', 'prefs'))):
        if f.endswith('.py'):
            m = re.search(r"^TOP_VAR\s*=\s*'([A-Z]+)_PINS'", open(os.path.join(REPO, 'tools', 'prefs', f), encoding='utf-8').read(), re.M)
            if m: keys[m.group(1)] = f[:-3]
    entries, prefs = [], []
    for var, d in sets.items():
        key, pc = keys[var], code[var]
        guide = open(os.path.join(REPO, 'articles', key, 'index.html'), encoding='utf-8').read()
        group = {}
        for g, body in re.findall(r'<div class="kg-group"><h4>(.*?)</h4><ul>(.*?)</ul>', guide, re.S):
            for s in re.findall(r'<a href="([^"/]+)/index\.html"', body):
                group.setdefault(s, text(g))
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', guide, re.S)
        prefs.append({'p': pc, 'k': key, 'n': pref_ru[pc]})
        entries.append({'k': 'g', 'p': pc, 't': text(h1.group(1)) if h1 else pref_ru[pc], 'u': f'/articles/{key}/index.html',
                        'i': f'/articles/{key}/thumb.jpg' if os.path.exists(os.path.join(REPO, 'articles', key, 'thumb.jpg')) else ''})
        by_art = {}
        for p in d['pins']:
            for s in p['s']:
                by_art.setdefault(s, []).append(p)
        for s, a in d['art'].items():
            ps = by_art.get(s, [])
            cats = []
            for p in ps:
                if p['c'] in CAT_RU and p['c'] not in cats: cats.append(p['c'])
            places = []
            for p in ps:
                for x in (p['n'], p['a']):
                    if x and x not in places: places.append(x)
            entries.append({'k': 'a', 'p': pc, 's': s, 't': a['t'], 'u': '/' + a['u'], 'i': '/' + a['i'] if a.get('i') else '',
                            'l': short(a.get('l', '')), 'g': group.get(s, ''), 'c': cats, 'x': places})
    prefs.sort(key=lambda p: p['p'])
    entries.sort(key=lambda e: (e['p'], e['k'] != 'g'))
    data = {'cats': CAT_RU, 'prefs': prefs, 'items': entries}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    return sum(1 for e in entries if e['k'] == 'a')


if __name__ == '__main__':
    print('search-index.json:', build(), 'articles')
