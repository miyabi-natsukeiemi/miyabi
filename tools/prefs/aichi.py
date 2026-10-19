"""Aichi: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/aichi_articles'
SKIP=set()
BAR_BACK='Айти на карте'
MAP_TITLE='Айти на карте'
ARIA='Карта префектуры Айти'
VIEW='[35.0,137.15],9'
INTRO='{places} из наших статей о префектуре Айти: замки Инуяма и Киёсу, сибори Аримацу, керамика Сэто, сакэ «Кухэйдзи» и мирин Микавы, полуостров Ацуми, архитектура Нагои, Тоёты, Ханды и Итиномии, праздник в Цусиме, места трёх объединителей страны и их полководцев. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Айти'
LIST_LINK='все статьи о префектуре Айти'
TOP_VAR='AICHI_PINS'
# Shown on the prefecture page only: the older top-map pin cb2-inuyama (~0.9 km off, the same castle) links to 01.
# r2-arimatsu and r2-seto link to 02 and 04 but are town points, so those article pins stay on the top map.
TOP_SKIP={('01','Замок Инуяма')}
# No MERGE: the same place in two articles keeps two pins (Kiyosu castle in 06 and 30 is spread ~25 m apart).
# 08: the Sumiya Bunjiro pin was left out (no visits for individuals; Ren 2026-10-19).

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 30 by Claude on 2026-10-19 (quality-checked and photo-checked the same day; prices and hours not checked yet)
 ("Замки",['01','06']),
 ("Аримацу",['02','03']),
 ("Сэто",['04','05']),
 ("Нагоя: еда, сауна, сакэ",['07','12','13','14']),
 ("Ремёсла Айти",['22']),
 ("Полуостров Ацуми и Микава",['08','09','10','11','19']),
 ("Тоёта, Ханда, Итиномия",['15','16','20','21']),
 ("Цусима",['17','18']),
 ("Три объединителя",['23','24','25']),
 ("Полководцы Овари",['26','27','28','29','30']),
]
