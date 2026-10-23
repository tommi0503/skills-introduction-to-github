from pathlib import Path
from playwright.sync_api import sync_playwright
import json,re,sys
B=Path(__file__).parent;AUDIT=(B/'render.py').read_text().split("AUDIT=r'''",1)[1].split("'''",1)[0]
CONTRAST='''() => {
 const canvas=document.createElement('canvas');canvas.width=canvas.height=1;const ctx=canvas.getContext('2d');
 function rgba(c){ctx.clearRect(0,0,1,1);ctx.fillStyle=c;ctx.fillRect(0,0,1,1);return [...ctx.getImageData(0,0,1,1).data].map((x,i)=>i===3?x/255:x/255)}
 function lum(a){return a.slice(0,3).map(x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4).reduce((s,x,i)=>s+x*[.2126,.7152,.0722][i],0)}
 const out=[];const root=document.querySelector('article.review-active .slide'); if(!root)return out;
 for(const n of root.querySelectorAll('[data-el] *')){if(![...n.childNodes].some(x=>x.nodeType===3&&x.textContent.trim()))continue;const st=getComputedStyle(n),r=n.getBoundingClientRect();if(st.display==='none'||st.visibility==='hidden'||!r.width||!r.height)continue;
 const fg=rgba(st.color);let bg=[1,1,1,1];const ancestors=[];for(let a=n;a&&root.contains(a);a=a.parentElement)ancestors.push(a);
 for(const a of ancestors.reverse()){const c=rgba(getComputedStyle(a).backgroundColor);bg=c.map((x,i)=>i===3?1:c[3]*x+(1-c[3])*bg[i])}
 const l1=lum(fg),l2=lum(bg),ratio=(Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05),needed=parseFloat(st.fontSize)>=28?3:4.5;
 if(ratio<needed-.03)out.push({text:n.textContent.slice(0,50),el:n.closest('[data-el]').dataset.el,part:n.className,ratio:Math.round(ratio*100)/100,size:st.fontSize,color:st.color,background:bg});
 }return out;
}'''
a={'sizes':{},'contrast':{},'centering':{},'tested':0}
with sync_playwright() as w:
 b=w.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);p=b.new_page(viewport={'width':1280,'height':720})
 for mode in ['light','dark']:
  p.goto('http://127.0.0.1:8765/anchor-frame-review/library/'+mode+'.html');p.evaluate('document.fonts.ready');p.add_style_tag(content='body{display:block;padding:0;margin:0}article{display:none}article.review-active{display:block}article.review-active>h2{display:none}.frame{width:1280px;height:720px;border-radius:0}.frame>.slide{transform:none}')
  for idx in range(p.locator('article').count()):
   p.evaluate('(i)=>document.querySelectorAll("article").forEach((a,k)=>a.classList.toggle("review-active",i===k))',idx);title=p.locator('article').nth(idx).locator(':scope > h2').inner_text()
   if title.startswith('foundation'):continue
   if len(sys.argv)>1 and not title.startswith(sys.argv[1]+' /'):continue
   contrast=p.evaluate(CONTRAST)
   if contrast:a['contrast'][mode+'/'+title]=contrast
   minimum=re.search(r'min\s+(\d+)x(\d+)',title);mc,mr=map(int,minimum.groups()) if minimum else (12,6)
   for c in range(mc,13):
    for r in range(mr,7):
     p.evaluate('([i,c,r])=>{for(const n of document.querySelectorAll("article")[i].querySelectorAll(".body > *")){n.style.gridColumn="1 / span "+c;n.style.gridRow="1 / span "+r}}',[idx,c,r]);errs=p.evaluate(AUDIT);a['tested']+=1
     if errs:a['sizes'][mode+'/'+title+f'/{c}x{r}']=errs
 b.close()
(B/('all-sizes-'+sys.argv[1]+'-audit.json' if len(sys.argv)>1 else 'all-sizes-audit.json')).write_text(json.dumps(a,ensure_ascii=False,indent=2));print('cases',a['tested'],'size failure cases',len(a['sizes']),'contrast fixture cases',len(a['contrast']))
for k,v in a['contrast'].items():
 if k.startswith('light'):print('CONTRAST',k,str(v)[:250])
for k,v in a['sizes'].items():
 if k.startswith('light'):print('SIZE',k,str(v)[:220])
