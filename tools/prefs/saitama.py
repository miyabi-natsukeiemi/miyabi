"""Saitama: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/saitama_articles'
SKIP=set()
BAR_BACK='Сайтама на карте'
MAP_TITLE='Сайтама на карте'
ARIA='Карта префектуры Сайтама'
VIEW='[35.95,139.35],9'
INTRO='{places} из наших статей о префектуре Сайтама: железнодорожный музей и бонсай в Омии, старые здания и пиво Кавагоэ, музей в Токородзаве, святилище и сакэ Титибу, сауны и пивоварня в Огосэ и Токигаве, ферма в Соке. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Сайтаме'
LIST_LINK='все статьи о Сайтаме'
TOP_VAR='SAITAMA_PINS'
# Older top-map pins linked via url: kt2-saitama-railmuseum (01), kt-kawagoe (02), kt-chichibu (04);
# kt7-saitama-hitsujiyama title «Читибу» → «Титибу» (Ren, 2026-10-23).
TOP_SKIP={('01','Железнодорожный музей'), ('02','«Тэути соба Хякудзё»'), ('02','«Модан-тэй Тайёкэн»')}

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 12 by Claude on 2026-10-21 (no 06, 13, 15, 16: nowhere to visit; quality-checked and photo-checked; prices and hours not checked yet)
 ("Омия и Сайтама",['01','07','08']),
 ("Кавагоэ и Токородзава",['02','03','09']),
 ("Титибу",['04','05']),
 ("Огосэ и Токигава",['10','11','12']),
 ("Ещё в Сайтаме",['14']),
]
