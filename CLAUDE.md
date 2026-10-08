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

- Every page has a sticky `<!-- site-bar --> … <!-- /site-bar -->` block (brand link + back link). Keep it when editing.
- Article styling lives inside each page under `.mj-article` (fonts: Playfair Display + PT Serif, red accent #B3261E). Keep new styles scoped so they don't leak into other pages.

## Kagawa map (articles/kagawa/index.html)

The Kagawa page has a Leaflet map ("Кагава на карте", `#kagawa-map`) with 50 pins and a themed list of all Kagawa articles (`#kagawa-articles`).
Both are **generated** by `tools/kagawa_map_build.py` and live between marker comments:
`<!-- kagawa-map -->…<!-- /kagawa-map -->` and `<!-- kagawa-articles -->…<!-- /kagawa-articles -->`.
Do not hand-edit inside those markers; change the script and re-run it.

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
