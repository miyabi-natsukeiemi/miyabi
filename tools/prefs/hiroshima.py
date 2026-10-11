"""Hiroshima: config for tools/pref_map_build.py. Pins come from pins_batch*.json in the source folder."""
SRC='~/Documents/miyabi_articles/hiroshima_articles'
SKIP=set()
BAR_BACK='Хиросима на карте'
MAP_TITLE='Хиросима на карте'
ARIA='Карта префектуры Хиросима'
VIEW='[34.45,132.75],9'
INTRO='{places} из наших статей о Хиросиме: Миядзима и святилище Ицукусима, Ономити и острова Сэтоути, рёканы у моря, сакэ, мебель и деним, сладости, история рода Мори. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Хиросиме'
LIST_LINK='все статьи о Хиросиме'
TOP_VAR='HIROSHIMA_PINS'

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('Святилище Ицукусима', None, [('01','Святилище Ицукусима'), ('22','Святилище Ицукусима')], ('01','Святилище Ицукусима')),
]

def pins(A):
    return json_pins(SRC, A, MERGE)  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 18 does not exist (the bakery closed in 2022)
 ("Миядзима и западное побережье",['01','02','03','04','05']),
 ("Ономити, Сэтода и море",['06','07','08','21','23']),
 ("Восток префектуры",['09','10','11']),
 ("Ремёсла и вкусы",['12','13','14','15','16','17']),
 ("Город Хиросима и история",['19','20','22']),
]
