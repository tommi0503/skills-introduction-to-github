"""Read-only full-descendant replica inventory; output separate residual map parts.
No collection CSS, renderer, existing map part, or immutable source is modified.
"""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright
import json,threading,hashlib,sys,re
R=Path('/workspace/work/rebuild');OLD=Path('/workspace/work/delivery')
NAMES=['tide-tab','cutfield','filament','portico','toggle-grid','lamella','rulemark']
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
JS=r'''()=>{let out=[],sel=e=>{let a=[];for(;e&&e!==document.body;e=e.parentElement){let t=e.tagName.toLowerCase();if(e.id){a.unshift('#'+CSS.escape(e.id));break}let cs=typeof e.className==='string'?e.className.trim().split(/\s+/).filter(Boolean):[];if(cs.length)t+='.'+cs.map(CSS.escape).join('.');let sib=e.parentElement?[...e.parentElement.children].filter(x=>x.tagName===e.tagName):[];if(sib.length>1)t+=':nth-of-type('+(sib.indexOf(e)+1)+')';a.unshift(t)}return a.join(' > ')};
for(let e of document.body.querySelectorAll('*')){if(e.closest('defs,clipPath,mask,marker,style,script'))continue;let c=getComputedStyle(e),r=e.getBoundingClientRect();if(c.display==='none'||c.visibility==='hidden'||+c.opacity===0||r.width<.01||r.height<.01)continue;let selector=sel(e),bbox=[r.x,r.y,r.width,r.height].map(x=>Math.round(x*10000)/10000),border=['Top','Right','Bottom','Left'].map(d=>({side:d.toLowerCase(),width:parseFloat(c['border'+d+'Width']),style:c['border'+d+'Style'],color:c['border'+d+'Color']}));let base={selector,tag:e.tagName.toLowerCase(),classes:e.getAttribute('class'),bbox,text:e.textContent.trim().slice(0,120),background:c.background,color:c.color,border,transform:c.transform,html:e.outerHTML.slice(0,5000),ancestors:[...function*(n){for(let p=n.parentElement;p&&p!==document.body;p=p.parentElement)yield p}(e)].map(p=>({selector:sel(p),classes:p.getAttribute('class')}))};if(e instanceof SVGElement){if(e.tagName.toLowerCase()==='svg'&&!e.parentElement.closest('svg'))out.push({...base,kind:'svg',hasText:!!e.querySelector('text'),html:e.outerHTML});continue}
if(!e.textContent.trim()&&(c.backgroundColor!=='rgba(0, 0, 0, 0)'||c.backgroundImage!=='none'||border.some(b=>b.width>0&&b.style!=='none')))out.push({...base,kind:'empty-painted'});
if(e.textContent.trim()&&border.some(b=>b.width>0&&b.style!=='none'))out.push({...base,kind:'text-border'});
for(let pseudo of ['::before','::after']){let p=getComputedStyle(e,pseudo);if(p.content==='none'||p.content==='normal'||p.display==='none')continue;let pb=['Top','Right','Bottom','Left'].map(d=>({side:d.toLowerCase(),width:parseFloat(p['border'+d+'Width']),style:p['border'+d+'Style'],color:p['border'+d+'Color']}));if(p.backgroundColor==='rgba(0, 0, 0, 0)'&&p.backgroundImage==='none'&&!pb.some(b=>b.width>0&&b.style!=='none')&&['""',"''"].includes(p.content))continue;out.push({...base,kind:'pseudo',pseudo,owner_bbox:bbox,content:p.content,pseudoStyle:{position:p.position,left:p.left,top:p.top,right:p.right,bottom:p.bottom,width:p.width,height:p.height,background:p.background,color:p.color,transform:p.transform,content:p.content,border:pb}})}
}return out}'''
def capture():
 server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(OLD)));threading.Thread(target=server.serve_forever,daemon=True).start()
 with sync_playwright()as pw:
  browser=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-breakpad']);page=browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
  for name in NAMES:
   out={};hashes={}
   for path in sorted((OLD/name/'review/replica').glob('slide_*.html')):
    nn=path.stem[-2:];hashes[path.name]=hashlib.sha256(path.read_bytes()).hexdigest();page.goto(f'http://127.0.0.1:{server.server_port}/{name}/review/replica/{path.name}');page.evaluate('document.fonts.ready');out[nn]=page.evaluate(JS)
   (R/name/'build/source-residual-furniture-dom.json').write_text(json.dumps({'collection':name,'source_hashes':hashes,'pages':out},ensure_ascii=False,indent=2));print(name,len(out),'pages',sum(map(len,out.values())),'paint candidates',flush=True)
  browser.close()
 server.shutdown()
def contains(a,b,tol=1):
 return a[0]>=b[0]-tol and a[1]>=b[1]-tol and a[0]+a[2]<=b[0]+b[2]+tol and a[1]+a[3]<=b[1]+b[3]+tol
def equal(a,b,tol=.05):return all(abs(x-y)<=tol for x,y in zip(a,b))
def map_all():
 total=[]
 for name in NAMES:
  B=R/name/'build';capture_path=B/'source-residual-furniture-dom.json';cap=json.loads(capture_path.read_text());review=json.loads((R/name/'review/map.json').read_text());existing=list(review['instances']);parts={}
  for f in sorted(B.glob('map-*.json')):
   if f.name=='map-residual-furniture.json':continue
   q=json.loads(f.read_text());parts[f.name]=hashlib.sha256(f.read_bytes()).hexdigest();existing+=q.get('instances',[])
  vectors=json.loads((B/'source-vector-dom.json').read_text());out=[];audit=[]
  def add(page,n,bbox,design,role=None,svg=None,foreground=False,use='furniture',source_extra=None):
   # Compare actual paint rectangles. Broad background planes do not own a
   # different-colored line placed over them. No root is altered to fit a line.
   if any(a['page']==page and a['use']!='background' and equal(a['bbox'],bbox) for a in existing+out):return 'already-mapped exact apparatus'
   a={'id':page+'-residual-furniture-'+str(len(out)+1),'page':page,'bbox':bbox,'leaf':None,'use':use,'design':design,'source':{'file':'replica/slide_'+page+'.html','selector':n['selector'],'measurements':{'bbox':n['bbox'],'background':n['background'],'border':n['border'],'html':n['html']}}}
   if source_extra:a['source']['measurements'].update(source_extra)
   if use=='background':a.update(region=True,role=role)
   else:a.update(foundation_slot='deco')
   if role and use!='background':a.update(graphic='hairline',role=role)
   if svg:a.update(source_svg=svg,foreground_role='--ink')
   if foreground:a['foreground_device']=True
   out.append(a);return 'added '+a['id']
  for page,ns in cap['pages'].items():
   ms=[a for a in existing if a['page']==page];rootbg=next((a for a in ms if a['use']=='background'and not a.get('region')),None)
   for n in ns:
    b=n['bbox'];kind=n['kind'];sel=n['selector'];decision=None;owners=[]
    # Explicit source-only independent apparatus. Own connectors and all
    # decorations within a mapped component are never extracted here.
    component_owners=[a for a in ms if (a.get('leaf')or a['use']=='unexpressible')and contains(b,a['bbox'])]
    if component_owners:decision='owned component or unsupported container: '+','.join(sorted(set(a.get('id',a.get('leaf')or'gap')for a in component_owners)))
    elif name=='tide-tab'and page=='07'and kind=='empty-painted'and 'div.topline'in sel:
     decision=add(page,n,b,'일정 페이지 주 표제 좌우의 독립 가는 가이드 괘선. 일정판 또는 기간 막대의 연결선이 아니다.','--n-3')
    elif name=='cutfield'and page=='01'and kind=='empty-painted'and equal(b,[1168,65,36,2]):
     decision=add(page,n,b,'표지 오른쪽 위 페이지 라벨 아래의 독립 36×2 accent 괘선.','--a1')
    elif name=='cutfield'and page=='13'and kind=='pseudo'and 'div.arrow'in sel:
     if n['pseudo']=='::before':
      svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 38 38"><rect x="3" y="18" width="37" height="1.5" fill="#29caa3" transform="rotate(-45 21.5 18.75)"/><rect x="9" y="3" width="26" height="1" fill="#29caa3"/><rect x="34" y="3" width="1" height="26" fill="#29caa3"/></svg>'
      decision=add(page,n,b,'Join Us 표제 오른쪽의 독립 대각선 CTA 읽기 표식. 연결 멤버 없는 페이지 방향 장치이며 카드 연결선이 아니다.',svg=svg,source_extra={'pseudo_before':n['pseudoStyle'],'pseudo_after':next(x['pseudoStyle']for x in ns if x['selector']==sel and x.get('pseudo')=='::after'),'source_css':'.arrow:before left3 top18 width37 height1.5 rotate(-45deg) center; :after right2 top3 width26 height26 border-top/right1.5 source declaration; browser computed actual border1 at DPR1'})
     else:decision='included in same independent CTA arrow before/after composite'
    elif name=='portico'and kind=='empty-painted'and ((min(b[2:])<=1.01 and max(b[2:])>=100)or(page=='05'and n['border'][1]['width']>0)):
     if page=='05':bb=[round(b[0]+b[2]-n['border'][1]['width'],4),b[1],n['border'][1]['width'],b[3]]
     else:bb=b
     decision=add(page,n,bb,'정보 요소와 별개인 페이지 구획 괘선. 원본 DOM의 전체 길이를 유지하고 기본 deco 깊이0으로 본문/사진 아래에 놓여 원래 가림 순서를 보존한다.','--n-4',source_extra={'paint_bbox':bb,'source_occlusion':'For05, later photo placeholders cover the part below y438; no artificial truncation or new element CSS.'})
    elif name=='portico'and page=='08'and kind=='text-border'and n['border'][1]['width']>0:
     bb=[round(b[0]+b[2]-n['border'][1]['width'],4),b[1],n['border'][1]['width'],b[3]];decision=add(page,n,bb,'왼쪽 본문 구획과 오른쪽 수익 모델 도식 사이의 독립 세로 경계. 두 개 prose/headline의 내부 테두리로 옮기지 않는다.','--n-4',source_extra={'paint_bbox':bb})
    elif name=='portico'and page=='05'and kind=='svg'and equal([b[1],b[2],b[3]],[427,23,23]):
     decision=add(page,n,b,'설명 구획과 아래 기기 화면 사이의 독립 원형 하향 읽기 표식. 카드/사진을 잇는 연결선은 없으며 전체 3열 장면에서 반복한다.',svg=n['html'],foreground=True)
    elif name=='toggle-grid'and page=='02'and 'div.switch'in sel:
     if kind=='empty-painted':
      svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 111 43"><rect width="111" height="43" rx="21.5" fill="#141414"/><ellipse cx="89" cy="21.5" rx="18" ry="18.5" fill="#ff6d1e"/></svg>'
      decision=add(page,n,b,'표지 제목 아래의 텍스트 없는 switch 브랜드 장식. 실제111×43 검정 capsule과 오른쪽36×37 주황 타원만 유지한다.',svg=svg,source_extra={'source_css':'.switch width111 height43 radius999; :after right4 top3 width36 height37 radius50%','pseudo_after':next(x['pseudoStyle']for x in ns if x['selector']==sel and x.get('pseudo')=='::after')})
     else:decision='included in same independent switch composite'
    elif name=='rulemark'and page=='03'and kind=='empty-painted'and equal(b,[0,253,66,399]):
     decision=add(page,n,b,'사진 왼쪽에 남긴 검정 페이지 구획 면. 원본 frame의 일부로 늘리거나 추가하지 않는 독립 scene 면이다.','--ink',use='background')
    if decision is None:
     if kind=='pseudo'and name=='tide-tab'and sel=='main.slide'and n['pseudo']=='::after':
      bb=[0,712,1280,8];decision='already-mapped foundation split-rule'if any(equal(a['bbox'],bb)for a in ms if a['use']=='furniture')else'UNRESOLVED global split-rule'
     elif kind=='svg'and n.get('hasText'):
      # Existing vector capture verifies no painted geometry accompanies these
      # text-only full-page SVG viewports; their text is covered by other maps.
      vv=next((v for v in vectors.get(page,[])if v['html']==n['html']),None)
      decision='text-only SVG viewport; no geometric paint parts'if vv is not None and not vv['parts']else'UNRESOLVED text SVG geometry'
     elif name=='filament'and ((page=='04'and(equal(b,[45,370,280,280])or equal(b,[371,465,95,95])))or(page=='06'and kind=='svg'and equal(b,[289,107,420,530]))or(page=='07'and equal(b,[1229,487,45,45]))):
      decision='external owner leaf_text:04 complex graphic placeholder and X /06 complex graphic placeholder /07 plus; expressly excluded from residual to prevent duplicate map parts'
     elif name=='cutfield'and page=='03'and equal(b,[0,0,640,720]):decision='redundant source rectangle equals entire page base color (--a2); existing full-page background already paints this left half'
     elif name=='cutfield'and page=='06'and equal(b,[795,205,389,411]):decision='existing unexpressible containing panel06-gap-1; actual outer box differs from old mapped[801,237,381,380]. Not converted to furniture.'
     else:
      owners=[a for a in ms if a['use']!='background'and contains(b,a['bbox'])]
      if owners:decision='owned component or apparatus: '+','.join(sorted(set(a.get('id',a.get('leaf')or'foundation')for a in owners)))
      elif kind=='empty-painted'and any(a['use']=='background'and equal(b,a['bbox'])for a in ms):decision='already-mapped page plane'
      elif kind=='svg':
       vv=next((v for v in vectors.get(page,[])if v['html']==n['html']),None);parts2=vv['parts']if vv else[]
       if parts2 and all(any(a['use']!='background'and contains(z['bbox'],a['bbox'])for a in ms)for z in parts2):decision='SVG viewport exceeds tight root bbox, but all actual paint parts belong to mapped components/connectors'
       else:decision='UNRESOLVED SVG paint geometry'
      else:decision='UNRESOLVED painted candidate'
    audit.append({'page':page,'kind':kind,'selector':sel,'bbox':b,'pseudo':n.get('pseudo'),'decision':decision})
  result={'collection':name,'group':'residual-furniture','instances':out};(B/'map-residual-furniture.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
  report={'collection':name,'tool_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_pages':len(cap['pages']),'paint_candidates':len(audit),'added_instances':len(out),'source_capture_sha256':hashlib.sha256(capture_path.read_bytes()).hexdigest(),'existing_map_part_hashes':parts,'review_map_sha256':hashlib.sha256((R/name/'review/map.json').read_bytes()).hexdigest(),'immutable_source_unchanged':all(hashlib.sha256((OLD/name/'review/replica'/f).read_bytes()).hexdigest()==h for f,h in cap['source_hashes'].items()),'external_owner_items':[a for a in audit if a['decision'].startswith('external owner')],'known_gap_geometry_differences':[a for a in audit if a['decision'].startswith('existing unexpressible containing panel')],'unresolved':[a for a in audit if a['decision'].startswith('UNRESOLVED')],'decisions':audit};(B/'residual-furniture-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));total.append({k:report[k]for k in ['collection','source_pages','paint_candidates','added_instances','unresolved','immutable_source_unchanged']});print(name,'added',len(out),'unresolved',len(report['unresolved']),flush=True)
 (R/'build/residual-furniture-audit.json').write_text(json.dumps({'collections':total,'source_pages':sum(a['source_pages']for a in total),'paint_candidates':sum(a['paint_candidates']for a in total),'added_instances':sum(a['added_instances']for a in total),'external_owner_items':sum(len(json.loads((R/a['collection']/'build/residual-furniture-audit.json').read_text())['external_owner_items'])for a in total),'known_gap_geometry_differences':sum(len(json.loads((R/a['collection']/'build/residual-furniture-audit.json').read_text())['known_gap_geometry_differences'])for a in total)},ensure_ascii=False,indent=2))
if __name__=='__main__':
 if '--capture'in sys.argv:capture()
 if '--map'in sys.argv:map_all()
