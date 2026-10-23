from pathlib import Path
import html,json,re
P=Path(__file__).parent;C=P/'crossrail';O=P/'reassembled';O.mkdir(exist_ok=True);(P/'assets').mkdir(exist_ok=True)
# This file is the source presentation's external style color provider, not collection design CSS.
pal=json.loads(Path('/workspace/work/reference/contract/palette.json').read_text())['light'];v={}
N='#1e385d';stages=['#f7f8fa','#edf0f5','#d4d8e2','#bfc6d6','#969fb7','#65719a','#1e385d','#172c4a','#102139']
for k in pal:
 if k=='--page':v[k]='#ffffff'
 elif k=='--ink':v[k]=N
 elif k.startswith('--n-'):v[k]=['#f1f2f5','#e7e9ee','#d4d6df','#bbc1d0','#969fb7','#747d94','#656565','#3d4658',N][int(k[-1])-1]
 elif re.match(r'--a[1-4]-on$',k):v[k]='#ffffff'
 elif re.match(r'--a[1-4]$',k):v[k]=[N,'#65719a','#969fb7','#d4d8e2'][int(k[-1])-1]
 elif re.match(r'--a[1-4]-[1-9]',k):v[k]=stages[int(k[5])-1]
 elif k=='--good':v[k]='#237044'
 elif k=='--bad':v[k]='#a73236'
 elif k=='--warn':v[k]='#9d6e15'
(P/'assets/source-palette.css').write_text('/* External source style: source-deck colors only. */\n.slide{'+''.join(k+':'+c+';' for k,c in v.items())+'}\n')
def el(folder,root,body,cl='',style=''):
 return f'<div class="{root} {cl}" data-el="crossrail-{folder}"'+(f' style="{style}"' if style else '')+'>'+body+'</div>'
def slot(s,col=1,span=12,row=1,rows=6):
 m=re.search(r'<\w+',s); pos=s.find('>',m.start()); head=s[:pos];rest=s[pos:]
 if ' style="' in head:head=head.replace(' style="',f' style="grid-column:{col} / span {span};grid-row:{row} / span {rows};')
 else:head+=f' style="grid-column:{col} / span {span};grid-row:{row} / span {rows}"'
 return head+rest
def group(children,cl=''):return '<div class="group '+cl+'">'+''.join(children)+'</div>'
def card(name,note='',fig='',kick='',cl='quiet',mark=''):
 return el('card','card','<div class="parts">'+(f'<p class="kick">{kick}</p>' if kick else '')+(f'<span class="mark">{mark}</span>' if mark else '')+(f'<p class="fig">{fig}</p>' if fig else '')+f'<p class="name">{name}</p>'+(f'<p class="note">{note}</p>' if note else '')+'</div>',cl)
def prose(text,cl=''):return el('prose','prose',''.join('<p>'+x+'</p>' for x in text.split('\n\n')),cl)
def head(text,note='',cl=''):return el('headline','headline',f'<h2>{text}</h2>'+(f'<p class="note">{note}</p>' if note else ''),cl)
def pill(name,note='',cl=''):return el('pill','pill','<div class="parts"><p class="name">'+name+'</p>'+(f'<p class="note">{note}</p>' if note else '')+'</div>',cl)
def listing(pairs,cl=''):return el('list','list',''.join('<div class="item"><p class="name">'+a+'</p>'+(f'<p class="note">{b}</p>' if b else '')+'</div>' for a,b in pairs),cl)
def table(rows,headers=None):
 return el('table','tablebox','<table class="table">'+('<thead><tr>'+''.join('<th>'+x+'</th>' for x in headers)+'</tr></thead>' if headers else '')+'<tbody>'+''.join('<tr>'+''.join('<td'+(' class="num"' if i>0 else '')+'>'+str(x)+'</td>' for i,x in enumerate(row))+'</tr>' for row in rows)+'</tbody></table>')
def metric(fig,name,note=''):return el('metric','stat','<div class="parts"><p class="fig">'+fig+'</p><p class="name">'+name+'</p><p class="note">'+note+'</p></div>')
def bars(vals,labels,maxv=100):return el('chart-bar','bars',''.join(f'<div class="bar'+(' on' if i==len(vals)-1 else '')+f'" style="--v:{v}"><b>{v}</b><span>{labels[i]}</span></div>' for i,v in enumerate(vals)),style=f'--max:{maxv}')
def lines(vals,labels,maxv):return el('chart-line','lines',''.join(f'<div class="pt" style="--v:{v}"><b>{v:,}</b><span>{labels[i]}</span></div>' for i,v in enumerate(vals)),style=f'--max:{maxv}')
def donut(v,name,fig=None):return el('chart-donut','donut','<p class="fig">'+(str(v)+'%' if fig is None else fig)+'</p><p class="name">'+name+'</p>',style=f'--v:{v}')
def steps(names,notes,cl='',marks=None):return el('steps','steps',''.join('<div class="step"><span class="mark">'+(str(i+1).zfill(2) if marks is None else marks[i])+'</span><p class="name">'+name+'</p><p class="note">'+notes[i]+'</p></div>' for i,name in enumerate(names)),cl)
def hub(names,core='핵심 가치',icons=None):return el('hub','hub','<div class="core"><b class="name">'+core+'</b></div>'+''.join('<div class="spoke">'+(f'<span class="mark"><span class="icon" data-icon="{icons[i]}"></span></span>' if icons else '')+'<p class="name">'+a+'</p></div>' for i,a in enumerate(names)))
def frame(n=1):return el('image-frame','frame',f'<div class="seat" data-ph="{n}"></div>')
def agenda(names,start=1):return el('agenda','agenda',''.join(f'<div class="entry"><span class="mark">{start+i:02d}</span><p class="name">{a}</p></div>' for i,a in enumerate(names)))
def side(body,cl=''):return '<div class="side '+cl+'">'+body+'</div>'
def roadmap():
 a='<div class="heads">'+''.join('<span>'+str(i)+'분기</span>' for i in range(1,5))+'</div>'
 for i,(start,end,label) in enumerate([(0,2,'일정 관리를 한눈에.'),(0,3,'막대 길이로 흐름을 파악하세요.'),(1.4,3.1,'일정 관리를 한눈에.'),(2,4,'막대 길이로 흐름을 파악하세요.')]):a+=f'<div class="lane"><p class="name">핵심 기능 구현</p><div class="bar'+(' on' if i in [1,3] else '')+f'" style="--from:{int(start)};--to:{int(end)}"><span>{label}</span></div></div>'
 return el('roadmap','roadmap',a,style='--cols:4')
T=[('',''),('',''),('회사 개요','COMPANY OVERVIEW'),('회사 개요 상세','COMPANY OVERVIEW (DETAILS)'),('회사<br>비전','VISION & MISSION'),('비전 구조','VISION FRAMEWORK'),('핵심 가치 체계','CORE VALUES FRAMEWORK'),('전략 방향','STRATEGIC DIRECTION'),('전략 핵심 포인트','KEY STRATEGIC POINTS'),('전략 흐름','STRATEGY FLOW'),('주요 사업','KEY BUSINESS AREAS'),('사업 구조','BUSINESS STRUCTURE'),('사업 프로세스','BUSINESS PROCESS'),('운영 흐름','OPERATIONAL FLOW'),('장비 현황','PRODUCTS & SERVICES'),('장비 스펙','PRODUCT & SERVICE DETAILS'),('KPI 구조','KPI FRAMEWORK'),('회사 강점','COMPANY STRENGTHS'),('협업 및 파트너십','COLLABORATION & PARTNERSHIPS'),('KPI 상세 지표','KPI DETAILS'),('주요 수치 요약','KEY FIGURES'),('성과 추이','PERFORMANCE TREND'),('성과 비교','PERFORMANCE COMPARISON'),('매출 비중','REVENUE DISTRIBUTION'),('',''),('프로젝트 일정','PROJECT TIMELINE'),('연간 일정','ANNUAL SCHEDULE'),('중장기 로드맵','MID-TO-LONG TERM ROADMAP'),('전략 포지션','STRATEGIC POSITIONING'),('감사합니다.','MIRI COMPANY')]
B={};notes='프로젝트의 전체 과정을 선으로 연결하여 시각화하세요. 각 단계의 핵심을 아이콘으로 표현하면 전달력이 좋아집니다.'
B[2]=slot(group([agenda(['회사 개요','회사 비전','전략방향','주요 사업','운영흐름']),agenda(['장비 현황','KPI 구조','회사 강점','성과 추이','매출 비중'],6)]),1,12,2,5)
B[3]=slot(head('우리는 기술과 경험을 바탕으로<br>현장의 문제를 구조적으로 해결하는 기업입니다.'),1,12,1,2)+slot(prose('우리는 기술과 경험을 바탕으로<br>현장의 문제를 구조적으로 바라보고 해결해 왔습니다.\n\n사업의 출발점부터 현재에 이르기까지<br>문제를 함께 고민하고 해결해온 과정 속에서<br>신뢰받는 파트너로서의 관계를 만들어 왔습니다.\n\n이러한 접근 방식은<br>다양한 프로젝트 경험 속에서 축적된 우리의 일하는 기준입니다.'),1,6,3,4)+slot(prose('시장의 변화와 고객의 요구를 면밀히 분석해<br>실행 가능한 해법으로 연결합니다.\n\n단기적인 대응보다 문제의 본질을 정의하는 것을 우선하며,<br>복잡한 상황을 명확한 구조로 정리하는 데 집중합니다.\n\n<b>우리는 단순한 서비스 제공을 넘어,<br>고객의 상황에 맞는 방향과 결과를 함께 만들어갑니다.</b>'),7,6,3,4)
B[4]=slot(table([['산업','제조업','사원수','100명'],['기업 구분','중소기업','설립일','20xx.06.13'],['대표자','김미리','매출액','400억'],['주요 사업','제조 장비 개발 및 대여','주소','미리시 미리구 미리대로 7001번 길']]),1,9,3,4)+slot(frame(),10,3,1,6)
B[5]=slot(group([card('고객과 함께<br>성장하자','해당 페이지는 회사의 핵심 가치와 비전을 적는 페이지입니다. 회사가 추구하는 핵심적인 가치 세 가지만 뽑아보세요. 이 가치를 추구하는 이유는 무엇인지, 이것들을 통해 이루고 싶은 비전이나 목표는 무엇인지 설명해 주세요.',kick='VISION 1'),card('최고의 품질을<br>추구하자','회사가 추구하는 비전을 이루기 위해 어떤 노력과 사업을 하는지 적어보세요. 회사의 사업과 핵심 가치가 어떤 연관성을 가지고 있는지 설명해 주세요.',kick='VISION 2'),card('정직함으로<br>진심을 다하자','회사의 비전은 누구나 이해하기 쉽도록 명확하고 간결하게 작성해야 합니다. 회사가 장기적으로 달성하려는 목표는 무엇인지 생각해 보세요.',kick='VISION 3')]),3,10,1,6)
B[6]=slot(group([pill(a) for a in ['행동','욕구','흥미','인지']],'col'),1,2,1,6)+slot(el('pyramid','pyramid',''.join('<div class="level"><p class="name">키워드 '+a+'</p></div>' for a in 'ABCD')),3,5,1,6)+slot(prose('하단은 기초, 상단은 핵심입니다.\n\n계층 구조로 단계별 성장을 보여줘요.\n\n피라미드 구조는 시각적 안정감을 줍니다.\n\n핵심 키워드 아래 탄탄한 기초를 강조해요.'),8,5,1,6)
B[7]=slot(group([card('유기적인 연결망','각 요소가 독립적이지 않고 서로 긴밀하게 영향을 주고받는 유기적인 관계임을 보여줍니다.'),card('핵심은 정중앙에','중앙에 가장 중요한 키워드를 배치하고 주변으로 뻗어 나가는 원형 구조를 활용해 보세요.')],'col'),1,4,1,6)+slot(hub(['정직','신뢰','도전','혁신']),5,4,1,6)+slot(group([card('균형 잡힌 배치','위아래 순서가 있는 목록형과 달리 원형 배치는 모든 요소를 동등한 비중으로 다룹니다.'),card('정보의 생태 사이클','시선이 중앙에서 시작해 바깥으로 자연스럽게 이동하며 정보의 위계와 관계를 파악합니다.')],'col'),9,4,1,6)
B[8]=slot(listing([('노출','다양한 자료 중 핵심만 남기는 과정을 보여주세요. 위쪽에는 전체 데이터를 두고 아래쪽에는 최종 결과를 배치해 집중을 시각화합니다.'),('유입','시선이 자연스럽게 아래로 모이는 역삼각형 구조를 활용해 보세요. 상단에서 시작해 하단으로 내려갈수록 정보가 구체화됩니다.'),('구매','전체 시장에서 거점 시장으로 범위를 좁혀가며 타겟의 선명도를 높이세요. 대상은 줄어들지만 공략해야 할 대상이 누구인지 명확히 정의 내는 과정을 담습니다.')],'divided'),1,7,1,6)+slot(el('funnel','funnel',''.join(f'<div class="stage" style="--v:{v}"><p class="name">STEP 0{i+1}</p><p class="fig"></p></div>' for i,v in enumerate([100,67,34]))),8,5,1,6)
B[9]=''.join(slot(card(a,'타이포그래피 자체가 디자인이 되도록 폰트 굵기를 조절하여 세련된 느낌을 연출해 보세요.',f),1+(i%2)*6,6,1+(i//2)*3,3) for i,(f,a) in enumerate([('00%','성과 달성'),('+00%','전년 대비 성장'),('00%','시장 점유율'),('000%','목표 달성률')]))
B[10]=slot(head('단계별 과정을 순서대로 보여줘 이해를 돕습니다.'),1,12,1,1)+slot(steps(['노출','실행','점검','개선'],['왜 이 프로젝트가 시작되었는지 그리고 어떤 문제를 해결하고자 하는지 구체적으로 서술해 보세요.','문제의 원인을 정확히 파악해야 올바른 해결책이 나올 수 있으니 현상을 깊이 있게 분석하세요.','다양한 해결 방안을 모색하는 브레인스토밍을 통해 도출된 아이디어 중 핵심을 추려내야 합니다.','목표 달성을 위한 세부 전략을 수립하고 필요한 예산과 인력 그리고 일정을 확정 지어야 합니다.']),1,12,2,5)
B[11]=''.join(slot(card(a,b,kick='주요 사업 '+str(i+1)),1+(i%2)*6,6,1+(i//2)*3,3) for i,(a,b) in enumerate([('고성능 부품 개발','해당 페이지는 회사의 주요 사업에 관해 설명하는 페이지 입니다. 각 사업의 핵심 포인트를 간결하고 명확하게 적어주세요. 현재 업계 트렌드나 시장의 미래 전망을 언급해 가능성을 강조하세요.'),('산업용 장비 개발','사업의 장점과 혜택을 고객의 관점에서 설명해 보세요. 고객이 얻을 수 있는 장점을 명확하게 전달하는 것이 중요합니다.'),('제조 장비 개발','사업 설명에 중요한 키워드나 문장을 강조해 보세요. 고객이 중요한 정보를 쉽게 파악하도록 도와줍니다.'),('제조 장비 대여','사업의 성공 사례를 소개하며 회사의 사업이 효과적이었음을 보여주세요. 주요 파트너사와 협력 관계를 강조하며 신뢰성을 보여주세요.')]))
B[12]=slot(group([card(a,b+'<br><br>• 항목의 비중이 비슷할 때 효과적입니다.<br><br>• 텍스트 분량을 맞춰 균형을 잡으세요.',kick='ABCD'[i]) for i,(a,b) in enumerate([('주요 특징','시선은 왼쪽에서 오른쪽으로 이동합니다. 정보를 가로로 나열하면 내용을 편안하게 읽을 수 있습니다.'),('핵심 역량','시간 순서대로 진행되는 프로젝트 일정이나 단계별 프로세스를 설명할 때 가장 효과적입니다.'),('체크 포인트','핵심 내용을 가로로 나란히 배치하여 복잡한 정보를 한눈에 비교할 수 있도록 정리해 보세요.'),('서비스','다루는 항목들의 비중이 서로 비슷할 때 사용하면 가장 안정적이고 효과적인 구조입니다.')])]),1,12,1,6)
B[13]=slot(head('복잡한 절차를 단순화하여 명쾌하게 정리했어요.'),1,12,1,1)+slot(steps(['인지','탐색','구매','리뷰'],['읽는 이에게 전체적인 방향성을 제시하고 프로젝트에 대한 기대감을 심어주는 도입부 역할을 합니다.','객관적인 수치나 근거 자료를 제시하여 분석의 신뢰도를 높이고 논리적인 타당성을 확보해야 해요.','아이디어 선정 기준과 이유를 명확히 명시하면 기획의 설득력이 높아지고 공감을 얻기 쉽습니다.','막연했던 아이디어가 체계적인 실행 계획으로 구체화되는 과정을 보여주어 신뢰도를 높여 보세요.'],'col'),1,12,2,5)
B[14]=slot(steps(['노출','유입','활동'],['프로젝트의 정의와 범위를 명확히 설정하여 앞으로 전개될 내용의 길잡이 역할을 하는 단계입니다.','내부 역량과 외부 환경을 종합적으로 분석하여 우리가 가진 강점과 약점을 명확히 파악해 보세요.','시장의 빈틈을 파고드는 전략을 수립하여 프로젝트가 성공할 수밖에 없는 이유를 증명해 보세요.']),1,12,1,3)+slot(steps(['추천','재구매','전환'],['다양한 환경에서의 테스트 결과를 제시하여 서비스가 어떤 상황에서도 잘 작동함을 증명해야 해요.','단순한 기능 구현을 넘어 사용자 경험을 고려한 디테일한 개발 과정을 보여주어 전문성을 높여요.','각 단계별로 필요한 자원을 배분하고 리스크 관리 계획을 세워 프로젝트의 안정성을 확보하세요.'],marks=['06','05','04']),1,12,4,3)
B[15]=slot(el('person','people',''.join(el('person','person',f'<div class="seat avatar" data-ph="{i+1}"></div><p class="name">제조 장비 {a}</p><p class="note">장비 명　제조 장비<br>제조회사　미리 컴퍼니<br>고유 번호　00011110<br>모델명　Miri-00000</p>') for i,a in enumerate('ABC'))),1,12,1,6)
B[16]=slot(group([table([['구동 형태','Motor Driver'],['전압','24VDC'],['장비 하중','300kg'],['길이','1500mm'],['높이','1200mm'],['넓이','800mm']],['모델명','Miri-00000']) for i in range(2)]),1,12,1,6)
B[17]=slot(el('matrix','matrix',''.join('<div class="cell'+(' on' if i==0 else '')+'"><p class="name">'+a+'</p><p class="note">'+b+'</p></div>' for i,(a,b) in enumerate([('핵심 시장','프로젝트의 안정성을 증명하는 핵심 강점을 시각적으로 강조하세요. 긍정적인 내부 요인이 무엇인지 보여줍니다.'),('유망 시장','분석 결과를 토대로 약점을 보완할 구체적인 행동 지침을 만드세요. 문제를 인식하는 것이 해결의 시작입니다.'),('쇠퇴 시장','약점을 보완하고 기회를 활용하는 반전 전략을 짤 수도 있습니다. 외부의 호재가 내부의 부족함을 채워줍니다.'),('철수 시장','분석을 통해 도출된 위험 요인은 위기 관리 매뉴얼의 기초가 됩니다. 선제적인 방어가 최선의 공격입니다.')]))),1,12,1,6)
B[18]=slot(group([card('혁신적인 기술','회사의 강점과 경쟁력을 적는 페이지입니다. 키워드를 적어보세요.'),card('고객 중심 서비스','경쟁사와 차별화되는 우리 회사만의 독특한 서비스와 제품을 강조해 보세요.')],'col'),1,4,1,6)+slot(hub(['기술','파트너십','네트워크','서비스','성장력'],'우리의 강점',['cpu','globe','trending-up','user','handshake']),5,4,1,6)+slot(group([card('강력한 파트너십','실제 고객의 긍정적인 피드백이나 추천사를 인용해 신뢰도를 높여보세요.'),card('글로벌 네트워크','높은 고객 유지율을 강조하며 회사의 네트워크가 견고함을 보여주세요.'),card('지속 가능한 성장력','회사의 미래 가능성과 장기적인 비전과 목표를 보여주세요.')],'col'),9,4,1,6)
B[19]=slot(el('versus','versus',side('<p class="name">교육 훈련</p>'+listing([('복합 원인을 나열해요.','주장을 뒷받침할 수 있는 데이터를 이 공간에 배치해 보세요.'),('핵심 키워드 위주로 간결하게 작성해요.',''),('핵심 키워드 위주로 간결하게 작성해요.','')]))+'<b class="vs">VS</b>'+side('<p class="name">업무 효율</p>'+listing([('핵심 메시지 한 문장.','긍정적인 결과에 대한 분석이라면 이 성공 요인을 어떻게 유지하고 다른 프로젝트에 확산시킬지 설명하세요.'),('결론적으로 도출된 핵심 메시지 요약하세요.',''),('결론적으로 도출된 핵심 메시지 요약하세요.','')]),'on')),1,12,1,6)
B[20]=slot(table([['매출 목표','10억원','15억원','20억원','25억원'],['달성률','98%','105%','100%','110%']],['구분','1분기','2분기','3분기','4분기']),1,6,1,3)+slot(prose('많은 데이터를 한 번에 정리하기에 표만큼 좋은 도구는 없습니다. 동일한 기준에 따라 데이터를 칼럼별로 입력하면, 읽는 이가 정보를 쉽게 비교하고 분석할 수 있죠. 각 항목에 구체적인 수치나 단위를 정확하게 기입하여 객관성을 확보하고 프레젠테이션의 신뢰도를 높이세요.'),1,6,4,3)+slot(bars([10,15,20,25],['1분기','2분기','3분기','4분기'],30),8,5,1,6)
B[21]=slot(metric('1위','업계 순위','숫자를 크게 배치하여 정보를 직관적으로 전달하는 레이아웃입니다. 긴 설명보다 명확한 수치 하나가 내용을 빠르게 이해시킵니다.'),1,3,1,6)+''.join(slot(card(a,'가장 자랑하고 싶은 핵심 성과를 크게 적어 시선을 사로잡으세요.',f),4+(i%2)*4,4 if i%2==0 else 5,1+(i//2)*3,3) for i,(f,a) in enumerate([('No.1','브랜드 평판'),('4.9점','고객 평점'),('1위','선호도 조사'),('AAA','등급 획득')]))
B[22]=slot(prose('과거의 기록을 바탕으로 전략적 의사결정을 내려야 할 때 필수적인 그래프입니다. 꾸준히 성장하고 있는지, 아니면 특정 주기로 등락을 반복하는지 패턴을 분석해 보세요. 변화의 흐름을 읽는 것은 곧 경쟁력이 되며, 이 페이지는 비즈니스의 나침반 역할을 톡톡히 해냅니다.'),1,5,1,3)+slot(metric('5,200','일별 생산량 최대','단순한 기록을 넘어 전략적 의사결정을 돕는 나침반이 됩니다.'),1,5,4,3)+slot(lines([5000,4500,4000,5000,4800,5000,5200],['월요일','화요일','수요일','목요일','금요일','토요일','일요일'],7000),6,7,1,6)
B[23]=slot(bars([80,100],['경쟁사','자사'],100),1,5,1,6)+slot(head('월별 고객 유입 수'),7,6,1,1)+slot(group([card('경쟁사','데이터의 크기를 길이로 변환하여 항목 간의 차이를 직관적으로 비교하는 데 최적화된 레이아웃으로 활용해 보세요.','80만 명'),card('자사','가장 긴 막대와 짧은 막대를 대조하면 우열이 한눈에 들어옵니다. 복잡한 수치도 그림이 되면 이해 속도가 빨라지죠.','100만 명')]),7,6,2,5)
B[24]=slot(group([group([pill('북미','20%'),pill('아시아','10%')]),group([pill('남미','25%'),pill('아프리카','30%')]),pill('유럽','15%')],'col'),1,6,1,3)+slot(prose('<b>글로벌 매출 비중</b>\n\n원 그래프와 유사하지만 중앙 공간 활용도가 높아 정보 전달과 디자인을 동시에 잡을 수 있는 레이아웃입니다. 그래프 옆이나 하단에는 데이터가 시사하는 핵심 내용을 요약해 적어주세요.'),1,6,4,3)+slot(donut(30,'글로벌 매출','Global'),8,5,1,6)
B[26]=slot(prose('장기 프로젝트의 경우 월 단위로, 단기 프로젝트는 주 단위로 쪼개어 관리하는 것이 좋습니다.'),1,12,1,1)+slot(roadmap(),1,12,2,5)
cal=[]
for r in range(5):cal.append([str(r*7+c) if 1<=r*7+c<=31 else '' for c in range(7)])
B[27]=slot(group([pill('15일','리드 회의'),pill('15~20일','성과 평가 기간')]),1,6,1,2)+slot(listing([('일정 관리 가이드',''),('일정을 한눈에 관리하세요.',''),('마감 기한이 명시된 일정은 시간을 엄수해 주시기 바랍니다.',''),('마감 기한이 명시된 일정은 시간을 엄수해 주시기 바랍니다.','')],'check'),1,6,3,4)+slot(table(cal,['SUN','MON','TUE','WED','THU','FRI','SAT']),7,6,1,6)
B[28]=slot(el('timeline','track',''.join('<div class="stop"><p class="kick">'+str(i+1)+'분기</p><p class="name">'+a+'</p><p class="note">'+notes+'</p></div>' for i,a in enumerate(['법인 설립','서비스 출시','특허 등록','투자 유치'])),'alt'),1,12,1,6)
B[29]=slot(el('positioning','posmap','<div class="axis-x"><span>불안정</span><span>안정</span></div><div class="axis-y"><span>느림</span><span>빠름</span></div>'+''.join(f'<div class="mark'+(' on' if i==5 else '')+f'" style="--x:{x};--y:{y}"><p class="name">버전 {i+1}</p></div>' for i,(x,y) in enumerate([(18,18),(28,48),(53,23),(45,72),(86,40),(86,86)]))),1,6,1,6)+slot(head('서비스 안정성 및 속도','가까이 모여 있는 점들을 하나의 그룹으로 묶어서 설명해 보세요.'),7,6,1,2)+slot(table([[f'버전 {i+1}',b] for i,b in enumerate(['느린속도, 불안정','중간속도, 불안정','느린속도, 안정','빠른속도, 낮은안정','중간속도, 안정','빠른속도, 높은안정'])]),7,6,3,4)
B[30]=slot(listing([('주소','미리시 미리구 미리대로 7001번 길'),('대표 전화','031-000-0000'),('이메일','miricompany @ 0000.com'),('홈페이지','www.000000.com'),('상담 시간','월~금 09:00~18:00')]),1,12,3,4)
links='<link rel="stylesheet" href="../assets/type-steps.css"><link rel="stylesheet" href="../../assets/fonts/fonts.css"><link rel="stylesheet" href="../crossrail/kit/css/tokens.css"><link rel="stylesheet" href="../crossrail/foundation/foundation.css">'+''.join('<link rel="stylesheet" href="../crossrail/elements/'+e.name+'/element.css">' for e in sorted((C/'elements').iterdir()))+'<link rel="stylesheet" href="../assets/source-palette.css">'
for n in range(1,31):
 if n==1:body='<section class="slide cover"><div class="page"><div class="lockup at-top-left"><p class="kicker">가이드에 따라 쉽고 빠르게 만드는</p><h1 class="title">명확하게 전달하는<br><b>회사 소개서</b></h1></div><p class="meta">MIRI COMPANY</p><div class="deco"></div></div></section>'
 elif n==25:body='<section class="slide cover"><div class="page"><div class="lockup at-left"><p class="kicker">SECTION OVERVIEW</p><h1 class="title">이번 섹션에서 다룰 핵심 내용을<br>간단히 정리합니다</h1><p class="lead">챕터가 존재하는 이유를 명확하게 설명해 보세요.</p></div><div class="deco"></div></div></section>'
 else:
  title,kick=('목차','TABLE OF CONTENTS') if n==2 else T[n-1]
  body='<section class="slide'+(' on' if n in [9,13,17,21] else '')+'"><div class="page">'+('<div class="rail on"></div>' if n in [2,30] else '')+'<header class="head'+(' at-bottom-left' if n==30 else '')+'"><p class="kicker">'+kick+'</p><h1 class="title">'+title+'</h1><span class="no">'+(str(n-2).zfill(2) if n>2 else '')+'</span></header><div class="body">'+B[n]+'</div></div></section>'
 if n==30:body=re.sub(r'<span class="no">.*?</span>','',body)
 (O/f'slide_{n:02d}.html').write_text('<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>Crossrail reassembled '+str(n)+'</title>'+links+'</head><body>'+body+'</body></html>')
print('Reassembled 30 pages from collection only')
