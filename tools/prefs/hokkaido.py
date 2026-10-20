"""Hokkaido: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/hokkaido_articles'
SKIP=set()
BAR_BACK='Хоккайдо на карте'
MAP_TITLE='Хоккайдо на карте'
ARIA='Карта Хоккайдо'
VIEW='[43.4,142.6],7'
INTRO='{places} из наших статей о Хоккайдо: айнская деревня и природа озера Акан, Сиретоко, лето в Нисэко, Упопой в Сираой, вина Ёити, Отару, онсэны и сауны, дороги через перевалы и поля Токати. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Хоккайдо'
LIST_LINK='все статьи о Хоккайдо'
TOP_VAR='HOKKAIDO_PINS'
# Onnechise: the same house in 01 and 04 (~25 m apart), one pin at 01's point (Ren, 2026-10-20).
MERGE=[('«Оннэ-тисэ»', None, [('01','«Оннэ-тисэ»'), ('04','Дом «Оннэ-тисэ» (праздник маримо)')], ('01','«Оннэ-тисэ»'))]
# 45 (design onsen and saunas) has no pins of its own: it is about KAI Poroto (26) and KITAKOBUSHI (06).
EXTRA={('06','KITAKOBUSHI SHIRETOKO Hotel & Resort'):['45'], ('26','KAI Poroto'):['45']}

def pins(A):
    return json_pins(SRC, A, merge=MERGE, extra=EXTRA, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 45 by Claude on 2026-10-19 (quality-checked and photo-checked 2026-10-19/20; prices and hours not checked yet)
 ("Озеро Акан и айны",['01','02','03','04']),
 ("Сиретоко и восток",['05','06','42','44']),
 ("Нисэко",['07','08','09','10','11','12']),
 ("Озеро Тоя, Сираой и залив Утиура",['13','25','26','34']),
 ("Саппоро, Отару и окрестности",['14','19','20','21','22','41']),
 ("Ёити и Сякотан",['18','28','29','30','31']),
 ("Юг и север",['16','17','32','37']),
 ("Центр: Фурано, Асахикава, Томаму",['15','23','27','40','43']),
 ("Токати",['24','33','35','36','38']),
 ("Онсэны на севере и дизайн",['39','45']),
]
