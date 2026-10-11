"""Tokushima: config for tools/pref_map_build.py. Pins come from pins_batch*.json in the source folder."""
SRC='~/Documents/miyabi_articles/tokushima_articles'
SKIP=set()
BAR_BACK='Токусима на карте'
MAP_TITLE='Токусима на карте'
ARIA='Карта префектуры Токусима'
VIEW='[33.95,134.2],9'
INTRO='{places} из наших статей о Токусиме: Ава-одори, долина Ия, город на воде, индиго и сакэ долины Ёсино, Камикацу без отходов, мастерские и сладости. Нажмите на точку, чтобы открыть статью.'
LIST_TITLE='Все статьи о Токусиме'
LIST_LINK='все статьи о Токусиме'
TOP_VAR='TOKUSHIMA_PINS'

# One place written up in several articles: keep one pin that lists all of them (first article = card on the top map).
# (name to show, area or None to keep, [(article number, name in the JSON), ...], optional (number, name) whose coordinates to use);
# see json_pins in pref_map_build.py
MERGE=[
    # 03's point is closer to the real building (at the Bizan ropeway station)
    ('Ава-одори кайкан', None, [('01','Ава-одори кайкан'), ('03','Зал Ава-одори')], ('03','Зал Ава-одори')),
    ('Квартал удацу Вакимати', None, [('07','Историческая улица удацу'), ('04','Квартал удацу Вакимати')], ('07','Историческая улица удацу')),
]
EXTRA={('05','Кафе «Полстар»'):['07']}  # article 07 also tells about this cafe

def pins(A):
    return json_pins(SRC, A, MERGE, EXTRA)  # json_pins comes from tools/pref_map_build.py

GROUPS=[
 ("Праздники и природа",['01','02']),
 ("Города и кварталы",['03','07']),
 ("Ремёсла, вкусы и мастерские",['04','08','09']),
 ("Камикацу и горы Нака",['05','06']),
]
