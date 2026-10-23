from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);g=b.new_page(viewport={'width':700,'height':500});g.goto('http://127.0.0.1:8765/qa/anchor-math.html');g.screenshot(path='/workspace/work/rhetis-part07/qa/anchor-math.png');print(g.evaluate('''()=>[...document.querySelectorAll('.pt')].map(e=>{let p=getComputedStyle(e,'::before');return {rect:e.getBoundingClientRect().toJSON(),before:{left:p.left,right:p.right,top:p.top,bottom:p.bottom,w:p.width,h:p.height,background:p.backgroundImage}}})'''));b.close()
