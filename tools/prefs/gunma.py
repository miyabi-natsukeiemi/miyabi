"""Gunma: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/gunma_articles'
SKIP=set()
BAR_BACK='Гумма на карте'
MAP_TITLE='Гумма на карте'
ARIA='Карта префектуры Гумма'
VIEW='[36.55,138.95],9'
INTRO='{places} из наших статей о префектуре Гумма: онсэны Кусацу, Икахо и Хоси, шёлковая фабрика Томиока, гора Танигава и Одзе, арт-отель в Маэбаси, музеи Сибукавы и Оты, сакэварня в Кавабе и праздник в Кирю. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Гумме'
LIST_LINK='все статьи о Гумме'
TOP_VAR='GUNMA_PINS'
# Older top-map pins linked via url: kt-kusatsu (01), kt2-gunma-tomioka (05, renamed «Шёлкопрядильная фабрика Томиока»),
# kt5-gunma-onsen2 (06), kt5-gunma-tanigawa (08). kt-mizusawa and r2-morinji have no article (Ren, 2026-10-23).
TOP_SKIP={('01','Юбатакэ'), ('05','Шёлкопрядильная фабрика Томиока, склад коконов «Ниси-окимаю-сё»')}

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 20 by Claude on 2026-10-21 (quality-checked and photo-checked the same day; prices and hours not checked yet)
 ("Кусацу",['01','02','03','04']),
 ("Икахо и Сибукава",['06','07','14']),
 ("Минаками и Одзе",['08','09','10','11']),
 ("Маэбаси, Ота и Томиока",['05','12','13','15']),
 ("Ещё в Гумме",['16','17','18','19','20']),
]
