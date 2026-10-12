"""Yamaguchi: config for tools/pref_map_build.py. Pins come from pins_*.json in the source folder (batch and claude files)."""
SRC='~/Documents/miyabi_articles/yamaguchi_articles'
SKIP=set()
BAR_BACK='Ямагути на карте'
MAP_TITLE='Ямагути на карте'
ARIA='Карта префектуры Ямагути'
VIEW='[34.15,131.6],9'
INTRO='{places} из наших статей о Ямагути: старый город Хаги и герои Мэйдзи, плато Акиёсидай, мост Цуносима, онсэн Нагато-Юмото, Симоносэки, остров Суо-Осима, фестиваль фонарей в Ямагути. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Ямагути'
LIST_LINK='все статьи о Ямагути'
TOP_VAR='YAMAGUCHI_PINS'

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('Рёкан «Отанисансо»', None, [('08','Рёкан „Отанисансо“'), ('07','Рёкан «Отанисансо»')]),
    ('Святилище Сёин и школа Сёка Сондзюку', None, [('01','Святилище Сёин и школа Сёка Сондзюку'), ('02','Школа Сёка Сондзюку (святилище Сёин)')]),
]

def pins(A):
    return json_pins(SRC, A, MERGE, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 01-10 by Genspark, 11-19 by Claude (prices and hours in 11, 12, 14-19 not checked yet)
 ("Хаги и история",['01','02','03']),
 ("Природа",['04','05']),
 ("Нагато и онсэны",['06','07','08','10','12','13']),
 ("Город Ямагути и Юда",['09','14','17']),
 ("Симоносэки",['11','15','19']),
 ("Восток префектуры",['16','18']),
]
