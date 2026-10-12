"""Okayama: config for tools/pref_map_build.py. Pins come from pins_batch*.json in the source folder."""
SRC='~/Documents/miyabi_articles/okayama_articles'
SKIP=set()
BAR_BACK='Окаяма на карте'
MAP_TITLE='Окаяма на карте'
ARIA='Карта префектуры Окаяма'
VIEW='[34.8,133.85],9'
INTRO='{places} из наших статей об Окаяме: квартал Бикан в Курасики, сад Коракуэн, керамика Бидзэн и джинсы Кодзимы, остров Инудзима, искусство и архитектура города Окаяма, фрукты и чай, Цуяма. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи об Окаяме'
LIST_LINK='все статьи об Окаяме'
TOP_VAR='OKAYAMA_PINS'

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('Сад Коракуэн', None, [('02','Сад Коракуэн'), ('18','Сад Коракуэн')]),
    ('Галерея «Фукуока сёю»', None, [('14','Галерея «Фукуока сёю»'), ('21','Галерея «Фукуока сёю»')]),
    ('Чайный салон SABOE OKAYAMA', None, [('18','Чайный салон SABOE OKAYAMA'), ('21','SABOE OKAYAMA')]),
]

def pins(A):
    return json_pins(SRC, A, MERGE)  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # no 12 (no visits), 17 (closed), 20 (the source had almost nothing on Okayama)
 ("Курасики и Кодзима",['01','05','06','13']),
 ("Город Окаяма",['02','14','15','18','21','22']),
 ("Море, мост и острова",['04','08','09','11']),
 ("Ремёсла и вкусы",['03','16','19','24']),
 ("Север префектуры",['07','10','23']),
]
