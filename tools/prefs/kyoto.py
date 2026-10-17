"""Kyoto: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/kyoto_articles'
SKIP=set()
BAR_BACK='Киото на карте'
MAP_TITLE='Киото на карте'
ARIA='Карта префектуры Киото'
VIEW='[35.15,135.5],9'
INTRO='{places} из наших статей о префектуре Киото: Фусими Инари и Арасияма, замок Нидзё и дворец Госё, Удзи и чай, Охара, отели и рётэи, кафе и сладости, бани сэнто, «Киото у моря» (Аманохасидатэ, Инэ, Танго), Мияма и юг префектуры. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Киото'
LIST_LINK='все статьи о префектуре Киото'
TOP_VAR='KYOTO_PINS'
# Shown on the prefecture page only: older top-map pins at the same place link to the article
# (kyo-fushimi → 01, kn3-kyoto-nijo → 09).
TOP_SKIP={'Святилище Фусими Инари-тайся','Замок Нидзё'}
# No MERGE, no DROP: the same place in two articles keeps two pins (as in Nara); identical coordinates were spread ~25 m apart.

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 63 by Claude on 2026-10-17 (prices and hours not checked yet)
 ("Фусими и юг города",['01','07','17','42','55']),
 ("Арасияма и Сага",['02','03','04','05','18','20','43']),
 ("Центр, дворец и Нидзё",['08','09','10','11','12','29','36','39','40','52']),
 ("Гион и Хигасияма",['06','19','22','25','33','35','37','38','41']),
 ("Окадзаки и север",['21','23','24','27','28','30','31','46','53']),
 ("Вокзал и отели",['32','34']),
 ("Еда, кафе и сладости",['44','45','47','48','49','50','51','56','63']),
 ("Бани",['54']),
 ("Удзи и Охара",['13','14','15','16']),
 ("Оямадзаки",['26']),
 ("«Киото у моря»",['57','58','59','60','61']),
 ("Мияма и юг префектуры",['62']),
]
