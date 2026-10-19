"""Niigata: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/niigata_articles'
SKIP=set()
BAR_BACK='Ниигата на карте'
MAP_TITLE='Ниигата на карте'
ARIA='Карта префектуры Ниигата'
VIEW='[37.55,138.75],8'
INTRO='{places} из наших статей о префектуре Ниигата: искусство Этиго-Цумари, остров Садо, сакэ и пиво, лосось Мураками, металл Цубамэ и Сандзё, онсэны Уонумы и Мацуноямы, фейерверк Нагаоки, жадеит Итоигавы. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Ниигата'
LIST_LINK='все статьи о префектуре Ниигата'
TOP_VAR='NIIGATA_PINS'
# Shown on the prefecture page only: the older top-map pin cb-sado links to 05.
# (cb-kiyotsu, ~10 km off, was removed; 04's Tunnel of Light pin shows instead.)
TOP_SKIP={('05','Исторический памятник «Садо Киндзан»')}
# No MERGE: the same place in two articles keeps two pins (as Nara, Kyoto, Ishikawa); identical coordinates were spread ~25 m apart.

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 23 by Claude on 2026-10-19 (quality-checked the same day; prices and hours not checked yet)
 ("Этиго-Цумари",['01','02','03','04','14']),
 ("Садо и побережье",['05','06']),
 ("Уонума и Минамиуонума",['07','12','15','19']),
 ("Мураками и север",['08','13']),
 ("Цубамэ, Сандзё и Нагаока",['09','10','16']),
 ("Город Ниигата",['11','22','23']),
 ("Запад: Дзёэцу и Итоигава",['17','18']),
 ("История",['20','21']),
]
