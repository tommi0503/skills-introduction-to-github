from pathlib import Path
from playwright.sync_api import sync_playwright
import json,sys
sys.path.insert(0,"/workspace/work/tools")
from render_review import load
R=Path('/workspace/work/deliverables/dockside');C=R/'collection/dockside';V=R/'review'
css=''.join(p.read_text() for p in [C/'foundation/foundation.css',C/'elements/chart-donut/element.css',C/'kit/css/tokens.css'])
css+=(V/'assets/environment.css').read_text()
f=(C/'elements/chart-donut/fixtures/donuts-4.html').read_text().replace('span 12','span 4').replace('span 6','span 3')
p=R/'build/probe.html';p.write_text('<!doctype html><style>body{margin:0}'+css+'</style><section class="slide"><div class="page"><div class="body">'+f+'</div></div></section>')
with sync_playwright() as pp:
 b=pp.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage']);pg=b.new_page(viewport={'width':1280,'height':720});load(pg,p);pg.screenshot(path=str(R/'build/probe.png'));print(pg.locator('.donuts,.donut').evaluate_all('(es)=>es.map(e=>({c:e.className,r:e.getBoundingClientRect().toJSON(),w:getComputedStyle(e).width,h:getComputedStyle(e).height,container:getComputedStyle(e).containerType,count:getComputedStyle(e).getPropertyValue("--dockside-count")}))'));print(pg.evaluate('CSS.supports("width","calc((min(100cqw,100cqh) - 24px*2)/2)")'));print(pg.evaluate('CSS.supports("width","calc((min(100cqw,100cqh) - 24px * 2) / 2)")'));print(pg.locator('.donut').first.evaluate('(e)=>({gap:getComputedStyle(e).getPropertyValue("--gap"), pad:getComputedStyle(e).getPropertyValue("--pad"), matches:e.matches(".donuts:has(>.donut:nth-child(4))>.donut")})'));pg.add_style_tag(content='.donuts[data-el="dockside-chart-donut"]>.donut[data-el="dockside-chart-donut"]{width:calc((min(100cqw,100cqh) - 48px)/2);height:calc((min(100cqw,100cqh) - 48px)/2)}');print(pg.locator('.donut').first.bounding_box());print(pg.locator('.donut').first.evaluate('(e)=>{let a=[];function f(rs){for(let r of rs){if(r.cssRules?.length)f(r.cssRules);if(r.selectorText&&e.matches(r.selectorText)&&r.style.width)a.push([r.selectorText,r.style.width,r.style.height]);}} for(let s of document.styleSheets)f(s.cssRules);return a}'));b.close()
