"""Kanagawa: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/kanagawa_articles'
SKIP=set()
BAR_BACK='Канагава на карте'
MAP_TITLE='Канагава на карте'
ARIA='Карта префектуры Канагава'
VIEW='[35.4,139.4],9'
INTRO='{places} из наших статей о префектуре Канагава: замок Одавара и обсерватория Сугимото, Югавара и Манадзуру, гора Ояма, отели и рестораны Ёкогамы, Сёнан и Камакура, Хаяма и Миура, онсэны и музеи Хаконэ. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Канагаве'
LIST_LINK='все статьи о Канагаве'
TOP_VAR='KANAGAWA_PINS'
# Older top-map pins linked via url: kt7-kanagawa-odawara (01), kt4-oyama (02); the other 13 are left as they are (Ren, 2026-10-23).
TOP_SKIP={('01','Замок Одавара')}

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 46 by Claude on 2026-10-23 (no 05, 31, 33, 35; quality-checked and photo-checked; prices and hours not checked yet)
 ("Одавара и Югавара",['01','03','04','06','07','08']),
 ("Ояма и центр",['02','22','23','24']),
 ("Ёкогама и Кавасаки",['09','10','11','12','13','14','15','16','17','18','19','20','21']),
 ("Сёнан и Камакура",['25','26','27','28','29','30','32']),
 ("Хаяма, Дзуси, Ёкосука, Миура",['34','36','37','38','39','40','41','42']),
 ("Хаконэ",['43','44','45','46','47','48','49','50']),
]
