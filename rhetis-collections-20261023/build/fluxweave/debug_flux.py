from playwright.sync_api import sync_playwright
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=b.new_page();pg.goto('http://127.0.0.1:8762/library/light.html')
 print(pg.locator('[data-el="fluxweave-radar"][style*="--n:8"]>.series').evaluate_all('''ns=>ns.map(n=>({values:n.getAttribute('style'),clip:getComputedStyle(n,'::before').clipPath,ax:n.parentElement.querySelectorAll('.axis').length,max:getComputedStyle(n).getPropertyValue('--max')}))'''))
 print(pg.locator('[data-el="fluxweave-slope"]:not(.dumbbell)>.pair').first.evaluate('''n=>({root:n.parentElement.getBoundingClientRect().toJSON(),pair:n.getBoundingClientRect().toJSON(),width:getComputedStyle(n,'::after').width,matrix:getComputedStyle(n,'::after').transform,rotate:getComputedStyle(n,'::after').rotate})'''))
 b.close()
