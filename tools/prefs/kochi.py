"""Kochi: config for tools/pref_map_build.py. Pins come from pins_batch*.json in the source folder."""
import os, json, glob, math
SRC='~/Documents/miyabi_articles/kochi_articles'
SKIP=set()
BAR_BACK='Коти на карте'
MAP_TITLE='Коти на карте'
ARIA='Карта префектуры Коти'
VIEW='[33.5,133.5],9'
INTRO='{places} из наших статей о Коти: замок и рынок в городе, река Симанто, мыс Мурото, горные посёлки, мастерские и гостиницы. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Коти'
LIST_LINK='все статьи о Коти'
TOP_VAR='KOCHI_PINS'

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...])
MERGE=[
    ('Отель hotel nansui', None, [('21','Отель hotel nansui'), ('04','Окякуба при отеле hotel nansui')]),
    ('Рёкан «Кагэцу»', 'Мурото', [('06','Рёкан «Кагэцу»'), ('10','Рётэй Кагэцу')]),
    ('Гора Ёкогура', None, [('12','Гора Ёкогура'), ('14','Гора Ёкогура')]),
    ('Музей природы «Ёкогураяма»', None, [('12','Музей природы Ёкогураяма'), ('14','Музей природы «Ёкогураяма»')]),
]

def pins(A):
    src=os.path.expanduser(SRC); raw=[]
    for f in sorted(glob.glob(os.path.join(src,'pins_batch*.json'))):
        raw+=json.load(open(f,encoding='utf-8'))
    out=[]; seen={}
    def key(p): return (p['article'][:2], p['name_ru'])
    merged={k:m for m in MERGE for k in m[2]}
    for p in raw:
        k=key(p)
        if k in seen:  # same article, same place in another batch
            continue
        m=merged.get(k)
        if m:
            if m[0] in seen: continue
            group=[q for q in raw if key(q) in m[2]]
            exact=[q for q in group if not q['approx']] or group
            base=exact[0]
            pin=[m[0], m[1] or base['area_ru'], base['category'], base['lat'], base['lng'], 1 if all(q['approx'] for q in group) else 0,
                 A(*[n for n,_ in m[2]])]
            seen[m[0]]=pin; out.append(pin); continue
        pin=[p['name_ru'], p['area_ru'], p['category'], p['lat'], p['lng'], int(p['approx']), A(p['article'][:2])]
        seen[k]=pin; out.append(pin)
    # Different places that share placeholder coordinates (all approx=1): spread them ~150 m around the point,
    # otherwise only the top one can be clicked on the Leaflet map.
    by={}
    for p in out: by.setdefault((round(p[3],4),round(p[4],4)),[]).append(p)
    for g in by.values():
        if len(g)<2: continue
        for i,p in enumerate(g):
            a=2*math.pi*i/len(g)
            p[3]=round(p[3]+0.0014*math.sin(a),6); p[4]=round(p[4]+0.0016*math.cos(a),6)
    return out

GROUPS=[
 ("Город Коти и ёсакой",['01','05','06','15']),
 ("Вкус Коти и застолье",['03','04']),
 ("Реки, озёра и побережье",['02','07','10','11']),
 ("Горные дороги и лесная железная дорога",['08','09','12','17']),
 ("Ботаник Томитаро Макино",['13','14']),
 ("Деревни, вера и люди",['16','18','19']),
 ("Где остановиться",['20','21']),
]
