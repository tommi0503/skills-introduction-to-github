"""Review the two foundation fixtures at native slide size in both palettes."""
from pathlib import Path
import sys,json
from playwright.sync_api import sync_playwright
sys.path.insert(0,'/workspace/work/rhetis-elements-v2/tools');from sheets import AUDIT
P=Path(__file__).parent;K=P/'vectorbox';D=P/'sheets';pal=json.loads(Path('/workspace/work/reference/contract/palette.json').read_text());out=[]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);q=b.new_page(viewport={'width':1280,'height':720})
 for name in ['seat','cover']:
  for mode in ['light','dark']:
   markup=(K/'foundation/fixtures'/f'{name}.html').read_text()
   if mode=='dark':markup=markup.replace('class="slide','class="slide dark',1)
   variables='.slide'+('.dark' if mode=='dark' else '')+'{'+''.join(k+':'+v+';' for k,v in pal[mode].items())+'}'
   links=['../assets/fonts/fonts.css','../assets/type-steps.css','../vectorbox/kit/css/tokens.css','../vectorbox/foundation/foundation.css']
   path=D/f'foundation-{name}-{mode}.html';path.write_text('<!doctype html><html lang="ko"><meta charset="utf-8">'+''.join('<link rel="stylesheet" href="'+v+'">' for v in links)+'<style>html,body{margin:0;width:1280px;height:720px;overflow:hidden}'+variables+'</style><body>'+markup+'</body></html>')
   q.goto('http://127.0.0.1:8875/vectorbox-project/sheets/'+path.name);q.evaluate('document.fonts.ready');q.screenshot(path=str(path.with_suffix('.png')));d=q.locator('.slide').evaluate(AUDIT);d.update({'fixture':name,'mode':mode});out.append(d)
 b.close()
(D/'foundation-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('Foundation2fixtures4native renders complete')
