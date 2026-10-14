"""Kumamoto: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/kumamoto_articles'
SKIP=set()
BAR_BACK='Кумамото на карте'
MAP_TITLE='Кумамото на карте'
ARIA='Карта префектуры Кумамото'
VIEW='[32.75,130.75],9'
INTRO='{places} из наших статей о префектуре Кумамото: кальдера Асо и луга Кусасэнри, онсэн Курокава и Минамиогуни, острова Амакуса, кума-сётю из Хитоёси, бары и бани города Кумамото, веера Ямаги, чай Минаматы. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Кумамото'
LIST_LINK='все статьи о префектуре Кумамото'
TOP_VAR='KUMAMOTO_PINS'
# Left off the maps (handover): two places in the city of Kumamoto only mentioned in passing in the Aso article (02).
DROP={'Coffee Gallery', 'Toranosuke'}
# Shown on the prefecture page only: the older top-map pin ky-aso links to 02.
TOP_SKIP={'Кратер Накадакэ'}

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('Yakoboku и Ruri-AN', None, [('08','Yakoboku'), ('10','Yakoboku'), ('08','Ruri-AN')]),
    ('Hananoka Shuzo', None, [('09','Hananoka Shuzo'), ('15','Hananoka Shuzo')]),
    ('Takenokuma Shoso и кафе Takenokuma', None, [('06','Takenokuma Shoso'), ('06','Кафе Takenokuma')]),
]

def pins(A):
    return [p for p in json_pins(SRC, A, MERGE, pattern='pins_*.json') if p[0] not in DROP]  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 16 by Claude (prices and hours not checked yet); no 13 (the Shiranui museum and library closed after the July 2026 earthquake)
 ("Асо и Курокава",['01','02','03','06','07']),
 ("Город Кумамото",['08','09','10','11','12']),
 ("Север (Ямага, Нагоми, Нанкан)",['14','15','16']),
 ("Юг (Хитоёси, Минамата, Амакуса)",['04','05','17']),
]
