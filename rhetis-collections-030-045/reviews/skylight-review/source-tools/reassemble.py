from pathlib import Path
from html import escape
import json,re
C=Path('/workspace/work/deliverables/skylight');R=Path('/workspace/work/deliverables/skylight-review/reassembled');R.mkdir(exist_ok=True)
# Exact collection source is concatenated; the only additional styles are host palette and type scale.
css=(C/'kit/css/tokens.css').read_text()+(C/'foundation/foundation.css').read_text()+''.join(p.read_text() for p in sorted(C.glob('elements/*/element.css')))
defaults={};regs={}
for jp in [C/'foundation/foundation.json',*sorted(C.glob('elements/*/element.json'))]:
 j=json.loads(jp.read_text());defaults.update(j.get('tokenDefaults',{}));regs.update(j.get('registrations',{}))
css='\n'.join(regs.values())+'\n.slide{'+''.join(k+':'+v+';' for k,v in defaults.items())+'}\n'+css
(R/'collection.css').write_text(css)
palette=json.load(open('/workspace/work/reference/contract/palette.json'))['light']
palette.update({'--page':'#ffffff','--ink':'#2c4b69','--a1':'#58a4ee','--a1-on':'#ffffff','--a2':'#6488a8','--a2-on':'#ffffff','--a3':'#8aa8bf','--a3-on':'#12212e','--a4':'#aacce8','--a4-on':'#12212e'})
ns=['#f7f7f7','#ecf1f5','#d4dee6','#bbbbbb','#aaaaaa','#7e95a8','#5d7890','#626262','#294760']
for i,n in enumerate(ns,1):palette[f'--n-{i}']=n
shades=['#f0f8fd','#daedff','#b8d9fa','#8dc8ff','#68bafb','#008ff3','#2c4b69','#24455f','#1c3850']
for a in range(1,5):
 for i,n in enumerate(shades,1):
  for suf in ['','-soft','-muted']:palette[f'--a{a}-{i}{suf}']=n
palette['--a2-2-soft']='#d5f4fc'
palette['--a2-3-soft']='#bbf1fa'
style='.slide {'+''.join(f'{k}:{v};' for k,v in palette.items())+''.join(f'--type-{n}:{n}px;' for n in json.load(open('/workspace/work/reference/contract/type-steps.json')))+'}'
def el(f,root,inner,cls='',pos=None,stylev=''):
 st=''
 if pos:
  x,y,w,h=pos;st=f'grid-column:{x} / span {w}; grid-row:{y} / span {h};'
 st+=stylev
 return f'<div class="{root} {cls}" data-el="skylight-{f}"'+(f' style="{st}"' if st else '')+'>'+inner+'</div>'
def group(inner,pos,cls='group'):
 x,y,w,h=pos;return f'<div class="{cls}" style="grid-column:{x} / span {w}; grid-row:{y} / span {h}">{inner}</div>'
def head(n,note='',kick='',pos=None,cls=''):
 return el('headline','headline',(f'<p class="kick">{kick}</p>' if kick else '')+f'<h2>{n}</h2>'+(f'<p class="note">{note}</p>' if note else ''),cls,pos)
def card(n,note='',fig='',kick='',cls='',pos=None):
 return el('card','card','<div class="parts">'+(f'<p class="kick">{kick}</p>' if kick else '')+(f'<b class="fig">{fig}</b>' if fig else '')+f'<p class="name">{n}</p>'+(f'<p class="note">{note}</p>' if note else '')+'</div>',cls,pos)
def lst(items,pos=None,cls='',nameonly=False):
 out=''
 for a in items:
  if isinstance(a,tuple):n,nt=a
  else:n,nt=a,''
  out+='<div class="item"><p class="name">'+n+'</p>'+(f'<p class="note">{nt}</p>' if nt else '')+'</div>'
 return el('list','list',out,cls,pos)
def call(s,pos):return el('callout','callout','<p>'+s+'</p>',pos=pos)
def bars(vals,labs,pos=None,maxv=None,horiz=False):
 return el('chart-bar','bars',''.join(f'<div class="bar'+(' on' if i==len(vals)-1 else '')+f'" style="--v:{v}"><b>{v:,}</b><span>{n}</span></div>' for i,(v,n) in enumerate(zip(vals,labs))), 'h' if horiz else '',pos,f'--max:{maxv or max(vals)*1.1}')
def lines(vals,labs,pos=None,maxv=None):
 return el('chart-line','lines',''.join(f'<div class="pt'+(' on' if i==len(vals)-1 else '')+f'" style="--v:{v}"><b>{v}</b><span>{n}</span></div>' for i,(v,n) in enumerate(zip(vals,labs))),pos=pos,stylev=f'--max:{maxv or max(vals)*1.1}')
def meter(n,fig,v,pos=None):return el('gauge','meter',f'<b class="name">{n}</b><b class="fig">{fig}</b>',pos=pos,stylev=f'--v:{v}')
def frame(n,pos=None):return el('image-frame','frame',f'<div class="seat" data-ph="{n}"></div>',pos=pos)
def person(n,note,ph,pos=None,portrait=True):return el('person','person',f'<div class="seat'+(' portrait' if portrait else '')+f'" data-ph="{ph}"></div><b class="name">{n}</b><p class="note">{note}</p>',pos=pos)
def pill(n,note='',pos=None,cls=''):return el('pill','pill','<div class="parts"><b class="name">'+n+'</b>'+(f'<span class="note">{note}</span>' if note else '')+'</div>',cls,pos)
def table(heads,rows,pos=None):return el('table','tablebox','<table class="table"><thead><tr>'+''.join('<th>'+h+'</th>' for h in heads)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+v+'</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table>',pos=pos)
def donut(n,v,pos=None):return el('chart-donut','donut',f'<b class="fig">{v}<small>%</small></b><p class="name">{n}</p>',pos=pos,stylev=f'--v:{v}')
def shell(i,kicker,title,content,lead='',cover=False,where='at-left'):
 if cover:
  body=f'<section class="slide cover"><div class="page"><div class="lockup {where}"><p class="kicker">{kicker}</p><h1 class="title">{title}</h1><p class="lead">{lead}</p></div><div class="deco"></div><p class="meta"><span class="deck">MIRICOMPANY</span><span class="sec">이곳에 업무환경 개선안에 관한 간단한 설명을 입력해 보세요.</span><span class="src">www.miricompany.com</span><span class="label">미리컴퍼니 경영지원팀</span><span class="no">2080.03</span></p></div></section>'
 else:
  body=f'<section class="slide"><div class="page"><div class="top"><span class="deck">MIRICOMPANY</span><span class="sec">PROPOSAL BACKGROUND</span></div><header class="head"><p class="kicker">{kicker}</p><h1 class="title">{title}</h1>'+ (f'<p class="lead">{lead}</p>' if lead else '')+f'</header><div class="body">{content}</div><footer class="foot"><span class="src">미리컴퍼니 경영지원팀</span><span class="deck">www.miricompany.com</span><span class="no">2080.03</span></footer></div></section>'
 return f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>Skylight reassembled {i:02d}</title><link rel="stylesheet" href="../fonts/fonts.css"><link rel="stylesheet" href="collection.css"><style>{style}</style></head><body style="margin:0">{body}</body></html>'
P={}
P[1]=shell(1,'Workplace<br>Improvement Plan','바로 통과되는<br><b>업무환경 개선안</b>','',lead='이곳에 업무환경 개선안에 관한 간단한 설명을 입력해 보세요.',cover=True)
P[2]=shell(2,'CONTENTS','목차를 입력하세요',el('agenda','agenda',''.join(f'<div class="entry"><b class="mark">0{i+1}</b><p class="name">{n}</p><p class="note">해당 목차에 대한 간략한 내용을 입력해주세요.</p></div>' for i,n in enumerate(['추진 배경 및<br>현황 분석','문제점 도출 및<br>개선 목표','개선 방안','타사 사례 및<br>기대효과','추진 일정 및<br>예산 계획'])),pos=(1,1,12,6)))
P[3]=shell(3,'CHAPTER 01.','추진 배경 및 현황 분석','',lead='해당 항목의 핵심 내용을 입력해 보세요. 구체적인 실행 방법이나 목표를 포함해 보세요.',cover=True,where='at-center')
P[4]=shell(4,'제안 배경','해당 제안을 추진하게 된 배경과 제안의 필요성을 입력해 보세요.',group(card('제안<br>내용<br>요약',cls='quiet')+'<div class="stack">'+''.join(card(n,'• &nbsp; 해당 항목의 핵심 내용을 입력해 보세요.<br>• &nbsp; 구체적인 실행 방법이나 목표를 포함해 보세요.',cls='quiet') for n in ['현황','개선 방안','기대 효과'])+'</div>',(1,1,12,6),'split'))
caption=lambda t:el('prose','prose','<p><b>'+t+'</b></p>','quiet')
cs=group('<div class="group two"><div class="split">'+caption('연도별<br>업무 환경<br>개선 투자액')+bars([1900,1700,1500,1300,1200],['2075','2076','2077','2078','2090'],maxv=2000).replace('--max:2000','--max:2000;--skylight-axis-steps:4').replace('class="bar"','class="bar tone-1"').replace('class="bar on"','class="bar tone-1"')+'</div><div class="split">'+caption('변화 추이<br>그래프')+lines([15,12,8,6,3],['2075','2076','2077','2078','2079'],maxv=15).replace('--max:15','--max:15;--skylight-axis-steps:3').replace('class="pt on"','class="pt"').replace('</b>','%</b>')+'</div></div><div class="split">'+caption('핵심<br>키워드')+'<div class="stack">'+''.join(pill('#핵심 키워드',cls='on tone-'+str(i+1)) for i in range(3))+'</div></div>',(1,1,12,5),'split wide-left')+el('callout','callout','<span class="icon" data-icon="arrow-down"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v15m-6-6 6 6 6-6"/></svg></span><p>임직원 생산성 향상과 조직 경쟁력 확보를 위한 <b>선제적 투자 시점</b></p>',pos=(1,5,12,2))
P[5]=shell(5,'추진 배경','2060년 이후 업무 환경 개선 투자가 감소하며 시설 노후화 심화',cs,lead='이곳에 상위 문제나 원인을 입력해 보세요.')
cs=group(head('<b>분석 키워드</b>',cls='on center')+'<div class="stack">'+el('treemap','treemap','<div class="branch" style="--v:35"><b class="name"></b><div class="tile" style="--v:70"><b class="name">부족한 회의실</b><b class="fig">XX %</b></div><div class="tile" style="--v:30"><b class="name">키워드</b><b class="fig">XX %</b></div></div><div class="branch" style="--v:65"><b class="name"></b><div class="tile" style="--v:30"><b class="name">열악한 휴게실</b><b class="fig">XX %</b></div><div class="tile on" style="--v:70"><b class="name">노후 사무공간</b><b class="fig">XX %</b></div></div>')+el('prose','prose','<p>현재 업무 환경에 대한<br>구체적인 설명을 입력해 보세요.</p>','quiet')+'</div>',(1,1,4,6),'group col')
cs+=group(head('<b>디지털 환경</b>',cls='on center')+'<div class="stack">'+bars([40,70],['현재','필요수준'],maxv=80).replace('--max:80','--max:80;--skylight-axis-steps:4').replace('class="bar on"','class="bar tone-3"')+lst([('환경1','레거시 시스템 의존도가 높아 업무 효율성 저하'),('환경2','협업 툴 부재로 비효율 발생')])+'</div>',(5,1,4,6),'group col')
cs+=group(head('<b>업무 문화</b>',cls='on center')+lst([(n,'해당 키워드에 관한 현황 설명') for n in ['경직된 회의 문화','부족한 자율성','키워드 입력란']],cls='divided'),(9,1,4,6),'group col')
P[6]=shell(6,'현황 분석','현재 업무 환경 실태',cs,lead='이곳에 상위 문제나 원인을 입력해 보세요.')
q=el('quote','quote','<blockquote><p>“업무 툴의 불편함으로 효율적인<br>소통에 제약이 있어요.”</p><p>“회의 공간이 부족해<br>원활한 협업이 어려워요.”</p><p>“구체적이고 공감 가능한 불편사항<br>을 표현해 보세요.”</p></blockquote><div class="by"><b class="name">조사결과</b></div>')
ms=el('gauge','meter','<b class="name">업무 환경<br>개선 필요</b><b class="fig">72%</b>',stylev='--v:72;--skylight-meter-extent:78')+el('gauge','meter','<b class="name">조사<br>항목명</b><b class="fig">64%</b>',stylev='--v:64;--skylight-meter-extent:64')
hs=head('가장 불편한 요소','위 데이터에 대한<br>구체적인 설명이나<br>세부 내용을 입력해보세요.')+head('세부 분석 제목','위 데이터에 대한<br>구체적인 설명이나<br>세부 내용을 입력해보세요.')
cs=group('<div class="split"><div class="stack">'+ms+'</div><div class="stack">'+hs+'</div></div>'+q,(1,1,12,6),'split wide-left')
P[7]=shell(7,'현황 분석','직원 만족도 조사 결과',cs,lead='직원 만족도 조사의 핵심 결과를 간단하게 요약해 보세요.')
cs=group(card('환경적 요인','❶ &nbsp;10년 이상 노후 공간이 70% 차지<br>❷ &nbsp;환경적 요인으로 인한 주요 문제점을 입력하세요.')+card('제도적 요인','❶ &nbsp;제도적 요인으로 인한 주요 문제점을 입력하세요.<br>❷ &nbsp;제도적 요인으로 인한 주요 문제점을 입력하세요.'),(1,1,3,6),'stack')+group(head('<b>핵심 문제점</b>',cls='on center')+lst([('공간 효율성 저하','1인당 근무 면적 권장 기준 미달<br>문제의 구체적인 내용을 설명해 보세요.'),('시스템 노후화','업데이트 없는 업무 시스템 다수<br>문제의 구체적인 내용을 설명해 보세요.'),('경직된 근무 방식','문제의 구체적인 내용을 설명해 보세요.<br>문제의 구체적인 내용을 설명해 보세요.')],None,'num divided'),(4,1,5,6),'stack')+el('flowchart','flowchart','<div class="node end" style="grid-column:1;grid-row:1">생산성<br>저하로<br>이어지는<br>악순환<br>구조 형성</div>',pos=(9,1,4,6))
P[8]=shell(8,'문제점 도출','도출된 문제점의 핵심을 간단하게 요약해 보세요.',cs)
P[9]=shell(9,'개선 목표','개선을 통해 달성하고자 하는 최종 목표를 간단하게 요약해 보세요.',group(''.join(card(n,note) for n,note in [('쾌적한 물리적 환경 조성','노후 시설 교체 및 현대화<br>구체적인 목표 내용 입력란'),('디지털 업무 환경 고도화','통합 협업 플랫폼 구축<br>구체적인 목표 내용 입력란'),('세 번째 개선 목표','수평적 소통 문화 확립<br>구체적인 목표 내용 입력란')]),(1,1,12,2),'group three')+call('VISION<br><b>최종적으로 달성하고자 하는 비전을 입력해 보세요.</b>',(4,3,6,4)))
cs=head('물리적 환경 개선의 핵심 방향',pos=(1,1,4,1))+card('고정 좌석제를 자율 좌석제로<br>전환해 공간 활용도 향상',cls='tone-1',pos=(1,2,4,3))+card('협업 공간 30% 확충 및<br>다양한 업무 존 구성',cls='tone-2',pos=(1,4,4,3))+head('공간별 개선 계획',pos=(5,1,8,1),cls='on center')+group(''.join('<div class="stack">'+person(n,'해당 공간에 대한<br>설명을 입력해주세요.',i+1,portrait=False)+'</div>' for i,n in enumerate(['오픈 협업존','포커스존','라운지존'])),(5,2,8,5),'group three')
P[10]=shell(10,'개선 방안 : 물리적 환경','물리적 환경 개선의 핵심 방향과 목표를 간단하게 요약해 보세요.',cs)
cs=''
for i,n in enumerate(['레거시 시스템','통합 협업 플랫폼']):
 names=[['일반 메신저 사용','파일 공유 시 이메일 의존','개선 전 문제점 설명','개선 전 문제점 설명'],['메신저, 문서 통합 환경','개선 후 변화 내용 설명','클라우드 기반 실시간 협업','개선 후 변화 내용 설명']][i]
 cs+='<div class="group col">'+head('<b>'+n+'</b>' if i==0 else n,cls='on center')+el('matrix','matrix',''.join('<div class="cell'+(' on' if i else '')+'"><b class="name">'+('<small>'+z+'</small>' if len(z)>12 else z)+'</b><p class="note">해당 내용에 대한 설명을<br>간략하게 입력해주세요.</p></div>' for z in names))+'</div>'
P[11]=shell(11,'개선 방안 : 디지털 환경','디지털 환경 개선의 핵심 방향과 목표를 간단하게 요약해 주세요.',group(cs,(1,1,12,6),'split'))
ns=['회의 문화','의사결정','근무 방식','사내 복지','지원금 제도'];a=['주 평균 15시간의 비효율적 회의','다단계 결재로 처리 지연 (평균 X일)']+['이곳에 현재의 업무 문화를 설명해 보세요.']*3;b=['회의 시간 50% 단축 및 사전 아젠다 필수화','결재 단계 축소 및 권한 위임 확대','이곳에 개선 후 변화 내용을 입력해 보세요.']+['이곳에 현재의 업무 문화를 설명해 보세요.']*2
cs=''
for x,t,vals,pick in [(1,'개선<br>사항',a,''),(7,'개선 후<br>모습',b,'pick')]:
 cs+=el('table','tablebox','<table class="table"><thead><tr><th colspan="2" class="'+pick+'">'+t+'</th></tr></thead><tbody>'+''.join('<tr><th>'+n+'</th><td>'+v+'</td></tr>' for n,v in zip(ns,vals))+'</tbody></table>',pos=(x,1,6,6))
P[12]=shell(12,'개선 방안 : 업무 문화 개선','업무 문화 개선의 핵심방향과 목표를 간단하게 요약해 보세요.',cs)

desc='이곳에 개선 전 환경을 설명해 보세요. 업무 비효율이 발생한 원인과 개선이 필요한 여지에 대해 서술해 보세요.'
photo=lambda n:el('image-frame','frame',f'<div class="seat portrait" data-ph="{n}"></div>')
textnote=lambda:el('prose','prose','<p>'+desc+'</p>','quiet')
cs=group('<div class="stack">'+head('<b>개선 전</b>',cls='on center')+photo(1)+textnote()+'</div><div class="stack">'+head('개선 후',cls='on center')+'<div class="group">'+''.join('<div class="stack">'+photo(i+2)+textnote()+'</div>' for i in range(3))+'</div></div>',(1,1,12,6),'split')
P[13]=shell(13,'개선 전후 비교 예상','개선 전후 비교의 핵심 변화를 간단하게 요약해 보세요.',cs)
cs=el('gauge','meter','<b class="name">협업 효율성<br>변화율</b><b class="fig">58%</b>',pos=(3,1,8,2),stylev='--v:58;--skylight-meter-extent:51')+el('gauge','meter','<b class="name"></b><b class="fig">86%</b>',pos=(3,1,8,2),stylev='--v:86;--skylight-meter-extent:100')+head('XX%<br>차이',pos=(10,1,2,2),cls='center')
quant=el('table','tablebox','<table class="table"><thead><tr><th colspan="2">정량적<br>변화</th></tr></thead><tbody>'+''.join('<tr><th>'+str(1 if i==0 else 2)+'</th><td><b>'+n+'</b><p>구체적인 변화 내용을 입력해 보세요.</p></td></tr>' for i,n in enumerate(['업무 처리 속도 평균 40% 단축','정량적 변화를 입력해주세요.','정량적 변화를 입력해주세요.']))+'</tbody></table>')
qual=el('table','tablebox','<table class="table"><thead><tr><th colspan="2" class="pick">정성적<br>변화</th></tr></thead><tbody>'+''.join('<tr><th>keyword</th><td>눈에 보이는 변화에 대해<br>설명해 보세요.</td></tr>' for i in range(3))+'</tbody></table>')
cs+=group('<div class="split">'+quant+qual+'</div><div class="stack">'+head('<b>“일하고 싶은<br>직장으로 거듭나는<br>실질적 변화”</b>',cls='on center')+'</div>',(1,3,12,4),'split wide-left')
P[14]=shell(14,'개선 전후 비교 예상','개선 전후 비교의 핵심 변화를 간단하게 요약해 보세요.',cs)
cs=call('연쇄적인 효과들이 만들어내는 <b>궁극적 결과</b>를 입력해 보세요.',(4,1,6,1))+el('venn','venn','<div class="set"><b class="name">생산성 향상<br><small>효율적인 업무 환경으로 직<br>원 1인당 생산성 20% 향상</small></b></div><div class="set on"><b class="name">인재 경쟁력<br><small>우수 인재 유치 및<br>이직률 30% 감소 예상</small></b></div>',pos=(1,1,12,6))+el('steps','steps',''.join(f'<div class="step"><b class="mark"></b><b class="name">{n}</b></div>' for i,n in enumerate(['업무 효율<br>증대','직원<br>만족도 향상','조직<br>경쟁력 강화'])),pos=(4,4,6,3))
P[15]=shell(15,'기대효과','기대효과의 핵심 내용을 간단하게 요약해 보세요.',cs)
cs=''
for i,(n,note) in enumerate([('직원 만족도 향상','쾌적한 환경으로 업무 몰입도 증가<br>직원 만족도 지수 35% 향상'),('운영 효율성 확대','디지털화를 통한 프로세스 간소화<br>행정 업무 시간 30% 단축'),('기업 이미지 및 브랜드 가치 향상','혁신적 업무 환경으로 브랜드 가치 향상<br>ESG 경영 실천 사례로 대외 인지도 제고'),('효과 영역 키워드','해당 영역의 기대효과에 대한 설명을 간략하게 입력해주세요.')]):
 cs+=person(n,note,i+1,(1+(i%2)*6,1+(i//2)*3,6,3))
P[16]=shell(16,'기대효과','기대효과의 핵심 내용을 간단하게 요약해 보세요.',cs+card('통합적<br>시너지 효과',cls='on',pos=(6,2,2,3)))
cs='<div class="tablebox" data-el="skylight-table" style="grid-column:1 / span 12; grid-row:1 / span 6"><table class="table"><thead><tr><th>추진<br>일정</th><th>Q1</th><th>Q2</th><th>Q3</th><th>Q4</th><th>다음해 상반기</th></tr></thead><tbody><tr><th>추진<br>일정</th><td><b>계획 수립</b><strong>업무 환경 개선<br>TF 구성</strong><p>직원 의견 수렴 및 요구 분석</p></td><td><b>설계 및 준비</b><strong>주요 추진 내용<br>입력란</strong><p>직원 의견 수렴 및 요구 분석</p></td><td><b>단계별 키워드</b><strong>주요 추진 내용<br>입력란</strong><p>직원 의견 수렴 및 요구 분석</p></td><td><b>단계별 키워드</b><strong>주요 추진 내용<br>입력란</strong><p>직원 의견 수렴 및 요구 분석</p></td><td><b>안정화</b><strong>주요 추진 내용<br>입력란</strong><p>직원 의견 수렴 및 요구 분석</p></td></tr><tr><th>점검 사항</th><td>직원 의견 수렴 및 요구 분석</td><td>예산 확정 및 업체 선정</td><td>주의 및 점검 사항 입력</td><td>주의 및 점검 사항 입력</td><td>주의 및 점검 사항 입력</td></tr></tbody></table></div>'
P[17]=shell(17,'추진 일정','추진 일정의 전체 기간과 목표를 간단하게 요약해 보세요.',cs)
cs=lst([('예산 분배','공간 개선에 전체 예산의 40% 집중 투자'),('예산 규모','예산 배분 원칙이나 방향을 입력해 보세요.'),('투자 방향','예산 배분 원칙이나 방향을 입력해 보세요.')],(1,1,8,4),'num divided')+table(['항목','예산','비고'],[['텍스트공간개선','X억원','-'],['디지털 인프라 구축','X억원','-'],['','','']],(1,4,8,3))+head('예산 분배','공간 개선에 전체 예산의 40% 집중 투자',pos=(9,1,4,2),cls='center')+''.join(el('chart-donut','donut',f'<b class="fig">{v}</b><p class="name">{n}</p>',f'quiet tone-{i+1}',pos=(9,1,4,6),stylev=f'--v:{v};--skylight-donut-start-angle:{a}deg;--skylight-donut-key:{i}') for i,(n,v,a) in enumerate([('공간 개선',30,0),('디지털 인프라',30,108),('제도 및 운영',30,216),('예비비',10,324)]))
P[18]=shell(18,'예산 계획','예산 규모와 투자 방향을 간단하게 요약해 보세요.',cs)
cs=el('person','people',''.join(person(n,note,i+1) for i,(n,note) in enumerate([('김미리 <small>상무</small>','전체 총괄 및 의사결정,<br>예산 승인'),('이미리 <small>팀장</small>','물리적 환경 설계 및<br>시공 관리'),('최미리 <small>직책</small>','이곳에 담당 역할을<br>설명해 보세요.'),('박미리 <small>직책</small>','이곳에 담당 역할을<br>설명해 보세요.'),('권미리 <small>직책</small>','이곳에 담당 역할을<br>설명해 보세요.'),('심미리 <small>직책</small>','이곳에 담당 역할을<br>설명해 보세요.')])),pos=(1,1,12,6))
P[19]=shell(19,'담당 조직 및 역할','업무 환경 개선 TF <small>담당 조직 구성과 운영 방식을 간단하게 요약해 보세요.</small>',cs)
emptline=el('chart-line','lines',''.join(f'<div class="pt" style="--v:{v}"><b></b><span></span></div>' for v in [50,40,30,20,15]),stylev='--max:50')
cs=group('<div class="split">'+card('B사 스마트<br>오피스 전환<br>프로젝트','6개월 프로젝트<br>투자비 X억 원',cls='quiet')+'<div class="stack">'+lst([('2078년 본사 업무 공간 전면 리뉴얼','구체적인 변화 내용을 입력해 보세요.'),('6개월 만에 생산성 28% 향상 달성','구체적인 변화 내용을 입력해 보세요.'),('개선 세부 내용','구체적인 변화 내용을 입력해 보세요.')],cls='num')+el('steps','steps','<div class="step"><b class="mark"></b><b class="name">고정 좌석,<br>칸막이 사무실</b></div><div class="step"><b class="mark"></b><b class="name">자율좌석,<br>개방형 협업 공간</b></div>')+'</div></div><div class="stack">'+head('B사 생산성 및 퇴사자 추이',cls='center')+'<div class="group two"><div class="stack">'+bars([50,40,30,20,15],['1Q','2Q','3Q','4Q','5Q'],maxv=50).replace('--max:50','--max:50;--skylight-axis-steps:5').replace('class="bar"','class="bar tone-2"').replace('class="bar on"','class="bar tone-2"')+'</div><div class="stack">'+emptline+'</div></div><div class="group">'+''.join(el('image-frame','frame',f'<div class="seat portrait" data-ph="{i+1}"></div>') for i in range(3))+'</div></div>',(1,1,12,6),'split')
P[20]=shell(20,'타사 환경 개선 사례','타사 사례 분석의 목적과 핵심 내용을 간단하게 요약해 보세요.',cs)
P[21]=shell(21,'THANK YOU','',head('감사합니다.','프로젝트의 의미와 당부를 담은 두세줄 정도의 마무리 문장을 입력해 보세요.',pos=(1,1,10,3),cls='big')+el('prose','prose',''.join('<p><b>'+n+'</b>'+v+'</p>' for n,v in [('TEL.','02-0000-0000'),('E-MAIL','CONTACT@MIRIDIH.COM'),('ADDRESS','미리시 미리구 미리로 123'),('HOME','WWW.MIRIDIH.COM')]),'quiet',pos=(8,3,5,4)))
for i,h in P.items():(R/f'slide_{i:02d}.html').write_text(re.sub(r'data-ph="[^"]*"','data-ph=""',h))
(R/'index.html').write_text('<!doctype html><meta charset="utf-8"><h1>Skylight reassembled</h1>'+''.join(f'<p><a href="slide_{i:02d}.html">Slide {i:02d}</a></p>' for i in P))
print('reassembled',len(P))
