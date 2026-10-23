from pathlib import Path
from html import escape
P=Path(__file__).parent; R=P/'replica'; R.mkdir(exist_ok=True)
icons={
 'target':'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="3"/><path d="M12 12 23 1m-1 0v4h4m-7-3v5h5"/>',
 'users':'<circle cx="5" cy="8" r="2.5"/><circle cx="12" cy="10" r="2.5"/><circle cx="19" cy="8" r="2.5"/><path d="M.5 18v-1c0-5 9-5 9 0m5 0c0-5 9-5 9 0v1m-16 2v-1c0-5 9-5 9 0v1"/>',
 'chart':'<path d="M2 2v20h20M5 18l5-7 5 3L21 4m-4 0h4v4"/>',
 'rocket':'<path d="M9 7c4-5 8-6 13-5 1 5-1 10-6 14l-5-1-3-4Zm3 8-3 5-4-1 1-4m-1-1-3 4m0 4 5-5m4 1-4 4M9 7l-6 1 1 4m12 4-1 6-4-1"/><circle cx="15.5" cy="8" r="2"/>',
 'file':'<rect x="3" y="2" width="16" height="19" rx="1.5"/><path d="M6 6h10M6 10h10M6 14h8M6 18h5m2 4 2-6 6-6 3 3-6 6-5 3"/>',
 'search':'<circle cx="10" cy="10" r="8"/><circle cx="10" cy="9" r="3"/><path d="M5 16v-1c0-5 10-5 10 0v1m1 1 6 6 2-2-6-6"/>',
 'gear':'<path d="m10 2 1-1h3l1 2 3 1 2-1 2 3-1 2 1 3 2 1v3l-2 1-1 3 1 2-3 2-2-1-3 1-1 2h-3l-1-2-3-1-2 1-2-3 1-2-1-3-2-1v-3l2-1 1-3-1-2 3-2 2 1Z"/><circle cx="12" cy="12" r="4"/>',
 'refresh':'<path d="M21 7A10 10 0 0 0 3 9M3 9V4M3 9h5m-5 8a10 10 0 0 0 18-2m0 0v5m0-5h-5"/>',
 'clipboard':'<rect x="4" y="3" width="16" height="20" rx="1.5"/><rect x="9" y="1" width="6" height="4" rx="1"/><path d="m7 9 1 1 2-2m2 1h5M7 14l1 1 2-2m2 1h5M7 19l1 1 2-2m2 1h5"/>',
 'layers':'<path d="m4 3-2 6h20l-2-6Zm0 6-2 6h20l-2-6M4 15l-2 6h20l-2-6"/>',
 'message':'<path d="M3 3h18v13H13l-3 5-2-5H3Z M7 7h10M7 11h7"/>',
 'lightbulb':'<path d="M8 19h8m-7 3h6M8 16c0-3-3-4-3-8a7 7 0 0 1 14 0c0 4-3 5-3 8Zm4-18v-3M2 7h-3m26 0h-3M4 0 2-2m18 2 2-2"/>',
 'receipt':'<path d="M5 1h14v22l-2-2-2 2-2-2-2 2-2-2-2 2-2-2ZM8 5h8M8 8h8M8 11h8M8 16h8m-7-2 2 6 2-6 2 6 2-6"/>',
 'pie':'<circle cx="12" cy="12" r="10"/><path d="M12 2v10l-9 5"/>',
 'badge':'<path d="M9 3c1-4 5-4 6 0 4-2 7 1 5 5 4 1 4 6 0 7 2 4-1 7-5 5-1 4-6 4-7 0-4 2-7-1-5-5-4-1-4-6 0-7-2-4 1-7 6-5Z"/><path d="m7 12 4 4 7-8"/>',
 'ruler':'<path d="m2 5 3-3 17 17-3 3ZM7 7l2-2m3 7 2-2m3 7 2-2M3 22l1-6L20 0l4 4L8 20Z"/>',
 'monitor':'<rect x="1" y="2" width="22" height="15" rx="1"/><path d="M8 21h8m-4-4v4"/><circle cx="9" cy="9" r="3"/><circle cx="17" cy="6" r="2"/>',
 'shield':'<path d="m3 7 9-7 9 7v16H3Zm9 2-6 10h12Z M12 12v3m0 2h.01"/>',
 'coins':'<ellipse cx="9" cy="5" rx="7" ry="3"/><path d="M2 5v12c0 4 14 4 14 0V5M2 9c0 4 14 4 14 0M2 13c0 4 14 4 14 0M17 4c7-2 9 3 4 5m-4 1c7 1 7 5 0 6m0 1c7 1 7 5 0 6"/>',
 'mic':'<rect x="8" y="1" width="8" height="15" rx="4"/><path d="M5 11v2a7 7 0 0 0 14 0v-2m-7 9v4m-4 0h8M8 6h3m-3 4h3"/>',
 'medal':'<path d="M6 1h12l-2 10M6 1l2 10M9 1l1 9m5-9-1 9"/><circle cx="12" cy="16" r="7"/><circle cx="12" cy="16" r="5"/>',
 'phone':'<path d="M5 2c2-1 5 3 4 5L7 9c2 4 4 6 8 8l2-2c2-1 6 2 5 4l-2 3C10 23 0 13 2 4Z"/>',
 'mail':'<rect x="1" y="4" width="22" height="16" rx="1"/><path d="m2 5 10 8L22 5M1 20l8-8m14 8-8-8"/>',
 'globe':'<circle cx="12" cy="12" r="11"/><ellipse cx="12" cy="12" rx="5" ry="11"/><path d="M1 12h22M3 5h18M3 19h18"/>',
 'pin':'<path d="M19 8c0 6-7 12-7 12S5 14 5 8a7 7 0 0 1 14 0Z"/><circle cx="12" cy="8" r="2"/><path d="m5 16-4 5 11 3 11-3-4-5"/>',
 'fax':'<rect x="6" y="1" width="12" height="15"/><path d="m9 8 2 2 4-4M6 11H2v12h20V11h-4M6 20h12"/>',
 'portrait':'<rect x="4" y="1" width="16" height="22" rx="1.5"/><circle cx="12" cy="12" r="4" fill="currentColor" stroke="none"/><path d="M5 23c1-8 13-8 14 0" fill="currentColor" stroke="none"/><path d="M10 4h4"/>'}
def icon(key,size=100,color='#2863e7'):
 return f'<svg width="{size}" height="{size}" viewBox="-2 -3 28 29" style="color:{color}" fill="none" stroke="currentColor" stroke-width=".9" stroke-linecap="round" stroke-linejoin="round">{icons[key]}</svg>'
def at(x,y,w,h,content='',cls='',style=''):
 return f'<div class="abs {cls}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{style}">{content}</div>'
def text(x,y,w,h,s,size=24,weight=400,color='#000',align='left',extra=''):
 return at(x,y,w,h,s,'text',f'font-size:{size}px;font-weight:{weight};color:{color};text-align:{align};{extra}')
def box(x,y,w,h,s='',blue=True,cls=''):
 c='#2863e7' if blue else '#000';return at(x,y,w,h,s,'selection '+('blue ' if blue else 'black ')+cls,f'--box:{c};')
def head(k,title='',dot=0):
 s=at(62,63,8,44,'','', 'background:#2863e7')+text(98,73,740,32,k,20,600,extra="font-family:'Montserrat'")
 if title:s+=text(98,149,1100,74,title,60,850,extra='letter-spacing:-1.5px')
 if dot:s+=at(998,71,220,20,''.join(f'<i style="background:{"#2863e7" if i==dot else "#f0f0f0"}"></i>' for i in range(1,9)),'dots')
 return s
pages={}
# Contents
s=head('CONTENTS','목차')
for col,names in enumerate([['프로젝트 개요','시장 분석','핵심 전략','핵심 기능'],['경쟁력','기대 효과','프로젝트 절차','예산 계획']]):
 for i,name in enumerate(names):s+=text(189+col*360,263+i*89,60,50,f'{col*4+i+1:02}',36,600,'#2863e7')+text(262+col*360,269+i*89,310,40,name,26,650)
s+=box(1065,182,350,478)+box(892,544,340,260);pages['02']=s
# Overview
s=head('PROJECT OVERVIEW','MIRI PROJECT',1).replace('font-size:60px;font-weight:850;color:#000;text-align:left;letter-spacing:-1.5px','font-size:52px;font-weight:750;color:#000;text-align:left;letter-spacing:-1px;font-family:Montserrat')+text(98,235,760,70,'시장 환경과 고객 요구를 분석하여<br>효율적인 비즈니스 솔루션을 제안합니다.',25,450,extra='line-height:1.4')
for i,(ic,name,note) in enumerate([('target','프로젝트 목적','고객의 문제를 정의하고<br>해결 방안을 제시합니다.'),('users','주요 대상','핵심 고객과 이해 관계자를<br>분석합니다.'),('chart','기대 성과','정량적, 정성적 성과를<br>예상합니다.'),('rocket','추진 방향','전략적 실행 방향과<br>계획을 수립합니다.')]):
 x=126+i*282;s+=box(x,344,176,175,icon(ic,122),False,'center')+text(x-40,539,256,37,name,27,700,'#2863e7','center')+text(x-45,577,266,65,note,23,450,align='center',extra='line-height:1.35')
pages['03']=s
# Market
s=head('MARKET ANALYSIS','시장 분석',2)
s+=at(314,270,18,18,'','','background:#2863e7;border-radius:5px')+text(335,267,115,28,'시장 규모(억)',18)+at(438,270,18,18,'','','background:#000;border-radius:5px')+text(460,267,150,28,'고객 수(만 명)',18)
for j in range(6):
 y=601-j*55.6;s+=at(150,y,609,1,'','','background:#d4d4d4')+text(101,y-13,41,26,str(j*20),18,450,align='right')
for i,(a,b) in enumerate([(35,22),(60,30),(73,39),(85,48)]):
 x=168+i*152;s+=at(x,601-a*2.78,50,a*2.78,'','','background:#2863e7')+at(x+67,601-b*2.78,50,b*2.78,'','','background:#000')+text(x+1,608,118,30,str(2023+i),20,450,align='center')
for y,v,ic,lab,c in [(183,85,'medal','고객 만족도','#2863e7'),(427,42,'chart','연간 성장률','#000')]:
 s+=at(825,y,159,159,f'<b>{v}<small>%</small></b>','burst',f'background:{c}')+box(960,y-9,175,175,icon(ic,109,c),c!='#000','center')+text(959,y+174,176,32,lab,23,450,align='center')
pages['04']=s
# Strategy
s=head('KEY STRATEGY','핵심 전략',3)
for i,(ic,name,note) in enumerate([('file','시장 분석','고객의 문제를 정의하고<br>해결 방안을 제시합니다.'),('search','사용자 중심','핵심 고객과 이해 관계자를<br>분석합니다.'),('gear','표율적인 운영','정량적, 정성적 성과를<br>예상합니다.'),('refresh','지속적인 성장','전략적 실행 방향과<br>계획을 수립합니다.')]):
 x=99+i*284;s+=at(x,256,229,229,icon(ic,142,'#000'),'ring center')+text(x-25,512,279,40,name,27,700,'#2863e7','center')+text(x-20,561,269,65,note,23,450,align='center',extra='line-height:1.35')
pages['05']=s
# Feature
s=head('KEY FEATURE','핵심 기능',4)+at(464,270,352,326,'','feature-square')+at(534,326,215,215,icon('layers',107,'#fff')+'<b>통합 솔루션</b>','core')
for x,y,ic,name,note,left in [(409,218,'gear','자동화 기능','반복 업무 자동화 및<br>워크플로우 최적화',True),(737,218,'clipboard','프로젝트 관리','업무 일정 및 진행상황<br>체계적 관리',False),(409,509,'users','협업 시스템','팀원 간 효율적인<br>커뮤니케이션 지원',True),(737,509,'file','성과 측정','실시간 KPI 모니터링<br>및 성과 분석',False)]:
 s+=at(x,y,137,137,icon(ic,100,'#fff'),'blue-circle center')
 tx=x-228 if left else x+154;align='right' if left else 'left'
 s+=text(tx,y+24,208,40,name,28,750,'#2863e7',align)+text(tx,y+69,212,62,note,23,450,align=align,extra='line-height:1.3')
pages['06']=s
# Competition
s=head('COMPETITIVENESS','경쟁력',5)
rows=[['업무 효율','X','O','업무 처리 시간 단축'],['관리 편의성','X','O','직관적인 관리 기능'],['데이터 분석','O','O','실시간 데이터 분석'],['확장성','X','O','유연한 시스템 확장'],['비용 효율','X','O','운영 비용 절감 효과']]
s+=at(107,245,1065,397,'<table><thead><tr>'+''.join(f'<th>{x}</th>' for x in ['항목','기존 방식','제안 솔루션','비고'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{x}</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>','competition')
pages['07']=s
# Results
s=head('EXPETED RESULTS','기대 효과',6)
for i,(ic,name,note) in enumerate([('lightbulb','업무 효율 향상','프로세스 간소화를 통해<br>업무 처리 속도를<br>향상시킵니다.'),('receipt','비용 절감','중복 업무를 줄여<br>운영 비용을 절감하고<br>수익성을 높입니다.'),('pie','데이터 기반','실시간 데이터 분석으로<br>빠르고 정확한 의사결정을<br>지원합니다.'),('badge','고객 만족도','사용자 경험 개선으로<br>고객 만족도를<br>극대화합니다.')]):
 x=91+i*284;s+=box(x,244,245,394)+at(x+50,299,145,132,icon(ic,132),'center')+text(x+5,459,235,44,name,29,750,'#2863e7','center')+text(x+7,510,231,110,note,23,450,align='center',extra='line-height:1.32')
pages['08']=s
# Process
s=head('KEY STRATEGY','프로젝트 절차',7)
for i,(ic,name,note) in enumerate([('lightbulb','기획','프로젝트 목표<br>정의 및 계획 수립'),('clipboard','분석','시장 및 고객 분석<br>요구사항 정의'),('ruler','설계','서비스 구조 설계<br>UI/UX 설계'),('monitor','개발','시스템 개발 및<br>기능 구현'),('shield','테스트','품질 검증 및<br>사용성 테스트'),('rocket','오픈','서비스 오픈 및<br>운영 시작')]):
 x=74+i*199
 if i<5:s+=at(x+140,355,60,0,'','connector')
 s+=at(x,282,140,140,icon(ic,100,'#fff'),'blue-circle center')+text(x-10,461,160,36,f'{i+1:02}',27,700,'#2863e7','center')+text(x-10,512,160,38,name,27,700,align='center')+text(x-30,555,200,65,note,22,450,align='center',extra='line-height:1.3')
pages['09']=s
# Budget
s=head('BUDGET PLAN','예산 계획',8)+at(116,244,378,378,'','budget-donut')+at(248,390,125,97,icon('coins',105),'center')
for i,(lab,c) in enumerate([('기획','#2863e7'),('개발','#86a8f3'),('디자인','#dfE9fe'),('테스트','#7b7b7b'),('유지보수','#aaa'),('기타','#282828')]):s+=at(540,313+i*46,28,28,'','',f'background:{c};border-radius:6px')+text(590,310+i*46,180,37,lab+' 25%',23,450)
s+=box(789,262,351,325)+text(820,310,290,55,'효율적인 예산 운영',33,750,'#2863e7','center')+text(819,391,291,120,'각 단계별 최적의 자원<br>배분을 통해 프로젝트의<br>성공을 지원합니다.',28,450,align='center',extra='line-height:1.36')+at(1032,538,87,70,icon('coins',80),'center')
pages['10']=s
# Q&A
s=head('Q&A','질의응답')+box(1018,75,330,295)+box(-70,448,340,330)+box(205,280,869,239)+at(308,363,86,86,icon('message',80),'center')+text(418,356,443,100,'궁금하신 사항이 있으시면<br>편하게 질문해 주세요.',34,450,align='center',extra='line-height:1.4')+at(898,361,80,80,icon('mic',72),'center');pages['11']=s
# Contact
s=head('CONTACT','문의 및 연락')+box(100,250,263,400)+text(112,271,239,45,'담당자',28,650,align='center')+at(146,333,170,193,icon('portrait',225),'center')+text(113,547,237,32,'영업 1팀 / 팀장',21,450,'#666','center')+text(112,578,239,45,'김미리',29,650,align='center')
for x,y,ic,name,note in [(444,297,'phone','전화','123-456-789'),(835,297,'globe','홈페이지','www.website.com'),(444,427,'mail','이메일','email@email.com'),(835,427,'pin','회사주소','미리도 미리시 미리구 미리동<br>1234'),(444,557,'fax','팩스','123-456-789')]:
 s+=at(x,y,42,44,icon(ic,42),'center')+text(x+90,y-10,270,40,name,29,650)+text(x+90,y+30,292,65,note,22,450,'#666',extra='line-height:1.45')
 if name in ['전화','이메일','홈페이지']:s+=at(x-20,y+85,355,1,'','','border-top:1.5px dashed #2863e7')
pages['12']=s
# Thank you
s=head('BUSINESS PROPOSAL')+text(76,185,780,94,'경청해주셔서',76,850,'#2863e7',extra='letter-spacing:-3px')+text(73,276,850,128,'감사합니다',104,900,extra='letter-spacing:-4px')+text(77,413,807,48,'최적의 전략과 체계적인 실행으로 퍼포먼스를 보여드리겠습니다.',24,450)+box(974,18,264,508)+box(800,410,341,261)+box(-65,544,400,260)+at(975,87,198,253,'','placeholder')+at(801,550,154,120,'','placeholder')+text(77,592,400,67,'MIRI COMPANY<br>email@email.com',21,450,'#888',extra='line-height:1.6');pages['13']=s
css='''@font-face{font-family:'Pretendard Variable';src:url('fonts/PretendardVariable.woff2');font-weight:100 900}@font-face{font-family:'Montserrat';src:url('fonts/Montserrat.woff2');font-weight:100 900}*{box-sizing:border-box}html,body{margin:0;width:1280px;height:720px;overflow:hidden}body{font-family:'Pretendard Variable';background:#fff;color:#000}.slide{position:relative;width:1280px;height:720px;overflow:hidden}.abs{position:absolute}.text{line-height:1.15}.center{display:flex;align-items:center;justify-content:center}.selection{border:1px solid color-mix(in srgb,var(--box) 55%,white);position:absolute}.selection:before{content:'';position:absolute;inset:-3px;background:linear-gradient(var(--box),var(--box)) 0 0/7px 7px no-repeat,linear-gradient(var(--box),var(--box)) 100% 0/7px 7px no-repeat,linear-gradient(var(--box),var(--box)) 0 100%/7px 7px no-repeat,linear-gradient(var(--box),var(--box)) 100% 100%/7px 7px no-repeat;pointer-events:none}.selection.blue:after{content:'';position:absolute;inset:-3px;pointer-events:none;background:linear-gradient(var(--box),var(--box)) 0 0/14px 6px no-repeat,linear-gradient(var(--box),var(--box)) 0 0/6px 14px no-repeat,linear-gradient(var(--box),var(--box)) 100% 0/14px 6px no-repeat,linear-gradient(var(--box),var(--box)) 100% 0/6px 14px no-repeat,linear-gradient(var(--box),var(--box)) 0 100%/14px 6px no-repeat,linear-gradient(var(--box),var(--box)) 0 100%/6px 14px no-repeat,linear-gradient(var(--box),var(--box)) 100% 100%/14px 6px no-repeat,linear-gradient(var(--box),var(--box)) 100% 100%/6px 14px no-repeat}.dots{display:flex;justify-content:space-between;align-items:center}.dots i{display:block;width:17px;height:17px;border-radius:50%}.ring{border:15px solid #2863e7;border-radius:50%}.blue-circle{border-radius:50%;background:#2863e7}.feature-square{border:1px solid #aaa}.core{border-radius:50%;background:#000;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px}.core b{font-size:25px}.competition table{width:100%;height:100%;border-collapse:collapse;table-layout:fixed;text-align:center;font-size:23px}.competition th{background:#000;color:#fff;font-weight:650;height:66px;border-right:1px solid #ddd}.competition td{height:66px;border-right:1px solid #eee;border-bottom:1px solid #eee}.competition th:nth-child(3){background:#2863e7}.competition td:nth-child(3){background:#dfe8fb}.connector{border-top:3px dotted #ccc}.connector:after{content:'';position:absolute;right:2px;top:-7px;width:10px;height:10px;border-top:3px solid #ccc;border-right:3px solid #ccc;transform:rotate(45deg)}.budget-donut{border-radius:50%;background:conic-gradient(#2863e7 0 25%,#86a8f3 25% 55%,#dfe9fe 55% 70%,#aaa 70% 80%,#7b7b7b 80% 90%,#282828 90%);position:absolute}.budget-donut:after{content:'';position:absolute;inset:69px;background:#fff;border-radius:50%}.burst{clip-path:polygon(50% 3%,63% 0,71% 11%,86% 13%,88% 27%,99% 36%,94% 50%,99% 63%,88% 73%,86% 87%,71% 90%,63% 100%,50% 95%,37% 100%,28% 89%,14% 87%,12% 73%,1% 63%,6% 50%,1% 36%,12% 27%,14% 13%,28% 11%,37% 0);display:flex;align-items:center;justify-content:center;color:#fff;font-size:56px}.burst small{font-size:30px}.placeholder{background:#eceef1}'''
(R/'shared.css').write_text(css)
for no,body in pages.items():(R/f'slide_{no}.html').write_text(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>069 · {no} replica</title><link rel="stylesheet" href="shared.css"></head><body><section class="slide">{body}</section></body></html>')
print('Created',len(pages),'replicas')
