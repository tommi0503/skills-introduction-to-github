from pathlib import Path
import sys,json
sys.path.insert(0,'/workspace/work/tools')
from render_review import load,browser
from playwright.sync_api import sync_playwright
R=Path('/workspace/work/deliverables/dockside')
with sync_playwright() as p:
 b=browser(p);page=b.new_page(viewport={'width':1280,'height':720})
 for n in [5,30]:
  load(page,R/f'review/reassembled/slide_{n:02}.html');page.wait_for_timeout(600);print(n,page.locator('.head,.title,.body,.pill').evaluate_all('(es)=>es.map(e=>({c:e.className,r:e.getBoundingClientRect().toJSON(),z:getComputedStyle(e).zIndex,pos:getComputedStyle(e).position,col:getComputedStyle(e).color,disp:getComputedStyle(e).display}))'));page.screenshot(path=str(R/f'build/current{n}.png'))
 b.close()
