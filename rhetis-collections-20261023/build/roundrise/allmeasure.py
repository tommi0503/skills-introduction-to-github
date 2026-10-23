from playwright.sync_api import sync_playwright
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);g=b.new_page(viewport={'width':1280,'height':720})
 for i in [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24]:
  g.goto(f'http://127.0.0.1:8767/reassembled/slide_{i:02}.html');g.evaluate('document.fonts.ready')
  print(i,g.evaluate('''()=>[...document.querySelectorAll('.body,.body>.headline,.body>.card,.body>.posmap,.body>.steps,.body>.track,.group>.card,.headline>.kick,.headline>h2,.headline>.note,.areas,.stat,.card .name,.bars')].map(e=>{let r=e.getBoundingClientRect(),s=getComputedStyle(e);return [e.className,e.textContent.slice(0,15),[r.x,r.y,r.width,r.height].map(n=>Math.round(n)),s.fontSize,s.backgroundColor]})'''))
 b.close()
