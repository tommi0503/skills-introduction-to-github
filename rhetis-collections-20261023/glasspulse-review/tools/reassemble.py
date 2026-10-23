from pathlib import Path
import json
C=Path('/workspace/output/glasspulse');R=Path('/workspace/output/glasspulse-review');D=R/'reassembled'
# The assembled pages use the collection CSS verbatim. Only the host palette and type scale are supplied.
css=(C/'kit/css/tokens.css').read_text()+(C/'foundation/foundation.css').read_text()+''.join(p.read_text() for p in sorted(C.glob('elements/*/element.css')))
(R/'library/collection.css').write_text(css)
steps=json.load(open('/workspace/work/reference/contract/type-steps.json'));pal=json.load(open('/workspace/work/reference/contract/palette.json'))
# Original deck palette belongs to the host style, never to the collection.
palette=pal['dark'].copy();palette.update({'--page':'#000000','--ink':'#f8fbff','--a1':'#38a2fe','--a1-on':'#ffffff','--n-1':'#16171d','--n-2':'#202733','--n-3':'#414141','--n-4':'#596b7b','--n-5':'#7c8a94','--n-6':'#b9bfc2','--n-7':'#c1c7cd','--n-8':'#e1e6ea','--n-9':'#f8fbff'})
for n in range(1,10):
 for suffix in ['', '-soft','-muted']:
  if n<=3: val=['#091522','#123149','#24465e'][n-1]
  else:val='#38a2fe'
  palette[f'--a1-{n}{suffix}']=('#203a4b' if n==2 and suffix=='-muted' else val)
style='.slide{'+''.join(f'--type-{x}:{x}px;' for x in steps)+'}\n.slide.dark{'+''.join(k+':'+v+';' for k,v in palette.items())+'}\n'
(R/'library/source-style.css').write_text(style)
def el(cl,folder,body,grid=None,values=''):
 s=(f'grid-column:{grid[0]} / span {grid[1]}; grid-row:{grid[2]} / span {grid[3]};' if grid else '')+values
 return f'<div class="{cl}" data-el="glasspulse-{folder}"'+(f' style="{s}"' if s else '')+'>'+body+'</div>'
def group(items,grid,cl='group'):
 return f'<div class="{cl}" style="grid-column:{grid[0]} / span {grid[1]}; grid-row:{grid[2]} / span {grid[3]}">'+''.join(items)+'</div>'
def card(name,fig='',note='',kick='',grid=None,variant='',mark=''):
 return el('card '+variant,'card','<div class="parts">'+(f'<p class="kick">{kick}</p>' if kick else '')+(f'<span class="mark">{mark}</span>' if mark else '')+(f'<p class="fig">{fig}</p>' if fig else '')+f'<b class="name">{name}</b>'+(f'<p class="note">{note}</p>' if note else '')+'</div>',grid)
def headline(k,t,n='',grid=(1,4,1,6),variant=''):
 return el('headline '+variant,'headline',f'<p class="kick">{k}</p><h2>{t}</h2>'+ (f'<p class="note">{n}</p>' if n else ''),grid)
def area(vals,grid,labels=None,name=''):
 pts=''.join(f'<div class="pt" style="--v:{v}"></div>' for v in vals)
 return el('areas','chart-area','<div class="series">'+(f'<b class="name">{name}</b>' if name else '')+pts+'</div><div class="axis">'+''.join(f'<span>{t}</span>' for t in (labels or ['20XX']*len(vals)))+'</div>',grid,'--max:100')
def callout(t,grid):return el('callout','callout',f'<p>{t}</p>',grid)
P={}
P[1]=('Town Hall','<b>2080</b> 상반기 타운홀',': 우리가 만든, 우리가 향할','cover')
P[2]=('','CONTENTS','프레젠테이션의 핵심 주제나 슬로건을 입력해 보세요.',el('agenda','agenda',''.join(f'<div class="entry"><span class="mark">0{i}</span><b class="name">{t}</b><p class="note"></p></div>' for i,t in enumerate(['상반기 돌아보기','주요 성과','고객 시장 현황','하반기 전략 방향','팀별 목표','Q&A'],1)),(1,12,1,6)))
P[3]=("Today's Agenda",'오늘의 아젠다','',el('steps','steps',''.join(f'<div class="step"><span class="mark">0{i}</span><b class="name">{t}</b><p class="note"></p></div>' for i,t in enumerate(['상반기<br>성과','하반기<br>전략','팀별<br>목표'],1)),(1,12,1,6)))
P[4]=('Overview','','',headline('','미리컴퍼니는<br><b>남들이 이루지 못할 것이라 말했던<br>목표</b>를 향해 달려왔습니다.','',(1,12,1,6),'big center'))
P[5]=('숫자로 보는 상반기','핵심 지표 요약','',group([card(t,f,'이곳에 설명을 입력해 보세요.',t) for t,f in [('상반기 매출','000억'),('신규 고객','000명'),('목표 달성률','00%')]],(1,12,1,6)))
P[6]=('Revenue & Growth','매출 및 성장 현황','',el('bars h','chart-bar','<div class="bar on" style="--v:86"><b>00%</b><span>20XX</span></div><div class="bar" style="--v:49"><b>00%</b><span>20XX</span></div>',(1,12,1,4),'--max:100')+callout('상반기 매출은 전년 동기 대비 <b>00%</b> 성장했습니다.',(1,12,5,2)))
P[7]=('','','',headline('Overview','주요 성과 1','해당 장표의 핵심 주제나 요약 내용을 입력해 보세요.',(1,4,1,3))+card('신규 계약 증가','00%','','',(1,4,4,3),'quiet')+area([20,47,33,100],(5,8,1,4))+callout('전년 대비 <b>00%</b> 증가했습니다.',(5,8,5,2)))
P[8]=('','','',headline('Overview','주요 성과 2','',(1,4,1,2))+el('prose lead','prose','<p>한 번 함께한 고객은 <b>미리컴퍼니 서비스</b>에 만족해 다시 돌아옵니다.</p>',(1,4,3,4))+area([36,21,43.5,36,89],(5,8,1,3),name='고객 만족도')+card('고객 재계약률','+00%','','',(5,8,4,3)))
P[9]=('Team Highlights','팀별 하이라이트','',group([card(t,'',n,'') for t,n in [('영업팀','신규 계약 000건 / 목표 대비 00% 달성<br>이곳에 각 팀별 핵심 성과 키워드 수치를 입력해 보세요.'),('마케팅팀','리드 000건 / 캠페인 00개 집행<br>이곳에 각 팀별 핵심 성과 키워드 수치를 입력해 보세요.'),('운영팀','고객 만족도 00점 / 처리 건수 000건<br>이곳에 각 팀별 핵심 성과 키워드 수치를 입력해 보세요.')]],(1,12,1,6),'stack'))
P[10]=('Challenges & Responses','우리의 도전과 대응','',group([card('외부<br>파트너십 확대','','인력 부족','도전'),card('핵심 고객<br>집중 전략 전환','','시장 경쟁 심화','대응')],(1,12,1,6)))
P[11]=('Customer & Market','고객 및 시장 현황','',el('stat','metric','<div class="parts"><b class="fig">000억 원+</b><b class="name">당사 타겟 시장 규모</b></div>',(1,4,1,4))+area([30,23,44,37,86],(5,8,1,4))+callout('시장은 연평균 <b>00%</b> 성장 중이며 우리의 기회는 확대되고 있습니다.',(1,12,5,2)))
P[12]=('Competitive Landscape','경쟁 환경 변화','',group([el('delta','delta',f'<span class="from">{a}</span><span class="to">{b}</span>') for a,b in [('신규 경쟁자 진입','시장 내 유사 서비스 증가로 차별화 더욱 중요'),('고객 기대 수준 상승','고객들의 품질, 속도 기대치가 전년 대비 상승'),('기술 변화 가속화','이곳에 기술 변화 관련 설명을 입력해 보세요.')]],(1,12,1,6),'stack'))
P[13]=('','','',headline('Business Position','우리의<br>현재 위치','해당 장표의 핵심 주제나 요약 내용을 입력해 보세요.',(1,4,1,6))+el('posmap','positioning','<div class="axis-x"><span>가격 경쟁력 낮음</span><span>가격 경쟁력 높음</span></div><div class="axis-y"><span>서비스 품질 낮음</span><span>서비스 품질 높음</span></div>'+''.join(f'<div class="mark {"on" if t=="미리컴퍼니" else ""}" style="--x:{x};--y:{y}"><b class="name">{t}</b></div>' for x,y,t in [(15,70,'A사'),(32,15,'B사'),(69,29,'C사'),(86,85,'미리컴퍼니')]),(5,8,1,6)))
P[14]=('하반기 핵심 전략 방향','하반기, 우리는 세가지에 집중합니다.','',group([card(t,'','이곳에 해당 주제에 맞는 하반기 핵심 전략 방향을 요약하여 입력해 보세요',f'0{i}') for i,t in enumerate(['고객 확대','신규 사업 진입','운영 효율화'],1)],(1,12,1,6)))
P[15]=('','','',headline('전략 상세 1','고객 확대','해당 장표의 핵심 주제나 내용을 입력해 보세요.',(1,3,1,6))+group([el('person','person',f'<div class="seat portrait" data-ph=""></div><b class="name"><small>overview. 0{i}</small>{t}</b><p class="note">이곳에 해당 주제에 맞는 하반기 핵심 전략 방향을 요약하여 입력해 보세요</p>') for i,t in enumerate(['기존 고객 업셀링 운영','신규 타겟 세그먼트 공략','파트너 채널 확대'],1)],(4,9,1,6)))
P[16]=('','','',headline('전략 상세 2','신규 사업<br>진입','해당 장표의 핵심 주제나 내용을 입력해 보세요.',(1,3,1,4))+el('steps','steps',''.join(f'<div class="step"><span class="mark"><span class="icon" data-icon="circle-check"></span></span><b class="name">{t}</b><p class="note"></p></div>' for t in ['시장 조사 완료','파일럿 준비중','하반기 론칭 예정']),(4,9,1,4))+callout('우리가 다음으로 향할 시장입니다. 이곳에 <b>신규 사업 방향 설명</b>을 입력해 보세요.',(1,12,5,2)))
P[17]=('Priority Initiatives','우선순위 과제','',el('venn','venn',''.join(f'<div class="set"><b class="name">{t}</b></div>' for t in ['핵심 고객 유지율 제고','내부 프로세스 자동화','신규 채널 개발']),(1,8,1,6))+card('이곳에 기대 효과 키워드를 입력해 보세요.','','','',(9,4,1,6),'on'))
P[18]=('H2 Goals by Team','팀별 하반기 목표','',group([card(n,v,'',c) for c,n,v in [('영업팀','신규 계약','000건'),('마케팅팀','리드','000건'),('운영팀','고객 만족도','00점'),('개발팀','신규 기능','00개 출시')]],(1,12,1,6),'group two'))
def wrapchart(body,grid):return el('card','card','<div class="parts">'+body+'</div>',grid)
P[6]=(P[6][0],P[6][1],P[6][2],wrapchart(el('bars h','chart-bar','<div class="bar on" style="--v:86"><b>00%</b><span>20XX</span></div><div class="bar" style="--v:49"><b>00%</b><span>20XX</span></div>',None,'--max:100')+callout('상반기 매출은 전년 동기 대비 <b>00%</b> 성장했습니다.',None),(1,12,1,6)))
P[7]=('','','',headline('Overview','주요 성과 1','해당 장표의 핵심 주제나 요약 내용을 입력해 보세요.',(1,4,1,3))+card('신규 계약 증가','00%','','',(1,4,4,3),'quiet')+wrapchart(area([20,47,33,100],None)+callout('전년 대비 <b>00%</b> 증가했습니다.',None),(5,8,1,6)))

P[3]=('','','',headline("Today's Agenda",'오늘의 아젠다','',(1,12,1,2),'big center')+el('steps','steps',''.join(f'<div class="step"><span class="mark">0{i}</span><b class="name">{t}</b><p class="note"></p></div>' for i,t in enumerate(['상반기<br>성과','하반기<br>전략','팀별<br>목표'],1)),(1,12,3,4)))
P[4]=('','','',el('headline center','headline','<div class="seat back" data-ph="1"></div><p class="kick">Overview</p><h2>미리컴퍼니는<br><b>남들이 이루지 못할 것이라 말했던<br>목표</b>를 향해 달려왔습니다.</h2>',(1,12,1,6)))
P[5]=('','','',headline('숫자로 보는 상반기','핵심 지표 요약','',(1,12,1,2),'big center')+group([card('',f,'이곳에 설명을 입력해 보세요.',t) for t,f in [('상반기 매출','000억'),('신규 고객','000명'),('목표 달성률','00%')]],(1,12,3,4)))
P[7]=('','','',headline('Overview','주요 성과 1','해당 장표의 핵심 주제나 요약<br>내용을 입력해 보세요.',(1,4,1,3))+card('신규 계약 증가','00%','','',(1,4,4,3),'quiet',mark='<span class="icon" data-icon="arrow-up"></span>')+wrapchart(area([20,47,33,100],None)+callout('전년 대비 <b>00%</b> 증가했습니다.',None),(5,8,1,6)))
P[8]=('','','',headline('Overview','주요 성과 2','',(1,4,1,3))+el('prose lead','prose','<p>한 번 함께한<br>고객은 <b>미리컴퍼니<br>서비스</b>에 <strong>만족해<br>다시 돌아</strong>옵니다.</p>',(1,4,4,3))+area([36,21,43.5,36,89],(5,8,1,3),name='고객 만족도')+card('고객 재계약률','+00%','','',(5,8,4,3),'quiet',mark='<span class="icon" data-icon="arrow-up"></span>'))
P[10]=('Challenges & Responses','우리의 도전과 대응','',group([card('외부<br>파트너십 확대','','인력 부족','도전',mark='<span class="icon" data-icon="arrow-down"></span>'),card('핵심 고객<br>집중 전략 전환','','시장 경쟁 심화','대응',mark='<span class="icon" data-icon="arrow-down"></span>')],(1,12,1,6)))
P[11]=('Customer & Market','고객 및 시장 현황','',wrapchart(el('stat','metric','<div class="parts"><b class="name">당사 타겟 시장 규모</b><b class="fig">000억 원+</b></div>')+area([30,23,44,37,86],None),(1,12,1,5))+callout('시장은 연평균 <b>00%</b> 성장 중이며 우리의 기회는 확대되고 있습니다.',(1,12,6,1)))
P[13]=('','','',headline('Business Position','우리의<br>현재 위치','해당 장표의 핵심 주제나<br>요약 내용을 입력해 보세요.',(1,4,1,6),'big')+P[13][3].split('</div>',1)[1] if False else P[13][3])
P[15]=('','','',headline('전략 상세 1','고객 확대','해당 장표의 핵심 주제나<br>내용을 입력해 보세요.',(1,3,1,6))+group([el('person','person',f'<div class="seat portrait" data-ph=""></div><b class="name"><small>overview. 0{i}</small>{t}</b><p class="note">이곳에 해당 주제에 맞는 하반기 핵심 전략 방향을 요약하여 입력해 보세요</p>') for i,t in enumerate(['기존 고객<br>업셀링 운영','신규 타겟<br>세그먼트 공략','파트너<br>채널 확대'],1)],(4,9,1,6)))
P[16]=('','','',headline('전략 상세 2','신규 사업<br>진입','해당 장표의 핵심 주제나<br>내용을 입력해 보세요.',(1,3,1,4))+el('steps','steps',''.join(f'<div class="step"><span class="mark"><span class="icon" data-icon="circle-check"></span></span><b class="name">{t}</b><p class="note"></p></div>' for t in ['시장 조사<br>완료','파일럿<br>준비중','하반기<br>론칭 예정']),(4,9,1,4))+callout('우리가 다음으로 향할 시장입니다. 이곳에 <b>신규 사업 방향 설명</b>을 입력해 보세요.',(1,12,5,2)))
P[17]=(P[17][0],P[17][1],P[17][2],el('venn','venn',''.join(f'<div class="set"><b class="name">{t}</b></div>' for t in ['핵심 고객<br>유지율 제고','내부 프로세스<br>자동화','신규 채널<br>개발']),(1,8,1,6))+card('이곳에 기대<br>효과 키워드를<br>입력해 보세요.','','','',(9,4,1,6),'on'))

P[8]=(P[8][0],P[8][1],P[8][2],P[8][3].replace('class="card quiet"','class="card line"'))
P[13]=(P[13][0],P[13][1],P[13][2],P[13][3].replace('class="headline "','class="headline big"'))
P[11]=(P[11][0],P[11][1],P[11][2],P[11][3].replace('class="callout"','class="callout quiet"'))
P[16]=(P[16][0],P[16][1],P[16][2],P[16][3].replace('class="callout"','class="callout on"'))

# Original team proof points retain their check marks and selective emphasis.
checks=[('영업팀','신규 계약 000건 / <b>목표 대비 00% 달성</b>'),('마케팅팀','리드 000건 / <b>캠페인 00개 집행</b>'),('운영팀','고객 만족도 00점 / <b>처리 건수 000건</b>')]
P[9]=(P[9][0],P[9][1],P[9][2],group([card(t,'','<span class="icon" data-icon="check"></span>'+n+'<br><span class="icon" data-icon="check"></span>이곳에 각 팀별 핵심 성과 키워드 수치를 입력해 보세요.','') for t,n in checks],(1,12,1,6),'stack'))

P[13]=(P[13][0],P[13][1],P[13][2],P[13][3].replace('해당 장표의 핵심 주제나 요약 내용을 입력해 보세요.','해당 장표의 핵심 주제나<br>요약 내용을 입력해 보세요.'))
P[14]=(P[14][0],P[14][1],P[14][2],P[14][3].replace('이곳에 해당 주제에 맞는 하반기 핵심 전략 방향을 요약하여 입력해 보세요','이곳에 해당 주제에 맞는<br>하반기 핵심 전략 방향을<br>요약하여 입력해 보세요'))
P[15]=(P[15][0],P[15][1],P[15][2],P[15][3].replace('이곳에 해당 주제에 맞는 하반기 핵심 전략 방향을 요약하여 입력해 보세요','이곳에 해당 주제에 맞는<br>하반기 핵심 전략 방향을<br>요약하여 입력해 보세요'))
for i in [15,16]:P[i]=(P[i][0],P[i][1],P[i][2],P[i][3].replace('class="headline "','class="headline big quiet"'))
for n,(k,t,lead,body) in P.items():
 if body=='cover':
  content=f'<section class="slide dark cover"><div class="top"><span class="deck">MIRI COMPANY</span></div><div class="page"><div class="deco"></div><div class="lockup at-center"><p class="kicker">{k}</p><h1 class="title">{t}</h1><p class="lead">{lead}</p></div><p class="meta">2080.00.00 미리동 A관</p></div></section>'
 else:
  head=f'<header class="head {"" if n in [9,12,17,18] else "center"}">'+(f'<p class="kicker">{k}</p>' if k else '')+(f'<h1 class="title">{t}</h1>' if t else '')+(f'<p class="lead">{lead}</p>' if lead else '')+'</header>' if k or t or lead else ''
  content=f'<section class="slide dark"><div class="top"><span class="deck">MIRI COMPANY</span><span class="label">2080 Town Hall</span></div><div class="page">{head}<div class="body">{body}</div></div></section>'
 html='<!doctype html><html lang="ko"><head><meta charset="utf-8"><link rel="stylesheet" href="../assets/fonts.css"><link rel="stylesheet" href="../library/collection.css"><link rel="stylesheet" href="../library/source-style.css"></head><body>'+content+'<script src="../assets/icons.js"></script></body></html>'
 # No new layout CSS. The browser default body margin is suppressed with a standard HTML body attribute.
 html=html.replace('<body>','<body style="margin:0">')
 (D/f'slide-{n:02}.html').write_text(html)
print('reassembled',len(P))
