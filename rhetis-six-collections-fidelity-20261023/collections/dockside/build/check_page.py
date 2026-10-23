import sys,json
sys.path.insert(0,'/workspace/work/tools')
from render_review import load,browser
from playwright.sync_api import sync_playwright
from pathlib import Path
with sync_playwright() as p:
 b=browser(p);page=b.new_page(viewport={'width':1280,'height':720});load(page,Path('/workspace/work/deliverables/dockside/review/reassembled/slide_26.html'));print(page.locator('.head,.title,.kicker').evaluate_all('(es)=>es.map(e=>({c:e.className,t:e.textContent,r:e.getBoundingClientRect().toJSON(),disp:getComputedStyle(e).display,vis:getComputedStyle(e).visibility,op:getComputedStyle(e).opacity}))'));page.screenshot(path='/workspace/work/deliverables/dockside/build/page26.png');print(page.locator('.title').evaluate('(e)=>({color:getComputedStyle(e).color,z:getComputedStyle(e).zIndex,hit:document.elementFromPoint(250,150).outerHTML.slice(0,400)})'));b.close()
