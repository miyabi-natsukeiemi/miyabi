"""Rebuild one prefecture's sub-articles, its Leaflet pin map and article list (articles/<pref>/index.html),
and its pins on the top-page Japan map (index.html).
Usage: python3 tools/pref_map_build.py kagawa   (config per prefecture: tools/prefs/<pref>.py; see CLAUDE.md)."""
import os, re, sys, shutil, json, html, importlib.util
REPO=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def plural(n,one,few,many):
    """Russian count form: 1 место, 2 места, 5 мест."""
    if n%10==1 and n%100!=11: return one
    if 2<=n%10<=4 and not 12<=n%100<=14: return few
    return many

def default_slug(d):
    s=re.sub(r'^\d+_','',d); s=re.sub(r'_merged$','',s); return s.replace('_','-')

BAR='''<!-- site-bar -->
<style>.mj-hero{margin-left:auto!important;margin-right:auto!important}  /* center the hero photo on wide screens */
p.credits{font-size:14px;line-height:1.5;color:var(--muted,#5C5C5C);margin:48px 0 0}  /* closing "Фото: …" line: small and quiet */
.site-bar{position:sticky;top:0;z-index:1000;background:rgba(252,252,250,.95);backdrop-filter:blur(8px);border-bottom:1px solid rgba(22,24,26,.14);font-family:Inter,system-ui,sans-serif}
.site-bar .in{max-width:1180px;margin:0 auto;padding:0 16px;height:56px;display:flex;align-items:center;justify-content:space-between;gap:12px}
.site-bar a{text-decoration:none;color:#16181A;font-size:14px}.site-bar .brand{font-family:"Cormorant Garamond",Georgia,serif;font-size:20px;font-weight:600}
.site-bar .back{color:#1E3050}.site-bar .back:hover{color:#B3352D}</style>
<div class="site-bar"><div class="in"><a class="brand" href="../../../index.html">Omamori Concierge</a><a class="back" href="../index.html#__KEY__-map">&larr; __BACK__</a></div></div>
<!-- /site-bar -->
'''
SECTION_MAP='''<!-- __KEY__-map -->
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
<section class="kg-map" id="__KEY__-map" aria-labelledby="kg-map-h">
<p class="kicker">Карта</p><h2 id="kg-map-h">__MAP_TITLE__</h2>
<p class="kg-intro">__INTRO__</p>
<div class="kg-filters" id="kg-filters" role="group" aria-label="Фильтр по типу места"></div>
<div id="kg-leaflet" role="region" aria-label="__ARIA__"></div>
<p class="kg-note">Пунктирный круг означает, что точка примерная: место находится в этом районе или на этом острове.</p>
</section>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
(function(){
var C={see:["Посмотреть","#1F5A7A"],stay:["Где остановиться","#7A4A8C"],eat:["Где поесть","#B3261E"],shop:["Где купить","#A0740A"],art:["Архитектура и искусство","#2F6B4A"],craft:["Мастерские","#4E6E8E"]};
var ART=__ART__, P=__PINS__;
var map=L.map("kg-leaflet",{scrollWheelZoom:false}).setView(__VIEW__);
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
<!-- /__KEY__-map -->'''
CATS={'see':['Посмотреть','#1F5A7A'],'stay':['Где остановиться','#7A4A8C'],'eat':['Где поесть','#B3261E'],'shop':['Где купить','#A0740A'],'art':['Архитектура и искусство','#2F6B4A'],'craft':['Мастерские','#4E6E8E']}
ANCHOR='<script>\n\n(function(){\n  // ---- production dataset'

def build(key):
    spec=importlib.util.spec_from_file_location(key,os.path.join(REPO,'tools','prefs',key+'.py'))
    C=importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
    SRC=os.path.expanduser(C.SRC); OUT=os.path.join(REPO,'articles',key)
    slug=getattr(C,'slug',default_slug)
    folders=sorted(d for d in os.listdir(SRC) if os.path.isdir(os.path.join(SRC,d)) and d not in C.SKIP and os.path.exists(os.path.join(SRC,d,'article_ru.html')))
    num={}; titles={}
    bar=BAR.replace('__KEY__',key).replace('__BACK__',C.BAR_BACK)
    for d in folders:
        s=slug(d); num[d[:2]]=s
        src=open(os.path.join(SRC,d,'article_ru.html'),encoding='utf-8').read()
        m=re.search(r'<h1[^>]*>(.*?)</h1>',src,re.S); titles[s]=re.sub(r'<[^>]+>','',m.group(1)).strip()
        if '<!-- site-bar -->' not in src:
            src=re.sub(r'(<body[^>]*>)',lambda m:m.group(1)+'\n'+bar,src,count=1)
        out=os.path.join(OUT,s); os.makedirs(out,exist_ok=True)
        open(os.path.join(out,'index.html'),'w',encoding='utf-8').write(src)
        imd=os.path.join(SRC,d,'images')
        if os.path.isdir(imd):
            shutil.copytree(imd,os.path.join(out,'images'),dirs_exist_ok=True,ignore=shutil.ignore_patterns('.DS_Store'))
    def A(*nums): return [num[n] for n in nums]
    P=C.pins(A)  # [name, area, category, lat, lng, approx, [article slugs]]
    used={a for p in P for a in p[6]}
    allnums=set(num); grouped={n for g in C.GROUPS for n in g[1]}
    assert allnums==grouped, (allnums-grouped, grouped-allnums)
    art_js={s:titles[s] for s in titles}
    pins_js=[dict(n=p[0],a=p[1],c=p[2],la=p[3],ln=p[4],x=p[5],s=p[6]) for p in P]
    lst=[]
    for g,ns in C.GROUPS:
        items=''.join(f'<li><a href="{num[n]}/index.html">{html.escape(titles[num[n]])}</a>{"" if num[n] in used else " <span class=\"kg-nopin\">без точки на карте</span>"}</li>' for n in ns)
        lst.append(f'<div class="kg-group"><h4>{g}</h4><ul>{items}</ul></div>')
    places=f'{len(P)} {plural(len(P),"место","места","мест")}'
    section_map=(SECTION_MAP.replace('__KEY__',key).replace('__MAP_TITLE__',C.MAP_TITLE).replace('__ARIA__',C.ARIA)
        .replace('__VIEW__',C.VIEW).replace('__INTRO__',C.INTRO.format(places=places))
        .replace('__ART__',json.dumps(art_js,ensure_ascii=False)).replace('__PINS__',json.dumps(pins_js,ensure_ascii=False)))
    section_list=f'''<!-- {key}-articles --><p class="kicker" id="{key}-articles">Наши статьи</p><h2>{C.LIST_TITLE}</h2><div class="kg-articles">{"".join(lst)}</div><!-- /{key}-articles -->'''
    page_path=os.path.join(OUT,'index.html'); page=open(page_path,encoding='utf-8').read()
    page=re.sub(rf'<!-- {key}-map -->.*?<!-- /{key}-map -->','',page,flags=re.S)
    page=re.sub(rf'<!-- {key}-articles -->.*?<!-- /{key}-articles -->','',page,flags=re.S)
    page=re.sub(r'<p class="kg-jump"[^>]*>.*?</p>','',page,flags=re.S)
    n_art=len(titles)
    jump=f'<p class="kg-jump" style="font-size:16px;margin:16px 0 0"><a href="#{key}-map">Карта: {places} из {n_art} {"статьи" if n_art%10==1 and n_art%100!=11 else "статей"}</a> · <a href="#{key}-articles">{C.LIST_LINK}</a></p>'
    page=page.replace('</p><p class="kicker" id="about">','</p>'+jump+section_map+'<p class="kicker" id="about">',1)
    page=page.replace('</div></article>',section_list+'</div></article>',1)
    assert f'{key}-map -->' in page and f'{key}-articles' in page
    open(page_path,'w',encoding='utf-8').write(page)
    print(key+':',len(titles),'articles,',len(P),'pins; nopin:',sorted(s for s in titles if s not in used))

    # Same pins on the top-page Japan map (index.html): shown when the user zooms into this prefecture.
    top_path=os.path.join(REPO,'index.html'); top=open(top_path,encoding='utf-8').read()
    def card(s):
        """Photo + short lead for the top-map popover: thumb.jpg made from the article's first image (macOS sips)."""
        d=os.path.join(OUT,s); src=open(os.path.join(d,'index.html'),encoding='utf-8').read()
        m=re.search(r'<p class="lede"[^>]*>(.*?)</p>',src,re.S) or re.search(r'<p>(.*?)</p>',src,re.S)
        lede=html.unescape(re.sub(r'<[^>]+>','',m.group(1))).strip() if m else ''
        if len(lede)>170: lede=lede[:170].rsplit(' ',1)[0].rstrip(' ,.;:—')+'…'
        c={'t':titles[s],'u':f'articles/{key}/{s}/index.html','l':lede}
        im=re.search(r'<img[^>]+src="([^"]+)"',src)
        if im and not im.group(1).startswith(('http','data:')):
            img=os.path.normpath(os.path.join(d,im.group(1))); th=os.path.join(d,'thumb.jpg')
            if os.path.exists(img):
                if not os.path.exists(th) or os.path.getmtime(th)<os.path.getmtime(img):
                    os.system(f'sips -Z 600 -s format jpeg -s formatOptions 72 "{img}" --out "{th}" >/dev/null')
                c['i']=f'articles/{key}/{s}/thumb.jpg'
        return c
    top_data=dict(cats=CATS,art={s:card(s) for s in titles},pins=pins_js)
    section_top=f'<!-- {key}-japan-pins --><script>window.{C.TOP_VAR}={json.dumps(top_data,ensure_ascii=False)};</script><!-- /{key}-japan-pins -->\n'
    if f'<!-- {key}-japan-pins -->' in top:
        top=re.sub(rf'<!-- {key}-japan-pins -->.*?<!-- /{key}-japan-pins -->\n',lambda m:section_top,top,flags=re.S)
    else:
        assert ANCHOR in top; top=top.replace(ANCHOR,section_top+ANCHOR,1)
    open(top_path,'w',encoding='utf-8').write(top)
    print(f'index.html: {key} pins on the Japan map updated')

if __name__=='__main__':
    keys=sys.argv[1:] or sorted(f[:-3] for f in os.listdir(os.path.join(REPO,'tools','prefs')) if f.endswith('.py'))
    for k in keys: build(k)
