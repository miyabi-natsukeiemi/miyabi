"""Saga: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/saga_articles'
SKIP=set()
BAR_BACK='Сага на карте'
MAP_TITLE='Сага на карте'
ARIA='Карта префектуры Сага'
VIEW='[33.3,130.05],10'
INTRO='{places} из наших статей о префектуре Сага: Карацу и замок Нагоя, фарфор Ариты и Хидзэн-Ёсиды, онсэны Такэо и Уресино, чай Уресино, сакэ Касимы. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Сага'
LIST_LINK='все статьи о префектуре Сага'
TOP_VAR='SAGA_PINS'
# Outside the prefecture (article 14 also mentions two places in Kyoto): left off the maps, kept in the article.
DROP={'святилище Кифунэ','храм Сэйсин-ин'}
# Shown on the prefecture page only: the top map already has this place (cs5-saga-yutoku, linked to 06 via url).
TOP_SKIP={'святилище Ютоку Инари'}

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('Wataya Besso', None, [('08','Wataya Besso'), ('09','Wataya Besso'), ('09','Pierre Hermé Paris Café')]),
    ('Nakashima Farm', None, [('12','Nakashima Farm'), ('13','Nakashima Farm')]),
    ('Onyado Fukuchiyo и Souan Nabeshima', None, [('06','Onyado Fukuchiyo'), ('06','Souan Nabeshima')]),
]

def pins(A):
    return [p for p in json_pins(SRC, A, MERGE, pattern='pins_*.json') if p[0] not in DROP]  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 14 by Claude (prices and hours not checked yet)
 ("Карацу и Нагоя",['01','02','03','04']),
 ("Арита",['05']),
 ("Такэо и Касима",['06','07']),
 ("Уресино и Сиота",['08','09','10','11','12','14']),
 ("Город Сага",['13']),
]
