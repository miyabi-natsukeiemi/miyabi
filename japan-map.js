/*!
 * <japan-map> — インタラクティブな日本地図（地方 → 都道府県の2段ドリルダウン）
 * 依存: d3 v7（未読込なら自動でCDNから取得）
 *
 *   <script src="japan-map.js" defer></script>
 *   <japan-map style="height:640px"></japan-map>
 *
 * 属性
 *   data-src   GeoJSONのURL（既定: jsDelivr の dataofjapan/land）
 *   d3-src     d3のURL（既定: unpkg d3@7）
 *   rail       "off" で左の地方リストを隠す
 *   panel      "off" で右の情報パネルを隠す
 *   caption    "off" で右下のキャプションを隠す
 *   region     初期選択の地方ID（hokkaido/tohoku/kanto/chubu/kinki/chugoku/shikoku/kyushu）
 *   pref       初期選択の都道府県コード（1–47）
 *
 * プロパティ / メソッド
 *   el.value            → {region, pref} | null
 *   el.select(region, pref)  外部から選択（どちらも null で全体表示）
 *   el.reset()
 *   el.data = {13: {...}}    県コードごとの追加データ（パネルに表形式で表示）
 *
 * イベント（いずれも bubbles、detail に {region, pref, prefName, regionName}）
 *   japan-map:select / japan-map:hover / japan-map:reset
 *
 * 配色は CSS カスタムプロパティで上書き可（ホスト要素に指定）
 *   --jm-bg --jm-ink --jm-accent --jm-land --jm-line --jm-duration --jm-font
 */
(function () {
  'use strict';

  var GEO = 'https://cdn.jsdelivr.net/gh/dataofjapan/land@master/japan.geojson';
  var D3 = 'https://unpkg.com/d3@7.9.0/dist/d3.min.js';

  var REGIONS = [
    {id:'hokkaido', name:'北海道', en:'Hokkaidō', ids:[1], prefs:1, area:'83,424', pop:'約514万人', hub:'札幌市',
     lead:'日本最北の島。広大な農地と原生林、そして冬の厳しさが生活と産業のかたちを決めてきた地方です。',
     note:'面積は全国の約2割を占める一方、人口密度は最も低い。'},
    {id:'tohoku', name:'東北', en:'Tōhoku', ids:[2,3,4,5,6,7], prefs:6, area:'66,948', pop:'約855万人', hub:'仙台市',
     lead:'奥羽山脈が南北に貫く、米と果樹の地方。太平洋側と日本海側で気候が大きく異なります。',
     note:'夏祭りの文化が濃く、青森ねぶた・秋田竿燈・仙台七夕が並ぶ。'},
    {id:'kanto', name:'関東', en:'Kantō', ids:[8,9,10,11,12,13,14], prefs:7, area:'32,433', pop:'約4,341万人', hub:'東京都区部',
     lead:'日本最大の平野に人口の三分の一が集中する地方。政治・経済・情報の中心が重なっています。',
     note:'国内総生産のおよそ3分の1を占める。'},
    {id:'chubu', name:'中部', en:'Chūbu', ids:[15,16,17,18,19,20,21,22,23], prefs:9, area:'66,807', pop:'約2,133万人', hub:'名古屋市',
     lead:'日本アルプスを抱え、日本海側・内陸・太平洋側の三つの顔をもつ地方。製造業の集積地でもあります。',
     note:'自動車産業を中心に、日本最大の工業出荷額を持つ地域を含む。'},
    {id:'kinki', name:'近畿', en:'Kinki', ids:[24,25,26,27,28,29,30], prefs:7, area:'33,126', pop:'約2,047万人', hub:'大阪市',
     lead:'古代からの都が置かれた地方。歴史都市と商業都市が近接し、独自の言語文化を保っています。',
     note:'京都・奈良に加え、琵琶湖は日本最大の湖。'},
    {id:'chugoku', name:'中国', en:'Chūgoku', ids:[31,32,33,34,35], prefs:5, area:'31,922', pop:'約732万人', hub:'広島市',
     lead:'中国山地が瀬戸内側と日本海側を分ける地方。穏やかな内海の港町が連なります。',
     note:'瀬戸内海は年間降水量が少なく、日照時間が長い。'},
    {id:'shikoku', name:'四国', en:'Shikoku', ids:[36,37,38,39], prefs:4, area:'18,803', pop:'約369万人', hub:'松山市',
     lead:'四国山地が中央を走る、日本の主要四島でもっとも小さな島。八十八箇所を巡る遍路の道が全域を結びます。',
     note:'太平洋側は日本有数の多雨地帯。'},
    {id:'kyushu', name:'九州・沖縄', en:'Kyūshū & Okinawa', ids:[40,41,42,43,44,45,46,47], prefs:8, area:'44,513', pop:'約1,426万人', hub:'福岡市',
     lead:'火山と温泉、そして大陸への玄関口。南へ連なる島々は亜熱帯の気候と独自の文化をもちます。',
     note:'活火山が集中し、地熱発電の導入量が国内最大級。'}
  ];
  var PREF = {
    1:['Hokkaidō','札幌市'],2:['Aomori','青森市'],3:['Iwate','盛岡市'],4:['Miyagi','仙台市'],5:['Akita','秋田市'],
    6:['Yamagata','山形市'],7:['Fukushima','福島市'],8:['Ibaraki','水戸市'],9:['Tochigi','宇都宮市'],10:['Gunma','前橋市'],
    11:['Saitama','さいたま市'],12:['Chiba','千葉市'],13:['Tōkyō','新宿区'],14:['Kanagawa','横浜市'],15:['Niigata','新潟市'],
    16:['Toyama','富山市'],17:['Ishikawa','金沢市'],18:['Fukui','福井市'],19:['Yamanashi','甲府市'],20:['Nagano','長野市'],
    21:['Gifu','岐阜市'],22:['Shizuoka','静岡市'],23:['Aichi','名古屋市'],24:['Mie','津市'],25:['Shiga','大津市'],
    26:['Kyōto','京都市'],27:['Ōsaka','大阪市'],28:['Hyōgo','神戸市'],29:['Nara','奈良市'],30:['Wakayama','和歌山市'],
    31:['Tottori','鳥取市'],32:['Shimane','松江市'],33:['Okayama','岡山市'],34:['Hiroshima','広島市'],35:['Yamaguchi','山口市'],
    36:['Tokushima','徳島市'],37:['Kagawa','高松市'],38:['Ehime','松山市'],39:['Kōchi','高知市'],40:['Fukuoka','福岡市'],
    41:['Saga','佐賀市'],42:['Nagasaki','長崎市'],43:['Kumamoto','熊本市'],44:['Ōita','大分市'],45:['Miyazaki','宮崎市'],
    46:['Kagoshima','鹿児島市'],47:['Okinawa','那覇市']
  };
  var PREF_JA = {1:'北海道',2:'青森県',3:'岩手県',4:'宮城県',5:'秋田県',6:'山形県',7:'福島県',8:'茨城県',9:'栃木県',10:'群馬県',11:'埼玉県',12:'千葉県',13:'東京都',14:'神奈川県',15:'新潟県',16:'富山県',17:'石川県',18:'福井県',19:'山梨県',20:'長野県',21:'岐阜県',22:'静岡県',23:'愛知県',24:'三重県',25:'滋賀県',26:'京都府',27:'大阪府',28:'兵庫県',29:'奈良県',30:'和歌山県',31:'鳥取県',32:'島根県',33:'岡山県',34:'広島県',35:'山口県',36:'徳島県',37:'香川県',38:'愛媛県',39:'高知県',40:'福岡県',41:'佐賀県',42:'長崎県',43:'熊本県',44:'大分県',45:'宮崎県',46:'鹿児島県',47:'沖縄県'};

  var REGION_OF = {}; REGIONS.forEach(function (r) { r.ids.forEach(function (i) { REGION_OF[i] = r.id; }); });
  var byId = {}; REGIONS.forEach(function (r) { byId[r.id] = r; });

  var CSS = `
:host{
  --_bg: var(--jm-bg, #f3f2f2);
  --_ink: var(--jm-ink, #201e1d);
  --_accent: var(--jm-accent, #ec3013);
  --_land: var(--jm-land, #e2e0df);
  --_line: var(--jm-line, rgba(32,30,29,.22));
  --_dur: var(--jm-duration, .72s);
  --_ease: cubic-bezier(.22,1,.36,1);
  --_font: var(--jm-font, "Archivo","Noto Sans JP",system-ui,sans-serif);
  --_tint: color-mix(in srgb, var(--_accent) 22%, var(--_bg));
  --_tint2: color-mix(in srgb, var(--_accent) 38%, var(--_bg));
  --_div: color-mix(in srgb, var(--_ink) 88%, transparent);
  --_mute: color-mix(in srgb, var(--_ink) 52%, transparent);
  display:block; position:relative; min-height:360px;
  background:var(--_bg); color:var(--_ink); font-family:var(--_font);
  container-type:inline-size;
}
*{box-sizing:border-box}
.shell{display:grid; grid-template-columns:210px 1fr 340px; height:100%; min-height:inherit}
.shell.no-rail{grid-template-columns:1fr 340px}
.shell.no-panel{grid-template-columns:210px 1fr}
.shell.no-rail.no-panel{grid-template-columns:1fr}
.rail{border-right:2px solid var(--_div); display:flex; flex-direction:column; min-height:0; overflow:auto}
.rail-list{display:flex; flex-direction:column}
.rail.off,.panel.off,.cap.off{display:none}
.head{font-size:11px; letter-spacing:.14em; text-transform:uppercase; color:var(--_mute); padding:16px 16px 8px}
.rail-item{display:grid; grid-template-columns:26px 1fr; align-items:baseline; gap:6px 10px; flex:none;
  text-align:left; background:none; border:0; border-top:1px solid color-mix(in srgb,var(--_ink) 14%,transparent);
  padding:11px 16px; cursor:pointer; color:inherit; font-family:inherit;
  transition:background .18s linear, color .18s linear}
.rail-item:last-of-type{border-bottom:1px solid color-mix(in srgb,var(--_ink) 14%,transparent)}
.rail-item:hover{background:color-mix(in srgb,var(--_ink) 6%,transparent)}
.rail-item.on{background:var(--_accent); color:var(--_bg)}
.rail-num{font-size:11px; color:color-mix(in srgb,var(--_ink) 45%,transparent); font-variant-numeric:tabular-nums}
.rail-item.on .rail-num,.rail-item.on .rail-en{color:rgba(255,255,255,.75)}
.rail-name{font-size:15px; font-weight:800}
.rail-en{grid-column:2; font-size:10px; letter-spacing:.1em; text-transform:uppercase; color:color-mix(in srgb,var(--_ink) 45%,transparent)}
.rail-foot{margin-top:auto; padding:16px; font-size:11px; line-height:1.6; color:var(--_mute);
  border-top:2px solid var(--_div)}
.stage{position:relative; min-width:0; overflow:hidden}
svg{display:block; width:100%; height:100%}
.land{fill:var(--_land); stroke:var(--_line); stroke-width:.6; vector-effect:non-scaling-stroke;
  transition:fill var(--_dur) var(--_ease), opacity .35s linear}
.region{cursor:pointer}
.region.hov .land{fill:var(--_tint); stroke:color-mix(in srgb,var(--_accent) 60%,transparent); stroke-width:1.1}
.region.on .land{fill:var(--_tint2); stroke:color-mix(in srgb,var(--_accent) 70%,transparent)}
.region.mute{opacity:.28}
.pref.hov .land{fill:var(--_tint); stroke:color-mix(in srgb,var(--_accent) 60%,transparent); stroke-width:1.1}
.pref.pick .land{fill:var(--_accent); stroke:color-mix(in srgb,var(--_accent) 40%,var(--_ink)); stroke-width:1.2}
.pref.dim{opacity:.42}
#camera{transition:transform var(--_dur) var(--_ease)}
.rlabel{font-size:22px; font-weight:800; fill:var(--_ink); paint-order:stroke; stroke:var(--_bg);
  stroke-width:5px; stroke-linejoin:round; pointer-events:none; transition:opacity .3s linear}
.plabel{font-size:17px; font-weight:600; fill:var(--_ink); paint-order:stroke; stroke:var(--_bg);
  stroke-width:4px; stroke-linejoin:round; pointer-events:none; text-anchor:middle}
#prefLabels{opacity:0; transition:opacity .3s linear}
#regionLabels.hide{opacity:0}
.inset-frame{fill:none; stroke:color-mix(in srgb,var(--_ink) 20%,transparent); stroke-width:2;
  transition:stroke .3s linear, stroke-width .3s linear}
.inset-frame.focus{stroke:var(--_accent); stroke-width:4}
.inset-cap{font-size:11px; letter-spacing:.12em; text-transform:uppercase; fill:var(--_mute)}
.cap{position:absolute; right:20px; bottom:14px; font-size:11px; letter-spacing:.1em; text-transform:uppercase;
  color:color-mix(in srgb,var(--_ink) 45%,transparent); pointer-events:none}
.crumb{position:absolute; left:20px; top:18px; display:flex; align-items:center; gap:10px}
.crumb button{font-size:11px; letter-spacing:.12em; text-transform:uppercase; background:none; border:0; padding:0;
  cursor:pointer; color:var(--_accent); font-family:inherit}
.crumb button:disabled{cursor:default; color:color-mix(in srgb,var(--_ink) 45%,transparent)}
.crumb span{font-size:11px; color:color-mix(in srgb,var(--_ink) 35%,transparent)}
.back{position:absolute; left:20px; top:44px; white-space:nowrap; font-family:inherit; font-size:13px;
  padding:9px 16px; border:2px solid var(--_div); background:var(--_bg); color:var(--_ink); cursor:pointer;
  opacity:0; transform:translateY(-6px); pointer-events:none;
  transition:opacity .3s linear, transform .3s var(--_ease), background .15s linear}
.back:hover{background:color-mix(in srgb,var(--_ink) 8%,transparent)}
.back.on{opacity:1; transform:none; pointer-events:auto}
.panel{border-left:2px solid var(--_div); position:relative; min-height:0; display:flex; flex-direction:column}
.body{padding:0 20px 20px; overflow:auto; opacity:0; transform:translateY(10px);
  transition:opacity .34s linear, transform .44s var(--_ease)}
.body.on{opacity:1; transform:none}
.hint{position:absolute; left:20px; right:20px; bottom:20px; font-size:13px; color:var(--_mute);
  transition:opacity .3s linear}
.hint.off{opacity:0}
.kicker{font-size:10px; letter-spacing:.14em; text-transform:uppercase; color:var(--_accent)}
.title{font-size:38px; line-height:1.05; margin:6px 0 2px; letter-spacing:-.02em; font-weight:800}
.en{font-size:11px; letter-spacing:.16em; text-transform:uppercase; color:var(--_mute)}
.rule{border:0; border-top:2px solid var(--_div); margin:16px 0}
.lead{font-size:14px; line-height:1.75; margin:0; text-wrap:pretty}
table{width:100%; border-collapse:collapse; margin:16px 0}
th{text-align:left; font-size:10px; letter-spacing:.1em; text-transform:uppercase; font-weight:600; width:38%;
  color:var(--_mute); padding:9px 0; border-bottom:1px solid color-mix(in srgb,var(--_ink) 14%,transparent)}
td{padding:9px 0; font-size:14px; font-variant-numeric:tabular-nums;
  border-bottom:1px solid color-mix(in srgb,var(--_ink) 14%,transparent)}
.sec{font-size:10px; letter-spacing:.14em; text-transform:uppercase; color:var(--_mute); margin-top:18px}
.tags{display:flex; flex-wrap:wrap; gap:6px; margin-top:8px}
.tag{font-size:12px; white-space:nowrap; padding:4px 9px; border:1px solid color-mix(in srgb,var(--_ink) 28%,transparent);
  cursor:pointer; transition:background .15s linear, color .15s linear}
.tag:hover{background:var(--_tint)}
.tag.on{background:var(--_accent); color:var(--_bg); border-color:var(--_accent)}
.loading{position:absolute; inset:0; display:grid; place-items:center; font-size:12px; letter-spacing:.12em;
  text-transform:uppercase; color:color-mix(in srgb,var(--_ink) 45%,transparent)}
.jm-pin{transition:opacity .25s linear}
.jm-pin .jm-dot{r:5; fill:var(--_accent); stroke:var(--_bg); stroke-width:2; transition:r .15s linear}
.jm-pin:hover .jm-dot{r:7}
.jm-pin-city .jm-dot{r:11; fill:var(--_ink); stroke:var(--_bg); stroke-width:3}
.jm-pin-city:hover .jm-dot{r:13}
.jm-pin .jm-label{font-size:12px; font-weight:700; fill:var(--_ink); text-anchor:middle; paint-order:stroke;
  stroke:var(--_bg); stroke-width:4px; stroke-linejoin:round; pointer-events:none}
button:focus-visible,.tag:focus-visible{outline:2px solid var(--_accent); outline-offset:2px}
@container (max-width: 900px){
  .shell,.shell.no-rail,.shell.no-panel{grid-template-columns:1fr; grid-template-rows:auto 1fr auto}
  .rail{border-right:0; border-bottom:2px solid var(--_div); overflow-x:auto; overflow-y:hidden}
  .rail-list{flex-direction:row}
  .rail .head,.rail-foot{display:none}
  .rail-item{border-top:0; border-right:1px solid color-mix(in srgb,var(--_ink) 14%,transparent); min-width:104px}
  .panel{border-left:0; border-top:2px solid var(--_div); max-height:44%}
  .title{font-size:28px}
}`;

  var loader = null;
  var D3_FALLBACKS = [
    'https://unpkg.com/d3@7.9.0/dist/d3.min.js',
    'https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js'
  ];
  function loadOneScript(src) {
    return new Promise(function (res, rej) {
      var s = document.createElement('script');
      s.src = src; s.crossOrigin = 'anonymous';
      s.onload = function () { res(window.d3); };
      s.onerror = function () { rej(new Error('failed: ' + src)); };
      document.head.appendChild(s);
    });
  }
  function loadD3(src) {
    if (window.d3 && window.d3.geoMercator) return Promise.resolve(window.d3);
    if (loader) return loader;
    var urls = src ? [src].concat(D3_FALLBACKS) : D3_FALLBACKS.slice();
    loader = urls.reduce(function (chain, url) {
      return chain.catch(function () { return loadOneScript(url); });
    }, Promise.reject());
    return loader;
  }

  var geoCache = {};
  var GEO_FALLBACKS = [
    'https://cdn.jsdelivr.net/gh/dataofjapan/land@master/japan.geojson',
    'https://raw.githubusercontent.com/dataofjapan/land/master/japan.geojson'
  ];
  function fetchGeoOne(url) {
    return fetch(url).then(function (r) {
      if (!r.ok) throw new Error('GeoJSON ' + r.status);
      return r.json();
    });
  }
  function loadGeo(url) {
    var key = url || 'default';
    if (!geoCache[key]) {
      var urls = url ? [url].concat(GEO_FALLBACKS) : GEO_FALLBACKS.slice();
      geoCache[key] = urls.reduce(function (chain, u) {
        return chain.catch(function () { return fetchGeoOne(u); });
      }, Promise.reject());
    }
    return geoCache[key];
  }

  function esc(v) {
    return String(v).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  class JapanMap extends HTMLElement {
    static get observedAttributes() { return ['region', 'pref', 'rail', 'panel', 'caption']; }

    constructor() {
      super();
      this._root = this.attachShadow({ mode: 'open' });
      this._active = null; this._pref = null; this._extra = {};
      this._ready = false; this._timer = null;
      this.W = 1000; this.H = 900; this.PAD = 46;
      this.INSET = { x: 40, y: 680, w: 190, h: 155 };
      this.VB = { x: 0, y: 0, w: 1000, h: 900 };
    }

    get value() { return this._active ? { region: this._active, pref: this._pref } : null; }
    set data(obj) { this._extra = obj || {}; if (this._ready) this._fillPanel(); }
    get data() { return this._extra; }

    select(region, pref) {
      this._active = region && byId[region] ? region : null;
      this._pref = this._active && pref && REGION_OF[+pref] === this._active ? +pref : null;
      if (this._ready) this._render();
      return this;
    }
    reset() { this.select(null); this._emit('reset'); return this; }

    connectedCallback() {
      if (this._built) return;
      this._built = true;
      this._build();
      var self = this;
      Promise.all([loadD3(this.getAttribute('d3-src') || D3), loadGeo(this.getAttribute('data-src') || GEO)])
        .then(function (r) { self._draw(r[0], r[1]); })
        .catch(function (e) {
          var l = self._root.querySelector('.loading');
          if (l) l.textContent = '地図データを読み込めませんでした';
          console.error('[japan-map]', e);
        });
    }

    attributeChangedCallback(n, o, v) {
      if (!this._built) return;
      if (n === 'region' || n === 'pref') this.select(this.getAttribute('region'), this.getAttribute('pref'));
      else this._applyLayout();
    }

    _emit(kind, extra) {
      var d = Object.assign({
        region: this._active, regionName: this._active ? byId[this._active].name : null,
        pref: this._pref, prefName: this._pref ? PREF_JA[this._pref] : null
      }, extra || {});
      this.dispatchEvent(new CustomEvent('japan-map:' + kind, { detail: d, bubbles: true, composed: true }));
    }

    _build() {
      var self = this;
      this._root.innerHTML =
        '<style>' + CSS + '</style>' +
        '<div class="shell">' +
          '<aside class="rail"><div class="head">地方 / Regions</div><div class="rail-list"></div>' +
            '<div class="rail-foot">地方をクリックすると拡大し、そのまま都道府県を選べます。<br>Esc で一段戻ります。</div></aside>' +
          '<main class="stage"><svg role="img" aria-label="日本の地方地図" preserveAspectRatio="xMidYMid meet"></svg>' +
            '<nav class="crumb" aria-label="階層"></nav>' +
            '<button class="back" type="button">← 全体に戻る</button>' +
            '<div class="cap">Mercator · 47 prefectures · 沖縄は別枠表示</div>' +
            '<div class="loading">地図データを読み込み中…</div></main>' +
          '<aside class="panel"><div class="head panel-head">地方情報 / Region</div>' +
            '<div class="body"></div>' +
            '<div class="hint">地方を選択すると、ここに詳細が表示されます。</div></aside>' +
        '</div>';

      var list = this._root.querySelector('.rail-list');
      REGIONS.forEach(function (r, i) {
        var b = document.createElement('button');
        b.type = 'button'; b.className = 'rail-item'; b.dataset.rail = r.id;
        b.innerHTML = '<span class="rail-num">' + String(i + 1).padStart(2, '0') + '</span>' +
          '<span class="rail-name">' + r.name + '</span><span class="rail-en">' + r.en + '</span>';
        b.addEventListener('mouseenter', function () { self._hoverRegion(r.id, true); });
        b.addEventListener('mouseleave', function () { self._hoverRegion(r.id, false); });
        b.addEventListener('click', function (e) {
          e.stopPropagation();
          self.select(self._active === r.id && !self._pref ? null : r.id); self._emit('select');
        });
        list.appendChild(b);
      });

      this._root.querySelector('.stage').addEventListener('click', function () {
        if (!self._active) return;
        self.select(null); self._emit('select');
      });
      this._root.querySelector('.back').addEventListener('click', function (e) {
        e.stopPropagation();
        self._pref ? self.select(self._active, null) : self.select(null);
        self._emit('select');
      });
      this._keys = function (e) {
        if (e.key !== 'Escape' || !self._active) return;
        self._pref ? self.select(self._active, null) : self.select(null);
        self._emit('select');
      };
      document.addEventListener('keydown', this._keys);
      this._applyLayout();
    }

    disconnectedCallback() { document.removeEventListener('keydown', this._keys); }

    _applyLayout() {
      var sh = this._root.querySelector('.shell');
      var noRail = this.getAttribute('rail') === 'off';
      var noPanel = this.getAttribute('panel') === 'off';
      sh.classList.toggle('no-rail', noRail);
      sh.classList.toggle('no-panel', noPanel);
      this._root.querySelector('.rail').classList.toggle('off', noRail);
      this._root.querySelector('.panel').classList.toggle('off', noPanel);
      this._root.querySelector('.cap').classList.toggle('off', this.getAttribute('caption') === 'off');
    }

    _draw(d3, geo) {
      var self = this, W = this.W, H = this.H, PAD = this.PAD, INSET = this.INSET;
      var l = this._root.querySelector('.loading'); if (l) l.remove();

      var feats = geo.features.filter(function (f) { return REGION_OF[f.properties.id]; });
      this._main = feats.filter(function (f) { return f.properties.id !== 47; });
      var okinawa = feats.filter(function (f) { return f.properties.id === 47; });
      this._byPref = {};

      var svg = d3.select(this._root.querySelector('svg'));
      var proj = d3.geoMercator().fitExtent([[PAD, PAD], [W - PAD, H - PAD]],
        { type: 'FeatureCollection', features: this._main });
      var path = d3.geoPath(proj);
      var pathOki = d3.geoPath(d3.geoMercator().fitExtent([[8, 8], [INSET.w - 8, INSET.h - 8]],
        { type: 'FeatureCollection', features: okinawa }));

      // 本土のみを投影基準に（伊豆・小笠原などの離島を除外）
      function cores() {
        feats.forEach(function (f) {
          var polys = f.geometry.type === 'MultiPolygon'
            ? f.geometry.coordinates.map(function (c) { return { type: 'Polygon', coordinates: c }; })
            : [f.geometry];
          var areas = polys.map(function (g) { return path.area({ type: 'Feature', geometry: g, properties: {} }) || 0; });
          var max = Math.max.apply(null, areas.concat([0]));
          var keep = polys.filter(function (g, i) { return areas[i] >= max * 0.06; });
          f.core = { type: 'Feature', properties: f.properties,
            geometry: keep.length > 1 ? { type: 'MultiPolygon', coordinates: keep.map(function (g) { return g.coordinates; }) } : (keep[0] || f.geometry) };
        });
      }
      cores();
      var coreFC = function () {
        return { type: 'FeatureCollection', features: self._main.map(function (f) { return f.core; }) };
      };
      proj = d3.geoMercator().fitExtent([[PAD, PAD], [W - PAD, H - PAD]], coreFC());
      path = d3.geoPath(proj);
      cores();
      this._path = path;
      this._proj = proj;
      this._d3 = d3;

      var bb = path.bounds(coreFC());
      this.VB = { x: bb[0][0] - PAD, y: bb[0][1] - PAD,
        w: (bb[1][0] - bb[0][0]) + PAD * 2, h: (bb[1][1] - bb[0][1]) + PAD * 2 };
      svg.attr('viewBox', this.VB.x + ' ' + this.VB.y + ' ' + this.VB.w + ' ' + this.VB.h);
      INSET.x = this.VB.x + 14; INSET.y = this.VB.y + this.VB.h - INSET.h - 14;

      var camera = svg.append('g').attr('id', 'camera').attr('transform', 'translate(0,0) scale(1)');
      REGIONS.forEach(function (r) {
        var g = camera.append('g').attr('class', 'region').attr('data-region', r.id);
        g.selectAll('g')
          .data(self._main.filter(function (f) { return REGION_OF[f.properties.id] === r.id; }))
          .join('g').attr('class', 'pref').attr('data-pref', function (f) { return f.properties.id; })
          .append('path').attr('class', 'land').attr('d', path);
      });
      this._main.forEach(function (f) { self._byPref[f.properties.id] = f; });

      var pl = camera.append('g').attr('id', 'prefLabels');
      this._main.forEach(function (f) {
        var c = path.centroid(f.core);
        if (!c || isNaN(c[0])) return;
        pl.append('text').attr('class', 'plabel')
          .attr('data-region', REGION_OF[f.properties.id]).attr('data-pref', f.properties.id)
          .attr('data-cx', c[0]).attr('data-cy', c[1])
          .attr('transform', 'translate(' + c[0] + ',' + c[1] + ')')
          .text(f.properties.nam_ja);
      });

      var NUDGE = { kanto: [40, 20], kinki: [10, 10], chugoku: [-26, -14], shikoku: [2, 22],
        kyushu: [-30, 26], chubu: [0, -8], tohoku: [8, 0], hokkaido: [0, -6] };
      var rl = svg.append('g').attr('id', 'regionLabels');
      REGIONS.forEach(function (r) {
        var fs = self._main.filter(function (f) { return REGION_OF[f.properties.id] === r.id; });
        if (!fs.length) return;
        var c = path.centroid({ type: 'FeatureCollection', features: fs.map(function (f) { return f.core; }) });
        var n = NUDGE[r.id] || [0, 0];
        rl.append('text').attr('class', 'rlabel').attr('x', c[0] + n[0]).attr('y', c[1] + n[1]).text(r.name);
      });

      var ins = svg.append('g').attr('transform', 'translate(' + INSET.x + ',' + INSET.y + ')');
      ins.append('rect').attr('class', 'inset-frame').attr('width', INSET.w).attr('height', INSET.h);
      ins.append('g').attr('class', 'region').attr('data-region', 'kyushu')
        .selectAll('g').data(okinawa).join('g').attr('class', 'pref').attr('data-pref', 47)
        .append('path').attr('class', 'land').attr('d', pathOki);
      ins.append('text').attr('class', 'inset-cap').attr('x', 4).attr('y', -8).text('沖縄県 / Okinawa');

      svg.selectAll('.region')
        .on('mouseenter', function () { self._hoverRegion(this.dataset.region, true); })
        .on('mouseleave', function () { self._hoverRegion(this.dataset.region, false); })
        .on('click', function (e) {
          e.stopPropagation();
          self.select(this.dataset.region); self._emit('select');
        });
      svg.selectAll('.pref')
        .on('mouseenter', function () { self._hoverPref(this.dataset.pref, true); })
        .on('mouseleave', function () { self._hoverPref(this.dataset.pref, false); })
        .on('click', function (e) {
          e.stopPropagation();
          var id = +this.dataset.pref, reg = REGION_OF[id];
          if (self._active !== reg) self.select(reg);
          else self.select(reg, self._pref === id ? null : id);
          self._emit('select');
        });

      this._pinsLayer = camera.append('g').attr('id', 'pinsLayer');
      this._ready = true;
      var r0 = this.getAttribute('region'), p0 = this.getAttribute('pref');
      if (r0 || p0) this.select(r0 || REGION_OF[+p0], p0);
      else this._render();
      if (this._pinsPending) { this.pins = this._pinsPending; this._pinsPending = null; }
      this._emit('ready');
    }

    set pins(arr) {
      this._pins = arr || [];
      if (!this._ready) { this._pinsPending = this._pins; return; }
      this._renderPins();
    }
    get pins() { return this._pins || []; }

    _renderPins() {
      var self = this;
      var layer = this._pinsLayer;
      if (!layer) return;
      var sel = layer.selectAll('g.jm-pin').data(this._pins, function (d) { return d.id; });
      sel.exit().remove();
      var enter = sel.enter().append('g').attr('class', function (d) { return 'jm-pin' + (d.cluster ? ' jm-pin-city' : ''); })
        .attr('data-id', function (d) { return d.id; })
        .style('cursor', 'pointer')
        .on('click', function (e, d) {
          e.stopPropagation();
          if (d.cluster) { self.select(REGION_OF[d.prefId], d.prefId); self._emit('select'); }
          self._emit('pin', { pin: d });
        });
      enter.append('circle').attr('class', 'jm-dot');
      enter.append('text').attr('class', 'jm-label').attr('y', -12);
      var merged = enter.merge(sel);
      merged.each(function (d) {
        var xy = self._proj([d.lon, d.lat]);
        self._d3.select(this).attr('transform', 'translate(' + xy[0] + ',' + xy[1] + ')');
      });
      merged.select('.jm-label').text(function (d) { return d.cluster ? d.title : ''; });
      this._updatePinVisibility();
    }

    _updatePinVisibility() {
      var self = this;
      if (!this._pinsLayer) return;
      var scale = this._lastScale || 1;
      var inv = 1 / scale;
      this._pinsLayer.selectAll('g.jm-pin').each(function (d) {
        var visible;
        if (d.cluster) visible = self._pref !== d.prefId;
        else if (d.clusterOf) visible = self._pref === d.clusterOf;
        else visible = true;
        var xy = self._proj([d.lon, d.lat]);
        self._d3.select(this)
          .style('display', (visible && d.__match !== false) ? '' : 'none')
          .attr('transform', 'translate(' + xy[0] + ',' + xy[1] + ') scale(' + inv + ')');
      });
    }

    setPinMatch(idSet) {
      if (!this._pins) return;
      var self = this;
      this._pins.forEach(function (p) { p.__match = idSet ? idSet.has(p.id) : true; });
      this._updatePinVisibility();
    }

    _hoverRegion(id, on) {
      if (this._active) return;
      this._root.querySelectorAll('.region[data-region="' + id + '"]').forEach(function (n) { n.classList.toggle('hov', on); });
      var b = this._root.querySelector('.rail-item[data-rail="' + id + '"]');
      if (b) b.style.background = on ? 'color-mix(in srgb, currentColor 6%, transparent)' : '';
      if (on) this._emit('hover', { hoverRegion: id, hoverRegionName: byId[id].name });
    }

    _hoverPref(id, on) {
      if (!this._active || REGION_OF[+id] !== this._active || this._pref) return;
      this._root.querySelectorAll('.pref[data-pref="' + id + '"]').forEach(function (n) { n.classList.toggle('hov', on); });
      if (on) this._emit('hover', { hoverPref: +id, hoverPrefName: PREF_JA[+id] });
    }

    _frame(features, fit) {
      var b = this._path.bounds({ type: 'FeatureCollection', features: features });
      var dx = Math.max(b[1][0] - b[0][0], 1), dy = Math.max(b[1][1] - b[0][1], 1);
      var s = Math.min(22, fit * Math.min(this.VB.w / dx, this.VB.h / dy));
      return [this.VB.x + this.VB.w / 2 - s * (b[0][0] + b[1][0]) / 2,
              this.VB.y + this.VB.h / 2 - s * (b[0][1] + b[1][1]) / 2, s];
    }

    _render() {
      var self = this, R = this._root, active = this._active, pref = this._pref;
      clearTimeout(this._timer);
      var pl = R.querySelector('#prefLabels');
      if (pl) pl.style.opacity = 0;

      R.querySelectorAll('.region').forEach(function (n) {
        n.classList.remove('hov');
        n.classList.toggle('on', !!active && !pref && n.dataset.region === active);
        n.classList.toggle('mute', !!active && n.dataset.region !== active);
      });
      R.querySelectorAll('.pref').forEach(function (n) {
        var id = +n.dataset.pref;
        n.classList.remove('hov');
        n.classList.toggle('pick', pref === id);
        n.classList.toggle('dim', !!pref && REGION_OF[id] === active && pref !== id);
      });
      R.querySelectorAll('.rail-item').forEach(function (n) {
        n.style.background = '';
        n.classList.toggle('on', n.dataset.rail === active);
      });
      var rlg = R.querySelector('#regionLabels'); if (rlg) rlg.classList.toggle('hide', !!active);
      var back = R.querySelector('.back');
      back.classList.toggle('on', !!active);
      back.textContent = pref ? '← 地方に戻る' : '← 全体に戻る';
      this._crumb();

      var cam = R.querySelector('#camera');
      if (!active) { cam.setAttribute('transform', 'translate(0,0) scale(1)'); this._lastScale = 1; this._updatePinVisibility(); this._fillPanel(true); return; }

      var inRegion = this._main.filter(function (f) { return REGION_OF[f.properties.id] === active; });
      var offMap = !!pref && !this._byPref[pref];              // 沖縄県はインセットのみ
      var target = (pref && !offMap) ? [this._byPref[pref]] : inRegion;
      var t = this._frame(target.map(function (f) { return f.core; }), (pref && !offMap) ? 0.62 : 0.78);
      cam.setAttribute('transform', 'translate(' + t[0] + ',' + t[1] + ') scale(' + t[2] + ')');
      this._lastScale = t[2]; this._updatePinVisibility();
      var fr = R.querySelector('.inset-frame'); if (fr) fr.classList.toggle('focus', offMap);

      R.querySelectorAll('#prefLabels .plabel').forEach(function (n) {
        var vis = n.dataset.region === active;
        n.style.display = vis ? '' : 'none';
        n.style.fontWeight = (+n.dataset.pref === pref) ? 800 : 600;
        if (vis) n.setAttribute('transform',
          'translate(' + n.dataset.cx + ',' + n.dataset.cy + ') scale(' + (1 / t[2]).toFixed(4) + ')');
      });
      this._timer = setTimeout(function () { if (pl) pl.style.opacity = 1; }, 720);
      this._fillPanel();
    }

    _crumb() {
      var self = this, c = this._root.querySelector('.crumb');
      if (!this._active) { c.innerHTML = ''; return; }
      var r = byId[this._active];
      var html = '<button type="button" data-lvl="0">日本</button><span>/</span>' +
        '<button type="button" data-lvl="1"' + (this._pref ? '' : ' disabled') + '>' + r.name + '</button>';
      if (this._pref) html += '<span>/</span><button type="button" data-lvl="2" disabled>' + PREF_JA[this._pref] + '</button>';
      c.innerHTML = html;
      c.querySelectorAll('button').forEach(function (b) {
        b.addEventListener('click', function (e) {
          e.stopPropagation();
          b.dataset.lvl === '0' ? self.select(null) : self.select(self._active, null);
          self._emit('select');
        });
      });
    }

    _fillPanel(reset) {
      var self = this, body = this._root.querySelector('.body'), hint = this._root.querySelector('.hint');
      var head = this._root.querySelector('.panel-head');
      if (reset) {
        body.classList.remove('on'); hint.classList.remove('off');
        head.textContent = '地方情報 / Region';
        return;
      }
      var r = byId[this._active];
      head.textContent = this._pref ? '都道府県 / Prefecture' : '地方情報 / Region';
      body.innerHTML = this._pref ? this._prefHTML(this._pref, r) : this._regionHTML(r);
      body.querySelectorAll('[data-jump]').forEach(function (t) {
        t.addEventListener('click', function (e) {
          e.stopPropagation();
          self.select(self._active, +t.dataset.jump); self._emit('select');
        });
      });
      body.classList.remove('on');
      requestAnimationFrame(function () { body.classList.add('on'); hint.classList.add('off'); });
    }

    _tags(ids, current) {
      return '<div class="tags">' + ids.map(function (i) {
        return '<span class="tag' + (i === current ? ' on' : '') + '" tabindex="0" data-jump="' + i + '">' + PREF_JA[i] + '</span>';
      }).join('') + '</div>';
    }

    _regionHTML(r) {
      var n = REGIONS.indexOf(r) + 1;
      return '<div class="kicker">Region ' + String(n).padStart(2, '0') + '</div>' +
        '<h2 class="title">' + r.name + '</h2><div class="en">' + r.en + '</div><hr class="rule">' +
        '<p class="lead">' + r.lead + '</p>' +
        '<table><tr><th>都道府県</th><td>' + r.prefs + '</td></tr>' +
        '<tr><th>面積</th><td>' + r.area + ' km²</td></tr>' +
        '<tr><th>人口</th><td>' + r.pop + '</td></tr>' +
        '<tr><th>中心都市</th><td>' + r.hub + '</td></tr></table>' +
        '<div class="sec">都道府県を選ぶ</div>' + this._tags(r.ids) +
        '<div class="sec">メモ</div><p class="lead">' + r.note + '</p>';
    }

    _prefHTML(id, r) {
      var p = PREF[id], extra = this._extra[id] || this._extra[String(id)];
      var rows = '<tr><th>県庁所在地</th><td>' + p[1] + '</td></tr>' +
        '<tr><th>地方</th><td>' + r.name + '（' + r.en + '）</td></tr>' +
        '<tr><th>コード</th><td>JIS ' + String(id).padStart(2, '0') + '</td></tr>';
      if (extra) Object.keys(extra).forEach(function (k) {
        rows += '<tr><th>' + esc(k) + '</th><td>' + esc(extra[k]) + '</td></tr>';
      });
      var inset = !this._byPref[id]
        ? '<p class="lead" style="color:var(--_accent)">この県は地図左下の別枠（インセット）に表示されています。</p>' : '';
      return '<div class="kicker">' + r.name + ' / Prefecture ' + String(id).padStart(2, '0') + '</div>' +
        '<h2 class="title">' + PREF_JA[id] + '</h2><div class="en">' + p[0] + '</div><hr class="rule">' +
        '<table>' + rows + '</table>' +
        '<div class="sec">同じ地方の都道府県</div>' + this._tags(r.ids, id) +
        '<div class="sec">メモ</div>' + inset + '<p class="lead">' + r.lead + '</p>';
    }
  }

  JapanMap.REGIONS = REGIONS;
  JapanMap.PREF_JA = PREF_JA;
  if (!customElements.get('japan-map')) customElements.define('japan-map', JapanMap);
  window.JapanMap = JapanMap;
})();
