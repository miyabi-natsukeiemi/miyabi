"""Oita: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/oita_articles'
SKIP=set()
BAR_BACK='Оита на карте'
MAP_TITLE='Оита на карте'
ARIA='Карта префектуры Оита'
VIEW='[33.15,131.45],9'
INTRO='{places} из наших статей о префектуре Оита: онсэны Юфуина и Беппу, каменные Будды и кухня Усуки, святилище Уса-дзингу, плато Кудзю, углекислые источники Нагаю, Хита и рыба Саики. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Оита'
LIST_LINK='все статьи о префектуре Оита'
TOP_VAR='OITA_PINS'
# Left off the maps (handover): the whole Kannawa onsen town; its places are pins of 10 and 20.
DROP={'Онсэн Каннава'}
# Shown on the prefecture page only: older top-map pins at these places link to the articles
# (ky3-usuki -> 11, ky5-oita-usa -> 15, ky-kuju -> 17).
TOP_SKIP={'Каменные Будды Усуки', 'святилище Уса-дзингу', 'HANA to HOSHI / цветочный парк Кудзю'}

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
# Not merged: «Кохи Мокуба» (01) and «Кохи кобо Мокуба» (04) may be the same cafe (Ren to confirm);
# the two «Сюнкоэн» (11 in Usuki, 27 in Hita) are different places.
MERGE=[
    ('«Цуканома»', None, [('02','«Цуканома»'), ('05','«Цуканома»'), ('10','«Цуканома»')]),
    ('«Каннава муси-ю»', None, [('10','«Каннава муси-ю»'), ('20','«Каннава муси-ю»')]),
    ('Придорожная станция «Камаэ» и Buri Laboratory', None, [('28','Придорожная станция «Камаэ»'), ('29','Buri Laboratory')]),
]

def pins(A):
    return [p for p in json_pins(SRC, A, MERGE, pattern='pins_*.json') if p[0] not in DROP]  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 31 by Claude (prices and hours not checked yet)
 ("Юфуин",['01','02','03','04','05','06','07','08','09','10']),
 ("Беппу",['18','19','20','21','22','23']),
 ("Усуки и Уса",['11','12','13','14','15','16']),
 ("Город Оита",['30','31']),
 ("Горы и ущелья (Кудзю, Нагаю, Бунго-Оно, Хита)",['17','24','25','26','27']),
 ("Саики",['28','29']),
]
