"""Shiga: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/shiga_articles'
SKIP=set()
BAR_BACK='Сига на карте'
MAP_TITLE='Сига на карте'
ARIA='Карта префектуры Сига'
VIEW='[35.2,136.1],9'
INTRO='{places} из наших статей о Сиге: озеро Бива, гора Хиэй и Энрякудзи, Оми-Хатиман, MIHO MUSEUM, фунадзуси. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Сиге'
LIST_LINK='все статьи о Сиге'
TOP_VAR='SHIGA_PINS'

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('Аллея метасеквой', None, [('18','Аллея метасеквой'), ('02','Аллея метасеквой')], ('18','Аллея метасеквой')),
]

def pins(A):
    return json_pins(SRC, A, MERGE, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 19 by Claude (prices and hours not checked yet); no 14 (the auberge is closed since January 2025)
 ("Оцу и юг озера",['05','09','12','16','20']),
 ("Восток (Хиконэ, Оми-Хатиман, Кока)",['06','10','11','13','15','17']),
 ("Север (Нагахама, Ёго, Майбара)",['03','04','07','08']),
 ("Запад и всё озеро",['01','02','18','19']),
]
