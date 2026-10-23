from playwright.sync_api import sync_playwright
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);g=b.new_page(viewport={'width':1280,'height':720})
 for i in [8,11]:
  g.goto(f'http://127.0.0.1:8767/reassembled/slide_{i:02}.html');g.evaluate('document.fonts.ready');print(i,g.evaluate('''()=>[...document.querySelectorAll('.donut,.headline,.headline>.kick,.headline>h2,.headline>.note,.stat,.stat .fig,.stat .note,.stat .name')].map(e=>{let r=e.getBoundingClientRect(),s=getComputedStyle(e);return [e.className,[r.x,r.y,r.width,r.height],s.fontSize,s.gap,s.marginTop]})'''))
 b.close()
