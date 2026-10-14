"""Nagasaki: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/nagasaki_articles'
SKIP=set()
BAR_BACK='Нагасаки на карте'
MAP_TITLE='Нагасаки на карте'
ARIA='Карта префектуры Нагасаки'
VIEW='[33.3,129.5],8'
INTRO='{places} из наших статей о префектуре Нагасаки: город Нагасаки, острова Гото и Ики, Цусима, онсэны Ундзэна и Обамы, Сасэбо. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Нагасаки'
LIST_LINK='все статьи о префектуре Нагасаки'
TOP_VAR='NAGASAKI_PINS'

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('«Ады» Ундзэна', None, [('19','«Ады» Ундзэна'), ('20','«Ады» Ундзэна')]),
    ('Музей Ики-коку', None, [('01','Музей Ики-коку'), ('11','Музей Икикоку')], ('11','Музей Икикоку')),
    ('Goto Retreat ray', None, [('14','Goto Retreat ray'), ('15','Goto Retreat ray by Onko Chishin')]),
    ('Yuyado Jyo-kiya', None, [('21','Yuyado Jyo-kiya'), ('22','Yuyado Jyo-kiya')]),
]

def pins(A):
    return json_pins(SRC, A, MERGE, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 27 by Claude (prices and hours not checked yet)
 ("Город Нагасаки",['02','03','04','05','06','07']),
 ("Север: Сасэбо, Хирадо, Хасами, Омура, Сайкай",['08','24','25','26','27']),
 ("Ики и Цусима",['01','11','12','13']),
 ("Острова Гото, Одзика и Уку",['09','10','14','15','16','17','18']),
 ("Ундзэн и Обама",['19','20','21','22','23']),
]
