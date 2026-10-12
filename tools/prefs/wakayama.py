"""Wakayama: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/wakayama_articles'
SKIP=set()
BAR_BACK='Вакаяма на карте'
MAP_TITLE='Вакаяма на карте'
ARIA='Карта префектуры Вакаяма'
VIEW='[33.95,135.5],8'
INTRO='{places} из наших статей о Вакаяме: гора Коя, тропы Кумано-кодо, огненный праздник Нати, онсэны Сирахама и Кацуура, умэбоси из Минабэ. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Вакаяме'
LIST_LINK='все статьи о Вакаяме'
TOP_VAR='WAKAYAMA_PINS'

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('Храм Конгобу-дзи', None, [('01','Храм Кондзобудзи'), ('02','Храм Конгобу-дзи'), ('03','Храм Конгобу-дзи')]),
    ('Дандзё-гаран', None, [('01','Дандзё-гаран'), ('03','Дандзё-гаран')]),
    ('Святилище Ниуцухимэ', None, [('02','Святилище Ниуцухимэ'), ('03','Святилище Ниуцухимэ')]),
    ('Святилище Ниу-кансёбу', None, [('02','Святилище Ниу-кансёбу'), ('03','Святилище Ниукансёбу')]),
    ('Храм Дзисон-ин', None, [('02','Храм Дзисон-ин'), ('03','Храм Дзисон-ин')]),
    ('Окуно-ин', None, [('02','Окуно-ин'), ('03','Окуно-ин (ночная экскурсия)')]),
    ('Святилище Кумано Нати-тайся', None, [('04','Кумано Нати Тайся'), ('05','Святилище Кумано Нати-тайся')]),
    ('Храм Нэгородзи', None, [('08','Храм Нэгородзи'), ('16','Храм Нэгородзи')], ('16','Храм Нэгородзи')),
]

def pins(A):
    return json_pins(SRC, A, MERGE, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 16 by Claude (prices and hours not checked yet)
 ("Коя",['01','02','03']),
 ("Север (Кинокава, Аридагава, Гобо)",['06','08','15','16']),
 ("Кумано",['04','05','11']),
 ("Юг и Сирахама",['07','09','10','12','13','14']),
]
