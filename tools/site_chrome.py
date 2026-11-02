"""Shared parts of every article page (the 47 prefecture guides and their sub-articles): the brand logo in the site-bar, the
closing call to action and, in <head>, the site icons and the share tags (Open Graph, Twitter; og:image = the article's
first photo).
Usage: python3 tools/site_chrome.py   (all pages under articles/; idempotent). pref_map_build.py applies it to the pages it writes."""
import os, re, sys, html
from sitemap_build import SITE
REPO=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BRAND='omamori'  # the brand name (provisional spelling): logo, CTA label, og:site_name. pref_map_build.py uses it too

# the logo: the brand name in the homepage's style (Cormorant Garamond 500, ink colour), linking to the homepage
BRAND_CSS='.site-bar .brand{font-family:"Cormorant Garamond",serif;font-size:28px;font-weight:500;line-height:1}'

def brand(page):
    page=re.sub(r'<a class="brand" href="([^"]*)"[^>]*>[^<]*</a>',lambda m:f'<a class="brand" href="{m.group(1)}" aria-label="{BRAND}, на главную">{BRAND}</a>',page,count=1)
    return re.sub(r'\.site-bar \.brand\{[^}]*\}',lambda m:BRAND_CSS,page,count=1)

# closing call to action, at the end of the page (before </body>; the editorial comments some articles end with are invisible)
CTA='''<!-- site-cta -->
<style>.site-cta{max-width:712px;margin:0 auto;padding:0 16px 88px;text-align:center;font-family:"PT Serif",Georgia,serif;color:#141414}
.site-cta .in{border-top:2px solid #141414;padding-top:40px}
.site-cta *{box-sizing:border-box;letter-spacing:normal}.site-cta h2{border:0;padding:0;text-align:center}  /* older article templates style bare h2 */
.site-cta h2{font-family:"Playfair Display",Georgia,serif;font-weight:600;font-style:italic;font-size:clamp(26px,4vw,34px);line-height:1.2;margin:0 0 28px;text-wrap:balance}
.site-cta .go{display:flex;flex-wrap:wrap;gap:14px 28px;justify-content:center;align-items:center;font-family:Inter,system-ui,sans-serif;font-size:16px}
.site-cta .btn{display:inline-flex;align-items:center;min-height:48px;padding:0 26px;border-radius:999px;background:#B3261E;color:#fff;text-decoration:none}
.site-cta .btn:hover{background:#8F1E18}
.site-cta .sv{color:#141414;text-decoration:none;border-bottom:1px solid #DADADA;padding-bottom:2px}
.site-cta .sv:hover{color:#B3261E;border-color:#B3261E}
.site-cta a:focus-visible{outline:2px solid #B3261E;outline-offset:3px}</style>
<aside class="site-cta" aria-label="Поездка с __BRAND__"><div class="in"><h2>Хотите поехать сюда? Соберём маршрут под вас</h2>
<div class="go"><a class="btn" href="/#ask">Написать нам</a><a class="sv" href="/services/">Услуги</a></div></div></aside>
<!-- /site-cta -->
'''

def cta(page):
    page=re.sub(r'<!-- site-cta -->.*?<!-- /site-cta -->\n?','',page,flags=re.S)
    i=page.rfind('</body>')
    return page[:i]+CTA.replace('__BRAND__',BRAND)+page[i:] if i>-1 else page

# in <head>: the site icons (files at the site root, made from favicon.svg)
ICONS='''<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">'''

def share(page,url):
    """Open Graph and Twitter tags. url: the page's address on the site, e.g. /articles/kagawa/guntu/"""
    a=lambda v:html.escape(html.unescape(v),quote=True)
    m=re.search(r'<title>(.*?)</title>',page,re.S); title=a(m.group(1).strip()) if m else BRAND
    m=re.search(r'<meta name="description" content="([^"]*)"',page); desc=a(m.group(1)) if m else ''
    body=page[page.find('<body'):]
    img=next((s for s in re.findall(r'<img[^>]+src="([^"]+)"',body) if not s.startswith(('http','data:'))),None)
    img=SITE+(re.sub(r'/[^/]*/\.\./','/',url+img) if img else '/assets/og.jpg')
    tags=[('property','og:type','article'),('property','og:site_name',BRAND),('property','og:locale','ru_RU'),('property','og:title',title),
        ('property','og:description',desc),('property','og:url',SITE+url),('property','og:image',img),('name','twitter:card','summary_large_image'),
        ('name','twitter:title',title),('name','twitter:description',desc),('name','twitter:image',img)]
    return '\n'.join(f'<meta {k}="{n}" content="{v}">' for k,n,v in tags)

def head(page,url):
    page=re.sub(r'<!-- site-head -->.*?<!-- /site-head -->\n?','',page,flags=re.S)
    i=page.find('</head>')
    return page[:i]+'<!-- site-head -->\n'+ICONS+'\n'+share(page,url)+'\n<!-- /site-head -->\n'+page[i:] if i>-1 else page

def url_of(path):
    return '/'+os.path.relpath(os.path.dirname(path),REPO).replace(os.sep,'/')+'/'

def apply(page,path):
    """path: where the page is written (articles/<pref>/[<slug>/]index.html)"""
    return head(cta(brand(page)),url_of(path))

def run(paths):
    n=0
    for p in paths:
        s=open(p,encoding='utf-8').read(); t=apply(s,p)
        if t!=s: open(p,'w',encoding='utf-8').write(t); n+=1
    return n

def all_pages():
    for root,dirs,files in os.walk(os.path.join(REPO,'articles')):
        dirs[:]=[d for d in dirs if d not in ('img','images')]
        if 'index.html' in files: yield os.path.join(root,'index.html')

if __name__=='__main__':
    print(run(all_pages()),'pages updated')
