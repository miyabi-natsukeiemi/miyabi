"""Ibaraki: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/ibaraki_articles'
SKIP=set()
BAR_BACK='Ибараки на карте'
MAP_TITLE='Ибараки на карте'
ARIA='Карта префектуры Ибараки'
VIEW='[36.35,140.35],9'
INTRO='{places} из наших статей о префектуре Ибараки: космический центр Цукуба, пиво Hitachino Nest и Paradise Beer, фейерверк в Цутиуре, еда и сакэ Ибараки, север префектуры и Окакура Тэнсин в Идзуре. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи об Ибараки'
LIST_LINK='все статьи об Ибараки'
TOP_VAR='IBARAKI_PINS'
# Older top-map pins are left as they are (none at an article place).

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 6 by Claude on 2026-10-21 (no 07, 08, 09: nowhere to visit; quality-checked and photo-checked the same day; prices and hours not checked yet)
 ("Цукуба и Цутиура",['01','04']),
 ("Пиво и сакэ",['02','03','05']),
 ("Север Ибараки",['06']),
]
