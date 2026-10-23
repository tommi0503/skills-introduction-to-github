from pathlib import Path
import json,re,asyncio,sys
from playwright.async_api import async_playwright
BASE=Path('/workspace/output');WORK=Path('/workspace/work/integration')
async def main(names):
 results=[]
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=await b.new_page()
  for name in names:
   entries=[]
   for f in list((BASE/name).glob('elements/*/element.css'))+[BASE/name/'foundation/foundation.css']:
    clean=re.sub(r'/\*.*?\*/','',f.read_text(),flags=re.S)
    for selector in re.findall(r'([^{}]+)\{',clean):
     selector=selector.strip()
     if selector and not selector.startswith('@'):
      depth=0;parts=[];start=0
      for i,ch in enumerate(selector):
       if ch in '([':depth+=1
       elif ch in ')]':depth-=1
       elif ch==',' and depth==0:parts.append(selector[start:i]);start=i+1
      parts.append(selector[start:])
      for part in parts:entries.append({'file':str(f.relative_to(BASE/name)),'selector':part.strip()})
   bad=await page.evaluate('(items)=>items.filter(x=>!CSS.supports("selector("+x.selector+")"))',entries)
   results.append({'collection':name,'selectors_tested':len(entries),'invalid_selectors':bad});print(name,len(entries),len(bad),'invalid selectors',flush=True)
  await b.close()
 (WORK/'selector-audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
asyncio.run(main(sys.argv[1:]))
