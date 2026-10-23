from pathlib import Path
import json,re
R=Path('/workspace/work/deliverables/dockside');C=R/'collection/dockside';V=R/'review';D=V/'reassembled';D.mkdir(exist_ok=True)
steps=json.load(open('/workspace/work/reference/contract/type-steps.json'));pal=json.load(open('/workspace/work/reference/contract/palette.json'));env="@font-face{font-family:'Pretendard Variable';src:url('font.woff2');font-weight:100 900}\n"+'.slide{'+''.join(f'--type-{n}:{n}px;' for n in steps)+'}\n'+''.join(('.slide.dark' if mode=='dark' else '.slide')+'{'+''.join(k+':'+v+';' for k,v in val.items())+'}\n' for mode,val in pal.items())
(V/'assets/environment.css').write_text(env)
links=['kit/css/tokens.css','foundation/foundation.css']+[str(p.relative_to(C)) for p in sorted(C.glob('elements/*/element.css'))]
HEAD='<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=1280"><title>Dockside reassembled</title>'+''.join('<link rel="stylesheet" href="../../collection/dockside/'+s+'">' for s in links)+'<link rel="stylesheet" href="../assets/environment.css"></head><body style="margin:0">'
def el(f,cls,content='',data=''):return f'<div class="{cls}" data-el="dockside-{f}"{(" style="+chr(34)+data+chr(34)) if data else ""}>{content}</div>'
def parts(k='',name='',note='',fig='',mark=''):
 return '<div class="parts">'+(f'<p class="kick">{k}</p>' if k else '')+(f'<div class="mark">{mark}</div>' if mark else '')+(f'<b class="fig">{fig}</b>' if fig else '')+(f'<h3 class="name">{name}</h3>' if name else '')+(f'<p class="note">{note}</p>' if note else '')+'</div>'
def card(name,note='',kick='',fig='',variant='',icon=None):return el('card','card '+variant,parts(kick,name,note,fig,('<span class="icon" data-icon="'+icon+'"></span>') if icon else ''))
def headline(t,note='',kick='',variant=''):return el('headline','headline '+variant,(f'<p class="kick">{kick}</p>' if kick else '')+'<h2>'+t+'</h2>'+(f'<p class="note">{note}</p>' if note else ''))
def prose(t,variant=''):return el('prose','prose '+variant,'<p>'+t+'</p>')
def frame(n):return el('image-frame','frame',f'<div class="seat" data-ph="{n}"></div>')
def pill(t,variant=''):return el('pill','pill '+variant,parts(name=t))
def callout(t):return el('callout','callout','<p>'+t+'</p>')
def listel(items,variant='check'):
 return el('list','list '+variant,''.join('<div class="item">'+((f'<span class="mark"><span class="icon" data-icon="{it[2]}"></span></span>') if len(it)>2 else '')+f'<b class="name">{it[0]}</b>'+((f'<p class="note">{it[1]}</p>') if len(it)>1 else '')+'</div>' for it in items))
def group(items,variant=''):return '<div class="group '+variant+'">'+''.join(items)+'</div>'
def stack(items):return '<div class="stack">'+''.join(items)+'</div>'
def donor(val,name):return '<div class="donut" style="--v:'+str(val)+'"><b class="fig">'+str(val)+'<small>%</small></b><span class="name">'+name+'</span></div>'
def donuts(items):return el('chart-donut','donuts',''.join(donor(v,t) for v,t in items))
def stat(fig,name,note=''):return el('metric','stat',parts(name=name,note=note,fig=fig))
def person(name,role,n):return '<div class="person"><div class="seat avatar" data-ph="'+str(n)+'"></div><b class="name">'+name+'</b><p class="note">'+role+'</p></div>'
def people(items):return el('person','people',''.join(person(*x) for x in items))
def steps(items):return el('steps','steps',''.join(f'<div class="step"><span class="mark">0{i+1}</span><b class="name">{t}</b><p class="note">{note}</p></div>' for i,(t,note) in enumerate(items)))
def hub(core,items):return el('hub','hub','<div class="core"><b class="name">'+core+'</b></div>'+''.join(f'<div class="spoke"><b class="name">{t}</b><p class="note">{n}</p></div>' for t,n in items))
def grid(s,c,r,cs=12,rs=6):
 m=re.search(r'<(?:div|section)\b[^>]*',s)
 if not m:raise ValueError(s)
 # body placement only; chart data declarations remain on their contract node.
 start=m.group(0)
 if ' style="' in start:new=start.replace(' style="',f' style="grid-column:{c} / span {cs}; grid-row:{r} / span {rs}; ')
 else:new=start+f' style="grid-column:{c} / span {cs}; grid-row:{r} / span {rs}"'
 return s[:m.start()]+new+s[m.end():]
rail='<aside class="rail">'+''.join(f'<div class="seat" data-ph="{i}"></div>' for i in range(1,10))+'</aside>'
scene=[]
def write(n,title,chapter,bodies,cover=False,subtitle=''):
 if cover:
  body='<section class="slide cover"><div class="page"><div class="top"><span class="deck">Miri Company</span><span>Innovation　 Strategy　 Proposal　 Project</span></div><div class="lockup at-center"><h1 class="title">'+title+'</h1>'+(f'<p class="lead">{subtitle}</p>' if subtitle else '')+'</div><div class="deco">'+''.join(f'<div class="seat{" on" if i==5 else ""}" data-ph="{i}"></div>' for i in range(1,10))+'</div></div></section>'
 else:body='<section class="slide">'+rail+'<div class="page"><div class="top"><span class="deck">Miri Company</span><span>Business Presentation</span></div><header class="head"><p class="kicker">Chapter '+str(chapter).zfill(2)+'</p><h1 class="title">'+title+'</h1></header><div class="body">'+''.join(bodies)+'</div></div></section>'
 (D/f'slide_{n:02}.html').write_text(HEAD+body+'<script src="../assets/icons.js"></script></body></html>')
# Same original page sequence, recomposed exclusively from the design library.
write(1,'<b>번뜩이는 생각 그대로</b><br>아이디어 피칭',0,[],True)
write(2,'<b>아이디어</b> 키워드 입력',0,[grid(stack([pill('아이디어를 한 문장으로 요약하여 입력합니다.','line'),group([pill('Keyword 01','line'),pill('Keyword 02','line'),pill('Keyword 03','line'),pill('Keyword 04','line')])]),2,2,10,3)])
write(3,'목차 안내',0,[grid(el('agenda','agenda',''.join('<div class="entry"><span class="mark">0'+str(i+1)+'</span><b class="name">'+t+'</b><p class="note">이곳에 하위 항목을 입력합니다.<br>항목이 여러 개인 경우 글머리표를 활용해 정리합니다.</p></div>' for i,t in enumerate(['우리가 발견한 문제','아이디어와 실행 방법','기대효과와 계획']))),1,2,12,5)])
write(4,'현재 상황',1,[grid(prose('<b>Current Situation</b><br>문제 인식을 공유하고 방향성을 설정하는 단계입니다.','quiet'),1,4,3,3),grid(listel([(t,) for t in ['시장 또는 타깃 고객이 처한 상황을 구체적으로 작성합니다.','가능한 수치나 사례를 포함하면 효과적입니다.','해당 상황에서 발생하는 주요 문제점이나 불편함을 작성합니다.','기존 해결책의 한계를 설명합니다.','핵심 내용을 가로로 나열해 강조하세요.']]),5,1,8,6)])
write(5,'현재 상황',1,[grid(prose('<b>Current Situation</b><br>현재 상황을 보여주는 주요 지표에 대해 그래프로 나타냅니다.','quiet'),1,4,3,3),grid(stack([pill('전년 대비 이용자수 증가율','on'),el('chart-bar','bars','<div class="bar" style="--v:100"><b>20XX</b><span>이전</span></div><div class="bar on" style="--v:250"><b>+150%</b><span>현재</span></div>','--max:300'),prose('이용자 수 150% 증가로 운영 부담과 매출 가능성이 높아졌습니다.','quiet')]),5,1,4,6),grid(stack([pill('고객 중 불편을 느끼는 비율','on'),donuts([(40,'불편을 느끼는 고객')]),prose('불편 경험 비율이 2배 증가하며 서비스 개선 필요성이 분명해졌습니다.','quiet')]),9,1,4,6)])
write(6,'페인포인트',2,[grid(prose('<b>Pain Point</b><br>고객의 페인 포인트를 시각적으로 표현하는 페이지입니다.','quiet'),1,4,3,3),grid(stack([frame(1),card('눈길을 끄는 시각 자료','이미지와 설명을 함께 배치해 내용을 직관적으로 전달하는 가장 효과적인 페이지입니다.')]),5,1,4,6),grid(stack([frame(2),card('신뢰를 주는 증거 사진','텍스트로만 설명하기 어려운 분위기나 디테일을 시각 자료로 보여주면 이해가 빨라집니다.')]),9,1,4,6)])
write(7,'페인포인트',2,[grid(hub('중심 키워드',[('시간 소요',''),('비용 부담',''),('정보 부족',''),('접근성 제한','')]),1,1,5,6),grid(listel([(t,'구체적인 불편사항이나 문제상황을 간단히 작성합니다.') for t in ['시간 소요','비용 부담','정보 부족','접근성 제한']],'num divided'),7,1,6,6)])
write(8,'우리의 <b>인사이트</b>',3,[grid(group([card('시장 트렌드','시장이나 고객 행동의 변화 트렌드를 작성합니다. 리서치 결과를 바탕으로 구체적인 변화 양상을 서술하세요.','INSIGHT 01',icon='chart-column'),card('충족되지 않은 니즈','현재 시장에서 충족되지 못한 고객의 숨은 요구나 불편을 작성합니다. 반복되는 불편 요소를 정리하세요.','INSIGHT 02',icon='notebook-text'),card('기회 포착','트렌드와 니즈를 바탕으로 발견한 비즈니스 기회를 작성합니다. 기대 효과나 차별화 포인트를 제시하세요.','INSIGHT 03',icon='target')]),1,2,12,5)])
write(9,'우리의 <b>인사이트</b>',3,[grid(prose('<b>Our Insights</b><br>환경과 조건을 바탕으로 핵심 인사이트와 기회를 정리하는 페이지입니다.','quiet'),1,4,3,3),grid(listel([('고객 행동 패턴','타깃 고객의 실제 행동이나 구매 패턴에서 발견한 특이점을 작성합니다.','search'),('경쟁사의 공백','기존 서비스나 경쟁사가 놓치고 있는 영역이나 약점을 작성합니다.','building-2'),('기술적 가능성','최근 기술 발전이나 인프라 개선으로 새롭게 실현 가능해진 솔루션을 작성합니다.','lightbulb')],'divided'),5,1,8,6)])
write(10,'핵심 <b>아이디어</b>',4,[grid(frame(1),1,1,12,4),grid(group([pill('Idea 01','line'),pill('Idea 02','line')]),1,5,4,1),grid(prose('아이디어의 핵심 개념을 한 문장으로 명확하게 작성합니다. 이 솔루션이 어떻게 작동하는지 간단한 메커니즘을 설명합니다.','quiet'),5,5,8,2)])
write(11,'아이디어 <b>개요</b>',4,[grid(frame(1),1,1,4,6),grid(stack([callout('이곳에 <b>아이디어 또는 핵심 가치</b>를 작성합니다.'),listel([(t,) for t in ['솔루션이 제공하는 핵심 기능과 특징을 작성합니다.','어떤 방식으로 문제를 해결하는지 구체적인 접근 방법을 서술합니다.','사용자가 이 솔루션을 통해 얻게 되는 주요 편익이나 경험을 작성합니다.','솔루션의 확장 가능성이나 추가 가치를 설명합니다.']])]),6,1,7,6)])
write(12,'작동 원리',5,[grid(group([stack([pill('사용자 입력 및 요청','on'),frame(1),prose('해당 단계에서 일어나는 주요 동작이나 과정을 작성합니다. 사용자 또는 시스템의 행동을 구체적으로 서술합니다.','quiet')]),stack([pill('데이터 처리 및 매칭','on'),frame(2),prose('해당 단계에서 일어나는 주요 동작이나 과정을 작성합니다. 사용자 또는 시스템의 행동을 구체적으로 서술합니다.','quiet')])]),1,1,12,6)])
write(13,'작동 원리',5,[grid(frame(1),1,1,7,6),grid(listel([(t,'숫자에 해당하는 기능이나 요소가 무엇인지, 어떤 역할을 하는지 설명합니다.') for t in ['사용자 입력 화면','데이터 분석 엔진','매칭 알고리즘','결과 제공 화면']],'num divided'),8,1,5,6)])
write(14,'주요 기능',6,[grid(frame(2),1,2,4,4),grid(frame(1),5,1,8,4),grid(callout('이곳에 <b>핵심 기능의 전체 개요나 컨셉트</b>를 한 줄로 작성합니다.'),5,5,8,2)])
write(15,'주요 기능',6,[grid(card('실시간 알림','해당 기능이 어떻게 작동하는지, 사용자에게 어떤 정보를 제공하는지 작성합니다.','핵심 기능 01'),1,1,4,3),grid(card('간편 결제','구체적인 예시를 포함해 사용자의 경험을 설명합니다.','핵심 기능 02'),1,4,4,3),grid(frame(1),5,2,4,4),grid(card('맞춤 추천','사용자 니즈에 맞는 기능의 역할과 제공 가치를 설명합니다.','핵심 기능 03'),9,1,4,3),grid(card('데이터 분석','데이터를 활용해 어떻게 사용자 문제를 해결하는지 설명합니다.','핵심 기능 04'),9,4,4,3)])
write(16,'그 외 기타 <b>기능</b>',6,[grid(group([stack([pill('알림 설정','on'),frame(1)]),stack([pill('데이터 저장','on'),frame(2)]),stack([pill('공유 기능','on'),frame(3)])]),1,1,12,5),grid(callout('이곳에 <b>핵심 기능의 전체 개요나 컨셉트</b>를 한 줄로 작성합니다.'),1,6,12,1)])
write(17,'차별화 <b>포인트</b>',7,[grid(hub('아이디어 관련 키워드',[(t,'해당 차별화 포인트가 타사 제품 혹은 기존 제품에 비해 나은 점을 입력합니다.') for t in ['빠른 응답 속도','차별화 포인트 키워드','직관적인 사용 경험','차별화 포인트 키워드']]),1,1,12,6)])
write(18,'차별화 <b>포인트</b>',7,[grid(stack([card('최신 AI 기술 적용','이것이 경쟁사나 기존 방식과 다른 차별화 요소를 작성합니다. 해당 포인트가 중요한 이유, 고객에게 제공하는 이점을 함께 서술합니다.','01',icon='sparkles'),card('사용자 중심 직관적 UI','이것이 경쟁사나 기존 방식과 다른 차별화 요소를 작성합니다. 고객에게 제공하는 이점을 함께 서술합니다.','02',icon='layout-dashboard')]),1,1,12,6)])
write(19,'예상 타겟 <b>페르소나</b>',8,[grid(people([('페르소나1 이름','직업이나 상황 입력 · 주요 니즈 입력 · 행동 패턴 입력',1),('페르소나2 이름','직업이나 상황 입력 · 주요 니즈 입력 · 행동 패턴 입력',2),('페르소나3 이름','직업이나 상황 입력 · 주요 니즈 입력 · 행동 패턴 입력',3)]),1,1,12,6)])
write(20,'기대효과',9,[grid(prose('<b>Expected Outcomes</b><br>솔루션 도입을 통해 기대되는 주요 성과를 정량적으로 보여주는 페이지입니다.','quiet'),1,4,3,3),grid(donuts([(40,'업무 관련 비용 절감'),(60,'고객 만족도 향상')]),5,1,8,4),grid(callout('솔루션 도입으로 <b>운영 효율성과 고객 경험</b>이 동시에 개선됩니다.'),5,5,8,2)])
write(21,'기대효과',9,[grid(listel([('사용자 만족도','예상되는 효과를 구체적으로 작성합니다. 개선 전후 수치나 예시를 포함합니다.','users'),('업무 효율성','예상되는 효과를 구체적으로 작성합니다. 개선 전후 수치나 예시를 포함합니다.','settings'),('비용 절감','예상되는 효과를 구체적으로 작성합니다. 개선 전후 수치나 예시를 포함합니다.','wallet')],'divided'),1,1,8,6),grid(hub('최종 기대효과 입력란',[('만족도','고객 경험 개선'),('효율','운영 개선'),('절감','비용 개선')]),9,2,4,4)])
write(22,'실행 계획',10,[grid(steps([(t,'해당 단계의 구체적인 활동을 작성합니다. 주요 타깃과 실행 방법을 작성합니다.') for t in ['프로토타입 만들기','소규모 사용자 모집','사용자 확대']]),1,1,12,6)])
write(23,'실행 계획',10,[grid(steps([(t,'핵심 시기와 주요 활동과 목표를 2~3줄로 작성합니다.') for t in ['아이디어 구체화','프로토타입 개발','베타테스트 진행','정식 서비스 오픈','사용자 피드백 반영']]),1,1,12,5),grid(callout('단계별 검증을 통해 <b>리스크를 최소화</b>합니다.'),7,6,6,1)])
write(24,'구현 시 <b>필요사항</b>',11,[grid(stack([card('중요 키워드 설명 01','항목에 대한 구체적인 설명이나 세부 요구사항을 2~3줄로 작성합니다. 왜 필요한지, 어떻게 확보할 것인지 등을 명시합니다.'),card('중요 키워드 설명 02','항목에 대한 구체적인 설명이나 세부 요구사항을 2~3줄로 작성합니다. 왜 필요한지, 어떻게 확보할 것인지 등을 명시합니다.')]),1,1,5,6),grid(hub('필요 요소',[(t,'') for t in ['예산 키워드','시간 키워드','기타 키워드','장비 키워드','파트너 키워드']]),7,1,6,6)])
write(25,'해결해야 할 <b>과제들</b>',12,[grid(stack([card('남은 과제들','해결되지 않은 기술적 문제나 구현 난이도를 작성합니다. 부족한 리소스나 시간 관련 이슈를 작성합니다. 시간이나 일정상의 제약 사항을 작성합니다.','Challenges'),card('해결 방법','해결하기 위한 구체적인 기술적 대안이나 방법론을 작성합니다. 파트너십 구축, 외부 협업 등 리소스 확보 방안을 작성합니다. 우선순위 조정 등 실행 전략을 작성합니다.','Solutions')]),2,1,10,6)])
write(26,'해결해야 할 <b>과제들</b>',12,[grid(prose('<b>Key Challenges</b><br>실행 과정에서 예상되는 주요 과제와 대응 방안을 정리하는 페이지입니다.','quiet'),1,4,3,3),grid(el('versus','versus','<div class="side"><b class="name">준비 과정 중 이슈</b>'+listel([('기술적 구현','어려운 부분이나 기술 관련 이슈를 작성합니다.'),('예산과 리소스','자원 관련 이슈를 작성합니다.'),('일정과 인력','실행 과정의 이슈를 작성합니다.')])+'</div><b class="vs">VS</b><div class="side on"><b class="name">이슈 해결 방안</b>'+listel([('대안 기술','구체적인 해결 방법이나 대안 기술을 작성합니다.'),('단계적 접근','파트너십이나 단계적 접근 방법을 작성합니다.'),('자원 활용','다양한 자원을 활용한 해결 방법을 작성합니다.')])+'</div>'),5,1,8,6)])
write(27,'우리팀 <b>소개</b>',13,[grid(prose('<b>Our Team</b><br>프로젝트를 수행하는 팀 구성과 역할 구조를 소개하는 페이지입니다.','quiet'),1,4,3,3),grid(el('hierarchy','org','<div class="root"><b class="name">김미리 · 팀장 / 리더</b></div>'+''.join('<div class="branch"><div class="node"><b class="name">'+t+'</b></div><div class="leaf">'+role+'</div></div>' for t,role in [('박미리','기획 / 개발'),('오미리','디자인 / UI'),('강미리','마케팅 / 운영')])),5,2,8,5)])
write(28,'우리팀 <b>소개</b>',13,[grid(el('mindmap','mindmap','<div class="core"><b class="name">Team Name<br>팀이름</b></div>'+''.join('<div class="branch"><b class="name">'+name+'</b><span class="leaf">'+role+'</span></div>' for name,role in [('김미리','기획'),('강미리','개발'),('박미리','디자인'),('오미리','마케팅')])),1,1,12,6)])
write(29,'예상 질문과 <b>답변</b>',14,[grid(stack([group([pill('Q. 기존 서비스와 무엇이 다른가요?','on'),card('질문에 대한 명확하고 구체적인 답변','청중이 궁금해할 만한 핵심 내용을 포함합니다. 또한 구체적인 예시나 수치를 포함하면 좋습니다.')]),group([pill('Q. 개발 기간은 얼마나 걸리나요?','on'),card('질문에 대한 명확하고 구체적인 답변','청중이 궁금해할 만한 핵심 내용을 포함합니다. 또한 구체적인 예시나 수치를 포함하면 좋습니다.')])]),1,1,12,6)])
write(30,'클로징',0,[],True,'경청해 주셔서 감사합니다.')
# Rhetis-like icon hydration only; no layout or design CSS is introduced.
(V/'assets/icons.js').write_text('''document.querySelectorAll('[data-icon]').forEach(e=>{const paths={"search":"<circle cx=10 cy=10 r=6/><path d=\\"m15 15 6 6\\"/>","lightbulb":"<path d=\\"M9 18h6m-6 3h6M9 15a7 7 0 1 1 6 0v3H9z\\"/>","target":"<circle cx=12 cy=12 r=8/><circle cx=12 cy=12 r=4/><path d=\\"m12 12 9-9\\"/>"};e.innerHTML='<svg viewBox="0 0 24 24" width="100%" height="100%" fill="none" stroke="currentColor" stroke-width="1.5">'+(paths[e.dataset.icon]||'<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/>')+'</svg>'});''')
print('Reassembled sources',len(list(D.glob('slide*.html'))))
