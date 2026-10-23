import sys,json
sys.path.insert(0,'/workspace/work/tools');import render_review as rr
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
 b=rr.browser(p);pg=b.new_page(viewport={'width':1280,'height':720});rr.load(pg,'/workspace/work/deliverables/diecut/review/reassembled/slide-01.html')
 print(pg.evaluate('''()=>[...document.querySelectorAll('.prose,.body')].map(e=>({tag:e.className,r:e.getBoundingClientRect().toJSON(),css:getComputedStyle(e).cssText,bg:getComputedStyle(e).backgroundColor,opacity:getComputedStyle(e).opacity,display:getComputedStyle(e).display,flex:getComputedStyle(e).flex,text:e.textContent.slice(0,40)}))'''))
 b.close()
