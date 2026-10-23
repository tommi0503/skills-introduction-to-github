import sys
sys.path.insert(0,'/workspace/work/tools')
import render_review as rr
from playwright.sync_api import sync_playwright
from pathlib import Path
with sync_playwright() as p:
 b=rr.browser(p);page=b.new_page(viewport={'width':1280,'height':720});rr.load(page,Path('/workspace/work/deliverables/nocturne/review/library/light.html'))
 page.evaluate('''()=>{const a=[...document.querySelectorAll('body>article')].find(e=>e.querySelector('h2').textContent.startsWith('sankey / sankey-3'));document.body.innerHTML=a.querySelector('.slide').outerHTML;}''')
 page.add_style_tag(content='body{margin:0;padding:0;display:block;width:1280px;height:720px}body>.slide{width:1280px;height:720px;transform:none}')
 print(page.evaluate('''()=>[...document.querySelectorAll('.sankey>.branch')].map(e=>{let s=getComputedStyle(e,'::before'),r=e.getBoundingClientRect();return {v:e.style.getPropertyValue('--v'),rect:{x:r.x,y:r.y,w:r.width,h:r.height},left:s.left,right:s.right,top:s.top,bottom:s.bottom,width:s.width,height:s.height,clip:s.clipPath,bg:s.backgroundColor,z:s.zIndex,content:s.content}})'''))
 page.screenshot(path='/workspace/work/deliverables/nocturne/build/sankey-probe.png');b.close()
