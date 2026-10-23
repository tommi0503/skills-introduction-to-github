from pathlib import Path
import html,json
P=Path(__file__).parent;R=P/'replica';R.mkdir(exist_ok=True)
N='#1e385d';MID='#65719a';SOFT='#969fb7';PALE='#d4d8e2';LIGHT='#f1f2f5';GRAY='#8c8c8c';RULE='#d4d6df'
def box(x,y,w,h,bg='',border='',extra='',content=''):
 return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;'+(f'background:{bg};' if bg else '')+(f'border:{border};' if border else '')+extra+'">'+content+'</div>'
def t(x,y,w,text,size=18,color=N,weight=400,extra=''):
 return box(x,y,w,0,extra=f'height:auto;font-size:{size}px;color:{color};font-weight:{weight};line-height:1.34;{extra}',content=text)
def line(x,y,w,h=1,c=RULE):return box(x,y,w,h,c)
def circ(x,y,d,bg=N,border='',text='',size=18,color='white',extra=''):
 return box(x,y,d,d,bg,border,'border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;'+extra,text if not text else f'<span style="font-size:{size}px;color:{color};font-weight:700">{text}</span>')
def ph(x,y,w,h,round=False):return box(x,y,w,h,'#e9eaec','',('border-radius:50%;' if round else ''))
def pill(x,y,w,h,text,color=N,bg='white',size=24):return box(x,y,w,h,bg,f'2px solid {RULE}','border-radius:999px;display:flex;align-items:center;justify-content:center;font-weight:700;'+f'font-size:{size}px;color:{color}',text)
def hatch(x,y,w,h):return box(x,y,w,h,extra=f'background:repeating-linear-gradient(135deg,transparent 0 2px,{PALE} 2px 3px);opacity:.55')
def shell(title,kick,no,dark=False):
 c='white' if dark else N
 return box(0,0,1280,720,N if dark else 'white')+box(0,0,1280,35,N)+line(1221,0,1,720)+hatch(1221,0,59,35)+t(95,98,1000,kick,18,'#99a3b9')+t(95,122,1080,title,64,c,700,'letter-spacing:-0.7px')+t(1157,98,50,str(no).zfill(2),20,c,700,'text-align:center')
def svg(content,x,y,w,h,view=None):return f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;overflow:visible" viewBox="{view or f"0 0 {w} {h}"}">{content}</svg>'
def icon(x,y,name,d=42,color=N):
 paths={'search':'<circle cx="10" cy="10" r="6"/><path d="m15 15 6 6"/>','target':'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>','bulb':'<path d="M8 16c0-3-4-4-4-8a8 8 0 0 1 16 0c0 4-4 5-4 8zM8 19h8M10 22h4"/>','chart':'<path d="M3 21V13h4v8m3 0V9h4v12m3 0V3h4v18M2 13l7-7 5 1 7-6"/>','user':'<circle cx="12" cy="7" r="4"/><path d="M3 22v-4a9 9 0 0 1 18 0v4z"/>','globe':'<circle cx="12" cy="12" r="10"/><ellipse cx="12" cy="12" rx="5" ry="10"/><path d="M2 12h20M4 6h16M4 18h16"/>','chip':'<rect x="5" y="5" width="14" height="14" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M8 1v4M12 1v4M16 1v4M8 19v4M12 19v4M16 19v4M1 8h4M1 12h4M1 16h4M19 8h4M19 12h4M19 16h4"/>','card':'<rect x="2" y="5" width="20" height="15" rx="2"/><path d="M2 10h20M5 15h5"/>','heart':'<path d="M12 21 2 11C-2 2 9-1 12 6c3-7 14-4 10 5z"/>','pie':'<path d="M12 2v10h10A10 10 0 0 0 12 2ZM9 4a9 9 0 1 0 11 11H9z"/>'}
 return svg(f'<g fill="none" stroke="{color}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{paths.get(name,paths["target"])}</g>',x,y,d,d,'0 0 24 24')
S={}; data=[]
# 01
s=box(0,0,1280,720,N)+line(1039,0,1,720)+line(1221,0,1,720)+line(0,588,1280)+line(0,653,1280)+hatch(1039,588,182,65)
s+=t(95,105,900,'가이드에 따라 쉽고 빠르게 만드는',36,'#96a3be')+t(95,164,950,'명확하게 전달하는',76,'white',400,'letter-spacing:-2px')+t(95,260,950,'회사 소개서',76,'white',700,'letter-spacing:-2px')+t(95,612,400,'MIRI COMPANY',18,'white');S[1]=s
# 02
s=box(0,0,1280,720,'white')+box(0,0,404,720,N)+line(404,57,876)+line(404,239,876)+line(1155,0,1,720)+line(1221,0,1,720)+hatch(1155,57,66,182)+t(95,99,300,'TABLE OF CONTENTS',18,'#96a3be')+t(95,131,300,'목차',76,'white',700)
for j,names in enumerate([['회사 개요','회사 비전','전략방향','주요 사업','운영흐름'],['장비 현황','KPI 구조','회사 강점','성과 추이','매출 비중']]):
 for i,name in enumerate(names):
  x=466+j*342;y=343+i*65;s+=t(x,y,265,name,32,'#5d5d5d',500)+t(x+225,y,64,str(i+1+j*5).zfill(2),34,N,700,'text-align:center')+line(x-2,y+51,290)
S[2]=s
#03
s=box(0,0,1280,720,N)+ph(0,337,1280,383)+box(57,63,1164,593,'white')+t(123,98,1000,'COMPANY OVERVIEW',18,'#969fb7')+t(123,129,1020,'회사 개요',64,N,700)+t(1155,98,45,'01',20,N,700)+t(123,239,1040,'우리는 기술과 경험을 바탕으로<br>현장의 문제를 구조적으로 해결하는 기업입니다.',28,N,700)+line(123,337,1030)
s+=t(123,379,475,'우리는 기술과 경험을 바탕으로<br>현장의 문제를 구조적으로 바라보고 해결해 왔습니다.<br><br>사업의 출발점부터 현재에 이르기까지<br>문제를 함께 고민하고 해결해온 과정 속에서<br>신뢰받는 파트너로서의 관계를 만들어 왔습니다.<br><br>이러한 접근 방식은<br>다양한 프로젝트 경험 속에서 축적된 우리의 일하는 기준입니다.',18,'#656565')+t(640,379,518,'시장의 변화와 고객의 요구를 면밀히 분석해<br>실행 가능한 해법으로 연결합니다.<br><br>단기적인 대응보다 문제의 본질을 정의하는 것을 우선하며,<br>복잡한 상황을 명확한 구조로 정리하는 데 집중합니다.<br><br><b style="color:'+N+'">우리는 단순한 서비스 제공을 넘어,<br>고객의 상황에 맞는 방향과 결과를 함께 만들어갑니다.</b>',18,'#656565');S[3]=s
#04
s=box(0,0,1280,720,'white')+ph(830,0,450,720)+line(58,0,1,720)+line(0,380,966)+line(0,655,966)+t(95,99,720,'COMPANY OVERVIEW (DETAILS)',18,SOFT)+t(95,131,720,'회사 개요 상세',64,N,700)+t(1155,98,50,'02',20,N,700)+box(59,381,907,274,'white')
for j,pairs in enumerate([[('산업','제조업'),('기업 구분','중소기업'),('대표자','김미리'),('주요 사업','제조 장비 개발 및 대여')],[('사원수','100명'),('설립일','20xx.06.13'),('매출액','400억'),('주소','미리시 미리구 미리대로 7001번 길')]]):
 for i,(a,b) in enumerate(pairs):x=95+j*420;y=419+i*58;s+=t(x,y,130,a,20,N,700)+t(x+122,y,320,b,20,'#656565')
S[4]=s
#05
s=box(0,0,1280,720,'white')+box(502,0,778,720,N)+line(1221,0,1,720)+line(0,655,1280)+t(95,99,400,'VISION & MISSION',18,SOFT)+t(95,130,250,'회사<br>비전',64,N,700)+t(1155,98,50,'03',20,'white',700)
notes=['해당 페이지는 회사의 핵심 가치와 비전을 적는 페이지입니다. 회사가 추구하는 핵심적인 가치 세 가지만 뽑아보세요. 이 가치를 추구하는 이유는 무엇인지, 이것들을 통해 이루고 싶은 비전이나 목표는 무엇인지 설명해 주세요.','회사가 추구하는 비전을 이루기 위해 어떤 노력과 사업을 하는지 적어보세요. 회사의 사업과 핵심 가치가 어떤 연관성을 가지고 있는지 설명해 주세요. 비전으로 설득하고 싶은 분들은 무엇인지 적어보세요.','회사의 비전은 누구나 이해하기 쉽도록 명확하고 간결하게 작성해야 합니다. 회사가 장기적으로 달성하려는 목표는 무엇인지 생각해 보세요. 직원과 고객에게 영감을 줄 수 있는 내용을 적으면 좋습니다.']
for i,name in enumerate(['고객과 함께<br>성장하자','최고의 품질을<br>추구하자','정직함으로<br>진심을 다하자']):
 x=292+i*291;s+=box(x,98,275,524,'white')+t(x+23,256,230,'VISION '+str(i+1),28,PALE,700)+line(x,307,275)+t(x+23,329,228,name,28,N,700)+t(x+23,423,228,notes[i],18,GRAY)
S[5]=s
#06
s=shell('비전 구조','VISION FRAMEWORK',4)
levels=[(397,262,140,100,N,'키워드 A'),(336,369,264,81,MID,'키워드 B'),(270,457,394,88,SOFT,'키워드 C　　 키워드 C'),(196,551,543,103,PALE,'키워드 D　　 키워드 D　　 키워드 D')]
for i,(x,y,w,h,c,txt) in enumerate(levels):
 pts='50% 0, 100% 100%, 0 100%' if i==0 else ('16% 0,84% 0,100% 100%,0 100%')
 s+=box(x,y,w,h,c,extra=f'clip-path:polygon({pts});display:flex;align-items:center;justify-content:center;color:white;font-size:18px;font-weight:700',content=txt)
for i,(a,b) in enumerate(zip(['행동','욕구','흥미','인지'],['하단은 기초, 상단은 핵심입니다.','계층 구조로 단계별 성장을 보여줘요.','피라미드 구조는 시각적 안정감을 줍니다.','핵심 키워드 아래 탄탄한 기초를 강조해요.'])):
 y=263+i*102;s+=pill(96,y,98,66,a)+t(774,y+21,410,b,18,GRAY)+line(96,y+83,1184)
S[6]=s
#07
s=shell('핵심 가치 체계','CORE VALUES FRAMEWORK',5)
for x,y,a,b in [(95,260,'유기적인 연결망','각 요소가 독립적이지 않고 서로 긴밀하게 영향을 주고받는 유기적인 관계임을 보여줍니다.'),(877,260,'균형 잡힌 배치','위아래 순서가 있는 목록형과 달리 원형 배치는 모든 요소를 동등한 비중으로 다룹니다.'),(95,514,'핵심은 정중앙에','중앙에 가장 중요한 키워드를 배치하고 주변으로 뻗어 나가는 원형 구조를 활용해 보세요.'),(877,514,'정보의 생태 사이클','시선이 중앙에서 시작해 바깥으로 자연스럽게 이동하며 정보의 위계와 관계를 파악합니다.')]:
 s+=line(x,y,307)+line(x,y+54,307)+t(x,y+10,307,a,28,N,700,'text-align:center')+t(x+5,y+76,297,b,18,GRAY,400,'text-align:center')
s+=svg(f'<path d="M446 573a194 194 0 0 1 388 0" fill="none" stroke="{RULE}" stroke-width="2"/>',0,0,1280,720)
for x,y,name in [(427,427,'정직'),(529,342,'신뢰'),(663,342,'도전'),(765,427,'혁신')]:s+=circ(x,y,86,N,f'6px solid {PALE}',name)
s+=t(560,479,160,'핵심 가치',28,N,700,'text-align:center')+t(560,515,160,'Value',20,SOFT,700,'text-align:center');S[7]=s
#08
s=shell('전략 방향','STRATEGIC DIRECTION',6)
for i,(a,b) in enumerate([('노출','다양한 자료 중 핵심만 남기는 과정을 보여주세요. 위쪽에는 전체 데이터를 두고 아래쪽에는 최종 결과를 배치해 집중을 시각화합니다.'),('유입','시선이 자연스럽게 아래로 모이는 역삼각형 구조를 활용해 보세요. 상단에서 시작해 하단으로 내려갈수록 정보가 구체화됩니다.'),('구매','전체 시장에서 거점 시장으로 범위를 좁혀가며 타겟의 선명도를 높이세요. 대상은 줄어들지만 공략해야 할 대상이 누구인지 명확히 정의 내는 과정을 담습니다.')]):
 y=268+i*142;s+=t(95,y,650,a,28,N,700)+t(95,y+43,620,b,18,GRAY);s+=line(0,y+111,779+i*74) if i<2 else ''
for i,(y,w,c) in enumerate([(260,456,SOFT),(395,301,MID),(527,150,N)]):
 s+=box(956-w/2,y,w,129,c,extra='clip-path:polygon(0 0,100% 0,50% 100%);' if i==2 else 'clip-path:polygon(0 0,100% 0,82% 100%,18% 100%);')+pill(881,y+32,150,66,'STEP 0'+str(i+1),'white',c,18)
S[8]=s
#09
s=shell('전략 핵심 포인트','KEY STRATEGIC POINTS',7,True)
for i,(fig,name) in enumerate([('00%','성과 달성'),('+00%','전년 대비 성장'),('00%','시장 점유율'),('000%','목표 달성률')]):
 x=95+(i%2)*553;y=260+(i//2)*206;s+=box(x,y,537,188,'white')+t(x+42,y+37,260,fig,44,N,700)+t(x+267,y+46,228,name,28,N,700,'text-align:right')+line(x+42,y+88,453)+t(x+42,y+112,453,'타이포그래피 자체가 디자인이 되도록 폰트 굵기를 조절하여 세련된 느낌을 연출해 보세요.',18,GRAY)
S[9]=s
#10
s=shell('전략 흐름','STRATEGY FLOW',8)+t(95,263,1080,'단계별 과정을 순서대로 보여줘 이해를 돕습니다.',28,N,700)
for i,(a,b,ic) in enumerate([('노출','왜 이 프로젝트가 시작되었는지 그리고 어떤 문제를 해결하고자 하는지 구체적으로 서술해 보세요.','target'),('실행','문제의 원인을 정확히 파악해야 올바른 해결책이 나올 수 있으니 현상을 깊이 있게 분석하세요.','bulb'),('점검','다양한 해결 방안을 모색하는 브레인스토밍을 통해 도출된 아이디어 중 핵심을 추려내야 합니다.','search'),('개선','목표 달성을 위한 세부 전략을 수립하고 필요한 예산과 인력 그리고 일정을 확정 지어야 합니다.','chart')]):
 x=95+i*274;s+=box(95+i*264,320,304,81,N,extra='clip-path:polygon(0 0,85% 0,100% 50%,85% 100%,0 100%,15% 50%);display:flex;align-items:center;justify-content:center;color:white;font-size:18px;font-weight:700',content=str(i+1)+' STEP')+circ(x,415,60,LIGHT)+icon(x+14,429,ic,33)+line(x,488,268)+line(x,542,268)+line(x,655,268)+t(x+8,500,250,a,28,N,700)+t(x+8,566,252,b,18,GRAY)
S[10]=s
#11
s=shell('주요 사업','KEY BUSINESS AREAS',9)
for i,(a,b) in enumerate([('고성능 부품 개발','해당 페이지는 회사의 주요 사업에 관해 설명하는 페이지 입니다. 각 사업의 핵심 포인트를 간결하고 명확하게 적어주세요. 현재 업계 트렌드나 시장의 미래 전망을 언급해 가능성을 강조하세요.'),('산업용 장비 개발','사업의 장점과 혜택을 고객의 관점에서 설명해 보세요. 고객이 얻을 수 있는 장점을 명확하게 전달하는 것이 중요합니다. 구체적인 고객 사례를 설명하며 사업의 실제 효과를 보여주세요.'),('제조 장비 개발','사업 설명에 중요한 키워드나 문장을 강조해 보세요. 고객이 중요한 정보를 쉽게 파악하도록 도와줍니다. 문장은 짧고 간결하게 적는 것을 추천합니다. 문장이 길어지면 고객이 이해하기 어려울 수 있습니다.'),('제조 장비 대여','사업의 성공 사례를 소개하며 회사의 사업이 효과적이었음을 보여주세요. 주요 파트너사와 협력 관계를 강조하며 신뢰성을 보여주세요. 기술적 혁신이나 회사만의 솔루션을 보여주는 것도 효과적입니다.')]):
 x=95+(i%2)*585;y=260+(i//2)*198;s+=line(0,y,1221)+box(x+397,y,148,31,N,extra='color:white;text-align:center;font-size:18px;font-weight:700;padding-top:5px',content='주요 사업 '+str(i+1))+t(x,y+43,510,a,28,N,700)+t(x,y+96,510,b,18,GRAY)
s+=line(640,260,1,396)+line(0,655,1221);S[11]=s
#12
s=shell('사업 구조','BUSINESS STRUCTURE',10)
for i,(a,b) in enumerate([('주요 특징','시선은 왼쪽에서 오른쪽으로 이동합니다. 정보를 가로로 나열하면 내용을 편안하게 읽을 수 있습니다.'),('핵심 역량','시간 순서대로 진행되는 프로젝트 일정이나 단계별 프로세스를 설명할 때 가장 효과적입니다.'),('체크 포인트','핵심 내용을 가로로 나란히 배치하여 복잡한 정보를 한눈에 비교할 수 있도록 정리해 보세요.'),('서비스','다루는 항목들의 비중이 서로 비슷할 때 사용하면 가장 안정적이고 효과적인 구조입니다.')]):
 x=95+i*281;s+=box(x,260,246,12,N)+t(x,285,245,'ABCD'[i],44,N,700)+line(x,351,246)+t(x,365,246,a,28,N,700)+line(x,406,246)+t(x,429,246,b,18,GRAY)
 for j in range(2):s+=t(x,541+j*71,246,'•　'+['항목의 비중이 비슷할 때 효과적입니다.','가로로 나열하여 보기 편하게 만드세요.','긴 줄글보다는 개조식으로 짧게 끊어 쓰세요.','텍스트 분량을 맞춰 균형을 잡으세요.'][i],18,N)
 if i<3:s+=line(x+263,260,1,395)
S[12]=s
#13
s=shell('사업 프로세스','BUSINESS PROCESS',11,True)+t(95,264,1090,'복잡한 절차를 단순화하여 명쾌하게 정리했어요.',28,PALE,700)+line(130,348,1,273)
for i,(a,b,ic) in enumerate([('인지','읽는 이에게 전체적인 방향성을 제시하고 프로젝트에 대한 기대감을 심어주는 도입부 역할을 합니다.','bulb'),('탐색','객관적인 수치나 근거 자료를 제시하여 분석의 신뢰도를 높이고 논리적인 타당성을 확보해야 해요.','search'),('구매','아이디어 선정 기준과 이유를 명확히 명시하면 기획의 설득력이 높아지고 공감을 얻기 쉽습니다.','card'),('리뷰','막연했던 아이디어가 체계적인 실행 계획으로 구체화되는 과정을 보여주어 신뢰도를 높여 보세요.','pie')]):
 y=314+i*90;s+=circ(95,y,70,'white')+icon(112,y+17,ic,36)+t(200,y+20,60,str(i+1).zfill(2),28,PALE,700)+box(279,y+1,905,66,'',f'2px solid {PALE}','border-radius:999px')+t(319,y+18,90,a,28,'white',700)+t(415,y+24,740,b,18,'white')
S[13]=s
#14
s=shell('운영 흐름','OPERATIONAL FLOW',12)
for i,(a,b) in enumerate([('노출','프로젝트의 정의와 범위를 명확히 설정하여 앞으로 전개될 내용의 길잡이 역할을 하는 단계입니다.'),('유입','내부 역량과 외부 환경을 종합적으로 분석하여 우리가 가진 강점과 약점을 명확히 파악해 보세요.'),('활동','시장의 빈틈을 파고드는 전략을 수립하여 프로젝트가 성공할 수밖에 없는 이유를 증명해 보세요.'),('추천','다양한 환경에서의 테스트 결과를 제시하여 서비스가 어떤 상황에서도 잘 작동함을 증명해야 해요.'),('재구매','단순한 기능 구현을 넘어 사용자 경험을 고려한 디테일한 개발 과정을 보여주어 전문성을 높여요.'),('전환','각 단계별로 필요한 자원을 배분하고 리스크 관리 계획을 세워 프로젝트의 안정성을 확보하세요.')]):
 col=i%3;row=i//3;x=95+col*371;y=260+row*226;c=[N,MID,SOFT][col];s+=box(x,y,346,46,c,extra=('clip-path:polygon(0 50%,7% 0,100% 0,93% 50%,100% 100%,7% 100%);' if row else 'clip-path:polygon(0 0,94% 0,100% 50%,94% 100%,0 100%,7% 50%);')+'color:white;text-align:'+('left' if row else 'right')+';padding:10px 55px;font-weight:700;font-size:20px',content=str((i+1) if row==0 else (9-i)).zfill(2))+t(x,y+60,346,a,28,N,700)+line(x,y+106,346)+t(x,y+127,346,b,18,GRAY)
S[14]=s
#15
s=shell('장비 현황','PRODUCTS & SERVICES',13)+line(0,354,1221)
for i in range(3):
 x=95+i*371;s+=circ(x+79,260,188,'white',f'2px solid {RULE}')+ph(x+88,269,170,170,True)+circ(x+225,260,42,N,text='ABC'[i],size=20)
 for j,(a,b) in enumerate([('장비 명','제조 장비'),('제조회사','미리 컴퍼니'),('고유 번호','00011110'),('모델명','Miri-00000')]):
  y=479+j*47;s+=t(x+28,y,160,a,20,N,700)+t(x+165,y,170,b,20,N,400,'text-align:center')+line(x,y+36,346)
S[15]=s
#16
s=shell('장비 스펙','PRODUCT & SERVICE DETAILS',14)
for i in range(2):
 x=95+i*573;s+=box(x,260,515,65,N)+t(x+36,277,220,'모델명',28,'white',700)+t(x+250,277,230,'Miri-00000',28,'white',700,'text-align:right')+box(x,339,515,315,LIGHT)
 for j,(a,b) in enumerate([('구동 형태','Motor Driver'),('전압','24VDC'),('장비 하중','300kg'),('길이','1500mm'),('높이','1200mm'),('넓이','800mm')]):
  y=368+j*47;s+=t(x+20,y,240,a,20,N,700)+t(x+270,y,226,b,20,N,400,'text-align:right')+line(x+20,y+36,476)
S[16]=s
#17
s=shell('KPI 구조','KPI FRAMEWORK',15,True)
for i,(a,b) in enumerate([('핵심 시장','프로젝트의 안정성을 증명하는 핵심 강점을 시각적으로 강조하세요. 긍정적인 내부 요인이 무엇인지 보여줍니다.'),('유망 시장','분석 결과를 토대로 약점을 보완할 구체적인 행동 지침을 만드세요. 문제를 인식하는 것이 해결의 시작입니다.'),('쇠퇴 시장','약점을 보완하고 기회를 활용하는 반전 전략을 짤 수도 있습니다. 외부의 호재가 내부의 부족함을 채워줍니다.'),('철수 시장','분석을 통해 도출된 위험 요인은 위기 관리 매뉴얼의 기초가 됩니다. 선제적인 방어가 최선의 공격입니다.')]):
 x=95+(i%2)*562;y=260+(i//2)*213;s+=box(x,y,527,181,SOFT if i==0 else '',f'1px solid {PALE}')+t(x+37,y+38,452,a,28,'white',700,'text-align:'+('right' if i%2 else 'left'))+t(x+37,y+83,330,b,18,'white',400,'margin-left:'+('120px;text-align:right;' if i%2 else '0;'))
s+=circ(492,309,296,'',f'2px solid {PALE}')+line(640,310,1,295)+line(493,457,294)+circ(558,376,164,'white',text='시장<br>매력도',size=28,color=N)
for x,y,ic in [(538,369,'search'),(707,369,'target'),(538,521,'chart'),(707,521,'pie')]:s+=icon(x,y,ic,38,PALE)
S[17]=s
#18
s=shell('회사 강점','COMPANY STRENGTHS',16)
for x,y,a,b in [(95,279,'혁신적인 기술','해당 페이지는 회사의 강점과 경쟁력을 적는 페이지입니다.<br>키워드를 적어보세요.'),(95,495,'고객 중심 서비스','경쟁사와 차별화되는 우리 회사만의<br>독특한 서비스와 제품을 강조해 보세요.'),(881,226,'강력한 파트너십','실제 고객의 긍정적인 피드백이나<br>추천사를 인용해 신뢰도를 높여보세요.'),(881,380,'글로벌 네트워크','높은 고객 유지율을 강조하며 회사의<br>네트워크가 견고함을 보여주세요.'),(881,535,'지속 가능한 성장력','회사의 미래 가능성을 보여줄 수 있는<br>장기적인 비전과 목표를 보여주세요.')]:
 s+=box(x,y,307,54,LIGHT)+line(x,y,307)+t(x,y+11,307,a,28,N,700,'text-align:center')+t(x+8,y+77,291,'• '+b,18,GRAY)
s+=svg(f'<polygon points="640,308 788,421 735,607 548,607 492,421" fill="{LIGHT}" stroke="{N}"/>',0,0,1280,720)+t(554,451,180,'우리의 강점',28,N,700,'text-align:center')+t(554,490,180,'Strength',20,SOFT,700,'text-align:center')
for x,y,ic in [(591,257,'globe'),(444,373,'chip'),(739,373,'chart'),(499,559,'user'),(686,559,'heart')]:s+=circ(x,y,96,N,f'6px solid {PALE}')+icon(x+28,y+28,ic,40,'white')
S[18]=s
#19
s=shell('협업 및 파트너십','COLLABORATION & PARTNERSHIPS',17)
for i,(a,b) in enumerate([('교육 훈련','복합 원인을 나열해요.'),('업무 효율','핵심 메시지 한 문장.')]):
 x=95+i*573;s+=box(x,260,515,65,MID if i==0 else N)+t(x,277,515,a,28,'white',700,'text-align:center')+box(x,339,515,315,LIGHT)+pill(x+32,365,450,65,b)+t(x+31,450,455,'주장을 뒷받침할 수 있는 데이터를 이 공간에 배치해 보세요. 원인에 대한 객관적인 증거를 텍스트로 요약하여 제시하면 추측이 아닌 분석임을 증명하게 됩니다.' if i==0 else '긍정적인 결과에 대한 분석이라면 이 성공 요인을 어떻게 유지하고 다른 프로젝트에 확산시킬지 설명하세요. 단순한 결과 보고를 넘어 미래 전략을 제시합니다.',18,GRAY)
 for j in range(3):s+=t(x+31,537+j*36,455,'•　'+('핵심 키워드 위주로 간결하게 작성해요.' if i==0 else '결론적으로 도출된 핵심 메시지 요약하세요.'),18,N)
s+=box(610,269,54,47,MID,extra='clip-path:polygon(0 20%,65% 20%,65% 0,100% 50%,65% 100%,65% 80%,0 80%);');S[19]=s
#20
s=shell('KPI 상세 지표','KPI DETAILS',18)
for j,(row,col,fg) in enumerate([(['구분','1분기','2분기','3분기','4분기'],LIGHT,N),(['매출 목표','10억원','15억원','20억원','25억원'],'white',N),(['달성률','98%','105%','100%','110%'],N,'white')]):
 y=[260,310,394][j];h=[50,84,84][j]
 for i,txt in enumerate(row):s+=box(95+i*113.4,y,113.4,h,col,f'1px solid {RULE}','display:flex;align-items:center;justify-content:center;font-size:'+str(20 if j==0 else 23)+'px;font-weight:'+str(700 if i==0 or j==2 else 400)+f';color:{fg}',txt)
s+=box(95,505,567,149,'',f'1px solid {RULE}')+t(125,532,507,'많은 데이터를 한 번에 정리하기에 표만큼 좋은 도구는 없습니다. 동일한 기준에 따라 데이터를 칼럼별로 입력하면, 읽는 이가 정보를 쉽게 비교하고 분석할 수 있죠. 각 항목에 구체적인 수치나 단위를 정확하게 기입하여 객관성을 확보하고 프레젠테이션의 신뢰도를 높이세요.',18,GRAY)+box(722,260,461,394,LIGHT)
for i,v in enumerate([0,10,20,30]):y=595-v*9.6;s+=line(790,y,354)+t(749,y-12,33,str(v),18,N,400,'text-align:right')
for i,v in enumerate([10,15,20,25]):x=813+i*88;s+=box(x,595-v*9.6,44,v*9.6,N)+t(x-12,597,70,str(i+1)+'분기',20,N,400,'text-align:center')+t(x-10,595-v*9.6-28,65,str(v),18,N,400,'text-align:center')
s+=pill(1060,300,99,46,'25',N,'white',28);S[20]=s
#21
s=shell('주요 수치 요약','KEY FIGURES',19,True)+circ(95,260,113,'', '1px solid white','1위',40)+t(95,440,235,'업계 순위',28,'white',700)+t(95,494,233,'숫자를 크게 배치하여 정보를 직관적으로 전달하는 레이아웃입니다. 긴 설명보다 명확한 수치 하나가 내용을 빠르게 이해시킵니다. 핵심 결과나 지표를 강조할 때 사용하세요.',18,'white')
for i,(f,a) in enumerate([('No.1','브랜드 평판'),('4.9점','고객 평점'),('1위','선호도 조사'),('AAA','등급 획득')]):
 x=367+(i%2)*415;y=260+(i//2)*206;s+=box(x,y,402,188,'white')+t(x+31,y+37,220,f,44,N,700)+t(x+190,y+46,181,a,28,N,700,'text-align:right')+line(x+31,y+88,340)+t(x+31,y+112,340,'가장 자랑하고 싶은 핵심 성과를 크게 적어 시선을 사로잡으세요.' if i in [0,3] else '복잡한 표 대신 핵심 지표만 골라내어 직관적으로 보여주는 게 좋습니다.',18,GRAY)
S[21]=s
#22
s=shell('성과 추이','PERFORMANCE TREND',20)+line(95,260,1088)+line(95,458,475)+line(95,655,1088)+box(570,261,613,394,LIGHT)+t(116,296,429,'과거의 기록을 바탕으로 전략적 의사결정을 내려야 할 때 필수적인 그래프입니다. 꾸준히 성장하고 있는지, 아니면 특정 주기로 등락을 반복하는지 패턴을 분석해 보세요. 변화의 흐름을 읽는 것은 곧 경쟁력이 되며, 이 페이지는 비즈니스의 나침반 역할을 톡톡히 해냅니다.',18,GRAY)+t(116,498,250,'일별 생산량 최대',28,N,700)+pill(320,494,212,72,'5,200',N,'white',44)+t(116,598,429,'단순한 기록을 넘어 전략적 의사결정을 돕는 나침반이 됩니다.',18,GRAY)+box(1021,261,162,31,N,extra='color:white;text-align:center;font-weight:700;font-size:18px;padding-top:5px',content='일별 생산량 추세')
s+=box(798,458,74,166,PALE)+box(1080,322,74,302,PALE)
vals=[5000,4500,4000,5000,4800,5000,5200];pts=[]
for i,v in enumerate(vals):
 x=700+i*68;y=582-v*.0384;pts.append(f'{x},{y}');s+=circ(x-5,y-5,10,N)+t(x-34,y-31,68,f'{v:,}',18,N,400,'text-align:center')+t(x-34,590,68,['월요일','화요일','수요일','목요일','금요일','토요일','일요일'][i],18,N,400,'text-align:center')
s+=svg(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{N}" stroke-width="1"/>',0,0,1280,720)
for i,v in enumerate([0,2000,4000,6000]):s+=t(610,570-v*.0384,48,f'{v:,}',18,N,400,'text-align:right')
S[22]=s
#23
s=shell('성과 비교','PERFORMANCE COMPARISON',21)+line(95,260,1088)+line(95,655,1088)+box(95,261,475,394,N)
for i,v in enumerate([0,20,40,60,80,100]):s+=t(125,582-v*3,40,str(v),18,'white',400,'text-align:right')
for i,v in enumerate([80,100]):s+=box(215+i*157,594-v*3,116,v*3,PALE if i==0 else 'white')+circ(234+i*140,490,94,'',f'1px solid {N if i else MID}', ['경쟁사','자사'][i],18,N)
s+=t(264,600,160,'고객 유입 수',18,'white',400,'text-align:center')+circ(622,284,60,LIGHT)+icon(637,298,'user',32)+t(699,299,450,'월별 고객 유입 수',28,N,700)+line(570,361,613)
for i,(f,a,b) in enumerate([('80만 명','경쟁사','데이터의 크기를 길이로 변환하여 항목 간의 차이를 직관적으로 비교하는 데 최적화된 레이아웃으로 활용해 보세요.'),('100만 명','자사','가장 긴 막대와 짧은 막대를 대조하면 우열이 한눈에 들어옵니다. 복잡한 수치도 그림이 되면 이해 속도가 빨라지죠.')]):
 x=622+i*281;s+=pill(x,391,244,66,f,SOFT if i==0 else N)+t(x,479,245,a,28,N,700)+t(x,532,245,b,18,GRAY)
S[23]=s
#24
s=shell('매출 비중','REVENUE DISTRIBUTION',22)
for i,(a,f,c) in enumerate([('북미','20%',PALE),('아시아','10%',MID),('남미','25%','#bcc3d5'),('아프리카','30%',N),('유럽','15%',SOFT)]):
 x=95+(i%2)*263;y=260+(i//2)*74;s+=pill(x,y,245,66,'',N)+box(x+18,y+26,13,13,c)+t(x+43,y+16,130,a,28,N,700)+t(x+143,y+16,82,f,28,SOFT,700,'text-align:center')
s+=t(95,499,500,'글로벌 매출 비중',28,N,700)+t(95,550,515,'원 그래프와 유사하지만 중앙 공간 활용도가 높아 정보 전달과 디자인을 동시에 잡을 수 있는 레이아웃입니다. 그래프 옆이나 하단에는 데이터가 시사하는 핵심 내용을 요약해 적어주세요. 그래프에서 도출된 결론을 텍스트로 보완하면 읽는 이에게 더욱 강력한 설득력을 줍니다.',18,GRAY)
s+=box(774,260,336,336,extra=f'border-radius:50%;background:conic-gradient({PALE} 0 20%,#bcc3d5 20% 45%,{SOFT} 45% 60%,{MID} 60% 70%,{N} 70% 100%);')+circ(841,327,202,LIGHT,text='글로벌 매출<br><span style="font-size:18px;color:'+SOFT+'">Global</span>',size=28,color=N)
for x,y,a in [(1150,264,'북미'),(1113,593,'남미'),(761,593,'유럽'),(689,540,'아시아'),(673,282,'아프리카')]:s+=t(x,y,120,a,18,N,700)
s+=svg(f'<g fill="none" stroke="{RULE}" stroke-width="2"><path d="M799 346 780 306H673M1081 335 1098 287H1180M1028 572 1049 620H1157M867 577 855 620H749M805 522 781 569H689"/></g>',0,0,1280,720)
for x,y,a in [(1004,305,'20'),(1046,480,'25'),(911,553,'15'),(802,504,'10'),(819,337,'30')]:s+=t(x,y,45,a,18,'white',400,'text-align:center;text-shadow:0 1px 1px '+N)
S[24]=s
#25
s=box(0,0,1280,720,N)+line(57,0,1,720)+line(920,0,1,720)+line(1221,0,1,720)+line(0,474,1280)+line(0,653,1280)+hatch(920,475,301,178)+t(95,282,950,'SECTION OVERVIEW',18,'#99a3b9')+t(95,320,900,'이번 섹션에서 다룰 핵심 내용을<br>간단히 정리합니다',48,'white',700)+t(95,515,820,'챕터가 존재하는 이유를 명확하게 설명해 보세요.',18,'white')+circ(1160,592,37,'white')+svg(f'<path d="m0 0 9 9-9 9" fill="none" stroke="{N}" stroke-width="2"/>',1173,602,10,18);S[25]=s
#26
s=shell('프로젝트 일정','PROJECT TIMELINE',24)+t(95,263,1089,'장기 프로젝트의 경우 월 단위로, 단기 프로젝트는 주 단위로 쪼개어 관리하는 것이 좋습니다.',18,GRAY)
for i,a in enumerate(['사업 기획','1분기','2분기','3분기','4분기']):s+=t(95 if i==0 else 275+(i-1)*227,310,200,a,20,N,700 if i==0 else 400)
for i in range(4):
 y=343+i*77;s+=line(95,y,1088)+t(95,y+27,170,'핵심 기능 구현',20,N,700)
for x,y,w,c,a in [(275,357,454,SOFT,'일정 관리를 한눈에.'),(275,435,161,N,'일정 관리'),(465,435,432,MID,'막대 길이로 흐름을 파악하세요.'),(592,512,389,MID,'일정 관리를 한눈에.'),(729,590,454,N,'막대 길이로 흐름을 파악하세요.')]:s+=box(x,y,w,50,c,extra='color:white;font-size:20px;font-weight:700;padding:13px;',content=a)
s+=line(95,655,1088);S[26]=s
#27
s=shell('연간 일정','ANNUAL SCHEDULE',25)+pill(95,261,260,86,'<span style="text-align:center;color:'+SOFT+'">15일<br><small style="font-size:20px;color:'+N+'">리드 회의</small></span>',size=28)+pill(380,261,260,86,'<span style="text-align:center;color:'+SOFT+'">15~20일<br><small style="font-size:20px;color:'+N+'">성과 평가 기간</small></span>',size=28)+box(95,374,547,280,LIGHT)+line(95,374,547)+t(116,397,510,'일정 관리 가이드',28,N,700)+box(662,261,521,393,LIGHT)
for i in range(4):s+=box(117,445+i*52,26,26,'',f'1px solid {N}')+svg(f'<path d="m1 11 8 8L29 0" fill="none" stroke="{N}" stroke-width="3"/>',120,445+i*52,28,20)+t(167,447+i*52,451,'일정을 한눈에 관리하세요.' if i==0 else '마감 기한이 명시된 일정은 시간을 엄수해 주시기 바랍니다.',18,N,700)
for i,a in enumerate(['SUN','MON','TUE','WED','THU','FRI','SAT']):s+=t(680+i*69.5,281,69,a,16,N,400,'text-align:center')
s+=line(680,306,486)
for day in range(1,32):
 i=day;col=i%7;row=i//7;x=680+col*69.5;y=315+row*67;s+=t(x,y,69,str(day),16,N,400,'text-align:center')
for i in range(6):s+=box(749+i*69.5,441,69.5,34,MID if i==0 else N,extra='color:white;text-align:center;padding-top:8px;font-size:16px',content=str(15+i))+box(749+i*69.5,475,69.5,33,PALE)
s+=t(754,482,75,'리드회의',14,N)+t(926,482,197,'성과 평가 기간',14,N);S[27]=s
#28
s=shell('중장기 로드맵','MID-TO-LONG TERM ROADMAP',26)+line(0,456,1221)
for i,(a,b) in enumerate([('1분기','법인 설립'),('2분기','서비스 출시'),('3분기','특허 등록'),('4분기','투자 유치')]):
 x=95+i*277;above=i%2==1;y=456 if above else 402;s+=box(x,y,258,54,N)+t(x+30,y+11,210,a,28,'white',700)
 yy=261 if above else 522;s+=t(x+31,yy,220,b,28,N,700)+t(x+31,yy+51,220,'프로젝트의 전체 과정을 선으로 연결하여 시각화하세요. 각 단계의 핵심을 아이콘으로 표현하면 전달력이 좋아집니다.',18,GRAY)+line(x if not above else x,279 if above else 456,1,177)+circ(x-4,(279 if above else 633)-4,9,N)
S[28]=s
#29
s=shell('전략 포지션','STRATEGIC POSITIONING',27)+box(95,260,515,394,LIGHT)+line(166,278,2,327,N)+line(166,604,421,2,N)+line(167,442,420)+line(377,278,1,327)+t(115,281,45,'빠름',18,N)+t(115,580,45,'느림',18,N)+t(206,613,100,'불안정',18,N)+t(536,613,70,'안정',18,N)
for x,y,a,c in [(217,486,'버전 1','white'),(250,389,'버전 2',SOFT),(362,471,'버전 3',SOFT),(327,318,'버전 4',MID),(493,412,'버전 5',MID),(493,280,'버전 6',N)]:s+=circ(x,y,94,c,f'1px solid {RULE}' if c=='white' else '',a,18,N if c=='white' else 'white')
s+=t(681,264,510,'서비스 안정성 및 속도',28,N,700)+t(681,309,510,'가까이 모여 있는 점들을 하나의 그룹으로 묶어서 설명해 보세요. 유사한 특징을 가진 항목들을 군집화합니다.',18,GRAY)
for i,b in enumerate(['느린속도, 불안정','중간속도, 불안정','느린속도, 안정','빠른속도, 낮은안정','중간속도, 안정','빠른속도, 높은안정']):
 y=396+i*44;s+=box(681,y,503,44,N if i==5 else 'white')+t(705,y+10,130,'버전 '+str(i+1),20,'white' if i==5 else N,700,'text-align:center')+t(894,y+10,290,b,20,'white' if i==5 else N,400,'text-align:center')+line(681,y+43,503)
s+=svg(f'<path d="M300 512 487 357m-12 0 12 0-2 13" fill="none" stroke="{PALE}" stroke-width="8"/>',0,0,1280,720)
S[29]=s
#30
s=box(0,0,1280,720,'white')+box(0,0,581,720,N)+line(581,57,699)+line(581,239,699)+line(1155,0,1,720)+line(1221,0,1,720)+hatch(1155,57,66,182)+t(95,99,400,'MIRI COMPANY',18,'#99a3b9')+t(95,539,440,'감사합니다.',76,'white',700)
for i,(a,b) in enumerate([('주소','미리시 미리구 미리대로 7001번 길'),('대표 전화','031-000-0000'),('이메일','miricompany @ 0000.com'),('홈페이지','www.000000.com'),('상담 시간','월~금 09:00~18:00')]):y=442+i*39;s+=t(686,y,120,a,20,N,700)+t(805,y,365,b,20,GRAY)
S[30]=s
css='''@font-face{font-family:'Pretendard Variable';src:url('../../assets/fonts/artifacts/pretendard/PretendardVariable.woff2')}*{box-sizing:border-box}html,body{margin:0;width:1280px;height:720px;overflow:hidden}body{font-family:'Pretendard Variable',sans-serif;-webkit-font-smoothing:antialiased}.slide{width:1280px;height:720px;position:relative;overflow:hidden}'''
(R/'replica.css').write_text(css)
for n,s in S.items():
 (R/f'slide_{n:02d}.html').write_text(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>Crossrail replica {n:02d}</title><link rel="stylesheet" href="replica.css"></head><body><section class="slide">{s}</section></body></html>')
print('Generated',len(S),'replica pages')
