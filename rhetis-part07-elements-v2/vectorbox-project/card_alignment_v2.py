from playwright.sync_api import sync_playwright
from pathlib import Path
import json,re
P=Path(__file__).parent;out=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage']);page=b.new_page(viewport={'width':1280,'height':720});page.goto('http://127.0.0.1:8875/vectorbox-project/sheet-runtime/stage-card.html')
 for f in sorted((P/'vectorbox/elements/card/fixtures').glob('card-*.html')):
  for size in [(12,6),tuple(map(int,re.search(r'min:\s*(\d+)x(\d+)',f.read_text()).groups()))]:
   page.locator('.body').evaluate('(e,args)=>{e.innerHTML=args[0];const r=e.firstElementChild;r.style.gridColumn="1 / span "+args[1][0];r.style.gridRow="1 / span "+args[1][1]}',[f.read_text(),size]);page.evaluate('document.fonts.ready')
   v=page.locator('.body>.group').evaluate('''e=>[...e.querySelectorAll('.parts')].map(p=>({name:p.querySelector('.name')?.getBoundingClientRect().y??null,fig:p.querySelector('.fig')?.getBoundingClientRect().y??null,kick:p.querySelector('.kick')?.getBoundingClientRect().y??null}))''')
   d={key:(max(vals)-min(vals) if len(vals)>1 else None) for key in ['name','fig','kick'] if (vals:=[x[key] for x in v if x[key] is not None])};out.append({'fixture':f.name,'size':size,'positions':v,'drift':d})
 b.close()
(P/'card-alignment-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
for x in out:print(x['fixture'],x['size'],x['drift'])
