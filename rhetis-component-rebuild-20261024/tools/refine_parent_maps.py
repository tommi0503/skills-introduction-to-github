from pathlib import Path
import json,sys,copy
sys.path.insert(0,str(Path(__file__).parent))
from size_review import browser,serve_url
from playwright.sync_api import sync_playwright
B=Path('/workspace/work/rebuild-20261024');O=Path('/workspace/work/deliverables')
TEXTBOX=r'''selector=>{let es=[...document.querySelectorAll(selector)],rs=[];for(let e of es){let w=document.createTreeWalker(e,NodeFilter.SHOW_TEXT);while(w.nextNode()){let n=w.currentNode;if(!n.textContent.trim())continue;let q=document.createRange();q.selectNodeContents(n);rs.push(...q.getClientRects())}}if(!rs.length)return null;let l=Math.min(...rs.map(r=>r.left)),t=Math.min(...rs.map(r=>r.top)),r=Math.max(...rs.map(r=>r.right)),b=Math.max(...rs.map(r=>r.bottom));return[l,t,r-l,b-t].map(x=>+x.toFixed(2))}'''
with sync_playwright() as pw:
 browser_=browser(pw)
 for name in ['afterglow','confluence']:
  p=B/name/'review/map.json';d=json.loads(p.read_text());out=[]
  for inst in d['instances']:
   if inst.get('parent_refined'):out.append(inst);continue
   pp=inst['page'];page=browser_.new_page(viewport={'width':1280,'height':720});page.goto(serve_url(O/name/'review/replica'/('slide_'+pp+'.html')));page.evaluate('document.fonts.ready')
   if name=='afterglow' and inst.get('leaf')in ['headline','prose']:
    b=page.evaluate(TEXTBOX,inst['replica_selector'])
    if b:inst['bbox']=b;inst['bbox_method']='union of rendered text ranges; excludes unrelated neighbouring illustrations'
   if name=='afterglow' and pp=='07' and inst.get('leaf')in ['tag','prose']:
    suffix='h3'if inst['leaf']=='tag'else'p'
    for k in range(4):
     x=copy.deepcopy(inst);x['replica_selector']='.process:nth-of-type('+str(k+1)+') '+suffix
     # CSS nth-of-type includes surrounding DIVs, so use an explicit locator index via evaluate.
     x['replica_selector']='.process.'+(['left.toprow','right.toprow','left.bottomrow','right.bottomrow'][k])+' '+suffix
     b=page.evaluate(TEXTBOX,x['replica_selector'])
     if b:x['bbox']=b
     if k and x['use']=='base':x['use']='same-as:07'
     x['parent_refined']=True;out.append(x)
   else:
    if name=='afterglow' and pp=='09' and inst.get('leaf')=='prose' and inst['use']=='variant:.quiet':inst['leaf']=None;inst['use']='furniture';inst.pop('fixture',None);inst['design']='13px 연락처와 문의 정보: closing page metadata'
    if name=='confluence' and inst.get('leaf')=='agenda':inst['bbox']=[94,272,1092,374]
    inst['parent_refined']=True;out.append(inst)
   page.close()
  d['instances']=out;p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
 browser_.close()
print('parent map text bounds and repeated local parts refined')
