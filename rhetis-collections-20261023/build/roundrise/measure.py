from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']); pg=b.new_page(viewport={'width':1280,'height':720})
 for i in [6,14,23]:
  pg.goto(f'http://127.0.0.1:8767/reassembled/slide_{i:02}.html');pg.evaluate('document.fonts.ready')
  print(i,pg.evaluate('''()=>[...document.querySelectorAll('.body,.head,.headline,.headline>.kick,.headline>h2,.headline>.note,.card,.card .name,.card .mark,.card .note,.bars')].map(e=>{let r=e.getBoundingClientRect(),s=getComputedStyle(e);return [e.className,e.textContent.slice(0,30),[r.x,r.y,r.width,r.height],s.fontSize,s.paddingTop,s.justifyContent,s.backgroundColor]})'''))
 b.close()
