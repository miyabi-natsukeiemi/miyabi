"""Rebuild the Kagawa sub-articles, the Leaflet pin map and the article list on articles/kagawa/index.html.
Run from anywhere: python3 tools/kagawa_map_build.py  (see CLAUDE.md)."""
import os, re, shutil, json, html
SRC=os.path.expanduser('~/Documents/miyabi_articles/kagawa_articles')
REPO=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KG=os.path.join(REPO,'articles','kagawa')
SKIP={'19_ohloy-brewing','25_lemon-hotel'}
def slug(d):
    s=re.sub(r'^\d+_','',d); s=re.sub(r'_merged$','',s); return s.replace('_','-')
folders=sorted(d for d in os.listdir(SRC) if os.path.isdir(os.path.join(SRC,d)) and d not in SKIP and os.path.exists(os.path.join(SRC,d,'article_ru.html')))
num={}; titles={}
BAR='''<!-- site-bar -->
<style>.site-bar{position:sticky;top:0;z-index:1000;background:rgba(252,252,250,.95);backdrop-filter:blur(8px);border-bottom:1px solid rgba(22,24,26,.14);font-family:Inter,system-ui,sans-serif}
.site-bar .in{max-width:1180px;margin:0 auto;padding:0 16px;height:56px;display:flex;align-items:center;justify-content:space-between;gap:12px}
.site-bar a{text-decoration:none;color:#16181A;font-size:14px}.site-bar .brand{font-family:"Cormorant Garamond",Georgia,serif;font-size:20px;font-weight:600}
.site-bar .back{color:#1E3050}.site-bar .back:hover{color:#B3352D}</style>
<div class="site-bar"><div class="in"><a class="brand" href="../../../index.html">Omamori Concierge</a><a class="back" href="../index.html#kagawa-map">&larr; Кагава на карте</a></div></div>
<!-- /site-bar -->
'''
for d in folders:
    s=slug(d); num[d[:2]]=s
    src=open(os.path.join(SRC,d,'article_ru.html'),encoding='utf-8').read()
    m=re.search(r'<h1[^>]*>(.*?)</h1>',src,re.S); titles[s]=re.sub(r'<[^>]+>','',m.group(1)).strip()
    if '<!-- site-bar -->' not in src:
        src=re.sub(r'(<body[^>]*>)',lambda m:m.group(1)+'\n'+BAR,src,count=1)
    out=os.path.join(KG,s); os.makedirs(out,exist_ok=True)
    open(os.path.join(out,'index.html'),'w',encoding='utf-8').write(src)
    imd=os.path.join(SRC,d,'images')
    if os.path.isdir(imd):
        shutil.copytree(imd,os.path.join(out,'images'),dirs_exist_ok=True,ignore=shutil.ignore_patterns('.DS_Store'))
def A(*nums): return [num[n] for n in nums]
T1='о. Тэсима (豊島), рядом с Сёдосимой'; T2='о. Тэсима (手島), острова Сиваку'
# name, area, cat, lat, lng, approx, articles
P=[
["№71 Ияданидзи","Митоё","see",34.221462,133.716888,1,A('03')],
["№72 Мандарадзи","Дзэнцудзи","see",34.223492,133.750412,0,A('03')],
["№73 Сюссякадзи","Дзэнцудзи","see",34.216114,133.749374,0,A('03')],
["№74 Коямадзи","Дзэнцудзи","see",34.231613,133.765747,0,A('03')],
["№75 Дзэнцудзи","Дзэнцудзи","see",34.224976,133.774338,0,A('03')],
["№76 Кондзодзи","Дзэнцудзи","see",34.249863,133.780991,0,A('03')],
["№77 Дорюдзи","Тадоцу","see",34.27618,133.762985,0,A('03')],
["Кондитерская Кумаока","Дзэнцудзи","shop",34.225811,133.77475,0,A('03')],
["Удонная «Охара»","Дзэнцудзи","eat",34.227173,133.768005,0,A('03')],
["Аквариум Сикоку","Утадзу","see",34.312881,133.80809,0,A('05')],
["Карабуро Цукахара","Сануки","see",34.246601,134.165421,0,A('06')],
["Баня Сима-ю","о. Сёдосима","see",34.488445,134.169907,0,A('07')],
["HOMEMAKERS","о. Сёдосима","eat",34.507465,134.226166,1,A('10')],
["Хакуэйдо","Канъондзи","shop",34.129396,133.652686,0,A('11','12')],
["Хогэцудо","Маругамэ","shop",34.291752,133.797089,0,A('13')],
["Мэйбуцу Камадо","Сакаидэ","shop",34.316189,133.873306,0,A('14','15')],
["Томоэдо","Хигасикагава","shop",34.250877,134.33461,0,A('16','17')],
["Ёсиока Гэмпэймоти хомпо","Такамацу","shop",34.34502,134.056473,0,A('18')],
["Митани Сэйто","Хигасикагава","shop",34.215862,134.418686,0,A('20')],
["OHLOY BREWING","Такамацу, Мурэ","eat",34.349121,134.132751,1,A('19')],
["Удонная «Варая»","Такамацу, Ясима","eat",34.343757,134.108237,0,A('22')],
["Сикоку-мура","Такамацу, Ясима","art",34.345005,134.108124,0,A('52','59','60','64','42','49')],
["Рёкан Рока","о. Наосима","stay",34.459797,133.99559,1,A('23')],
["SANA MANE и сауна SAZAE","о. Наосима","stay",34.45166,133.976456,1,A('27')],
["Умитота",T1,"stay",34.485191,134.05954,1,A('24')],
["Лимонный отель",T1,"stay",34.479767,134.092285,1,A('25')],
["URASHIMA VILLAGE","Митоё, полуостров Сёнай","stay",34.233791,133.617584,1,A('26')],
["UDON HOUSE","Митоё","stay",34.149197,133.678284,1,A('26')],
["Юсансо Асан Котонами","Манно","stay",34.097458,133.973175,1,A('67')],
["Здание правительства префектуры","Такамацу","art",34.340183,134.044388,0,A('36','38')],
["Анабуки-арена Кагава","Такамацу","art",34.353642,134.046143,0,A('36')],
["MIMOCA, музей Инокумы","Маругамэ","art",34.291058,133.791855,0,A('36','55')],
["Музей Кайи Хигасиямы в Сэтоути","Сакаидэ, о. Сямидзима","art",34.347679,133.824036,1,A('36')],
["Мемориал Джорджа Накасимы","Такамацу, Мурэ","art",34.334358,134.15303,0,A('36')],
["Sinra (лак)","Аягава","craft",34.261898,133.993729,0,A('69')],
["Итивадо когэй (лак)","Такамацу, Ясима","craft",34.34296,134.114594,0,A('69')],
["Кавагутия сиккитэн (лак)","Сануки","craft",34.250072,134.172409,0,A('69')],
["Окавара сэнсёку хомпо (крашение)","Такамацу","craft",34.342068,134.056122,0,A('69')],
["A-LOOK (оливковая кожа)","Хигасикагава","craft",34.240795,134.334167,0,A('69')],
["Фукусин (перчатки)","Хигасикагава","craft",34.24218,134.35907,0,A('69','73')],
["Тэсима тоэн (керамика)",T2,"craft",34.397011,133.669601,1,A('70')],
["Стеклянная мастерская Масахиро Тая","Аягава","craft",34.252308,133.917908,1,A('71','72')],
["«Кува то хон»","о. Огидзима","stay",34.4262,134.0612,1,A('75')],
["Огидзима Юкуру","о. Огидзима","stay",34.4243,134.0590,1,A('75')],
["«Дамонтэ сёкай»","о. Огидзима","eat",34.422315,134.055101,0,A('75')],
["Квартал Касасима","о. Хондзима","see",34.395897,133.779175,0,A('77')],
["Кюфуку брюинг Хондзима","о. Хондзима","eat",34.385258,133.77916,1,A('77')],
["Пустыня Отодзан","о. Хиросима","see",34.362606,133.702143,0,A('77')],
["Оноэ-тэй","о. Хиросима","see",34.375813,133.722794,1,A('77')],
["Мост Сэто-Охаси, парк у моста","Сакаидэ","see",34.351391,133.825638,0,A('80')],
]
used={a for p in P for a in p[6]}
GROUPS=[
 ("Паломничество",['03']),
 ("Сладости в обёртках Кунибо Вады",['11','12','13','14','15','16','17','18']),
 ("Архитектура и искусство",['36','38','55','52','59','60','64','42','49']),
 ("Вкус Кагавы",['08','09','10','19','20','21','22']),
 ("Мастера и ремёсла",['69','70','71','72','73']),
 ("Где остановиться",['23','24','25','26','27','67','28']),
 ("Острова, море и бани",['05','06','07','75','77','80','81']),
]
allnums=set(num); grouped={n for g in GROUPS for n in g[1]}
assert allnums==grouped, (allnums-grouped, grouped-allnums)
art_js={s:titles[s] for s in titles}
pins_js=[dict(n=p[0],a=p[1],c=p[2],la=p[3],ln=p[4],x=p[5],s=p[6]) for p in P]
lst=[]
for g,ns in GROUPS:
    items=''.join(f'<li><a href="{num[n]}/index.html">{html.escape(titles[num[n]])}</a>{"" if num[n] in used else " <span class=\"kg-nopin\">без точки на карте</span>"}</li>' for n in ns)
    lst.append(f'<div class="kg-group"><h4>{g}</h4><ul>{items}</ul></div>')
SECTION_MAP='''<!-- kagawa-map -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<style>
.kg-map{margin:56px -110px 0;scroll-margin-top:72px}
.kg-map .kicker{margin-top:0}
.kg-map .kg-intro{max-width:712px;margin:0 auto 20px;padding:0 110px;box-sizing:content-box;font-size:17px}
.kg-filters{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:0 0 14px;font-family:Inter,system-ui,sans-serif}
.kg-filters button{font:inherit;font-size:14px;display:inline-flex;align-items:center;gap:7px;padding:6px 12px;border:1px solid var(--line);background:#fff;color:var(--ink);border-radius:999px;cursor:pointer}
.kg-filters button i{width:10px;height:10px;border-radius:50%;display:inline-block}
.kg-filters button[aria-pressed="false"]{opacity:.45}
.kg-filters button:focus-visible{outline:2px solid var(--red);outline-offset:2px}
#kg-leaflet{height:560px;border-top:2px solid var(--ink);border-bottom:1px solid var(--ink);background:#e8eef0}
.kg-note{font-size:14px;font-style:italic;color:var(--muted);margin:10px 0 0;text-align:center}
.kg-pop{font-family:"PT Serif",Georgia,serif;font-size:15px;line-height:1.45;min-width:200px}
.kg-pop b{font-family:"Playfair Display",Georgia,serif;font-size:17px;display:block}
.kg-pop .ar{color:#5C5C5C;font-size:13px}
.kg-pop .ct{font-size:11px;letter-spacing:.12em;text-transform:uppercase;margin:4px 0 6px;display:block}
.kg-pop ul{margin:6px 0;padding-left:16px}.kg-pop li{margin:3px 0}
.kg-pop a{color:#B3261E}
.kg-pop .ap{font-size:12px;color:#5C5C5C;font-style:italic}
@media (max-width:960px){.kg-map{margin:48px 0 0}.kg-map .kg-intro{padding:0}#kg-leaflet{height:460px}}
.kg-articles{margin-top:16px}
.kg-group h4{font-family:"Playfair Display",Georgia,serif;font-style:italic;font-size:21px;font-weight:600;margin:28px 0 6px}
.kg-group ul{margin:0;padding-left:20px}.kg-group li{margin:6px 0}.kg-group li::marker{color:var(--red)}
.kg-nopin{font-size:13px;color:var(--muted);font-style:italic;white-space:nowrap}
</style>
<section class="kg-map" id="kagawa-map" aria-labelledby="kg-map-h">
<p class="kicker">Карта</p><h2 id="kg-map-h">Кагава на карте</h2>
<p class="kg-intro">__COUNT__ мест из наших статей о Кагаве: храмы паломничества, кондитерские, мастерские, музеи и гостиницы на островах. Нажмите на точку, чтобы открыть статью. На карте два разных острова Тэсима: 豊島 рядом с Сёдосимой и 手島 в архипелаге Сиваку.</p>
<div class="kg-filters" id="kg-filters" role="group" aria-label="Фильтр по типу места"></div>
<div id="kg-leaflet" role="region" aria-label="Карта префектуры Кагава"></div>
<p class="kg-note">Пунктирный круг означает, что точка примерная: место находится в этом районе или на этом острове.</p>
</section>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
(function(){
var C={see:["Посмотреть","#1F5A7A"],stay:["Где остановиться","#7A4A8C"],eat:["Где поесть","#B3261E"],shop:["Где купить","#A0740A"],art:["Архитектура и искусство","#2F6B4A"],craft:["Мастерские","#4E6E8E"]};
var ART=__ART__, P=__PINS__;
var map=L.map("kg-leaflet",{scrollWheelZoom:false}).setView([34.3,134.0],10);
L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png",{maxZoom:18,attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'}).addTo(map);
var on={},layers={};Object.keys(C).forEach(function(k){on[k]=true;layers[k]=L.layerGroup().addTo(map)});
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
var all=[];
P.forEach(function(p){
  var m=L.circleMarker([p.la,p.ln],{radius:p.x?11:8,color:p.x?C[p.c][1]:"#fff",weight:2,dashArray:p.x?"3 3":null,fillColor:C[p.c][1],fillOpacity:p.x?.45:.95});
  var links=p.s.map(function(s){return '<li><a href="'+s+'/index.html">'+esc(ART[s])+'</a></li>'}).join("");
  m.bindPopup('<div class="kg-pop"><b>'+esc(p.n)+'</b><span class="ar">'+esc(p.a)+'</span><span class="ct" style="color:'+C[p.c][1]+'">'+C[p.c][0]+'</span><ul>'+links+'</ul>'+(p.x?'<span class="ap">Точка примерная</span>':'')+'</div>');
  m.bindTooltip(p.n);
  m.addTo(layers[p.c]);all.push(m);
});
var f=document.getElementById("kg-filters");
Object.keys(C).forEach(function(k){
  var n=P.filter(function(p){return p.c===k}).length;
  var b=document.createElement("button");b.type="button";b.setAttribute("aria-pressed","true");
  b.innerHTML='<i style="background:'+C[k][1]+'"></i>'+C[k][0]+' · '+n;
  b.onclick=function(){on[k]=!on[k];b.setAttribute("aria-pressed",on[k]);on[k]?map.addLayer(layers[k]):map.removeLayer(layers[k])};
  f.appendChild(b);
});
map.fitBounds(L.featureGroup(all).getBounds().pad(0.05));
})();
</script>
<!-- /kagawa-map -->'''
SECTION_MAP=SECTION_MAP.replace('__COUNT__',str(len(P))).replace('__ART__',json.dumps(art_js,ensure_ascii=False)).replace('__PINS__',json.dumps(pins_js,ensure_ascii=False))
SECTION_LIST=f'''<!-- kagawa-articles --><p class="kicker" id="kagawa-articles">Наши статьи</p><h2>Все статьи о Кагаве</h2><div class="kg-articles">{"".join(lst)}</div><!-- /kagawa-articles -->'''
page_path=os.path.join(KG,'index.html'); page=open(page_path,encoding='utf-8').read()
page=re.sub(r'<!-- kagawa-map -->.*?<!-- /kagawa-map -->','',page,flags=re.S)
page=re.sub(r'<!-- kagawa-articles -->.*?<!-- /kagawa-articles -->','',page,flags=re.S)
page=re.sub(r'<p class="kg-jump"[^>]*>.*?</p>','',page,flags=re.S)
jump=f'<p class="kg-jump" style="font-size:16px;margin:16px 0 0"><a href="#kagawa-map">Карта: {len(P)} мест из {len(titles)} статей</a> · <a href="#kagawa-articles">все статьи о Кагаве</a></p>'
page=page.replace('</p><p class="kicker" id="about">','</p>'+jump+SECTION_MAP+'<p class="kicker" id="about">',1)
page=page.replace('</div></article>',SECTION_LIST+'</div></article>',1)
assert 'kagawa-map -->' in page and 'kagawa-articles' in page
open(page_path,'w',encoding='utf-8').write(page)
print(len(titles),'articles,',len(P),'pins; nopin:',sorted(s for s in titles if s not in used))

# Same pins on the top-page Japan map (index.html): shown when the user zooms into Kagawa.
top_path=os.path.join(REPO,'index.html'); top=open(top_path,encoding='utf-8').read()
CATS={'see':['Посмотреть','#1F5A7A'],'stay':['Где остановиться','#7A4A8C'],'eat':['Где поесть','#B3261E'],'shop':['Где купить','#A0740A'],'art':['Архитектура и искусство','#2F6B4A'],'craft':['Мастерские','#4E6E8E']}
def card(s):
    """Photo + short lead for the top-map popover: thumb.jpg made from the article's first image (macOS sips)."""
    d=os.path.join(KG,s); src=open(os.path.join(d,'index.html'),encoding='utf-8').read()
    m=re.search(r'<p class="lede"[^>]*>(.*?)</p>',src,re.S) or re.search(r'<p>(.*?)</p>',src,re.S)
    lede=html.unescape(re.sub(r'<[^>]+>','',m.group(1))).strip() if m else ''
    if len(lede)>170: lede=lede[:170].rsplit(' ',1)[0].rstrip(' ,.;:—')+'…'
    c={'t':titles[s],'u':f'articles/kagawa/{s}/index.html','l':lede}
    im=re.search(r'<img[^>]+src="([^"]+)"',src)
    if im and not im.group(1).startswith(('http','data:')):
        img=os.path.normpath(os.path.join(d,im.group(1))); th=os.path.join(d,'thumb.jpg')
        if os.path.exists(img):
            if not os.path.exists(th) or os.path.getmtime(th)<os.path.getmtime(img):
                os.system(f'sips -Z 600 -s format jpeg -s formatOptions 72 "{img}" --out "{th}" >/dev/null')
            c['i']=f'articles/kagawa/{s}/thumb.jpg'
    return c
kg_top=dict(cats=CATS,art={s:card(s) for s in titles},pins=pins_js)
SECTION_TOP=f'<!-- kagawa-japan-pins --><script>window.KAGAWA_PINS={json.dumps(kg_top,ensure_ascii=False)};</script><!-- /kagawa-japan-pins -->\n'
ANCHOR='<script>\n\n(function(){\n  // ---- production dataset'
if '<!-- kagawa-japan-pins -->' in top:
    top=re.sub(r'<!-- kagawa-japan-pins -->.*?<!-- /kagawa-japan-pins -->\n',lambda m:SECTION_TOP,top,flags=re.S)
else:
    assert ANCHOR in top; top=top.replace(ANCHOR,SECTION_TOP+ANCHOR,1)
open(top_path,'w',encoding='utf-8').write(top)
print('index.html: Kagawa pins on the Japan map updated')
