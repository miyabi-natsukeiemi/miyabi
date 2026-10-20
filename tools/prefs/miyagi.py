"""Miyagi: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/miyagi_articles'
SKIP=set()
BAR_BACK='Мияги на карте'
MAP_TITLE='Мияги на карте'
ARIA='Карта префектуры Мияги'
VIEW='[38.35,140.95],9'
INTRO='{places} из наших статей о префектуре Мияги: Танабата в Сендае, онсэны Наруко и Акиу, сакура на реке Сироиси, станция Онагава, дизайн Исиномаки, устрицы Хигаси-Мацусимы, соевый соус Сиогамы, кухня Сендая. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Мияги'
LIST_LINK='все статьи о Мияги'
TOP_VAR='MIYAGI_PINS'
# Shown on the prefecture page only: the older top-map pin th-tanabata (~770 m) marks the same festival and links to 01.
# th2-naruko-onsen links to 02 (area point).
TOP_SKIP={('01','Праздник Танабата в Сендае')}

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 12 by Claude on 2026-10-20 (no 12: visits for business partners only; quality-checked and photo-checked the same day; prices and hours not checked yet)
 ("Сендай",['01','04','11','13']),
 ("Онсэны",['02','05','06']),
 ("Юг: сакура",['03']),
 ("Побережье: Онагава, Исиномаки, Мацусима, Сиогама",['07','08','09','10']),
]
