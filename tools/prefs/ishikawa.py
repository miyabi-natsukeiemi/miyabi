"""Ishikawa: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/ishikawa_articles'
SKIP=set()
BAR_BACK='Исикава на карте'
MAP_TITLE='Исикава на карте'
ARIA='Карта префектуры Исикава'
VIEW='[36.75,136.75],9'
INTRO='{places} из наших статей о префектуре Исикава: Канадзава и её музеи, сладости и кухня Кага, полуостров Ното после землетрясения 2024 года и его лак Вадзима-нури, онсэны Кага, ремёсла и сакэ Комацу, гора Хакусан. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Исикава'
LIST_LINK='все статьи о префектуре Исикава'
TOP_VAR='ISHIKAWA_PINS'
# Shown on the prefecture page only: the older top-map pin r2-abare-matsuri links to 01;
# Natadera is shown on the top map once, from 22 (r2-natadera, ~10 km off, was removed).
TOP_SKIP={'Фестиваль Абарэ', ('26','Храм Натадэра')}
# No MERGE: the same place in two articles keeps two pins (as Nara, Kyoto); identical coordinates were spread ~25 m apart.

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 29 by Claude on 2026-10-17 (prices and hours not checked yet)
 ("Полуостров Ното",['01','02','03','04','05','06','07','08']),
 ("Лак Вадзимы",['09','10','11']),
 ("Канадзава и Кахоку",['12','13','14','15','16','17','18','19','20']),
 ("Онсэны Кага",['21','22','23']),
 ("Комацу",['24','25','26','27']),
 ("Хакусан",['28','29']),
]
