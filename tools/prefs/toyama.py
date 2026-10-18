"""Toyama: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/toyama_articles'
SKIP=set()
BAR_BACK='Тояма на карте'
MAP_TITLE='Тояма на карте'
ARIA='Карта префектуры Тояма'
VIEW='[36.65,137.25],9'
INTRO='{places} из наших статей о префектуре Тояма: гора Татэяма и ущелье Куробэ, рыба залива Тояма, суши и комбу, сакэ Ивасэ, «Овара кадзэ-но бон» в Яцуо, литьё и ремёсла Такаоки, отели среди рисовых полей Тонами и Тоги. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Тояма'
LIST_LINK='все статьи о префектуре Тояма'
TOP_VAR='TOYAMA_PINS'
# Shown on the prefecture page only: the older top-map pin cb-amaharashi (same place) links to 18.
TOP_SKIP={'Побережье Амахараси'}
# No MERGE: the same place in two articles keeps two pins (as Nara, Kyoto, Ishikawa); identical coordinates were spread ~25 m apart.

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 23 by Claude on 2026-10-17 (prices and hours not checked yet)
 ("Татэяма и горы",['01','19']),
 ("Залив Тояма и его рыба",['02','03','04','05','06']),
 ("Сакэ",['07']),
 ("Ущелье Куробэ",['09']),
 ("Город Тояма и Яцуо",['08','20']),
 ("Такаока, город ремёсел",['10','11','12','13','14','15']),
 ("Тонами и Нанто",['16','17','23']),
 ("Хими",['18']),
 ("Сладости",['21','22']),
]
