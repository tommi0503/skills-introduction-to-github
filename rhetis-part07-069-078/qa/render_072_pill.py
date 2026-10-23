import json,importlib.util
from playwright.sync_api import sync_playwright
from audit_css import BASE,REFERENCE
s=importlib.util.spec_from_file_location('pv',REFERENCE/'tools/preview.py');pv=importlib.util.module_from_spec(s);s.loader.exec_module(pv)
m=pv.sheet(BASE/'seedmark-project/seedmark',json.loads((REFERENCE/'contract/type-steps.json').read_text()),json.loads((REFERENCE/'contract/palette.json').read_text()),fonts_href='/seedmark-project/assets/fonts/fonts.css',dark=True)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);q=b.new_page(viewport={'width':1360,'height':900});q.goto('http://127.0.0.1:8765/qa/probe.html');q.set_content(m,wait_until='networkidle');q.evaluate('document.fonts.ready')
 for text,size in [('pill / pill-stack',[4,3])]:
  a=q.locator('article').filter(has=q.locator('h2',has_text=text)).first
  q.locator('article').evaluate_all("all=>all.forEach(a=>a.style.display='none')");a.evaluate("a=>a.style.display='block'")
  a.evaluate('''(a,size)=>{let f=a.querySelector('.frame');f.style.width='1280px';f.style.height='720px';f.querySelector('.slide').style.transform='none';let body=a.querySelector('.body');for(let e of body.children){e.style.gridColumn='1 / span '+size[0];e.style.gridRow='1 / span '+size[1]}}''',size)
  a.locator('.slide').screenshot(path=str(BASE/'qa'/('072-'+text.split(' / ')[-1]+'.png')))
 b.close()
