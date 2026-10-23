from pathlib import Path
import json,re
P=Path(__file__).parent;C=P/'vectorbox';O=P/'reassembled';O.mkdir(exist_ok=True);A=P/'assets';A.mkdir(exist_ok=True)
(A/'fonts.css').write_text("@font-face{font-family:'Pretendard Variable';src:url('../replica/fonts/PretendardVariable.woff2');font-weight:100 900}@font-face{font-family:'Montserrat';src:url('../replica/fonts/Montserrat.woff2');font-weight:100 900}")
(A/'type-steps.css').write_text('.slide{'+''.join(f'--type-{n}:{n}px;' for n in json.loads(Path('/workspace/work/reference/contract/type-steps.json').read_text()))+'}')
pal=json.loads(Path('/workspace/work/reference/contract/palette.json').read_text());vals=pal['light'];vals['--a1']='#2863e7';vals['--a1-on']='#ffffff';vals['--page']='#ffffff';vals['--ink']='#000000';vals['--a2']='#000000';vals['--a2-on']='#ffffff'
import colorsys
for i in range(1,10):
 for suf in ['', '-soft','-muted']:
  # Source style is supplied independently of role-only collection CSS.
  t=(i-1)/8; rgb=colorsys.hls_to_rgb(.62,.97-.73*t,.65 if suf else .8)
  vals[f'--a1-{i}{suf}']='#'+''.join(f'{round(x*255):02x}' for x in rgb)
vals['--a1-7']='#2863e7';vals['--a1-3-soft']='#dfe8fb';vals['--a1-4-soft']='#8dabef'
(A/'source-palette.css').write_text('.slide{'+''.join(f'{k}:{v};' for k,v in vals.items())+'}')
def slot(c,r,w,h):return f'style="grid-column:{c} / span {w};grid-row:{r} / span {h}"'
def el(k,cls,inside,c=1,r=1,w=12,h=6,extra=''):
 return f'<div class="{cls}" data-el="vectorbox-{k}" {slot(c,r,w,h)} {extra}>{inside}</div>'
def icon(n):return f'<span class="icon" data-icon="{n}"></span>'
def card(name,note,ic='',variant=''):
 return f'<div class="card {variant}" data-el="vectorbox-card"><div class="parts">'+(f'<span class="mark">{icon(ic)}</span>' if ic else '')+f'<p class="name">{name}</p><p class="note">{note}</p></div></div>'
def group(items,c=1,r=1,w=12,h=6):return f'<div class="group" {slot(c,r,w,h)}>'+''.join(items)+'</div>'
def prose(s,c,r,w,h):return el('prose','prose','<p>'+s+'</p>',c,r,w,h)
pages={}
# Preserve original order and source text, including obvious source spelling errors.
items=['프로젝트 개요','시장 분석','핵심 전략','핵심 기능','경쟁력','기대 효과','프로젝트 절차','예산 계획']
pages['02']=('CONTENTS','목차',el('agenda','agenda',''.join(f'<div class="entry"><span class="mark">{i+1:02}</span><p class="name">{x}</p></div>' for i,x in enumerate(items)),1,1,9,6),0)
pages['03']=('PROJECT OVERVIEW','MIRI PROJECT',prose('시장 환경과 고객 요구를 분석하여<br>효율적인 비즈니스 솔루션을 제안합니다.',1,1,10,1)+group([card(n,t,ic,'line') for n,t,ic in [('프로젝트 목적','고객의 문제를 정의하고<br>해결 방안을 제시합니다.','target'),('주요 대상','핵심 고객과 이해 관계자를<br>분석합니다.','users'),('기대 성과','정량적, 정성적 성과를<br>예상합니다.','chart-no-axes-combined'),('추진 방향','전략적 실행 방향과<br>계획을 수립합니다.','rocket')]],1,2,12,5),1)
bars=''.join(f'<div class="bar {"on" if i%2==0 else "tone-2"}" style="--v:{v}"><b>{v}</b><span>{2023+i//2}</span></div>' for i,v in enumerate([35,22,60,30,73,39,85,48]))
pages['04']=('MARKET ANALYSIS','시장 분석',el('legend','legend','<span class="key tone-1">시장 규모(억)</span><span class="key tone-2">고객 수(만 명)</span>',1,1,7,1)+el('chart-bar','bars',bars,1,2,7,5, 'style="--max:100"')+el('metric','stat','<div class="parts"><b class="fig">85<small>%</small></b><p class="name">고객 만족도</p></div>',9,1,2,3)+el('card','card line','<div class="parts"><span class="mark">'+icon('medal')+'</span></div>',11,1,2,3)+el('metric','stat','<div class="parts"><b class="fig">42<small>%</small></b><p class="name">연간 성장률</p></div>',9,4,2,3)+el('card','card line','<div class="parts"><span class="mark">'+icon('chart-line')+'</span></div>',11,4,2,3),2)
# Correct chart root has one style attribute containing placement and numeric data.
pages['04']=(pages['04'][0],pages['04'][1],pages['04'][2].replace('grid-row:2 / span 5" style="--max:100"','grid-row:2 / span 5;--max:100"').replace('<div class="group" style="grid-column:9 / span 4;grid-row:1 / span 6">','<div class="stack" style="grid-column:9 / span 4;grid-row:1 / span 6">'),2)
pages['05']=('KEY STRATEGY','핵심 전략',group([card(n,t,ic,'quiet') for n,t,ic in [('시장 분석','고객의 문제를 정의하고<br>해결 방안을 제시합니다.','file-pen-line'),('사용자 중심','핵심 고객과 이해 관계자를<br>분석합니다.','user-search'),('표율적인 운영','정량적, 정성적 성과를<br>예상합니다.','settings'),('지속적인 성장','전략적 실행 방향과<br>계획을 수립합니다.','refresh-cw')]]),3)
hub='<div class="core"><b class="name">통합 솔루션</b></div>'
for n,t,ic in [('자동화 기능','반복 업무 자동화 및 워크플로우 최적화','cpu'),('프로젝트 관리','업무 일정 및 진행상황 체계적 관리','clipboard-check'),('성과 측정','실시간 KPI 모니터링 및 성과 분석','hand-coins'),('협업 시스템','팀원 간 효율적인 커뮤니케이션 지원','messages-square')]:hub+=f'<div class="spoke"><span class="mark">{icon(ic)}</span><p class="name">{n}</p><p class="note">{t}</p></div>'
pages['06']=('KEY FEATURE','핵심 기능',el('hub','hub',hub),4)
rows=[['업무 효율','X','O','업무 처리 시간 단축'],['관리 편의성','X','O','직관적인 관리 기능'],['데이터 분석','O','O','실시간 데이터 분석'],['확장성','X','O','유연한 시스템 확장'],['비용 효율','X','O','운영 비용 절감 효과']]
table='<table class="table"><thead><tr>'+''.join(f'<th class="{"pick" if i==2 else ""}">{t}</th>' for i,t in enumerate(['항목','기존 방식','제안 솔루션','비고']))+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td class="{"pick" if i==2 else ""}">{t}</td>' for i,t in enumerate(row))+'</tr>' for row in rows)+'</tbody></table>'
pages['07']=('COMPETITIVENESS','경쟁력',el('table','tablebox',table),5)
pages['08']=('EXPETED RESULTS','기대 효과',group([card(n,t,ic) for n,t,ic in [('업무 효율 향상','프로세스 간소화를 통해 업무 처리 속도를 향상시킵니다.','lightbulb'),('비용 절감','중복 업무를 줄여 운영 비용을 절감하고 수익성을 높입니다.','receipt'),('데이터 기반','실시간 데이터 분석으로 빠르고 정확한 의사결정을 지원합니다.','chart-pie'),('고객 만족도','사용자 경험 개선으로 고객 만족도를 극대화합니다.','badge-check')]]),6)
steps=''
for i,(n,t,ic) in enumerate([('기획','프로젝트 목표 정의 및 계획 수립','lightbulb'),('분석','시장 및 고객 분석 요구사항 정의','clipboard-check'),('설계','서비스 구조 설계 UI/UX 설계','pencil-ruler'),('개발','시스템 개발 및 기능 구현','monitor-cog'),('테스트','품질 검증 및 사용성 테스트','triangle-alert'),('오픈','서비스 오픈 및 운영 시작','rocket')]):steps+=f'<div class="step"><span class="mark">{icon(ic)}</span><p class="kick">{i+1:02}</p><p class="name">{n}</p><p class="note">{t}</p></div>'
pages['09']=('KEY STRATEGY','프로젝트 절차',el('steps','steps',steps),7)
pages['10']=('BUDGET PLAN','예산 계획',el('chart-donut','donut','<b class="fig">25<small>%</small></b><p class="name">기획</p>',1,1,5,6, 'style="--v:25"')+el('legend','legend',''.join(f'<span class="key tone-{i+1 if i<4 else 5}">{x} 25%</span>' for i,x in enumerate(['기획','개발','디자인','테스트','유지보수','기타'])),6,1,2,6)+el('card','card','<div class="parts"><p class="name">효율적인 예산 운영</p><p class="note">각 단계별 최적의 자원 배분을 통해 프로젝트의 성공을 지원합니다.</p><span class="mark">'+icon('coins')+'</span></div>',9,1,4,6),8)
pages['10']=(pages['10'][0],pages['10'][1],pages['10'][2].replace('grid-row:1 / span 6" style="--v:25"','grid-row:1 / span 6;--v:25"'),8)
pages['11']=('Q&A','질의응답',el('callout','callout',icon('message-square')+'<p>궁금하신 사항이 있으시면<br>편하게 질문해 주세요.</p>'+icon('mic'),2,2,10,4),0)
contact='<div class="seat portrait" data-ph="1"></div><p class="name">담당자 · 김미리</p><p class="note">영업 1팀 / 팀장</p>'
contactlist=''
for n,t,ic in [('전화','123-456-789','phone'),('홈페이지','www.website.com','globe'),('이메일','email@email.com','mail'),('회사주소','미리도 미리시 미리구 미리동 1234','map-pin'),('팩스','123-456-789','printer')]:contactlist+=f'<div class="item"><span class="mark">{icon(ic)}</span><p class="name">{n}</p><p class="note">{t}</p></div>'
pages['12']=('CONTACT','문의 및 연락',el('person','person',contact,1,1,3,6)+el('list','list divided',contactlist,5,1,8,6),0)
pages['13']=('BUSINESS PROPOSAL','',el('headline','headline big','<h2><b>경청해주셔서</b><br>감사합니다</h2><p class="note">최적의 전략과 체계적인 실행으로 퍼포먼스를 보여드리겠습니다.</p>',1,1,9,4)+prose('MIRI COMPANY<br>email@email.com',1,5,6,2)+el('image-frame','frame','<div class="seat portrait" data-ph="1"></div>',11,1,2,4)+el('image-frame','frame','<div class="seat" data-ph="2"></div>',9,5,3,2),0)
links=['../assets/fonts.css','../assets/type-steps.css','../vectorbox/kit/css/tokens.css','../assets/source-palette.css','../vectorbox/foundation/foundation.css']+['../vectorbox/elements/'+p.name+'/element.css' for p in sorted((C/'elements').iterdir())]
for no,(kick,title,body,dot) in pages.items():
 nav='<div class="idx">'+''.join(f'<span class="no {"on" if i==dot else ""}"></span>' for i in range(1,9))+'</div>' if dot else ''
 html='<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>Vectorbox · 069 '+no+'</title>'+''.join(f'<link rel="stylesheet" href="{x}">' for x in links)+'</head><body style="margin:0"><section class="slide"><div class="page"><header class="head"><p class="kicker">'+kick+'</p><h1 class="title">'+title+'</h1></header><div class="body">'+body+'</div>'+nav+'</div></section></body></html>'
 (O/f'slide_{no}.html').write_text(html)
print('Reassembled',len(pages),'pages using collection-only layout')
