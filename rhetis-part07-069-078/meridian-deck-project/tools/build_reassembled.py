from pathlib import Path
import json,html,colorsys
P=Path(__file__).parent;C=P/'meridian-deck';A=P/'assets';A.mkdir(exist_ok=True);R=P/'reassembled';R.mkdir(exist_ok=True)
pal=json.load(open('/workspace/work/reference/contract/palette.json'))
# External source style: only palette assignments, geometry remains in collection.
light=pal['light'].copy();light['--page']='#ffffff';light['--ink']='#222222';light['--a1']='#0063ed';light['--a1-on']='#ffffff'
for depth in range(1,10):
 for suffix in ['', '-soft','-muted']:
  r,g,b=colorsys.hls_to_rgb(.597,.98-depth*.085, .9 if not suffix else .75 if suffix=='-soft' else .4)
  light[f'--a1-{depth}{suffix}']='#%02x%02x%02x'%(round(r*255),round(g*255),round(b*255))
light['--a1-7']='#0063ed'
light['--a1-7']='#0063ed'
(A/'source-palette.css').write_text('.slide{'+''.join(f'{k}:{v};' for k,v in light.items())+'}\n.slide.dark{'+''.join(f'{k}:{v};' for k,v in pal['dark'].items())+'}')
steps=json.load(open('/workspace/work/reference/contract/type-steps.json'));(A/'type-steps.css').write_text('.slide{'+''.join(f'--type-{v}:{v}px;' for v in steps)+'}')
def esc(s):return html.escape(str(s))
def el(e,root,content='',extra='',attrs=''):
 return f'<div class="{root}{(" "+extra) if extra else ""}" data-el="meridian-deck-{e}"{(" "+attrs) if attrs else ""}>{content}</div>'
def place(s,c,r,w,h):
 # Add placement to root without duplicating style attributes.
 import re
 m=re.search(r'<\w+\b[^>]*',s);tag=m.group(0);grid=f'grid-column:{c} / span {w}; grid-row:{r} / span {h}'
 if 'style="' in tag:new=tag.replace('style="','style="'+grid+'; ',1)
 else:new=tag+' style="'+grid+'"'
 return s[:m.start()]+new+s[m.end():]
def seat(n=1,cl=''):return f'<div class="seat {cl}" data-ph="{n}"></div>'
def frame(n=1):return el('image-frame','frame',seat(n))
def headline(s,note='',big=False,center=False,on=False):return el('headline','headline',f'<h2>{s}</h2>'+ (f'<p class="note">{note}</p>' if note else ''),' '.join(x for x in ['big' if big else '', 'center' if center else '', 'on' if on else ''] if x))
def prose(s,extra=''):return el('prose','prose',''.join('<p>'+x+'</p>' for x in s.split('\n\n')),extra)
def card(name,note='',fig='',ic='',on=False,quiet=False,line=False):
 p=(f'<span class="mark"><span class="icon" data-icon="{ic}"></span></span>' if ic else '')+(f'<p class="fig">{fig}</p>' if fig else '')+f'<p class="name">{name}</p>'+ (f'<p class="note">{note}</p>' if note else '')
 return el('card','card',f'<div class="parts">{p}</div>','on' if on else 'quiet' if quiet else 'line' if line else '')
def group(items,extra=''):return '<div class="group '+extra+'">'+''.join(items)+'</div>'
def stack(items):return '<div class="stack">'+''.join(items)+'</div>'
def pill(name,note='',on=True):return el('pill','pill',f'<div class="parts"><p class="name">{name}</p>'+ (f'<p class="note">{note}</p>' if note else '')+'</div>','on' if on else 'quiet')
def callout(s):return el('callout','callout','<p>'+s+'</p>')
def ls(items,notes=None,extra=''):
 return el('list','list',''.join(f'<div class="item"><b class="name">{s}</b>'+ (f'<p class="note">{notes[i]}</p>' if notes else '')+'</div>' for i,s in enumerate(items)),extra)
def bars(vals,labels=None):return el('chart-bar','bars',''.join(f'<div class="bar {"on" if i%2 else ""}" style="--v:{v}"><b>{v}</b><span>{labels[i] if labels else str(i+1)}</span></div>' for i,v in enumerate(vals)),attrs=f'style="--max:{max(vals)*1.15}"')
def lines(vals,labels=None):return el('chart-line','lines',''.join(f'<div class="pt" style="--v:{v}"><b>{v}</b><span>{labels[i] if labels else str(i+1)}</span></div>' for i,v in enumerate(vals)),attrs=f'style="--max:{max(vals)*1.15}"')
def donut(v,name=''):return el('chart-donut','donut',f'<b class="fig">{v}<small>%</small></b><p class="name">{name}</p>',attrs=f'style="--v:{v}"')
def person(n,name='김미리 대리',note='프로젝트 내 역할과 담당 분야를 명시해 책임 소재를 밝혀주세요.'):
 return el('person','person',seat(n,'portrait')+f'<b class="name">부서명</b><p class="note">{name}<br><br>{note}</p>')
def table(heads,rows):return el('table','tablebox','<table class="table"><thead><tr>'+''.join('<th>'+x+'</th>' for x in heads)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+str(v)+'</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table>')
def steps(names,notes=None):return el('steps','steps',''.join(f'<div class="step"><span class="mark">{i+1:02d}</span><b class="name">{x}</b><p class="note">{notes[i] if notes else "관련 내용을 간략하게 입력해주세요."}</p></div>' for i,x in enumerate(names)))
note='내용을 텍스트로 간략하게 입력해주세요. 관련 내용을 텍스트로 간략하게 입력해주세요.'
copy='이 페이지는 CEO의 인사말을 적는 페이지입니다. ESG에 관한 회사의 입장이나 20xx년의 성과에 대해 적어보세요. 회사 경영 방침이나 CEO의 의지를 표현할 수 있습니다.'
S={};heads={}
def page(n,title,sub,children):heads[n]=(title,sub);S[n]=''.join(children)
# Each slot below is solely a contract element or foundation grouping.
S[1]='<div class="lockup at-top-left"><h1 class="title">BUSINESS PROPOSAL<br><b>PRESENTATION</b></h1><p class="lead">Miri Company Project</p></div><div class="deco"></div><p class="meta">2090 BUSINESS PROJECT　　Please write down the presentation information here</p>'
page(2,'CONTENTS','서브 타이틀과 텍스트가 있는 목차',[place(el('agenda','agenda',''.join(f'<div class="entry"><b class="mark">{i:02d}</b><b class="name">상세설명형 목차</b><p class="note">각 파트의 구체적인 내용을 적어주세요.</p></div>' for i in range(1,10))),1,1,12,6)])
page(3,'','',[place(frame(),4,1,6,1),place(headline('<b>01</b><br>목차별 타이틀','각 파트의 상세 내용을 요약해주세요<br>주요 내용을 2-3줄로 정리해서 타이틀 내용을 설명해주세요',True,True),2,2,10,4),place(prose(note),2,6,10,1)])
page(4,'CEO MESSAGE','안녕하세요, 미리컴퍼니 대표 강미리 입니다.',[place(stack([prose('<b>'+h+'</b><br>'+copy) for h in ['존경하는 이해관계자 여러분에게,','하나, 앞으로의 경영 전략에 대해 적어주세요','둘, 앞으로의 경영 전략에 대해 적어주세요','셋, 앞으로의 경영 전략에 대해 적어주세요']]),1,1,7,6),place(person(1,'미리컴퍼니 대표이사 강미리','페이지내 인물사진은 샘플이미지입니다.'),9,1,3,6)])
page(5,'KEY POINT','비전을 소개하는 레이아웃',[place(group([card('VISION','텍스트로 간략하게 입력해주세요. 관련 내용을 간략하게 입력해주세요.',on=True) for i in range(3)]),2,2,10,4),place(prose('<b>VISION</b>　'+note+' '+note),2,6,10,1)])
page(6,'MAIN PROJECT','주요 프로젝트를 소개해주세요',[place(stack([frame(),prose('관련 이미지를 넣어주세요. 실제로 경험한 이미지를 실제로 경험한 업무 내용을 입력해주세요.')]),1,1,5,6),place(stack([stack([headline(f'<b>{i+1:02d}</b> '+h,note),group([pill('강조하고 싶은 포인트 내용을 입력하세요')]*2)]) for i,h in enumerate(['고객 니즈 │ CUSTOMER','문제 OR 기회상황 │ COMPANY','비교 대상 │ COMPETITOR'])]),6,1,7,6)])
page(7,'PROJECT NAME','텍스트 레이아웃',[place(headline('강조하고 싶은 내용은<br>이곳에 텍스트로 입력하세요',note+'<br>'+note,big=True,on=True),1,1,7,6),place(frame(),8,1,5,6)])
page(8,'PROJECT NAME','3개의 텍스트 목록 레이아웃',[place(ls(['이곳에 첫 번째 제목을 입력하세요','이곳에 두 번째 제목을 입력하세요','이곳에 세 번째 제목을 입력하세요'],[note]*3,'num divided'),1,1,6,6),place(frame(),8,1,5,4),place(frame(2),7,4,4,3)])
page(9,'KEY POINT','프로젝트 4단 핵심 포인트',[place(group([card(f'POINT {i+1:02d}','깔끔한 아이콘을 사용한 정리는 PPT의 퀄리티를 올려줍니다. 이곳에 관련 내용을 입력해주세요.',ic=ic,on=True) for i,ic in enumerate(['handshake','files','lightbulb','presentation'])]),1,1,12,6)])
page(10,'PROJECT NAME','아이콘과 텍스트 레이아웃',[place(frame(),1,1,5,6),place(ls(['제목을 입력하세요','이곳에 제목을 입력하세요','제목을 입력하세요'],[note]*3,'divided'),6,1,7,6)])
page(11,'PROJECT PROCESS','프로세스 상세 내용',[place(stack([card('경로 다변화로 신규 사용자 참여 확대','신규 유입의 주요 경로가 커뮤니티 콘텐츠 추천 흐름으로 이동. 콘텐츠 기반 유입 고객의 전환율이 기존 대비 +7%p'),card('기존 사용자의 반복 참여가 참여율 향상 견인','기존 고객의 반복 전환 비중이 성장. 이용 빈도 증가가 전환율 개선에 직접 기여.')]),1,1,5,6),place(stack([pill('고객 전환율 변화'),bars([35,39,43,48,50,54,64,69],['1Q','1Q','2Q','2Q','3Q','3Q','4Q','4Q'])]),6,1,7,6)])
page(12,'PROJECT NAME','SWOT 다이어그램',[place(el('matrix','matrix',''.join(f'<div class="cell"><b class="kick">{char}</b><b class="name">{name}</b>'+ls([note])+'</div>' for char,name in [('S','STRENGTH │ 강점'),('W','WEAKNESS │ 약점'),('O','OPPORTUNITY │ 기회'),('T','THREAT │ 위기')]),'swot'),1,1,12,6)])
page(13,'PROJECT PROCESS','프로세스 상세 내용',[place(headline('사용자 참여 확대 및 광고·제휴 수익 강화를 위해<br><b>연초 설정한 핵심 전략 방향</b>',center=True),2,1,10,1),place(group([card('커뮤니티 활동량 확대 및 사용자 체류 시간 증가',ic='message-circle',on=True),card('광고·제휴 기반 수익 구조 강화',ic='monitor-up',on=True)]),3,2,8,2),place(group([card(h,'일간 인기 콘텐츠 큐레이션 강화. 목표 달성을 위한 구체적인 전략 방향을 제시합니다.') for h in ['핵심 카테고리 콘텐츠 공급 확대','사용자 참여 촉진 구조 고도화','광고·제휴 상품 경쟁력 강화']]),1,4,12,3)])
values=[5,8,15,12,20,10,18,22,25,40,52,60,72,65,64]
area=el('chart-area','areas','<div class="series"><b class="name">성과 추이</b>'+''.join(f'<div class="pt" style="--v:{v}"><b>{v}</b></div>' for v in values)+'</div><div class="axis">'+''.join('<span>'+f'{i+1:02d}'+'</span>' for i in range(15))+'</div>',attrs='style="--max:80"')
page(14,'PROJECT DETAILS','프로세스 상세 내용',[place(headline('상단 <b>문장,</b><br>하단 <b>그래프</b> 넣는 페이지'),1,1,6,2),place(prose('<b>상단에는 아래의 그래프나 수치와 관련된 내용을 입력해 주세요.</b><br>프레젠테이션 주제와 관련된 동향이나 전망, 트렌드 등을 설명하는 용도로 사용해도 좋습니다.'),7,1,6,2),place(area,2,3,10,4)])
arch=el('architecture','arch',''.join('<div class="layer"><b class="name">'+h+'</b>'+''.join('<span class="chip">'+c+'</span>' for c in chips)+'</div>' for h,chips in [('VISION',['사업 목표 & 비전']),('STRATEGY',['핵심전략','핵심전략']),('ACTION',['세부전략','세부전략','세부전략'])]))
page(15,'PROJECT DETAILS','프로세스 상세 내용',[place(arch,1,1,12,6)])
page(16,'PROJECT DETAILS','프로세스 상세 내용',[place(stack([group([frame(i+1),headline(f'<b>{i+1:02d} {h}</b>', '좌측에 관련 이미지를 넣어주세요. 실제로 경험한 이미지를 넣으면 더 좋습니다. 업무 현장 사진을 추가해주세요. 관련 도표를 넣어주셔도 좋습니다.')]) for i,h in enumerate(['고객 니즈 │ CUSTOMER','문제 OR 기회상황 │ COMPANY','비교대상 │ COMPETITOR'])]),1,1,12,6)])
page(17,'PROJECT DETAILS','프로세스 상세 내용',[place(headline('<b>3개 프로젝트 모두 핵심 지표에서</b><br>일정 수준 이상의 개선을 보이며 안정적인 성과 달성',center=True),2,1,10,1),place(stack([pill('성과요약'),pill('관련수치',on=False),pill('분기별 지표',on=False)]),1,3,2,4),place(group([stack([card(f'프로젝트 {i+1}',note,quiet=True),lines(v,['2Q','3Q','4Q'])]) for i,v in enumerate([[20,35,61],[25,65,80],[30,36,69]])]),3,2,10,5)])
hub=el('hub','hub','<div class="core"><b class="name">아이템 또는<br>핵심 기술명</b></div>'+''.join(f'<div class="spoke"><b class="name">{h}</b><p class="note">텍스트를 입력해주세요.<br>폰트는 프리텐다드 Regular 입니다.<br>강조 텍스트는 Bold를 사용해주세요.</p></div>' for h in ['분야 및 타겟','특징','용도 및 성능','장점']))
page(18,'PROJECT DETAILS','프로세스 상세 내용',[place(hub,1,1,12,6)])
page(19,'PROJECT DETAILS','프로세스 상세 내용',[place(group([card('타이틀을 입력해주세요','판매 방법 및 전략에 대한 설명을 입력해주세요. 폰트는 프리텐다드 Regular 크기는 16입니다.')]*4,'two'),1,1,5,6),place(table(['프로젝트 자금','금액','자기자금','타인자금'],[[h,'텍스트 입력','텍스트 입력','텍스트 입력'] for h in ['창업자금','부지매입','공장건축','생산설비','제조원가','일반관리']]),7,1,6,6)])
page(20,'PROJECT DEVELOPE','프로세스 해결 방안',[place(headline('운영 과정에서 확인된 주요 이슈와<br><b>이를 해결하기 위한 개선 방향</b>',center=True),2,1,10,1),place(stack([group([card(h,ic=ic,on=True),prose(a),el('delta','delta','<span class="from"></span><span class="to"></span>'),prose(b)]) for h,ic,a,b in [('사용자 경험','network','초기 진입 시 원하는 콘텐츠를 찾기까지 단계가 많아 이탈 존재','진입 동선을 단순화하고 핵심 콘텐츠 접근성을 높이는 구조 개편 검토 필요'),('노출 로직','grid-3x3','로직이 사용자 패턴을 충분히 반영하지 못해 일관성 낮음','사용자 행동 기반 데이터 반영을 강화하고 추천 기준을 재정비'),('콘텐츠 품질','calendar','사용자 경험에 부정적 영향을 준 문제를 한 줄로 입력해 보세요.','해결을 위해 향후 추진할 필요가 있는 개선 방향을 작성해 보세요.')]]),1,2,12,5)])
rows=[[h,'프로젝트 인력 비용' if i==0 else '상세 내역을 적어주세요',v+'원',m,'XX팀 포함 총 3인' if i==0 else '내용을 적어주세요','내용을 적어주세요'] for i,(h,v,m) in enumerate(zip(['인건비','비품','운영비','예비비','광고비','항목'],['3,000,000','500,000','5,000,000','2,000,000','800,000','9,000,000'],['3월 중순','2월 중순','3월 중순','4월 중순','2월 중순','3월 중순']))]
page(21,'PROJECT DEVELOPE','표를 활용한 레이아웃',[place(table(['항목','상세내역','예산비용','집행시기','비고','비고2'],rows),1,1,12,6)])
cycle=el('cycle','cycle','<div class="core"><b class="name">개선 방향</b></div>'+''.join(f'<div class="node"><b class="name">{x}</b><p class="note">키워드{x}에 대해 입력해주세요.</p></div>' for x in 'ABCD'))
page(22,'PROJECT DEVELOPE','그래픽을 활용한 레이아웃',[place(headline('운영 과정에서 확인된 주요 이슈와<br><b>이를 해결하기 위한 개선 방향</b>',center=True),2,1,10,1),place(cycle,3,2,8,5),place(prose('주제에 대한 세부내용을 간략하게 입력해주세요.'),1,3,2,3),place(prose('주제에 대한 세부내용을 간략하게 입력해주세요.'),11,3,2,3)])
track=el('timeline','track',''.join(f'<div class="stop {"on" if i%2==0 else ""}"><p class="kick">{i+1:02d}<br>20XX</p><b class="name">타이틀 텍스트 입력</b><p class="note">{note}</p></div>' for i in range(5)),'alt')
page(23,'PROJECT NAME','연혁을 나타내는 레이아웃',[place(track,1,1,12,6)])
page(24,'PROJECT DEVELOPE','프로세스 해결 방안',[place(callout('이곳에 프로젝트 결과에 대해 강조하고 싶은 내용을 텍스트로 입력해 주세요. 관련 내용을 텍스트로 입력해주세요.'),1,1,12,1),place(stack([group([headline('<b>'+h+'</b>',note),ls(['강조하고 싶은 포인트 내용을 입력하세요']*2)]) for h in ['문제해결 액션','생산성 증가 액션','의사소통 협상 액션']]),1,2,7,5),place(frame(),8,2,5,5)])
pos=el('positioning','posmap','<div class="axis-x"><span>낮음</span><span>실행용이성</span><span>높음</span></div><div class="axis-y"><span>높음</span><span>영향도</span><span>낮음</span></div>'+''.join(f'<div class="mark on" style="--x:{x};--y:{y}"><b class="name">{h}</b></div>' for x,y,h in [(88,93,'배송 시스템 개선'),(49,78,'간편 결제 오류 해결'),(77,61,'CS 응대 표준화'),(46,46,'반품 프로세스 간소화')]))
page(25,'PROJECT NAME','사분면을 나타내는 레이아웃',[place(ls(['배송 시스템 개선','응대 표준화','결제 오류 해결','반품 과정 간소화'],[note]*4,'divided'),1,1,4,6),place(stack([pill('실행용이성 사분면'),pos]),6,1,7,6)])
page(26,'PROJECT NAME','그래프를 나타내는 레이아웃',[place(headline('프로젝트와 관련된 내용을 기재하고<br><b>강조할 내용은 포인트 컬러를 활용하세요</b>',center=True),2,1,10,1),place(group([stack([pill('키워드',on=i==3),prose('업무별 성과 달성률이나 예산 집행률 표현에 좋아요.'),donut(v)]) for i,v in enumerate([80,70,75,91])]),1,2,12,5)])
page(27,'PROJECT NAME','3개의 사진과 텍스트',[place(group([stack([frame(i+1),card('타이틀 텍스트 입력',note)]) for i in range(3)]),1,1,12,6)])
page(28,'PROJECT NAME','단계별 프로세스 레이아웃',[place(steps(['물류 중계 거점 확대','AI 기반 배송 최적화','멀티 물류사 통합 관리','고객 맞춤 배송 서비스'],['개선과제의 상세내용을 넣어보세요.']*4),1,1,12,5),place(callout('전체 예상 투자 규모: <b>XX억원</b>　│　연간 기대 효과: <b>매출 증대 XX억원, 비용 절감 XX억원</b>'),1,6,12,1)])
page(29,'PROJECT NAME','4개 이미지 레이아웃',[place(headline('부서별 인재에 대해 상세 설명을 기재해주세요',center=True),2,1,10,1),place(el('person','people',''.join(person(i+1) for i in range(4))),1,2,12,5)])
S[30]='<div class="lockup at-center"><p class="kicker">Miri Company Project</p><h1 class="title">THANK YOU FOR<br><b>ATTENTION</b></h1><p class="lead">프레젠테이션을 마치겠습니다. 감사합니다.</p></div><div class="deco"></div><p class="meta">2090 BUSINESS PROJECT　　담당자: 김미리　│　T 02.1234.5678　│　M 010.1234.5678　│　E mm@miricompany.com</p>'
links=['../assets/fonts/fonts.css','../meridian-deck/kit/css/tokens.css','../meridian-deck/foundation/foundation.css','../assets/type-steps.css','../assets/source-palette.css']+['../meridian-deck/elements/'+x.name+'/element.css' for x in sorted((C/'elements').iterdir())]
for n,body in S.items():
 if n not in [1,30]:
  title,sub=heads[n];body='<header class="head"><p class="kicker">2090 BUSINESS PROJECT</p><h1 class="title">'+title+'</h1><p class="lead">'+sub+'</p></header><div class="body">'+body+'</div><footer class="foot">PRESENTATION · '+str(1 if n<=6 else 2 if n<=8 else 3 if n==9 else 4 if n<=13 else 5 if n<=18 else 6 if n<=23 else 7 if n<=27 else 8).zfill(2)+'</footer>'
 else:body=body
 (R/f'slide_{n:02d}.html').write_text('<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=1280"><title>Meridian Deck Reassembled '+str(n)+'</title>'+''.join('<link rel="stylesheet" href="'+x+'">' for x in links)+'</head><body><section class="slide '+('cover' if n in [1,30] else '')+'"><div class="page">'+body+'</div></section></body></html>')
fixtures=C/'foundation/fixtures'
for f in fixtures.glob('*.html'):f.unlink()
(fixtures/'seat.html').write_text('<!-- min: 12x6 -->\n<section class="slide"><div class="page"><header class="head"><p class="kicker">2090 BUSINESS PROJECT</p><h1 class="title">PROJECT NAME</h1><p class="lead">정보의 위계를 명확히 전달합니다</p></header><div class="body"><div class="seat" data-ph="1" style="grid-column:1 / span 5;grid-row:1 / span 6"></div><div class="seat" data-ph="2" style="grid-column:7 / span 6;grid-row:1 / span 6"></div></div><footer class="foot">PRESENTATION</footer></div></section>')
(fixtures/'cover.html').write_text('<!-- min: 12x6 -->\n<section class="slide cover"><div class="page">'+S[1]+'</div></section>')
print('Reassembled pages:',len(S))
