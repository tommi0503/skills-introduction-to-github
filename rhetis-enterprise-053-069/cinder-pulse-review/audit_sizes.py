import asyncio,json
from pathlib import Path
from playwright.async_api import async_playwright
B=Path(__file__).parent
async def main():
 report=[]
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=await b.new_page(viewport={'width':1280,'height':720})
  for mode in ['light','dark']:
   await page.goto('http://127.0.0.1:8765/cinder-pulse-review/library/'+mode+'.html');await page.evaluate('document.fonts.ready')
   result=await page.evaluate('''()=>{const result=[];for(const a of document.querySelectorAll('article')){let label=a.querySelector('h2').textContent, min=label.match(/min (\\d+)x(\\d+)/),root=a.querySelector('.body')?.firstElementChild;if(!root||!min)continue;let old=root.getAttribute('style'),count=0,bad=[];for(let w=+min[1];w<=12;w++)for(let h=+min[2];h<=6;h++){root.style.gridColumn='1 / span '+w;root.style.gridRow='1 / span '+h;let b=root.getBoundingClientRect();let problems=[];for(let e of root.querySelectorAll('.name,.note,.fig,.chip,.kick,p,td,th')){if(!e.textContent.trim()||getComputedStyle(e).display==='none')continue;let r=e.getBoundingClientRect();if(r.width&&r.height&&(r.left<b.left-1||r.right>b.right+1||r.top<b.top-1||r.bottom>b.bottom+1))problems.push(e.className||e.tagName);}count++;if(problems.length)bad.push({size:w+'x'+h,parts:[...new Set(problems)]});}root.setAttribute('style',old||'');result.push({label,count,failures:bad});}return result}''')
   report.append(dict(mode=mode,fixtures=result))
  await b.close()
 (B/'size-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('tested',sum(x['count'] for m in report for x in m['fixtures']),'size-mode combinations');print('failures',sum(len(x['failures']) for m in report for x in m['fixtures']))
asyncio.run(main())
