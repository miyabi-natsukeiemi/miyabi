"""Fukuoka: config for tools/pref_map_build.py. Pins come from pins_claude.json in the source folder."""
SRC='~/Documents/miyabi_articles/fukuoka_articles'
SKIP=set()
BAR_BACK='Фукуока на карте'
MAP_TITLE='Фукуока на карте'
ARIA='Карта префектуры Фукуока'
VIEW='[33.55,130.55],9'
INTRO='{places} из наших статей о префектуре Фукуока: Дадзайфу и святилище Митидзанэ Сугавара, Хаката и Тэндзин, каналы Янагавы, чай Ямэ, керамика Коисивара, Китакюсю и Кокура, Итосима. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о префектуре Фукуока'
LIST_LINK='все статьи о префектуре Фукуока'
TOP_VAR='FUKUOKA_PINS'
# Shown on the prefecture page only: older top-map pins at these places link to the articles
# (fuk-dazaifu -> 01, fuk-ohori -> 04).
# Left off the maps (handover): the airport and the hotel are only mentioned in 16; 11 has no shop (online sales).
DROP={'Аэропорт Китакюсю', 'The Ritz-Carlton, Fukuoka', 'Традиционный гёкуро Ямэ (Ямэ)'}
TOP_SKIP={'святилище Дадзайфу Тэммангу', 'Ohori Terrace'}

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    ('Национальный музей Кюсю', None, [('01','Национальный музей Кюсю'), ('02','Национальный музей Кюсю')]),
    ('BATHHOUSE Dazaifu и NISHIKIMACHI', None, [('02','BATHHOUSE Dazaifu'), ('02','NISHIKIMACHI')]),
    ('Fairfield by Marriott Fukuoka Ukiha и придорожная станция «Укиха»', None,
     [('08','Fairfield by Marriott Fukuoka Ukiha'), ('08','Придорожная станция «Укиха»')]),
]

def pins(A):
    return [p for p in json_pins(SRC, A, MERGE, pattern='pins_*.json') if p[0] not in DROP]  # json_pins comes from tools/pref_map_build.py

GROUPS=[  # all 21 by Claude (prices and hours not checked yet); 07 (sweets of Hakata and Kurume) is in two groups, as in the handover
 ("Дадзайфу",['01','02','03']),
 ("Город Фукуока",['04','06','17','18','19','20','21']),
 ("Хаката (сладости)",['07']),
 ("Янагава и Мияма",['05','12']),
 ("Ямэ и Курумэ",['07','10','11']),
 ("Укиха и Тохо",['08','09']),
 ("Мунаката и Итосима",['13','14']),
 ("Китакюсю",['15','16']),
]
