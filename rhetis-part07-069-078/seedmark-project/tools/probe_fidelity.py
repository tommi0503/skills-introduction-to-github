import asyncio,json,re
from pathlib import Path
from playwright.async_api import async_playwright
P=Path(__file__).parent;C=P/'seedmark';D=P/'local-review/fidelity-probes';D.mkdir(parents=True,exist_ok=True)
css=(C/'kit/css/tokens.css').read_text()+(C/'foundation/foundation.css').read_text()+''.join(p.read_text()for p in(C/'elements').glob('*/element.css'))
steps=json.loads(Path('/workspace/work/reference/contract/type-steps.json').read_text());css+='.slide{'+''.join(f'--type-{n}:{n}px;'for n in steps)+'}'
pal=json.loads(Path('/workspace/work/reference/contract/palette.json').read_text());css+=''.join(('.slide.dark'if mode=='dark'else'.slide')+'{'+''.join(f'{n}:{v};'for n,v in vals.items())+'}'for mode,vals in pal.items())
for p in (C/'elements').glob('*/element.json'):
 defaults=json.loads(p.read_text())['tokenDefaults'];css+='.slide{'+''.join(f'{n}:{v};'for n,v in defaults.items())+'}'
spec=[('flowchart', 'system-cylinders'), ('flowchart', 'controller-gateway-devices'), ('timeline', 'photo-phases-5'), ('steps', 'icon-cycle-5'), ('card', 'hanging-icon-3'), ('pill', 'database-cylinders-3'), ('chart-donut', 'pie-allocation'), ('tag', 'milestone-label'), ('person', 'people-5-leader'), ('card', 'revenue-plans-4'), ('agenda', 'agenda-11'), ('metric', 'allocation-details-2'), ('prose', 'technology-heading')]
import sys
if len(sys.argv)>1:spec=[x for x in spec if x[0] in sys.argv[1:]]
async def main():
 checks=[]
 async with async_playwright()as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=await b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for n,fixture in spec:
   f=C/'elements'/n/'fixtures'/(fixture+'.html');body=f.read_text();m=re.search(r'min:\s*(\d+)x(\d+)',body);cw,ch=map(int,m.groups())if m else(12,6)
   for mode in ['light','dark']:
    for size in ['full','min']:
     src=body
     if size=='min':src=re.sub(r'grid-column:\s*1\s*/\s*span\s*12;\s*grid-row:\s*1\s*/\s*span\s*6',f'grid-column:1/span {cw};grid-row:1/span {ch}',src,count=1)
     key=f'{n}-{fixture}-{mode}-{size}';html='<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="/assets/fonts/fonts.css"><style>'+css+'</style><section class="slide '+('dark'if mode=='dark'else'')+'"><div class="page"><div class="body">'+src+'</div></div></section>'
     (D/(key+'.html')).write_text(html)
     await page.goto('http://127.0.0.1:8765/seedmark-project/local-review/fidelity-probes/'+key+'.html');await page.evaluate('document.fonts.ready');await page.screenshot(path=str(D/(key+'.png')))
     if size=='full'and mode=='light':
      data=await page.evaluate('''()=>[...document.querySelectorAll('[data-el]')].map(e=>({el:e.dataset.el,cls:e.className,w:e.getBoundingClientRect().width,h:e.getBoundingClientRect().height,before:[getComputedStyle(e,'::before').width,getComputedStyle(e,'::before').height],after:[getComputedStyle(e,'::after').width,getComputedStyle(e,'::after').height]}))''');checks.append({'fixture':key,'data':data})
  await b.close()
 (D/'checks.json').write_text(json.dumps(checks,indent=2));print('Probed',len(spec)*4,'screens')
asyncio.run(main())
