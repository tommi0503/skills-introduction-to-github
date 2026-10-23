import json,asyncio,sys,re
from pathlib import Path
from playwright.async_api import async_playwright
BASE=Path('/workspace/output');WORK=Path('/workspace/work/integration')
async def main(names):
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  for name in names:
   page=await b.new_page(viewport={'width':1280,'height':720});await page.goto('http://127.0.0.1:8760/'+name+'-audit.html')
   allchecks=[]
   for f in sorted((BASE/name).glob('elements/*/fixtures/*.html')):
    if f.parts[-3] not in ['card','pill','tag','architecture','agenda','steps','timeline']:continue
    html=re.sub(r'<!--.*?-->','',f.read_text(),flags=re.S)
    await page.evaluate('(h)=>document.body.innerHTML=h','<section class="slide"><div class="page"><div class="body">'+html+'</div></div></section>');await page.evaluate('document.fonts.ready')
    checks=await page.evaluate('''()=>Array.from(document.querySelectorAll('.tag,.chip,.mark')).filter(el=>el.childElementCount===0&&el.textContent.trim()&&el.getClientRects().length).filter(el=>{let s=getComputedStyle(el);return !el.matches('.mark')||s.backgroundImage!=='none'||(s.backgroundColor!=='rgba(0, 0, 0, 0)'&&s.backgroundColor!=='transparent')||parseFloat(s.borderTopWidth)>0}).map(el=>{let b=el.getBoundingClientRect(),r=document.createRange();r.selectNodeContents(el);let q=r.getBoundingClientRect();return{text:el.textContent.trim(),class:el.className,dx:Math.round((q.x+q.width/2-b.x-b.width/2)*100)/100,dy:Math.round((q.y+q.height/2-b.y-b.height/2)*100)/100,box:[b.width,b.height],font:getComputedStyle(el).fontFamily}})''')
    for c in checks:c['fixture']=str(f.relative_to(BASE/name));c['aligned']=abs(c['dx'])<=4 and abs(c['dy'])<=4
    allchecks+=checks
   (WORK/(name+'-chip-audit.json')).write_text(json.dumps({'collection':name,'method':'Rendered text range and chip box centers; 4px tolerance, followed by visual review','checked':len(allchecks),'alignment_candidates':[c for c in allchecks if not c['aligned']],'checks':allchecks},ensure_ascii=False,indent=2))
   print(name,len(allchecks),'chip centers',sum(not c['aligned'] for c in allchecks),'review candidates',flush=True)
   await page.close()
  await b.close()
asyncio.run(main(sys.argv[1:]))
