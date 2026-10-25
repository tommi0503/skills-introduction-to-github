"""Render fresh assembly, with automatic page/font/text diagnostics and 3-way PNGs."""
import argparse,asyncio,hashlib,io,json,math,re,time
from pathlib import Path
from PIL import Image,ImageChops,ImageDraw
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
def dependency_manifest(cid):
 C=ROOT/cid;R=ROOT/(cid+'-review')
 files=[ROOT/'runtime.css',R/'runtime-defaults.css',R/'map.json',ROOT/'foundation-geometry.json',ROOT/'collections.json',ROOT/'tools/build_reassembled.py',ROOT/'tools/render_reassembled.py',ROOT/'contract/palette.json',ROOT/'contract/type-steps.json',ROOT/'round5/furniture-additions.json']
 files+=sorted(p for p in C.rglob('*')if p.is_file()and p.suffix in ['.css','.json'])
 for directory in [ROOT/'fonts',ROOT/'assets',ROOT/'reference/frozen'/(cid+'-review')/'replica',ROOT/'reference/originals'/cid]:
  files+=sorted(p for p in directory.rglob('*')if p.is_file())
 files+=sorted((R/'reassembled').glob('*.html'))
 return{str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest()for f in files}
AUDIT=r'''()=>{
 const slide=document.querySelector('.slide'),s=slide.getBoundingClientRect(),text=[],outside=[],overlap=[],roots=[];
 for(const root of slide.querySelectorAll('.body>:is([data-el],.panel,.seat)')){
  const b=root.getBoundingClientRect();roots.push({element:root.dataset.el||'foundation-panel',box:[b.x,b.y,b.width,b.height]});
 }
 const walk=document.createTreeWalker(slide,NodeFilter.SHOW_TEXT);let n;
 while(n=walk.nextNode()){
  if(!n.textContent.trim()||n.parentElement.closest('style,script,svg'))continue;
  const e=n.parentElement,style=getComputedStyle(e);if(style.display==='none'||style.visibility==='hidden')continue;
  const range=document.createRange();range.selectNodeContents(n);
  for(const b of range.getClientRects()){
   if(b.width<.5||b.height<.5)continue;
   const owner=e.closest('[data-el]')||e.closest('.panel')||slide,ob=owner.getBoundingClientRect();
   const entry={text:n.textContent.trim().slice(0,100),root:owner.dataset?.el||'foundation',box:[b.x,b.y,b.width,b.height],font:style.fontFamily,size:style.fontSize};text.push(entry);
   if(b.left<ob.left-2||b.right>ob.right+2||b.top<ob.top-2||b.bottom>ob.bottom+2)outside.push({...entry,kind:'root'});
   if(b.left<-.5||b.right>1280.5||b.top<-.5||b.bottom>720.5)outside.push({...entry,kind:'page'});
  }
 }
 for(let i=0;i<text.length;i++)for(let j=i+1;j<text.length;j++){
  let a=text[i],b=text[j],w=Math.min(a.box[0]+a.box[2],b.box[0]+b.box[2])-Math.max(a.box[0],b.box[0]),h=Math.min(a.box[1]+a.box[3],b.box[1]+b.box[3])-Math.max(a.box[1],b.box[1]);
  if(w>3&&h>Math.min(a.box[3],b.box[3])*.42&&w*h>Math.min(a.box[2]*a.box[3],b.box[2]*b.box[3])*.25)overlap.push({a:a.text,b:b.text,roots:[a.root,b.root],width:w,height:h});
 }
 return{pageSize:[s.width,s.height],documentSize:[document.documentElement.scrollWidth,document.documentElement.scrollHeight],fontStatus:document.fonts.status,fontErrors:[...document.fonts].filter(f=>f.status==='error').map(f=>f.family),loadedFonts:[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family),roots,outside,overlap};
}'''
async def main(args):
 all_audits=[]
 async with async_playwright()as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
  page=await browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for item in json.loads((ROOT/'collections.json').read_text()):
   cid=item['id']
   if args.collections and cid not in args.collections:continue
   R=ROOT/(cid+'-review');out=R/'reassembled';compare=R/'compare-reassembled';compare.mkdir(exist_ok=True)
   audits=[];inputs=dependency_manifest(cid);input_hash=hashlib.sha256(json.dumps(inputs,sort_keys=True).encode()).hexdigest()
   for f in sorted(out.glob('slide_*.html')):
    nn=re.search(r'(\d+)\.html$',f.name)[1];errors=[]
    handler=lambda response:errors.append({'status':response.status,'url':response.url})if response.status>=400 else None
    page.on('response',handler)
    await page.goto(args.url+'/'+str(f.relative_to(ROOT))+'?revision='+str(time.time_ns()),wait_until='networkidle')
    await page.evaluate('document.fonts.ready');await page.evaluate('window.scrollTo(0,0)')
    audit=await page.evaluate(AUDIT);audit.update({'collection':cid,'page':nn,'errors':errors,'htmlSHA256':hashlib.sha256(f.read_bytes()).hexdigest(),'inputsSHA256':input_hash})
    target=f.with_suffix('.png');normal_bytes=await page.screenshot(path=str(target));normal=Image.open(io.BytesIO(normal_bytes)).convert('RGB');audit['pngSHA256']=hashlib.sha256(target.read_bytes()).hexdigest();audit['paintOverflow']=[]
    nodes=page.locator('.body>:is([data-el],.panel,.seat)')
    for index in range(await nodes.count()):
     node=nodes.nth(index);original_style=await node.get_attribute('style');bounds=await node.bounding_box();name=await node.get_attribute('data-el')or'foundation-panel'
     await node.evaluate("e=>e.style.setProperty('visibility','hidden','important')")
     empty=Image.open(io.BytesIO(await page.screenshot())).convert('RGB')
     await node.evaluate("(e,s)=>s===null?e.removeAttribute('style'):e.setAttribute('style',s)",original_style)
     diff=ImageChops.difference(normal,empty);channels=diff.split();mask=ImageChops.lighter(ImageChops.lighter(channels[0],channels[1]),channels[2]).point(lambda v:255 if v>24 else 0)
     x,y,w,h=[bounds[k]for k in ['x','y','width','height']];ImageDraw.Draw(mask).rectangle((math.floor(x-1.5),math.floor(y-1.5),math.ceil(x+w+1.5),math.ceil(y+h+1.5)),fill=0);ink=mask.getbbox();pixels=mask.histogram()[255]
     if ink and pixels>8:
      # Hiding a root may rerasterize a sibling SVG edge. Attribute paint only
      # after an independent pass with every sibling hidden, preserving layout.
      candidate={'root':name,'pixels':pixels,'box':list(ink)}
      saved=await nodes.evaluate_all("es=>es.map(e=>e.getAttribute('style'))")
      await nodes.evaluate_all("es=>es.forEach(e=>e.style.setProperty('visibility','hidden','important'))")
      await node.evaluate("(e,s)=>s===null?e.removeAttribute('style'):e.setAttribute('style',s)",original_style)
      isolated=Image.open(io.BytesIO(await page.screenshot())).convert('RGB')
      await node.evaluate("e=>e.style.setProperty('visibility','hidden','important')")
      blank=Image.open(io.BytesIO(await page.screenshot())).convert('RGB')
      await nodes.evaluate_all("(es,ss)=>es.forEach((e,i)=>ss[i]===null?e.removeAttribute('style'):e.setAttribute('style',ss[i]))",saved)
      channels=ImageChops.difference(isolated,blank).split();owned=ImageChops.lighter(ImageChops.lighter(channels[0],channels[1]),channels[2]).point(lambda v:255 if v>24 else 0)
      ImageDraw.Draw(owned).rectangle((math.floor(x-1.5),math.floor(y-1.5),math.ceil(x+w+1.5),math.ceil(y+h+1.5)),fill=0)
      isolated_ink=owned.getbbox();isolated_pixels=owned.histogram()[255]
      audit.setdefault('paintOwnershipChecks',[]).append({'candidate':candidate,'method':'Same root visible/hidden with sibling roots isolated, preserving their layout boxes','ownedPixels':isolated_pixels,'ownedBox':list(isolated_ink)if isolated_ink else None})
      if isolated_ink and isolated_pixels>8:audit['paintOverflow'].append({'root':name,'pixels':isolated_pixels,'box':list(isolated_ink)})
    page.remove_listener('response',handler)
    original=next((ROOT/'reference/originals'/cid).glob('*'+nn+'.png'))
    # Preserve the user's existing replica PNG in the middle column.
    replica=next((ROOT/'reference/frozen'/(cid+'-review')/'replica').glob('*'+nn+'.png'))
    canvas=Image.new('RGB',(3840,720),'white')
    for k,path in enumerate([original,replica,target]):
     im=Image.open(path).convert('RGB');assert im.size==(1280,720),(str(path),im.size);canvas.paste(im,(1280*k,0))
    canvas.save(compare/('slide_'+nn+'.png'));audits.append(audit)
    print(cid,nn,'outside',len(audit['outside']),'overlaps',len(audit['overlap']),'paint',len(audit['paintOverflow']),'http',len(errors),flush=True)
   after=dependency_manifest(cid);stale=after!=inputs
   for audit in audits:audit['staleDuringRender']=stale
   (R/'reassembled-dependencies.json').write_text(json.dumps({'sha256':input_hash,'files':inputs,'staleDuringRender':stale},ensure_ascii=False,indent=2))
   (R/'reassembled-audit.json').write_text(json.dumps(audits,ensure_ascii=False,indent=2));all_audits+=audits
  await browser.close()
 (ROOT/'reassembled-audit.json').write_text(json.dumps(all_audits,ensure_ascii=False,indent=2))
if __name__=='__main__':
 p0=argparse.ArgumentParser();p0.add_argument('collections',nargs='*');p0.add_argument('--url',default='http://127.0.0.1:8767');asyncio.run(main(p0.parse_args()))
