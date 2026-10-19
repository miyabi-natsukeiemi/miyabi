"""Gifu: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/gifu_articles'
SKIP=set()
BAR_BACK='Гифу на карте'
MAP_TITLE='Гифу на карте'
ARIA='Карта префектуры Гифу'
VIEW='[35.8,137.0],9'
INTRO='{places} из наших статей о префектуре Гифу: замок Гифу и Сэкигахара, танцы Гудзё-одори, Хида-Такаяма, мингэй и резьба по дереву, онсэны Окухиды, Накасэндо, ножи Хасимы, плитка Тадзими. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Гифу'
LIST_LINK='все статьи о префектуре Гифу'
TOP_VAR='GIFU_PINS'
# Shown on the prefecture page only: the older top-map pins r2-gifucastle and cb2-gujo-hachiman link to 01 and 02.
TOP_SKIP={('01','Замок Гифу'), ('02','Гудзё-одори')}
# No MERGE: the same place in two articles keeps two pins (as Nara, Kyoto, Ishikawa).

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 24 by Claude on 2026-10-19 (quality-checked the same day; prices and hours not checked yet)
 ("Город Гифу и Мино",['01','14','15','16']),
 ("Гудзё",['02']),
 ("Хида-Такаяма и Фурукава",['03','04','05','06','07','08','09','21']),
 ("Окухида",['10','11']),
 ("Юг: Хасима, Огаки, Сэкигахара",['12','17','19','20']),
 ("Восточное Мино",['13','18']),
 ("История",['22','23','24']),
]
