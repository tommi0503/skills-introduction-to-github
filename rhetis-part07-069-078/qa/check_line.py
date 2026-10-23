from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);g=b.new_page(viewport={'width':1360,'height':900});g.goto('http://127.0.0.1:8765/vectorbox-project/library/light.html');g.evaluate('document.fonts.ready')
 d=g.evaluate('''()=>{let e=document.querySelector('[data-el="vectorbox-chart-line"]'),out=[];for(let p of [...e.children].slice(0,3)){let s=getComputedStyle(p),x=getComputedStyle(p,'::before');out.push({rect:p.getBoundingClientRect().toJSON(),anchor:s.anchorName,before:{pos:x.position,left:x.left,right:x.right,top:x.top,bottom:x.bottom,w:x.width,h:x.height,background:x.backgroundImage,z:x.zIndex}})}return {root:e.getBoundingClientRect().toJSON(),scope:getComputedStyle(e).anchorScope,out}}''');print(json.dumps(d,indent=2));b.close()
