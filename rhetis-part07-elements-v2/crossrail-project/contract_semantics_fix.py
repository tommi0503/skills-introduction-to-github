from pathlib import Path
from lxml import html,etree
import json,re
P=Path(__file__).parent;K=P/'crossrail';E=K/'elements';M=json.loads((P/'map.json').read_text());I={i['id']:i for i in M['instances']}
# Source07 is an arc/track, not a hub. Its original fixture cannot pretend to be the inferred radial hub.
i=I['p07-semicircle'];i.update(use='unexpressible',fixture=None,why='The source has four peer nodes following a semicircular track and a separate lower caption. No spoke connects a central core to the peers, so hub.radial cannot express this relation.',requiredMarkup='<div class="arc-track"><div class="node">…</div>…<div class="caption">…</div></div> (a contracted semicircular peer-track element)')
M['baseChoices'].pop('hub',None)
f=E/'hub/fixtures/replica-07.html'
if f.exists():f.unlink()
f=P/'reassembled/slide_07.html';d=html.fromstring(f.read_text())
for e in d.xpath('//*[@data-el="crossrail-hub"]'):e.getparent().remove(e)
f.write_text('<!doctype html>'+html.tostring(d,encoding='unicode')+'\n')
f=P/'original-assembly-identities.json';ids=json.loads(f.read_text());ids['7']=[x for x in ids['7'] if x!='p07-semicircle'];f.write_text(json.dumps(ids,ensure_ascii=False,indent=2)+'\n')
# Bare metric: retain numbers, alignment and typography, remove only the uncontracted value frame.
f=E/'metric/element.css';s=f.read_text().replace('border:2px solid var(--n-3);border-radius:999px;','border:0;');f.write_text(s)
(E/'metric/description.md').write_text('Bare figures, names and supporting notes share a clear numeric hierarchy. There is no value surface or enclosing outline. Thin separators may distinguish members of a metric group.\n')
r=next(r for r in I['p22-maximum-figure']['sourceMeasurements'] if r['id']=='source-14')
if 'p22-maximum-outline' not in I:M['instances'].append({'id':'p22-maximum-outline','page':22,'leaf':'metric','use':'unexpressible','bbox':r['bbox'],'sourceMeasurements':[],'why':'The number/name/note remain a bare metric. The source puts a capsule outline around the number, but metric.bare explicitly has no surface; this ornament is not hidden in metric CSS.','requiredMarkup':'<div class="numeric-badge"><span class="fig">…</span></div> (a separate contracted numeric badge)'} )
# The arrow relation is valid for versus; its original header-band placement still requires a composition contract.
arrow=I['p19-header-direction-arrow'];dest=I['p19-training-impact']
for r in arrow['sourceMeasurements']:r['owner']=dest['id'];dest['sourceMeasurements'].append(r)
arrow.update(leaf=None,bbox=[95,260,1090,65],sourceMeasurements=[],why='The directional comparison mark is supported by versus and drawn inside its root. The source puts it between two independent header bands above the fixed body slot; that position cannot be represented without a comparison-panel composition. The page grid is not shifted.',requiredMarkup='<div class="comparison-panel"><div class="headers"><div class="from">…</div><div class="mark"></div><div class="to">…</div></div><div class="faces">…</div></div> (a contracted header-and-faces comparison composition)')
dest['bbox']=[95,269,1090,385]
f=E/'versus/element.css';s=f.read_text();start=s.index('.versus[data-el="crossrail-versus"] .vs{');end=s.index('@container',start)
s=s[:start]+'.versus[data-el="crossrail-versus"] .vs{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:min(5cqw,15cqh);height:calc(min(5cqw,15cqh)*47/54);display:block;margin:0;background:transparent;border:0;font-size:var(--type-18);font-weight:var(--label-weight);z-index:2}.versus[data-el="crossrail-versus"] .vs::before{content:"";position:absolute;inset:0;background:var(--a2-7);clip-path:polygon(0 20%,65% 20%,65% 0,100% 50%,65% 100%,65% 80%,0 80%)}'+s[end:];f.write_text(s)
for f in (E/'versus/fixtures').glob('*.html'):
 st=f.read_text();minimum=re.match(r'<!--.*?-->',st,re.S)[0];d=html.fromstring(st)
 for mark in d.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," vs ")]'):mark.text='';[mark.remove(x) for x in list(mark)]
 f.write_text(minimum+'\n'+html.tostring(d,encoding='unicode')+'\n')
# Every visible source instance receives an actual visual design description, not an id/semantic label.
patterns={'agenda':'이름과 번호를 가로 분리하고 항목을 세로로 나열하는 목록','headline':'면 없이 드러낸 굵은 제목 글자와 명시적 줄바꿈','prose':'독립 문단과 빈 줄의 위계가 있는 보조 본문','card':'직각 정보 면 또는 얇은 분할선 안에서 분리된 이름·수치·설명','pill':'가운데 정렬한 짧은 이름을 담는 작은 capsule','pyramid':'수평으로 분할되지만 외곽 사선이 이어지는 삼각 계층','list':'점 또는 번호와 텍스트가 일정한 시작선에 맞는 목록','funnel':'아래로 좁아지는 연속 삼각 외곽과 세 단계 caption','steps':'연결 chevron 또는 아이콘 열과 얇은 capsule 행','image-frame':'원형 또는 직사각 사진 자리의 단색 placeholder','tag':'짧은 한 글자 이름을 가운데 놓은 작은 badge','table':'키와 값의 시작선을 맞춘 행·열, 얇은 가로 구분선','versus':'좌우 비교면과 독립 제목·설명·목록 및 방향 mark','chart-bar':'동일 축 기준에서 값에 비례하는 막대와 수치·분기 label','chart-line':'일곱 점의 실제 수치를 연결한 선과 점별 값·요일','metric':'면과 외곽선 없는 독립 수치·이름·note','legend':'색 자리별 이름과 비율이 짝을 이루는 범례','roadmap':'분기별 시간축에 from/to 구간을 놓은 네 행과 다섯 막대','timeline':'시간순 stop을 연결하는 가는 선, 분기와 이름·설명','positioning':'교차하는 두 축 안의 원형 위치 mark와 이름'}
for i in M['instances']:
 x,y,w,h=i['bbox'];rr=i.get('sourceMeasurements',[]);texts=[r for r in rr if r.get('text')];sizes=sorted({r.get('typography',{}).get('size') for r in texts if r.get('typography',{}).get('size')});weights=sorted({r.get('typography',{}).get('weight') for r in texts if r.get('typography',{}).get('weight')});lines=sum(bool(re.search(r'height:1px|width:1px',r.get('style',''))) for r in rr);rounds=sum('border-radius' in r.get('style','') for r in rr)
 if i['use']=='background':form='슬라이드 전체를 덮는 단색 바탕 면'
 elif i['use']=='furniture':
  r=rr[0] if rr else{};st=r.get('style','')
  form='얇은 페이지 rail·구분선' if re.search(r'height:1px|width:1px',st) else '가운데 또는 좌측 시작선을 갖는 페이지 제목·번호·영문 kicker' if texts else '페이지 가장자리의 직각 면과 교차선·hatch 장식'
 elif i['use']=='unexpressible':form=i.get('why','독립 구성 도형의 계약 미표현 영역')
 else:form=patterns.get(i.get('leaf'),'원본 측정에 따라 분리된 독립 도해')
 detail=f'{w:g}×{h:g}px, 좌표({x:g},{y:g})의 {form}.'
 if texts:detail+=' 보이는 텍스트 '+str(len(texts))+'개; 글자 '+', '.join(sizes)+' / 굵기 '+', '.join(weights)+'. 첫 문구는 “'+texts[0]['text'].replace('\n',' ')[:48]+'”.'
 if lines:detail+=' '+str(lines)+'개의1px 경계/연결선이 포함된다.'
 if rounds:detail+=' 원 또는 capsule 모서리 '+str(rounds)+'개를 포함한다.'
 i['design']=detail
(P/'map.json').write_text(json.dumps(M,ensure_ascii=False,indent=2)+'\n')
gaps=[i for i in M['instances'] if i['use']=='unexpressible'];out=['# Crossrail 계약상 미표현 영역','', '원문과 공개 수치는 지원되는 본문/차트에 보존한다. 아래는 실제 미지원 도형/구성만을 나타내며, 새 fixture 문장으로 원문을 대신하지 않는다.','']
for i in gaps:out+=['## '+i['id'],f'원본{i["page"]:02} / bbox `{i["bbox"]}`',i['design'],i.get('why',''), '필요한 계약 마크업: `'+i.get('requiredMarkup','새로 명시한 의미 부품이 필요하다.')+'`.','']
(P/'GAPS.md').write_text('\n\n'.join(out)+'\n')
print('map',len(M['instances']),'gaps',len(gaps),'design',sum(bool(i.get('design')) for i in M['instances']))
