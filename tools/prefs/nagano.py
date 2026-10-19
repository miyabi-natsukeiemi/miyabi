"""Nagano: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/nagano_articles'
SKIP=set()
BAR_BACK='Нагано на карте'
MAP_TITLE='Нагано на карте'
ARIA='Карта префектуры Нагано'
VIEW='[36.2,138.1],8'
INTRO='{places} из наших статей о префектуре Нагано: отели и рестораны Каруидзавы, онсэн Асама и сладости Мацумото, Обусэ, Хакуба и Нодзава онсэн, вино долины Тикума, Татэсина и плато Яцугатакэ, род Санада. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Нагано'
LIST_LINK='все статьи о префектуре Нагано'
TOP_VAR='NAGANO_PINS'
# No TOP_SKIP: the older top-map pins cb-karuizawa, cb2-obuse, cb3-hakuba and cb9-nagano-togakushi link to 01, 18, 20, 21
# but stand at other points (town centres), so the article pins stay on the top map too.
# No MERGE: the same place in two articles keeps two pins (as Nara, Kyoto, Ishikawa); identical coordinates were spread ~25 m apart.

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 42 by Claude on 2026-10-19 (quality-checked the same day; prices and hours not checked yet)
 ("Каруидзава",['01','02','03','04','05','06','07','08']),
 ("Мацумото",['09','10','11','12','13','14','15','16','17','25']),
 ("Север: Обусэ, Нагано, Тогакуси",['18','21','30','34','35']),
 ("Хакуба и Омати",['19','20','26','29']),
 ("Нодзава, Сига Когэн, Иияма",['22','23','24','28']),
 ("Вино и Тикума",['27','37','41','42']),
 ("Татэсина, Тино, Venus Line",['31','32','33','36','38']),
 ("Юг: Симогури",['39']),
 ("История",['40']),
]
