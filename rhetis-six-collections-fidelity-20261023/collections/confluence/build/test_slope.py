from pathlib import Path
from playwright.sync_api import sync_playwright
q='.slope[data-el="confluence-slope"]:not(.dumbbell)'
s=f'''{q} .pair::before{{content:none}}{q} .pair::after{{--confluence-rise:max(0,sign(var(--b) - var(--a)));content:"";position:absolute;left:anchor(var(--confluence-slope-a) center);right:anchor(var(--confluence-slope-b) center);top:calc(min(anchor(var(--confluence-slope-a) center),anchor(var(--confluence-slope-b) center)) - 1px);bottom:calc(min(anchor(var(--confluence-slope-a) center),anchor(var(--confluence-slope-b) center)) - 1px);width:auto;height:auto;background:var(--n-4);clip-path:polygon(0 calc(var(--confluence-rise)*100% - 1px),100% calc((1 - var(--confluence-rise))*100% - 1px),100% calc((1 - var(--confluence-rise))*100% + 1px),0 calc(var(--confluence-rise)*100% + 1px))}}{q} .pair.on::after{{background:var(--a1)}}'''
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);pg=b.new_page();pg.goto('http://127.0.0.1:8020/review/library/light.html');pg.evaluate('document.fonts.ready');pg.add_style_tag(content=s)
 print(pg.locator('.slope:not(.dumbbell)').first.evaluate('e=>[...e.querySelectorAll(".pair")].map(p=>({after:Object.fromEntries(["top","bottom","height","width","clipPath"].map(k=>[k,getComputedStyle(p,"::after")[k]]))}))'))
 pg.locator('.slope:not(.dumbbell)').first.screenshot(path='/workspace/work/deliverables/confluence/build/slope-test.png');b.close()
Path('/workspace/work/deliverables/confluence/build/slope_geometry.css').write_text(s)
