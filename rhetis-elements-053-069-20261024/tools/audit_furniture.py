"""Independently audit page furniture in both palettes, leaving source pages untouched."""
import asyncio,io,json,time
from pathlib import Path
from PIL import Image
from playwright.async_api import async_playwright
from element_sheets import ratio
ROOT=Path(__file__).resolve().parents[1]
JS=r'''()=>{
 const cc=document.createElement('canvas'),ctx=cc.getContext('2d'),text=[];
 const rgba=c=>{ctx.clearRect(0,0,1,1);ctx.fillStyle=c;ctx.fillRect(0,0,1,1);return [...ctx.getImageData(0,0,1,1).data]};
 let n;const w=document.createTreeWalker(document.querySelector('.slide'),NodeFilter.SHOW_TEXT);
 while(n=w.nextNode()){
  if(!n.textContent.trim()||n.parentElement.closest('svg,script,style'))continue;
  let e=n.parentElement,s=getComputedStyle(e),r=document.createRange();r.selectNodeContents(n);
  for(const b of r.getClientRects()){
   if(!b.width||!b.height)continue;
   text.push({text:n.textContent.trim(),box:[b.x,b.y,b.width,b.height],color:rgba(s.color),size:parseFloat(s.fontSize),font:s.fontFamily,weight:s.fontWeight});
  }
 }
 return{fontStatus:document.fonts.status,fontErrors:[...document.fonts].filter(x=>x.status==='error').map(x=>x.family),text};
}'''
async def main():
 report=[]
 async with async_playwright()as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);a=await b.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for item in json.loads((ROOT/'collections.json').read_text()):
   for f in sorted((ROOT/(item['id']+'-review')/'reassembled').glob('*.html')):
    for mode in ['light','dark']:
     await a.goto('http://127.0.0.1:8766/'+str(f.relative_to(ROOT))+'?furniture='+str(time.time_ns()));await a.evaluate('document.fonts.ready')
     await a.evaluate("m=>{document.querySelector('.body')?.remove();document.querySelector('.slide').classList.toggle('dark',m==='dark')}",mode)
     data=await a.evaluate(JS);normal=Image.open(io.BytesIO(await a.screenshot())).convert('RGB')
     await a.add_style_tag(content='.slide *{-webkit-text-fill-color:transparent!important;text-shadow:none!important}')
     bg=Image.open(io.BytesIO(await a.screenshot())).convert('RGB');contrast=[];outside=[];overlap=[]
     for t in data['text']:
      x,y,w,h=t['box'];cr=min(ratio(t['color'],bg.getpixel((min(1279,max(0,round(x+w*k))),min(719,max(0,round(y+h*.5))))))for k in [.25,.5,.75]);threshold=3 if t['size']>=28 else 4.5
      if cr+.02<threshold:contrast.append({**t,'contrast':round(cr,2),'required':threshold})
      if x<-.5 or y<-.5 or x+w>1280.5 or y+h>720.5:outside.append(t)
     for i,t in enumerate(data['text']):
      for u in data['text'][i+1:]:
       x,y,w,h=t['box'];xx,yy,ww,hh=u['box'];iw=min(x+w,xx+ww)-max(x,xx);ih=min(y+h,yy+hh)-max(y,yy)
       if iw>3 and ih>min(h,hh)*.42 and iw*ih>min(w*h,ww*hh)*.25:overlap.append([t['text'],u['text']])
     report.append({'collection':item['id'],'page':f.stem,'mode':mode,'fontErrors':data['fontErrors'],'contrast':contrast,'outside':outside,'overlap':overlap})
   print(item['id'],'furniture audited',flush=True)
  await b.close()
 (ROOT/'furniture-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('flagged',sum(bool(x['contrast']or x['outside']or x['overlap']or x['fontErrors'])for x in report))
if __name__=='__main__':asyncio.run(main())
