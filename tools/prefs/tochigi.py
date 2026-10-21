"""Tochigi: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/tochigi_articles'
SKIP=set()
BAR_BACK='Тотиги на карте'
MAP_TITLE='Тотиги на карте'
ARIA='Карта префектуры Тотиги'
VIEW='[36.72,139.82],9'
INTRO='{places} из наших статей о префектуре Тотиги: Никко и озеро Тюдзэндзи, онсэны Кинугавы, Сиобары и Насу, ферма в лесу, гончарный городок Масико, сакэварня в Сано и станция Кэнго Кумы. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Тотиги'
LIST_LINK='все статьи о Тотиги'
TOP_VAR='TOCHIGI_PINS'
# Older top-map pins are left as they are (none at an article place); kt5-tochigi-oya renamed «Каменоломни Оя» (Ren).

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 16 by Claude on 2026-10-21 (no 06: KAI Kawaji closed in 2024; no 17: Sanjodo takes no visitors; quality-checked and photo-checked the same day; prices and hours not checked yet)
 ("Никко и Кинугава",['01','02','03','04','05']),
 ("Насу и Сиобара",['07','08','09','10','11','12']),
 ("Масико",['13','14','16']),
 ("Ещё в Тотиги",['15','18']),
]
