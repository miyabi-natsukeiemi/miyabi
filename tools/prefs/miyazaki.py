"""Miyazaki: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/miyazaki_articles'
SKIP=set()
BAR_BACK='Миядзаки на карте'
MAP_TITLE='Миядзаки на карте'
ARIA='Карта префектуры Миядзаки'
VIEW='[32.2,131.4],9'
INTRO='{places} из наших статей о префектуре Миядзаки: остров Аосима и курганы Сайтобару, обеды поезда «36 плюс 3» и Такатихо, камааги-удон и карамэн города Миядзаки, рыбацкая кухня Нобэоки, джин и виски Osuzuyama. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Миядзаки'
LIST_LINK='все статьи о префектуре Миядзаки'
TOP_VAR='MIYAZAKI_PINS'
# Left off the maps (handover): Skal is an office, not a place to visit; Pappacarbone has no known address.
DROP={'Skal', 'Pappacarbone'}
# Shown on the prefecture page only: older top-map pins at these places link to 01 (ky-aoshima, r2-saitobaru).
TOP_SKIP={'Святилище Аосима', 'Курганы Сайтобару'}

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('Святилище Аосима', None, [('01','Святилище Аосима'), ('02','святилище Аосима')]),
]

def pins(A):
    return [p for p in json_pins(SRC, A, MERGE, pattern='pins_*.json') if p[0] not in DROP]  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 5 by Claude (prices and hours not checked yet)
 ("Аосима и город Миядзаки",['01','02','03']),
 ("Север префектуры (Нобэока, Такатихо, Кидзё)",['04','05']),
]
