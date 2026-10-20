"""Akita: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/akita_articles'
SKIP=set()
BAR_BACK='Акита на карте'
MAP_TITLE='Акита на карте'
ARIA='Карта префектуры Акита'
VIEW='[39.75,140.2],9'
INTRO='{places} из наших статей о префектуре Акита: фестивали Канто и намахагэ, сакура Какунодатэ, фейерверк в Омагари, онсэны Нюто, сакэ Оги, мисо Юдзавы, музей в Аките, линия Гоно. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи об Аките'
LIST_LINK='все статьи об Аките'
TOP_VAR='AKITA_PINS'
# Older top-map pins: th-kanto and th-kakunodate were removed (01 and 02 have pins there); th6-akita-samurai and th2-oga link to 02 and 03.

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 13 by Claude on 2026-10-20 (no 05: no shop or tours; quality-checked and photo-checked the same day; prices and hours not checked yet)
 ("Праздники",['01','03','07','08']),
 ("Город Акита",['10','12']),
 ("Ога и побережье",['04','13','14']),
 ("Какунодатэ и онсэны",['02','09']),
 ("Ремёсла и вкусы",['06','11']),
]
