"""Osaka: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/osaka_articles'
SKIP=set()
BAR_BACK='Осака на карте'
MAP_TITLE='Осака на карте'
ARIA='Карта префектуры Осака'
VIEW='[34.65,135.5],10'
INTRO='{places} из наших статей об Осаке: замок Осака, праздники Тэндзин-мацури и Кисивада-дандзири, Наканосима, сладости из Яо. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи об Осаке'
LIST_LINK='все статьи об Осаке'
TOP_VAR='OSAKA_PINS'
# Shown on the prefecture page only: the top map already has this place (kn3-osaka-shitennoji, linked to 15 via url).
TOP_SKIP={'Храм Ситэнно-дзи'}

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 15 by Claude (prices and hours not checked yet)
 ("Центр Осаки",['01','02','04','05','06','07','11','15']),
 ("Юг (Кисивада, Сакаи, Нагаи, Яо)",['03','08','12','14']),
 ("Север и порт (Моригути, Носэ, Хокко)",['09','10','13']),
]
