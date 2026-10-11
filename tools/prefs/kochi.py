"""Kochi: config for tools/pref_map_build.py. Pins come from pins_batch*.json in the source folder."""
SRC='~/Documents/miyabi_articles/kochi_articles'
SKIP=set()
BAR_BACK='Коти на карте'
MAP_TITLE='Коти на карте'
ARIA='Карта префектуры Коти'
VIEW='[33.5,133.5],9'
INTRO='{places} из наших статей о Коти: замок и рынок в городе, река Симанто, мыс Мурото, горные посёлки, мастерские и гостиницы. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Коти'
LIST_LINK='все статьи о Коти'
TOP_VAR='KOCHI_PINS'

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...]); see json_pins in pref_map_build.py
MERGE=[
    ('Отель hotel nansui', None, [('21','Отель hotel nansui'), ('04','Окякуба при отеле hotel nansui')]),
    ('Рёкан «Кагэцу»', 'Мурото', [('06','Рёкан «Кагэцу»'), ('10','Рётэй Кагэцу')]),
    ('Гора Ёкогура', None, [('12','Гора Ёкогура'), ('14','Гора Ёкогура')]),
    ('Музей природы «Ёкогураяма»', None, [('12','Музей природы Ёкогураяма'), ('14','Музей природы «Ёкогураяма»')]),
]

def pins(A):
    return json_pins(SRC, A, MERGE)  # json_pins comes from tools/pref_map_build.py

GROUPS=[
 ("Город Коти и ёсакой",['01','05','06','15']),
 ("Вкус Коти и застолье",['03','04']),
 ("Реки, озёра и побережье",['02','07','10','11']),
 ("Горные дороги и лесная железная дорога",['08','09','12','17']),
 ("Ботаник Томитаро Макино",['13','14']),
 ("Деревни, вера и люди",['16','18','19']),
 ("Где остановиться",['20','21']),
]
