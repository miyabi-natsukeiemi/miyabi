"""Tottori: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/tottori_articles'
SKIP=set()
BAR_BACK='Тоттори на карте'
MAP_TITLE='Тоттори на карте'
ARIA='Карта префектуры Тоттори'
VIEW='[35.45,133.9],9'
INTRO='{places} из наших статей о Тоттори: мингэй и керамика, дюны Тоттори, Курайоси, онсэны Мисаса и Иваи, музей Сёдзи Уэды у горы Дайсэн, краб мацуба. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Тоттори'
LIST_LINK='все статьи о Тоттори'
TOP_VAR='TOTTORI_PINS'

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('Морской рынок «Кароити»', None, [('06','Морской рынок «Кароити»'), ('08','Рынок «Кароити»')], ('08','Рынок «Кароити»')),
]

def pins(A):
    return json_pins(SRC, A, MERGE, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 9 by Claude (prices and hours not checked yet)
 ("Мингэй",['01','02','09']),
 ("Дюны и море",['06','08']),
 ("Центр префектуры",['03','05']),
 ("Горы",['04','07']),
]
