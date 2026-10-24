"""Tokyo (part 1): config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/tokyo_articles'
SKIP=set()
BAR_BACK='Токио на карте'
MAP_TITLE='Токио на карте'
ARIA='Карта Токио'
VIEW='[35.69,139.6],10'
FIT_MINLAT=35  # open on mainland Tokyo; the Izu and Ogasawara islands are further south (zoom out)
INTRO='{places} из наших статей о Токио: Асакуса и Сумида, музеи Уэно и Янаки, Маруноути, Нихонбаси и Гиндза, рынки Цукидзи и Тоёсу, Аояма и Роппонги, Сибуя и Сэтагая, Сибамата, гора Такао и Окутама. Острова Идзу и Огасавара южнее: уменьшите карту. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Токио'
LIST_LINK='все статьи о Токио'
TOP_VAR='TOKYO_PINS'
# Older top-map pins linked via url: tky-asakusa and kt9-tokyo-sensoji2 (01), tky-tsukiji (17, renamed «Рынок Цукидзи»),
# kt4-roppongi (19), kt3-yanaka (10, ~150 m off), kt3-mitorquets (47, Toyosu; the 4 shop pins stay); kt3-oedo-onsen removed (closed in 2021). Ren, 2026-10-23.
TOP_SKIP={('01','Храм Сэнсо-дзи'), ('19','Музей Мори')}

def pins(A):
    return json_pins(SRC, A, pattern='pins_*.json')  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # 62 by Claude on 2026-10-23 (part 1: 01–30, part 2: 31–63 without 59, HINOKO TOKYO closed in 2023; quality-checked and photo-checked; prices and hours not checked yet)
 ("Асакуса и Сумида",['01','02','03','04','05','31','32','33','34','35','36','38']),
 ("Уэно, Янака, Юсима",['06','07','08','09','10','39','40']),
 ("Маруноути, Нихонбаси, Гиндза, Тоёсу",['11','12','13','14','15','16','17','41','42','43','44','45','46','47']),
 ("Акасака, Роппонги, Аояма",['18','19','20','48','49','50','51','52']),
 ("Сибуя, Мэгуро, Сэтагая",['21','22','23','24','53','54','55','56']),
 ("Сибамата и Тосима",['37','57']),
 ("Запад Токио",['25','26','27','58','60','61']),
 ("Острова",['28','29','30','62','63']),
]
