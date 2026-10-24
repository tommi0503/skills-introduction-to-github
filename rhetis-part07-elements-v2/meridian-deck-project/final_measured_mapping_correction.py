from pathlib import Path
from copy import deepcopy
from lxml import html
import json,shutil
P=Path(__file__).parent;C=P/'meridian-deck';f=P/'map.json';M=json.loads(f.read_text());A=Path('/tmp/meridian-final-unsupported074');A.mkdir(exist_ok=True)
I={x['id']:x for x in M['instances']}
def bounds(parts):
 boxes=[x['inkBBox'] or x['bbox'] for x in parts];x=min(z['x'] for z in boxes);y=min(z['y'] for z in boxes);r=max(z['x']+z['w'] for z in boxes);b=max(z['y']+z['h'] for z in boxes);return {'x':x,'y':y,'w':r-x,'h':b-y}
def restrict(unit,parts):
 unit['sourceMeasurements']=deepcopy(parts);unit['parts']=[x['id'] for x in parts];unit['sourceNodes']=unit['parts'][:];unit['selectors']=['main.slide > :nth-child('+str(x['index'])+')' for x in parts];unit['bounds']=bounds(parts);unit['bbox']=[unit['bounds'][k] for k in ['x','y','w','h']]
def gap(unit,name,why):
 unit.update(name=name,leaf=None,status='unexpressible',use='unexpressible',why=why);unit.pop('fixture',None);unit.pop('baseRef',None);unit.pop('baseInstance',None);unit['variant']='base';unit['design']='원본 영역 '+','.join(str(x) for x in unit['bbox'])+'. '+why
# Registered table semantics remain truthful; the two different visual designs
# are never called same-as of the directly extracted capsule table.
for uid in ['p17-10','p21-08']:
 u=I[uid];gap(u,'Rectangular table decoration', 'The source uses rectangular column panels/cells, while the sole extracted table base on page19 uses individual capsule cells. table.grid has no named variant for the second visual design. All original values, prose and nested trends remain in an explicitly disclosed semantic table fallback using the page19 capsule base; its appearance is not claimed to reproduce the rectangular source.')
 u['semanticFallback']={'contract':'table.grid@1','baseRef':'p19-10','purpose':'Preserve all original cell values and relationships; capsule appearance is a documented fallback.'}
# Keep stress testing the semantic fallback, without asserting source shape.
for old,new in [('replica-17.html','nested-contracts.html'),('replica-21.html','budget-grid.html')]:
 src=C/'elements/table/fixtures'/old;data=src.read_bytes();(A/('table-'+old)).write_bytes(data);src.unlink();(C/'elements/table/fixtures'/new).write_bytes(data)
# Four keyword captions are individual capsules, not a chart key.
u=I['p26-09'];parts=deepcopy(u['sourceMeasurements']);newunits=[]
for n in range(4):
 t=deepcopy(u);t['id']=u['id'] if n==0 else 'p26-keyword-'+str(n+1);restrict(t,parts[n*2:n*2+2]);t.update(name='Independent keyword capsule '+str(n+1),leaf='pill',variant='quiet' if n<2 else 'base' if n==2 else 'on',fixture='elements/pill/fixtures/replica-26.html',use='variant:.quiet' if n<2 else 'same-as:28' if n==2 else 'variant:.on',baseRef='p28-nested-pill');t.pop('baseInstance',None);t['design']='原本 영역 '+','.join(str(x) for x in t['bbox'])+'. 한 개의 keyword를 나타내는 독립 수평 capsule이며 pill.'+t['variant']+'로 대응한다. 회색 중성 두 단계는 quiet의 동일 팔레트 자리를 공유하고, 진한 중성/강조 면은 base/on으로 표현한다. swatch+label인 legend와는 다른 원형이다.';newunits.append(t)
I['p26-09'].clear();I['p26-09'].update(newunits[0]);M['instances']+=newunits[1:]
def pill(text,state=''):
 return '<div class="pill '+state+'" data-el="meridian-deck-pill"><div class="parts"><b class="name">'+text+'</b></div></div>'
fx=C/'elements/legend/fixtures/replica-26.html';(A/'legend-replica-26.html').write_bytes(fx.read_bytes());fx.unlink();(C/'elements/pill/fixtures/replica-26.html').write_text('<!-- min: 12x1 -->\n<div class="group" style="grid-column:1 / span 12;grid-row:1 / span 6">'+''.join(pill('보전비',v) for v in ['quiet','quiet','','on'])+'</div>\n')
f=P/'reassembled/slide_26.html';doc=html.fromstring(f.read_text());legend=doc.xpath('//*[@data-el="meridian-deck-legend"]')[0];group=html.fragment_fromstring('<div class="group">'+''.join(pill(x.text_content(),v) for x,v in zip(legend,['quiet','quiet','','on']))+'</div>');legend.getparent().replace(legend,group);f.write_text('<!doctype html>\n'+html.tostring(doc,encoding='unicode'))
# Separate the two inter-row rules from the delta root's own two text states.
u=I['p20-10'];rules=[x for x in u['sourceMeasurements'] if x['index'] in [15,22]];restrict(u,[x for x in u['sourceMeasurements'] if x['index'] not in [15,22]]);u['design']='原本 영역 '+','.join(str(x) for x in u['bbox'])+'. 세 개의 독립 before→after 비교. 각 delta는 왼쪽18px 보통 본문·가운데107×75 투명→강조 gradient화살표·오른쪽18px 굵은 본문을 소유한다. 세로 capsule로 모양을 전환하지 않는다. 두 행 사이 공유 가로선은 별도 계약 공백으로 분리한다.'
for n,part in enumerate(rules,1):
 g=deepcopy(u);g['id']='p20-shared-rule-'+str(n);restrict(g,[part]);gap(g,'Shared comparison row rule','The source has a thin rule between three independent before/after rows. delta.change owns one pair and has no multi-row or rule variant; inspecting sibling order would violate the reusable element rule. A comparison-rows owner with delta children is required to own these two shared rules.');M['instances'].append(g)
# The vertical count transition has no named delta variant. Preserve both
# authentic state captions as capsules, and disclose only the connector gap.
u=I['p28-nested-delta'];parts=deepcopy(u['sourceMeasurements']);triangle=next(x for x in parts if x['index']==21);before=[x for x in parts if x['index'] in [19,20]];after=[x for x in parts if x['index'] in [22,45]];restrict(u,[triangle]);gap(u,'Vertical count-transition connector','The source has a downward gradient triangle between two count capsules. The extracted delta base20 is a horizontal plain-text comparison, and delta has no named vertical/capsule variant. The two actual count states remain as pill base/on; a named vertical delta or an explicit transition owner is needed for the connector.')
for name,ps,state in [('before',before,'base'),('after',after,'on')]:
 t=deepcopy(I['p28-nested-pill']);t['id']='p28-nested-count-'+name;restrict(t,ps);t.update(name='Count state '+name,leaf='pill',variant=state,fixture='elements/pill/fixtures/replica-28-count.html',use='same-as:28' if state=='base' else 'variant:.on',baseRef='p28-nested-pill');t['design']='原本 영역 '+','.join(str(x) for x in t['bbox'])+'. 원본의 실제 개소 수 한 개를 담은 독립 capsule. pill '+state+' 원형으로 보존하며 다른 상태와의 삼각 연결은 unexpressible 소유자에 분리했다.';M['instances'].append(t)
f=P/'reassembled/slide_28.html';doc=html.fromstring(f.read_text());delta=doc.xpath('//*[@data-el="meridian-deck-delta"]')[0];texts=[x.text_content() for x in delta];stack=html.fragment_fromstring('<div class="stack">'+pill(texts[0])+pill(texts[1],'on')+'</div>');delta.getparent().replace(delta,stack);f.write_text('<!doctype html>\n'+html.tostring(doc,encoding='unicode'))
fx=C/'elements/delta/fixtures/replica-28.html';(A/'delta-replica-28.html').write_bytes(fx.read_bytes());fx.unlink();(C/'elements/pill/fixtures/replica-28-count.html').write_text('<!-- min: 3x2 -->\n<div class="stack" style="grid-column:1 / span 12;grid-row:1 / span 6">'+pill('2개조')+pill('5개조','on')+'</div>\n')
# Keep duplicate per-page views exactly synchronised with the global units.
by={x['id']:x for x in M['instances']}
for pg in M['pages']:
 for key in ['instances','furniture']:pg[key]=[deepcopy(by[x['id']]) for x in pg.get(key,[])]
 existing={x['id'] for x in pg['instances']}
 for x in M['instances']:
  if x['page']==pg['page'] and x['kind']=='element' and x['id'] not in existing:pg['instances'].append(deepcopy(x))
(P/'map.json').write_text(json.dumps(M,ensure_ascii=False,indent=2)+'\n')
print('Instances',len(M['instances']),'Gaps',sum(x.get('use')=='unexpressible' for x in M['instances']))
