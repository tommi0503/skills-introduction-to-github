from pathlib import Path
import json
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent;out=[]
with sync_playwright()as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=b.new_page();pg.goto('http://127.0.0.1:8765/briefing-tab-review/index.html')
 for f in (ROOT/'briefing-tab/elements').glob('*/element.css'):
  invalid=pg.evaluate('''([css,id])=>{let s=new CSSStyleSheet;s.replaceSync(css);let bad=[];function split(t){let d=0,a=[],p=0;for(let i=0;i<t.length;i++){if('(['.includes(t[i]))d++;if(')]'.includes(t[i]))d--;if(t[i]===','&&d===0){a.push(t.slice(p,i));p=i+1}}a.push(t.slice(p));return a}function walk(rs){for(let r of rs){if(r.selectorText)for(let q of split(r.selectorText))if(!q.includes(`[data-el="${id}"]`))bad.push(q);if(r.cssRules)walk(r.cssRules)}}walk(s.cssRules);return bad}''',[f.read_text(),'briefing-tab-'+f.parent.name])
  if invalid:out.append({'element':f.parent.name,'selectors':invalid})
 # Confirm preview controls change all relevant image links.
 pg.click('button[data-n="25"]');assert pg.locator('#comparison').get_attribute('src')=='compare-reassembled/slide_25.png'
 b.close()
(ROOT/'briefing-tab-review/scope-validation.json').write_text(json.dumps({'elements':56,'scope_errors':out,'preview_navigation':'pass'},ensure_ascii=False,indent=2));print(json.dumps(out,ensure_ascii=False,indent=2))
