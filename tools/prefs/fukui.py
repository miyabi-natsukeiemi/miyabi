"""Fukui: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/fukui_articles'
SKIP=set()
BAR_BACK='Фукуи на карте'
MAP_TITLE='Фукуи на карте'
ARIA='Карта префектуры Фукуи'
VIEW='[35.85,136.1],9'
INTRO='{places} из наших статей о префектуре Фукуи: краб Этидзэн-гани и порт Микуни, рыба залива Вакаса, сакэ и вода Оно и Кацуяма, ESHIKOTO, ножи, лак и бумага Этидзэн, старые дома Обамы и Цуруги. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Фукуи'
LIST_LINK='все статьи о префектуре Фукуи'
TOP_VAR='FUKUI_PINS'
# The dinosaur museum is in 03 and 04: the top map shows 03's pin only (cb-dino, ~10 km off, was removed).
TOP_SKIP={('04','Музей динозавров префектуры Фукуи')}
# No MERGE: the same place in two articles keeps two pins (as Nara, Kyoto, Ishikawa); identical coordinates were spread ~25 m apart.

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 13 by Claude on 2026-10-19 (quality-checked the same day; prices and hours not checked yet)
 ("Краб и море",['01','02','06']),
 ("Оно и Кацуяма",['03','10']),
 ("Эйхэйдзи и город Фукуи",['04','05']),
 ("Микуни",['07']),
 ("Обама и Цуруга",['08','09']),
 ("Ремёсла Этидзэн и Сабаэ",['11','12','13']),
]
