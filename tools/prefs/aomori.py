"""Aomori: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/aomori_articles'
SKIP=set()
BAR_BACK='Аомори на карте'
MAP_TITLE='Аомори на карте'
ARIA='Карта префектуры Аомори'
VIEW='[40.65,140.75],9'
INTRO='{places} из наших статей о префектуре Аомори: фестивали нэбута и нэпута, сакура в Хиросаки, ущелье Ойрасэ и озеро Товада, онсэны Хаккоды, леса Сираками, музеи современного искусства, сладости и поезд с печкой. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи об Аомори'
LIST_LINK='все статьи об Аомори'
TOP_VAR='AOMORI_PINS'
# Shown on the prefecture page only: the older top-map pins th-nebuta (~430 m) and th-hirosaki (~60 m) mark the same
# places and link to 01 and 03. th-oirase and th2-shirakami link to 09 and 12 (area points).
TOP_SKIP={('01','Фестиваль Нэбута в Аомори'), ('03','Парк Хиросаки')}

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 19 by Claude on 2026-10-20 (no 06: nowhere to visit; quality-checked and photo-checked the same day; prices and hours not checked yet)
 ("Фестивали",['01','02','14']),
 ("Хиросаки",['03','04','05','07']),
 ("Ойрасэ, Товада и Хаккода",['08','09','10','11','15']),
 ("Север Цугару и Сираками",['12','16','17']),
 ("Музеи и дизайн",['13','18','19','20']),
]
