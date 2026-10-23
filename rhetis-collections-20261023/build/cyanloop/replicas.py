from pathlib import Path
import shutil,json
R=Path('/workspace/output/cyanloop-review'); D=Path('/workspace/work/deck/miricanvas_기업_selected/003_1la0o_하늘색_모던_교육_자료')
# All photographs are deliberately neutral seats; all diagrams remain editable HTML/SVG.
navy='#001134';cyan='#00a9ee';teal='#2bd4c8';blue='#0753d6';paper='#f5f5f5'
css='''*{box-sizing:border-box}html,body{margin:0;width:1280px;height:720px;overflow:hidden}body{font-family:'Pretendard Variable';font-size:18px;color:#111}.s{position:relative;width:1280px;height:720px;background:#f5f5f5;overflow:hidden}.t{position:absolute;margin:0;white-space:pre-line;line-height:1.5}.display{font-family:'Anton';font-weight:400;line-height:1.05;letter-spacing:-1px}.box{position:absolute;border-radius:10px}.circle{position:absolute;border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;color:white}.ph{background:#e4e5e7;color:#8b9097;display:flex;align-items:center;justify-content:center}.pill{position:absolute;border-radius:999px;display:flex;align-items:center;justify-content:center;text-align:center}.icon{width:52px;height:52px;display:block;margin:auto}.thin{font-family:'Oswald';font-weight:500}.center{text-align:center}table{border-collapse:collapse;width:100%;height:100%;table-layout:fixed}th,td{text-align:center;border:1px solid #eee;padding:14px;font-size:18px}th{height:70px;background:#0753d6;color:white;font-weight:700}td{background:white}td:first-child{background:#00a9ee;color:white;font-weight:700}svg{overflow:visible}.small{font-size:16px}'''
(R/'replica'/'replica.css').write_text(css)
shutil.copytree('/workspace/work/reference/fonts',R/'fonts',dirs_exist_ok=True)
with (R/'fonts'/'fonts.css').open('a') as f:f.write("\n@font-face{font-family:'Anton';src:url('Anton.ttf');font-weight:400}\n@font-face{font-family:'Oswald';src:url('Oswald.ttf');font-weight:200 700}\n")

def tx(x,y,text,size=18,color='#111',w=600,cl='',width=None):
 return f'<div class="t {cl}" style="left:{x}px;top:{y}px;font-size:{size}px;color:{color};font-weight:{w};'+(f'width:{width}px;' if width else '')+f'">{text}</div>'
def box(x,y,w,h,bg,content='',radius=10,extra=''):
 return f'<div class="box" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};border-radius:{radius}px;{extra}">{content}</div>'
def circle(x,y,d,bg,content='',extra=''):
 return f'<div class="circle" style="left:{x}px;top:{y}px;width:{d}px;height:{d}px;background:{bg};{extra}">{content}</div>'
def pill(x,y,w,h,bg,content,color='white',extra=''):
 return f'<div class="pill" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};color:{color};{extra}">{content}</div>'
def ph(x,y,w,h,n=1,radius=10):return box(x,y,w,h,'#e4e5e7',f'<div class="ph" style="width:100%;height:100%;border-radius:{radius}px">{n}</div>',radius)
def icon(kind='book',color='white',size=52):
 shapes={'book':'<path d="M10 7h24l8 8v34H10Z M34 7v10h8 M17 27h18 M17 34h18 M17 41h12"/>','chart':'<path d="M8 46V10h36 M14 38l10-12 9 6 12-15 M34 17h11v11"/>','users':'<circle cx="27" cy="14" r="6"/><circle cx="12" cy="30" r="5"/><circle cx="42" cy="30" r="5"/><path d="M18 29v-4q9-9 18 0v4 M4 47v-5q8-9 16 0v5 M34 47v-5q8-9 16 0v5"/>','check':'<path d="M15 10h25v38H10V10h5 M20 7h12v8H20Z M16 26l4 4 7-8 M30 27h6 M16 39l4 4 7-8 M30 40h6"/>','target':'<circle cx="27" cy="27" r="20"/><circle cx="27" cy="27" r="12"/><circle cx="27" cy="27" r="4"/><path d="M27 27L48 6 M38 6h10v10"/>','mail':'<path d="M6 20h42v29H6Z M6 22l21 16 21-16 M13 23V8h28v15 M18 14h18 M18 19h18"/>'}
 return f'<svg class="icon" width="{size}" height="{size}" viewBox="0 0 54 54" fill="none" stroke="{color}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">{shapes.get(kind,shapes["book"])}</svg>'
def line(x1,y1,x2,y2,color='#aaa',dash=False):return f'<svg style="position:absolute;left:0;top:0" width="1280" height="720"><line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1" '+('stroke-dasharray="2 3"' if dash else '')+'/></svg>'
def loop(x,y,d=340,color=teal,rot=0):
 # Open-ended annular stroke. A vector, not a screenshot.
 return f'<svg style="position:absolute;left:{x}px;top:{y}px;transform:rotate({rot}deg)" width="{d}" height="{d}" viewBox="0 0 400 400"><defs><linearGradient id="l{x}{y}"><stop stop-color="{navy}"/><stop offset="1" stop-color="{color}"/></linearGradient></defs><path d="M60 200a140 140 0 1 0 280 0" fill="none" stroke="url(#l{x}{y})" stroke-width="76"/><circle cx="340" cy="200" r="38" fill="{color}"/></svg>'

def logo(x,y):
 return f'<svg style="position:absolute;left:{x}px;top:{y}px" width="39" height="40" viewBox="0 0 40 40" fill="white"><circle cx="20" cy="7" r="6"/><circle cx="8" cy="19" r="6"/><circle cx="32" cy="19" r="6"/><circle cx="20" cy="31" r="6"/><path d="M8 19Q20 31 32 19L28 29 20 35 12 29Z"/></svg>'
def special(n):
 defs='<defs><linearGradient id="teal" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#00eee2"/><stop offset="1" stop-color="#001134"/></linearGradient><linearGradient id="reverse"><stop stop-color="#001134"/><stop offset="1" stop-color="#00eee2"/></linearGradient><linearGradient id="blue" gradientUnits="userSpaceOnUse" x1="0" y1="633" x2="1034" y2="633"><stop stop-color="#001134"/><stop offset="1" stop-color="#0753d6"/></linearGradient><linearGradient id="mix" x1="1" y1="0" x2="0" y2="1"><stop stop-color="#00a9ee"/><stop offset="1" stop-color="#0753d6"/></linearGradient><linearGradient id="vert" gradientUnits="userSpaceOnUse" x1="1192" y1="0" x2="1192" y2="461"><stop stop-color="#00bbb8"/><stop offset="1" stop-color="#001134"/></linearGradient></defs>'
 if n==1:
  paths='<path d="M1192 0V461" stroke="url(#vert)" stroke-width="81"/><path d="M857 461A167.5 167.5 0 0 1 1192 461" stroke="url(#teal)" stroke-width="83"/><circle cx="857" cy="461" r="41.5" fill="#00eee2"/><path d="M1192 461A172 172 0 0 1 1034 633" stroke="url(#mix)" stroke-width="83"/><circle cx="1192" cy="461" r="41.5" fill="#00a9ee"/><path d="M0 633H1034" stroke="url(#blue)" stroke-width="83"/><circle cx="1034" cy="633" r="41.5" fill="#0753d6"/>'
 elif n==2:
  defs+='<linearGradient id="bottom2" gradientUnits="userSpaceOnUse" x1="801" y1="0" x2="1065" y2="0"><stop stop-color="#001134"/><stop offset="1" stop-color="#00a9ee"/></linearGradient><linearGradient id="right2" gradientUnits="userSpaceOnUse" x1="1050" y1="0" x2="1370" y2="0"><stop stop-color="#0753d6"/><stop offset="1" stop-color="#001134"/></linearGradient>'
  paths='<path d="M801 247A139 139 0 1 1 1065 160" stroke="url(#teal)" stroke-width="70"/><path d="M1065 160A139 139 0 0 1 801 247" stroke="url(#bottom2)" stroke-width="70"/><circle cx="801" cy="247" r="35" fill="#00eee2"/><path d="M1065 160A139 139 0 1 1 1340 115A139 139 0 0 1 1065 160" stroke="url(#right2)" stroke-width="70"/><circle cx="1065" cy="160" r="35" fill="#0753d6"/>'

 elif n==3:
  defs+='<linearGradient id="blue3" gradientUnits="userSpaceOnUse" x1="95" y1="0" x2="375" y2="0"><stop stop-color="#0753d6"/><stop offset="1" stop-color="#001134"/></linearGradient>'
  paths='<path d="M655 123A160 160 0 0 1 882 278" stroke="url(#reverse)" stroke-width="78"/><circle cx="882" cy="278" r="39" fill="#00eee2"/><path d="M882 297A161 161 0 0 0 1204 297" stroke="url(#reverse)" stroke-width="78"/><circle cx="1204" cy="297" r="39" fill="#2bd4c8"/><path d="M95 480A140 140 0 0 0 375 480" stroke="url(#blue3)" stroke-width="78"/><circle cx="95" cy="480" r="39" fill="#0753d6"/><circle cx="882" cy="278" r="39" fill="#00eee2"/>'
 else:
  defs+='<linearGradient id="low18" gradientUnits="userSpaceOnUse" x1="1056" y1="260" x2="1211" y2="494"><stop stop-color="#001134"/><stop offset="1" stop-color="#00eee2"/></linearGradient><linearGradient id="blue18" gradientUnits="userSpaceOnUse" x1="985" y1="0" x2="1285" y2="0"><stop stop-color="#001134"/><stop offset="1" stop-color="#0753d6"/></linearGradient>'
  paths='<path d="M808 82A125 160 0 0 0 1058 82" stroke="url(#reverse)" stroke-width="78"/><circle cx="1058" cy="82" r="39" fill="#2bd4c8"/><path d="M1056 296C1018 410 1098 490 1211 494" stroke="url(#low18)" stroke-width="78"/><circle cx="1211" cy="494" r="39" fill="#00eee2"/><path d="M985 720A150 150 0 0 1 1285 720" stroke="url(#blue18)" stroke-width="80"/>'
 return '<svg style="position:absolute;left:0;top:0" width="1280" height="720" viewBox="0 0 1280 720" fill="none">'+defs+paths+'</svg>'

titles=['HRD Learning Solution','CONTENTS','EDUCATION PROPOSAL','Why Tranning Matters','Training Objectives','About Miri HRD','Why Miri HRD','Training Framework','Training Areas','Annual Learning Roadmap','Training Process','Onboarding Program','Leadership Program','Job Training Program','Instructor','Expected Outcome','Implementation Plan','Thank You!']
subs=['','','','왜 지금 직원 교육이 필요한가?','교육 목표 및 추진 방향','MIRI HRD 소개','미리HRD만의 차별화','계층별 교육 체계','교육 분야 소개','연간 교육 로드맵','교육 운영 프로세스','신입 교육','리더십 교육 프로그램','직무별 교육 과정','강사진 소개','기대 효과','실행 계획','']
types=['표지','목차','섹션 표지','막대+선 복합차트','목표 카드','회사소개','차별화 카드','교육체계 피라미드','허브','연간 로드맵','교육 프로세스 사이클','온보딩 허브','리더십 역량 허브','교육표','강사 프로필','성과 KPI','실행 간트','맺음말']
elements=['foundation cover','agenda,list','foundation cover,agenda','chart-bar,chart-line,legend,image-frame,prose','card,callout,hierarchy','prose,pill,image-frame','card,callout','pyramid,pill,callout','hub,pill','timeline,image-frame','cycle,prose','hub,pill,image-frame','hub,card','table','person,list','metric,card,list','roadmap','foundation cover,prose']
pages=[]
for n in range(1,19):
 s='';dark=n in (1,2,3,13,18)
 if n in (1,2,3,18): s=box(0,0,1280,720,navy,radius=0)
 if n not in (1,2,3,18):
  barbg=paper if n==13 else navy;barink=navy if n==13 else 'white'
  s+=box(0,0,1280,78,barbg,radius=0)+circle(65,39,12,barink)+tx(89,34,f'Chapter {n-3:02}',18,barink)+line(202,45,1207,45,'#798293')
  # Display titles retain their own width; subtitle starts after readable heading.
  sizes={k:60 for k in range(4,18)}
  s+=tx(59,126,titles[n-1],sizes[n],'white' if n==13 else navy,400,'display')
  subtitle_x={4:595,5:527,6:427,7:384,8:549,9:412,10:682,11:469,12:559,13:548,14:574,15:311,16:513,17:562}[n]
  s+=tx(subtitle_x,163,'| '+subs[n-1],16,'#999',600)
 if n==1:
  s+=tx(60,130,'HRD Learning',114,'#00eee2',400,'display')+tx(60,249,'Solution',114,'white',400,'display')
  s+=box(60,413,580,55,'transparent',radius=999,extra='background:linear-gradient(90deg,#0753d6,transparent)')+circle(60,413,55,blue)+tx(134,423,'직원 역량 강화 교육 프로그램 제안서',27,'white')
  s+=special(1)
  s+=logo(61,614)+tx(115,615,'MIRI HRD',30,'white',700)
 elif n==2:
  s+=special(2)
  s+=pill(83,96,430,54,navy,'직원 역량 강화 교육 프로그램 제안서','white','border:1px solid #b3bfce;font-size:25px;font-weight:700')+tx(83,177,'CONTENTS',132,'#00eee2',400,'display')+box(0,350,1280,370,paper,radius=0)
  heads=['교육 제안 배경','교육 체계','교육 과정','운영 및 성과'];lists=[['교육 목표','MIRI HRD 소개','미리HRD의 차별화'],['계층별 교육 체계','핵심 역량 모델','연간 교육 로드맵','교육 운영 프로세스'],['신입(Onboarding) 교육','직무 전문 교육','전문 강사진'],['기대 효과','실행 계획']]
  for i in range(4):
   x=83+i*288;s+=tx(x,430,f'{i+1:02}',60,navy,400,'display')+tx(x+69,459,heads[i],21,navy,700)+line(x,505,x+249,505,'#aaa',True)
   s+=tx(x,526,'\n'.join('•  '+v for v in lists[i]),20,'#111',400,'',257)
 elif n==3:
  s+=special(3)
  s+=tx(54,137,'01.',132,'#00eee2',400,'display')+tx(54,285,'EDUCATION PROPOSAL',98,'white',400,'display')
  s+=tx(721,553,'교육 제안 배경',25,'white',700)+line(894,554,894,641,'#8791a5')+tx(918,542,'•  교육 목표                ··········    01\n•  MIRI HRD 소개          ··········    02\n•  MIRI HRD의 차별화    ··········    03',20,'white',400)
 elif n==4:
  s+=tx(59,246,'급변하는 경영 환경에서 지속적인 역량 개발은\n기업 경쟁력 확보의 핵심입니다.',22,'#111',600)+tx(59,323,'교육 투자가 확대될수록 조직의 성과도 함께 성장합니다.\n지속적인 교육은 조직의 경쟁력을 높이는 장기적인 성장 전략입니다.',18,'#111',400)+ph(60,398,502,281)
  vals=[55,61,68,74,81];pts=[16,20,24,29,34]
  for k in range(6):
   y=662-k*83;s+=line(605,y,1190,y,'#ddd')+tx(1198,y-12,str(k*20),14,'#222',400)
  s+=circle(622,264,13,cyan)+tx(644,262,'기업 교육 투자 비중(%)',14,'#333',400)+circle(622,290,13,blue)+tx(644,288,'교육 도입 후 평균 조직 성과 향상(%)',14,'#333',400)
  for i,v in enumerate(vals):
   x=626+i*117;h=v*4.14;s+=box(x,662-h,77,h,cyan,radius=42,extra='border-bottom-left-radius:0;border-bottom-right-radius:0;background:linear-gradient(#00a9ee,#b9e4f5)')+tx(x+28,662-h-28,str(v),16,cyan,400)+tx(x+22,669,str(2080+i),14,'#111',400)
   y=662-pts[i]*4.14;s+=circle(x+32,y-6,12,blue)+tx(x+30,y-34,str(pts[i]),15,blue,400)
   if i: s+=line(x-85,662-pts[i-1]*4.14,x+38,y,blue)
 elif n==5:
  s+=pill(371,246,538,54,navy,'조직과 개인이 함께 성장하는 교육 체계를 구축합니다.','white','font-size:22px;font-weight:700')+line(640,308,640,357)+line(263,329,1017,329)+line(263,329,263,357)+line(1017,329,1017,357)
  cards=[('Goal 1','조직 경쟁력 강화','기업 비즈니스 방향과 연계된 전략적 교육을\n통해 실질적인 성과 향상을 도모합니다.\n교육이 단순히 학습에 머무르지 않고,\n조직의 경쟁력을 실질적으로 견인하는\n비즈니스 임팩트를 창출하도록 설계합니다.'),('Goal 2','직무 전문성 향상','•  현업 최적화 직무 스킬 강화\n\n•  실무 적용률을 높이는 문제 해결 훈련\n\n•  직무별 핵심 역량 모델링 구축'),('Goal 3','미래 인재 육성','신입부터 리더까지, 개인의 성장이 조직의\n미래가 되는 맞춤형 로드맵을 운영합니다.')]
  for i,(a,b,c) in enumerate(cards):
   x=81+i*379;s+=box(x,357,362,306,[cyan,blue,'#e4e5e7'][i])+tx(x,389,a,18,'white' if i<2 else navy,400,'center',362)+tx(x,432,b,22,'white' if i<2 else navy,700,'center',362)+tx(x+27,495 if i<2 else 568,c,18,'white' if i<2 else navy,400,'center',310)
 elif n==6:
  s+=tx(59,232,'기업과 사람의 성장을 만드는 교육 파트너, MIRI HRD는 산업별 맞춤형 교육과\n체계적인 운영 시스템으로 기업의 지속 가능한 성장을 지원합니다.',18,'#111',400)
  s+=pill(59,316,323,43,navy,'기업과 함께 성장하는 교육 전문기관','white','font-size:21px;font-weight:700')+tx(59,380,'MIRI HRD는 다양한 산업 분야의 기업 교육 경험을 바탕으로 조직의 목표와 직무에\n맞는 맞춤형 교육 프로그램을 제공합니다. 교육 기획부터 운영, 성과 분석까지\n전 과정을 체계적으로 지원하며, 기업의 인재 경쟁력 향상에 기여하고 있습니다.',18,'#111',400)
  for i,word in enumerate(['Professional','Practical','Partnership']):
   x=65+i*205;s+=circle(x,490,180,[cyan,teal,cyan][i],f'<div style="display:grid;justify-items:center;gap:15px">{icon(["book","chart","users"][i])}<b>{word}</b></div>')
  s+=f'<svg style="position:absolute;left:674px;top:116px" width="552" height="556"><path d="M278 0 A278 278 0 0 0 278 556" fill="none" stroke="{teal}" stroke-width="20"/></svg>'+ph(694,134,522,522,1,999)+circle(1028,573,102,cyan,'',extra='background:transparent;border:24px solid #64c9ec')+circle(1159,571,42,'#00eee2')
 elif n==7:
  names=['맞춤형 교육 설계','실무 중심 커리큘럼','전문 강사진','교육 성과 관리'];notes=['기업의 업종과 조직 문화, 교육 목표를 분석하여\n최적의 커리큘럼을 설계합니다.','현업 사례와 프로젝트 기반 학습으로 교육 내용을\n실제 업무에 바로 적용할 수 있습니다.','풍부한 실무 경험과 교육 노하우를 갖춘 전문 강사진이\n교육을 진행합니다.','교육 만족도 조사와 성과 분석을 통해 지속적인 교육\n개선과 효과를 지원합니다.']
  for i in range(4):
   x=59+(i%2)*584;y=225+(i//2)*195;s+=box(x,y,572,181,'white')+circle(x+37,y+22,138,[cyan,teal,teal,cyan][i],icon(['check','chart','users','target'][i]))+tx(x+199,y+28,f'Keyword {i+1}',16,'#999',400)+tx(x+199,y+63,names[i],22,'#111',700)+tx(x+199,y+104,notes[i],18,'#111',400)
  s+=pill(65,613,1152,70,navy,'미리HRD는 기업의 목표와 구성원의 성장을 연결하는 맞춤형 교육 솔루션을 제안합니다.','white','font-size:24px;font-weight:700')
 elif n==8:
  s+=tx(65,228,'신입부터 관리자, 리더까지 각 계층에서\n요구되는 핵심 역량을 중심으로\n단계별 교육 과정을 제공합니다.',20,'#111',400)
  rows=[(408,238,318,'Executive','임원리더십','조직 전략 수립 · 의사결정 · 조직문화 구축','white'),(298,333,428,'Manager','관리자 리더십','성과관리 · 코칭 및 피드백 · 팀 운영 · 문제 해결',teal),(210,424,516,'Staff','실무 역량','직무 전문성 · 커뮤니케이션 · 업무 개선',cyan),(124,515,602,'New Employee','신입 온보딩','조직 적응 · 업무 기본기 · 기업문화 이해 · 비즈니스 매너',blue)]
  for x,y,w,a,b,c,col in rows:
   s+=pill(x,y,w,77,col,f'<b style="position:absolute;left:46px;font-size:22px">{a}</b><span style="position:absolute;right:29px">{b}</span>','#111' if col=='white' else 'white')+tx(746,y+27,c,19,'#111',400)+line(746,y+85,1140,y+85,'#ccc',True)
  s+=pill(65,613,1152,70,navy,'미리HRD는 단계별 성장에 맞춘 교육으로 개인의 역량을 조직의 성과로 연결합니다.','white','font-size:24px;font-weight:700')
 elif n==9:
  s+=tx(728,163,'기업의 목표와 직무에 맞춰 다양한 교육 분야를 맞춤형으로 제공합니다.',18,'#111',400)
  names=['리더십 교육','커뮤니케이션','디지털 역량','직무 전문 교육','조직문화','문제 해결'];eng=['Leadership','Communication','Digital Skills','Job Skills','Organization','Problem Solving'];notes=['리더의 역할과 성과 관리\n의사결정 및 팀 운영 역량 강화','효과적인 소통과 협업을 통해\n원활한 업무 환경을 구축','AI · 데이터 활용 등 변화하는\n업무 환경에 필요한 역량 개발','직무별 역량과 전문성을 높여\n업무 효율과 성과 향상을 지원','기업의 핵심 가치와 비전공유\n긍정적인 조직문화 조성','분석력과 창의적 문제 해결\n능력을 향상']
  for i in range(6):
   x=62 if i<3 else 788;y=253+(i%3)*136;s+=line(x+215,y+58,640,447,'#888',True)+pill(x,y,430,116,cyan if i%2==0 else blue,f'<div style="position:absolute;left:45px;text-align:left"><b style="font-size:21px">{names[i]}</b><p style="font-size:15px;margin:3px 0">| {eng[i]}</p></div><div style="position:absolute;left:192px;text-align:left;font-size:17px;line-height:1.5">{notes[i].replace(chr(10),"<br>")}</div>')
  s+=circle(509,317,262,navy,'<div style="color:white"><div class="display" style="font-size:36px">Miri HRD</div><p style="font-size:19px;line-height:1.4">기업의 목표와 특성에 맞춰<br>다양한 교육 분야를<br>맞춤형으로 제공합니다.</p></div>')
 elif n==10:
  names=['조직 적응','직무 역량 강화','리더십 강화','성과 공유'];notes=['신입 온보딩 · 기업문화\n비즈니스 매너','직무 전문교육\n업무 프로세스','성과관리\n조직관리','우수사례 발표 · 성과 리뷰\n차년도 계획']
  for i in range(4):
   x=65+i*280;col=[teal,cyan,blue,navy][i];s+=circle(x+60,424,249,col,f'<div><b style="font-size:23px">{i+1}Q</b><h3 style="font-size:23px;margin:14px 0">{names[i]}</h3><div style="font-size:18px;line-height:1.4">{notes[i].replace(chr(10),"<br>")}</div></div>',extra='color:white')+circle(x,246,247,col)+ph(x+5,251,237,237,i+1,999)
   if i<3:s+=tx(x+315,528,'›',42,cyan,400)
 elif n==11:
  s+=tx(796,161,'교육 설계부터 성과 분석까지 체계적으로 운영합니다.\n전 과정을 체계적으로 관리하여 교육 효과를 극대화합니다.',18,'#111',400,'',420)
  # Organic process drawn from overlapping discs and a central cutout, editable vector.
  s+=f'<svg style="position:absolute;left:393px;top:243px" width="450" height="447" viewBox="0 0 450 447"><defs><linearGradient id="process"><stop stop-color="#00a9ee"/><stop offset=".45" stop-color="#0753d6"/><stop offset=".75" stop-color="#001134"/></linearGradient></defs><path d="M121 3C187-4 199 79 273 67C330 58 396 35 433 98C478 175 400 211 423 278C458 367 419 443 330 443C249 442 226 361 263 287C292 227 242 189 188 199C122 215 115 254 150 292C178 327 165 358 126 355C91 353 58 330 84 290C109 246 42 257 20 218C-13 150 52 125 75 98C101 71 66 22 121 3Z" fill="url(#process)"/><circle cx="213" cy="215" r="100" fill="{paper}"/></svg>'
  circles=[(505,257,112,blue,'users'),(417,400,88,cyan,'check'),(477,519,66,cyan,'book'),(690,302,139,navy,'target'),(660,516,160,navy,'check')]
  for x,y,d,col,k in circles:s+=circle(x-10,y-10,d+20,col)+circle(x,y,d,'white',icon(k,col))
  s+=tx(549,437,'Miri HRD',41,navy,400,'display')
  left=[(339,279,'Step 3.  교육 운영','온·오프라인 교육 진행 학습 참여 관리'),(247,408,'Step 2.  교육 설계','맞춤형 커리큘럼 구성 교육 일정 및 방식 설계'),(243,533,'Step 1.  교육 니즈 분석','조직 및 직무 요구사항 분석 현황 진단 및 요구 조사\n직무 요구사항 분석 현황 진단 및 요구 조사')]
  for x,y,a,b in left:s+=tx(x,y,a,20,'#111',700)+tx(59,y+37,b,18,'#111',400,'',410)
  s+=tx(869,279,'Step 4.  성과 평가',20,'#111',700)+tx(869,317,'만족도 및 학습 성취도 평가를 통해 교육 참여자의\n전반적인 교육 경험과 이해도를 확인하고,\n교육 전·후 역량 향상 결과를 분석하여 실질적인\n성장 효과를 검증\n이를 바탕으로 교육 효과를 종합적으로 측정하고,\n향후 교육 과정 및 콘텐츠 개선에 반영',18,'#111',400)+tx(869,531,'Step 5.  사후 관리',20,'#111',700)+tx(869,568,'교육 결과와 참여자 피드백을 바탕으로 개선안을\n도출하고 이를 반영하여 교육 품질을 높일 수 있는\n차기 교육 계획을 수립합니다.',18,'#111',400)
 elif n==12:
  s+=tx(859,164,'빠른 조직 적응과 안정적인 업무 시작을 지원합니다.',18,'#111',400)+ph(70,224,460,460,1,999)+circle(152,306,299,navy,f'<div style="color:white">{icon("target")}<h3>교육 목표</h3><p style="line-height:1.4">기업문화와 업무 기본기를<br>이해하고 조직에 빠르게<br>적응할 수 있도록 지원</p></div>')
  names=['기업문화 이해','비즈니스 기본기','커뮤니케이션','실무 적응'];notes=['기업 비전 · 조직문화','업무 프로세스 · 문서 작성 · 비즈니스 매너','협업 · 피드백','직무 이해 · 업무 실습 · 사례 학습']
  for i in range(4):
   x=539 if i in(0,3) else 577;y=250+i*106;s+=line(440,454,x,y+43,'#888',True)+pill(x,y,633,89,[cyan,blue,teal,cyan][i],f'<div style="position:absolute;left:36px"><span style="font-size:15px">Module {i+1}. </span><b style="font-size:22px">{names[i]}</b></div><div style="position:absolute;left:257px;font-size:17px">{notes[i]}</div><div style="position:absolute;right:40px">{icon(["book","mail","check","chart"][i])}</div>')
 elif n==13:
  s=box(0,78,1280,642,navy,radius=0)+s
  s+=tx(846,163,'효과적인 리더는 다양한 역량의 균형 있는 성장을 통해\n조직과 구성원의 성과를 이끌어냅니다.',18,'white',400)
  names=['전략적 사고','성과관리','코칭 & 피드백','커뮤니케이션','변화관리','문제 해결'];notes=['조직 목표를 이해하고\n장기적인 방향을\n설정하는 역량','목표 수립과 성과 점검으로\n지속적인 개선을\n이끄는 역량','구성원의 성장을 지원하고\n동기를 부여하는\n코칭 및 피드백 역량','신뢰를 기반으로\n원활하게 소통하고\n협업을 이끄는 역량','환경에 유연하게 대응하고\n조직의 변화를\n주도하는 역량','상황 분석과 합리적인\n의사결정을 통해\n문제를 해결하는 역량'];coords=[(78,496),(222,325),(423,228),(657,228),(858,325),(1002,496)]
  for i,(x,y) in enumerate(coords):
   s+=line(x+106,y+106,640,720,'#bbb',True)+circle(x,y,212,[cyan,blue,teal,blue,cyan,teal][i],f'<div style="color:white"><b style="font-size:21px">{names[i]}</b><p style="font-size:17px;line-height:1.4">{notes[i].replace(chr(10),"<br>")}</p></div>')
  s+=circle(364,469,552,'#bbb')+circle(374,479,532,'white', '<div style="color:#111;margin-top:-260px"><p style="font-size:16px">Effective Leadership</p><h3 style="font-size:22px">조직의 성과를 이끄는 핵심 리더 역량</h3><p style="font-size:19px;line-height:1.4">대상과 조직에 맞춰 핵심 역량을 중심으로<br>맞춤형 리더십 교육 프로그램을 설계합니다.</p></div>')
 elif n==14:
  s+=tx(795,164,'직무 특성에 맞춘 맞춤형 교육으로 실무 경쟁력을 강화합니다.',18,'#111',400)
  rows=[['영업 역량 강화','영업 담당자','고객 상담, 협상 전략, 제안 스킬','8H','집합교육'],['마케팅 실무','마케팅 담당자','콘텐츠 기획, 데이터 분석, 디지털 마케팅','8H','집합 + 온라인'],['기획·전략','기획 담당자','전략 수립, 문제 해결, 보고서 작성','8H','워크숍'],['생산·품질','생산·품질 담당자','품질관리, 공정 개선, 생산성 향상','6H','집합교육'],['고객 서비스','CS 담당자','고객 응대, 컴플레인 대응, 서비스 품질','6H','실습 중심']]
  table='<table><colgroup><col style="width:20%"><col style="width:15%"><col style="width:34%"><col style="width:11%"><col style="width:20%"></colgroup><thead><tr>'+''.join('<th>'+a+'</th>' for a in ['교육 과정','교육 대상','주요 교육 내용','교육 시간','교육 방식'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+v+'</td>' for v in r)+'</tr>' for r in rows)+'</tbody></table>'
  s+=box(61,245,1158,423,'transparent',table,radius=0)
 elif n==15:
  s+=tx(1029,137,'* 페이지 내 인물 사진은 샘플 이미지입니다.',12,'#999',400)+tx(846,163,'교육은 개인의 성장을 넘어 조직의 성과로 이어집니다.',18,'#111',400)
  names=['김미리','박미리','이미리'];roles=['책임교수','수석강사','전문강사'];notes=['HR 컨설팅 경력 15년\n리더십 교육 350회+\n대기업·공공기관 교육 운영','조직 커뮤니케이션 전문\n기업 교육 500회+','현업 실무 경력 12년\n리더십 교육 200회+\n직무교육 전문\n프로젝트 기반 교육 운영'];eng=['LEADERSHIP EXPERT','BUSINESS COMMUNICATION','JOB SKILL TRAINER']
  for i in range(3):
   x=55+i*394;s+=box(x,328,382,392,[cyan,blue,navy][i],radius=190,extra='border-bottom-left-radius:0;border-bottom-right-radius:0')+ph(x+188,214,195,506,i+1,0).replace('background:#e4e5e7;', 'background:#e4e5e7;clip-path:polygon(40% 0,65% 0,72% 4%,75% 10%,70% 16%,92% 20%,100% 32%,93% 53%,78% 57%,80% 100%,60% 100%,55% 58%,4% 55%,0 36%,12% 21%,37% 16%,30% 10%,32% 4%);')+tx(x+30,481,names[i],25,'white',700)+tx(x+110,487,'| '+roles[i],16,'#cfe7ef',400)+tx(x+30,527,'\n'.join('•  '+a for a in notes[i].split('\n')),17,'white',400)+tx(x+30,668,eng[i],22,'#a6d6ea',500,'display thin')
 elif n==16:
  s+=tx(64,231,'교육은 개인의 성장을 넘어 조직의 성과로 이어집니다.',18,'#111',400)+tx(60,487,'사내 교육 참여자',21,'#111',700)+tx(214,383,'1,500+',130,cyan,500,'display thin')+line(60,540,514,540,'#aaa',True)+tx(65,558,'기대효과',23,'#111',700)+tx(156,561,'•  업무 생산성 향상\n•  조직 커뮤니케이션 강화\n•  직무 전문성 향상',18,'#111',400)+tx(337,561,'•  조직 몰입도 향상\n•  리더십 역량 강화\n•  키워드를 입력해주세요.',18,'#111',400)
  names=['교육 만족도','교육 수료율','업무 적용률','교육 추천 의향','연간 학습 운영','키워드 입력'];figs=['4.8 / 5.0','97%','89%','95%','120H','00%']
  for i in range(6):
   x=530+(i%2)*350;y=241+(i//2)*149;s+=box(x,y,336,136,'white')+tx(x+27,y+20,f'Keyword {i+1}',16,'#999',400)+tx(x+27,y+50,names[i],22,'#111',700)+tx(x+198,y+77,figs[i],48,blue,500,'display thin')
 elif n==17:
  s+=tx(850,164,'교육 도입부터 성과 분석까지 체계적으로 지원합니다.',18,'#111',400)
  x0=277;y0=226;cw=93.8;rh=74
  for i in range(10):s+=box(x0+i*cw,y0,cw,74,navy,radius=0)+tx(x0+i*cw+33,y0+26,f'W{i+1}',20,'white',700)
  names=['교육 요구 분석','교육 설계','콘텐츠 개발','교육 운영','성과 분석'];ranges=[(0,2),(1,3),(2,5),(5,10),(9,10)];labs=['조직 분석 및\n교육 니즈 조사','과정 설계 및 일정 협의','교안 및 실습 자료 제작','과정 운영 및 학습 관리','만족도 조사\n결과 분석']
  for i in range(5):
   y=300+i*74;s+=line(59,y,1216,y,'#ccc')+tx(118,y+25,names[i],21,'#111',700)
   for j in range(11):s+=line(x0+j*cw,y,x0+j*cw,y+74,'#ddd',True)
   a,b=ranges[i];s+=box(x0+a*cw,y,(b-a)*cw,74,cyan if i%2==0 else blue,radius=0)+tx(x0+a*cw,y+22 if i not in(0,4) else y+11,labs[i],18,'white',400,'center',(b-a)*cw)
  s+=line(59,670,1216,670,'#888')
 elif n==18:
  s+=special(18)
  s+=pill(74,153,548,58,navy,'함께 성장하는 조직을 위한 최고의 교육 파트너','white','border:1px solid #8993a6;font-size:27px;font-weight:700')+tx(84,226,'Thank You!',145,'#00eee2',400,'display')+tx(85,396,'미리교육은 기업의 성장 단계와 교육 목표에 맞춘\n최적의 교육 솔루션을 제안합니다.',22,'white',400)+tx(85,544,'Contact.',25,'white',700)+tx(202,546,'Address. 미리시 미리구 미리로 000\nTel.  00-0000-0000\nE-mail. kimmiri@miridih.com\nWeb.  www.miriedu.co.kr',18,'white',400)+logo(1027,620)+tx(1073,624,'MIRI HRD',25,'white',700)
 pages.append(s)
 (R/'replica'/f'slide_{n:02}.html').write_text(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><link rel="stylesheet" href="../fonts/fonts.css"><link rel="stylesheet" href="replica.css"><title>{n:02} {titles[n-1]}</title></head><body><section class="s">{s}</section></body></html>')
(R/'inventory.md').write_text('# cyanloop 원본 이미지 목록\n\n| 이미지 | 크기 | 페이지 유형 | 계약 대응 |\n|---|---|---|---|\n'+'\n'.join(f'| slide_{i+1:02}.png | 1280×720 | {types[i]} | {elements[i]} |' for i in range(18)))
Path('/workspace/work/cyanloop/pages.json').write_text(json.dumps({'titles':titles,'subs':subs,'types':types,'elements':elements},ensure_ascii=False))
print('replica 18 built')
