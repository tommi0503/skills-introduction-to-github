import sys
sys.path.insert(0,'/workspace/work/tools')
from render_review import browser,load
from playwright.sync_api import sync_playwright
from pathlib import Path
with sync_playwright() as p:
 b=browser(p);q=b.new_page(viewport={'width':1280,'height':720})
 for n,sel in [(28,'.person>.name'),(29,'.mark>.icon'),(17,'.core')]:
  load(q,Path(f'/workspace/work/deliverables/dockside/review/reassembled/slide_{n:02}.html'));print(n,q.locator(sel).evaluate_all('(es)=>es.map(e=>({text:e.textContent,css:getComputedStyle(e).cssText,font:getComputedStyle(e).fontSize,w:e.getBoundingClientRect().width,h:e.getBoundingClientRect().height}))'))
 b.close()
