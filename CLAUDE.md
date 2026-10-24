# Miyabi / Omamori Concierge site

Static website for a Japan travel concierge aimed at Russian-speaking travelers.
Owner: Ren (GitHub: miyabi-natsukeiemi). Ren talks to Claude in Japanese; all site copy is in Russian.

> This repo is deployed as-is, so this file is publicly readable on the site. Never put secrets, tokens or private notes here.

## Stack and deploy

- Plain static HTML/CSS/JS. No build step, no framework, no package.json.
  (A Next.js rebuild is planned separately; do not migrate this repo unless Ren asks.)
- Hosting: **Cloudflare Pages**, project `miyabi-concierge`. Every push to `main` deploys automatically.
  - Production: https://miyabi-concierge.pages.dev/
  - Check a deploy: `gh api repos/miyabi-natsukeiemi/miyabi/commits/main/check-runs --jq '.check_runs[] | {name,conclusion}'` and look for "Cloudflare Pages".
  - Two Cloudflare **Workers** builds (`miyabi`, `miyabi-pro`) are also wired to this repo and currently fail. They do not affect the Pages site. Ignore unless Ren asks.
- Workflow: edit → preview locally (`python3 -m http.server 8765` in the repo root, open http://localhost:8765/) → commit → push to `main`.
- Always exclude `.DS_Store` from commits.

## Layout

```
index.html                 Top page with the interactive SVG Japan map (#map-section). Large (~1.2 MB), inline everything.
tokyo.html, osaka.html,    Small redirect stubs kept for old links. Leave as they are.
kyoto.html, hokkaido.html,
fukuoka.html
articles/<prefecture>/     One folder per prefecture (47), e.g. articles/kagawa/
  index.html               Prefecture guide (magazine style, class .mj-article)
  img/                     Photos for the guide
  thumb.jpg                Thumbnail used by the top-page map
articles/kagawa/<slug>/    Kagawa sub-articles (44). index.html + images/ + thumb.jpg
articles/kochi/<slug>/     Kochi sub-articles (21), same layout; also ehime (12), tokushima (9), hiroshima (22)
```

- Japan map (`<japan-map>` in index.html): 9 regions; Okinawa is its own region (not part of Kyūshū). It lives only in the
  bottom-left inset, which shows on the whole-Japan view and grows to fill the map when Okinawa is opened (main map hidden).
  Inside Okinawa, island groups (`ISLES`: main island, Miyako, Yaeyama, Daitō; split by polygon longitude) can be clicked to zoom in,
  like prefectures inside a region. The inset sits left of Kyūshū, in the visible strip outside the viewBox (`_placeInset`).
  The Northern Territories (Kunashiri, Etorofu, Shikotan, Habomai) are removed from the Hokkaido shape in `_draw` (Ren's request).
- Every page has a sticky `<!-- site-bar --> … <!-- /site-bar -->` block (brand link + back link). Keep it when editing.
  Its `<style>` also carries a rule that centers the hero photo (`.mj-hero` has an inline `margin:0` in the article HTML)
  and, in sub-articles, the `p.credits` style.
  For generated sub-articles (Kagawa, Kochi) the block comes from `BAR` in `tools/pref_map_build.py`.
- Article styling lives inside each page under `.mj-article` (fonts: Playfair Display + PT Serif, red accent #B3261E). Keep new styles scoped so they don't leak into other pages.

## Prefecture article maps (Kagawa, Kochi, Ehime, Tokushima, Hiroshima, Okayama, Yamaguchi, Tottori, Shimane, Hyogo, Wakayama, Osaka, Shiga, Kyushu and Okinawa, Mie, Nara, Kyoto, Ishikawa, Toyama, Niigata, Nagano, Gifu, Fukui, Shizuoka, Aichi, Yamanashi, Hokkaido, Aomori, Akita, Iwate, Miyagi, Yamagata, Fukushima, Ibaraki, Tochigi, Gunma, Saitama, Chiba, Kanagawa, Tokyo)

Prefectures with their own sub-articles get the same three things, all **generated** by
`tools/pref_map_build.py <pref>` from a config in `tools/prefs/<pref>.py`:

1. Sub-articles: `~/Documents/miyabi_articles/<pref>_articles/NN_slug/` (`article_ru.html` + `images/`) are copied to
   `articles/<pref>/<slug>/` (slug = folder name without `NN_`), with the site-bar injected (`BAR`) and a `thumb.jpg`.
2. On the prefecture guide `articles/<pref>/index.html`: a Leaflet map ("Кагава на карте", "Коти на карте"; `#<pref>-map`)
   and a themed list of all articles (`#<pref>-articles`), between `<!-- <pref>-map -->…` and `<!-- <pref>-articles -->…`.
3. On the top page `index.html`: the same pins between `<!-- <pref>-japan-pins -->…` (`window.KAGAWA_PINS`, `window.KOCHI_PINS`, …).
   Only `article_ru.html` and `images/` are copied; other files in the source folders (`article.md` etc.) stay out.

Do not hand-edit inside those markers; change the config or script and re-run it. Run from the repo root:
`python3 tools/pref_map_build.py kagawa` (or another prefecture; no argument = all). It is idempotent.

Config per prefecture (`tools/prefs/<pref>.py`): source folder, skipped folders, Russian labels (map title, intro, list title,
back link), Leaflet start view, `TOP_VAR`, `pins(A)` returning `[name, area, category, lat, lng, approx, [article slugs]]`,
and `GROUPS` (themes of the article list; must cover every article).
- Kagawa: pins are written out in the config. For 19 and 25 there are two folders each; the site uses `19_ohloy_brewing` and `25_lemon_hotel` (underscores) and skips the hyphen ones (Ren's choice). These two use an older template without `.mj-article`.
  Two different islands are both "Тэсима": 豊島 (near Shodoshima) and 手島 (Shiwaku). Area labels keep the kanji.
- Kochi and the later prefectures: pins come from `pins_batch*.json` in the source folder via `json_pins` in the script
  (`name_ja` and `source` are not shown; from Yamaguchi on, `pattern='pins_*.json'` also reads `pins_claude*.json`). `MERGE` joins one place written up in several articles into one pin (first article =
  card; an optional 4th item picks whose coordinates to use); `EXTRA` adds articles to a pin. Different places that share
  coordinates are spread ~150 m around the point so each can be clicked on the Leaflet map.
  - Kochi (39): 21 articles, 73 pins. MERGE: hotel nansui (21+04), Кагэцу (06+10), Ёкогура mountain and museum (12+14).
  - Ehime (38): 12 articles (no 12: the Nakajima ecotour had ended), 20 pins. MERGE: рёкан «Кия» (02+09).
  - Tokushima (36): 9 articles, 45 pins. MERGE: Ава-одори кайкан (01+03, at 03's point), удацу Вакимати (07+04).
    EXTRA: cafe «Полстар» (05) also links 07.
  - Hiroshima (34): 22 articles (no 18: the bakery closed in 2022), 43 pins. MERGE: святилище Ицукусима (01+22, at 01's point).
  - Okayama (33): 21 articles (no 12, 17, 20), 53 pins. MERGE: сад Коракуэн (02+18), галерея «Фукуока сёю» (14+21), SABOE OKAYAMA (18+21).
  - Yamaguchi (35): 19 articles (01–10 Genspark, 11–19 Claude; cards of 11, 12, 14–19 not checked yet), 61 pins.
    MERGE: рёкан «Отанисансо» (08+07), святилище Сёин / Сёка Сондзюку (01+02).
  - The next six were written by Claude on 2026-10-12; prices and hours on their cards are not checked yet (`<pref>_card_check.md`
    in the source folder), and almost all pin positions are estimates from addresses (approx=1).
  - Tottori (31): 9 articles, 26 pins. MERGE: рынок «Кароити» (06+08, at 08's point).
  - Shimane (32): 22 articles, 81 pins. MERGE: Идзумо-тайся (01+02), музей Адати (04+11), рёкан «Саги-но-ю со» (11+13),
    «Юномати кагурадэн» (17+19).
  - Hyogo (28): 22 articles, 67 pins. MERGE: замок Химэдзи (01+02).
  - Wakayama (30): 16 articles, 65 pins. MERGE: Конгобу-дзи (01+02+03), Дандзё-гаран (01+03), Ниуцухимэ, Ниу-кансёбу,
    Дзисон-ин, Окуно-ин (02+03 each), Кумано Нати-тайся (04+05), Нэгородзи (08+16, at 16's point).
  - Osaka (27): 15 articles, 18 pins (17 on the top map, see `TOP_SKIP`). No MERGE.
  - Shiga (25): 19 articles (no 14: the auberge has been closed since January 2025), 36 pins. MERGE: аллея метасеквой (18+02, at 18's point).
  - Kyushu and Okinawa, written by Claude on 2026-10-12/13; cards not checked yet (`<pref>_card_check.md`). `DROP` in the config
    leaves pins off both maps (outside the prefecture, mentioned in passing, or no address), as the handovers proposed.
    On 2026-10-14 the 105 pins that sat in the sea got new coordinates (`_pipeline/KYUSHU8_SEA_PINS.md`, backup in
    `_pipeline/_bak_20261014_pins/`); 2026-10-16 Daimaru (Oita 24) moved ~25 m out of the river.
  - Nagasaki (42): 27 articles, 95 pins. MERGE: «Ады» Ундзэна (19+20), музей Ики-коку (01+11, at 11's point), Goto Retreat ray (14+15),
    Yuyado Jyo-kiya (21+22).
  - Saga (41): 14 articles, 28 pins. DROP: the two Kyoto places of 14. MERGE: Wataya Besso with Pierre Hermé (08+09),
    Nakashima Farm (12+13), Fukuchiyo and Souan Nabeshima (06).
  - Fukuoka (40): 21 articles (07 is in two groups), 37 pins. DROP: Kitakyushu airport, the Ritz-Carlton (16), the Yame point (11).
    MERGE: Kyushu National Museum (01+02), BATHHOUSE and NISHIKIMACHI (02), Fairfield Ukiha and the roadside station (08).
  - Kumamoto (43): 16 articles (no 13: the Shiranui museum closed after the July 2026 earthquake), 36 pins.
    DROP: Coffee Gallery, Toranosuke (02). MERGE: Yakoboku and Ruri-AN (08+10), Hananoka Shuzo (09+15), Takenokuma (06).
  - Oita (44): 31 articles, 94 pins. DROP: the Kannawa town point (21). MERGE: «Цуканома» (02+05+10), «Каннава муси-ю» (10+20),
    roadside station Kamae and Buri Laboratory (28+29). Not merged: «Кохи Мокуба» (01) and «Кохи кобо Мокуба» (04), same shop unconfirmed.
  - Miyazaki (45): 5 articles, 18 pins. DROP: Skal, Pappacarbone. MERGE: святилище Аосима (01+02).
  - Kagoshima (46): 30 articles, 121 pins. DROP: the Yakushima island point (07), Тябана, TOBA TOBA COLA, Satsuma Vidro Kogei,
    «Сакая Маэкава». MERGE: Сэнганъэн (01+06), five Amami places (22/25/26/28), MIJORA and 2 waters (24).
  - Okinawa (47): 69 articles, 237 pins. DROP: замок Сюри, рынок Макиси, остров Такэтоми, two Shuri utaki, the placeholder of 48.
    14 MERGE (HOSHINOYA x2, Kintiti soba, EIBUN, LIQUID, Като сёкудо, Mizuho Shuzo, Ихэя, museums, Идзэна, Кудака, HYGGE).
  - No pin on the map: Fukuoka 11, Kagoshima 09, 17, 30, Okinawa 01, 02, 48, 52.
  - Mie (24): 27 articles by Claude (2026-10-16 in Claude Code on the Mac, `_pipeline/WRITER_MAC.md`; cards not checked yet),
    97 pins. Re-applied 2026-10-17 after Ren's edits (Latin shop names, «Цубакикиси», pins of Okage Yokocho spread apart).
    MERGE: Дзингу Тёкокан (02+15), рёкан «Асакити» (06+15), Тадо-тайся (18+19), Yunoyama Sosuikyo (20+21), Цубаки-оками (22+21).
  - Nara (29): 37 articles by Claude (2026-10-17; cards not checked yet), 134 pins. No MERGE (Ren: the same place in two
    articles keeps two pins; identical coordinates were spread ~25 m apart), no DROP. 15 (Сакон Сима) points to the
    ruins of Tsubai castle instead of Sekigahara. 19 is `uhn-maruto-shoyu` (the inn was renamed in 2026).
  - Kyoto (26), part 1: 63 articles by Claude (2026-10-17; cards not checked yet, except 32, 44, 49, 52, 54, 63 brought up to date
    on Ren's request), 229 pins. No MERGE, no DROP (as in Nara). 40 Kyoto Brighton closes 2026-11-30 until winter 2028 (said in the
    text). 42 is `momoyama-onsen-tsukimikan` (the inn's official name). Part 2 candidates are in `_pipeline/kyoto_tasks.md`.
  - Ishikawa (17): 29 articles by Claude (2026-10-17, quality-checked and fixed the same night; cards not checked yet), 80 pins.
    No MERGE, no DROP (as in Nara). Noto places (01–11) were checked for reopening after the January 2024 earthquake. Slugs follow
    the official names: 04 `flatts`, 07 `hitotsu-notojima`, 29 `wataya`. 12: the 21st Century Museum closes 2027-05-06 to 2028-03.
  - Toyama (16): 23 articles by Claude (2026-10-17, quality-checked and fixed 2026-10-18; cards not checked yet), 67 pins.
    No MERGE, no DROP. 氷見 is «Хими». Slugs follow the readings: 14 `kane-no-sanzun-nikoka` (和香＝にこか), 15 `takaoka-ichibamachi`
    (市場街＝いちばまち). Kurobe Gorge Railway reopened to Keyakidaira on 2026-10-01 (07, 09; Keyakidaira is limited to the station area).
  - Niigata (15): 23 articles by Claude (2026-10-19, quality-checked and photo-checked the same day; cards not checked yet), 81 pins.
    No MERGE, no DROP. Echigo-Tsumari articles (01–04) describe only works on view all year (the sources are about the 2022 festival).
  - Nagano (20): 42 articles by Claude (2026-10-19, quality-checked and photo-checked the same day; cards not checked yet), 100 pins.
    No MERGE, no DROP. Slugs follow the official names: 24 `grand-phenix-okushiga`, 25 `kai-alps-matsumoto` (two KAI inns).
    Links between articles use full production URLs (md2html does not turn relative links into links).
  - Gifu (21): 24 articles by Claude (2026-10-19, quality-checked and photo-checked the same day; cards not checked yet), 57 pins.
    No MERGE, no DROP (16 Gifu Cola stays although its sales could not be confirmed). 01: Gifu castle keep closed 2026-05-19 to late
    October 2027 (said in the text).
  - Fukui (18): 13 articles by Claude (2026-10-19, quality-checked the same day; cards not checked yet), 44 pins. No MERGE, no DROP.
    The dinosaur museum is in 03 and 04 (two pins). 越前 is «Этидзэн».
  - Shizuoka (22): 30 articles by Claude (2026-10-19, quality-checked and photo-checked the same day; cards not checked yet), 57 pins.
    No 27 (the Vangi museum closed in 2023). No MERGE, no DROP. 15: the Oigawa line is closed between Kawane-Onsen-Sasamado and
    Senzu since 2022 and the Ikawa line is reservation-only since July 2026 (said in the text); 14: the Suruga Bay ferry stops
    2027-01-12 to 01-29 (said in the text). Slugs follow the readings: 20 `tempura-naruse` (成生), 24 `houkouen-tea` (豊好園).
  - Aichi (23): 30 articles by Claude (2026-10-19, quality-checked and photo-checked the same day; cards not checked yet), 69 pins
    (68 on the top map, see `TOP_SKIP`). No MERGE, no DROP; 08 has no pin for Sumiya Bunjiro (no visits for individuals, Ren).
    Kiyosu castle is in 06 and 30 (two pins ~25 m apart). 23–30 are warlords of Owari and Mikawa with places in Aichi only;
    30 Fukushima Masanori also has a Nagano article (`nagano/fukushima-masanori`, linked). 16 is `matsuzuki` (まつ月＝まつづき).
  - Yamanashi (19): 22 articles by Claude (2026-10-19, quality-checked and photo-checked the same day; cards not checked yet), 40 pins
    (38 on the top map, see `TOP_SKIP`). No MERGE, no DROP. No 23 (Wanoka sweets) and 24 (Totsuka vinegar): nowhere to visit.
    塩山 is «Эндзан». Slugs follow the official names: 07 `zen-bed-bogetsuan` (望月庵＝ぼうげつあん), 11 `mt-shakushi-gateway-camp`.
    Fufu is written «Fufu» as in Shizuoka 01. 04: the Yoshida trail has a fee and a cap at the fifth station since 2024 (said in the text).
  - Hokkaido (1), Aomori (2), Akita (5), Iwate (3), Miyagi (4): all by Claude on 2026-10-19/20, quality-checked and photo-checked
    (`<pref>_articles/qc_review_claude.md`; cards not checked yet). Put on the site 2026-10-20 with the open questions of the
    reports left as they are.
  - Hokkaido (1): 45 articles, 123 pins. MERGE: «Оннэ-тисэ» (01+04, at 01's point). EXTRA: 45 (design onsen and saunas) has no pins
    of its own and is added to KITAKOBUSHI (06) and KAI Poroto (26). Slugs: 13 `toya-hikari-no-uta`, 22 `benizakura-gin`,
    23 `yukomanso`, 29 `mongaku-valley`.
  - Aomori (2): 19 articles (no 06: Nigara knives, nowhere to visit), 41 pins (39 on the top map, see `TOP_SKIP`). No MERGE, no DROP.
  - Akita (5): 13 articles (no 05: Aramasa has no shop or tours), 31 pins. No MERGE, no DROP.
  - Iwate (3): 13 articles (no 04, 14, 15: nowhere to visit), 20 pins. No MERGE, no DROP. 06 is `tonoya-yo`, 13 `laureole-tanohata`.
  - Miyagi (4): 12 articles (no 12: Ozoyama studio, business visits only), 21 pins (20 on the top map, see `TOP_SKIP`). No MERGE, no DROP.
  - Yamagata (6): 15 articles by Claude (2026-10-20/21, quality-checked and photo-checked 2026-10-21; cards not checked yet), 32 pins.
    No 02, 17, 18 (nowhere to visit). No MERGE, no DROP. At most 12 photos per article from here on (Ren, 2026-10-20: Cloudflare
    Pages allows 20 000 files, the site had ~15 100). 07, 08, 10, 15 carry visiting details from official sites (Ren: keep).
  - Fukushima (7): 13 articles by Claude (2026-10-21, quality-checked and photo-checked the same day; cards not checked yet), 39 pins
    (38 on the top map, see `TOP_SKIP`). No 10, 12 (nowhere to visit). No MERGE, no DROP; Takayu onsen keeps two pins (02, 06, Ren).
    Slugs: 03 `tashiroyama-drive` (Mt Tashiro, not Oze), 15 `nekoma-mountain` (Alts Bandai and Nekoma merged in 2023).
  - Ibaraki (8): 6 articles by Claude (2026-10-21, quality-checked and photo-checked the same day; cards not checked yet), 15 pins.
    No 07, 08, 09 (nowhere to visit). No MERGE, no DROP. 02 uses the official «Kiuchi Brewery» (Ren).
  - Tochigi (9): 16 articles by Claude (2026-10-21, quality-checked and photo-checked the same day; cards not checked yet), 29 pins.
    No 06 (KAI Kawaji closed in 2024, now TAOYA Kawaji) and 17 (Sanjodo takes no visitors). No MERGE, no DROP. 16 covers three
    Mashiko potters with places to visit (six source articles). «Каноя» (佳乃や) has a pin in both 13 and 16. 05 «KAI Кинугава» in the
    text, «KAI Kinugawa» on the card and pin; 08 «Daikokuya» (official Latin), both as written (Ren). 14 keeps the source's award line.
  - Gunma (10), Saitama (11), Chiba (12), Kanagawa (14): all by Claude on 2026-10-21/23, quality-checked and photo-checked
    (`<pref>_articles/qc_review_claude.md`; cards not checked yet). Put on the site 2026-10-23 with Ren's answers ("all as recommended").
  - Gunma (10): 20 articles, 38 pins (36 on the top map, see `TOP_SKIP`). No MERGE, no DROP. 塚越屋七兵衛 is «Цукагосия Ситибээ»,
    西の河原 «Сайнокавара», 真茶亭 «Маттятэй». 15 uses the official «Coffee & Th!ngs Oh!».
  - Saitama (11): 12 articles (no 06, 13, 15, 16: nowhere to visit), 19 pins (16 on the top map). No MERGE, no DROP.
    04 (and Chiba 01) credit the illustrator «Хитоми Иха (иллюстрация)». 11 Tamagawa terrace and 14 Chavipelto (fire in 2025) not
    confirmed open in 2026 (Ren: keep as written).
  - Chiba (12): 17 articles (no 16: no place to visit), 18 pins (17 on the top map). No MERGE, no DROP. 08 Hoki museum closed after
    the August 2026 flood and 05/06 Kominato line partly suspended after the September 2026 typhoon (said in the text, Ren: keep).
  - Kanagawa (14): 46 articles (no 05, 31, 33, 35), 55 pins (54 on the top map). No MERGE, no DROP. Slugs follow the official names:
    04 `enoura-retreat-rimon`, 06 `calanques-yugawara`, 10 `yokohama-timber-wharf`, 30 `femme-de-bateau-aoki`, 34 `hayama-kachi-tei`.
    Latin shop names stay (Ren). «тапрум» everywhere (Nagano 29 and Yamanashi 06 changed from «таплум» the same day, Ren).
  - Tokyo (13): part 1 (01–30) and part 2 (31–63) by Claude (2026-10-23/24, quality-checked and photo-checked; cards not checked yet),
    62 articles (no 59: HINOKO TOKYO closed in 2023), 111 pins (109 on the top map, see `TOP_SKIP`). No MERGE, no DROP. Ren limited each
    part to about 30 (larger batches mean more errors); further candidates are in `_pipeline/tokyo_tasks.md`. Slugs: 39 `hanaju` (花重),
    60 `shizenjin-mura` (the campsite, run by do-mo). 56 YUEN BETTEI DAITA has only pre-opening renderings, captioned as such (Ren).
    Temporary (COVID-era) hours in a source are replaced by the official 2026 hours (Ren: 19, 43, 50, 58). eyebrow is «Токио · …» (not a prefecture). Ren's answers 2026-10-23: 19 Mori
    shows the official 2026 hours; 24 keeps «Тихий Дон» with a short note on the manga; Ханако Усуи is named with her role (03, 14, 17).
    Island pins (Kozushima, Hachijojima, Ogasawara) are left out of both map frames: `FIT_MINLAT=35` in `tools/prefs/tokyo.py`
    (the Leaflet map opens on mainland Tokyo) and `PIN_FRAME_MINLAT` in index.html (the top map frames mainland Tokyo only).
  - Photographer 宮地工 (Kou Miyaji) is «Ко Миядзи» on every page (Ren, 2026-10-21).
- `TOP_SKIP` (optional, a set of pin names, or `('NN', name)` to hide only that article's pin when two articles share a name): pins shown on the prefecture page only, because an older top-map pin at that place
  already links to the article (Osaka: Храм Ситэнно-дзи → `kn3-osaka-shitennoji`; also Yutoku Inari, Dazaifu, Ohori Terrace,
  Nakadake, Usuki Buddhas, Usa, Kuju, Aoshima, Saitobaru, Sengan-en, the Ibusuki sand baths, Nara's Kimpusen-ji → `kn-yoshino`, Kyoto's Fushimi Inari → `kyo-fushimi`, Nijo castle → `kn3-kyoto-nijo`, Ishikawa's Abare festival → `r2-abare-matsuri`, Natadera of 26, Toyama's Amaharashi coast → `cb-amaharashi`, Niigata's Sado Kinzan → `cb-sado`, Gifu castle → `r2-gifucastle`, Gujo-odori → `cb2-gujo-hachiman`, Fukui's dinosaur museum of 04, Aichi's Inuyama castle → `cb2-inuyama`, Yamanashi's Oshino Hakkai → `cb-oshinohakkai` and Fuji fifth station → `cb2-fuji5th`, Aomori's Nebuta → `th-nebuta`, Hirosaki park → `th-hirosaki`, Miyagi's Tanabata → `th-tanabata`, Fukushima's Tsurugajo → `th-tsurugajo`, Gunma's Yubatake → `kt-kusatsu` and Tomioka → `kt2-gunma-tomioka`, Saitama's railway museum → `kt2-saitama-railmuseum` and two Kawagoe restaurants → `kt-kawagoe`, Chiba's Katori → `r2-katori-jingu`, Kanagawa's Odawara castle → `kt7-kanagawa-odawara`, Tokyo's Senso-ji → `tky-asakusa` and Mori museum → `kt4-roppongi`).
- Categories: see / stay / eat / shop / art / craft. `approx=1` draws a dashed circle "Точка примерная". Ren accepted approximate positions.
- Map tiles: OpenStreetMap standard tiles (CARTO tiles need an API key).
- Adding a prefecture: write `tools/prefs/<pref>.py`, add `[window.<PREF>_PINS, <code>, '<prefix>']` to `PREF_SETS` in index.html.

### On the top-page Japan map
- Article pins appear only once their prefecture is open (`clusterOf` = prefecture code: Kagawa 37, Kochi 39, Ehime 38,
  Tokushima 36, Hiroshima 34, Okayama 33, Yamaguchi 35, Tottori 31, Shimane 32, Hyogo 28, Wakayama 30, Osaka 27, Shiga 25,
  Fukuoka 40, Saga 41, Nagasaki 42, Kumamoto 43, Oita 44, Miyazaki 45, Kagoshima 46, Okinawa 47, Mie 24, Nara 29, Kyoto 26, Ishikawa 17, Toyama 16, Niigata 15, Nagano 20, Gifu 21, Fukui 18, Shizuoka 22, Aichi 23, Yamanashi 19, Hokkaido 1, Aomori 2, Iwate 3, Miyagi 4, Akita 5, Yamagata 6, Fukushima 7, Ibaraki 8, Tochigi 9, Gunma 10, Saitama 11, Chiba 12, Tokyo 13, Kanagawa 14).
- Categories map to the map filters in `KG_TYPE` in index.html
  (see→Виды, eat/shop→Гастрономия, art→История, craft→Активности, stay→Где остановиться).
- Pin colors = filter type (`TYPE_COLOR`; the filter chips show the same dots). A pin takes the color of its first type, or of its
  first selected type while filters are on. The Leaflet maps on the prefecture pages keep their own 6 category colors.
- Whole-Japan view shows only a spaced-out sample of pins (`_thin(24)`); a region or prefecture shows all.
- Overlapping pins are nudged apart on screen by `_spread` (max ~1 dot radius from the true spot), so they never move to another place.
- Popover: photo card like the prefecture card (first article's photo, title, lead, "Читать статью", other articles of the place below).
  `thumb.jpg` (600px, macOS `sips`) comes from the article's first image, the lead from `p.lede`.
- In a prefecture with article pins (`group`), `<japan-map>` zooms closer, uses a light fill, merges pins that overlap on screen into
  a numbered marker (`_renderClusters`; click zooms into them, `_focus`), and the pointer catches the nearest pin within ~26px
  (`_magnet`). Ordinary pins of that prefecture take part too. Clicking empty map there does not zoom out.
- Hover opens the card after a short delay; a click keeps it open until closed.
- Several pins can share one article (e.g. Kagawa's 7-temple pilgrimage has 9 places). One pin per place: the card says
  "Место N из M в этой статье" (pin order) and the other places of that article are highlighted (`highlightPins`).
- Older top-map pins at the same place as an article pin were removed: Kochi castle and Sunday market, Dogo, Uwajima,
  Awa-odori, Iya, Oboke, Onomichi, Takehara. Kochi: tataki and Shimanto link to
  articles 03 and 02 via `url`; Ashizuri has no article.
  Later prefectures, removed: Hagi, Akiyoshido, Izumo, Adachi, Himeji castle, Arima, Nachi waterfall, Osaka castle, the Miho museum
  ("Музей Michu"), lake Biwa. Linked via `url`: fugu Shimonoseki (Yamaguchi 11), Tottori dunes (06), Matsue sunset (05), Tsuwano (18),
  Kobe Kitano (11), Himeji anago (02), Sasayama (09), Koyasan (01), Kumano kodo (04), Shirahama (09), Nakanoshima (Osaka 07),
  Shitennoji (15), Hiei (Shiga 05), Omihachiman (17), Nagahama (03), Daisen (Tottori 04), Uradome (Tottori 02),
  Yunotsu (Shimane 16), Hinomisaki (Shimane 10).
  Kyushu: Kaneda castle, Sasebo (x2), Karatsu, Arita (x2), Yutoku, Dazaifu, Ohori, Yanagawa, Kurokawa, Aso, Amakusa, Yufuin,
  Usuki, Usa, Kuju, Aoshima, Saitobaru, Takachiho, Sakurajima, Sengan-en, Ibusuki, Kirishima, Yakushima; Okinawa: Shuri, Makishi,
  soba, Kerama, Zamami, Taketomi, Ishigaki, Miyako, Yonaguni, cape Hedo; Mie: Toba ama (14), cb-ise removed (01's inner-shrine
  pin replaces it, Ren); Nara: Asuka (01), Yoshino (02), Horyuji (03), Nara park (04); Kyoto: Fushimi Inari (01), Arashiyama (02),
  Nijo (09), Nishijin (12), Kamo river dinner (07), Uji (13), Ohara (15); Ishikawa: Abare festival (01); `r2-natadera` (~10 km off)
  removed, 22's Natadera pin shows instead (as cb-ise in Mie); Toyama: Tateyama snow walls (01), Toyama bay (02), Amaharashi (18); Niigata: Echigo-Tsumari (01), Sado (05), sake (07);
  `cb-kiyotsu` (~10 km off) removed, 04's Tunnel of Light pin shows instead; Nagano: Karuizawa (01), Obuse (18), Hakuba (20),
  Togakushi (21), all at other points than the article pins, so no TOP_SKIP; Gifu: castle (01), Gujo-Hachiman (02), Hida-Furukawa (03);
  Fukui: Echizen crab (01), Ichijodani (04); `cb-dino` (~10 km off) removed, 03's dinosaur museum pin shows instead;
  Shizuoka: Atami (01), Izu onsen (04 Asaba), Nihondaira (14), ~1 km from the article pins, so no TOP_SKIP;
  Aichi: Inuyama castle (01, article pin TOP_SKIP), Arimatsu (02), Seto (04);
  Yamanashi: Kawaguchiko (01), Oshino Hakkai and Fuji fifth station (04, article pins TOP_SKIP), Katsunuma vineyards (05);
  `cb2-shosenkyo` stood ~17 km off near Enzan and was moved to the gorge (35.7426, 138.5653) on 2026-10-19 (Ren).
  Hokkaido, linked via `url`: Akan (01), Shiretoko (05), Utoro (06), Niseko (08), Toya (13), Otaru canal (14), Furano (15), Rebun (16),
  Esashi (17), Shakotan (18), Abashiri drift ice (03), Daisetsuzan (23), Wakkanai (44). Aomori: Nebuta (01), Hirosaki (03),
  Oirase (09), Shirakami (12). Akita: `th-kanto` and `th-kakunodate` removed (01 and 02 have pins there); samurai quarter (02)
  and Oga (03) linked. Miyagi: Tanabata (01), Naruko onsen (02). Iwate: older pins left as they are (Ren), including
  `th2-towada-art` (Aomori's Towada, but prefId 3). Yamagata: older pins left as they are (none at an article place).
  Fukushima: Tsurugajo (05) and Bandai (15) linked; `th-ouchijuku` (~14 km off) removed, 08's Ouchi-juku pin shows instead;
  «Гошикинума» renamed «Госикинума» (Ren). Ibaraki: older pins left as they are (none at an article place). Tochigi: older pins left as they are (none at an article place);
  «Каменоломни Ōя» renamed «Каменоломни Оя» (Ren).
  Gunma, linked via `url`: Kusatsu (01), Tomioka (05, renamed «Шёлкопрядильная фабрика Томиока»), Ikaho (06, ~4 km off), Tanigawa (08);
  Mizusawa udon and Morinji left as they are. Saitama: railway museum (01), Kawagoe (02), Chichibu night festival (04);
  «Холм Хицудзияма (Титибу)» renamed. Chiba: Katori (01); «Мыс Инубо», «Гора Нокогирияма» renamed. Kanagawa: Odawara castle (01),
  Oyama (02, ~1 km off, no TOP_SKIP); the other 13 left as they are. Tokyo, linked via `url`: Asakusa and Nakamise (01), Tsukiji
  (17, renamed «Рынок Цукидзи»; the 9 shop pins stay), Roppongi (19), Yanaka (10, ~150 m off), Toyosu `kt3-mitorquets` (47; the 4 shop pins stay); `kt3-oedo-onsen` removed (closed 2021);
  «Китидзёдзи и парк Инокасира», «Улица Юякэ Дандан», «Накамисэ-дори», «Янака, старый квартал Токио» renamed. Older names with stray Latin letters (Hokkaido «Ниseko», «Сounкё» etc.,
  Akita «Кисаки-мабэ») are not fixed yet.
  Known offsets of older pins, left as they are (Ren): r2-kanedajo, ky3-usuki, ky2-obi, ky3-satsuma, cs5-saga-yutoku (~20 km);
  titles: ky-kurokawa «Онсэн Куроками», ky5-saga-arita2 «Керамические печи Имари» (linked to Arita 05), ky-kuju (old park name).
  Okinawa inset: article pins show once Okinawa is open; close pins merge into numbered markers that zoom step by step
  (`_clusterLayerOki`, `OKI_FOCUS_MAX`). Prefectures with article pins frame those pins too (`pinFrame`, e.g. Yoron).
  Pins that fell into the sea were moved by address (GSI address search, OSM) on 2026-10-12; the source note is in `pins_claude*.json`.

## Content rules

- Do not change article text unless Ren asks. Article content was checked by Ren.
- Japanese text Ren asks for: don't use 「・」 as a list connector; use 「、」 or 「や」 (proper nouns are fine).
- Proper nouns (revision of 2026-10-09, all guides and sub-articles; full rules: `_pipeline/rules_common.md` 4.7 on Ren's Mac):
  places and dishes, festivals, the article's hero and world-famous names stay; passing town names and minor people are replaced by
  a description or role; historical figures stay with years and a 1–3 sentence explanation. Name order is "имя фамилия".
- Photo credits are not in captions: one closing line `<p class="credits">Фото: …</p>` (Kagawa and Kochi sub-articles only;
  guides have none). Its style `p.credits` is in the site-bar `<style>` of the sub-articles (`BAR` in `tools/pref_map_build.py`).
- Revised files carry "- редактура имён собственных (v1)" in the closing `<!-- АКТУАЛИЗИРОВАНО … -->` comment.
  Pre-revision copies on Ren's Mac: `47_main_articles_v1/`, `kagawa_articles_v1/`, `kochi_articles_v1/`.
- Prefecture guides come from `~/Documents/miyabi_articles/47_main_articles/<pref>_<id>.zip` (`index.html`; Hyogo is `hyogo.zip`).
  A repo guide is that file plus the site-bar block (and a blank line) right after `<body …>`; Kagawa and Kochi also get the
  generated blocks. To update: write the zip's `index.html` with the repo's site-bar inserted, then re-run the build script.
- Several article HTML files end with editorial HTML comments (sourcing notes). They are invisible on screen but public in the page source. Ren has not decided yet whether to remove them.

## Source material on Ren's Mac

- `~/Documents/miyabi_articles/47_main_articles/` – prefecture guides (source)
- `~/Documents/miyabi_articles/kagawa_articles/` – Kagawa sub-articles (source for the build script)
- `~/Documents/miyabi_articles/<pref>_articles/` (kochi, ehime, tokushima, hiroshima) – sub-articles and `pins_batch*.json` (source for the build script)
- `~/Documents/miyabi_articles/_pipeline/<PREF>_SITE_HANDOVER.md` – handover notes for adding each prefecture
- `~/Documents/miyabi_articles/miyabi_site/` – older local copy of the site; this repo is now the source of truth
- `~/Documents/miyabi_articles/_to_delete/` – junk to be deleted by Ren

## Ideas in progress

- Theme feature pages for non-place content (local industry, art). First prototype planned: "Сладости в обёртках Кунибо Вады" — the 8 wagashi shops (articles 11–18) as a story plus a route map.
- Concierge CTA on craft/industry articles ("we can arrange a workshop visit").
