"""Mie: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/mie_articles'
SKIP=set()
BAR_BACK='Миэ на карте'
MAP_TITLE='Миэ на карте'
ARIA='Карта префектуры Миэ'
VIEW='[34.6,136.5],9'
INTRO='{places} из наших статей о префектуре Миэ: святилище Исэ и улица Окагэ-ёкотё, отели Исэ-Сима, острова у Тобы, тропа Кумано-кодо, донабэ из Иги, Кувана, онсэны Юнояма и Сакакибара. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Миэ'
LIST_LINK='все статьи о префектуре Миэ'
TOP_VAR='MIE_PINS'
# The older top-map pin cb-ise was replaced by 01's inner-shrine pin (Ren, 2026-10-17).

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('Музей Дзингу Тёкокан', None, [('02','Музей Дзингу Тёкокан'), ('15','Музей Дзингу Тёкокан')], ('02','Музей Дзингу Тёкокан')),
    ('Рёкан «Асакити»', None, [('06','Рёкан Асакити'), ('15','Рёкан «Асакити»')], ('06','Рёкан Асакити')),
    ('Святилище Тадо-тайся', None, [('18','Святилище Тадо-тайся'), ('19','Святилище Тадо-тайся')]),
    ('Yunoyama Sosuikyo', None, [('20','Yunoyama Sosuikyo'), ('21','Yunoyama Sosuikyo')], ('20','Yunoyama Sosuikyo')),
    ('Святилище Цубаки-оками', None, [('22','Святилище Цубаки-оками'), ('21','Святилище Цубаки Оками-ясиро')]),
]

def pins(A):
    return json_pins(SRC, A, MERGE, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 27 by Claude on 2026-10-16 (prices and hours not checked yet)
 ("Святилище Исэ",['01','02','03','04']),
 ("Город Исэ",['05','06','07','08','15']),
 ("Исэ-Сима и Тоба",['09','10','11','12','13','14']),
 ("Кумано и Ига",['16','17']),
 ("Север: Кувана, Комоно, Судзука, Инабэ",['18','19','20','21','22','27']),
 ("Центр: Камэяма и Цу",['23','24','25']),
 ("Юг: Кихо",['26']),
]
