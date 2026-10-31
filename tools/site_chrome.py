"""Shared parts of every article page (the 47 prefecture guides and their sub-articles): the 雅 logo in the site-bar.
Usage: python3 tools/site_chrome.py   (all pages under articles/; idempotent). pref_map_build.py applies it to the pages it writes."""
import os, re, sys
REPO=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# the logo: 雅 in the homepage's style (Cormorant Garamond 500, ink colour), linking to the homepage
BRAND_CSS='.site-bar .brand{font-family:"Cormorant Garamond",serif;font-size:28px;font-weight:500;line-height:1}'

def brand(page):
    page=re.sub(r'<a class="brand" href="([^"]*)"[^>]*>[^<]*</a>',lambda m:f'<a class="brand" href="{m.group(1)}" aria-label="雅, на главную">雅</a>',page,count=1)
    return re.sub(r'\.site-bar \.brand\{[^}]*\}',lambda m:BRAND_CSS,page,count=1)

def apply(page):
    return brand(page)

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
