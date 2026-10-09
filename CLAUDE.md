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
articles/kochi/<slug>/     Kochi sub-articles (21), same layout
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

## Prefecture article maps (Kagawa, Kochi)

Prefectures with their own sub-articles (now Kagawa and Kochi) get the same three things, all **generated** by
`tools/pref_map_build.py <pref>` from a config in `tools/prefs/<pref>.py`:

1. Sub-articles: `~/Documents/miyabi_articles/<pref>_articles/NN_slug/` (`article_ru.html` + `images/`) are copied to
   `articles/<pref>/<slug>/` (slug = folder name without `NN_`), with the site-bar injected (`BAR`) and a `thumb.jpg`.
2. On the prefecture guide `articles/<pref>/index.html`: a Leaflet map ("Кагава на карте", "Коти на карте"; `#<pref>-map`)
   and a themed list of all articles (`#<pref>-articles`), between `<!-- <pref>-map -->…` and `<!-- <pref>-articles -->…`.
3. On the top page `index.html`: the same pins between `<!-- <pref>-japan-pins -->…` (`window.KAGAWA_PINS`, `window.KOCHI_PINS`).

Do not hand-edit inside those markers; change the config or script and re-run it. Run from the repo root:
`python3 tools/pref_map_build.py kagawa` (or `kochi`; no argument = all). It is idempotent.

Config per prefecture (`tools/prefs/<pref>.py`): source folder, skipped folders, Russian labels (map title, intro, list title,
back link), Leaflet start view, `TOP_VAR`, `pins(A)` returning `[name, area, category, lat, lng, approx, [article slugs]]`,
and `GROUPS` (themes of the article list; must cover every article).
- Kagawa: pins are written out in the config. For 19 and 25 there are two folders each; the site uses `19_ohloy_brewing` and `25_lemon_hotel` (underscores) and skips the hyphen ones (Ren's choice). These two use an older template without `.mj-article`.
  Two different islands are both "Тэсима": 豊島 (near Shodoshima) and 手島 (Shiwaku). Area labels keep the kanji.
- Kochi: pins come from `pins_batch1..4.json` in the source folder (`name_ja` and `source` are not shown). `MERGE` joins one place
  written up in several articles into one pin (hotel nansui, Кагэцу, Ёкогура mountain and museum). Different places that share
  placeholder coordinates are spread ~150 m around the point so each can be clicked on the Leaflet map.
- Categories: see / stay / eat / shop / art / craft. `approx=1` draws a dashed circle "Точка примерная". Ren accepted approximate positions.
- Map tiles: OpenStreetMap standard tiles (CARTO tiles need an API key).
- Adding a prefecture: write `tools/prefs/<pref>.py`, add `[window.<PREF>_PINS, <code>, '<prefix>']` to `PREF_SETS` in index.html.

### On the top-page Japan map
- Article pins appear only once their prefecture is open (`clusterOf` = prefecture code: Kagawa 37, Kochi 39).
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
- Kochi's older top-map pins: castle and Sunday market were removed (article pins replace them); tataki and Shimanto link to
  articles 03 and 02 via `url`; Ashizuri has no article.

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
- `~/Documents/miyabi_articles/kochi_articles/` – Kochi sub-articles and `pins_batch*.json` (source for the build script)
- `~/Documents/miyabi_articles/miyabi_site/` – older local copy of the site; this repo is now the source of truth
- `~/Documents/miyabi_articles/_to_delete/` – junk to be deleted by Ren

## Ideas in progress

- Theme feature pages for non-place content (local industry, art). First prototype planned: "Сладости в обёртках Кунибо Вады" — the 8 wagashi shops (articles 11–18) as a story plus a route map.
- Concierge CTA on craft/industry articles ("we can arrange a workshop visit").
