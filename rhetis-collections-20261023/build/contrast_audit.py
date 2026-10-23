import json,asyncio,sys,re
from pathlib import Path
from playwright.async_api import async_playwright
WORK=Path('/workspace/work/integration');OUT=Path('/workspace/output')
JS=r'''() => {
const cache={},cv=document.createElement('canvas');cv.width=cv.height=1;const ctx=cv.getContext('2d',{willReadFrequently:true});
const rgb=s=>{if(cache[s])return cache[s];ctx.clearRect(0,0,1,1);ctx.fillStyle=s;ctx.fillRect(0,0,1,1);return cache[s]=Array.from(ctx.getImageData(0,0,1,1).data).map((v,i)=>i===3?v/255:v)};
const over=(a,b)=>{let k=a[3]+b[3]*(1-a[3]);return [0,1,2].map(i=>(a[i]*a[3]+b[i]*b[3]*(1-a[3]))/k).concat(k)};
const lum=c=>[0.2126,0.7152,0.0722].reduce((v,k,i)=>v+k*(c[i]/255<=.04045?c[i]/255/12.92:((c[i]/255+.055)/1.055)**2.4),0);
let root=document.querySelector('.body').firstElementChild,bad=[],walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);
while(walker.nextNode()){
let node=walker.currentNode,el=node.parentElement,s=getComputedStyle(el),text=node.textContent.trim();
if(!text||!el.getClientRects().length||s.visibility==='hidden')continue;
let range=document.createRange();range.selectNodeContents(node);let tr=range.getBoundingClientRect();let ancestors=[],a=el,gradient=false;while(a){ancestors.push(a);a=a.parentElement;}
let bg=rgb(getComputedStyle(document.querySelector('.slide')).getPropertyValue('--page').trim());for(let anc of ancestors.reverse()){let q=getComputedStyle(anc);if(q.backgroundImage!=='none')gradient=true;let ar=anc.getBoundingClientRect();if(anc===el||(ar.left<=tr.left+1&&ar.right>=tr.right-1&&ar.top<=tr.top+1&&ar.bottom>=tr.bottom-1))bg=over(rgb(q.backgroundColor),bg);}
let fg=over(rgb(s.color),bg),l1=lum(fg),l2=lum(bg),ratio=(Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05),limit=parseFloat(s.fontSize)>=28?3:4.5;
if(ratio<limit-.05)bad.push({text:text.slice(0,60),class:el.className,size:s.fontSize,color:s.color,background:bg,ratio:Math.round(ratio*100)/100,required:limit,gradientAncestor:gradient});
}
return bad;
}'''
async def main(name):
 results=[]
 async with async_playwright() as p:
  b=await p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=await b.new_page(viewport={'width':1280,'height':720})
  await page.goto('http://127.0.0.1:8760/'+name+'-audit.html')
  for f in sorted((OUT/name).glob('elements/*/fixtures/*.html')):
   body=re.sub(r'<!--.*?-->','',f.read_text(),flags=re.S)
   for mode in ['light','dark']:
    await page.evaluate('(html)=>document.body.innerHTML=html','<section class="slide'+(' dark' if mode=='dark' else '')+'"><div class="page"><div class="body">'+body+'</div></div></section>')
    await page.evaluate('document.fonts.ready')
    issues=await page.evaluate(JS)
    if issues:results.append({'fixture':str(f.relative_to(OUT/name)),'mode':mode,'issues':issues})
  await b.close()
 (WORK/(name+'-contrast-audit.json')).write_text(json.dumps(results,ensure_ascii=False,indent=2))
 print(name,len(results),'fixtures with color concerns')
if __name__=='__main__':asyncio.run(main(sys.argv[1]))
