from pathlib import Path
import shutil,json
R=Path('/workspace/work/deliverables/dockside');V=R/'review';P=V/'replica';P.mkdir(parents=True,exist_ok=True)
(V/'assets').mkdir(exist_ok=True);shutil.copy('/workspace/work/reference/fonts/artifacts/pretendard/PretendardVariable.woff2',V/'assets/font.woff2')
css='''@font-face{font-family:P;src:url('../assets/font.woff2')}*{box-sizing:border-box}html,body{margin:0;width:1280px;height:720px;overflow:hidden}body{font-family:P;color:#303231;background:#fafafa}.slide{width:1280px;height:720px;position:relative;overflow:hidden;background:radial-gradient(ellipse at 110% 95%,#d0eaff75,transparent 45%),radial-gradient(ellipse at 100% 3%,#e6f4d970,transparent 25%),#fafafa}.slide:before{content:'';position:absolute;inset:0;pointer-events:none;background:repeating-linear-gradient(47deg,transparent 0 47px,#a5d3f017 48px 95px);clip-path:polygon(71% 0,100% 0,100% 100%,92% 100%)}.slide.cover:before{clip-path:polygon(0 50%,100% 50%,100% 100%,0 100%);background:repeating-linear-gradient(47deg,transparent 0 46px,#a5d3f028 47px 94px)}.slide.cover:after,.slide.index:after{content:'';position:absolute;bottom:0;left:0;width:100%;height:15px;background:#3297ec}.business{position:absolute;right:47px;top:38px;font-size:13px;color:#888}.brand{position:absolute;top:35px;left:47px;font-size:15px;letter-spacing:1px;font-weight:700}.brand b{color:#389ee8;font-size:25px;margin-right:10px}.rail{position:absolute;top:0;bottom:0;left:0;width:104px;border-left:15px solid #3299ef;background:#f2f2f2;padding:12px 15px;display:flex;flex-direction:column;justify-content:space-between}.rail .seat{width:58px;height:58px;border-radius:12px;border:2px solid white;background:#e8e8e8;box-shadow:0 7px 15px #00000005;font-size:10px}.rail:after{content:'';position:absolute;top:var(--rail-y,110px);left:0;border-left:19px solid #3299ef;border-top:13px solid transparent;border-bottom:13px solid transparent}.chapter{position:absolute;left:143px;top:94px;min-width:120px;height:39px;border-radius:999px;background:#303231;color:white;display:flex;align-items:center;justify-content:center;font-size:14px;box-shadow:0 6px 10px #0002}.title{position:absolute;left:143px;top:153px;margin:0;font-size:53px;line-height:1.14;letter-spacing:-2.7px;font-weight:600;max-width:1050px}.title b{color:#409ae0;font-weight:600}.aside{position:absolute;left:143px;top:525px;width:245px}.aside b{display:block;color:#398fd0;font-size:18px;font-weight:500;margin-bottom:19px}.aside b:after{content:'';display:block;width:27px;height:1px;background:#398fd0;margin-top:11px}.aside p{font-size:14px;line-height:1.55;color:#7a7c7c;margin:0}.intro{position:absolute;left:712px;top:141px;width:490px;font-size:14px;line-height:1.6;color:#777}.box{position:absolute;border:2px solid #fff;border-radius:24px;background:linear-gradient(150deg,#ffffff80,#f6f6f6aa);box-shadow:0 10px 25px #00000009;padding:25px}.box h3{font-size:20px;letter-spacing:-.6px;margin:15px 0;color:#363936;font-weight:600}.box p,.box li{font-size:14px;line-height:1.6;color:#737777}.box p{margin:0}.box ul{padding-left:18px;margin:10px 0}.seat{background:#e7e7e7;display:flex;align-items:center;justify-content:center;color:#969696;font-size:13px;overflow:hidden}.circle{border-radius:50%}.image{border-radius:18px;width:100%;height:235px}.pill{border:2px solid #fff;border-radius:999px;background:#349cf5;color:white;min-height:43px;display:flex;align-items:center;justify-content:center;padding:0 23px;font-size:15px;box-shadow:0 6px 12px #248edf44}.pill.dark{background:#303331;color:white;box-shadow:0 4px 9px #0002}.arrow{position:absolute;right:15px;bottom:20px;width:47px;height:47px;border-radius:50%;background:#303331;color:#fff;display:grid;place-items:center;box-shadow:0 7px 12px #0002}.arrow svg{width:26px;height:26px;stroke:currentColor;fill:none;stroke-width:1.5}.plus{position:absolute;right:18px;top:-19px;width:43px;height:43px;border-radius:50%;background:#303331;color:white;display:grid;place-items:center;font-size:25px;font-weight:300;box-shadow:0 6px 12px #0003}.check{width:23px;height:23px;background:#329ef5;border:3px solid #bce4ff;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;margin-right:15px;color:#fff;font-size:12px;flex:none}.check:before{content:'';width:8px;height:5px;border-left:1.5px solid currentColor;border-bottom:1.5px solid currentColor;transform:rotate(-45deg);margin-top:-3px}.row{position:absolute;display:flex;align-items:center;gap:20px}.row .text{font-size:16px;color:#777;line-height:1.5}.small{font-size:14px;color:#777;line-height:1.6}.center{text-align:center}.donut{position:absolute;border-radius:50%;background:conic-gradient(#329bf1 0 var(--pct),#eee var(--pct) 360deg);border:20px solid #fff;box-shadow:0 8px 22px #0000000a;display:grid;place-items:center}.donut:before{content:'';position:absolute;inset:14px;border-radius:50%;background:#fafafa}.donut .inside{z-index:1;text-align:center}.donut b{font-size:44px}.donut p{font-size:17px;margin:15px 0}.line{position:absolute;background:#ddd}.iconbox{background:#329cf4;display:grid;place-items:center;border-radius:8px;color:white;box-shadow:0 6px 12px #2589d84d}.iconbox svg{width:55%;height:55%;fill:none;stroke:currentColor;stroke-width:1.4}.cover-nav{position:absolute;left:75px;top:38px;right:75px;height:59px;border-radius:999px;box-shadow:0 0 18px #0000000a;border:2px solid #fff;background:#ffffff50;display:flex;align-items:center;padding:0 18px;font-size:16px;letter-spacing:1px}.cover-nav .circle{width:40px;height:40px;background:#303331;color:white;display:grid;place-items:center;font-weight:700;font-size:23px;margin-right:13px}.cover-nav span{margin-left:auto;color:#888;font-size:14px;letter-spacing:0}.dock{position:absolute;left:38px;right:38px;bottom:36px;display:flex;align-items:flex-end;justify-content:space-between}.dock .seat{width:90px;height:90px;border:2px solid #fff;border-radius:22px;background:#ffffff60;box-shadow:0 5px 18px #2775a509}.dock .seat.focus{width:145px;height:145px;margin-bottom:10px}.capsule{border:2px solid #fff;border-radius:999px;background:#ffffff90;box-shadow:0 8px 14px #0000000a}.num{font-size:30px;font-weight:300;color:#bbb}.item-title{font-size:18px;color:#333;font-weight:600}.connector{position:absolute;border-top:2px solid #ddd}.connector.vertical{border-top:0;border-left:2px solid #ddd}.footnote{position:absolute;font-size:11px;color:#bbb}.head-icon{width:85px;height:85px;border:2px solid #fff;border-radius:18px}.thin-circle{border:2px solid #fff;border-radius:50%;box-shadow:0 9px 20px #00000008;position:absolute;background:#ffffff20}.button{background:#303331;color:#fff;border-radius:4px;display:flex;align-items:center;justify-content:center;height:42px;padding:0 32px;box-shadow:0 6px 9px #0002;font-size:15px}'''
(P/'replica.css').write_text(css)
A='<span class="arrow"><svg viewBox="0 0 24 24"><path d="M3 12h17M13 5l7 7-7 7"/></svg></span>'
def div(c,x,y,w,h,t='',more=''):return f'<div class="{c}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{more}">{t}</div>'
def seat(x,y,w,h,n=1,extra=''):return div('seat '+extra,x,y,w,h,str(n),'position:absolute;')
def box(x,y,w,h,t='',extra=''):return div('box '+extra,x,y,w,h,t)
def pill(x,y,w,t,dark=False):return div('pill'+(' dark' if dark else ''),x,y,w,43,t,'position:absolute;')
def icon(x,y,w=90,kind='search'):
 path={'search':'<circle cx="10" cy="10" r="6"/><path d="m15 15 5 5"/>','light':'<path d="M9 18h6m-6 3h6M9 15a7 7 0 1 1 6 0v3H9z"/>','chart':'<path d="M4 20V10h4v10m2 0V4h4v16m2 0v-7h4v7"/>','gear':'<circle cx="12" cy="12" r="4"/><path d="m10 3 4 0 1 3 3 1 3 4-2 3-1 4-4 3-3-2-4-1-3-4 2-3 1-4z"/>','people':'<circle cx="8" cy="7" r="3"/><circle cx="17" cy="8" r="2"/><path d="M2 21v-6l6-3 6 3v6m1-7 5 2v5"/>'}.get(kind,'<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/>')
 return div('iconbox',x,y,w,w,f'<svg viewBox="0 0 24 24">{path}</svg>','position:absolute;')
def small(t):return f'<p class="small">{t}</p>'
C=[]
def add(t):C.append(t)
def base(n,title='',chapter='',aside=None,intro=None,cover=False,index=False):
 global C;C=[]
 if cover:
  add('<div class="cover-nav"><b class="circle">w</b><b>Miri Company</b><span>Innovation　　　Strategy　　　Proposal　　　Project</span></div>')
 else:
  add('<div class="business">Business Presentation</div>')
  if index:add('<div class="brand"><b>w</b>Miri Company</div>')
  else:add('<div class="rail">'+''.join(f'<div class="seat">{i}</div>' for i in range(1,10))+'</div>')
 if chapter:add(f'<div class="chapter">Chapter {chapter:02}</div>')
 if title:add(f'<h1 class="title">{title}</h1>')
 if aside:add(f'<div class="aside"><b>{aside[0]}</b><p>{aside[1]}</p></div>')
 if intro:add(div('intro',712,141,490,60,intro))
def save(n,cover=False,index=False):
 text='<!doctype html><html lang="ko"><meta charset="utf-8"><title>Dockside replica '+str(n)+'</title><link rel="stylesheet" href="replica.css"><body><section class="slide'+(' cover' if cover else '')+(' index' if index else '')+'">'+''.join(C)+'</section></body></html>'
 (P/f'slide_{n:02}.html').write_text(text)
DEFAULT='해당 기능이 어떻게 작동하는지, 사용자에게 어떤 정보를 제공하는지 작성합니다. 구체적인 예시를 포함해 설명하세요.'
# 1
base(1,cover=True);add(div('center',180,231,920,230,'<div style="font-size:70px;color:#449fdd;letter-spacing:-4px">번뜩이는 생각 그대로</div><div style="font-size:88px;line-height:1.4;letter-spacing:-5px;font-weight:600">아이디어 피칭</div>','position:absolute;'));add('<div class="dock">'+''.join(f'<div class="seat {"focus" if i==5 else ""}">{i}</div>' for i in range(1,10))+'</div>');save(1,cover=True)
# 2
base(2,cover=True);add(div('center',190,227,900,100,'<h1 style="font-size:64px;letter-spacing:-3px;font-weight:600;margin:0"><b style="color:#429ad9">아이디어</b> 키워드 입력</h1>','position:absolute;'));add(div('capsule row',265,365,750,95,seat(12,7,78,78,1,'circle')+'<div style="margin-left:120px;font-size:21px;color:#777">아이디어를 한 문장으로 요약하여 입력합니다.</div>'));add(pill(883,385,114,'View',True));
for j in range(4):add(div('capsule center',265+j*192,492,180,58,f'Keyword 0{j+1}','position:absolute;padding:18px;font-size:15px;color:#777'))
save(2,cover=True)
# 3
base(3,index=True);add(pill(579,113,122,'Index',True));add(div('center',300,181,680,70,'<h1 style="font-size:54px;margin:0;font-weight:600">목차 안내</h1>','position:absolute;'))
for j,(a,b) in enumerate([('우리가<br>발견한 <b>문제</b>','01'),('아이디어와<br><b>실행 방법</b>','02'),('기대효과와<br><b>계획</b>','03')]):
 add(box(85+j*380,325,343,335,f'<div class="num">{b}</div><h3 style="font-size:26px;line-height:1.2">{a}</h3><hr style="border:0;border-top:1px solid #e5e5e5"><ul><li>이곳에 하위 항목을 입력합니다.</li><li>항목이 여러개인 경우 글머리표를 활용해 정리합니다.</li></ul>'+A));add(seat(350+j*380,347,48,48,j+1))
save(3,index=True)
# 4
base(4,'현재 상황',1,('Current Situation','문제 인식을 공유하고 방향성을 설정하는 단계입니다.'));add(box(444,113,755,549,'<div class="small" style="color:#bbb;margin-bottom:25px">Content Brief</div>'));texts=['시장 또는 타깃 고객이 처한 상황을 구체적으로 작성합니다.','가능한 수치나 사례를 포함하면 효과적입니다.','해당 상황에서 발생하는 주요 문제점이나 불편함을 작성합니다.','기존 해결책의 한계를 설명합니다.','핵심 내용을 가로로 나열해 강조하세요.']
for j,t in enumerate(texts):add(div('capsule row',477,185+j*94,687,76,f'<span class="check"></span><span class="text">{t}</span>','padding:0 26px;'))
add(div('plus',1124,125,45,45,'+'));save(4)
#5
base(5,'현재 상황',1,('Current Situation','현재 상황을 보여주는 주요 지표에 대해 그래프로 나타냅니다.'))
for j,t in enumerate(['전년 대비 이용자수 증가율','고객 중 불편을 느끼는 비율']):add(box(445+j*402,210,360,400));add(pill(477+j*402,166,305,'✓　'+t))
add(div('',530,283,110,222,'<div style="height:142px;background:#329ef5;color:white;padding:45px 20px;text-align:center;border-radius:10px 10px 0 0">20XX<br>XXX,XXX명</div><div style="height:80px;background:#ddd;text-align:center;padding-top:25px">20XX</div>','position:absolute;'));add(pill(650,385,104,'+150% 증가',True));add(div('small center',484,540,283,70,'이용자 수 150% 증가로 운영 부담과<br>매출 가능성이 높아졌습니다.','position:absolute;'));add(div('donut',966,277,178,178,'<div class="inside"><span>20XX</span><br><b style="font-size:36px">40%</b></div>','--pct:40%;'));add(div('thin-circle center',894,404,111,111,'<div style="font-size:24px;margin-top:34px">20%</div>','background:#eee;'));add(pill(1090,455,101,'2배 증가',True));add(div('small center',878,540,283,70,'불편 경험 비율이 2배 증가하며 서비스 개선<br>필요성이 분명해졌습니다.','position:absolute;'));save(5)
#6
base(6,'페인포인트',2,('Pain Point','고객의 페인 포인트를 시각적으로 표현하는 페이지 입니다.'))
for j,(t,desc) in enumerate([('눈길을 끄는 시각 자료','이미지와 설명을 함께 배치해 내용을 직관적으로 전달하는 가장 효과적인 페이지입니다.'),('신뢰를 주는 증거 사진','텍스트로만 설명하기 어려운 분위기나 디테일을 시각 자료로 보여주면 이해가 빨라집니다.')]):
 x=435+j*401;y=210-j*42;add(box(x,y,365,503,f'<div class="seat image">{j+1}</div><h3 style="color:#499ed6">{t}</h3><p>{desc}</p>'+A))
save(6)
#7
base(7,'페인포인트',2);add(div('thin-circle',165,265,362,362,'','border:1px dashed #88bce0;'));add(div('thin-circle',191,290,312,312,'','border:3px solid #56a9e7;background:linear-gradient(135deg,#fafafa,#b8d5fb);'));add(div('thin-circle center',238,337,218,218,'<p class="small" style="margin-top:40px">Keyword</p><div class="seat circle" style="width:70px;height:65px;margin:auto">1</div><b style="color:#4296ce;font-size:23px">중심 키워드</b>'));add(div('plus',435,307,39,39,'+'))
for j,(a,b) in enumerate([('Problem 01','시간 소요'),('Problem 02','비용 부담'),('Problem 03','정보 부족'),('Problem 04','접근성 제한')]):
 add(box(594,209+j*122,635,95,'', ''));add(pill(612,233+j*122,140,a));add(div('item-title',774,245+j*122,130,37,b,'position:absolute;'));add(div('small',910,235+j*122,283,60,'구체적인 불편사항이나 문제상황을 간단히 작성합니다.','position:absolute;border-left:1px solid #ddd;padding-left:20px;'))
save(7)
#8
base(8,'우리의 <b>인사이트</b>',3,intro='데이터와 관찰을 바탕으로 시장 변화와 고객 니즈를 해석하고, 이를 통해 도출한 핵심 인사이트와 비즈니스 기회를 정리하는 페이지입니다.')
for j,(t,d) in enumerate([('시장 트렌드','시장이나 고객 행동의 변화 트렌드를 작성합니다. 회사의 전체를 대상으로 구체적인 변화 양상을 2~3줄로 서술하세요.'),('충족되지 않은 니즈','현재 시장에서 충족되지 못한 고객의 숨은 요구나 불편을 작성합니다. 어떤 문제가 반복되는지 짧은 요소를 정리하세요.'),('기회 포착','트렌드와 니즈를 바탕으로 발견한 비즈니스 기회를 작성합니다. 기대 효과나 차별화 포인트를 간단히 제시하세요.')]):
 x=190+j*347;add(box(x,328,314,306,f'<div style="height:132px"></div><h3 class="center">{t}</h3><p>{d}</p>'));add(div('pill',x,307,314,62,f'INSIGHT 0{j+1}','position:absolute;border-radius:5px;justify-content:flex-start;font-size:13px;'));add(seat(x+110,367,90,90,j+1,'head-icon'));add(div('plus',x+258,322,35,35,'+'))
save(8)
#9
base(9,'우리의<br><b>인사이트</b>',3,('Our Insights','환경과 조건을 바탕으로 핵심 인사이트와 기회를 정리하는 페이지입니다.'))
for j,(t,k) in enumerate([('고객 행동 패턴','search'),('경쟁사의 공백','chart'),('기술적 가능성','light')]):
 y=208+j*146;add(icon(455,y,110,k));add(box(580,y,633,110,f'<h3 style="color:#459bd5;margin:0 0 8px">{t}</h3><p>타깃 고객의 실제 행동이나 구매 패턴에서 발견한 특이점을 작성합니다.</p>'));add(div('plus',1154,y+35,35,35,'›'))
save(9)
#10
base(10,'핵심 <b>아이디어</b>',4,intro='핵심 아이디어와 솔루션의 작동 원리를 한눈에 보여주는 페이지입니다.<br>주요 컨셉과 기능을 간단히 이해할 수 있도록 구성합니다.');add(box(202,220,969,470));add(seat(222,238,925,337,1,'image'));add(pill(249,499,141,'Idea 01'));add(pill(399,499,141,'Idea 02'));add(div('small center',315,597,720,70,'아이디어의 핵심 개념을 한 문장으로 명확하게 작성합니다.<br>이 솔루션이 어떻게 작동하는지 간단한 메커니즘을 설명합니다.','position:absolute;'));add(div('plus',1109,545,48,48,'›'));save(10)
#11
base(11,'아이디어 <b>개요</b>',4);add(seat(210,282,299,438,1,'image'))
for j,t in enumerate(['이곳에 아이디어 또는 핵심 가치를 작성합니다.','솔루션이 제공하는 핵심 기능과 특징을 작성합니다.','어떤 방식으로 문제를 해결하는지 구체적인 접근 방법을 서술합니다.','사용자가 이 솔루션을 통해 얻게 되는 주요 편익이나 경험을 작성합니다.','솔루션의 확장 가능성이나 추가 가치를 설명합니다.']):
 add(box(600,190+j*95,607,77,f'<div class="row" style="position:static;gap:0"><span class="check"></span><div class="text">{t}</div></div>',''))
add(pill(600,190,607,'이곳에 아이디어 또는 핵심 가치를 작성합니다.'));save(11)
#12
base(12,'작동 원리',5,intro='사용자 요청부터 결과 도출까지의 처리 흐름을 단계별로 설명합니다.<br>시스템이 어떻게 작동하는지 전체 과정을 중심으로 보여줍니다.')
for j,t in enumerate(['사용자 입력 및 요청','데이터 처리 및 매칭']):
 x=196+j*509;add(box(x,247,470,398));add(pill(x+20,266,430,t));add(seat(x+20,352,430,195,j+1,'image'));add(div('small',x+25,565,420,70,'• 해당 단계에서 일어나는 주요 동작이나 과정을 작성합니다.<br>• 사용자 또는 시스템의 행동을 구체적으로 서술합니다.','position:absolute;'));add(div('plus',x+414,257,46,46,'+'))
save(12)
#13
base(13,'작동 원리',5);add(seat(187,269,546,372,1,'image'))
for j,t in enumerate(['사용자 입력 화면','데이터 분석 엔진','매칭 알고리즘','결과 제공 화면']):
 add(box(800,195+j*121,417,104,f'<b class="item-title">{j+1}　 {t}</b><p style="margin-left:32px">수집된 데이터는 기능이나 요소가 무엇인지, 어떤 역할을 하는지 설명합니다.</p>'))
add(pill(800,195,417,'1　사용자 입력 화면'));save(13)
#14
base(14,'주요 기능',6);add(box(428,196,770,467));add(seat(449,219,728,317,1,'image'));add(seat(201,286,267,267,2,'circle'));add(icon(454,567,52,'search'));add(div('small',530,567,600,70,'<b style="color:#333">이곳에 핵심 기능의 전체 개요나 컨셉트를 한 줄로 작성합니다.</b><br>이 기능이 무엇을 하는지, 사용자에게 어떤 가치를 제공하는지 구체적으로 작성합니다.','position:absolute;'));add(div('plus',1141,570,35,35,'›'));save(14)
#15
base(15,'주요 기능',6,intro='솔루션이 제공하는 핵심 기능과 사용자 가치를 정리하는 페이지입니다.<br>각 기능의 역할과 활용 방식을 간단히 보여줍니다.');add(box(146,232,1087,442));add(seat(554,349,250,225,1,'image'))
for j,(x,y,t) in enumerate([(194,275,'실시간 알림'),(1055,275,'맞춤 추천'),(194,523,'간편 결제'),(1055,523,'데이터 분석')]):
 add(pill(x,y,130,t));add(div('small',x if x<500 else 940,y+57,270,95,DEFAULT,'position:absolute;'))
for x,y,n in [(534,300,2),(760,300,3),(534,532,4),(760,532,5)]:add(seat(x,y,80,80,n,'head-icon'))
save(15)
#16
base(16,'그 외 기타 <b>기능</b>',6)
for j,t in enumerate(['알림 설정','데이터 저장','공유 기능']):
 x=174+j*358;add(box(x,286,332,270));add(pill(x+15,252,170,t+'　○'));add(seat(x+15,302,302,237,j+1,'image'));add(div('plus',x+260,502,45,45,'+'))
add(pill(174,596,998,'이곳에 핵심 기능의 전체 개요나 컨셉트를 한 줄로 작성합니다.'));save(16)
#17
base(17,'차별화 <b>포인트</b>',7)
for j,(x,y,t) in enumerate([(338,275,'빠른 응답 속도'),(735,275,'차별화 포인트 키워드'),(163,491,'직관적인 사용 경험'),(913,491,'차별화 포인트 키워드')]):
 add(box(x,y,307,130,'<p>해당 차별화 포인트가 타사 제품 혹은 기존 제품에 비해 나은 점을 입력합니다. 작동 방식을 함께 설명해도 좋습니다.</p>'));add(div('pill dark',x,y-30,221,48,t,'position:absolute;border-radius:4px;'))
add(div('thin-circle',511,432,378,378,'','border:1px dashed #7db6df'));add(div('donut',561,482,278,278,'<div class="inside"><b style="font-size:26px;color:#419ddd">아이디어 관련<br>키워드</b></div>','--pct:100%;'));add(seat(656,496,90,90,1,'circle'));save(17)
#18
base(18,'차별화 <b>포인트</b>',7,intro='경쟁사 대비 차별화되는 핵심 강점과 가치를 정리하는 페이지입니다.<br>차별 요소가 사용자 경험에 어떤 이점을 주는지 보여줍니다.');add(box(172,229,1019,448))
for j,t in enumerate(['최신 AI 기술 적용','사용자 중심 직관적 UI']):
 y=266+j*162;add(box(212,y,974,145,f'<div class="num" style="position:absolute;left:20px;top:13px">0{j+1}</div><p style="margin-left:200px;margin-top:53px">이것이 경쟁사나 기존 방식과 다른 차별화 요소를 작성합니다. 해당 포인트가 중요한 이유, 고객에게 제공하는 이점을 함께 서술합니다.</p>'));add(seat(270,y+20,90,90,j+1,'head-icon'));add(pill(432,y+25,217,t));add(div('check',1124,y+52,28,28,''))
add(div('button',620,608,157,42,'See More　>','position:absolute;'));save(18)
#19
base(19,'예상 타겟 <b>페르소나</b>',8)
for j,name in enumerate(['페르소나1 이름','페르소나2 이름','페르소나3 이름']):
 x=210+j*330;y=284-(35 if j==1 else 0);add(box(x,y,291,398,'<div style="height:224px"></div><p>직업이나 상황 입력</p><p>주요 니즈 입력</p><p>행동 패턴 입력</p>'));add(seat(x+35,y+19,220,220,j+1,'circle'));add(pill(x+35,y+206,220,'♙　'+name))
save(19)
#20
base(20,'기대효과',9,('Expected Outcomes','솔루션 도입을 통해 기대되는 주요 성과를 정량적으로 보여주는 페이지입니다.'))
for j,(val,t) in enumerate([(40,'업무 관련 비용 절감'),(60,'고객 만족도 향상')]):
 add(div('donut',468+j*362,170,331,331,f'<div class="inside"><p>{t}</p><b>{val}<small style="font-size:18px">%</small></b></div>',f'--pct:{val}%;'+('background:conic-gradient(#dafa81 0 60%,#eee 60% 100%);' if j else '')));add(div('plus',720+j*362,207,43,43,'+'))
add(box(469,548,741,92,'<div style="margin-left:163px" class="small">솔루션 도입으로 운영 효율성과 고객 경험이 동시에 개선됩니다.<br>비용 절감과 만족도 향상이 경쟁 우위로 실현됩니다.</div>'));add(pill(490,571,135,'Results'));save(20)
#21
base(21,'기대효과',9,intro='솔루션 도입으로 기대되는 핵심 성과를 정리하는 페이지입니다.<br>사용자 가치와 운영 효율, 비용 측면의 효과를 제시합니다.');add(box(164,242,656,426))
for j,(t,k) in enumerate([('사용자 만족도','people'),('업무 효율성','gear'),('비용 절감','chart')]):
 y=269+j*133;add(box(187,y,607,110));add(icon(208,y+15,80,k));add(div('item-title',317,y+34,160,35,t,'position:absolute;'));add(div('small',514,y+26,256,62,'• 예상되는 효과를 구체적으로 작성합니다.<br>• 개선 전후 수치나 예시를 포함합니다.','position:absolute;'))
add(div('donut',929,306,278,278,'<div class="inside"><b style="font-size:24px;color:#389fe7">최종 기대효과<br>입력란</b></div>','--pct:80%;'));save(21)
#22
base(22,'실행 계획',10,intro='아이디어를 구현하기 위한 단계별 실행 계획을 제시하는 페이지입니다.<br>개발부터 검증, 확산까지의 흐름을 보여줍니다.')
for j,t in enumerate(['프로토타입<br>만들기','소규모 사용자<br>모집','사용자 확대']):
 x=193+j*363;add(div('thin-circle center',x,270,261,261,'','border:12px solid #fff;'));add(pill(x+86,308,94,f'Step 0{j+1}'));add(seat(x+105,365,70,70,j+1,'circle'));add(div('item-title center',x+45,440,190,50,t,'position:absolute;'));add(div('small',x,566,280,80,'• 해당 단계의 구체적인 활동을 작성합니다.<br>• 주요 타깃과 실행 방법을 작성합니다.','position:absolute;'))
 if j<2:add(div('plus',x+292,384,36,36,'»'))
save(22)
#23
base(23,'실행 계획',10,intro='아이디어를 서비스로 발전시키는 단계별 실행 흐름을 보여주는 페이지입니다. 구체화부터 개선까지의 추진 과정을 순서대로 제시합니다.');add(box(144,220,1094,458))
for j,t in enumerate(['아이디어 구체화','프로토타입 개발','베타테스트 진행','정식 서비스 오픈','사용자 피드백 반영']):
 x=162+j*218;y=444-j*44;add(box(x,y,190,215,f'<div class="small" style="color:#48a0df">Step 0{j+1}</div><h3 style="font-size:18px;margin:4px 0">{t}</h3><p>핵심 시기와 주요 활동과 목표를 2~3줄로 작성합니다.</p><div style="height:7px;background:#439ee2;border-radius:99px;margin-top:25px"></div>'));add(icon(x+14,y-29,65,['light','gear','chart','search','people'][j]))
add(div('capsule small',831,573,367,71,'Key Message<br>단계별 검증을 통해 리스크를 최소화합니다.','position:absolute;padding:13px 30px;'));save(23)
#24
base(24,'구현 시 <b>필요사항</b>',11)
for j in range(2):
 x=205;y=289+j*201;add(box(x,y,394,156,'<p style="margin-top:45px">항목에 대한 구체적인 설명이나 세부 요구사항을 2~3줄로 작성합니다. 왜 필요한지, 어떻게 확보할 것인지 등을 명시합니다.</p>'));add(pill(x,y-30,250,f'중요 키워드 설명 0{j+1}'))
add(div('thin-circle',724,245,385,385,'','border:1px dashed #86b9da;'));add(div('donut',770,291,293,293,'<div class="inside"><b style="font-size:22px;color:#4b9ed7">필요 요소</b></div>','--pct:85%;'))
for j,(x,y,t) in enumerate([(843,193,'예산 키워드'),(1028,306,'시간 키워드'),(976,533,'기타 키워드'),(734,533,'장비 키워드'),(664,310,'파트너 키워드')]):add(div('thin-circle center',x,y,146,146,seat(45,15,58,58,j+1,'circle')+f'<div style="position:absolute;bottom:23px;width:100%;font-size:17px">{t}</div>'))
save(24)
#25
base(25,'해결해야 할 <b>과제들</b>',12)
for j,(t,items) in enumerate([('남은 과제들',['해결되지 않은 기술적 문제나 구현 난이도를 작성합니다.','부족한 리소스나 시간 관련 이슈를 작성합니다.','시간이나 일정상의 지연 사항을 작성합니다.']),('해결 방법',['해결하기 위한 구체적인 기술적 대안이나 방법론을 작성합니다.','파트너십 구축, 외부 협업 등 리소스 확보 방안을 작성합니다.','우선순위 조정 등 실행 전략을 작성합니다.'])]):
 y=278+j*207;add(box(277,y,831,143,'<ul style="margin:5px 0 0 210px">'+''.join(f'<li>{t}</li>' for t in items)+'</ul>'));add(pill(321,y+47,172,t));add(div('plus',1078,y+42,43,43,'+'))
save(25)
#26
base(26,'해결해야 할<br><b>과제들</b>',12,('Key Challenges','실행 과정에서 예상되는 주요 과제와 대응 방안을 정리하는 페이지입니다.'))
for j,(t,cap,items) in enumerate([('준비 과정 중 이슈','Challenges',['기술적으로 구현이 어려운 부분이나 기술 관련 이슈를 작성합니다.','예산이나 리소스 부족 등 자원 관련 이슈를 작성합니다.','일정 지연이나 인력 확보 등 실행 과정의 이슈를 작성합니다.']),('이슈 해결 방안','Solutions',['구체적인 해결 방법이나 대안 기술을 작성합니다.','파트너십이나 단계적 접근 방법을 작성합니다.','그 외 다양한 자원을 활용한 이슈 해결 방법을 작성합니다.'])]):
 x=485+j*397;add(box(x,174,315,471,f'<h3 class="center" style="margin-top:65px">{t}</h3><div style="height:137px"></div>'+''.join('<p style="margin:10px 0">'+t+'</p>' for t in items)));add(pill(x+100,205,115,cap));add(seat(x+113,302,90,90,j+1,'head-icon'))
add(div('plus',826,387,40,40,'»'));save(26)
#27
base(27,'우리팀<br><b>소개</b>',13,('Our Team','프로젝트를 수행하는 팀 구성과 역할 구조를 소개하는 페이지입니다.'))
add(div('connector',559,402,547,2,''));add(div('connector vertical',831,348,1,57,''));
for j,(x,y,t,role) in enumerate([(721,179,'김미리','팀장 / 리더'),(448,491,'박미리','기획 / 개발'),(722,491,'오미리','디자인 / UI'),(995,491,'강미리','마케팅 / 운영')]):
 add(box(x,y,222,169,f'<div style="height:84px"></div><h3 class="center">{t}</h3>'));add(seat(x+55,y-55,112,112,j+1,'circle'));add(pill(x+49,y+59,130,role))
save(27)
#28
base(28,'우리팀 <b>소개</b>',13);add(box(167,228,1048,450))
add(pill(588,411,192,'Team Name　팀이름'))
for j,(x,y,t,role) in enumerate([(211,303,'김미리','기획'),(865,303,'박미리','디자인'),(211,519,'강미리','개발'),(865,519,'오미리','마케팅')]):
 add(box(x,y,300,107,f'<div style="margin-left:119px;margin-top:38px;font-size:21px">{t}</div>'));add(seat(x-5,y-6,116,116,j+1,'circle'));add(pill(x+146,y+12,122,role));add(div('connector',x+300 if x<500 else 780,y+53,80,2,''))
save(28)
#29
base(29,'예상 질문과 <b>답변</b>',14);add(box(174,224,1069,454))
for j,t in enumerate(['Q. 기존 서비스와 무엇이 다른가요?','Q. 개발 기간은 얼마나 걸리나요?']):
 y=273+j*204;add(seat(230,y,67,67,j+1,'circle'));add(pill(315,y+3,317,t));add(box(609,y+59,466,113,'<p>• 질문에 대한 명확하고 구체적인 답변을 작성합니다.<br>• 청중이 궁금해할 만한 핵심 내용을 포함합니다.<br>• 또한 구체적인 예시나 수치를 포함하면 좋습니다.</p>'));add(seat(1103,y+60,70,70,j+3,'circle'))
save(29)
#30
base(30,cover=True);add(div('center',200,224,880,220,'<h1 style="font-size:64px;margin:0 0 20px;letter-spacing:-2px">클로징</h1><div style="color:#429bda;font-size:40px;letter-spacing:-1.5px">경청해 주셔서 감사합니다.</div><p class="small" style="margin-top:25px">피드백이나 참여 의사가 있으시면 연락주세요.</p>','position:absolute;'))
for j,t in enumerate(['contact@miridih.com','연락처를 입력하세요.','SNS를 입력하세요.']):add(div('capsule center',160+j*333,442,300,59,t,'position:absolute;padding-top:18px;font-size:17px;'))
add('<div class="dock">'+''.join(f'<div class="seat {"focus" if i==5 else ""}">{i}</div>' for i in range(1,10))+'</div>');save(30,cover=True)
print('Replica sources',len(list(P.glob('slide*.html'))))
