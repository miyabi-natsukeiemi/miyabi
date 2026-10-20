"""Fukushima: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/fukushima_articles'
SKIP=set()
BAR_BACK='Фукусима на карте'
MAP_TITLE='Фукусима на карте'
ARIA='Карта префектуры Фукусима'
VIEW='[37.45,140.3],8'
INTRO='{places} из наших статей о префектуре Фукусима: сладость «Акабэко» Айдзу, дорога Бандай-Адзума и горнолыжный курорт у Бандай, линия Тадами, сакура через 15 лет после 2011 года, онсэны Такаю и Дакэ, утварь Оку-Айдзу, дарума Сиракавы, ресторан HAGI в Иваки, Одака и сауна в Минамисоме. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Фукусиме'
LIST_LINK='все статьи о Фукусиме'
TOP_VAR='FUKUSHIMA_PINS'
# Shown on the prefecture page only: the older top-map pin th-tsurugajo marks the same castle and links to 05.
# th-ouchijuku stood ~14 km off and was removed (08's Ouchi-juku pin shows instead); th2-bandai links to 15.
# Takayu onsen keeps two pins (02 and 06, Ren).
TOP_SKIP={('05','Замок Цуругадзё')}

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 13 by Claude on 2026-10-21 (no 10, 12: nowhere to visit; quality-checked and photo-checked the same day; prices and hours not checked yet)
 ("Айдзу",['01','08','15']),
 ("Горы Адзума и город Фукусима",['02','06']),
 ("Юг Айдзу и линия Тадами",['03','04']),
 ("Сакура",['05']),
 ("Накадори: Нихоммацу и Сиракава",['07','09']),
 ("Побережье: Иваки и Минамисома",['11','13','14']),
]
