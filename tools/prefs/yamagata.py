"""Yamagata: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/yamagata_articles'
SKIP=set()
BAR_BACK='Ямагата на карте'
MAP_TITLE='Ямагата на карте'
ARIA='Карта префектуры Ямагата'
VIEW='[38.5,140.1],8'
INTRO='{places} из наших статей о префектуре Ямагата: резиденция Уэсуги в Ёнэдзаве, закусочные Цуруоки и отель среди рисовых полей, паломничество Могами, онсэн Каминояма, мебель и сёги Тэндо, ковры и керамика, остров Тобисима, сауны Нисикавы. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Ямагате'
LIST_LINK='все статьи о Ямагате'
TOP_VAR='YAMAGATA_PINS'
# Older top-map pins are left as they are; none marks the same place as an article pin (Ren, 2026-10-21).

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 15 by Claude on 2026-10-20/21 (no 02, 17, 18: nowhere to visit; quality-checked and photo-checked 2026-10-21; prices and hours not checked yet)
 ("Ёнэдзава",['01','09','13']),
 ("Цуруока, Сёнай и Тобисима",['03','04','15']),
 ("Город Ямагата и Каминояма",['06','10','11','12','14']),
 ("Тэндо",['07','08']),
 ("Могами и Нисикава",['05','16']),
]
