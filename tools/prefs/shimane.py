"""Shimane: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/shimane_articles'
SKIP=set()
BAR_BACK='Симанэ на карте'
MAP_TITLE='Симанэ на карте'
ARIA='Карта префектуры Симанэ'
VIEW='[35.4,132.6],8'
INTRO='{places} из наших статей о Симанэ: святилище Идзумо-тайся, Мацуэ и озеро Синдзи, музей Адати, Ивами Гиндзан и Ивами-кагура, Цувано, острова Оки. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Симанэ'
LIST_LINK='все статьи о Симанэ'
TOP_VAR='SHIMANE_PINS'

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('Святилище Идзумо-тайся', None, [('01','Святилище Идзумо-тайся'), ('02','Святилище Идзумо-тайся')]),
    ('Музей Адати', None, [('04','Музей Адати'), ('11','Музей Адати')]),
    ('Рёкан «Саги-но-ю со»', None, [('11','«Саги-но-ю со»'), ('13','«Сагиною-со»')]),
    ('«Юномати кагурадэн»', None, [('17','«Юномати кагурадэн»'), ('19','«Юномати кагурадэн»')]),
]

def pins(A):
    return json_pins(SRC, A, MERGE, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 22 by Claude (prices and hours not checked yet)
 ("Идзумо",['01','02','03','10','12','13']),
 ("Мацуэ и озеро Синдзи",['05','06','07','08','09','15']),
 ("Восток",['04','11','14']),
 ("Ивами",['16','17','18','19']),
 ("Оки",['20','21','22']),
]
