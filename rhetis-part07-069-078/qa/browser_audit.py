"""Ask the actual Chromium parser whether source selectors/declarations are supported."""
from pathlib import Path
import json,sys
from playwright.sync_api import sync_playwright
from audit_css import BASE,COLLECTIONS,parse_rules,split_top,declarations

def records(text):
 out=[]
 for prelude,body,line in parse_rules(text):
  if prelude.startswith('@'):
   if prelude.startswith(('@container','@media','@supports')):out.extend(records(body))
  elif prelude!='!PARSE':out.append({'selector':prelude,'selectors':split_top(prelude),'line':line,'declarations':list(declarations(body))})
 return out

if __name__=='__main__':
 selected=sys.argv[1:] or COLLECTIONS
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
  page=browser.new_page();page.goto('http://127.0.0.1:8765/qa/probe.html')
  for kid in selected:
   root=BASE/(kid+'-project')/kid;findings=[];count=0
   for source in sorted(root.rglob('*.css')):
    items=records(source.read_text());count+=len(items)
    errors=page.evaluate(r'''records=>{const errors=[];for(const r of records){for(const sel of r.selectors)if(!CSS.supports('selector('+sel+')'))errors.push({rule:'browser-selector',selector:sel,line:r.line});for(const [prop,value] of r.declarations){if(prop.startsWith('--'))continue;if(!CSS.supports(prop,value.replace(/\s*!important\s*$/i,'')))errors.push({rule:'browser-declaration',selector:r.selector,property:prop,value:value,line:r.line});}}return errors;}''',items)
    for e in errors:e['file']=str(source.relative_to(root));findings.append(e)
   result={'collection':kid,'ruleCount':count,'unsupported':findings,'browserVersion':browser.version}
   (BASE/'qa'/(kid+'-browser-css-audit.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
   print(kid,count,'rules',len(findings),'unsupported')
  browser.close()
