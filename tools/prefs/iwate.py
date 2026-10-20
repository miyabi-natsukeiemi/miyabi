"""Iwate: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/iwate_articles'
SKIP=set()
BAR_BACK='Иватэ на карте'
MAP_TITLE='Иватэ на карте'
ARIA='Карта префектуры Иватэ'
VIEW='[39.55,141.4],8'
INTRO='{places} из наших статей о префектуре Иватэ: придорожная станция Хираидзуми, мингэй и чугун Мориоки, пиво Тоно, сакура и народные представления Китаками, онсэны Ханамаки, лак Дзёбодзи, железная дорога Санрику, ферма Коиваи. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи об Иватэ'
LIST_LINK='все статьи об Иватэ'
TOP_VAR='IWATE_PINS'
# Older top-map pins are left as they are (Ren, 2026-10-20).

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 13 by Claude on 2026-10-20 (no 04, 14, 15: nowhere to visit; quality-checked and photo-checked the same day; prices and hours not checked yet)
 ("Мориока и Коиваи",['02','03','16']),
 ("Тоно",['05','06']),
 ("Юг: Хираидзуми, Итиносэки, Китаками, Ханамаки",['01','07','08','09','10']),
 ("Север и побережье Санрику",['11','12','13']),
]
