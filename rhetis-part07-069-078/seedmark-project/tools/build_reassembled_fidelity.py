from pathlib import Path
import json,re
P=Path(__file__).parent;C=P/'seedmark';R=P/'reassembled';R.mkdir(exist_ok=True)
STEPS=json.loads(Path('/workspace/work/reference/contract/type-steps.json').read_text())
(R/'type-steps.css').write_text('.slide{'+''.join(f'--type-{n}: {n}px;'for n in STEPS)+'}')
# This file only assigns externally supplied measure tokens; all geometry comes from collection sources.
links='<link rel="stylesheet" href="../assets/fonts/fonts.css"><link rel="stylesheet" href="../seedmark/kit/css/tokens.css"><link rel="stylesheet" href="type-steps.css"><link rel="stylesheet" href="../assets/source-palette.css"><link rel="stylesheet" href="../seedmark/foundation/foundation.css">'+''.join(f'<link rel="stylesheet" href="../seedmark/elements/{e.name}/element.css">'for e in sorted((C/'elements').iterdir()))
def el(folder,root,html='',attrs='',cl=''):return f'<div class="{root} {cl}" data-el="seedmark-{folder}" {attrs}>{html}</div>'
def place(s,c,r,w,h):
 grid=f'grid-column:{c} / span {w};grid-row:{r} / span {h};'
 head,tail=s.split('>',1)
 if 'style="' in head:head=re.sub(r'style="([^"]*)"',lambda m:'style="'+grid+m.group(1)+'"',head,count=1)
 else:head+=' style="'+grid+'"'
 return head+'>'+tail
def pure(s):
 head,tail=s.split('>',1);head=re.sub(r' style="grid-column:[^"]*"','',head);return head+'>'+tail
def group(items,c=1,r=1,w=12,h=6,cl=''):return f'<div class="group {cl}" style="grid-column:{c} / span {w};grid-row:{r} / span {h}">'+''.join(items)+'</div>'
def stack(items,c=1,r=1,w=12,h=6):return f'<div class="stack" style="grid-column:{c} / span {w};grid-row:{r} / span {h}">'+''.join(items)+'</div>'
def card(name,note='',kick='',fig='',icon='',cl=''):
 x=(f'<span class="mark"><span class="icon" data-icon="{icon}"></span></span>'if icon else'')+(f'<p class="kick">{kick}</p>'if kick else'')+(f'<p class="fig">{fig}</p>'if fig else'')+(f'<h3 class="name">{name}</h3>'if name else'')+(f'<p class="note">{note}</p>'if note else'')
 return el('card','card','<div class="parts">'+x+'</div>',cl=cl)
def pill(name,note='',mark='',cl=''):
 return el('pill','pill','<div class="parts">'+(f'<span class="mark">{mark}</span>'if mark else'')+f'<span class="name">{name}</span>'+(f'<span class="note">{note}</span>'if note else'')+'</div>',cl=cl)
def headline(s,note='',kick='',cl=''):return el('headline','headline',(f'<p class="kick">{kick}</p>'if kick else'')+f'<h2>{s}</h2>'+(f'<p class="note">{note}</p>'if note else''),cl=cl)
def prose(s,cl=''):return el('prose','prose',''.join(f'<p>{p}</p>'for p in s.split('\n')),cl=cl)
def metric(fig,name,note=''):return el('metric','stat',f'<div class="parts"><p class="fig">{fig}</p><p class="name">{name}</p><p class="note">{note}</p></div>')
def donut(v,fig,name=''):return el('chart-donut','donut',f'<p class="fig">{fig}</p><p class="name">{name}</p>',f'style="--v:{v}"')
def donuts(items):return el('chart-donut','donuts',''.join(donut(*i)for i in items))
def steps(items,col=False):return el('steps','steps',''.join(f'<div class="step"><span class="mark">{j+1:02}</span><p class="name">{n}</p><p class="note">{t}</p></div>'for j,(n,t)in enumerate(items)),cl='col'if col else'')
def bars(vals,labels=None,cl=''):
 labels=labels or [f'205{j}년'for j in range(len(vals))]
 return el('chart-bar','bars',''.join(f'<div class="bar {"on"if j==len(vals)-1 else""}" style="--v:{v}"><b>{v}</b><span>{labels[j]}</span></div>'for j,v in enumerate(vals)),f'style="--max:{max(vals)}"',cl)
def lines(vals,labels=None):
 labels=labels or [f'205{j}년'for j in range(len(vals))]
 return el('chart-line','lines',''.join(f'<div class="pt" style="--v:{v}"><b>{v}</b><span>{labels[j]}</span></div>'for j,v in enumerate(vals)),f'style="--max:{max(vals)}"')
def lst(items,cl=''):return el('list','list',''.join(f'<div class="item"><p class="name">{n}</p><p class="note">{t}</p></div>'for n,t in items),cl=cl)
def callout(s):return el('callout','callout',f'<p>{s}</p>')
def frame(n):return el('image-frame','frame',f'<div class="seat" data-ph="{n}"></div>')
def arch(layers):return el('architecture','arch',''.join(f'<div class="layer"><p class="name">{n}</p>'+''.join(f'<span class="chip">{x}</span>'for x in chips)+'</div>'for n,chips in layers))
def venn(items,core=''):return el('venn','venn',''.join(f'<div class="set {"on"if j==1 else""}"><p class="name">{t}</p></div>'for j,t in enumerate(items))+(f'<div class="core">{core}</div>'if core else''))
heads={3:('INFORMATION','[제품/서비스명]은 [고객]의 [가장 큰 문제]를 <b>해결하는</b><br>혁신적인 솔루션입니다.','회사소개'),4:('VISION & MISSION','여기에 회사가 꿈꾸는 궁극적인 <b>미래상을</b><br>한 문장으로 제시하세요.','비전과 미션'),5:('PROBLEM','여기에 해결하려는 <b>문제의 핵심을</b><br>간결하게 정의하세요.','시장의 문제점'),6:('SOLUTION','여기에 문제에 대한 <b>명쾌한 해결책을</b> 제시하세요.','우리의 해결책'),7:('MARKET SIZE & OPPORTUNITY','','시장 규모 및 기회'),8:('MARKET VOLUME','[시장 규모] 시장에서 <b>우리의 독점적 기회</b>를 보여주세요.','시장의 크기'),9:('PRODUCT/SERVICE','여기에 <b>우리 기술의 핵심을</b> 보여주세요.','제품 및 서비스'),10:('BUSINESS MODEL','여기에 회사의 <b>수익 창출 모델</b>을 보여주세요.','비즈니스 모델'),11:('BUSINESS MODEL','어떻게 <b>가치를 만들고 전달하는지</b> 보여주세요.','비즈니스 모델'),12:('REVENUE MODEL','<b>수익 모델의 핵심</b>을 한줄로 설명해주세요.','수익 모델'),13:('TRACTION & KEY METRICS','여기에 <b>성장을 증명하는</b> 핵심 지표들을 넣어보세요.','성장지표'),14:('TRACTION','우리의 <b>성과가 말해주는 것</b>을 수치로 보여주세요.','성과'),15:('COMPETITIVE LANDSCAPE','','경쟁 환경 분석'),16:('COMPETITIVE LANDSCAPE','우리의 <b>시장에서 우리의 독보적 위치</b>를 보여주세요.','경쟁 환경 및 우리의 독보적 위치'),17:('GO-TO-MARKET & GROWTH STRATEGY','여기에 <b>성장전략을</b> 구체적으로 제시하세요.','성장 전략'),18:('TECHNOLOGY & IP','독자적인 <b>기술 아키텍처와 독점 데이터</b> 등을 적어주세요.','보유 기술 및 IP'),19:('THE TEAM','비전을 실현할 <b>최고의 팀을</b> 소개하세요.','팀 소개'),20:('FUNDRAISING & FINANCIAL PLAN','NEXT-LEVEL을 위한 <b>성장 동력을</b> 어필하세요.','투자 유치 및 재무 계획'),21:('FUNDRAISING & FINANCIAL PLAN','투자금이 <b>어떻게 쓰일지</b> 보여주세요.','투자 유치 및 재무 계획')}
body={}
body[1]='<section class="slide cover"><div class="top"><span class="deck">20XX IR PRESENTATION</span><span class="sec">MIRICOMPANY.CO.KR</span></div><div class="page"><div class="lockup at-left"><p class="kicker">포인트가 있는 모노톤의 심플한</p><h1 class="title">투자유치<br><b>발표용 IR덱</b></h1></div><div class="seat back" data-ph="1"></div><p class="meta">MIRI Company</p></div></section>'
items=['연혁과 성과','미션과 비전','문제','솔루션','시장상황','서비스(제품) 소개','차별성/경쟁력','경쟁사','시장 진입(확장) 전략','팀 소개','투자 유치 및 재무 계획']
body[2]=place(headline('TABLE OF<br><b>CONTENTS</b>','IR DECK 목차 안내',cl='big'),1,1,5,6)+place(el('agenda','agenda',''.join(f'<div class="entry"><span class="mark">{j+1:02}</span><p class="name">{t}</p></div>'for j,t in enumerate(items))),6,1,7,6)
body[3]=place(prose('우리는 [우리가 타겟하는 명확한 고객]이 겪고 있는 [가장 큰 문제점]을 해결하기 위해, [우리의 솔루션을 한 문장으로 정의]인 [제품/서비스명]을 개발하고 운영합니다. 우리의 비즈니스는 [창업 계기]를 기반으로 시작되었으며, [핵심 제품/서비스] MVP 출시를 통해 시장의 니즈를 검증했습니다. 이러한 과정을 통해 우리는 [가장 큰 문제]를 해결하는 가장 효율적인 방법을 찾아냈고, 이는 현재의 [제품/서비스명]으로 구체화되었습니다. 우리의 목표는 [산업]의 새로운 표준이 되는 것입니다.'),1,1,5,6)+stack([pill('MISSION','우리의 존재 이유를 한 문장으로 정의합니다. 우리의 사명은 [타겟 고객]의 [문제]를 해결하는 것입니다.'),pill('VISION','우리가 그리는 미래를 서술합니다. 우리는 [산업 분야]의 [선두 주자]가 되는 것을 목표로 합니다.',cl='line')],7,1,6,6)
body[4]=place(venn(['비전을 명확하게 표현해 보세요.','회사의 미션과 장기적인 비전을 이 슬라이드에 담으세요. 큰 그림을 보여주며 투자자의 공감을 이끌어내는 페이지입니다.','미션을 명확하게 표현해 보세요.']),1,1,12,6)
body[5]=group([card('비효율성','고객이 어떤 불편함을 느끼고 시간/비용적으로 얼마나 손해를 보고 있는지 구체적인 수치로 설명하세요.','PAIN POINT 01',icon='settings'),card('높은 비용','기존의 방식이나 해결책이 왜 비싸고 접근하기 어려운지, 그로 인해 어떤 기회비용이 발생하는지 설명하세요.','PAIN POINT 02',icon='shopping-cart',cl='line'),card('정보 부족','고객이 올바른 결정을 내리는 데 필요한 정보가 왜 부족하거나 비대칭적인지, 어떤 부정적 결과를 낳는지 보여주세요.','PAIN POINT 03',icon='pencil-line')])
body[6]=''
for j in range(4):
 body[6]+=place(pill('핵심 기능명',mark='SOLUTION 04',cl='on'),1+j*3,1,3,2)+place(card('','이 기능을 통해 고객이 얻게 될 핵심적인 이점을 작성하세요. 앞서 제시한 문제를 해결하기 위해, 우리의 솔루션을 소개합니다. 솔루션의 핵심 기능과 차별점을 간결하고 직관적으로 설명하세요.'if j%2==0 else'앞서 제시한 문제를 해결하기 위해, 우리의 솔루션을 소개합니다. 솔루션의 핵심 기능과 차별점을 간결하고 직관적으로 설명하세요.'),1+j*3,3,3,4)
body[7]=place(el('concentric','orbit','<div class="ring"><p class="name">TAM</p><p class="fig">전체 시장</p></div><div class="ring"><p class="name">SAM</p><p class="fig">유효 시장</p></div><div class="ring"><p class="name">SOM</p><p class="fig">초기 목표</p></div>'),1,1,5,6)+place(headline('여기에 공략할 시장의<br><b>크기와 성장 가능성을</b><br>숫자로 보여주세요.'),7,1,6,3)+stack([metric('420억원','전체 시장','회사가 속한 가장 큰 시장의 규모를 제시하세요.'),metric('120억원','유효 시장','회사의 제품과 서비스가 공략 가능한 시장의 규모를 보여주세요.'),metric('80억원','초기 목표 시장','향후 1~3년 내에 현실적으로 점유할 수 있는 시장을 정의하세요.')],7,4,6,3)
body[8]=place(donuts([(20,'경쟁사 A','KEYWORD'),(60,'기타','KEYWORD'),(20,'경쟁사 B','KEYWORD')]),2,1,10,4)+group([card('경쟁 구도','현재 시장은 [경쟁사]가 점유하고 있지만, 그들이 해결하지 못하는 [틈새시장]이 존재합니다.','POINT 1'),card('시장 기회','우리는 [시장 규모]조 원의 이 틈새시장을 공략하여 독점적인 지위를 확보할 것입니다.','POINT 2')],1,5,12,2)
body[9]=stack([card('KEYWORD','이곳에 사용된 요소를 가지고 우리 기술의 시스템을 명확히 설명해 보세요.','',icon='trash-2'),card('','이곳에 사용된 요소를 가지고 우리 기술의 시스템을 명확히 설명해 보세요.')],1,1,3,4)+place(arch([('데이터 엔진',['KEYWORD','KEYWORD','KEYWORD']),('우리 기술을 설명하는 핵심 문장',['처리','연결'])]),5,1,4,4)+stack([card('','이곳에 사용된 요소를 가지고 우리 기술의 시스템을 명확히 설명해 보세요.'),card('KEYWORD','명확한 데이터 흐름을 연결합니다.','',icon='network')],10,1,3,4)+place(callout('제품의 기술 구조를 다이어그램으로 시각화하여 데이터 흐름, 핵심 엔진, 서비스 모듈 등을 보여주세요.<br>기술에 대한 깊은 이해도를 어필할 수 있습니다.'),1,5,12,2)
body[10]=group([card('구독료 (SAAS)','어떤 고객이 어떤 가치에 대해 월/연 단위로 비용을 지불하는지 설명합니다. BASIC: 월 10만 원 / PRO: 월 50만 원','수익모델 01'),card('중개 수수료','플랫폼 내에서 발생하는 거래의 어떤 부분에서 몇 %의 수수료를 받는지 설명합니다. 거래액의 5~10%','수익모델 02'),card('기타','데이터 판매, 부가 서비스 등 추가적인 수익원이 있다면 기재합니다. 리포트 건당/API 호출당 과금','수익모델 03'),card('강조할 수익 모델','여기에 가장 강조하고 싶은 우리 회사의 수익 모델에 대해 기재합니다. 상세 내용을 입력해보세요.','수익모델 04',cl='line')])
body[11]=place(steps([('고객 유입','채널'),('서비스 제공 및','핵심 가치 창출 활동'),('고객이 얻는','혜택 및 성공'),('수익 발생 및','고객 유지'),('수익을 통한','서비스 고도화 및 재투자')]),1,1,12,3)+group([card('누구에게','우리의 명확한 타겟 고객은 누구이며 고객의 니즈는 무엇인지 다시 한번 정의합니다.',icon='users-round'),card('어떤 가치를','우리가 고객에게 제공하는 3가지 핵심 가치(예: 비용 절감, 시간 절약, 매출 증대)를 명확히 제시합니다.',icon='gem'),card('어떻게','그 가치를 어떤 핵심 채널을 통해 전달하고, 어떤 방식으로 강화해 나갈 것인지 설명합니다.',icon='lightbulb')],1,4,12,3)
body[12]=stack([card('가격 전략','우리의 가격은 단순히 원가나 경쟁사를 따르는 것이 아니라, 고객이 우리 서비스를 통해 얻는 가치에 기반하여 책정되었음을 설명합니다.','POINT 1'),card('수익 구조','현재 또는 목표 시점의 매출 비중을 보여줍니다. 안정적인 반복 매출과 부가적인 수익원이 어떻게 조화를 이루는지 설명하세요.','POINT 2')],1,1,6,6)+place(headline('수익원 구조',cl='center'),7,1,6,1)+place(donuts([(60,'60%','수익원 1'),(20,'20%','수익원 2'),(20,'20%','수익원 3')]),7,2,6,3)+group([prose('안정적인 현금 흐름을 창출하는 우리 회사의 핵심 수익원'),prose('사용량이 늘어남에 따라 매출도 함께 성장하는 구조의 수익원'),prose('전문가 컨설팅, 맞춤형 구축 등 고부가가치 서비스를 제공')],7,5,6,2)
body[13]=stack([metric('342만','사용자 지표','누적 가입자, 월간 활성 사용자(MAU), 재방문율 등 인기를 증명하는 지표를 제시하세요.'),metric('200억 원','재무 지표','매출, 거래액, 월간 반복 매출(MRR) 등 회사의 재무적 성장을 증명하는 지표를 제시하세요.'),metric('95%','고객 만족도','고객 재구매율, 만족도 평점, 주요 고객 후기 등을 통해 서비스의 품질을 구체적인 수치와 함께 증명하세요.')],1,1,6,6)+place(headline('누적 서비스 가입자','기간 : 2050년–2055년'),7,1,6,1)+place(bars([24,48,72,48,108,120]),7,2,6,5)
body[14]=place(headline('시장성'),1,1,4,1)+place(headline('수익성'),5,1,4,1)+place(headline('경쟁 우위'),9,1,4,1)+place(el('chart-area','areas','<div class="series tone-1"><p class="name">시장성</p>'+''.join(f'<div class="pt" style="--v:{v}"></div>'for v in[15,5,20,45,65,75])+'</div><div class="axis">'+''.join(f'<span>205{j}년</span>'for j in range(6))+'</div>','style="--max:75"'),1,2,4,3)+place(lines([15,5,10,35,60,75],['06월','07월','08월','09월','10월','11월']),5,2,4,3)+place(bars([80,75,6,8,5,11]),9,2,4,3)+place(prose('월간 활성 사용자(MAU) 성장은 [수치%]에 달하며, 이는 우리 서비스에 대한 시장의 높은 수요를 보여줍니다.'),1,5,4,2)+place(prose('우리는 [기간] 내에 손익분기점(BEP)에 도달할 것으로 예상됩니다. 이 내용은 매출과 영업이익을 함께 보여주는 선 그래프로 표현하는 것이 좋습니다.'),5,5,4,2)+place(prose('우리의 고객 유지율(RETENTION)은 [경쟁사] 대비 월등히 높아, 서비스의 가치를 증명합니다.'),9,5,4,2)
body[15]=place(el('positioning','posmap','<div class="axis-x"><span>높은 응답 빈도</span><span>낮은 응답 빈도</span></div><div class="axis-y"><span>저비용</span><span>고비용</span></div>'+''.join(f'<div class="mark {cl}" style="--x:{x};--y:{y}"><p class="name">{n}</p></div>'for n,x,y,cl in[('타이틀 A',27,72,''),('타이틀 B',28,22,''),('타이틀 C',67,28,''),('MIRI COMPANY',77,87,'on')])),1,1,5,6)+place(headline('여기에 우리 회사가 가진<br><b>독보적인 경쟁 우위를</b><br>명확히 설명하세요.'),7,1,6,3)+place(lst([('타사 응답 서비스 대비 저렴한 비용과 높은 응답 빈도',''),('이곳에 경쟁사가 따라하기 어려운 요소를 적어주세요',''),('우리만의 독점적인 기술이나 특허 등을 적어주세요','')],'divided check'),7,4,6,3)
body[16]=place(lst([('기술적 우위','우리는 [핵심 기술]을 통해 경쟁사가 따라올 수 없는 성능을 제공합니다.'),('고객 중심 솔루션','고객의 [고통스러운 문제]를 정확하게 해결하는 맞춤형 솔루션을 제공합니다.'),('비용 효율성','우리의 [비즈니스 모델]은 경쟁사 대비 [비용]을 획기적으로 절감합니다.')],'divided'),1,1,6,6)+place(venn(['경쟁사 A','경쟁사 B','경쟁사 C'],'우리의 핵심기술'),7,1,6,6)
body[17]=''
for j in range(5):body[17]+=place(frame(j+1),1+j*2,1,2,2)+place(card('초기 시장 진입 (~1년)'if j==0 else'본격적인 성장 및 확장 (~3년)','목표 달성을 위한 구체적인 액션 플랜을 제시하세요. (예: 특정 커뮤니티 타겟 마케팅 등)'if j%2==0 else'이 단계의 구체적인 목표를 작성하세요. (예: 국내 시장 점유율 1위 달성)'),1+j*2,3,2,4)
body[18]=place(prose('<b>우리의 기술과 독점 데이터</b>','lead'),1,1,5,2)+place(prose('회사의 기술적 깊이와 방어력을 증명하여, 투자자 단기적인 성과를 넘어 장기적으로 지속 가능한 가치를 가질 것임을 설득하세요. 우리의 기술 아키텍처는 비전문가인 투자자도 쉽게 이해할 수 있도록 설명주세요. 회사가 보유한 가장 중요한 기술 자산인 특허와 독점 데이터베이스는 우리의 기술력을 증명합니다.\n이러한 기술, IP, 그리고 데이터는 경쟁사와의 격차를 만들고 후발주자의 진입을 어렵게 만드는 강력한 진입 장벽이 됩니다.'),1,2,5,5)+place(arch([('시스템 콘트롤러',[]),('클라우드 서버 클러스터',['게이트웨이','기기','기기','기기']),('KEYWORD',['처리','연결','분석']),('시각화 시스템',[])]),7,1,6,6)
people=[]
for j,(n,role)in enumerate([('한미리','ENGINEER'),('최미리','ENGINEER'),('박미리','CEO'),('우미리','MARKETER'),('현미리','MARKETER')]):people.append(el('person','person',f'<div class="seat avatar" data-ph="{j+1}"></div><p class="name">{n}</p><p class="note">{role}</p>'+lst([('핵심 경력을 적어보세요.',''),('전문성을 보여주세요.','')],'')))
body[19]=place(el('person','people',''.join(people)),1,1,12,6)
body[20]=stack([pill('200억 원','투자 유치 목표',mark='THE ASK',cl='on'),pill('우리 기업이 왜 투자 가치가 있는지, 투자자에게 강조하고 싶은 한 문장을 적어주세요.',mark='MESSAGE',cl='line')],1,1,4,6)+place(card('자금 사용 계획','R&D 및 기술 고도화: 40% (80억 원)<br>마케팅 및 고객 확보: 20% (40억 원)<br>핵심 인재 영입: 30% (60억 원)<br>운영 자금 및 기타: 10% (20억 원)','단위 : 억 원'),5,1,4,6)+place(headline('자사 예상 영업이익률','기간 : 2050년–2055년'),9,1,4,2)+place(bars([5,10,15,10,25]),9,3,4,4)
body[21]=stack([metric('10%','운영 자금 및 기타: 20억 원','운영 자금 및 기타 항목은 어떤 운영 효율화나 안정적 서비스 제공에 사용될지, 구체적인 활용 방안을 예시로 작성해보세요.'),metric('30%','핵심 인재 영입: 60억 원','핵심 인재 영입을 위해 어떤 직무나 역량의 인재를 확보하고, 이를 통해 어떤 가치를 창출할지 예시를 들어 설명해보세요.')],1,1,4,6)+place(donut(40,'40%','R&D 및 기술 고도화'),5,1,4,6)+stack([metric('40%','R&D 및 기술 고도화: 80억 원','R&D 및 기술 고도화를 위해 어떤 방식으로 투자금액을 활용할지, 구체적인 예시를 들어 설명해보세요.'),metric('20%','마케팅 및 고객 확보: 40억 원','마케팅 및 고객 확보를 위해 투자금액을 어떤 채널과 전략에 사용할지, 구체적인 사례를 들어 작성해보세요.')],9,1,4,6)
# Original semantic information preserved inside the contracted table and equal-width group wrappers.
body[7]=body[7].split('<div class="stack"')[0]+place(el('table','tablebox','<table class="table"><thead></thead><tbody><tr><td><b>420억원</b><br>전체 시장</td><td>회사가 속한 가장 큰 시장의 규모를 제시하세요. 예: 글로벌 인테리어 시장</td></tr><tr><td><b>120억원</b><br>유효 시장</td><td>회사의 제품과 서비스가 공략 가능한 시장의 규모를 보여주세요. 예: 국내 온라인 인테리어 플랫폼 시장</td></tr><tr><td><b>80억원</b><br>초기 목표 시장</td><td>향후 1~3년 내에 현실적으로 점유할 수 있는 시장을 정의하세요. 예: 수도권 아파트 전문 디자인 서비스 시장</td></tr></tbody></table>'),7,4,6,3)
growth=[]
for j in range(5):
 t='목표 달성을 위한 구체적인 액션 플랜을 제시하세요. (예: 특정 커뮤니티 타겟 마케팅 등)' if j%2==0 else '이 단계의 구체적인 목표를 작성하세요. (예: 국내 시장 점유율 1위 달성)'
 n='초기 시장 진입 (~1년)' if j==0 else '본격적인 성장 및 확장 (~3년)'
 growth.append('<div class="stack">'+frame(j+1)+card('',f'<b>{n}</b><br>{t}')+'</div>')
body[17]=group(growth)
def paired(comp,ours):
 nodes=[]
 for j,(cv,ov)in enumerate(zip(comp,ours)):
  nodes.append(f'<div class="bar tone-5" style="--v:{cv}"><b></b><span>205{j}년</span></div>')
  nodes.append(f'<div class="bar tone-1 {"on" if j==len(ours)-1 else ""}" style="--v:{ov}"><b></b><span></span></div>')
 return el('chart-bar','bars',''.join(nodes),f'style="--max:{max(comp+ours)}"')
body[13]=body[13].replace(place(bars([24,48,72,48,108,120]),7,2,6,5),place(paired([12,36,24,18,36,60],[24,48,72,48,108,120]),7,2,6,5))
body[14]=body[14].replace(place(bars([80,75,6,8,5,11]),9,2,4,3),place(paired([100,86,60,86,33,27],[80,75,6,8,5,11]),9,2,4,3))
body[20]=body[20].replace(place(bars([5,10,15,10,25]),9,3,4,4),place(paired([2.5,7.5,5,3.7,7.5],[5,10,15,10,25]),9,3,4,4))

# New fidelity composition is defined below. Original component sources are preserved.
from lxml import html as LH
from lxml import etree as ET
def at(i,x,y):
 doc=LH.parse(str(P/'replica'/f'slide_{i:02}.html'))
 for n in doc.xpath('//main/div'):
  st=n.get('style','')
  if f'left:{x}px;' in st and f'top:{y}px;' in st:
   n=LH.fromstring(ET.tostring(n))
   for q in n.iter():
    q.attrib.pop('style',None)
    if q.get('class')=='hl':q.tag='b'
    q.attrib.pop('class',None)
   return (n.text or '')+''.join(ET.tostring(q,encoding='unicode',method='html')for q in n)
 raise ValueError((i,x,y))
def ico(n):return f'<span class="icon" data-icon="{n}"></span>'
def tag(s):return '<span class="tag" data-el="seedmark-tag">'+s+'</span>'
def cparts(s,cl=''):return el('card','card','<div class="parts">'+s+'</div>',cl=cl)
def node(s,c,r,w=1,h=1,cl=''):return f'<div class="node {cl}" style="grid-column:{c}/span {w};grid-row:{r}/span {h}">{s}</div>'
def flow(s,cols=10):return el('flowchart','flowchart',s,f'style="--cols:{cols}"')
def listcopy(items,check=False):return el('list','list',''.join('<div class="item"><p class="name">'+v+'</p></div>'for v in items),cl='check'if check else'')
def iconlabel(n,label='KEYWORD'):
 return pill(label,mark=ico(n),cl='quiet')
def noteCard(s):return cparts('<p class="note">'+s+'</p>')
def cardsource(name,note,kick='',extras='',cl=''):
 return cparts((f'<p class="kick">{kick}</p>'if kick else'')+f'<h3 class="name">{name}</h3><p class="note">{note}</p>'+extras,cl=cl)
# Original text is pulled from the independently recreated slide, without geometry or CSS.
body[2]=place(headline('TABLE OF<br><b>CONTENTS</b>','IR DECK 목차 안내',cl='big'),1,1,5,6)+place(el('agenda','agenda',''.join(f'<div class="entry"><span class="mark">{j+1:02}</span><p class="name">{t}</p></div>'for j,t in enumerate(items))),6,2,7,5)
body[3]=place(prose(at(3,84,329)+'\n'+tag('KEYWORD')+'　KEYWORD'),1,1,5,6)+stack([pill('MISSION',at(3,829,351),ico('gem'),cl='line'),pill('VISION',at(3,829,519),ico('lightbulb'),cl='line')],7,1,6,6)
body[5]=group([card(n,at(5,126+j*378,510),f'PAIN POINT 0{j+1}',icon=ic,cl='line'if j==1 else'')for j,(n,ic)in enumerate([('비효율성','settings'),('높은 비용','shopping-cart'),('정보 부족','pencil-line')])])
body[4]=place(venn([ico('lightbulb')+'<br>비전을 명확하게<br>표현해 보세요.<br>'+tag('VISION'),ico('puzzle')+'<br>회사의 미션과 장기적인 비전을<br>이 슬라이드에 담으세요. 큰 그림을 보여주며<br>투자자의 공감을 이끌어내는 페이지입니다.<br>'+tag('OUR<br>COMPANY'),ico('diamond')+'<br>미션을 명확하게<br>표현해 보세요.<br>'+tag('MISSION')]),1,1,12,6)
body[6]=group([stack([pill('핵심 기능명',mark='SOLUTION 04',cl='on'),noteCard(at(6,114+j*287,416))])for j in range(4)])
body[7]=place(el('concentric','orbit',''.join(f'<div class="ring"><p class="name">{n}</p><p class="fig">{t}</p></div>'for n,t in [('TAM','(전체 시장)'),('SAM','(유효 시장)'),('SOM','(초기 목표 시장)')])),1,1,6,6)
body[7]+=stack([headline(at(7,639,133)),stack([metric(at(7,638,365+j*96),at(7,638,409+j*96),at(7,798,371+j*96))for j in range(3)])],7,1,6,6)
body[8]=place(el('chart-donut','donuts',''.join(donut(*v)for v in [(20,'경쟁사 A','KEYWORD'),(60,'기타','KEYWORD'),(20,'경쟁사 B','KEYWORD')]),cl='line'),2,1,10,4)+group([cardsource('경쟁 구도',at(8,264,547),'POINT 1'),cardsource('시장 기회',at(8,838,547),'POINT 2')],1,5,12,2)
# 09: a composed data flow, rather than replacement architecture rows.
lefttop=cparts('<div class="group">'+''.join(iconlabel(k)for k in ['trash-2','messages-square','settings'])+'</div>')
rightbottom=cparts('<div class="group">'+''.join(iconlabel(k)for k in ['puzzle','globe','share-2'])+'</div>')
engine=cparts('<div class="group">'+''.join(pill('KEYWORD',mark=ico('database'),cl='line')for _ in range(3))+'</div>',cl='quiet')
diagram=node(lefttop,1,1,1,3,'to-r')+node(noteCard(at(9,104,430)),1,4,1,3)+node(engine,2,1,1,4,'to-r to-d')+node(pill(at(9,424,456),cl='on'),2,5,1,2,'to-r')+node(noteCard(at(9,914,289)),3,1,1,3)+node(rightbottom,3,4,1,3)
body[9]=stack([flow(diagram,3),callout(at(9,84,559))])
body[10]=group([cardsource(at(10,116+j*282,338),at(10,116+j*282,429),f'수익모델 0{j+1}',listcopy(at(10,116+j*282,(554 if j==0 else 583)).split('<br>'),True),cl='line'if j==3 else'')for j in range(4)])
# 11: preserve the five icon steps and complete cyclic return path.
st=[]
for j,(n,t)in enumerate([('users','고객 유입<br>채널'),('diamond','서비스 제공 및<br>핵심 가치 창출 활동'),('gift','고객이 얻는<br>혜택 및 성공'),('target','수익 발생 및<br>고객 유지'),('lightbulb','수익을 통한<br>서비스 고도화 및 재투자')]):
 st.append(f'<div class="step"><span class="mark">{ico(n)}</span><p class="name">STEP 0{j+1}</p><p class="note">{t}</p></div>')
body[11]=place(el('steps','steps',''.join(st)),1,1,12,3)+group([cparts('<span class="mark">'+ico(ic)+'</span><h3 class="name">'+n+'</h3><p class="note">'+at(11,x,y)+'</p>')for ic,n,x,y in [('users','누구에게',179,538),('diamond','어떤 가치를',562,538),('lightbulb','어떻게',945,538)]],1,4,12,3)
# 12–15: complete copy, original chart annotations and quiet graph surfaces.
body[12]=stack([cardsource('가격 전략',at(12,262,320),'POINT 1'),cardsource('수익 구조',at(12,262,512),'POINT 2')],1,1,6,6)+place(headline('수익원 구조',cl='center'),7,1,6,1)+place(donuts([(60,'60%','수익원 1'),(20,'20%','수익원 2'),(20,'20%','수익원 3')]),7,2,6,3)+group([prose(at(12,680+j*182,558))for j in range(3)],7,5,6,2)
body[13]=stack([metric(at(13,84,263+j*140),at(13,84,305+j*140),at(13,245,268+j*140))for j in range(3)],1,1,6,6)
body[13]+=place(cparts('<h3 class="name">누적 서비스 가입자</h3><p class="kick">기간 : 2050년–2055년</p>'+el('legend','legend','<span class="key tone-5">타사</span><span class="key tone-1">MIRI COMPANY</span>')+paired([1,3,2,1.5,3,5],[2,4,6,4,9,10])+tag('120만 명'),cl='quiet'),7,1,6,6)
area=el('chart-area','areas','<div class="series tone-1"><p class="name"></p>'+''.join(f'<div class="pt" style="--v:{v}"></div>'for v in[15,5,20,45,65,75])+'</div><div class="axis">'+''.join(f'<span>205{j}년</span>'for j in range(6))+'</div>','style="--max:75"')
line=el('chart-line','lines',''.join(f'<div class="pt" style="--v:{v}"><b></b><span>{m}</span></div>'for v,m in zip([15,5,10,35,60,75],['06월','07월','08월','09월','10월','11월'])),'style="--max:75"')
body[14]=group([pure(stack([headline(n),chart,prose(at(14,x,558))]))for n,chart,x in [('시장성',area,84),('수익성',line,473),('경쟁 우위',paired([10,8.6,6,8.6,3.3,2.7],[8,7.5,.6,.8,.5,1.1]),864)]])
body[14]+=place(el('legend','legend','<span class="key tone-5">타사</span><span class="key tone-1">MIRI COMPANY</span>'),9,2,4,2)
body[14]+=place(el('tag','tag','<span>BEP</span>',cl='line'),7,2,1,3)
pos=el('positioning','posmap','<div class="axis-x"><span>높은 응답 빈도</span><span>낮은 응답 빈도</span></div><div class="axis-y"><span>저비용</span><span>고비용</span></div>'+''.join(f'<div class="mark {cl}" style="--x:{x};--y:{y}"><p class="name">{n}</p></div>'for n,x,y,cl in[('타이틀 A',27,72,''),('타이틀 B',28,22,''),('타이틀 C',67,28,''),('MIRI<br>COMPANY',77,87,'on')]))
points=el('list','list',''.join('<div class="item"><span class="mark">'+ico(ic)+'</span><p class="name">'+at(15,708,380+j*96)+'</p></div>'for j,ic in enumerate(['check-check','crosshair','gem'])),cl='divided')
body[15]=place(pos,1,1,6,6)+stack([headline('여기에 우리 회사가 가진<br><b>독보적인 경쟁 우위를</b><br>명확히 설명하세요.'),points],7,1,6,6)
# 16: original two-column evidence and three-set overlap.
body[16]=stack([cparts(f'<p class="kick">POINT {j+1}</p><h3 class="name">{at(16,84,292+j*134)}</h3><p class="note">{at(16,295,273+j*134)}</p>',cl='quiet')for j in range(3)],1,1,6,6)
body[16]+=place(venn(['경쟁사 A','경쟁사 B','경쟁사 C'],'우리의<br>핵심기술'),7,1,6,6)
body[16]+=place(tag('기존의 서비스'),7,2,2,1)+place(tag('솔루션'),11,2,2,1)+place(tag('키워드 입력'),9,6,2,1)
# 17: a five-stop track with grouped period bands and all phase labels.
stops=[]
for j in range(5):
 period='초기 시장 진입 (~1년)'if j==0 else'본격적인 성장 및 확장 (~3년)'if j in [1,3] else''
 stops.append('<div class="stop'+(' on'if j==3 else'')+'"><p class="kick">'+period+'</p><div class="name">'+frame(j+1)+'</div><p class="note">'+at(17,107+j*223,485)+'</p></div>')
body[17]=place(el('timeline','track',''.join(stops)),1,1,12,6)+place(tag('PHASE 1'),1,6,3,1)+place(tag('PHASE 2'),5,6,3,1)+place(tag('PHASE 3'),10,6,3,1)
# 18: positioned system nodes, fan-out, cloud and output paths.
body[18]=place(prose('<b>우리의 기술과 독점 데이터</b>','lead'),1,1,5,2)+place(prose(at(18,84,365).replace('<br>',' ').replace('설명주','설명해주'),'quiet'),1,2,5,4)+group([tag('KEYWORD'),tag('KEYWORD')],1,6,3,1)
process=cparts('<div class="group">'+''.join(iconlabel(k)for k in ['trash-2','messages-square','settings'])+'</div>')
devices='<div class="stack">'+''.join(pill('기기',cl='line')for _ in range(3))+'</div>'
diagram=node('시스템 콘트롤러',1,1,5,1,'to-d to-r')+node('클라우드 서버 클러스터',1,2,5,1,'to-d to-l')+node('게이트<br>웨이',9,1,2,2,'to-r')+node(devices,11,1,2,3)+node(process,3,3,5,1,'to-r')+node('시각화 시스템',8,4,5,1,'end')
body[18]+=place(flow(diagram,12),6,1,7,6)
# 19: original unequal CEO portrait and each person's own career text.
people=[]
for j,(n,role)in enumerate([('한미리','ENGINEER'),('최미리','ENGINEER'),('박미리','CEO'),('우미리','MARKETER'),('현미리','MARKETER')]):
 career=at(19,89+j*231,587).replace('•  ','').split('<br>')
 people.append(el('person','person',f'<span class="seat avatar" data-ph="{j+1}"></span><b class="name">{n}</b><p class="note">{role}</p>'+listcopy(career)))
body[19]=place(el('person','people',''.join(people)),1,1,12,6)

# 20: retain the labelled ask, segmented allocation bar, list, chart legend and annotation.
ask=pill('200억 원','투자 유치 목표','THE ASK',cl='on')
message=pill('우리 기업이 왜 투자 가치가 있는지,<br>투자자에게 강조하고 싶은 한 문장<br>을 적어주세요.',mark='MESSAGE',cl='line')
body[20]=stack([ask,message],1,1,4,6)
segments=''.join(f'<div class="seg tone-{tone}" style="--v:{v}"><b>{v}%</b></div>'for v,tone in [(40,1),(20,5),(30,2),(10,5)])
allocation=el('chart-stack','stacks pct h','<div class="sbar"><span></span>'+segments+'</div>','style="--max:100"')
funds=['R&D 및 기술 고도화: 40% (80억 원)','마케팅 및 고객 확보: 20% (40억 원)','핵심 인재 영입: 30% (60억 원)','운영 자금 및 기타: 10% (20억 원)']
body[20]+=place(cparts('<h3 class="name">자금 사용 계획</h3><p class="kick">단위 : 억 원</p>'+allocation+listcopy(funds)),5,1,4,6)
legend=el('legend','legend','<span class="key tone-5">타사</span><span class="key tone-1">MIRI COMPANY</span>')
body[20]+=place(cparts('<h3 class="name">자사 예상 영업이익률</h3><p class="kick">기간 : 2050년–2055년</p>'+legend+paired([1,3,2,1.5,3],[2,4,6,4,9])+tag('25%')),9,1,4,6)
# 21: independently valid one-share donut roots occupy the same slot; data controls start/hole.
def detailmetric(fig,name,note):
 return el('metric','stat','<div class="parts"><p class="fig">'+fig+'</p><p class="name">'+name+'</p><div class="note">'+prose(note)+'</div></div>')
left=stack([detailmetric(at(21,84,y),at(21,184,y+16),at(21,84,y+62))for y in [285,495]])
right=stack([detailmetric(at(21,879,y),at(21,979,y+16),at(21,879,y+62))for y in [285,495]])
pie=[]
for v,start,icon,tone in [(40,0,'pencil-line',1),(20,144,'lightbulb',2),(30,216,'target',3),(10,324,'house',5)]:
 pie.append(el('chart-donut','donut',f'<p class="fig">{v}%</p><p class="name">{ico(icon)}</p>',f'style="--v:{v};--seedmark-donut-start:{start}deg;--seedmark-donut-hole:0;--seedmark-donut-layer:1"',cl=f'tone-{tone}'))
def ungrid(s):
 head,tail=s.split('>',1)
 head=re.sub(r' style="grid-column:[^"]*"','',head)
 return head+'>'+tail
body[21]=group([ungrid(left),ungrid(stack(pie)),ungrid(right)],cl='overrides')
defaults={}
for metadata in (C/'elements').glob('*/element.json'):defaults.update(json.loads(metadata.read_text()).get('tokenDefaults',{}))
(P/'assets/source-defaults.css').write_text('.slide{'+''.join(str(k)+':'+str(v)+';'for k,v in defaults.items())+'}')
links+='<link rel="stylesheet" href="../assets/source-defaults.css">'
for i,content in body.items():
 if i!=1:
  if i==2:head='';section='MIRICOMPANY.CO.KR'
  else:
   k,t,section=heads[i];head=f'<header class="head center"><p class="kicker">{k}</p>'+ (f'<h1 class="title">{t}</h1>'if t else'')+'</header>'
  content=f'<section class="slide'+(' overrides'if i==21 else'')+f'"><div class="top"><span class="deck">20XX IR PRESENTATION</span><span class="sec">{section}</span></div><div class="page">{head}<div class="body">{content}</div></div></section>'
 content=content.replace('class="slide', 'class="slide src',1)
 if i==19:content=content.replace('</section>','<div class="foot"><span class="src">*페이지 내 인물 사진은 샘플 이미지입니다.</span></div></section>')
 (R/f'slide_{i:02}.html').write_text(f'<!doctype html><html lang="ko"><meta charset="utf-8"><title>Seedmark reassembled {i:02}</title>{links}<body>{content}<script src="../assets/lucide.min.js"></script><script src="../assets/render-icons.js"></script></body></html>')
print('Reassembled fidelity pages:',len(body))
