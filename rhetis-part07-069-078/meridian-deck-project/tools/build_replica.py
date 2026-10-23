from pathlib import Path
import json,html,math
P=Path(__file__).parent;R=P/'replica';R.mkdir(exist_ok=True)
B='#0063ed';G='#5b5b5b';L='#f2f2f2';C='#cacaca'
CSS="""@font-face{font-family:Deck;src:url('../assets/fonts/artifacts/pretendard/PretendardVariable.woff2');font-weight:100 900}*{box-sizing:border-box}html,body{margin:0;width:1280px;height:720px;overflow:hidden;background:#fff;font-family:Deck,sans-serif;color:#5b5b5b}.slide{position:relative;width:1280px;height:720px;overflow:hidden}.txt{position:absolute;margin:0;white-space:pre-line;line-height:1.55;letter-spacing:-.6px}.shape{position:absolute}.ph{background:#e8e8e8}.center{display:flex;align-items:center;justify-content:center;text-align:center}.pill{border-radius:999px}.rule{position:absolute;height:1px;background:currentColor}.icon{display:block}svg{overflow:visible} .shadow{box-shadow:5px 12px 18px #0002}table{border-collapse:collapse;table-layout:fixed;width:100%;height:100%;font-size:16px}td:first-child,th:first-child{width:120px}td,th{text-align:center;padding:8px;border-right:4px solid white;border-bottom:1px solid #aaa}th{height:32px;padding:4px;background:#0063ed;color:white;font-weight:700}td{background:#f2f2f2}td:first-child{background:white;color:#0063ed;font-weight:700;font-size:18px}"""
(R/'replica.css').write_text(CSS)
def text(x,y,w,s,size=16,color=G,weight=400,align='left',lh=1.55):
 return f'<div class="txt" style="left:{x}px;top:{y}px;width:{w}px;font-size:{size}px;color:{color};font-weight:{weight};text-align:{align};line-height:{lh}">{s}</div>'
def box(x,y,w,h,color=L,r=0,border='',extra=''):
 return f'<div class="shape" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{color};border-radius:{r}px;{("border:"+border+";") if border else ""}{extra}"></div>'
def circle(x,y,d,color=B,border='',extra=''):return box(x,y,d,d,color,d/2,border,extra)
def ph(x,y,w,h,r=0):return box(x,y,w,h,'#e8e8e8',r)
def line(x,y,w,color=B):return box(x,y,w,1,color)
def pill(x,y,w,h,s,color=B,size=16,fg='white',weight=400):return box(x,y,w,h,color,h/2)+text(x,y+(h-size*1.2)/2,w,s,size,fg,weight,'center',1.2)
def svg(x,y,w,h,body):return f'<svg class="shape" style="left:{x}px;top:{y}px" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>'
def icon(x,y,s,kind='folder',color=B):
 paths={'folder':'<path d="M3 7h7l2-3h9v16H3z"/><path d="M3 9h20l-3 11H3z"/>','pencil':'<path d="M4 20l1-5L17 3l4 4L9 19zM14 6l4 4M5 15l4 4"/>','graduation-cap':'<path d="M1 8l11-5 11 5-11 5zM5 10v7c4 4 10 4 14 0v-7M22 9v9"/>','handshake':'<path d="M2 8l5-5 5 3 5-3 5 5-3 9-4 4-4-2-3 1-6-7zM7 7l5 5 4-3M8 15l7 5M11 12l8 6"/>','files':'<path d="M4 2h13v17H4zM9 6h5M7 10h7M7 13h7M20 6h2v17H9v-2"/>','lightbulb':'<path d="M8 19h8M9 22h6M8 16c-6-7-3-14 4-14s10 7 4 14l-1 3H9zM12 7v8M8 10l4 3 4-3"/>','presentation':'<path d="M2 3h20v15H2zM12 18v5M7 23h10M6 13V8M9 13v-3M16 9h4M17 7a2 2 0 1 0 0 .1"/>','message-circle':'<path d="M3 18l-1 5 6-3c14 4 19-12 8-17C6-2-3 9 3 18zM7 10h1M12 10h1M17 10h1"/>','monitor-up':'<path d="M2 3h20v15H2zM12 18v5M7 23h10M12 14V6M8 10l4-4 4 4"/>','network':'<circle cx="12" cy="3" r="3"/><circle cx="3" cy="20" r="3"/><circle cx="21" cy="20" r="3"/><path d="M10 6L5 17M14 6l5 11M6 20h12"/>','grid-3x3':'<path d="M2 2h20v20H2zM8 2v20M15 2v20M2 8h20M2 15h20"/>','calendar':'<path d="M2 4h20v18H2zM2 9h20M6 1v6M18 1v6M8 13h7l-3 6"/>'}
 return svg(x,y,s,s,f'<g transform="scale({s/24})" fill="none" stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{paths.get(kind,paths["folder"])}</g>')
def standard(n,title,sub='',white=False):
 color='white' if white else B
 return text(58,41,170,'<b>2090</b> BUSINESS PROJECT',14,color,500)+line(243,49,990,'#ccc' if white else '#78a6df')+(box(102,103,3,50,'white' if white else '#ddd') if title else '')+text(130,98,900,title,48,color,650,lh=1.2)+text({'CONTENTS':405,'CEO MESSAGE':485,'KEY POINT':400,'MAIN PROJECT':499,'PROJECT NAME':516,'PROJECT PROCESS':594,'PROJECT DETAILS':570,'PROJECT DEVELOPE':617}.get(title,130),118,650,sub,20,'#d4d4d4' if white else '#222')+line(58,677,1024,color)+text(1095,666,130,('PRESENTATION' if n in [2,3] else f'PRESENTATION · {1 if n<=6 else 2 if n<=8 else 3 if n==9 else 4 if n<=13 else 5 if n<=18 else 6 if n<=23 else 7 if n<=27 else 8:02d}'),14,color,400,'right')
def regular_note(x,y,w,lines=2,size=16,color='#888'):
 s='내용을 텍스트로 간략하게 입력해주세요. 관련 내용을\n텍스트로 간략하게 입력해주세요. 내용을 텍스트로\n간략하게 입력해주세요. 관련 내용을 입력해주세요.'
 return text(x,y,w,'\n'.join(s.splitlines()[:lines]),size,color)
def donut(x,y,d,v,color=B,size=56):
 a=v/100*360
 return box(x,y,d,d,f'conic-gradient({color} 0deg {a}deg,#f7f7f7 {a}deg 360deg)',d/2)+circle(x+14,y+14,d-28,'white')+text(x,y+d/2-size*.7,d,f'{v}<span style="font-size:{int(size*.45)}px">%</span>',size,B if color==B else G,650,'center',1.3)
def miniline(x,y,w,h,vals):
 pts=[(i*w/(len(vals)-1),h-v/max(vals)*h*.8) for i,v in enumerate(vals)]
 path=' '.join(f'{a},{b}' for a,b in pts)
 return svg(x,y,w,h,f'<polyline points="{path}" fill="none" stroke="{B}" stroke-width="1"/>'+''.join(f'<circle cx="{a}" cy="{b}" r="5" fill="white" stroke="{B}"/>' for a,b in pts))+line(x,y+h,w,G)
S={}
S[1]=text(87,95,1100,'BUSINESS PROPOSAL',72,'#222',700,lh=1.15)+text(87,176,1100,'PRESENTATION',72,B,700,lh=1.15)+text(88,273,700,'Miri Company Project',36,G)+ph(643,424,760,500,360)+circle(544,497,102,'#d7d7d7')+icon(573,528,46,'folder','white')+circle(875,236,53,'#d7d7d7')+icon(889,247,28,'pencil','white')+circle(1123,345,63,'#d7d7d7')+icon(1133,359,43,'graduation-cap','white')+box(87,598,4,50,'#ddd')+text(109,599,500,'<b>2090</b> BUSINESS PROJECT',20,B,600)+text(109,631,600,'Please write down the presentation information here',14,'#aaa')
s=standard(2,'CONTENTS','서브 타이틀과 텍스트가 있는 목차')
for i in range(9):
 x=61+(i%3)*386;y=248+(i//3)*121
 s+=text(x,y,386,f'<b style="color:{B}">{i+1:02d}</b> <b>상세설명형 목차</b>',18,'#111',400,'center')+text(x,y+32,386,'각 파트의 구체적인 내용을 적어주세요.',14,G,400,'center')
for y in [335,456,577]:s+=line(61,y,1158,'#78a6df')
S[2]=s
S[3]=standard(3,'')+ph(369,104,540,146,40)+text(300,257,680,'01',56,B,650,'center')+text(220,325,840,'목차별 타이틀',68,G,700,'center')+text(200,433,880,'각 파트의 상세 내용을 요약해주세요\n주요 내용을 2-3줄로 정리해서 타이틀 내용을 설명해주세요',20,G,400,'center')+text(190,564,900,'내용을 텍스트로 간략하게 입력해주세요. 관련 내용을 텍스트로 간략하게 입력해주세요. 관련 내용을 간략하게 입력해주세요.',14,'#888',400,'center')
s=standard(4,'CEO MESSAGE','안녕하세요, 미리컴퍼니 대표 강미리 입니다.')+ph(809,175,310,412)+text(809,595,180,'미리컴퍼니 대표이사\n강미리',14,G,600)+text(977,598,230,'* 페이지내 인물사진은 샘플이미지입니다.',10,'#999')
for i,h in enumerate(['존경하는 이해관계자 여러분에게,','하나, 앞으로의 경영 전략에 대해 적어주세요','둘, 앞으로의 경영 전략에 대해 적어주세요','셋, 앞으로의 경영 전략에 대해 적어주세요']):
 y=219+i*110;s+=text(101,y,680,h,18,B,700)+text(101,y+35,680,'이 페이지는 CEO의 인사말을 적는 페이지입니다. ESG에 관한 회사의 입장이나\n20xx년의 성과에 대해 적어보세요. 회사 경영 방침이나 CEO의 의지를 표현할 수 있습니다.',16,G)
# Side panel is background, keep header above it
S[4]=box(969,0,311,720,'#f7f7f7')+s
s=standard(5,'KEY POINT','비전을 소개하는 레이아웃')+ph(369,181,540,140,50)
for i in range(3):
 x=165+i*341;s+=circle(x,271,268,B,extra='box-shadow:6px 17px 19px #0002')+text(x,361,268,'VISION',28,'white',500,'center')+text(x+15,406,238,'텍스트로 간략하게 입력해주세요.\n관련 내용을 간략하게 입력해주세요.',14,'white',400,'center')
 if i<2:s+=text(x+283,370,40,'+',46,B,700,'center')
s+=text(219,595,100,'VISION',20,B,700)+text(322,582,850,'내용을 텍스트로 간략하게 입력해주세요. 관련 내용을 텍스트로 간략하게 입력해주세요. 관련 내용을 간략하게 입력해주세요.\n내용을 텍스트로 간략하게 입력해주세요. 관련 내용을 텍스트로 간략하게 입력해주세요. 내용을 텍스트로 간략하게 입력해주세요.',16,G)
S[5]=s
s=standard(6,'MAIN PROJECT','주요 프로젝트를 소개해주세요')+ph(101,200,439,367)+text(101,586,450,'관련 이미지를 넣어주세요. 실제로 경험한 이미지를\n실제로 경험한 업무 내용을 입력해주세요.',16,G)
for i,(h,en) in enumerate([('고객 니즈','CUSTOMER'),('문제 OR 기회상황','COMPANY'),('비교 대상','COMPETITOR')]):
 y=181+i*162;s+=text(581,y,620,f'<b style="font-size:30px">{i+1:02d}</b> <b style="font-size:22px">{h}</b>　<span style="font-size:12px">│ {en}</span>',18,G)+line(581,y+42,618,'#888')+text(581,y+54,620,'간단한 설명을 이곳에 텍스트로 간략하게 입력해주세요. 관련 내용을 이곳에 텍스트를 입력해주세요.',14,G)
 for j in range(2):s+=pill(580+j*315,y+99,305,35,'•  강조하고 싶은 포인트 내용을 입력하세요',size=14)
S[6]=s
S[7]=ph(645,0,635,720)+svg(0,0,910,720,f'<polygon points="0,0 647,0 909,720 0,720" fill="{B}"/>')+standard(7,'PROJECT NAME','텍스트 레이아웃',True)+text(101,255,570,'강조하고 싶은 내용은\n이곳에 텍스트로 입력하세요',36,'white',500,lh=1.25)+text(101,387,550,'이곳에 브랜드를 설명하는 내용을 간략하게 입력해 주세요. 관련 내용을 텍스트로\n입력해주세요. 이곳에 브랜드를 설명하는 내용을 간략하게 입력해 주세요.\n관련 내용을 이곳에 간략하게 두세줄 정도 입력해주세요.',16,'white',400,lh=1.8)+text(101,497,550,'이곳에 브랜드를 설명하는 내용을 간략하게 입력해 주세요. 관련 내용을 텍스트로\n입력해주세요. 이곳에 브랜드를 설명하는 내용을 간략하게 입력해 주세요.\n관련 내용을 이곳에 간략하게 두세줄 정도 입력해주세요.',16,'white',400,lh=1.8)
s=standard(8,'PROJECT NAME','3개의 텍스트 목록 레이아웃')+ph(851,-80,580,580,290)+circle(851,-80,580,'transparent','1px solid #78a6df')+ph(684,272,336,336,168)+circle(684,272,336,'transparent','1px solid #78a6df')
for i,word in enumerate(['첫','두','세']):
 y=237+i*125;s+=box(111,y,518,114,'#f1f1f1',4)+circle(90,y+33,50,B,extra='box-shadow:3px 4px 6px #0002')+text(90,y+43,50,f'{i+1:02d}',18,'white',600,'center')+text(178,y+18,430,f'이곳에 {word} 번째 제목을 입력하세요',20,G,600)+regular_note(178,y+54,420,2,14,'#aaa')
S[8]=s
s=standard(9,'KEY POINT','프로젝트 4단 핵심 포인트')
for i,ic in enumerate(['handshake','files','lightbulb','presentation']):
 x=110+i*270;s+=box(x,270,251,367,B,11)+circle(x+54,212,143,'#fafafa',f'4px solid {B}')+icon(x+92,250,68,ic)+text(x,373,251,f'POINT {i+1:02d}',26,'white',650,'center')+line(x,421,251,'#ccc')+text(x+30,447,191,'깔끔한 아이콘을 사용한\n정리는 PPT의 퀄리티를\n올려줍니다.이곳에\n관련 내용을 입력해주세요.',16,'white',400,'center',1.7)
S[9]=s
s=standard(10,'PROJECT NAME','아이콘과 텍스트 레이아웃')+ph(87,196,440,440,220)+circle(87,196,440,'transparent','1px solid #78a6df')
for i,ic in enumerate(['folder','pencil','graduation-cap']):
 x=527+(85 if i==1 else 0);y=216+i*147;s+=circle(x,y,105,B if i!=1 else G,'2px solid white',extra='box-shadow:4px 8px 13px #0001')+icon(x+29,y+32,48,ic,'white')+line(x-24,y+52,25,B if i!=1 else G)+circle(x-29,y+47,12,'white',f'3px solid {B if i!=1 else G}')+text(x+150,y-5,500 if i!=1 else 430,('이곳에 제목을 입력하세요' if i==1 else '제목을 입력하세요')+'　 <span style="font-size:16px;color:#aaa">│ KEY POINT</span>',22,G,600)+text(x+150,y+43,500 if i!=1 else 430,'관련 내용을 텍스트로 간략하게 입력해주세요. 이곳에 관련 내용을 텍스트로\n간략하게 입력해주세요. 관련 내용을 텍스트로 간략하게 입력해주세요.',14,'#999',400,lh=1.8)
S[10]=s
s=standard(11,'PROJECT PROCESS','프로세스 상세 내용')
for i in range(2):
 y=178+i*252;s+=box(101,y,410,238,'#f2f2f2',8)+box(101,y,410,38,B,8)+box(101,y+18,410,20,B)+text(101,y+9,410,f'KEYWORD {i+1}',14,'white',500,'center')+text(125,y+68,362,'경로 다변화로 신규 사용자 참여 확대' if i==0 else '기존 사용자의 반복 참여가\n참여율 향상 견인',18,G,600,'center')+text(121,y+112 if i==0 else y+140,370,'•  신규 유입의 주요 경로가 커뮤니티 콘텐츠\n　→ 추천 흐름으로 이동\n•  콘텐츠 기반 유입 고객의 전환율이\n　 기존 대비 +7%p' if i==0 else '•  기존 고객의 반복 전환 비중이 성장\n•  이용 빈도 증가가 전환율 개선에 직접 기여\n•  관련된 세부내용을 입력해주세요.',16,G,400,lh=1.4)
s+=pill(756,222,268,38,'고객 전환율 변화',weight=700)+box(584,286,42,8,G)+text(631,281,80,'신규고객',10,'#888')+box(584,305,42,8,B)+text(631,300,80,'기존고객',10,'#888')+text(584,318,100,'[단위 : %]',10,'#888')
for i,(a,b) in enumerate([(138,152),(168,187),(196,212),(251,268)]):
 x=584+i*168
 for j,v in enumerate([a,b]):s+=box(x+j*61,606-v,53,v,G if j==0 else B)+text(x+j*61,584-v,53,'00',14,G,400,'center')
 s+=text(x,617,114,f'{i+1}Q',14,G,600,'center')
s+=line(556,606,667,'#bbb');S[11]=s
s=standard(12,'PROJECT NAME','SWOT 다이어그램')
for i,(char,color) in enumerate([('S',G),('W',B),('O',B),('T',G)]):
 x=457+(i%2)*184;y=221+(i//2)*185
 # Four interlocking petals drawn as quarter-round rotated teardrops
 angle=[-45,45,-135,135][i]
 s+=box(x,y,184,184,color,92,extra=f'transform:rotate({angle}deg);border-bottom-right-radius:0;box-shadow:5px 9px 18px #0002')+text(x,y+39,184,char,80,'white',700,'center')
for i,(h,k) in enumerate([('STRENGTH','강점'),('WEAKNESS','약점'),('OPPORTUNITY','기회'),('THREAT','위기')]):
 x=76 if i%2==0 else 864;y=260+(i//2)*188;s+=text(x,y,340,f'<b style="color:{B};font-size:26px">{h}</b> │ {k}',16,G,400,'right' if i%2==0 else 'left')+text(x,y+43,340,'내용을 텍스트로 간략하게 입력해주세요. 관련 내용을\n텍스트로 간략하게 입력해주세요. 내용을 텍스트로\n간략하게 입력해주세요. 관련 내용을 입력해주세요.',14,'#aaa',400,'right' if i%2==0 else 'left',1.8)
S[12]=s
s=standard(13,'PROJECT PROCESS','프로세스 상세 내용')+text(200,179,880,'사용자 참여 확대 및 광고·제휴 수익 강화를 위해\n<b style="color:#0063ed">연초 설정한 핵심 전략 방향</b>',30,G,700,'center',1.4)
for i,(ic,h) in enumerate([('message-circle','커뮤니티 활동량 확대 및\n사용자 체류 시간 증가'),('monitor-up','광고·제휴 기반 수익 구조 강화')]):
 x=272+i*394;s+=box(x,285,340,149,B,13)+icon(x+150,314,42,ic,'white')+text(x+20,365,300,h,20,'white',650,'center',1.4)
s+=svg(527,438,225,65,'<polygon points="112,0 225,35 175,35 225,65 0,65 50,35 0,35" fill="#cfe1fa"/>')
for i,h in enumerate(['핵심 카테고리 콘텐츠 공급 확대','사용자 참여 촉진 구조 고도화','광고·제휴 상품 경쟁력 강화']):
 x=83+i*378;s+=box(x,502,359,156,'#f6f6f6',10)+box(x,502,359,44,'#cfe1fa',8)+text(x,513,359,h,18,G,600,'center')+text(x+41,573,300,'•  일간 인기 콘텐츠 큐레이션 강화\n•  신규 게시글 생성 프로그램 운영' if i==0 else '•  참여형 캠페인 운영\n•  목표 달성을 위한 구체적 전략적 방향',16,G,400,lh=1.9)
S[13]=s
s=standard(14,'PROJECT DETAILS','프로세스 상세 내용')+text(135,184,550,'상단 <b style="color:#0063ed">문장,</b>\n하단 <b style="color:#0063ed">그래프</b> 넣는 페이지',42,G,400,lh=1.25)+text(706,215,470,'<b>상단에는 아래의 그래프나 수치와 관련된 내용을 입력해 주세요.</b>\n프레젠테이션 주제와 관련된 동향이나,\n전망, 트렌드 등을 설명하는 용도로 사용해도 좋습니다.',18,G,400,lh=1.4)
vals=[5,8,15,12,20,10,18,22,25,40,52,60,72,65,64];points=[]
for i,v in enumerate(vals):points.append((214+i*62.3,617-v*3.34))
for v in [0,20,40,60,80]:s+=line(183,617-v*3.34,935,'#ccc')+text(145,607-v*3.34,31,str(v),14,B,400,'right')
s+=svg(0,0,1280,720,f'<polygon points="214,617 '+ ' '.join(f'{x},{y}' for x,y in points)+f' {points[-1][0]},617" fill="#b4cff6"/><polyline points="'+ ' '.join(f'{x},{y}' for x,y in points)+f'" fill="none" stroke="{B}" stroke-width=".7"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="3.5" fill="{B}"/>' for x,y in points))
for i,(x,y) in enumerate(points):s+=text(x-20,y-26,40,str(vals[i]),14,B,400,'center')+text(x-20,623,40,f'{i+1:02d}',14,B,400,'center')
S[14]=s
s=standard(15,'PROJECT DETAILS','프로세스 상세 내용')+text(90,184,400,'VISION',22,B,700)+text(334,184,400,'STRATEGY',22,B,700)+text(574,184,400,'ACTION',22,B,700)+line(83,223,1114,G)+box(109,247,189,383,B,95)+text(119,383,169,'사업 목표\n&\n비전',28,'white',650,'center',1.25)
for y in [247,446]:
 s+=circle(354,y,184,G)+text(354,y+37,184,'핵심전략',14,'#ddd',600,'center')+text(364,y+82,164,'핵심문장을\n입력해주세요',20,'white',700,'center',1.4)+text(300,y+66,55,'⟶',42,B,400,'center')+text(531,y+66,55,'⟶',42,G,400,'center')
 for j in range(3):s+=circle(601+j*197,y+5,174,'#f8f8f8')+text(601+j*197,y+38,174,'세부전략',14,'#4080d0',600,'center')+text(611+j*197,y+80,154,'텍스트를 입력해주세요\n텍스트를 입력해주세요',14,G,400,'center')
S[15]=s
s=standard(16,'PROJECT DETAILS','프로세스 상세 내용')
for i,(h,en) in enumerate([('고객 니즈','CUSTOMER'),('문제 OR 기회상황','COMPANY'),('비교대상','COMPETITOR')]):
 y=177+i*167;s+=text(110,y+32,70,f'{i+1:02d}',44,B,700,'center')+ph(211,y,297,137)+text(566,y+11,600,f'<b style="color:{B}">{h}</b>　 <span style="font-size:12px">│ {en}</span>',18,G,400)+text(566,y+51,610,'좌측에 관련 이미지를 넣어주세요. 실제로 경험한 이미지를 넣으면 더 좋습니다. 업무 현장 사진을\n추가해주세요. 업무 현장 사진을 추가해주세요. 관련 도표를 넣어주셔도 좋습니다.\n실제로 경험한 업무 내용을 입력해주세요. 관련된 프로젝트 사진을 아래에 넣어주세요.',14,G,400,lh=1.65)
 if i<2:s+=line(110,y+153,1060,G)
S[16]=s
s=standard(17,'PROJECT DETAILS','프로세스 상세 내용')+text(180,169,920,'<b style="color:#0063ed">3개 프로젝트 모두 핵심 지표에서</b>\n일정 수준 이상의 개선을 보이며 안정적인 성과 달성',32,G,700,'center',1.4)
for i,(h,co) in enumerate([('성과요약',B),('관련수치','#999'),('분기별 지표',G)]):s+=box(103,333+i*90,172,83 if i<2 else 136,co,11)+text(103,364+i*90,172,h,20,'white',650,'center')
for i in range(3):
 x=289+i*304;s+=box(x,277,290,373,'#f2f2f2',11)+box(x,277,290,44,B,10)+box(x,299,290,22,B)+text(x,289,290,f'프로젝트 {i+1}',18,'white',600,'center')+text(x+20,353,250,['월간 신규 게시글 수와 주간 재방문율\n모두 목표 대비 높은 수준으로 상승','댓글·공감수 증가와 참여 기반 전환율\n향상에 기여','광고 상품 이용률과 제휴 캠페인 수\n모두 성장세 유지'][i],16,G)+line(x+18,420,254,'#aaa')+text(x+20,439,250,'•  신규 게시글 <b>+28%</b>\n•  활동 전환율 <b>+7%p</b>' if i==0 else '•  참여 액션 <b>XX만 건</b>\n•  참여율 <b>+14%</b>' if i==1 else '•  관련 성과 키워드 1\n•  관련 성과 키워드 2',16,G,400,lh=1.9)+line(x+18,510,254,'#aaa')+miniline(x+55,520,178,90,[20,35,61] if i==0 else [25,65,80] if i==1 else [30,36,69])
 for j in range(3):s+=text(x+35+j*89,617,40,f'{j+2}Q',12,G,400,'center')
S[17]=s
s=standard(18,'PROJECT DETAILS','프로세스 상세 내용')+ph(463,237,355,355,178)+text(483,362,315,'아이템 또는\n핵심 기술명',32,'white',650,'center')+text(483,468,315,'페이지에 알맞는 사진을 넣어주세요',12,'white',400,'center')
for i,h in enumerate(['분야 및 타겟','특징','용도 및 성능','장점']):
 x=82 if i%2==0 else 819;y=243 if i<2 else 470
 for j in range(5):s+=line(x,y+j*30,375,'#999')
 for j,tx in enumerate(['텍스트를 입력해주세요.','폰트는 프리텐다드 Regular 입니다.','강조 텍스트는 Bold를 사용해주세요.','크기는 16, 자간은 -4입니다.']):s+=text(x,y+4+j*30,375,tx,14,B if j==2 and i!=2 else G,650 if j==2 else 400,'center')
 cx=382 if i%2==0 else 756;s+=circle(cx,y-10,144,B)+text(cx,y+45,144,h,22,'white',650,'center')
S[18]=s
s=standard(19,'PROJECT DETAILS','프로세스 상세 내용')+text(82,193,500,'1. 프로젝트 판매 전략',18,G,600)+text(653,193,500,'2. 프로젝트 자금 및 운용자금',18,G,600)
for i in range(4):
 x=82+i%2*255;y=227+i//2*219;s+=box(x,y,233,199,'#f8f8f8',10)+text(x,y+26,233,'타이틀을 입력해주세요',18,B,700,'center')+text(x+15,y+75,203,'판매 방법 및 전략에 대한\n설명을 입력해주세요.\n폰트는 프리텐다드 Regular\n크기는 16입니다.',14,G,400,'center',1.6)
for j,h in enumerate(['금액','자기자금','타인자금']):s+=text(727+j*161,228,150,h,14,B,600,'center')
for i,h in enumerate(['창업자금','부지매입','공장건축','생산설비','제조원가','일반관리']):
 y=260+i*64;s+=box(653,y,160,51,'#e6eefb' if i<3 else '#3781ec',26)+text(653,y+15,74,h,14,G if i<3 else 'white',400,'center',1.2)
 for j in range(3):s+=pill(727+j*161,y,150,51,'텍스트 입력','#f2f2f2',14,G)
S[19]=s
s=standard(20,'PROJECT DEVELOPE','프로세스 해결 방안')+text(200,181,880,'운영 과정에서 확인된 주요 이슈와\n<b style="color:#0063ed">이를 해결하기 위한 개선 방향</b>',32,G,700,'center',1.4)
for i,(ic,h,a,b) in enumerate([('network','사용자 경험','초기 진입 시 원하는 콘텐츠를\n찾기까지 단계가 많아 이탈 존재','진입 동선을 단순화하고 핵심 콘텐츠\n접근성을 높이는 구조 개편 검토 필요'),('grid-3x3','노출 로직','로직이 사용자 패턴을\n충분히 반영하지 못해 일관성 낮음','사용자 행동 기반 데이터 반영을\n강화하고 추천 기준을 재정비'),('calendar','콘텐츠 품질','사용자 경험에 부정적 영향을 준\n문제를 한 줄로 입력해 보세요.','해결을 위해 향후 추진할 필요가 있는\n개선 방향을 작성해 보세요.')]):
 y=291+i*125;s+=box(143,y,183,103,B,12)+icon(216,y+23,35,ic,'white')+text(143,y+67,183,h,18,'white',650,'center')+text(355,y+24,320,a,18,G,400,'center')+svg(680,y+15,107,75,'<polygon points="0,20 71,20 71,0 107,37 71,75 71,55 0,55" fill="#87b1f6"/>')+text(838,y+24,340,b,18,G,600,'center')
 if i<2:s+=line(333,y+120,800,'#999')
S[20]=s
s=standard(21,'PROJECT DEVELOPE','표를 활용한 레이아웃')
heads=['항목','상세내역','예산비용','집행시기','비고','비고2'];rs=[]
for i,(h,v,m) in enumerate(zip(['인건비','비품','운영비','예비비','광고비','항목'],['3,000,000','500,000','5,000,000','2,000,000','800,000','9,000,000'],['3월 중순','2월 중순','3월 중순','4월 중순','2월 중순','3월 중순'])):rs.append([h,'프로젝트 인력 비용' if i==0 else '상세 내역을 적어주세요',v+'원',m,'XX팀 포함 총 3인' if i==0 else '내용을 적어주세요','내용을 적어주세요'])
s+=f'<div class="shape" style="left:65px;top:195px;width:1153px;height:437px"><table><thead><tr>'+''.join('<th>'+h+'</th>' for h in heads)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+v+'</td>' for v in row)+'</tr>' for row in rs)+'</tbody></table></div>';S[21]=s
s=standard(22,'PROJECT DEVELOPE','그래픽을 활용한 레이아웃')+text(200,181,880,'운영 과정에서 확인된 주요 이슈와\n<b style="color:#0063ed">이를 해결하기 위한 개선 방향</b>',32,G,700,'center',1.4)
# Fan sectors are pure SVG, not image placeholders
s+=svg(318,347,650,317,'<path d="M0 317 A325 325 0 0 1 87 102 L240 254 A108 108 0 0 0 216 317Z" fill="#bfd7fa"/><path d="M100 88 A325 325 0 0 1 317 0 L317 216 A108 108 0 0 0 253 244Z" fill="#bfd7fa"/><path d="M332 0 A325 325 0 0 1 550 88 L395 244 A108 108 0 0 0 332 216Z" fill="#bfd7fa"/><path d="M564 102 A325 325 0 0 1 650 317 L434 317 A108 108 0 0 0 410 254Z" fill="#bfd7fa"/>')
for x,y,c,h in [(302,506,'A','키워드A에 대해\n입력해주세요.'),(478,331,'B','키워드B에 대해\n입력해주세요.'),(726,331,'C','키워드C에 대해\n입력해주세요.'),(902,506,'D','키워드D에 대해\n입력해주세요.')]:s+=circle(x,y,82,'#bfd7fa','8px solid white')+text(x,y+24,82,c,26,G,700,'center')
for x,y in [(398,586),(491,431),(672,431),(773,586)]:s+=text(x,y,160,'키워드에 대해\n입력해주세요.',20,G,700,'center',1.4)
for x,y in [(105,496),(258,291),(860,291),(1013,496)]:s+=text(x,y,200,'·  주제에 대한 세부내용을\n　간략하게 입력해주세요.\n·  폰트는 프리텐다드 레귤\n　러, 크기는 18pt 입니다.',18,G,400,lh=1.6)
S[22]=s
s=standard(23,'PROJECT NAME','연혁을 나타내는 레이아웃')
for i in range(5):
 x=151+i*197;y=304+(24 if i%2 else 0);co=B if i%2==0 else G;s+=circle(x,y,190,co,extra='box-shadow:4px 13px 16px #0002')+text(x,y+44,190,f'<u>{i+1:02d}</u>',22,'white',500,'center')+text(x,y+77,190,'20XX',30,'white',400,'center')+text(x,y+116,190,'타이틀 텍스트 입력',16,'white',400,'center')
 if i%2==0:
  s+=box(x+94,y+197,3,31,co)+circle(x+89,y+223,13,'white',f'3px solid {co}')+text(x-50,551,290,'타이틀 텍스트 입력',18,G,700,'center')+text(x-50,584,290,'내용을 텍스트로 간략하게 입력해주세요. 관련 내용을\n텍스트로 간략하게 입력해주세요.',14,'#aaa',400,'center')
 else:s+=box(x+94,y-31,3,24,co)+circle(x+89,y-45,13,G)+text(x-50,246,290,'타이틀 텍스트 입력',18,G,700,'center')+text(x-50,197,290,'내용을 텍스트로 간략하게 입력해주세요. 관련 내용을\n텍스트로 간략하게 입력해주세요.',14,'#aaa',400,'center')
S[23]=s
s=standard(24,'PROJECT DEVELOPE','프로세스 해결 방안')+pill(68,184,1144,40,'이곳에 프로젝트 결과에 대해 강조하고 싶은 내용을 텍스트로 입력해 주세요. 관련 내용을 텍스트로 입력해주세요.',weight=650)+ph(779,258,429,392)
for i,h in enumerate(['문제해결 액션','생산성 증가 액션','의사소통 협상 액션']):
 y=243+i*151;s+=text(86,y,330,h,20,B,700)+text(86,y+40,330,'좌측에 관련 이미지를 넣어주세요. 실제로 경험한\n이미지를 넣으면 더 좋습니다. 상단에 현장 사진을\n추가해주세요. 관련 도표를 넣어주셔도 좋습니다.',14,G,400,lh=1.6)
 for j in range(2):s+=box(428,y+15+j*49,326,41,'#f7f7f7')+text(453,y+24+j*49,290,'•  강조하고 싶은 포인트 내용을 입력하세요',14,G)
 if i<2:s+=line(72,y+136,682,G)
S[24]=s
s=standard(25,'PROJECT NAME','사분면을 나타내는 레이아웃')+pill(767,202,188,39,'실행용이성 사분면',size=20)+box(551,273,633,324,'linear-gradient(to right,#deefff,#ffffff)')+box(861,273,323,324,'linear-gradient(to right,#b9defc,#ffffff)')+line(551,435,633,'#ccc')+box(861,273,1,324,'#ccc')+text(490,270,40,'높음',14,G)+text(490,578,40,'낮음',14,G)+text(487,423,60,'영향도',14,G)+text(825,612,100,'실행용이성',14,G)+text(1156,612,40,'높음',14,G)
for i,h in enumerate(['배송 시스템 개선','응대 표준화','결제 오류 해결','반품 과정 간소화']):
 y=205+i*118;s+=pill(94,y,137,27,h,G,14)+text(247,y-3,270,'•  물류사 협업 체계 강화\n•  실시간 배송 추적 시스템 고도화\n•  성수기 물량 대응 프로세스 구축' if i==0 else '•  간편결제 연동 안정화\n•  결제 오류 시 즉시 복구 시스템 구축\n•  오류 발생 시 안내 메시지 개선' if i==2 else '•  관련 내용을 이곳에 입력하세요\n•  관련 내용을 이곳에 입력하세요\n•  관련 내용을 이곳에 입력하세요',14,G,400,lh=1.6)
 if i<3:s+=line(94,y+92,360,'#ddd')
for x,y,h in [(1055,279,'배송 시스템\n개선'),(851,326,'간편 결제\n오류 해결'),(979,378,'CS 응대\n표준화'),(801,423,'반품 프로세스\n간소화')]:s+=pill(x,y,89,40,h,B,12)
S[25]=s
s=standard(26,'PROJECT NAME','그래프를 나타내는 레이아웃')+text(200,181,880,'프로젝트와 관련된 내용을 기재하고\n<b style="color:#0063ed">강조할 내용은 포인트 컬러를 활용하세요</b>',32,G,700,'center',1.4)
for i,(v,co) in enumerate([(80,'#ccc'),(70,'#999'),(75,G),(91,B)]):
 x=102+i*294;s+=pill(x,307,192,41,'키워드',co,20,weight=650)+text(x-20,365,232,'업무별 성과 달성률이나\n예산 집행률 표현에 좋아요.',18,G,400,'center',1.3)+donut(x,437,192,v,co,60)
S[26]=s
s=standard(27,'PROJECT NAME','3개의 사진과 텍스트')
for i in range(3):
 x=95+i*377;s+=box(x,228,350,203,'white',0,'1px solid #78a6df')+ph(x+6,234,338,191)+circle(x-5,221,33,B)+text(x-5,220,33,'+',30,'white',650,'center',1)+box(x,439,350,164,'#f8f8f8')+text(x,456,350,'타이틀 텍스트 입력',24,B,650,'center')+line(x+27,491,296,'#78a6df')+text(x+20,507,310,'내용을 텍스트로 간략하게 입력해주세요.\n관련 내용을 텍스트로 간략하게 입력해주세요.\n내용을 텍스트로 간략하게 입력해주세요.',16,G,400,'center',1.6)
S[27]=s
s=standard(28,'PROJECT NAME','단계별 프로세스 레이아웃')+box(83,195,1115,4,G)+box(910,195,288,4,B)+svg(1182,188,16,18,f'<polygon points="0,0 16,9 0,18" fill="{B}"/>')+pill(368,184,257,26,'물류·배송 인프라 혁신',G,14)+pill(987,184,151,26,'디지털 플랫폼 고도화',B,14)
for i,h in enumerate(['물류 중계 거점 확대','AI 기반 배송 최적화','멀티 물류사 통합 관리','고객 맞춤 배송 서비스']):
 x=83+i*280;co=['#f2f2f2',G,'#222',B][i];s+=svg(x,227,285,44,f'<polygon points="0,0 270,0 285,22 270,44 0,44 15,22" fill="{co}"/>')+text(x+10,237,265,h,16,G if i==0 else 'white',400,'center')+box(x,280,273,275,'#f2f2f2')+text(x+22,311,240,'•  개선과제의 상세내용을 넣어보세요.\n•  개선과제의 상세내용을 넣어보세요.',14,G,400,lh=1.8)+pill(x+63,385,147,50,['2개소','AI 활용','물류사 A','배송 서비스'][i],G if i<2 else '#222' if i==2 else B,18)+(pill(x+63,475 if i==0 else 447,147,50,['5개소','AI 활용','','배송 서비스'][i],B if i==0 else G if i==1 else B,18) if i!=2 else '')
s+=svg(178,440,80,30,'<polygon points="0,0 80,0 40,30" fill="#9dc3fa"/>')+line(707,459,140,'#ccc')+box(707,459,1,10,'#ccc')+box(847,459,1,10,'#ccc')+box(777,449,1,20,'#ccc')+''.join(box(687+j*70,482,50,43,B,6)+text(687+j*70,491,50,chr(65+j),22,'white',400,'center') for j in range(3))
s+=box(83,561,1115,72,B)+text(110,581,1060,'전체 예상 투자 규모: <b>XX억원</b>　│　연간 기대 효과: <b>매출 증대 XX억원, 비용 절감 XX억원</b>',20,'white',400,'center');S[28]=s
s=standard(29,'PROJECT NAME','4개 이미지 레이아웃')+text(200,181,880,'부서별 인재에 대해 상세 설명을 기재해주세요',32,G,700,'center')+text(1065,228,160,'* 페이지 내 인물 사진은 샘플 이미지입니다.',8,G)
for i in range(4):
 x=62+i*299;s+=ph(x,248,262,218)+text(x,495,262,'<b style="color:#0063ed">부서명</b>\n김미리 대리',20,G,400,lh=1.4)+line(x,566,262,'#ddd')+text(x,582,262,'프로젝트 내 역할과 담당 분야를 명시해\n책임 소재를 밝혀주세요.',18,G,400,lh=1.4)
S[29]=s
S[30]=text(300,99,680,'Miri Company Project',38,G,400,'center')+text(110,145,1060,'THANK YOU FOR',88,G,700,'center',1.2)+text(200,240,880,'ATTENTION',88,B,700,'center',1.2)+text(300,359,680,'프레젠테이션을 마치겠습니다. 감사합니다.',22,'#999',400,'center')+ph(154,450,970,168,70)+circle(181,357,102,B,'2px solid white',extra='box-shadow:3px 6px 11px #0001')+icon(209,389,48,'folder','white')+circle(440,495,60,B,'2px solid white')+icon(457,513,28,'pencil','white')+circle(984,461,64,B,'2px solid white')+icon(998,478,34,'graduation-cap','white')+box(56,611,1168,62,B,7)+text(190,630,240,'<b>2090</b> BUSINESS PROJECT',18,'white',600,'center')+text(462,631,730,'담당자: 김미리　│　T 02.1234.5678　│　M 010.1234.5678　│　E mm@miricompany.com',16,'#a4c7fa')
for n,s in S.items():
 # Repeated photographic world maps are deliberately single flat placeholders.
 (R/f'slide_{n:02d}.html').write_text(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>074 Replica {n:02d}</title><link rel="stylesheet" href="replica.css"></head><body><main class="slide">{s}</main></body></html>')
(P/'pages.json').write_text(json.dumps({str(k):v for k,v in S.items()},ensure_ascii=False,indent=2))
print('Replica HTML pages:',len(S))
