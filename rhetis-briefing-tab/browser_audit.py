from pathlib import Path
import json,re
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent;R=ROOT/'briefing-tab-review';C=ROOT/'briefing-tab'
# Audits text ranges, visible boxes and computed colours rather than whole-image pixel similarity.
AUDIT=r'''() => {
const root=document.querySelector('.slide'), box=root.getBoundingClientRect(), issues=[], rects=[];
const cv=document.createElement('canvas');cv.width=cv.height=1;const cx=cv.getContext('2d',{willReadFrequently:true});
function rgba(s){cx.clearRect(0,0,1,1);cx.fillStyle=s;cx.fillRect(0,0,1,1);return Array.from(cx.getImageData(0,0,1,1).data)}
function lum(a){let x=a.slice(0,3).map(v=>{v/=255;return v<=.04045?v/12.92:((v+.055)/1.055)**2.4});return .2126*x[0]+.7152*x[1]+.0722*x[2]}
function bg(e,rr){let a=[255,255,255,255],chain=[];for(;e;e=e.parentElement)chain.push(e);for(let n of chain.reverse()){let z=n.getBoundingClientRect();if(rr.length&&!rr.some(r=>(r.left+r.right)/2>=z.left&&(r.left+r.right)/2<=z.right&&(r.top+r.bottom)/2>=z.top&&(r.top+r.bottom)/2<=z.bottom))continue;let c=rgba(getComputedStyle(n).backgroundColor),f=c[3]/255;a=a.map((v,i)=>i<3?c[i]*f+v*(1-f):255)}return a}
const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let t;while(t=w.nextNode()){
if(!t.textContent.trim())continue;const e=t.parentElement,cs=getComputedStyle(e);if(['SCRIPT','STYLE'].includes(e.tagName)||cs.display==='none'||cs.visibility==='hidden'||parseFloat(cs.fontSize)===0||!e.getClientRects().length)continue;
let range=document.createRange();range.selectNodeContents(t);let rr=Array.from(range.getClientRects()).filter(r=>r.width&&r.height);
for(let r of rr){rects.push({x:r.x,y:r.y,right:r.right,bottom:r.bottom,text:t.textContent.trim().slice(0,45),el:e});if(r.left<box.left-1||r.right>box.right+1||r.top<box.top-1||r.bottom>box.bottom+1)issues.push({kind:'page-overflow',text:t.textContent.trim().slice(0,70)});}
let slot=e.closest('[data-el]');if(slot){let s=slot.getBoundingClientRect();if(s.width>1&&s.height>1){for(let r of rr)if(r.left<s.left-2||r.right>s.right+2||r.top<s.top-2||r.bottom>s.bottom+2)issues.push({kind:'slot-overflow',element:slot.dataset.el,text:t.textContent.trim().slice(0,70)})}}
let fg=rgba(cs.color),back=bg(e,rr),L=lum(fg),B=lum(back),ratio=(Math.max(L,B)+.05)/(Math.min(L,B)+.05),minimum=parseFloat(cs.fontSize)>=28?3:4.5;if(ratio+.05<minimum)issues.push({kind:'contrast',element:slot?.dataset.el,text:t.textContent.trim().slice(0,45),ratio:Math.round(ratio*100)/100,minimum});
for(let n=e;n&&n!==root;n=n.parentElement){let z=getComputedStyle(n),nr=n.getBoundingClientRect();if(z.overflow==='hidden'||z.overflow==='clip'){if(rr.some(r=>r.right>nr.right+1||r.bottom>nr.bottom+1||r.left<nr.left-1||r.top<nr.top-1)){issues.push({kind:'clipping',element:slot?.dataset.el,text:t.textContent.trim().slice(0,45)});break}}}
}
for(let i=0;i<rects.length;i++)for(let j=i+1;j<rects.length;j++){let a=rects[i],b=rects[j];if(a.el===b.el||a.el.contains(b.el)||b.el.contains(a.el))continue;if(Math.min(a.right,b.right)-Math.max(a.x,b.x)>2&&Math.min(a.bottom,b.bottom)-Math.max(a.y,b.y)>2)issues.push({kind:'text-overlap',a:a.text,b:b.text,element:a.el.closest('[data-el]')?.dataset.el})}
return {issues:issues.slice(0,100),font:document.fonts.check('20px "Pretendard Variable"')&&document.fonts.check('48px "Noto Sans KR"'),size:[box.width,box.height],textRanges:rects.length};}'''
results={'library':[],'pages':[],'cases':0,'font_failures':0}
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage']);pg=b.new_page(viewport={'width':1280,'height':720})
 for mode in ['light','dark']:
  pg.goto(f'http://127.0.0.1:8765/briefing-tab-review/library/{mode}.html');pg.evaluate('document.fonts.ready')
  html=pg.content();styles=pg.locator('head').inner_html();styles=re.sub(r'<style>body\{margin:0;padding:24px.*?</style>','',styles,flags=re.S)
  pg.set_content('<!doctype html><html lang="ko"><head><base href="http://127.0.0.1:8765/briefing-tab-review/library/">'+styles+'</head><body style="margin:0"></body></html>');pg.evaluate('document.fonts.ready');pg.evaluate('''async()=>{await Promise.all([document.fonts.load('400 20px \"Pretendard Variable\"'),document.fonts.load('700 48px \"Noto Sans KR\"')])}''')
  for folder in sorted((C/'elements').iterdir()):
   if not folder.is_dir():continue
   for f in sorted((folder/'fixtures').glob('*.html')):
    text=f.read_text();m=re.match(r'<!-- min: (.*?) -->',text);mins=[tuple(map(int,a))for a in re.findall(r'(\d+)x(\d+)',m.group(1))]if m else [(12,6)]
    cases={(c,r)for mc,mr in mins for c in range(mc,13)for r in range(mr,7)}
    text=re.sub(r'^<!--.*?-->\s*','',text,flags=re.S)
    entry={'mode':mode,'element':folder.name,'fixture':f.stem,'cases':len(cases),'failures':[]}
    for c,r in sorted(cases):
     pg.evaluate('''([text,mode,c,r])=>{document.body.innerHTML=`<section class="slide ${mode==='dark'?'dark':''}"><div class="page"><div class="body">${text}</div></div></section>`;let e=document.querySelector('.body').firstElementChild;e.style.gridColumn=`1 / span ${c}`;e.style.gridRow=`1 / span ${r}`;}''',[text,mode,c,r])
     out=pg.evaluate(AUDIT);results['cases']+=1
     if not out['font']:results['font_failures']+=1
     if out['issues']:entry['failures'].append({'size':f'{c}x{r}','issues':out['issues']})
    results['library'].append(entry)
   print(mode,folder.name,'checked',flush=True)
 for folder in ['replica','reassembled']:
  for n in range(20,31):
   pg.goto(f'http://127.0.0.1:8765/briefing-tab-review/{folder}/slide_{n}.html');pg.evaluate('document.fonts.ready');out=pg.evaluate(AUDIT)
   results['pages'].append({'kind':folder,'slide':n,**out})
 b.close()
(R/'browser-validation.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
summary={'cases':results['cases'],'font_failures':results['font_failures'],'library_fixtures_with_issues':sum(bool(x['failures'])for x in results['library']),'page_issues':[(x['kind'],x['slide'],len(x['issues']))for x in results['pages']if x['issues']]}
print(json.dumps(summary,ensure_ascii=False,indent=2))
