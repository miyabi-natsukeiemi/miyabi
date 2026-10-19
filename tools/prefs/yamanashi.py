"""Yamanashi: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/yamanashi_articles'
SKIP=set()
BAR_BACK='Яманаси на карте'
MAP_TITLE='Яманаси на карте'
ARIA='Карта префектуры Яманаси'
VIEW='[35.6,138.65],9'
INTRO='{places} из наших статей о префектуре Яманаси: отели у озера Кавагутико с видом на Фудзи, путь паломников на гору, ткачи Фудзиёсиды, винодельни Косю и Эндзана, ресторан nôtori, деревня Косугэ и её пиво, Хокуто у подножия Яцугатакэ, онсэн Симобэ и музей Милле в Кофу. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Яманаси'
LIST_LINK='все статьи о префектуре Яманаси'
TOP_VAR='YAMANASHI_PINS'
# Shown on the prefecture page only: the older top-map pins cb-oshinohakkai (~1 km) and cb2-fuji5th (~330 m) mark the same
# places and link to 04. cb-kawaguchiko and cb7-yamanashi-shosenkyo2 (Katsunuma vineyards) link to 01 and 05 (area points).
TOP_SKIP={('04','Осино Хаккай'), ('04','Пятая станция тропы Ёсида')}
# No MERGE: the same place in two articles keeps two pins (as Nara, Kyoto, Ishikawa); identical coordinates were spread ~25 m apart.

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 22 by Claude on 2026-10-19 (no 23, 24: nowhere to visit; quality-checked and photo-checked the same day; prices and hours not checked yet)
 ("Озеро Кавагутико",['01','02','03','08','10']),
 ("Фудзи и Фудзиёсида",['04','11','13']),
 ("Осино и Нарусава",['09','12']),
 ("Вино Косю и Эндзана",['05','06','07']),
 ("Оцуки и деревня Косугэ",['14','15','16']),
 ("Хокуто и Яцугатакэ",['17','18','19']),
 ("Кофу, Фуэфуки, Минобу",['20','21','22']),
]
