"""Ehime: config for tools/pref_map_build.py. Pins come from pins_batch*.json in the source folder."""
SRC='~/Documents/miyabi_articles/ehime_articles'
SKIP=set()
BAR_BACK='Эхимэ на карте'
MAP_TITLE='Эхимэ на карте'
ARIA='Карта префектуры Эхимэ'
VIEW='[33.6,132.7],9'
INTRO='{places} из наших статей об Эхимэ: Увадзима и её праздник, острова Симанами, Дого-онсэн, Одзу, мыс Сада, отели и пивоварни. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи об Эхимэ'
LIST_LINK='все статьи об Эхимэ'
TOP_VAR='EHIME_PINS'

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('Рёкан «Кия»', None, [('02','Рёкан «Кия»'), ('09','Рёкан «Кия»')]),
]

def pins(A):
    return json_pins(SRC, A, MERGE)  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 12 does not exist (the Nakajima ecotour had ended)
 ("Увадзима",['01','02','03']),
 ("Острова Симанами",['04','05']),
 ("Города, архитектура и дороги",['06','07','08']),
 ("Онсэны, пиво и вкусы Эхимэ",['09','10','11','13']),
]
