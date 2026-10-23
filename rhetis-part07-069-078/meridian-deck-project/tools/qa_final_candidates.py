from pathlib import Path
import importlib.util,json
from playwright.sync_api import sync_playwright
P=Path(__file__).parent;B=P.parent;R=Path('/workspace/work/reference');s=importlib.util.spec_from_file_location('pv',R/'tools/preview.py');pv=importlib.util.module_from_spec(s);s.loader.exec_module(pv)
requests=[('foundation / source-composition-09',12,6,False,'source09-light'),('hub / hub-4',6,3,True,'hub4-min-dark'),('person / person ',6,3,False,'person-min-light'),('foundation / source-composition-24',12,6,False,'source24-light'),('pyramid / pyramid-3',4,3,False,'pyramid3-min-light'),('pyramid / pyramid-4',6,4,False,'pyramid4-min-light')]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);q=b.new_page(viewport={'width':1280,'height':720});q.goto('http://127.0.0.1:8765/qa/probe.html')
 for title,c,r,dark,name in requests:
  m=pv.sheet(P/'meridian-deck',json.loads((R/'contract/type-steps.json').read_text()),json.loads((R/'contract/palette.json').read_text()),dark=dark,fonts_href='/meridian-deck-project/assets/fonts/fonts.css');q.set_content(m,wait_until='networkidle');q.evaluate('document.fonts.ready')
  a=q.locator('article').filter(has=q.locator('h2').filter(has_text=title)).first
  if a.count()!=1:raise Exception(title)
  a.evaluate('''(a,sz)=>{for(let x of document.querySelectorAll('article'))if(x!==a)x.style.display='none';document.body.style.padding='0';a.querySelector('h2').style.display='none';let f=a.querySelector('.frame');f.style.width='1280px';f.style.height='720px';f.style.borderRadius='0';f.querySelector('.slide').style.transform='none';let body=a.querySelector('.body');if(body&&!a.querySelector('h2').textContent.startsWith('foundation /'))for(const el of body.children){el.style.gridColumn='1 / span '+sz[0];el.style.gridRow='1 / span '+sz[1]}}''',[c,r])
  a.locator('.frame').first.screenshot(path=str(B/'qa'/f'meridian-final-{name}.png'))
  if 'source09' in name:print('rulewidth',a.locator('.card .name').first.evaluate("e=>{let out=[];function walk(rs){for(let r of rs){if(r.cssRules)walk(r.cssRules);else if(r.selectorText&&e.matches(r.selectorText)&&r.style.width)out.push([r.selectorText,r.style.width]);}}for(let s of document.styleSheets)walk(s.cssRules);return [getComputedStyle(e).cssText,out,getComputedStyle(e.parentElement).gridTemplateColumns,getComputedStyle(e).width]}"));print('source09',a.locator('.card,.card .parts,.card .name').evaluate_all('es=>es.slice(0,3).map(e=>{let r=e.getBoundingClientRect(),s=getComputedStyle(e);return {cl:e.className,x:r.x,y:r.y,w:r.width,h:r.height,p:s.padding,margin:s.margin,pos:s.position,inset:s.inset}})'))
  if 'source24' in name:print('source24 boxes',a.locator('.frame[data-el],.seat').evaluate_all('es=>es.map(e=>{let r=e.getBoundingClientRect();return {cl:e.className,x:r.x,y:r.y,w:r.width,h:r.height}})'))
 b.close()
