from pathlib import Path
import shutil, math
P=Path(__file__).parent; R=P/'replica';R.mkdir(exist_ok=True)
(R/'assets').mkdir(exist_ok=True)
shutil.copy('/workspace/work/reference/fonts/artifacts/noto-sans-kr/NotoSansKR.woff2',R/'assets/NotoSansKR.woff2')
css='''@font-face{font-family:Noto;src:url(assets/NotoSansKR.woff2);font-weight:100 900}*{box-sizing:border-box}html,body{margin:0;width:1280px;height:720px;overflow:hidden}.slide{width:1280px;height:720px;background:#fff;color:#2c2c2b;position:relative;font-family:Noto,sans-serif;font-size:18px;line-height:1.55;font-weight:350}.abs{position:absolute}p,h1,h2,h3{margin:0}.small{font-size:13px;font-weight:300;color:#999}.pill{display:flex;justify-content:center;align-items:center;background:#2b2b2a;color:white;border-radius:999px;font-weight:700}.box{border:2px solid #d8d8d8;border-radius:16px;padding:30px}.box.strong{border-color:#333}.hl{display:inline-block;position:relative;background:#d9e4ae;font-weight:700;border-left:3px solid #2c2c2b;border-right:3px solid #2c2c2b;padding:0 10px;line-height:1.38}.hl:before,.hl:after{content:'';position:absolute;width:14px;height:14px;border-radius:50%;background:#2b2b2a;left:-8px;top:-7px}.hl:after{left:auto;right:-8px;top:auto;bottom:-7px}.title{font-size:44px;line-height:1.4;font-weight:350;letter-spacing:-1.5px;text-align:center}.caption{font-size:14px;line-height:1.5}.label{white-space:nowrap;display:flex;align-items:center;justify-content:center;border:1px solid #333;border-radius:5px;background:#fff;font-size:12px;line-height:1;font-weight:450;height:26px;min-width:94px;padding:0 10px}.rule{height:2px;background:#d8d8d8}.icon{display:flex;align-items:center;justify-content:center}.icon svg{width:100%;height:100%}.mini{font-size:13px}.photo{background:#e9e9e9;display:flex;align-items:center;justify-content:center;color:#aaa}.circle{border-radius:50%}.center{text-align:center}.bold{font-weight:700}.donut{position:absolute;border-radius:50%;background:conic-gradient(#2b2b2a calc(var(--v)*1%),#d9d9d9 0)}.donut:before{content:'';position:absolute;inset:10%;border-radius:50%;background:#fff}.donut>div{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}.donut b{font-size:26px}.donut span{font-size:14px}.tick{display:inline-block;width:13px;height:8px;border-left:3px solid #333;border-bottom:3px solid #333;transform:rotate(-45deg);margin-right:13px;vertical-align:4px}'''
(R/'replica.css').write_text(css)
def a(x,y,w,h,s='',cls='',style=''):
 if '<br>' in s:style+=';white-space:nowrap'
 return f'<div class="abs {cls}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{style}">{s}</div>'
def hl(s):return f'<span class="hl">{s}</span>'
def title(s,y=134):return a(84,y,1112,120,s,'title')
def rule(y=233,x=84,w=1112):return a(x,y,w,2,'','rule')
def label(s,x,y,w=94):return a(x,y,w,26,s,'label')
def ico(kind,x,y,size=34,color='#333'):
 d={'diamond':'<path d="m5 4 14 0 4 7-11 14L1 11 5 4Z M1 11h22 M5 4l7 21 7-21 M8 4l-3 7m11-7 3 7"/>','bulb':'<path d="M9 21h6m-7-4c-8-9 13-14 8 0l-1 3H9l-1-3Zm4-16V0M3 5 1 3m21 2 2-2M1 12h-2m26 0h-2M8 24h8"/>','gear':'<path d="m9 0 6 0 1 4 4 2 4 0 2 5-3 3v4l-4 3-4-1-4 2-4-2-3-3 1-5-3-3 2-5 5 0 2-4Z"/><circle cx="12" cy="12" r="5"/>','pencil':'<path d="m2 21 3-7L18 1l5 5L10 19l-8 2Zm3-7 5 5M1 24h23M16 3l5 5"/>','gift':'<path d="M2 9h22v5H2V9Zm2 5v12h18V14M11 9v17h4V9M12 9C1 9 4-2 9 2l3 7Zm1 0c11 0 8-11 3-7l-3 7Z"/>','target':'<circle cx="12" cy="13" r="11"/><circle cx="12" cy="13" r="7"/><circle cx="12" cy="13" r="3"/><path d="m12 13 12-13m-1 0-5 1-1 5"/>','users':'<circle cx="5" cy="5" r="3"/><circle cx="19" cy="5" r="3"/><circle cx="12" cy="12" r="3"/><path d="M0 19v-5c0-5 9-5 9 0m6 0c0-5 9-5 9 0v5M7 27v-8c0-4 10-4 10 0v8m-7-7v7m4-7v7"/>','cart':'<path d="M0 2h4l3 16h15l3-12H5M8 10h16M9 14h14M10 6v12m5-12v12m5-12v12"/><circle cx="10" cy="23" r="2"/><circle cx="21" cy="23" r="2"/>','check':'<path d="m2 13 7 7L23 4M2 25h23"/>','home':'<path d="m0 12 13-11 13 11-3 2v13H3V14l-3-2ZM10 27V17h7v10"/>','trash':'<path d="M2 6h22M5 6v21h17V6M9 6V2h9v4m-8 4v12m7-12v12"/>','message':'<path d="M2 2h23v19H12l-6 5v-5H2V2Zm5 5h13M7 11h13M7 15h9"/>','puzzle':'<path d="m2 8 6-6 5 5c-2-6 6-6 7-2 1 2-1 4-2 4l6 5-6 6-5-5c3 6-6 6-7 2-1-2 1-4 2-4L2 8Z"/>','globe':'<circle cx="13" cy="13" r="12"/><ellipse cx="13" cy="13" rx="6" ry="12"/><path d="M1 13h24M4 6h18M4 20h18"/>','share':'<circle cx="4" cy="13" r="4"/><circle cx="22" cy="3" r="4"/><circle cx="22" cy="24" r="4"/><path d="m8 11 10-6M8 15l10 7"/>'}.get(kind,'<circle cx="12" cy="12" r="10"/>')
 return a(x,y,size,size,f'<svg viewBox="-2 -2 32 32" fill="none" stroke="{color}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">{d}</svg>','icon')
def base(i,kicker=None,section=''):
 s=a(84,64,250,24,'20XX IR PRESENTATION','small')+a(900,64,296,24,section,'small', 'text-align:right')
 if kicker:s+=a(84,74,1112,32,f'<span style="display:inline-flex;height:32px;padding:0 18px;background:#686868;color:white;font-size:22px;line-height:1;align-items:center;justify-content:center;border-radius:7px;font-weight:500;letter-spacing:-.6px">{kicker}</span>','center')
 return s
def box(x,y,w,h,s,strong=False,style=''):return a(x,y,w,h,s,'box'+(' strong' if strong else ''),style)
def donut(x,y,d,v,fig,name=''):
 return a(x,y,d,d,f'<div><b>{fig}</b><span>{name}</span></div>','donut',f'--v:{v}')
def svg(s,x,y,w,h):return a(x,y,w,h,f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">{s}</svg>')
def bars(x,y,w,h,v1,v2=None,labels=None,title_='',foot=None):
 labels=labels or [f'205{j}년' for j in range(len(v1))]; vmax=max(v1+(v2 or [])); bottom=h-35; top=45; chartH=bottom-top
 s=''
 for j in range(6):
  yy=top+j*chartH/5;s+=f'<line x1="10" y1="{yy}" x2="{w-10}" y2="{yy}" stroke="#d5d5d5"/>'
 for j,v in enumerate(v1):
  xx=20+j*(w-25)/len(v1); bw=(w-25)/len(v1)*(.24 if v2 else .45);height=v/vmax*chartH
  if v2:
   hh=v2[j]/vmax*chartH;s+=f'<rect x="{xx}" y="{bottom-hh}" width="{bw}" height="{hh}" rx="4" fill="#d7d7d7"/>';xx+=bw+6
  s+=f'<rect x="{xx}" y="{bottom-height}" width="{bw}" height="{height}" rx="4" fill="#2c2c2b"/><text x="{20+j*(w-25)/len(v1)+bw}" y="{h-12}" font-family="Noto" font-size="11" text-anchor="middle" fill="#333">{labels[j]}</text>'
 if v2:s+='<rect x="14" y="55" width="8" height="8" rx="2" fill="#d7d7d7"/><text x="29" y="63" font-family="Noto" font-size="11" fill="#333">타사</text><rect x="14" y="74" width="8" height="8" rx="2" fill="#2c2c2b"/><text x="29" y="82" font-family="Noto" font-size="11" fill="#333">MIRI COMPANY</text>'
 return a(x,y,w,48,title_,'bold', 'font-size:28px')+svg(s,x,y+34,w,h)
def trend(x,y,w,h,values,area=False,labels=None):
 labels=labels or [f'205{j}년' for j in range(len(values))];left=20;right=w-20;top=20;bot=h-40;maxv=max(values)
 pts=[(left+j*(right-left)/(len(values)-1),bot-v/maxv*(bot-top)) for j,v in enumerate(values)];s=''
 for j in range(4):
  yy=top+j*(bot-top)/3;s+=f'<line x1="0" y1="{yy}" x2="{w}" y2="{yy}" stroke="#ddd"/>'
 if area:s+=f'<polygon points="{left},{bot} '+ ' '.join(f'{a},{b}'for a,b in pts)+f' {right},{bot}" fill="#bdbdbd"/>'
 s+='<polyline points="'+' '.join(f'{a},{b}'for a,b in pts)+'" fill="none" stroke="#555" stroke-width="1"/>'
 for j,((xx,yy),v) in enumerate(zip(pts,values)):s+=f'<circle cx="{xx}" cy="{yy}" r="3.5" fill="#333"/><text x="{xx}" y="{h-8}" font-family="Noto" font-size="11" text-anchor="middle" fill="#333">{labels[j]}</text>'
 return svg(s,x,y,w,h)
pages={}
# 01
s=base(1,None,'MIRICOMPANY.CO.KR');s+=a(98,181,500,50,'포인트가 있는 모노톤의 심플한',style='font-size:32px;color:#737373;letter-spacing:-1px')+a(97,222,490,134,'투자유치','bold', 'font-size:100px;letter-spacing:-6px;line-height:1.3')+a(82,355,500,140,hl('발표용 IR덱'),style='font-size:100px;letter-spacing:-4px;line-height:1.45')+a(663,126,617,528,'','photo', 'border-radius:270px 0 0 270px')+a(84,635,250,28,'MIRI Company','bold','font-size:16px');pages[1]=s
#02
s=base(2,None,'MIRICOMPANY.CO.KR');s+=a(84,124,450,86,'TABLE OF','bold','font-size:64px;line-height:1.2;letter-spacing:-1.5px')+a(90,197,356,79,hl('CONTENTS'),style='font-size:60px;line-height:1.2;letter-spacing:-2px')+a(84,294,450,50,'IR DECK 목차 안내',style='font-size:28px;color:#777;letter-spacing:-1px')
items=['연혁과 성과','미션과 비전','문제','솔루션','시장상황','서비스(제품) 소개','차별성/경쟁력','경쟁사','시장 진입(확장) 전략','팀 소개','투자 유치 및 재무 계획']
for j,t in enumerate(items):
 c=j//6;r=j%6;x=603+c*321;y=221+r*69;s+=rule(y,x,273)+a(x,y+20,30,35,f'{j+1:02}',style='font-size:15px;font-weight:500')+a(x+35,y+14,260,45,t,style='font-size:25px;letter-spacing:-1px')
s+=rule(636,603,273)+a(603,221,273,3,'',style='background:#333')+a(924,221,272,3,'',style='background:#333');pages[2]=s
#03
s=base(3,'INFORMATION','회사소개')+title('[제품/서비스명]은 [고객]의 [가장 큰 문제]를 '+hl('해결하는')+'<br>혁신적인 솔루션입니다.')+rule(293)
s+=a(84,329,465,247,'우리는 [우리가 타겟하는 명확한 고객]이 겪고 있는<br>[가장 큰 문제점]을 해결하기 위해, [우리의 솔루션을 한 문장으로<br>정의]인 [제품/서비스명]을 개발하고 운영합니다. 우리의 비즈니스는<br>[창업 계기]를 기반으로 시작되었으며, [핵심 제품/서비스] MVP<br>출시를 통해 시장의 니즈를 검증했습니다. 이러한 과정을 통해<br>우리는 [가장 큰 문제]를 해결하는 가장 효율적인 방법을 찾아냈고,<br>이는 현재의 [제품/서비스명]으로 구체화되었습니다.<br>우리의 목표는 [산업]의 새로운 표준이 되는 것입니다.',style='font-size:17px;line-height:30px;letter-spacing:-.5px')+label('KEYWORD',84,585)+a(207,587,130,25,'KEYWORD',style='font-size:12px')
for y,k,t,icon in [(332,'MISSION','우리의 존재 이유를 한 문장으로 정의합니다.<br>우리의 사명은 [타겟 고객]의 [문제]를 해결하는<br>것입니다.','diamond'),(485,'VISION','우리가 그리는 미래를 서술합니다. 우리는 [산업<br>분야]의 [선두 주자]가 되는 것을 목표로 합니다.','bulb')]:
 s+=box(639,y,557,126,'',y==485,style='border-radius:999px')+a(614,y+37,53,53,'','pill')+ico(icon,629,y+52,25,'#fff')+a(688,y+43,140,40,k,'bold','font-size:25px')+a(829,y+19 if y==332 else y+34,350,90,t,style='font-size:17px;line-height:28px;letter-spacing:-.5px')
s+=a(917,459,1,26,'',style='border-left:2px dashed #ddd');pages[3]=s
#04
s=base(4,'VISION & MISSION','비전과 미션')+title('여기에 회사가 꿈꾸는 궁극적인 '+hl('미래상을')+'<br>한 문장으로 제시하세요.')+rule(293)
for x,t,k,icon in [(116,'비전을 명확하게<br>표현해 보세요.','VISION','bulb'),(864,'미션을 명확하게<br>표현해 보세요.','MISSION','diamond')]:
 s+=box(x,337,301,301,'',False,'border-radius:50%;padding:0')+ico(icon,x+132,390,40)+a(x+30,459,241,70,t,'center','font-size:21px;line-height:29px;letter-spacing:-.5px')+a(x+50,559,201,30,k,'center mini')
s+=box(347,337,588,301,'',True,'border-radius:160px;padding:0')+ico('puzzle',622,385,38)+a(455,441,371,100,'회사의 미션과 장기적인 비전을<br>이 슬라이드에 담으세요. 큰 그림을 보여주며<br>투자자의 공감을 이끌어내는 페이지입니다.','center bold','font-size:21px;line-height:30px;letter-spacing:-.8px')+a(591,553,99,50,'OUR<br>COMPANY','center mini','line-height:18px');pages[4]=s
#05
s=base(5,'PROBLEM','시장의 문제점')+title('여기에 해결하려는 '+hl('문제의 핵심을')+'<br>간결하게 정의하세요.')
for j,(name,txt,ic) in enumerate([('비효율성','고객이 어떤 불편함을 느끼고 시간/비용<br>적으로 얼마나 손해를 보고 있는지 구체<br>적인 수치로 설명하세요.','gear'),('높은 비용','기존의 방식이나 해결책이 왜 비싸고 접<br>근하기 어려운지, 그로 인해 어떤 기회비<br>용이 발생하는지 설명하세요.','cart'),('정보 부족','고객이 올바른 결정을 내리는 데 필요한<br>정보가 왜 부족하거나 비대칭적인지, 어<br>떤 부정적 결과를 낳는지 보여주세요.','pencil')]):
 x=84+j*378;s+=box(x,344,356,294,'',j==1)+a(x+152,321,53,53,'','pill')+ico(ic,x+164,333,30,'white')+a(x+20,390,316,26,f'PAIN POINT 0{j+1}','center mini')+a(x+20,416,316,47,name,'center bold','font-size:31px')+rule(484,x+42,272)+a(x+42,510,280,100,txt,style='font-size:17px;line-height:27px;letter-spacing:-.5px')
pages[5]=s
#06
s=base(6,'SOLUTION','우리의 해결책')+title('여기에 문제에 대한 '+hl('명쾌한 해결책을')+' 제시하세요.')+rule()
s+=rule(319,100,1060)
for j in range(4):
 x=84+j*287;s+=a(x,280,251,79,'핵심 기능명','pill','font-size:25px')+label('SOLUTION 04',x+79,267,94)+a(x+125,359,1,26,'',style='border-left:2px dashed #ddd')+box(x,385,251,253,'')+a(x+30,416,194,200,('이 기능을 통해 고객이 얻게<br>될 핵심적인 이점을 작성하<br>세요. 앞서 제시한 문제를 해<br>결하기 위해, 우리의 솔루션<br>을 소개합니다. 솔루션의 핵<br>심 기능과 차별점을 간결하<br>고 직관적으로 설명하세요.' if j%2==0 else '앞서 제시한 문제를 해결하<br>기 위해, 우리의 솔루션을 소<br>개합니다. 솔루션의 핵심 기<br>능과 차별점을 간결하고 직<br>관적으로 설명하세요.'),style='font-size:17px;line-height:27px;letter-spacing:-.5px')
pages[6]=s
#07
s=base(7,'MARKET SIZE & OPPORTUNITY','시장 규모 및 기회')+a(639,133,557,190,'여기에 공략할 시장의<br>'+hl('크기와 성장 가능성을')+'<br>숫자로 보여주세요.','title','text-align:left')
s+=a(84,162,476,476,'','pill circle')+a(84,233,335,335,'','circle', 'background:#e8e8e8')+a(84,292,224,216,'','circle', 'background:white')+a(435,371,108,75,'<b style="font-size:30px">TAM</b><br><span style="font-size:13px">(전체 시장)</span>','center','color:white')+a(314,371,108,75,'<b style="font-size:30px">SAM</b><br><span style="font-size:13px">(유효 시장)</span>','center')+a(142,371,108,75,'<b style="font-size:30px">SOM</b><br><span style="font-size:13px">(초기 목표 시장)</span>','center')
for j,(f,n,t) in enumerate([('420억원','(전체 시장)','회사가 속한 가장 큰 시장의 규모를 제시하세요.<br>(예: 글로벌 인테리어 시장)'),('120억원','(유효 시장)','그 중 회사의 제품/서비스가 공략 가능한 시장의 규모를 보여<br>주세요. (예: 국내 온라인 인테리어 플랫폼 시장)'),('80억원','(초기 목표 시장)','향후 1~3년 내에 현실적으로 점유할 수 있는 시장의 규모를<br>정의하세요. (예: 수도권 아파트 전문 디자인 서비스 시장)')]):
 y=348+j*96;s+=rule(y,638,558)+a(638,y+17,150,45,f,'bold','font-size:31px')+a(638,y+61,150,25,n,'mini')+a(798,y+23,398,64,t,style='font-size:17px;line-height:28px;letter-spacing:-.5px')
s+=rule(636,638,558);pages[7]=s
#08
s=base(8,'MARKET VOLUME','시장의 크기')+title('[시장 규모] 시장에서 '+hl('우리의 독점적 기회')+'를 보여주세요.')+rule()+rule(376,375,530)
for x,v,t in [(272,20,'경쟁사 A'),(537,60,'기타'),(803,20,'경쟁사 B')]:s+=donut(x,275,205,v,t)+label('KEYWORD',x+56,397)
for j,(n,t) in enumerate([('경쟁 구도','현재 시장은 [경쟁사]가 점유하고 있지만, 그들<br>이 해결하지 못하는 [틈새시장]이 존재합니다.'),('시장 기회','우리는 [시장 규모]조 원의 이 틈새시장을 공략<br>하여 독점적인 지위를 확보할 것입니다.')]):
 x=84+j*574;s+=box(x,517,538,121,'')+a(x+44,545,150,25,f'POINT {j+1}','mini')+a(x+44,565,150,47,n,'bold','font-size:29px')+a(x+180,547,340,70,t,style='font-size:17px;line-height:28px;letter-spacing:-.5px')
pages[8]=s
#09
s=base(9,'PRODUCT/SERVICE','제품 및 서비스')+title('여기에 '+hl('우리 기술의 핵심을')+' 보여주세요.')+rule()
s+=box(84,267,302,124,'')+box(84,407,302,125,'')+box(894,267,302,124,'')+box(894,407,302,125,'')+a(424,267,431,177,'',style='background:#f2f2f2;border-radius:16px')
for j in range(3):
 x=465+j*127;s+=svg('<path d="M0 20v72c0 27 96 27 96 0V20" fill="white" stroke="#333"/><ellipse cx="48" cy="20" rx="48" ry="20" fill="white" stroke="#333"/>',x,292,98,112)+a(x+10,394,77,26,'KEYWORD','pill','font-size:12px;border-radius:5px;font-weight:400')
for x,y,ic in [(107,290,'trash'),(198,290,'message'),(289,290,'gear'),(917,430,'puzzle'),(1008,430,'globe'),(1099,430,'share')]:s+=a(x,y,76,76,'',style='background:#f2f2f2;border-radius:14px')+ico(ic,x+22,y+16,35)+a(x,y+53,76,25,'KEYWORD','pill','font-size:12px;border-radius:4px;font-weight:400')
s+=a(104,430,260,83,'이곳에 사용된 요소를 가지고<br>우리 기술의 시스템을<br>명확히 설명해 보세요.','center','font-size:19px;line-height:28px')+a(914,289,260,83,'이곳에 사용된 요소를 가지고<br>우리 기술의 시스템을<br>명확히 설명해 보세요.','center','font-size:19px;line-height:28px')+a(424,456,431,76,'우리 기술을 설명하는 핵심 문장을 적어보세요.','pill','font-size:20px;letter-spacing:-1px')+a(84,559,1112,78,'제품의 기술 구조를 다이어그램으로 시각화하여 데이터 흐름, 핵심 엔진, 서비스 모듈 등을 보여주세요.<br>기술에 대한 깊은 이해도를 어필할 수 있습니다.','center','background:#f2f2f2;border-radius:16px;padding:12px;font-size:18px')
s+=svg('<path d="M2 80 40 80 2 244H42M470 106h37L473 244h34M255 195v12" fill="none" stroke="#333" stroke-width="2"/>',384,249,510,261);pages[9]=s
#10
s=base(10,'BUSINESS MODEL','비즈니스 모델')+title('여기에 회사의 '+hl('수익 창출 모델')+' 보여주세요.')+rule()
for j,(n,t,foot) in enumerate([('구독료 (SAAS)','어떤 고객이 어떤 가치에 대해<br>월/연 단위로 비용을 지불하는<br>지 설명합니다.','BASIC: 월 10만 원<br>PRO: 월 50만 원'),('중개 수수료','플랫폼 내에서 발생하는 거래<br>의 어떤 부분에서 몇 %의 수수<br>료를 받는지 설명합니다.','거래액의 5~10%'),('기타','데이터 판매, 부가 서비스 등 추<br>가적인 수익원이 있다면 기재<br>합니다.','리포트 건당/API 호출당 과금'),('강조할 수익 모델','여기에 가장 강조하고 싶은 우<br>리 회사의 수익 모델에 대해 기<br>재합니다.','상세 내용을 입력해보세요.')]):
 x=84+j*282;s+=box(x,281,266,357,'',j==3)+a(x+32,313,210,27,f'수익모델 0{j+1}','mini')+a(x+32,338,210,53,n,'bold','font-size:27px;letter-spacing:-1px')+rule(401,x+32,202)+a(x+32,429,217,100,t,style='font-size:17px;line-height:28px;letter-spacing:-.5px')+a(x+32,554 if j==0 else 583,220,65,'<span class="tick"></span>'+foot,style='font-size:14px;line-height:28px;font-weight:500;letter-spacing:-.6px')
pages[10]=s
#11
s=base(11,'BUSINESS MODEL','비즈니스 모델')+title('어떻게 '+hl('가치를 만들고 전달하는지')+' 보여주세요.')+rule()
s+=box(134,314,1012,130,'',False,'border-radius:90px')
for j,(ic,t) in enumerate([('users','고객 유입<br>채널'),('diamond','서비스 제공 및<br>핵심 가치 창출 활동'),('gift','고객이 얻는<br>혜택 및 성공'),('target','수익 발생 및<br>고객 유지'),('bulb','수익을 통한<br>서비스 고도화 및 재투자')]):
 x=242+j*175;s+=a(x,268,94,94,'','pill')+ico(ic,x+24,289,50,'white')+label(f'STEP 0{j+1}',x+12,341,70)+a(x-18,377,130,55,t,'center','font-size:16px;line-height:23px;letter-spacing:-.6px')
 if j<4:s+=svg('<path d="M0 10h40m0 0-9-6v12Z" fill="#333" stroke="#333"/>',x+104,304,45,20)
for j,(n,t,ic) in enumerate([('누구에게','우리의 명확한 타겟 고객은 누구이며<br>고객의 니즈는 무엇인지 다시 한번<br>정의합니다.','users'),('어떤 가치를','우리가 고객에게 제공하는 3가지 핵<br>심 가치(예: 비용 절감, 시간 절약, 매<br>출 증대)를 명확히 제시합니다.','diamond'),('어떻게','그 가치를 어떤 핵심 채널을 통해 전<br>달하고, 어떤 방식으로 강화해 나갈<br>것인지 설명합니다.','bulb')]):
 x=84+j*383;s+=box(x,478,345,160,'')+a(x+30,533,51,51,'','pill')+ico(ic,x+42,545,27,'white')+a(x+95,502,230,37,n,'bold','font-size:22px')+a(x+95,538,230,84,t,style='font-size:16px;line-height:26px;letter-spacing:-.5px')
pages[11]=s
#12
s=base(12,'REVENUE MODEL','수익 모델')+title(hl('수익 모델의 핵심')+'을 한줄로 설명해주세요.')+rule()
for y,k,n,t in [(281,'POINT 1','가격 전략','우리의 가격은 단순히 원가나 경쟁사를 따르는<br>것이 아니라, 고객이 우리 서비스를 통해 얻는<br>가치에 기반하여 책정되었음을 설명합니다.'),(473,'POINT 2','수익 구조','현재 또는 목표 시점의 매출 비중을 보여줍니다.<br>안정적인 반복 매출과 부가적인 수익원이<br>어떻게 조화를 이루는지 설명하세요.')]:
 s+=box(84,y,532,165,'')+a(125,y+52,140,24,k,'mini')+a(125,y+72,140,50,n,'bold','font-size:29px')+a(262,y+39,332,95,t,style='font-size:17px;line-height:27px;letter-spacing:-.6px')
s+=a(672,277,524,48,'수익원 구조','center bold','font-size:29px')
for j,(v,t) in enumerate([(60,'안정적인 현금 흐름을<br>창출하는 우리 회사의<br>핵심 수익원'),(20,'사용량이 늘어남에 따라<br>매출도 함께 성장하는<br>구조의 수익원'),(20,'전문가 컨설팅, 맞춤형<br>구축 등 고부가가치<br>서비스를 제공')]):
 x=675+j*182;s+=donut(x,343,157,v,f'{v}%',f'수익원 {j+1}')+a(x+5,558,148,86,t,'center','font-size:17px;line-height:27px;letter-spacing:-.5px')+svg('<path d="M4 0v27m-2-4 2 4 2-4" fill="none" stroke="#333"/>',x+75,500,10,30)
pages[12]=s
#13
s=base(13,'TRACTION & KEY METRICS','성장지표')+title('여기에 '+hl('성장을 증명하는')+' 핵심 지표들을 넣어보세요.')+rule()
for j,(f,n,t) in enumerate([('342만','(사용자 지표)','누적 가입자, 월간 활성 사용자(MAU), 재방문율 등 인<br>기를 증명하는 지표를 제시하세요.'),('200억 원','(재무 지표)','매출, 거래액, 월간 반복 매출(MRR) 등 회사의 재무적<br>성장을 증명하는 지표를 제시하세요.'),('95%','(고객 만족도)','고객 재구매율, 만족도 평점, 주요 고객 후기<br>(TESTIMONIAL) 등을 통해 서비스의 품질을 구체적<br>인 수치와 함께 증명하세요.')]):
 y=263+j*140;s+=a(84,y,161,48,f,'bold','font-size:31px')+a(84,y+42,161,30,n,style='font-size:17px')+a(245,y+5,357,96,t,style='font-size:17px;line-height:28px;letter-spacing:-.6px')+rule(y+94,84,517)
s+=bars(674,278,522,337,[2,4,6,4,9,10],[1,3,2,1.5,3,5],title_='누적 서비스 가입자')+a(674,321,522,22,'기간 : 2050년–2055년','mini')+a(1094,303,110,40,'120만 명','bold','font-size:25px;text-align:right');pages[13]=s
#14
s=base(14,'TRACTION','성과')+title('우리의 '+hl('성과가 말해주는 것')+'을 수치로 보여주세요.')+rule()
for x,n in [(84,'시장성'),(473,'수익성'),(864,'경쟁 우위')]:s+=a(x,278,330,50,n,'bold','font-size:29px')
s+=trend(95,330,310,213,[1.5,.5,2,4.5,6.5,7.5],True)+trend(485,330,310,213,[1.5,.5,1,3.5,6,7.5],False,['06월','07월','08월','09월','10월','11월'])+bars(865,270,330,232,[8,7.5,.6,.8,.5,1.1],[10,8.6,6,8.6,3.3,2.7])
for x,t in [(84,'월간 활성 사용자(MAU) 성장은 [수치%]에 달하<br>며, 이는 우리 서비스에 대한 시장의 높은 수요를 보<br>여줍니다.'),(473,'우리는 [기간] 내에 손익분기점(BEP)에 도달할 것<br>으로 예상됩니다. 이 내용은 매출과 영업이익을 함<br>께 보여주는 선 그래프로 표현하는 것이 좋습니다.'),(864,'우리의 고객 유지율(RETENTION)은 [경쟁사] 대<br>비 월등히 높아, 서비스의 가치를 증명합니다.')]:s+=a(x,558,350,100,t,style='font-size:17px;line-height:28px;letter-spacing:-.6px')
s+=a(668,370,2,130,'',style='border-left:3px dotted #333')+label('BEP',647,338,46);pages[14]=s
#15
s=base(15,'COMPETITIVE LANDSCAPE','경쟁 환경 분석')+a(639,132,557,192,'여기에 우리 회사가 가진<br>'+hl('독보적인 경쟁 우위를')+'<br>명확히 설명하세요.','title','text-align:left')+a(84,149,497,489,'',style='background:#f2f2f2;border-radius:16px')+svg('<path d="M20 245H422m-4-2 4 2-4 2M221 43v393m-2-389 2-4 2 4m-2 389-2-4m2 4 2-4" fill="none" stroke="#ccc" stroke-width="2"/>',111,153,442,460)+a(300,162,70,25,'저비용','center mini')+a(300,601,70,25,'고비용','center mini')+a(99,362,23,100,'높은 응답 빈도','mini','writing-mode:vertical-rl;transform:rotate(180deg)')+a(543,362,23,100,'낮은 응답 빈도','mini','writing-mode:vertical-rl')
for x,y,n in [(190,278,'타이틀 A'),(195,507,'타이틀 B'),(387,481,'타이틀 C')]:s+=a(x,y,48,48,'','circle','background:#d7d7d7')+a(x-16,y+52,80,25,n,'center','font-size:11px;font-weight:500')
s+=a(374,196,159,84,'MIRI<br>COMPANY','pill center','font-size:16px;line-height:22px;font-weight:500')
for j,(t,ic) in enumerate([('타사 응답 서비스 대비 저렴한 비용과 높은 응답 빈도','check'),('이곳에 경쟁사가 따라하기 어려운 요소를 적어주세요','target'),('우리만의 독점적인 기술이나 특허 등을 적어주세요','diamond')]):
 y=348+j*96;s+=rule(y,638,558)+a(638,y+24,53,53,'','pill')+ico(ic,652,y+39,28,'white')+a(708,y+32,490,50,t,style='font-size:20px;letter-spacing:-.7px')
s+=rule(636,638,558);pages[15]=s
#16
s=base(16,'COMPETITIVE LANDSCAPE','경쟁 환경 및 우리의 독보적 위치')+title('우리의 '+hl('시장에서 우리의 독보적 위치')+'를 보여주세요.')+rule()
for j,(n,t) in enumerate([('기술적 우위','우리는 [핵심 기술]을 통해 경쟁사가 따라올 수 없는<br>성능을 제공합니다.'),('고객 중심 솔루션','고객의 [고통스러운 문제]를 정확하게 해결하는<br>맞춤형 솔루션을 제공합니다.'),('비용 효율성','우리의 [비즈니스 모델]은 경쟁사 대비 [비용]을<br>획기적으로 절감합니다.')]):
 y=270+j*134;s+=a(84,y,210,25,f'POINT {j+1}','mini')+a(84,y+22,220,55,n,'bold','font-size:29px;letter-spacing:-.7px')+a(295,y+3,340,80,t,style='font-size:17px;line-height:28px;letter-spacing:-.5px')+rule(y+99,84,552)
s+=svg('<circle cx="290" cy="140" r="124" fill="#e8e8e8" stroke="white" stroke-width="7"/><circle cx="220" cy="260" r="124" fill="#e8e8e8" stroke="white" stroke-width="7"/><circle cx="360" cy="260" r="124" fill="#e8e8e8" stroke="white" stroke-width="7"/><path d="M171 156Q220 128 288 154Q242 194 233 247Q190 222 171 156M304 154Q370 129 411 156Q393 221 348 248Q340 195 304 154M240 268Q291 293 344 268Q337 337 292 368Q247 335 240 268" fill="#2c2c2b" stroke="white" stroke-width="7"/>',644,251,550,397)+a(889,446,100,63,'우리의<br>핵심기술','center bold','font-size:19px;line-height:24px')+a(874,326,130,40,'경쟁사 A','center bold','font-size:19px;color:#aaa')+a(769,507,130,40,'경쟁사 B','center bold','font-size:19px;color:#aaa')+a(977,507,130,40,'경쟁사 C','center bold','font-size:19px;color:#aaa')+label('기존의 서비스',671,347,100)+label('솔루션',1095,347,100)+label('키워드 입력',887,652,100);pages[16]=s
#17
s=base(17,'GO-TO-MARKET & GROWTH STRATEGY','성장 전략')+title('여기에 '+hl('성장전략을')+' 구체적으로 제시하세요.')+rule()
for j in range(5):
 x=84+j*223;s+=a(x,246,2,368,'',style='background:#eee')+a(x+10,262,200,121,'','photo','border-radius:70px')+a(x+23,485,184,126,('목표 달성을 위한 구체적<br>인 액션 플랜을 제시하세<br>요. (예: 특정 커뮤니티 타<br>겟 마케팅 등)' if j%2==0 else '이 단계의 구체적인 목표<br>를 작성하세요. (예: 국내<br>시장 점유율 1위 달성)'),style='font-size:17px;line-height:27px;letter-spacing:-.6px')
s+=a(94,402,200,60,'초기 시장 진입 (~1년)','pill','font-size:18px;background:#f2f2f2;color:#333;border-radius:15px')+a(317,402,423,60,'본격적인 성장 및 확장 (~3년)','pill','font-size:18px;background:#f2f2f2;color:#333;border-radius:15px')+a(763,402,423,60,'본격적인 성장 및 확장 (~3년)','pill','font-size:18px;border-radius:15px')+a(84,625,1112,13,'',style='background:repeating-linear-gradient(90deg,#ddd 0 2px,white 2px 5px)')+label('PHASE 1',148,618)+label('PHASE 2',481,618)+label('PHASE 3',933,618);pages[17]=s
#18
s=base(18,'TECHNOLOGY & IP','보유 기술 및 IP')+title('독자적인 '+hl('기술 아키텍처와 독점 데이터')+' 등을 적어주세요.')+rule()+a(84,296,470,50,'우리의 기술과 독점 데이터','bold','font-size:28px;letter-spacing:-1px')+a(84,365,456,220,'회사의 기술적 깊이와 방어력을 증명하여, 투자자 단기적인 성과를<br>넘어 장기적으로 지속 가능한 가치를 가질 것임을 설득하세요. 우리<br>의 기술 아키텍처는 비전문가인 투자자도 쉽게 이해할 수 있도록 설명주<br>세요. 회사가 보유한 가장 중요한 기술 자산인 특허와 독점 데이터베<br>이스는 우리의 기술력을 증명합니다.<br>이러한 기술, IP, 그리고 데이터는 경쟁사와의 격차를 만들고 후발주<br>자의 진입을 어렵게 만드는 강력한 진입 장벽이 됩니다.',style='font-size:16.5px;line-height:31px;letter-spacing:-.4px')+label('KEYWORD',84,612)+label('KEYWORD',189,612)
for x,y,w,h,t,strong in [(589,298,249,69,'시스템 콘트롤러',True),(589,390,249,68,'클라우드 서버 클러스터',True),(988,320,94,138,'게이트<br>웨이',False),(1102,298,94,47,'기기',False),(1102,360,94,47,'기기',False),(1102,422,94,47,'기기',False),(696,482,267,70,'',False),(947,574,249,69,'시각화 시스템',True)]:
 s+=box(x,y,w,h,'',strong,'padding:0;border-radius:12px;background:'+('#2b2b2a'if y==574 else'white'))+a(x+6,y,w-12,h,t,'center bold','display:flex;align-items:center;justify-content:center;font-size:18px;line-height:26px;color:'+('white'if y==574 else'#333'))
s+=svg('<path d="M125 69v24M249 36h66v148M145 161v153h285M406 161v-44h-90M406 94l20-69M406 94h20M406 94l20 69M395 220h35v54" fill="none" stroke="#333" stroke-width="1.5"/>',589,298,610,345)
for j,ic in enumerate(['trash','message','gear']):s+=ico(ic,733+j*79,498,33)+a(716+j*79,540,66,21,'KEYWORD','pill','font-size:11px;border-radius:4px;font-weight:400')
pages[18]=s
#19
s=base(19,'THE TEAM','팀 소개')+title('비전을 실현할 '+hl('최고의 팀을')+' 소개하세요.')+rule()
for j,(n,role) in enumerate([('한미리','ENGINEER'),('최미리','ENGINEER'),('박미리','CEO'),('우미리','MARKETER'),('현미리','MARKETER')]):
 x=84+j*231;d=230 if j==2 else 190;y=264 if j==2 else 304;px=x-20 if j==2 else x;s+=a(px,y,d,d,'','photo circle','border:8px solid #e8e8e8')+a(x-5,509,200,45,n,'center bold','font-size:28px')+a(x-5,548,200,30,role,'center mini')+a(x+5,587,211,62,('•  핵심 경력을 적어보세요.<br>•  전문성을 보여주세요.'if j%2==0 else '•  관련 분야에서의 구체적인<br>   경험을 기재해주세요.'),style='font-size:17px;line-height:28px;letter-spacing:-.5px')
s+=a(485,667,310,20,'*페이지 내 인물 사진은 샘플 이미지입니다.','center','font-size:10px;color:#ccc');pages[19]=s
#20
s=base(20,'FUNDRAISING & FINANCIAL PLAN','투자 유치 및 재무 계획')+title('NEXT-LEVEL을 위한 '+hl('성장 동력을')+' 어필하세요.')+rule()+a(84,280,356,163,'<div><b style="font-size:39px">200억 원</b><br><span style="font-size:20px;font-weight:400">투자 유치 목표</span></div>','pill center')+label('THE ASK',215,267)+box(84,475,356,163,'',True,'border-radius:100px')+label('MESSAGE',215,462)+a(119,520,286,90,'우리 기업이 왜 투자 가치가 있는지,<br>투자자에게 강조하고 싶은 한 문장<br>을 적어주세요.','center bold','font-size:18px;line-height:25px;letter-spacing:-.5px')+box(462,281,356,357,'')+box(842,281,354,357,'')+a(498,307,280,49,'자금 사용 계획','bold','font-size:27px')+a(498,345,280,25,'단위 : 억 원','mini')+a(878,307,300,49,'자사 예상 영업이익률','bold','font-size:27px;letter-spacing:-1px')+a(878,345,300,25,'기간 : 2050년–2055년','mini')
x=498
for v,c in [(40,'#2b2b2a'),(20,'#e8e8e8'),(30,'#666'),(10,'#e8e8e8')]:
 w=283*v/100;s+=a(x,381,w,80,f'{v}%','center bold',f'background:{c};color:'+('white'if v in[40,30]else'#333')+';display:flex;align-items:center;justify-content:center;font-size:'+('20px'if v==40 else'14px'));x+=w
s+=a(498,480,290,130,'•  R&D 및 기술 고도화: 40% (80억 원)<br>•  마케팅 및 고객 확보: 20% (40억 원)<br>•  핵심 인재 영입: 30% (60억 원)<br>•  운영 자금 및 기타: 10% (20억 원)',style='font-size:17px;line-height:33px;letter-spacing:-.7px')+bars(875,313,286,274,[2,4,6,4,9],[1,3,2,1.5,3])+a(1116,351,50,37,'25%','bold','font-size:23px');pages[20]=s
#21
s=base(21,'FUNDRAISING & FINANCIAL PLAN','투자 유치 및 재무 계획')+title('투자금이 '+hl('어떻게 쓰일지')+' 보여주세요.')+rule()
for x,y,f,n,t in [(84,285,'10%','- 운영 자금 및 기타: 20억 원','운영 자금 및 기타 항목은 어떤 운영 효율화나 안<br>정적 서비스 제공에 사용될지, 구체적인 활용 방<br>안을 예시로 작성해보세요.'),(84,495,'30%','- 핵심 인재 영입: 60억 원','핵심 인재 영입을 위해 어떤 직무나 역량의 인재<br>를 확보하고, 이를 통해 어떤 가치를 창출할지 예<br>시를 들어 설명해보세요.'),(879,285,'40%','- R&D 및 기술 고도화: 80억 원','R&D 및 기술 고도화를 위해 어떤 방식으로 투자<br>금액을 활용할지, 구체적인 예시를 들어 설명해<br>보세요.'),(879,495,'20%','- 마케팅 및 고객 확보: 40억 원','마케팅 및 고객 확보를 위해 투자금액을 어떤 채<br>널과 전략에 사용할지, 구체적인 사례를 들어 작<br>성해보세요.')]:
 s+=a(x,y,100,68,f,'bold','font-size:42px;letter-spacing:-1px')+a(x+100,y+16,245,40,n,'bold','font-size:16px;letter-spacing:-.6px')+a(x,y+62,330,100,t,style='font-size:17px;line-height:28px;letter-spacing:-.6px')
s+=rule(461,84,316)+rule(461,879,316)
s+=svg('<path d="M180 180 180 0A180 180 0 0 1 286 326Z" fill="#2b2b2a" stroke="white" stroke-width="5"/><path d="M180 180 286 326A180 180 0 0 1 74 326Z" fill="#666" stroke="white" stroke-width="5"/><path d="M180 180 74 326A180 180 0 0 1 74 34Z" fill="#b2b2b2" stroke="white" stroke-width="5"/><path d="M180 180 74 34A180 180 0 0 1 180 0Z" fill="#d7d7d7" stroke="white" stroke-width="5"/>',460,289,360,360)+ico('pencil',706,393,53,'white')+ico('bulb',617,529,50,'white')+ico('target',526,433,45,'white')+ico('home',584,329,40,'#333')+a(705,449,70,38,'40%','center bold','font-size:26px;color:white')+a(610,584,70,38,'20%','center bold','font-size:26px;color:white')+a(518,473,70,38,'30%','center bold','font-size:20px;color:white')+a(581,372,45,30,'10%','center bold','font-size:20px');pages[21]=s
for i,s in pages.items():
 (R/f'slide_{i:02}.html').write_text(f'<!doctype html><html lang="ko"><meta charset="utf-8"><title>Seedmark replica {i:02}</title><link rel="stylesheet" href="replica.css"><body><main class="slide">{s}</main></body></html>')
print('Replicas written:',len(pages))
