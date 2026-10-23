from playwright.sync_api import sync_playwright
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page();page.goto('http://127.0.0.1:8760/glass-contract-proof.html')
 print(page.locator('[data-el="glasspulse-cycle"]>.node').first.evaluate('''n=>{let s=getComputedStyle(n),a=getComputedStyle(n,'::after');return {trim:s.getPropertyValue('--glasspulse-trim'),bg:a.background,height:a.height,clip:getComputedStyle(n).overflow,valid:CSS.supports('background','linear-gradient(90deg,transparent 70px,red 70px,red calc(100% - 70px),transparent calc(100% - 70px))'),mix:CSS.supports('color','color-mix(in srgb,white 0%,white 0%)')}}'''))
 b.close()
