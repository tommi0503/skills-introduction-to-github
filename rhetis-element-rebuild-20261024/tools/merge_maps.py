from pathlib import Path
import json,collections,re,hashlib
from map_foundation import mapone,NAMES,inside
R=Path('/workspace/work/rebuild');profiles=json.loads((R/'profiles.json').read_text())
profiles['toggle-grid']['roles']['회색 표 괘선']='--n-5';profiles['lamella']['roles']['독립 흰 면과 원형 차트 빈 트랙']='--n-1'
(R/'profiles.json').write_text(json.dumps(profiles,ensure_ascii=False,indent=2))
for n in NAMES:
 mapone(n);D=R/n/'build';out=[]
 for f in sorted(D.glob('map-*.json')):
  part=json.loads(f.read_text())
  for a in part['instances']:
   a=dict(a);a['owner']=part.get('group',f.stem[4:]);a['page']=str(a['page']).zfill(2)
   if 'proposedMarkup'in a:a['proposed_markup']=a.pop('proposedMarkup')
   if n=='cutfield'and a.get('leaf')=='prose':
    raw=' '.join(t.get('inline','')for t in a.get('source',{}).get('measurements',[])).lower()
    if '#ffffff'in raw or '#fff'in raw or 'rgb(255, 255, 255)'in raw:a['foundation_context']='on'
   out.append(a)
 # Independent corner directional devices missed by top-level class capture.
 if n=='cutfield':
  for a in json.loads((D/'unowned-graphics.json').read_text()):
   if a['page']in['11','14'] and not any(x['page']==a['page'] and x.get('foundation_slot')=='deco' and x['bbox']==a['bbox'] for x in out):
    out.append({'page':a['page'],'bbox':a['bbox'],'leaf':None,'use':'furniture','foundation_slot':'deco','graphic':'corner-arrow','design':'페이지 가장자리의 독립 대각선 방향 장치; timeline 멤버 사이 연결선이 아님','owner':'foundation','source_svg_part':a['html']})
 out.sort(key=lambda a:(a['page'],{'background':0,'furniture':1}.get(a['use'],2),a['bbox'][1],a['bbox'][0]))
 for idx,a in enumerate(out):a.setdefault('id',a['page']+'-'+('foundation'if a['leaf']is None else a['leaf'])+'-'+str(idx+1))
 errors=[];bases=collections.Counter(a['leaf'] for a in out if a['use']=='base')
 for k,v in bases.items():
  if v>1:errors.append(f'{k}: {v} bases')
 for a in out:
  if a['use']=='unexpressible' and (not a.get('why') or not a.get('proposed_markup')):errors.append(a['id']+': gap requires why and markup')
  if len(a['bbox'])!=4 or a['bbox'][2]<0 or a['bbox'][3]<0:errors.append(a['id']+': badbbox')
 src=json.loads((D/'source-dom.json').read_text());unowned=[]
 for p,v in src.items():
  for t in v['texts']:
   if not any(a['page']==p and a['use']!='background' and inside(t['bbox'],a['bbox']) for a in out):unowned.append({'page':p,**t})
 if unowned:errors.append(f'{len(unowned)} unowned text fragments')
 m={'collection':n,'coordinate_system':'replica pixels,1280x720; bbox=[x,y,width,height]','roles':profiles[n]['roles'],'instances':out}
 (R/n/'review/map.json').write_text(json.dumps(m,ensure_ascii=False,indent=2))
 gaps=['# Unexpressible instances','']
 for a in out:
  if a['use']!='unexpressible':continue
  gaps+=['## '+a['page']+' · '+a['id'],'',f"bbox: `{a['bbox']}`",'',a['design'],'',a['why'],'','Proposed markup (not a supported extension):','','```html',a['proposed_markup'],'```','']
 (R/n/'review/GAPS.md').write_text('\n'.join(gaps))
 report={'instances':len(out),'source_pages':len(src),'base_count':dict(bases),'unexpressible':sum(a['use']=='unexpressible'for a in out),'unowned_texts':unowned,'errors':errors}
 (R/n/'review/validation/map-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(n,len(out),report['unexpressible'],'gaps',errors)
