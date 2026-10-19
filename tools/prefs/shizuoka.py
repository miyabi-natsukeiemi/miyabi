"""Shizuoka: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/shizuoka_articles'
SKIP=set()
BAR_BACK='Сидзуока на карте'
MAP_TITLE='Сидзуока на карте'
ARIA='Карта префектуры Сидзуока'
VIEW='[34.95,138.45],9'
INTRO='{places} из наших статей о префектуре Сидзуока: рёканы Атами и Идзу, Сюдзэндзи, Западный Идзу, город Сидзуока и его кухня, театр SPAC, чай Рёгоути и Макинохары, железная дорога Oigawa, глубоководная рыба Нумадзу, святилище у подножия Фудзи. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Сидзуока'
LIST_LINK='все статьи о префектуре Сидзуока'
TOP_VAR='SHIZUOKA_PINS'
# No TOP_SKIP: the older top-map pins cb-atami, cb2-izu-onsen and cb7-shizuoka-nihondaira link to 01, 04 and 14
# but stand ~1 km from the article pins (town points), so the article pins stay on the top map too (as Nagano).
# No MERGE: the same place in two articles keeps two pins (as Nara, Kyoto, Ishikawa); identical coordinates were spread ~25 m apart.

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 30 by Claude on 2026-10-19 (no 27: the Vangi museum closed in 2023; quality-checked the same day; prices and hours not checked yet)
 ("Атами",['01','02','03']),
 ("Сюдзэндзи, Ито и Кавадзу",['04','05','06','08','09','13']),
 ("Западный и южный Идзу",['07','10','11','12']),
 ("Город Сидзуока",['14','17','18','19','20','22','23','24','28']),
 ("Нумадзу, Фудзи и Готэмба",['26','29','31']),
 ("Оигава, Яидзу, Хамамацу",['15','16','21','30']),
 ("История",['25']),
]
