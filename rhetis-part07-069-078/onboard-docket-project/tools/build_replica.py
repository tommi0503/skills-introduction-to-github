from pathlib import Path
import html,json
P=Path(__file__).parent; R=P/'replica';R.mkdir(exist_ok=True)
FONT='../assets/fonts/artifacts/noto-sans-kr/NotoSansKR.woff2'
CSS=f'''@font-face{{font-family:Noto;src:url("{FONT}");font-weight:100 900}}*{{box-sizing:border-box}}html,body{{margin:0;width:1280px;height:720px;overflow:hidden}}body{{font-family:Noto,sans-serif;color:#080808;background:#dcdcdc;font-weight:400}}.slide{{position:relative;width:1280px;height:720px;overflow:hidden}}.paper{{position:absolute;left:46px;top:92px;width:1188px;height:590px;background:#fdfdfd;border-radius:14px;box-shadow:24px 24px 35px #0002}}.rail{{position:absolute;left:46px;top:38px;width:1188px;height:49px;background:#3d7eea;border-radius:12px;box-shadow:2px 3px 5px #0002;color:white;display:flex;align-items:center;justify-content:space-between;padding:0 25px;font-size:18px;font-weight:700}}.brand{{display:flex;align-items:center;gap:10px;font-size:14px;font-weight:700}}.brand .logo{{height:22px;width:22px;background:#eceff3;border-radius:4px}}.chapter{{font-size:18px}}.head{{position:absolute;left:97px;top:133px;height:84px;width:1086px;border-bottom:1px solid #c8c8c8;display:flex;align-items:flex-start}}.head .num{{font-size:58px;font-weight:600;color:#4383e6;line-height:1.2;width:124px;height:83px;border-right:1px solid #c8c8c8;padding-left:27px}}.head .title{{font-size:48px;font-weight:600;line-height:1.3;letter-spacing:-2.6px;margin:3px 0 0 35px}}.head .suffix{{align-self:center;color:#4383e6;font-size:16px;letter-spacing:.5px;margin-left:24px;margin-top:8px;white-space:nowrap}}.ph{{background:#ededed;border:1px solid #e7e7e7}}.icon{{display:block}}@font-face{{font-family:Pen;src:url("../assets/fonts/artifacts/nanum-pen-script/NanumPenScript-Regular.woff2");font-weight:400}}.txt{{position:absolute;margin:0;line-height:1.6;letter-spacing:-.7px}}.blue{{color:#4383e6}}.muted{{color:#818181}}.pill{{display:flex;align-items:center;justify-content:center;border-radius:999px}}.center{{text-align:center}}.rule{{height:1px;background:#c8c8c8;position:absolute}}'''
(R/'replica.css').write_text(CSS)
icons={
'file-pen':'<path d="M12 19H5V3h10l4 4v4M14 3v5h5M8 11h5M8 15h3M15 20l6-6-3-3-6 6-1 4z"/>',
'briefcase':'<rect x="3" y="7" width="18" height="14" rx="2"/><path d="M8 7V3h8v4M3 12h18M10 12v3h4v-3"/>',
'folder':'<path d="M3 6h7l2 3h9v12H3zM5 6V3h9l3 4"/>',
'network':'<circle cx="5" cy="5" r="3"/><circle cx="19" cy="12" r="3"/><circle cx="5" cy="19" r="3"/><path d="m8 6 8 4M8 18l8-4M5 8v8"/>',
'message':'<path d="M4 3h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-9l-5 4v-4H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zM7 10h.01M12 10h.01M17 10h.01"/>',
'pencil':'<path d="m3 21 5-1 14-14-5-5L3 15zM14 4l5 5M3 15l5 5"/>',
'search':'<circle cx="10" cy="10" r="7"/><path d="m15 15 7 7"/>',
'globe':'<circle cx="12" cy="12" r="10"/><ellipse cx="12" cy="12" rx="5" ry="10"/><path d="M2 12h20"/>',
'bulb':'<path d="M9 18h6M9 21h6M10 24h4M8 16c0-3-4-4-4-9a8 8 0 0 1 16 0c0 5-4 6-4 9zM12 4v6M12 13v.1"/>',
'chart':'<path d="M2 22h21M4 22V12h5v10M10 22V2h5v20M16 22V8h5v14"/>',
'rocket':'<path d="M12 1c4 5 6 10 3 17H9C6 11 8 6 12 1zM8 12l-4 4v5l5-3M16 12l4 4v5l-5-3M10 19l2 4 2-4"/><circle cx="12" cy="8" r="2"/>',
'handshake':'<path d="m2 5 5 1-2 13-4-1zM22 5l-5 1 2 13 4-1M7 7l6-2 4 2M6 15l7 5 5-5-6-5-3 2-2-1 3-4M9 17l2-3M12 19l2-3"/>',
 'target':'<circle cx="11" cy="13" r="9"/><circle cx="11" cy="13" r="5"/><path d="m11 13 11-11M17 2v5h5"/>',
'heart':'<path d="M3 17h5l3-3h4c2 0 2 3 0 3h-4M2 15l3-2 4-1M2 21l4 2 9-3 7-7c1-2-1-3-3-1l-4 3M9 8C4 3 11-1 13 4c3-5 9-1 4 4l-4 4z"/>',
 'stairs':'<path d="M2 22h20v-5h-5v-5h-5v5H7v5M2 12l14-8-2-3 8 1-2 8-2-3L4 15z"/>'}
def ico(n,w=60,color='#4383e6'):
 return f'<svg class="icon" width="{w}" height="{w}" viewBox="0 0 24 26" fill="none" stroke="{color}" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">{icons.get(n,icons["file-pen"])}</svg>'
def pos(x,y,w,h,body,style='',cls=''):
 return f'<div class="{cls}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;{style}">{body}</div>'
def txt(x,y,w,text,size=18,color='#111',weight=400,extra=''):
 return pos(x,y,w,'auto',text,f'font-size:{size}px;color:{color};font-weight:{weight};line-height:1.6;letter-spacing:-.7px;{extra}') .replace('height:autopx','height:auto')
def ph(x,y,w,h): return pos(x,y,w,h,'',cls='ph')
def base(n,title='',ch=1):
 s='<div class="paper"></div><div class="rail"><div class="brand"><span class="logo"></span>MIRICOMPANY</div>'+(f'<span class="chapter">CHAPTER {ch:02}</span>' if n>=4 else '')+'</div>'
 if title:s+=f'<header class="head"><span class="num">{ch:02}</span><span class="title">{title}</span><span class="suffix">|　 MIRICOMPANY</span></header>'
 return s
PAGES={}
# 1 cover
s=pos(1125,55,108,610,'','background:#3d7eea;border-radius:0 26px 26px 0;')
for j,k in enumerate(['file-pen','briefcase','folder','network','message','pencil','search']):
 s+=pos(1176,100+j*83,30,30,ico(k,30,'#dbe8fa'))
 if j<6:s+=pos(1167,150+j*82,48,1,'','background:#bed1ed')
s+=pos(47,37,1104,644,'','background:#fdfdfd;border-radius:15px;box-shadow:22px 23px 40px #0003')
s+=txt(151,112,700,'<span style="display:inline-block;background:#e5e5e5;width:23px;height:23px;vertical-align:middle;border-radius:4px"></span> MIRICOMPANY',23,'#4383e6',750)
s+=txt(149,182,950,'MIRICOMPANY',82,'#000',750,'letter-spacing:-2px;line-height:1.2;min-height:1.5em')+txt(149,259,1000,'ONBOARDING BOOK',78,'#4383e6',750,'letter-spacing:-1.7px;line-height:1.2;min-height:1.5em')
s+=txt(150,372,920,'미리컴퍼니 사내 교육 입문 프로그램',35,'#333',400)
s+=pos(151,504,898,1,'','background:#c6c6c6')+pos(156,530,137,34,'ONBOARDING','background:#000;color:white;font-size:13px;','pill')
s+=txt(316,535,740,'인사팀 김미리 대리　 |　 010.1234.5678　 |　 miri_kim@miri.com　 |　 www.miricompany.com',14,'#888')
PAGES[1]=s
#2 index
s=base(2)+txt(400,130,480,'INDEX',74,'#000',750,'text-align:center;line-height:1.25;min-height:1.5em')+pos(127,240,1025,1,'','background:#c8c8c8')
for i in range(8):
 x=174+(i//4)*486;y=294+(i%4)*80
 s+=pos(x,y,451,64,'','background:#ececec;border-radius:999px')+pos(x,y+4,56,56,f'{i+1:02}','background:#4383e6;color:#fff;font-size:20px;font-weight:700;','pill')+txt(x+78,y+15,360,'목차를 이곳에 입력해주세요',22)
PAGES[2]=s
#3 chapter
PAGES[3]=base(3)+txt(300,202,680,'CHAPTER',74,'#000',750,'text-align:center;line-height:1.3;min-height:1.5em')+txt(400,276,480,'01',74,'#4383e6',700,'text-align:center;line-height:1.3;min-height:1.5em')+pos(191,461,898,1,'','background:#c8c8c8')+txt(260,482,760,'해당 챕터의 핵심 키워드와 궁극적 목적 문장을 적어주세요.<br>주제에 대한 세부 내용을 기재해주세요.<br>페이지에서 말하고자하는 내용을 적어주세요.',20,'#aaa',400,'text-align:center;line-height:1.55')
#4
s=base(4,'환영 인사',1)+ph(744,112,400,608)
s+=txt(177,250,560,'이곳에 기업 철학이나 기업을<br><span style="background:#000;color:white;padding:0 12px">대표하는 핵심 메시지를 적어주세요</span>',35,'#000',400,'line-height:1.55')
s+=pos(130,251,42,42,'<svg width="42" height="42" viewBox="0 0 42 42"><path d="M2 32V17L11 3h9L12 17h8v15zM24 32V17L33 3h9L34 17h8v15z"/></svg>')+pos(720,307,42,42,'<svg width="42" height="42" viewBox="0 0 42 42"><path d="M2 2v15L11 31h9l-8-14h8V2zM24 2v15l9 14h9l-8-14h8V2z"/></svg>')
s+=txt(176,389,560,'신입사원 여러분들, 미리컴퍼니에 오신 것을 진심으로 환영합니다.<br>이곳에 CEO 환영 인사말을 텍스트로 입력해주세요.<br>관련 내용을 이곳에 텍스트로 입력해주세요. 텍스트를 입력해주세요.<br><br>이곳에 CEO 환영 인사말을 텍스트로 입력해주세요.<br>관련 내용을 이곳에 텍스트로 입력해주세요. 텍스트를 입력해주세요.',17,'#888',400,'line-height:1.7')+txt(177,588,260,'대표이사　 <span style="font-family:Pen;font-size:36px">김　미　리</span>',19,'#111')
PAGES[4]=s
#5
s=base(5,'긴 글이 있는 레이아웃')+ph(753,250,420,395)
s+=txt(110,271,610,'이 페이지의 핵심내용을 입력해주세요.',24,'#444',700)+txt(110,326,622,'해당 페이지는 많은 분량 텍스트를 입력할 때 쓰기 좋은 페이지입니다.<br>10줄 이상의 텍스트를 넣어야 할 때 이 페이지를 활용해보세요.<br>중요한 내용이나 길게 의견을 보여주어야 할 경우 해당 페이지를 활용해보세요.<br>가독성의 핵심은 얼마나 내용을 간결하게 전달하는가 입니다.<br>쉽게 읽을 수 있고, 눈에 잘 띄는 것이 중요해요.',19,'#555',400,'line-height:1.65')+txt(110,516,610,'- 전체적인 톤앤매너와 맞는 폰트와 색상 등을 활용해주세요.<br>- 강조하고 싶은 부분은 볼드체 또는 큰 사이즈로 표현해보세요.<br>- 구체적인 예시나 수치 등을 활용하면 좋습니다.',16,'#888',400,'line-height:1.65')
PAGES[5]=s
#6 donut
s=base(6,'미리컴퍼니 인재상')+pos(181,253,101,30,'전문성','background:#333;color:#fff;font-size:16px','pill')+txt(289,255,850,'이곳에 관련 내용을 텍스트로 간략하게 입력해주세요. 관련 내용을 이곳에 입력해주세요. 관련 내용을 간략하게 입력해주세요.',14,'#888')
s+=pos(516,319,248,248,'','border-radius:50%;background:conic-gradient(from -60deg,#333 0 32%,#fff 32% 33.5%,#4383e6 33.5% 66.5%,#fff 66.5% 68%,#383c51 68% 99%,#fff 99% 100%)')+pos(555,357,170,170,'','background:#fdfdfd;border-radius:50%')
s+=pos(574,400,132,125,'<svg width="132" height="125" viewBox="0 0 132 125"><path d="M2 4 66 42 130 4M66 42v75" stroke="#cbd0cf" stroke-width="2" fill="none"/><g fill="#cbd0cf"><circle cx="2" cy="4" r="4"/><circle cx="130" cy="4" r="4"/><circle cx="66" cy="117" r="4"/></g></svg>')+pos(639,292,2,27,'','background:#444')+pos(468,430,49,1,'','background:#383c51')+pos(764,430,47,1,'','background:#4383e6')
for x,c,t in [(347,'#383c51','주도성'),(832,'#4383e6','책임감')]:s+=pos(x,413,101,30,t,f'background:{c};color:#fff;font-size:16px','pill')
s+=txt(128,457,320,'이곳에 관련 내용을 텍스트로 간략하게<br>입력해주세요. 관련 내용을 이곳에 입력해주세요.<br>관련 내용을 간략하게 입력해주세요.',16,'#888',400,'text-align:right;line-height:1.65')+txt(832,457,350,'이곳에 관련 내용을 텍스트로 간략하게<br>입력해주세요. 관련 내용을 이곳에 입력해주세요.<br>관련 내용을 간략하게 입력해주세요.',16,'#888',400,'line-height:1.65')+pos(97,601,1083,48,'미리인은 전문성을 바탕으로 주도적으로 목표를 달성하며 모든 과정에서 책임을 다하는 인재입니다.','background:#eaeaea;font-size:21px;','pill')
PAGES[6]=s
#7
s=base(7,'5줄 리스트 레이아웃')
entries=[('조직 및 역할 이해','조직 구조 및 신입사원의 기본 역할을 이해합니다.'),('기초 역량 개발','사회적 기술과 대인 관계 능력을 키워 조직 적응력을 높입니다.'),('직무 능력 배양','기본적인 직무 기술과 실무 역량을 강화합니다.'),('협업 및 협력 능력 강화','팀 내 원활한 의사소통과 협업 능력을 증진합니다.'),('발전성 구축','지속적인 자기 개발을 통해 성장형 인재로 발전합니다.')]
for i,(a,b) in enumerate(entries):
 y=267+i*75;s+=pos(151,y,977,54,'','background:#ececec;border-radius:999px')+pos(151,y,302,54,f'{i+1:02}.　{a}',f'background:{"#4383e6" if i%2==0 else "#383c51"};color:white;font-size:21px;font-weight:600;','pill')+txt(508,y+13,600,b,19,'#333')
PAGES[7]=s
#8
s=base(8,'미리컴퍼니의 이념')
for x,y,c,n,ic in [(239,248,'#383c51','VISION','globe'),(142,414,'#333','MISSION','file-pen'),(334,414,'#4383e6','VALUES','bulb')]:
 s+=pos(x,y,212,212,'',f'background:{c};border-radius:50%;outline:9px solid #fdfdfd')+pos(x+82,y+54,48,54,ico(ic,46,'white'))+txt(x+10,y+117,192,n,23,'white',500,'text-align:center')
for i,(n,detail) in enumerate([('VISION','회사의 미래 목표와 지향점을 간결하고<br>명확하게 적어보세요. 텍스트를 간략하게 입력해주세요.'),('MISSION','회사의 존재 이유와 핵심 활동을<br>구체적으로 설명해보세요. 관련 내용을 입력해주세요.'),('VALUES','회사가 중요하게 여기는 핵심 가치에 대한<br>설명을 이곳에 입력해보세요.')]):
 y=271+i*116;s+=pos(581,y,576,101,'','background:#f0f0f0;border-radius:10px')+txt(614,y+34,130,'• '+n,19,'#4383e6' if i==2 else '#383c51',600)+pos(737,y+18,1,64,'','background:#bfbfbf')+txt(764,y+25,370,detail,16,'#888',400,'line-height:1.65')
PAGES[8]=s
#9 org chart
s=base(9,'미리컴퍼니 조직도')+pos(551,256,178,41,'CEO : 김미리','background:#4383e6;color:white;font-size:16px','pill')
s+=pos(640,301,1,18,'','background:#ccc')+pos(380,318,521,39,'','border:1px solid #ccc;border-bottom:0;border-radius:14px 14px 0 0')
for x,n in [(299,'COO'),(801,'CFO')]:s+=pos(x,354,162,38,n,'background:#333;color:white;font-size:16px','pill')
s+=pos(379,400,1,15,'','background:#ccc')+pos(901,400,1,15,'','background:#ccc')+pos(189,415,900,39,'','border:1px solid #ccc;border-bottom:0;border-radius:14px 14px 0 0')
for i in range(5):
 x=132+i*224;s+=pos(x+57,416,1,35,'','background:#ccc')+pos(x,450,120,37,f'부서 {i+1}',f'background:{"#4383e6" if i%2==0 else "#383c51"};color:white;font-size:16px','pill')+pos(x+57,490,1,15,'','background:#ccc')
 for j in range(3):s+=pos(x,506+j*43,120,37,f'팀 {j+1}','background:#dcdcdc;font-size:16px','pill')
PAGES[9]=s
#10 steps col
s=base(10,'3가지 핵심 업무 원칙',2)
copy=['이 페이지는 비즈니스 프로세스를 한눈에 볼 수 있는 페이지입니다. 각 단계가 진행됨에 따라 세부 내용을<br>입력해 보세요.','이 페이지를 사용하여 비즈니스의 흐름을 설계해 보세요. 확장 과정을 단계별로 입력해 주시기 바랍니다.<br>각 단계별 액션과 세부 내용을 입력하여 성장 과정을 시각화하세요.','단계를 나누어 각 단계가 전체 흐름에 어떻게 기여하는지 설명해 주세요. 비즈니스 프로세스의 시작부터<br>끝까지 시각적으로 구성해 보세요. 이해와 전달력이 향상됩니다.']
for i in range(3):
 y=249+i*143;c=['#4383e6','#383c51','#333'][i];s+=pos(120,y,1040,122,'','background:#efefef')+pos(120,y,234,122,f'Step {i+1}',f'background:{c};color:white;font-size:27px;font-weight:700;border-radius:0;','pill')+txt(379,y+16,750,f'Step {i+1} 키워드 입력',19,'#000',650)+txt(379,y+48,760,copy[i],16,'#777',400,'line-height:1.8')
 if i<2:s+=pos(227,y+121,20,10,'',f'background:{c};clip-path:polygon(0 0,100% 0,50% 100%)')
PAGES[10]=s
#11 architecture cards
s=base(11,'3가지 핵심 업무 원칙',2)+txt(350,236,580,'업무 원칙과 관련된 단계별 내용',18,'#4383e6',700,'text-align:center')+pos(80,278,1119,54,'상위 단계에 해당하는 내용을 입력하세요','background:#5c91e7;border-radius:3px;color:white;font-size:19px;font-weight:650;display:flex;align-items:center;justify-content:center')
for i in range(3):
 x=80+i*378;s+=pos(x,347,364,142,'중간 단계에 해당하는 내용을 입력하세요.<br>2~3줄로 정리해봅시다.','background:#eef2f8;border-radius:10px;color:#4383e6;font-size:17px;font-weight:650;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1.6')+pos(x,503,364,142,'','background:#eaeaea;border-radius:10px')+txt(x+28,520,270,'<b>OOO</b> 상승',22,'#444')+txt(x+28,558,255,'세부 내용을 입력하세요.<br><b>2~3줄</b>로 정리해봅시다.',16)+pos(x+280,569,58,60,ico(['stairs','chart','bulb'][i],58,'#000'))
PAGES[11]=s
#12 mission
s=base(12,'4가지 핵심 업무 원칙',2)
for i,n in enumerate(['Our Mission','Our Vision']):
 y=284+i*193;s+=pos(151,y,155,35,n,'background:#555;color:white;font-size:18px;font-weight:600','pill')+txt(151,y+44,380,'기업의 존재의의를 명확하게<br>전달 해 보세요.',30,'#000',500,'line-height:1.45')
s+=txt(607,277,540,'대표나 경영진 등의 메시지를 게재 해 보세요. 프레젠테이션 자료나 회사 소개 자료에서는 경영진의 한마디가 신뢰성과 스토리텔링을 높이는 효과가 있습니다.<br><br>예를 들면, 왜 창업을 하게 되었는지에 대한 이야기나, 비전이나 미션에 대한 자세한 설명 등도 기업이 사업을 통해 이루고 싶은 미래에 대해 상대에게 보다 효과적으로<br>전달할 수 있게 됩니다. 기업이 소중히 여기는 가치관이나 사원 · 고객 · 파트너에게 향하는 메시지 등을 기재 해 보세요.',14,'#111',400,'line-height:1.75')+txt(607,474,300,'대표나 경영진 등의 메시지를 게재 해 보세요.<br>프레젠테이션 자료나 회사 소개 자료에서는<br>경영진의 한마디가 신뢰성과 스토리텔링을 높이는<br>효과가 있습니다. 기업이 소중히 여기는 가치관이나<br>사원 · 고객 · 파트너에게 향하는 메시지 등을<br>기재 해 보세요.',14,'#111',400,'line-height:1.7')+ph(933,471,196,145)
PAGES[12]=s
#13 hub semicircle
s=base(13,'4가지 핵심 업무 원칙',2)+pos(393,443,494,494,'','border:4px solid #ddd;border-radius:50%')+pos(503,548,274,274,'','background:#dcdcdc;border-radius:50%')+txt(550,615,180,'KEYWORD',25,'#4383e6',650,'text-align:center')
for i,(x,y,c,ic) in enumerate([(363,527,'#4383e6','target'),(490,410,'#383c51','heart'),(679,410,'#4383e6','bulb'),(806,527,'#383c51','file-pen')]):s+=pos(x,y,111,111,'',f'background:{c};border-radius:50%')+pos(x+35,y+30,43,50,ico(ic,43,'white'))
for i,(x,y,c,n) in enumerate([(136,487,'#4383e6','목　적'),(386,268,'#383c51','열　정'),(702,268,'#4383e6','책　임'),(953,487,'#383c51','보　고')]):
 s+=pos(x,y,192,48,n,f'background:{c};color:white;font-size:23px;font-weight:650;box-shadow:0 1px 4px #0003','pill')+pos(x+(156 if i<2 else 0),y+4,38,38,f'{i+1:02}',f'background:{c};color:white;font-size:18px;border:2px solid #fff','pill')+txt(x-18,y+70,225,'이곳에 관련 내용을 텍스트로 간략하게<br>입력해주세요. 관련 내용을 이곳에 입력해주세요.',15,'#888',400,'text-align:center;line-height:1.7')
PAGES[13]='<div style="position:absolute;inset:0;clip-path:inset(0 0 38px 0)">'+s+'</div>'
#14 overlapping circle keywords
s=base(14,'상세 키워드 프로세스',3)+pos(256,241,761,238,'','border:4px solid #ddd;border-radius:999px')
for i in range(4):
 x=275+i*171;c='#5b91e8' if i%2==0 else '#55596a'
 s+=pos(x,257,211,211,'',f'background:{c};border-radius:50%;opacity:.96')+txt(x+30,321,151,'ENTER A<br>KEY WORD',16,'white',750,'text-align:center;line-height:1.1')+txt(x+30,375,151,'키워드를<br>입력해주세요',14,'white',400,'text-align:center;line-height:1.5')+pos(x+105,468,1,36,'','border-left:1px dotted #bbb')+pos(x+101,502,8,8,'','background:#999;border-radius:50%')+txt(x+35,515,140,'키워드 '+chr(65+i),14,'#555',500,'text-align:center')
 x2=61+i*292;s+=pos(x2,576,279,90,'','background:#f1f1f1;border-radius:8px')+txt(x2+20,585,240,'키워드 '+chr(65+i),14,'#555',600)+txt(x2+20,610,240,'키워드와 관련된 상세 텍스트를 자유롭게<br>입력해주세요. 핵심 내용 위주로 나열해주세요.',13,'#888',400,'line-height:1.5')
PAGES[14]=s
#15 four steps
s=base(15,'단계별 레이아웃',3)
steptexts=['이 페이지는 비즈니스 프로세스를<br>한눈에 볼 수 있는 페이지입니다.<br>각 단계가 진행됨에 따라<br>세부내용을 입력해 보세요.','단계별로 주요 활동과 목표를<br>작성해 주세요. 이를 통해<br>프로세스의 완성도를 높일 수<br>있습니다.','프로세스 전체의 흐름을 보다 간단<br>하게 이해할 수 있도록, 중요한 포<br>인트를 간결하게 정리해<br>보세요.','이 스텝에서 어떤 액션을 취할건지<br>알려주세요. 듣는 사람의<br>입장에서 프로세스의 상세한<br>내용을 적어보세요.']
for i in range(4):
 x=122+i*280;s+=pos(x,251,196,196,'','background:#e9f0f9;border-radius:50%')+pos(x+66,306,70,80,ico(['handshake','bulb','chart','rocket'][i],70))+txt(x+10,465,176,f'Step {i+1}',21,'#000',600,'text-align:center')+txt(x-30,507,258,steptexts[i],17,'#888',400,'text-align:center;line-height:1.6')
 if i<3:s+=pos(x+231,328,16,50,'','background:#c9ecf7;clip-path:polygon(0 0,100% 50%,0 100%)')
PAGES[15]=s
#16 lists
s=base(16,'일자별 리스트 레이아웃',3)
days=[['OT 및 회사 투어','회사 비전 및 조직 문화 이해','팀 빌딩 활동','선배와의 Q&A','교육명을 입력하세요'],['기본 비즈니스 매너','커뮤니케이션 스킬','사업부와 부서 이해','실습 활동','교육명을 입력하세요'],['보고 및 스피치 스킬','팀별 과제 발표','피드백 세션','교육 수료식','교육명을 입력하세요']]
for i in range(3):
 x=161+i*326;s+=pos(x+20,261,266,53,f'{i+1}일차',f'background:{"#4383e6" if i!=1 else "#383c51"};color:white;font-size:22px;border-radius:14px 14px 0 0;display:flex;align-items:center;justify-content:center')+pos(x,306,306,324,'','background:#f0f0f0;border:2px solid white;border-radius:12px;box-shadow:0 2px 15px #0001')
 for j,t in enumerate(days[i]):
  s+=txt(x+29,328+j*61,260,'•　'+t,21,'#333')
  if j<4:s+=pos(x+28,373+j*61,250,1,'','background:#c5c5c5')
PAGES[16]=s
#17 kpi
s=base(17,'KPI 프로세스',3)
for i,c in enumerate(['#b4caf1','#709fe9','#4383e6']):
 y=228+i*144;s+=pos(98,y,290,137,'사업명을 입력',f'background:{c};color:#fff;font-size:23px;border-radius:4px;display:flex;align-items:center;justify-content:center')+pos(393,y,807,137,'','background:#eaeaea')
 for j,unit in enumerate(['원','개','명']):
  x=415+j*269;s+=txt(x,y+10,230,'키워드 입력',19,'#444')+txt(x+15,y+39,209,f'<b style="font-size:43px">000</b> {unit}',30,'#444',400,'text-align:right')+txt(x,y+99,235,'전년 동기 대비 00% 상승' if j==0 else '수치에 대한 부가 설명을 입력해주세요.',12,'#000',650,'text-align:center')
  if j<2:s+=pos(x+247,y+24,1,90,'','background:#555')
PAGES[17]=s
#18 photo list
s=base(18,'사진을 활용한 레이아웃',4)+ph(97,265,493,330)
for i in range(3):
 y=265+i*114;s+=pos(607,y,576,101,'','background:#f0f0f0;border-radius:10px')+txt(639,y+34,125,f'•　POINT {i+1:02}',19,'#383c51',600)+pos(762,y+18,1,64,'','background:#c7c7c7')+txt(790,y+25,370,'사진의 상세 내용을 이 곳에 요약하여<br>명확하게 적어보세요. 텍스트를 간략하게 입력해주세요.',16,'#888',400,'line-height:1.65')
PAGES[18]=s
#19 three photos
s=base(19,'사진을 활용한 레이아웃',4)+pos(96,237,108,397,'주요<br>이미지','background:#4383e6;color:white;font-size:18px;border-radius:3px;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1.5')
for i in range(3):
 x=220+i*326;s+=ph(x,237,311,267)+pos(x,517,311,117,'','background:#f0f0f0;border-radius:10px')+txt(x+27,540,260,'사진의 상세 내용을 이 곳에 요약하여<br>명확하게 적어보세요. 텍스트를 간략하게<br>입력해주세요.',16,'#888',400,'line-height:1.55')
PAGES[19]=s
for n,s in PAGES.items():
 (R/f'slide_{n:02}.html').write_text(f'<!doctype html><html lang="ko"><meta charset="utf-8"><title>078 / {n:02}</title><link rel="stylesheet" href="replica.css"><body><section class="slide">{s}</section></body></html>')
(P/'replica-data.json').write_text(json.dumps({'pages':19,'font':'Noto Sans KR','placeholder_pages':[1,4,5,12,18,19]},ensure_ascii=False,indent=2))
print('replicas',len(PAGES))
