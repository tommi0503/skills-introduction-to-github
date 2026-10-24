"""New source-derived library. Never reads the previous collection CSS."""
from pathlib import Path
import json,re,html,shutil
P=Path(__file__).resolve().parent;K=P/'onboard-docket';REF=Path('/workspace/work/reference');kid=K.name
measure=json.loads((P/'source-measurements.json').read_text())
roles={'검은 강조 띠':'--ink','짙은 중성 라벨':'--n-9','바깥 회색 면':'--n-3','흰 종이':'--page','강조 글자':'--a1-7','주 강조 채움':'--a1','주 강조 위 글자':'--a1-on','보조 진한 채움':'--a2-7','보조 채움 위 글자':'--page','진한 본문':'--n-8','중성 채움 위 글자':'--page','회색 카드 면':'--n-1','부드러운 강조 면':'--a1-1-soft','기본 글자':'--ink','보조 글자':'--n-7','얇은 구분선':'--n-4'}
instances=[];owned={}
def inst(page,ids,leaf,use,design,fixture=None,why=None,bbox=None):
 rows=[measure[page][i-1] for i in ids];bb=bbox or ([min(x['bbox'][0] for x in rows),min(x['bbox'][1] for x in rows),max(x['bbox'][0]+x['bbox'][2] for x in rows)-min(x['bbox'][0] for x in rows),max(x['bbox'][1]+x['bbox'][3] for x in rows)-min(x['bbox'][1] for x in rows)] if rows else [0,0,1280,720]);bb=[round(x,2) for x in bb];bb[2]=min(bb[2],1280-bb[0]);bb[3]=min(bb[3],(682 if page=='13' and use!='background' else 720)-bb[1]);d={'id':f'{page}-{len(instances)+1:03d}','page':page,'bbox':bb,'leaf':leaf,'use':use,'design':design,'selectors':[x['selector'] for x in rows],'sourceNodes':ids,'sourceMeasurements':rows}
 if fixture:d['fixture']=f'elements/{leaf}/fixtures/{fixture}.html'
 if why:d['why']=why
 instances.append(d);owned.setdefault(page,set()).update(ids)
for page,rows in measure.items():
 inst(page,[],None,'background','1280×720 단색 회색 페이지 전체 면')
 for row in rows:
  if row['classes'] in ['paper','rail','head'] or page in ['01','03']:
   if page not in ['01','03']:inst(page,[row['index']],None,'furniture','라운드 종이·상단 브랜드 레일·장 번호와 제목의 세로/가로 괘선')
 if page in ['01','03']:inst(page,list(range(1,len(rows)+1)),None,'furniture','표지 lockup·오른쪽 아이콘 rail 또는 가운데 chapter lockup, 메타 구분선')
# Source-visible units; connector owners stay whole.
inst('02',[3,4],None,'furniture','80px 가운데 INDEX 제목과 가로 구분선')
inst('02',list(range(5,len(measure['02'])+1)),'agenda','base','451×64px 알약 항목, 왼쪽56px 원형 번호, 4행×2열 세로 우선 순서','replica-02')
inst('04',[5,6,7,8,9],'quote','base','35px 인용문·검은 inline강조·양쪽 따옴표,17px 1.7행간 서신,19px 직함과36px 손글씨 서명','replica-04')
sub=json.loads((P/'source-subpart-measurements.json').read_text())['04'];highlight=next(x for x in sub if x['background']=='rgb(0, 0, 0)');inst('04',[],'tag','base','검은 면·흰 글자의 inline 강조 띠, 좌우12px padding','replica-04-highlight',bbox=highlight['bbox']);instances[-1]['selectors']=[highlight['selector']];instances[-1]['sourceSubparts']=[highlight]
inst('04',[4],'image-frame','same-as:18','400×608px 세로 인물 회색 자리; 계약 seat.portrait 자식','replica-04-portrait')
inst('05',[4],'image-frame','same-as:18','420×395px 회색 사진 자리')
inst('05',[5],'headline','same-as:12','24px 강조 제목 한 줄','replica-05')
inst('05',[6],'prose','base','19px 본문,1.6행간, 긴 문장 여러 줄','replica-05')
inst('05',[7],'prose','variant:.lead','16px 하단 강조 문단, 주 강조색과 같은 행간','replica-05-lead')
inst('06',[4],'pill','base','101×30px 진한 중성 알약,16px 가운데 단어','replica-06')
inst('06',[5],'prose','variant:.quiet','14px 보조 설명 한 줄','replica-06')
inst('06',[6,7,8,9,10,11],None,'unexpressible','3색 ring과 중앙3갈래 분기 및 외부 leader',why='donut은 한 share이며 cycle은3–6개 node와 core를 가진다. 세 조각 ring+외부 leader는 어느 구조와도 일치하지 않는다.')
inst('06',[12],'pill','variant:.quiet','101×30px 보조 강조순위의 조용한 진한 알약','replica-06-quiet')
inst('06',[13],'pill','variant:.on','101×30px 주 강조 알약','replica-06-on')
inst('06',[14,15],'prose','same-as:05','좌우3행 설명')
inst('06',[16],'callout','base','1083×48px 회색 긴 알약 결론,21px 가운데 문장','replica-06')
inst('07',list(range(4,19)),'list','base','977px 폭,54px 알약5행,75px pitch. 왼쪽302px 교대 채움 번호+이름, 오른쪽 설명','replica-07')
inst('08',[4,5,6,7,8,9,10,11,12],None,'unexpressible','아이콘과 이름을 담은 삼각 배치의3원·흰색 분리 틈',why='venn.set 구조는 name만 허용하며 원마다 icon을 담는 mark 부품이 없다. 아이콘을 빼거나 가짜 class를 추가하지 않는다.')
for start in [13,17,21]:inst('08',list(range(start,start+4)),'card','same-as:18','세로 괘선이 있는 회색 제목/설명 카드')
inst('09',list(range(4,len(measure['09'])+1)),None,'unexpressible','CEO·COO/CFO와5개 부서/3팀의 조직 트리',why='hierarchy의 branch 수는2–4이며 이 원본은 두 경영층과5개 부서로 이루어진다. 다른 중간 root를 억지로 더하지 않는다.')
inst('10',list(range(4,len(measure['10'])+1)),'steps','variant:.col','122px 회색 행3개, 왼쪽234px 단계 블록과 아래20×10px 연결 삼각형, 오른쪽 제목/본문','replica-10')
inst('11',[4],'headline','variant:.center','18px 주 강조 가운데 소제목','replica-11')
inst('11',[5],None,'unexpressible','1119×54px 세 카드 묶음을 제목 짓는 강조 띠',why='페이지 결론 문장이 아니라 여러 카드를 담는 패널 머리글이다. callout을 panel header인 척 사용하지 않는다.')
for start in [6,11,16]:inst('11',[start],'card','variant:.on','364×142px 부드러운 강조 면 위 가운데 설명','replica-11-on')
for start in [7,12,17]:inst('11',list(range(start,start+4)),'card','same-as:18','364×142px 회색 면,왼쪽 이름/설명,오른쪽 아래 Lucide mark')
inst('12',[4,5],'headline','base','155×35px 진한 알약 kick 아래30px 2행 heading','replica-12')
inst('12',[6,7],'headline','same-as:12','동일한 kick과2행 heading')
inst('12',[8,9],'prose','same-as:05','본문 두 영역')
inst('12',[10],'image-frame','same-as:18','196×145px 회색 사진 자리')
inst('13',list(range(4,len(measure['13'])+1)),None,'unexpressible','하단으로 잘리는 반원 ring 위4개 아이콘 원과 외부 제목·번호·설명',why='hub는 core에서 뻗는 spokes이며 이 구조는 반원 track의4개 point와 바깥 주석이다. 어느 contract도 이러한 track/annotation 구조를 제공하지 않는다.')
inst('14',list(range(4,11))+list(range(14,20))+list(range(23,29))+list(range(32,38)),None,'unexpressible','211px 원4개의 중첩, 둘레 캡슐, 각 원 아래 점선 leader/이름',why='venn은2–3집합의 포함/교집합이며 이 그림은4개 키워드 원의 나열이다. steps에는 원 안 kick/name과 원 밖 label을 함께 담는 부품이 없다.')
for start in [11,20,29,38]:inst('14',list(range(start,min(start+3,len(measure['14'])+1))),'card','variant:.quiet','279×90px 회색 작은 설명 카드','replica-14')
inst('15',list(range(4,len(measure['15'])+1)),'steps','base','196px 연한 원4개, 원 안58px 선 아이콘, 원 사이16×50px 삼각 화살표,22px 단계명과16px 설명','replica-15')
for start in [4,15,26]:
 inst('16',[start],None,'unexpressible','266×53px 상단만 둥근 탭',why='다른 요소를 담는 panel의 header/tab은 list나card 부품이 아니다.')
 inst('16',[start+1],None,'unexpressible','306×324px 둥근 목록 패널의 면·흰 테두리·그림자',why='list는 목록이며 panel surface를 별도 감싸는 계약이 없다. generic card로 list를 담아 panel인 척하지 않는다.')
 inst('16',list(range(start+2,min(start+11,len(measure['16'])+1))),'list','variant:.divided','61px 행간, 항목 사이250px 회색 괘선, 왼쪽 점','replica-16')
for start in [4,17,30]:
 inst('17',[start],None,'unexpressible','290×137px 사업명 강조 헤더 면',why='옆의 여러 metric을 제목 짓는 패널 면이며 standalone one-line pill이나 sentence callout과 의미가 다르다.')
 inst('17',[start+1],None,'unexpressible','807×137px 여러 지표를 담는 회색 패널',why='metric은 bare figure 계약이다. 패널 면을 metric CSS에 숨겨 추가하지 않는다.')
 inst('17',list(range(start+2,min(start+13,len(measure['17'])+1))),'metric','base' if start==4 else 'same-as:17','19px 왼쪽 이름·43px/700 숫자와30px 단위의 오른쪽 정렬·12px 왼쪽 note,34px 멤버 간격과90px 세로 괘선','replica-17' if start==4 else None)
inst('18',[4],'image-frame','base','493×330px 회색 사진 자리와 얇은 경계','replica-18')
inst('18',[5,6,7,8],'card','base','576×101px 둥근 회색 카드. 155px 제목 칸 뒤64px 세로 괘선, 오른쪽16px 설명','replica-18')
for start in [9,13]:inst('18',list(range(start,start+4)),'card','same-as:18','576×101px 동일한 제목·설명 회색 카드')
inst('19',[4],None,'unexpressible','108×397px 세로 이미지 묶음 헤더',why='표나 chart의 axis가 아니며 사진 세 개를 제목 짓는 세로 panel header 계약이 없다.')
for start in [5,8,11]:
 inst('19',[start],'image-frame','same-as:18','311×267px 사진 자리')
 inst('19',[start+1,start+2],'card','variant:.quiet','311×117px 회색 설명만 있는 카드','replica-19')
for page,rows in measure.items():
 missing=set(range(1,len(rows)+1))-owned.get(page,set())
 if missing:inst(page,sorted(missing),None,'unexpressible','기존 매핑에 귀속되지 않은 독립 가시 부품',why='해당 장식/문구를 정확히 담는 계약 부품이 없다. sourceNodes와 sourceMeasurements에 전체 수치를 보존한다.')
# Final source extraction corrections; preserve one owner per original node.
corrections=P/'support-map-corrections-073.json'
if corrections.exists():
 import copy
 edits={x['id']:x for x in json.loads(corrections.read_text())};out=[]
 for i in instances:
  if i['id'] not in edits:out.append(i);continue
  for fix in edits[i['id']]['replacements']:
   q=copy.deepcopy(i);ids=fix['sourceNodeIds'];q.update({k:v for k,v in fix.items() if k!='sourceNodeIds'});q['sourceNodes']=ids;q['sourceMeasurements']=[m for m in i.get('sourceMeasurements',[]) if m['index'] in ids];q['selectors']=[m['selector'] for m in q['sourceMeasurements']];q['extractionCorrection']=edits[i['id']]['reason'];out.append(q)
 instances=out
for i in instances:
 if i['id']=='04-076':i.update(leaf=None,use='unexpressible',design='본문 그리드 위로125px 뻗는400×608 인물 사진',why='foundation.body는y237..657이며 이 사진은y112..720이다. 계약의frame을본문정수그리드에배치해서는원래경계와크기를보존할수없다.')
 if i['id']=='08-092':i.update(use='variant:.tone-1',fixture='replica-08-tone-1.html',design='같은576×101카드, 주강조톤 제목과 중성 면')
 if i['id'].startswith('12-105-'):i.update(use='variant:.quiet' if i['id'].endswith('-1') else 'same-as:12',fixture='replica-12.html')
(P/'map.json').write_text(json.dumps({'collection':kid,'roles':roles,'coordinateSystem':'replica pixels, x/y/w/h at1280×720','sourceSubpartMeasurements':json.loads((P/'source-subpart-measurements.json').read_text()),'instances':instances,'coverage':{p:{'sourceNodeCount':len(rows),'mappedSourceNodeCount':len(owned[p])} for p,rows in measure.items()}},ensure_ascii=False,indent=2))
def proposed(i):
 p=i['page']
 if p=='04':return '<div class="page"><div class="portrait-bleed"><div class="seat portrait" data-ph="1"></div></div><header class="head">…</header><div class="body">…</div></div>'
 if p=='06':return '<div class="split-ring"><div class="ring">'+''.join('<div class="segment" style="--v:33.333"><span class="name">업무 기준</span></div>' for _ in range(3))+'</div><div class="core"><span class="icon" data-icon="git-fork"></span></div><div class="annotations"><span class="label">접수 분류</span><span class="label">승인 이력</span><span class="label">후속 점검</span></div></div>'
 if p=='08':return '<div class="icon-sets">'+''.join('<section class="set"><span class="icon" data-icon="'+icon+'"></span><p class="name">운영 기준</p></section>' for icon in ['globe','file-check','lightbulb'])+'</div>'
 if p=='09':return '<div class="executive-org"><div class="root">총괄 책임자</div><div class="executives"><div>고객 운영</div><div>기술 운영</div></div><div class="departments">'+''.join('<section class="department"><h3>담당 조직</h3><ul><li>접수 분류</li><li>승인 검토</li><li>품질 점검</li></ul></section>' for _ in range(5))+'</div></div>'
 if p=='13':return '<div class="semicircle-track"><div class="track"></div><div class="core"><p class="name">운영 원칙</p></div>'+''.join('<section class="point" style="--at:'+str(n)+'"><span class="icon" data-icon="shield-check"></span><div class="annotation"><p class="name">검토 항목</p><p class="note">담당 부서와 승인 근거를 확인합니다.</p></div></section>' for n in [0,33,66,100])+'</div>'
 if p=='14':return '<div class="topic-chain"><div class="outline"></div>'+''.join('<section class="topic"><p class="kick">SERVICE VALUE</p><p class="name">안정적인 응답</p><div class="leader"></div><p class="label">검토 범주</p></section>' for _ in range(4))+'</div>'
 if p in ['11','16','17','19']:return '<section class="panel"><header class="tab"><h2>검토 범주</h2></header><div class="content">'+('<div class="group"><div class="stat" data-el="onboard-docket-metric"><div class="parts"><p class="name">접수 건수</p><p class="fig">287</p></div></div></div>' if p=='17' else '<div class="list divided" data-el="onboard-docket-list"><div class="item"><p class="name">담당자 협의</p><p class="note">승인 근거를 기록합니다.</p></div><div class="item"><p class="name">담당 조직 확인</p><p class="note">이관 근거를 대조합니다.</p></div></div>')+'</div></section>'
 return '<div class="annotated-content"><div class="visual"></div><div class="annotation"><p class="name">검토 기준</p><p class="note">해당 도형의 역할과 소유 관계를 담는 별도 계약이 필요합니다.</p></div></div>'
gaps=[i for i in instances if i['use']=='unexpressible'];(P/'GAPS.md').write_text('# Unexpressible\n\n'+'\n\n'.join(f"## {i['id']} · page {i['page']}\n\n{i['design']}\n\n{i['why']}\n\nProposed markup (not admitted by the current contract):\n```html\n{proposed(i)}\n```" for i in gaps))
tokens={'--page':'#fdfdfd','--ink':'#111111','--font-display':"'Noto Sans KR'",'--font-body':"'Noto Sans KR'",'--weight-display':'600','--weight-body':'400','--tracking-display':'-.035em','--radius':'12px','--radius-sm':'8px','--stroke':'1px','--text-min':'12px','--margin-x':'97px','--margin-y':'38px','--gap':'20px','--gap-sm':'14px','--gap-lg':'32px','--pad':'24px','--furn-edge':'46px','--top-h':'49px','--foot-h':'25px','--furn-gap':'5px','--rail-w':'82px','--rail-gap':'18px'}
for prefix,weight,line,track in [('title',600,1.3,'-.054em'),('lead',500,1.6,'-.7px'),('figure',600,1.3,'-.7px'),('name',600,1.4,'-.7px'),('body',400,1.6,'-.7px'),('label',600,1.3,'0')]:tokens.update({f'--{prefix}-weight':str(weight),f'--{prefix}-line':str(line),f'--{prefix}-track':track})
tokens['--label-track-latin']='.5px'
extensions={'--onboard-docket-font-code':'font','--onboard-docket-font-signature':'font','--onboard-docket-value-weight':'weight','--onboard-docket-emphasis-weight':'weight','--onboard-docket-card-radius':'length','--onboard-docket-caption-line':'number','--onboard-docket-detail-line':'number','--onboard-docket-paper-radius':'length','--onboard-docket-metric-gap':'length','--onboard-docket-head-line':'number','--onboard-docket-cover-line':'number','--onboard-docket-statement-line':'number','--onboard-docket-quote-line':'number','--onboard-docket-letter-line':'number'}
tokens.update({'--onboard-docket-font-code':"'Nanum Gothic Coding'",'--onboard-docket-font-signature':"'Nanum Pen'",'--onboard-docket-value-weight':'700','--onboard-docket-emphasis-weight':'650','--onboard-docket-card-radius':'10px','--onboard-docket-caption-line':'1.5','--onboard-docket-detail-line':'1.65','--onboard-docket-paper-radius':'14px','--onboard-docket-metric-gap':'34px','--onboard-docket-head-line':'1.2','--onboard-docket-cover-line':'1','--onboard-docket-statement-line':'1.45','--onboard-docket-quote-line':'1.55','--onboard-docket-letter-line':'1.7'})
extensions.update({'--onboard-docket-cover-weight':'weight','--onboard-docket-cover-display-line':'number','--onboard-docket-cover-title-track':'tracking','--onboard-docket-cover-accent-track':'tracking'})
tokens.update({'--onboard-docket-cover-weight':'750','--onboard-docket-cover-display-line':'.94','--onboard-docket-cover-title-track':'-2px','--onboard-docket-cover-accent-track':'-1.7px'})
def put(rel,text):f=K/rel;f.parent.mkdir(parents=True,exist_ok=True);f.write_text(text)
put('kit/kit.json',json.dumps({'schema':'rhetis.kit/2','id':kid,'label':'Onboard Docket · source elements','tokens':'css/tokens.css','description':'description.md','extensions':extensions},indent=2))
put('kit/css/tokens.css','.slide{'+''.join(f'{k}:{v};' for k,v in tokens.items())+'}\n.slide.dark{--page:#151a23;--ink:#f2f4f7;}\n')
put('kit/description.md','A rounded paper docket beneath a slender binder rail. Split capsules pair an assertive numbered label with a quiet explanation; fine rules, spacious text and pale circular icon fields keep the educational material orderly. All chromatic decisions are palette roles.\n')
put('foundation/foundation.json',json.dumps({'schema':'rhetis.design-library-foundation-source/1','kit':kid,'registrations':{},'tokenDefaults':{}},indent=2))
put('foundation/description.md','A1188×590 paper at46,92 sits below the49px binder rail. The header pairs a58px chapter figure with a48px title, and the body is a twelve-by-six grid. Cover lockups and an optional vertical rail use the same paper and typography.\n')
put('foundation/foundation.css','''/* Replica02–19: rounded paper,49px rail, chapter/header rule. Replica01/03: cover furniture. */
.slide{container-type:size;box-sizing:border-box;width:1280px;height:720px;position:relative;overflow:hidden;background:var(--n-3);color:var(--ink);font-family:var(--font-body);font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track)}
.slide *{box-sizing:border-box}.slide .page{position:absolute;left:var(--furn-edge);right:var(--furn-edge);top:92px;bottom:38px;border-radius:var(--onboard-docket-paper-radius);background:var(--page);box-shadow:24px 24px 35px color-mix(in srgb,var(--n-9) 16%,transparent)}
.slide>.top{position:absolute;left:var(--furn-edge);right:var(--furn-edge);top:var(--margin-y);height:var(--top-h);background:var(--a1);color:var(--a1-on);border-radius:var(--radius);display:flex;align-items:center;justify-content:space-between;padding:0 var(--pad);font-size:var(--type-18);font-weight:var(--label-weight)}
.slide>.top .label{display:flex;align-items:center;gap:var(--gap-sm);font-size:var(--type-14)}.slide>.top .label::before{content:"";width:22px;height:22px;border-radius:4px;background:var(--n-1)}
.slide .head{position:absolute;left:51px;right:51px;top:41px;height:84px;display:flex;align-items:flex-start;border-bottom:var(--stroke) solid var(--n-4);gap:0}
.slide .head>.no{width:124px;flex:none;height:83px;border-right:var(--stroke) solid var(--n-4);font-size:clamp(var(--type-56),calc(4.53125cqw),var(--type-60));line-height:var(--onboard-docket-head-line);text-align:center;color:var(--a1-7);font-weight:var(--figure-weight)}
.slide .head>.title{margin:3px 0 0 35px;font-size:var(--type-48);font-weight:var(--title-weight);line-height:var(--title-line);letter-spacing:var(--title-track)}
.slide .head>.lead{align-self:center;margin:8px 0 0 var(--pad);font-size:var(--type-16);font-weight:var(--body-weight);letter-spacing:var(--label-track-latin);color:var(--a1-7);white-space:nowrap}
.slide .head.center{justify-content:center;top:41px;height:108px}.slide .head.center>.title{font-size:var(--type-80);font-weight:var(--figure-weight);line-height:var(--figure-line);margin:0}
.slide .body{container-type:size;position:absolute;left:51px;right:51px;top:145px;bottom:25px;display:grid;grid-template-columns:repeat(12,minmax(0,1fr));grid-template-rows:repeat(6,minmax(0,1fr));gap:var(--gap-sm);min-width:0;min-height:0}
.slide .body>*{min-width:0;min-height:0}.slide .group,.slide .stack,.slide .split{display:flex;gap:var(--gap-sm);min-width:0;min-height:0}.slide .group>*{flex:1;min-width:0;min-height:0}.slide .group.col,.slide .stack{flex-direction:column}.slide .stack{container-type:size}.slide .stack>*{flex:1;min-height:0}.slide .split>*{flex:1;min-width:0}.slide .split>:first-child{flex:.7}.slide .split.wide-left>:first-child{flex:1.4}
.slide .seat{aspect-ratio:1;inline-size:min(100%,90cqh,330px);align-self:center;justify-self:center;max-height:100%;background:var(--n-2);border:var(--stroke) solid var(--n-3);display:flex;align-items:center;justify-content:center;color:var(--n-7);font-size:var(--type-18);min-width:0;min-height:0}.slide .seat::after{content:attr(data-ph)}.slide .stack>.seat{flex:none;inline-size:min(100%,40cqh,330px);block-size:auto}.slide .seat.back{position:absolute;inset:0;width:100%;height:100%;aspect-ratio:auto;max-height:none}.slide.cover .lockup,.slide.cover .meta{z-index:1}.slide .seat.avatar{border-radius:50%}.slide .seat.portrait{aspect-ratio:3/4}.slide .seat.logo{aspect-ratio:1}.slide .icon{display:inline-flex;width:40px;height:40px;flex:none}.slide .icon>svg{width:100%;height:100%}
.slide.cover .lockup{position:absolute;max-width:calc(100% - 2*var(--gap-lg));}.slide.cover .lockup.at-center{left:10%;right:10%;top:20%;text-align:center}.slide.cover .lockup.at-left{left:104px;right:80px;top:70px}.slide.cover .lockup.at-bottom-left{left:var(--gap-lg);bottom:var(--gap-lg)}.slide.cover .lockup.at-top-left{left:var(--gap-lg);top:var(--gap-lg)}
.slide.cover .lockup>.kicker{margin:0 0 var(--gap-lg);color:var(--a1-7);font-size:var(--type-24);font-weight:var(--name-weight)}.slide.cover .lockup>.title{margin:0;font-size:var(--type-80);line-height:var(--onboard-docket-cover-line);font-weight:var(--figure-weight);letter-spacing:var(--title-track)}.slide.cover .lockup>.title b{color:var(--a1-7);font-weight:inherit}.slide.cover .lockup>.lead{font-size:var(--type-36);line-height:var(--lead-line);margin:var(--gap-lg) 0 0}.slide.cover .lockup.at-center>.lead{font-size:var(--type-18);line-height:var(--body-line);border-top:var(--stroke) solid var(--n-4);margin-top:96px;padding-top:var(--pad);color:var(--n-7)}
.slide.cover>.rail{position:absolute;right:47px;top:55px;bottom:55px;width:108px;border-radius:0 28px 28px 0;background:repeating-linear-gradient(to bottom,var(--a1-2-soft) 0 var(--stroke),transparent var(--stroke) 82.2px) 42px 95px / 48px 412px no-repeat,var(--a1);color:var(--a1-on);display:flex;flex-direction:column;justify-content:space-between;align-items:center;padding:calc(var(--pad)*1.875) 0 calc(var(--pad)*37/24) calc(var(--gap)*1.3)}.slide.cover>.rail>.icon{position:relative;width:30px;height:30px}.slide.cover:has(>.rail)>.page{left:47px;top:37px;bottom:39px;right:129px}.slide.cover .meta{position:absolute;left:104px;right:104px;bottom:105px;border-top:var(--stroke) solid var(--n-4);padding-top:var(--pad);font-size:var(--type-14);color:var(--n-7)}.slide.cover .meta>.label{display:inline-flex;border-radius:999px;background:var(--n-9);color:var(--page);padding:var(--gap-sm) var(--pad);margin-right:var(--gap)}
.slide.cover .lockup.at-left{top:75px}.slide.cover .lockup.at-left>.kicker{display:flex;align-items:center;gap:calc(var(--gap-sm)/2);font-size:clamp(var(--type-22),calc(1.796875cqw),var(--type-24));font-weight:var(--onboard-docket-cover-weight);line-height:var(--body-line);letter-spacing:var(--body-track)}.slide.cover .lockup.at-left>.kicker>.seat.logo{display:inline-flex;inline-size:23px;block-size:23px;aspect-ratio:1;font-size:var(--type-8);flex:none;border:0}
.slide.cover .lockup.at-left>.title{margin-left:calc(var(--stroke)*-2);font-size:clamp(var(--type-80),calc(6.40625cqw),var(--type-84));font-weight:var(--onboard-docket-cover-weight);line-height:var(--onboard-docket-cover-display-line);letter-spacing:var(--onboard-docket-cover-title-track)}.slide.cover .lockup.at-left>.title b{font-size:clamp(var(--type-76),calc(6.09375cqw),var(--type-80));letter-spacing:var(--onboard-docket-cover-accent-track)}.slide.cover .lockup.at-left>.lead{margin-top:calc(var(--pad)*37/24);margin-left:calc(var(--stroke)*-1);font-size:clamp(var(--type-32),calc(2.734375cqw),var(--type-36));line-height:var(--body-line);color:var(--n-9);letter-spacing:var(--body-track)}
.slide.cover:has(>.rail) .meta{left:104px;right:102px;bottom:94px;padding-top:var(--pad);font-size:var(--type-14);letter-spacing:var(--body-track)}.slide.cover:has(>.rail) .meta>.label{border-radius:999px;padding:calc(var(--gap-sm)/2) calc(var(--pad)*5/6);font-size:var(--type-12);font-weight:var(--body-weight);line-height:var(--body-line);margin-right:var(--gap)}

''')
put('foundation/fixtures/seat.html','<!-- min: 12x6 -->\n<section class="slide"><div class="top"><span class="label">AURUM WORKS</span><span class="sec">UNIT03</span></div><div class="page"><header class="head"><span class="no">03</span><h1 class="title">팀 성장을 위한 실행 원칙</h1></header><div class="body"><div class="seat" data-ph="1" style="grid-column:1 / span 12;grid-row:1 / span 6"></div></div></div></section>')
put('foundation/fixtures/cover.html','<!-- min: 12x6 -->\n<section class="slide cover"><div class="page"><div class="lockup at-center"><h1 class="title">TEAM GUIDE<br><b>04</b></h1><p class="lead">조직의 목표를 연결하고 다음 분기의 실행 기준을 함께 정합니다.</p></div></div></section>')
contract={json.loads((f/'element.json').read_text())['contract']:f.name for f in (REF/'samples/annual/elements').iterdir() if f.is_dir()};(P/'contract-folders.json').write_text(json.dumps(contract,indent=2))
print('map',len(instances),'instances;',len(gaps),'unexpressible; all19 pages source-node coverage complete; fresh kit/foundation')
