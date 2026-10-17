"""Nara: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/nara_articles'
SKIP=set()
BAR_BACK='Нара на карте'
MAP_TITLE='Нара на карте'
ARIA='Карта префектуры Нара'
VIEW='[34.45,135.85],9'
INTRO='{places} из наших статей о префектуре Нара: Асука и принц Сётоку, гора Ёсино, парк Нара и квартал Нарамати, гора Мива и сакэ, Госэ, Тэнри и дорога Яманобэ-но мити, отели и рёканы, онсэны Тоцукава. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Нара'
LIST_LINK='все статьи о префектуре Нара'
TOP_VAR='NARA_PINS'
# Shown on the prefecture page only: the older top-map pin kn-yoshino (about 700 m away) links to 02.
TOP_SKIP={'Храм Кимпусэн-дзи'}
# No MERGE: the same place in two articles keeps two pins (Ren, 2026-10-17); identical coordinates were spread ~25 m apart.

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 37 by Claude on 2026-10-17 (prices and hours not checked yet)
 ("Город Нара",['04','05','06','12','17','18','24','25','26','27','28','29','31','34']),
 ("Асука, Касихара и юг равнины",['01','11','13','16','33']),
 ("Мива, Тэнри и Сакураи",['07','10','19','20','21','30']),
 ("Хорюдзи и запад",['03','14','36']),
 ("Госэ",['08','09']),
 ("Ёсино и горы",['02','23','35']),
 ("Деревни востока (Ямадзоэ, Сони)",['22','32']),
 ("История",['15']),
 ("Еда и сладости",['37']),
]
