"""Chiba: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/chiba_articles'
SKIP=set()
BAR_BACK='Тиба на карте'
MAP_TITLE='Тиба на карте'
ARIA='Карта префектуры Тиба'
VIEW='[35.5,140.15],9'
INTRO='{places} из наших статей о префектуре Тиба: святилище Катори и купеческая Сахара, натуральное сакэ и стекло Sugahara, железная дорога Коминато и музей у озера Итихара, юг полуострова Босо, Ураясу и город Тиба. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Тибе'
LIST_LINK='все статьи о Тибе'
TOP_VAR='CHIBA_PINS'
# Older top-map pin r2-katori-jingu linked via url (01); titles fixed: «Мыс Инубо», «Гора Нокогирияма» (Ren, 2026-10-23).
TOP_SKIP={('01','Святилище Катори')}

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 17 by Claude on 2026-10-21 (no 16: no place to visit; quality-checked and photo-checked; prices and hours not checked yet)
 ("Катори и Сахара",['01','02','03']),
 ("Побережье Кудзюкури",['04','09']),
 ("Итихара и центр Босо",['05','06','07','08','18']),
 ("Юг Босо",['10','11','12']),
 ("Ураясу и Тиба",['13','14','15','17']),
]
