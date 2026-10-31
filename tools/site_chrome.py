"""Shared parts of every article page (the 47 prefecture guides and their sub-articles): the 雅 logo in the site-bar and the
closing call to action.
Usage: python3 tools/site_chrome.py   (all pages under articles/; idempotent). pref_map_build.py applies it to the pages it writes."""
import os, re, sys
REPO=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# the logo: 雅 in the homepage's style (Cormorant Garamond 500, ink colour), linking to the homepage
BRAND_CSS='.site-bar .brand{font-family:"Cormorant Garamond",serif;font-size:28px;font-weight:500;line-height:1}'

def brand(page):
    page=re.sub(r'<a class="brand" href="([^"]*)"[^>]*>[^<]*</a>',lambda m:f'<a class="brand" href="{m.group(1)}" aria-label="雅, на главную">雅</a>',page,count=1)
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
<aside class="site-cta" aria-label="Поездка с 雅"><div class="in"><h2>Хотите поехать сюда? Соберём маршрут под вас</h2>
<div class="go"><a class="btn" href="/#ask">Написать нам</a><a class="sv" href="/services/">Услуги</a></div></div></aside>
<!-- /site-cta -->
'''

def cta(page):
    page=re.sub(r'<!-- site-cta -->.*?<!-- /site-cta -->\n?','',page,flags=re.S)
    i=page.rfind('</body>')
    return page[:i]+CTA+page[i:] if i>-1 else page

def apply(page):
    return cta(brand(page))

def run(paths):
    n=0
    for p in paths:
        s=open(p,encoding='utf-8').read(); t=apply(s)
        if t!=s: open(p,'w',encoding='utf-8').write(t); n+=1
    return n

def all_pages():
    for root,dirs,files in os.walk(os.path.join(REPO,'articles')):
        dirs[:]=[d for d in dirs if d not in ('img','images')]
        if 'index.html' in files: yield os.path.join(root,'index.html')

if __name__=='__main__':
    print(run(all_pages()),'pages updated')
