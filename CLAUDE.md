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
articles/kagawa/<slug>/    Kagawa sub-articles (44). index.html + images/
```

- Japan map (`<japan-map>` in index.html): 9 regions; Okinawa is its own region (not part of Kyūshū). It lives only in the
  bottom-left inset, which shows on the whole-Japan view and grows to fill the map when Okinawa is opened (main map hidden).
  Inside Okinawa, island groups (`ISLES`: main island, Miyako, Yaeyama, Daitō; split by polygon longitude) can be clicked to zoom in,
  like prefectures inside a region. The inset sits left of Kyūshū, in the visible strip outside the viewBox (`_placeInset`).
  The Northern Territories (Kunashiri, Etorofu, Shikotan, Habomai) are removed from the Hokkaido shape in `_draw` (Ren's request).
- Every page has a sticky `<!-- site-bar --> … <!-- /site-bar -->` block (brand link + back link). Keep it when editing.
  Its `<style>` also carries a rule that centers the hero photo (`.mj-hero` has an inline `margin:0` in the article HTML).
  For Kagawa sub-articles the block comes from `BAR` in `tools/kagawa_map_build.py`.
- Article styling lives inside each page under `.mj-article` (fonts: Playfair Display + PT Serif, red accent #B3261E). Keep new styles scoped so they don't leak into other pages.

## Kagawa map (articles/kagawa/index.html)

The Kagawa page has a Leaflet map ("Кагава на карте", `#kagawa-map`) with 50 pins and a themed list of all Kagawa articles (`#kagawa-articles`).
Both are **generated** by `tools/kagawa_map_build.py` and live between marker comments:
`<!-- kagawa-map -->…<!-- /kagawa-map -->` and `<!-- kagawa-articles -->…<!-- /kagawa-articles -->`.
Do not hand-edit inside those markers; change the script and re-run it.

The same script also writes the pins into the top page (`index.html`) between `<!-- kagawa-japan-pins -->…<!-- /kagawa-japan-pins -->`
(`window.KAGAWA_PINS`). On the Japan map these article pins appear only once Kagawa is selected (`clusterOf:37`), colored by category.
Kagawa categories map to the map filters in `KG_TYPE` in index.html
(see→Виды, eat/shop→Гастрономия, art→История, craft→Активности, stay→Где остановиться).
- Pin colors on the Japan map = filter type (`TYPE_COLOR` in index.html; the filter chips show the same color dots).
  A pin takes the color of its first type, or of its first selected type while filters are on. The Leaflet map on the
  Kagawa page keeps its own 6 category colors.
- Whole-Japan view shows only a spaced-out sample of pins (`_thin(24)`, ~70 of ~450); a region or prefecture shows all.
- Overlapping pins are nudged apart on screen by `_spread` (max ~1 dot radius from the true spot), so they never move to another place.

- Popover: photo card like the prefecture card (first article's photo, title, lead, "Читать статью", other articles of the place below).
  The script makes `articles/kagawa/<slug>/thumb.jpg` (600px, via macOS `sips`) from each article's first image and takes the lead from `p.lede`.
- Pins marked `group` (the Kagawa ones) are handled specially by `<japan-map>` inside that prefecture: pins that overlap on screen
  merge into a numbered marker (`_renderClusters`; clicking it zooms into those pins, `_focus`), and the pointer catches the nearest
  pin within ~26px (`_magnet`). The 6 ordinary Kagawa pins take part too. Clicking empty map inside Kagawa does not zoom out.
- Hover opens the card after a short delay; a click keeps it open until closed.
- Several pins can share one article (e.g. the 7-temple pilgrimage has 9 places). Ren chose to keep one pin per place: the card says
  "Место N из M в этой статье" (list order of `P`) and the other places of that article are highlighted (`highlightPins`).

- Source articles: `~/Documents/miyabi_articles/kagawa_articles/NN_slug/` (`article_ru.html` + `images/`).
  The script copies each into `articles/kagawa/<slug>/`, injects the site-bar, and rebuilds the map and list.
  Folders `19_ohloy-brewing` and `25_lemon-hotel` are old duplicates and are skipped on purpose.
- Pins: list `P` in the script — Russian name, area label, category, lat, lng, approx flag, article slugs.
  Categories: see / stay / eat / shop / art / craft. `approx=1` draws a dashed circle labelled "Точка примерная" (district- or island-level position). Ren accepted approximate positions; no need to research exact ones.
- Two different islands are both "Тэсима" in Russian: 豊島 (near Shodoshima) and 手島 (Shiwaku islands). Area labels must keep the kanji to tell them apart.
- Map tiles: OpenStreetMap standard tiles (CARTO tiles need an API key and showed "API KEY REQUIRED").
- Run: `python3 tools/kagawa_map_build.py` from the repo root. It is idempotent.

## Content rules

- Do not change article text unless Ren asks. Article content was checked by Ren.
- Japanese text Ren asks for: don't use 「・」 as a list connector; use 「、」 or 「や」 (proper nouns are fine).
- Several article HTML files end with editorial HTML comments (sourcing notes). They are invisible on screen but public in the page source. Ren has not decided yet whether to remove them.

## Source material on Ren's Mac

- `~/Documents/miyabi_articles/47_main_articles/` – prefecture guides (source)
- `~/Documents/miyabi_articles/kagawa_articles/` – Kagawa sub-articles (source for the build script)
- `~/Documents/miyabi_articles/miyabi_site/` – older local copy of the site; this repo is now the source of truth
- `~/Documents/miyabi_articles/_to_delete/` – junk to be deleted by Ren

## Ideas in progress

- Theme feature pages for non-place content (local industry, art). First prototype planned: "Сладости в обёртках Кунибо Вады" — the 8 wagashi shops (articles 11–18) as a story plus a route map.
- Concierge CTA on craft/industry articles ("we can arrange a workshop visit").
