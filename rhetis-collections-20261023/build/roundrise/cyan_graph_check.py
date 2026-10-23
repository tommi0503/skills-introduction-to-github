from pathlib import Path
import asyncio,json,re
from playwright.async_api import async_playwright
B=Path('/workspace/output/cyanloop');R=Path('/workspace/work/reference');O=Path('/workspace/work/roundrise/cyan-check');O.mkdir(exist_ok=True)
E=['journey','mindmap','sankey','hierarchy','decision-tree']
css=(B/'kit/css/tokens.css').read_text()+(B/'foundation/foundation.css').read_text()
p=json.loads((R/'contract/palette.json').read_text());css+=''.join(('.slide.dark' if m=='dark' else '.slide')+'{'+''.join(k+':'+str(v)+';' for k,v in d.items())+'}' for m,d in p.items())
css+='.slide{'+''.join('--type-'+str(s)+':'+str(s)+'px;' for s in json.loads((R/'contract/type-steps.json').read_text()))+'}'
for e in E:css+=(B/'elements'/e/'element.css').read_text();j=json.loads((B/'elements'/e/'element.json').read_text());css+='.slide{'+''.join(k+':'+v+';' for k,v in j['tokenDefaults'].items())+'}'
async def go():
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  pg=await b.new_page(viewport={'width':1280,'height':720})
  await pg.goto('http://127.0.0.1:8760/cyanloop-audit.html')
  await pg.set_content('<!doctype html><html><meta charset="utf-8"><link rel="stylesheet" href="http://127.0.0.1:8760/fonts/fonts.css"><style>body{margin:0}'+css+'</style><body></body>')
  for e in E:
   for f in sorted((B/'elements'/e/'fixtures').glob('*.html')):
    txt=f.read_text();mi=re.search(r'min:\s*(\d+)x(\d+)',txt);c,r=map(int,mi.groups())
    txt=re.sub(r'<!--.*?-->','',txt,flags=re.S)
    for size in ['full','min']:
     await pg.evaluate('(h)=>document.body.innerHTML=h','<section class="slide"><div class="page"><div class="body">'+txt+'</div></div></section>')
     if size=='min':await pg.locator('.body').evaluate('(el,p)=>{el.firstElementChild.style.gridColumn="1 / span "+p[0];el.firstElementChild.style.gridRow="1 / span "+p[1]}',[c,r])
     await pg.evaluate('document.fonts.ready')
     await pg.screenshot(path=str(O/(e+'-'+f.stem+'-'+size+'.png')))
  await b.close()
asyncio.run(go())
