"""Kagoshima: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/kagoshima_articles'
SKIP=set()
BAR_BACK='Кагосима на карте'
MAP_TITLE='Кагосима на карте'
ARIA='Карта префектуры Кагосима'
VIEW='[31.6,130.6],9'  # mainland; the islands down to Yoron are brought in by fitBounds
INTRO='{places} из наших статей о префектуре Кагосима: залив Кинко и Сакурадзима, онсэны Ибусуки и Кирисимы, места реставрации Мэйдзи, лес Якусимы, Танэгасима, острова Амами, Токуносима и Ёрон. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Кагосима'
LIST_LINK='все статьи о префектуре Кагосима'
TOP_VAR='KAGOSHIMA_PINS'
# Left off the maps (handover): the whole island of Yakushima (older top-map pin ky-yakushima links to 07),
# a town-centre point, and three places without a known address.
DROP={'Якусима', 'Тябана', 'TOBA TOBA COLA (Кикай)', 'Satsuma Vidro Kogei', '«Сакая Маэкава»'}
# Shown on the prefecture page only: older top-map pins here link to the articles (ky3-satsuma -> 01, ky2-ibusuki -> 02).
TOP_SKIP={'Сад Сэнганъэн', 'Песчаные ванны «Сараку»'}

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('Сад Сэнганъэн', None, [('01','Сад Сэнганъэн'), ('06','Сад Сэнганъэн')]),
    ('Лес Кинсакубару', None, [('22','Лес Кинсакубару'), ('25','Лес Кинсакубару'), ('26','Лес Кинсакубару')]),
    ('«Амами сидзэн кансацу но мори»', None, [('22','«Амами сидзэн кансацу но мори»'), ('25','Лес для наблюдения за природой Амами'),
     ('26','Амами Сидзэн Кансацу но Мори')]),
    ('Центр охраны дикой природы Амами', None, [('25','Центр охраны дикой природы Амами'), ('26','Центр охраны дикой природы Амами')]),
    ('Мангровый парк «Куросио но мори»', None, [('25','Мангровый парк «Куросио но мори»'), ('26','Мангровый парк «Куросио но мори»')]),
    ('Домик наблюдения за амамийским кроликом', None, [('25','Домик наблюдения за амамийским кроликом'),
     ('28','Домик для наблюдения за амамийским кроликом')]),
    ('Denpaku The Beachfront MIJORA и 2 waters', None, [('24','Denpaku The Beachfront MIJORA'), ('24','2 waters')]),
]

def pins(A):
    return [p for p in json_pins(SRC, A, MERGE, pattern='pins_*.json') if p[0] not in DROP]  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 30 by Claude (prices and hours not checked yet)
 ("Город Кагосима и залив Кинко",['01','05','06','11','15']),
 ("Ибусуки и юг полуострова Сацума",['02','10']),
 ("Кирисима и север",['03','04','12','13','14','16','17','18','19']),
 ("Якусима и Танэгасима",['07','08','09','20']),
 ("Острова Амами",['21','22','23','24','25','26','27','28','29','30']),
]
