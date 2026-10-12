"""Hyogo: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/hyogo_articles'
SKIP=set()
BAR_BACK='Хёго на карте'
MAP_TITLE='Хёго на карте'
ARIA='Карта префектуры Хёго'
VIEW='[34.9,134.9],8'
INTRO='{places} из наших статей о Хёго: замок Химэдзи, Кобе и квартал Китано, онсэны Киносаки и Арима, остров Авадзи, Мики и Тацуно. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Хёго'
LIST_LINK='все статьи о Хёго'
TOP_VAR='HYOGO_PINS'

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('Замок Химэдзи', None, [('01','Замок Химэдзи'), ('02','Замок Химэдзи')]),
]

def pins(A):
    return json_pins(SRC, A, MERGE, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 22 by Claude (prices and hours not checked yet)
 ("Харима",['01','02','03','04','05','10']),
 ("Тадзима",['06','08']),
 ("Тамба",['09']),
 ("Кобе",['11','13','14','16','17','22']),
 ("Арима и Хансин",['07','12','15']),
 ("Авадзи",['18','19','20','21']),
]
