from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).parent
with sync_playwright() as w:
 b=w.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);g=b.new_page(viewport={'width':1360,'height':1000});g.goto('http://127.0.0.1:8765/crossrail-project/qa/final-light.html');g.evaluate('document.fonts.ready')
 for label,cols,rows in [('funnel / funnel-5',6,3),('pyramid / pyramid-3',4,3),('heatmap / calendar-12',6,3),('callout / callout-stack',6,2),('concentric / orbit-4',6,4)]:
  a=g.locator('article').filter(has=g.locator('h2',has_text=label)).first
  a.locator('.body').evaluate('(e,v)=>{let c=e.firstElementChild;c.style.gridColumn="1/span "+v[0];c.style.gridRow="1/span "+v[1]}',[cols,rows]);g.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');g.wait_for_timeout(100);a.screenshot(path=str(p/'qa'/('minimum-'+label.split(' / ')[0]+'.png')))
 b.close()
print('minimum probes done')
