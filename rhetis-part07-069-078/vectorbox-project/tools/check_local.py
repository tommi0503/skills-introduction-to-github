from pathlib import Path
from playwright.sync_api import sync_playwright
P=Path(__file__).parent;O=P/'qa';O.mkdir(exist_ok=True)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1400,'height':900})
 page.goto('http://127.0.0.1:8871/library/light.html');page.evaluate('document.fonts.ready');page.add_style_tag(content='body{grid-template-columns:1280px}.frame{width:1280px;height:720px}.frame>.slide{transform:none}')
 for name in ['chart-line / lines-12','chart-area / areas-stacked-3','chart-area / areas-2','chart-donut / donuts-3','card / card-4']:
  a=page.locator('article').filter(has=page.locator('h2',has_text=name)).first;a.locator('.frame').screenshot(path=str(O/(name.replace(' / ','-')+'.png')))
 print(page.locator('[data-el="vectorbox-chart-line"] .pt').nth(1).evaluate("e=>({before:{background:getComputedStyle(e,'::before').background,width:getComputedStyle(e,'::before').width,height:getComputedStyle(e,'::before').height},after:{background:getComputedStyle(e,'::after').background,width:getComputedStyle(e,'::after').width,height:getComputedStyle(e,'::after').height}})"))
 b.close()
