"""Okinawa: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/okinawa_articles'
SKIP=set()
BAR_BACK='Окинава на карте'
MAP_TITLE='Окинава на карте'
ARIA='Карта префектуры Окинава'
VIEW='[26.4,127.85],9'  # main island; the outer islands are brought in by fitBounds
INTRO='{places} из наших статей о префектуре Окинава: замок Сюри и королевство Рюкю, окинавская соба и рынок Макиси, Ямбару, острова Керама, Мияко, Исигаки, Такэтоми, Ириомотэ и Хатэрума, курортные отели, эйса и карате. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Окинава'
LIST_LINK='все статьи о префектуре Окинава'
TOP_VAR='OKINAWA_PINS'
# Left off the maps (handover): places that older top-map pins already show (ky-shurijo -> 01, ky3-naha-market -> 02,
# ky4-taketomi -> 06), two shrines that sit on Shuri castle, and the placeholder of 48 (a product, no place).
DROP={'замок Сюри', 'Первый общественный рынок Макиси', 'Каменные ворота Сонохян-утаки', 'Суимуи-утаки',
      '既存 ky4-taketomi を使う（新しいピンは不要）。参考：остров Такэтоми',
      'なし（商品記事で場所が特定できない。多良間島に置くなら CHURA COLA'}

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('Kintiti soba', None, [('03','Kintiti soba'), ('33','Kintiti soba')]),
    ('OKINAWA SOBA EIBUN', None, [('03','OKINAWA SOBA EIBUN'), ('33','OKINAWA SOBA EIBUN')]),
    ('LIQUID THE STORE', None, [('43','LIQUID THE STORE'), ('33','LIQUID THE STORE')], ('43','LIQUID THE STORE')),
    ('HOSHINOYA Taketomi Island', None, [('07','HOSHINOYA Taketomi Island'), ('06','HOSHINOYA Taketomi Island')]),
    ('HOSHINOYA Okinawa', None, [('16','HOSHINOYA Okinawa'), ('17','HOSHINOYA Okinawa')]),
    ('«Като сёкудо»', None, [('32','«Като сёкудо»'), ('57','«Като сёкудо»')]),
    ('Винокурня Mizuho Shuzo', None, [('33','«Мидзухо сюдзо»'), ('39','Винокурня Mizuho Shuzo')]),
    ('Остров Ихэя', None, [('39','ピン（任意）：Остров Ихэя'), ('58','Остров Ихэя')]),
    ('Префектурный музей и художественная галерея Окинавы', None,
     [('49','Музей префектуры Окинава'), ('51','Префектурный музей и художественная галерея Окинавы')]),
    ('Художественный музей Урасоэ', None, [('49','Художественный музей Урасоэ'), ('55','Художественный музей Урасоэ')]),
    ('Идзэна-тамаудун', None, [('50','Остров Идзэна (Идзэна-тамаудун)'), ('58','Идзэна тамаудун')]),
    ('Исторический музей города Наха', None, [('51','Исторический музей города Наха'), ('55','Музей истории города Наха')]),
    ('Остров Кудака', None, [('53','Остров Кудака'), ('60','Остров Кудака')]),
    ('HYGGE', None, [('32','HYGGE'), ('47','HYGGE')]),  # same shop since the 2026-10-14 coordinate fix
]

def pins(A):
    return [p for p in json_pins(SRC, A, MERGE, pattern='pins_*.json') if p[0] not in DROP]  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 69 by Claude (prices and hours not checked yet)
 ("Наха и Сюри",['01','02','22','31','40','41','45','46','47','51','56']),
 ("Центр и юг острова Окинава",['03','21','30','32','33','34','35','36','38','39','42','43','44','54','55','57','62','69']),
 ("Север (Ямбару, Онна, Наго)",['16','17','18','19','20','23','24','25','26','27','28','29','37','65','66','67','68']),
 ("Острова",['05','06','07','08','09','10','11','12','13','14','15','48','58','59','60','61']),
 ("Королевство Рюкю и культура",['04','49','50','52','53','63','64']),
]
