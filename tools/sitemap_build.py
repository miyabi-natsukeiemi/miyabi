"""Write sitemap.xml: the homepage, /services/, every prefecture guide and every article.
Usage: python3 tools/sitemap_build.py   (pref_map_build.py runs it after a build)."""
import os
REPO=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE='https://miyabi-concierge.pages.dev'  # production address; change it here when the site gets its own domain

def build():
    urls=['/','/services/']
    for root,dirs,files in os.walk(os.path.join(REPO,'articles')):
        dirs[:]=sorted(d for d in dirs if d not in ('img','images'))
        if 'index.html' in files: urls.append('/'+os.path.relpath(root,REPO).replace(os.sep,'/')+'/')
    xml=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    xml+=[f'  <url><loc>{SITE}{u}</loc></url>' for u in urls]
    xml.append('</urlset>')
    open(os.path.join(REPO,'sitemap.xml'),'w',encoding='utf-8').write('\n'.join(xml)+'\n')
    return len(urls)

if __name__=='__main__':
    print('sitemap.xml:',build(),'URLs')
