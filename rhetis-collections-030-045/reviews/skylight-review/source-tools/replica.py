from pathlib import Path
from html import escape
import shutil,json
ROOT=Path('/workspace/work/deliverables/skylight-review'); SRC=Path('/workspace/work/deck/miricanvas_기업_selected/038_1jp12_파랑_모던_업무환경_개선안_보고서')
shutil.copytree('/workspace/work/reference/fonts',ROOT/'fonts',dirs_exist_ok=True)
R=ROOT/'replica'; R.mkdir(exist_ok=True)
NAVY='#2c4b69'; BLUE='#58a4ee'; PALE='#e9f5fd'; GRAY='#f6f6f6'
def box(x,y,w,h,bg='',rad=0,extra='',content=''):
 if 'display:flex' in extra:content='<span>'+content+'</span>'
 return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;'+(f'background:{bg};' if bg else '')+f'border-radius:{rad}px;{extra}">{content}</div>'
def text(x,y,w,s,size=18,weight=400,color=NAVY,align='left',line=1.4,extra=''):
 if 13<=size<=19:size-=1
 if size>=20:extra+="font-family:'Noto Sans KR';"
 return box(x,y,w,'auto',extra=f'font-size:{size}px;font-weight:{weight};color:{color};text-align:{align};line-height:{line};{extra}',content=s).replace('height:autopx','height:auto')
def para(s):return escape(s).replace('\n','<br>')
def ph(x,y,w,h,n):return box(x,y,w,h,'#e6e8eb',6,content=f'<span style="display:none">사진 자리 {n}</span>')
def label(x,y,s,w=None):return box(x,y,w or len(s)*14+24,27,BLUE,2,'display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:700;color:white;',s)
def arrow(x,y,w=32,h=32,color=BLUE,d='r'):
 p='M6 16h20m-8-8 8 8-8 8' if d=='r' else 'M16 6v20m-8-8 8 8 8-8'
 return box(x,y,w,h,content=f'<svg viewBox="0 0 32 32" width="100%" height="100%"><circle cx="16" cy="16" r="15" fill="{color}"/><path d="{p}" stroke="white" fill="none" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>')
def hugearrow(x,y,w,h,d='r'):
 points='0,0 72,30 72,0 100,50 72,100 72,70 0,100' if d=='r' else '0,0 100,0 73,63 88,63 50,100 12,63 27,63'
 return box(x,y,w,h,content=f'<svg viewBox="0 0 100 100" preserveAspectRatio="none" width="100%" height="100%"><defs><linearGradient id="ar"><stop stop-color="#f7f3ff"/><stop offset="100%" stop-color="#64cde8"/></linearGradient></defs><polygon points="{points}" fill="url(#ar)"/></svg>')
def line(x,y,w,h=1,color='#bcc6ce',dotted=False):return box(x,y,w,h,extra=f'border-top:{2 if dotted else 1}px {"dotted" if dotted else "solid"} {color};')
def bullets(x,y,w,items,size=18,gap=32,color=NAVY):
 return ''.join(text(x,y+i*gap,w,'• &nbsp;'+para(s),size,color=color) for i,s in enumerate(items))
def banner(x,y,w,h,title,bg=NAVY,font=20):return box(x,y,w,h,bg,7,f'display:flex;align-items:center;justify-content:center;font-weight:700;font-size:{font}px;color:white;line-height:1.4;',title)
def circle(x,y,d,bg,content,sz=20,color=NAVY):return box(x,y,d,d,bg,d/2,f'display:flex;align-items:center;justify-content:center;text-align:center;font-size:{sz}px;font-weight:700;line-height:1.4;color:{color};',content)
def table(x,y,w,h,heads,rows,widths=None):
 widths=widths or [1/len(heads)]*len(heads)
 tx='<table><thead><tr>'+''.join('<th>'+v+'</th>' for v in heads)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+v+'</td>' for v in r)+'</tr>' for r in rows)+'</tbody></table>'
 return box(x,y,w,h,extra='font-size:16px;',content=tx)
def svgchart(x,y,w,h,vals,labels,maxv=None,kind='bar',colors=None,pct=False):
 maxv=maxv or max(vals)*1.05; left=38;top=24;bot=30;pw=w-left-12;ph=h-top-bot;n=len(vals);step=pw/n
 out=f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="overflow:visible">'
 steps=3 if maxv==15 else 5 if maxv==50 else 4
 for i in range(steps+1):
  yy=top+ph*i/steps;v=maxv*(steps-i)/steps;out+=f'<line x1="{left}" x2="{w-12}" y1="{yy}" y2="{yy}" stroke="#d0d0d0"/><text x="{left-7}" y="{yy+4}" text-anchor="end" fill="#8c8774" font-size="13">{v:.0f}{"%" if pct else ""}</text>'
 pts=[]
 for i,(v,lab) in enumerate(zip(vals,labels)):
  xx=left+step*(i+.5);yy=top+ph*(1-v/maxv);pts.append((xx,yy));c=(colors or [NAVY]*n)[i]
  if kind in ('bar','both'):out+=f'<rect x="{xx-step*.33}" y="{yy}" width="{step*.66}" height="{top+ph-yy}" fill="{c}"/>'
  out+=f'<text x="{xx}" y="{yy-8}" text-anchor="middle" fill="{NAVY}" font-size="14">{v:,}{"%" if pct else ""}</text><text x="{xx}" y="{h-10}" text-anchor="middle" fill="#8c8774" font-size="13">{lab}</text>'
 if kind in ('line','both'):
  out+=f'<polyline points="'+ ' '.join(f'{a},{b}' for a,b in pts)+f'" fill="none" stroke="{BLUE if kind=="both" else NAVY}" stroke-width="{2 if kind=="both" else 1}"/>'
  out+=''.join(f'<circle cx="{a}" cy="{b}" r="3.2" fill="{BLUE if kind=="both" else NAVY}"/>' for a,b in pts)
 return box(x,y,w,h,content=out+'</svg>')
def corners(mode='standard'):
 if mode=='cover':
  return box(736,0,174,174,'linear-gradient(45deg,white,#edf8fc)',extra='clip-path:polygon(0 0,100% 0,100% 100%);')+box(910,0,192,174,'linear-gradient(38deg,white,#79baf4)')+box(1102,174,178,190,'linear-gradient(45deg,white,#81bdf2)')+box(910,174,192,380,'linear-gradient(125deg,#e4f5fc,#74b4f3)',extra='clip-path:polygon(100% 0,100% 50%,0 100%,0 50%);')+box(910,364,370,190,'linear-gradient(45deg,#bbdef7,white 78%)',extra='clip-path:polygon(50% 0,100% 0,50% 100%,0 100%);')+box(719,364,155,154,'linear-gradient(40deg,#c5effa,white)')+box(719,554,191,166,'linear-gradient(45deg,white,#83bdf3)')+box(1102,554,178,166,'linear-gradient(45deg,#d1f3fc,white)')+box(552,554,167,166,'linear-gradient(45deg,#d1e9fa,white)',extra='clip-path:polygon(100% 0,100% 100%,0 100%);')+box(54,624,665,65,'#f7f7f7',2)
 if mode=='closing':
  return box(1082,0,198,198,'linear-gradient(45deg,white,#98c8f2)',extra='clip-path:polygon(0 0,100% 0,100% 100%);')+box(0,270,44,280,'linear-gradient(white,#96c8f5)')+box(0,550,324,170,'linear-gradient(35deg,#86bff2,#dff3ff)',extra='clip-path:polygon(0 0,14% 0,100% 100%,0 100%);')+box(44,406,280,314,'linear-gradient(35deg,#b9def8,white 78%)',extra='clip-path:polygon(0 46%,51% 0,100% 46%,100% 100%);')+box(324,550,956,170,'linear-gradient(20deg,#c6f2fb,#eaf9ff)')
 if mode=='chapter':
  return box(0,0,234,158,'linear-gradient(35deg,#d0f4fc,white)')+box(1036,0,244,48,'linear-gradient(30deg,#96c6f4,white)')+box(1116,48,164,240,'linear-gradient(135deg,white,#bcdef9)',extra='clip-path:polygon(0 0,100% 0,100% 100%);')+box(0,270,44,280,'linear-gradient(white,#96c8f5)')+box(0,550,324,170,'linear-gradient(35deg,#86bff2,#dfF3ff)',extra='clip-path:polygon(0 0,14% 0,100% 100%,0 100%);')+box(44,406,280,314,'linear-gradient(35deg,#b9def8,white 78%)',extra='clip-path:polygon(0 46%,51% 0,100% 46%,100% 100%);')+box(324,550,956,170,'linear-gradient(20deg,#c6f2fb,#eaf9ff)')
 return box(0,0,1280,65,'linear-gradient(90deg,#eff0f1,#e8f5ff)')+box(0,0,48,48,'linear-gradient(45deg,white,#97c7ef)',extra='clip-path:polygon(0 0,100% 0,0 100%);')+box(0,0,112,65,'linear-gradient(45deg,#d3e9f9,white)',extra='clip-path:polygon(43% 0,100% 0,43% 100%,0 100%,0 74%);')+box(1027,0,192,129,'linear-gradient(#b8daf6,white)',extra='clip-path:polygon(0 0,66% 0,100% 50%,100% 100%,33% 100%,0 50%);')+box(1219,0,61,257,'linear-gradient(#95c7f3,white)')
def shell(i,kicker='',title='',lead='',content='',mode='standard'):
 bg=corners(mode);s=bg
 if mode=='standard':
  s+=text(66,36,300,'MIRICOMPANY',15,800)+text(1049,37,190,'PROPOSAL BACKGROUND',14,500)
  s+=label(66,88,kicker)+text(66,126,1150,title,40,600,extra='letter-spacing:-1.6px;')
  if lead:s+=text(66,189,1150,lead,21)
  s+=box(66,630,1142,44,'#f8f8f8',2)+text(87,642,300,'미리컴퍼니 경영지원팀',13)+text(500,642,280,'www.miricompany.com',13,align='center')+text(1105,642,83,'2080.03',13,align='right')
 elif mode in ('cover','chapter'):
  s+=text(86,645,200,'MIRICOMPANY',15,800)+text(204,645,530,'이곳에 업무환경 개선안에 관한 간단한 설명을 입력해 보세요.',14)+text(768,647,200,'www.miricompany.com',12)+text(976,647,170,'미리컴퍼니 경영지원팀',12)+text(1165,647,60,'2080.03',12)
 if i==21:s=bg
 s+=content
 css='''*{box-sizing:border-box}html,body{margin:0;width:1280px;height:720px;overflow:hidden}body{font-family:'Pretendard Variable';color:#2c4b69;background:white}.slide{width:1280px;height:720px;position:relative;overflow:hidden}.bg{position:absolute;inset:0;width:1280px;height:720px}table{border-collapse:collapse;width:100%;height:100%;text-align:center}th{font-weight:700;background:#edf6fd;padding:10px}td{border-bottom:1px solid #eee;padding:10px;color:#777;background:#f8f8fb}p{margin:0}svg{display:block}svg text{font-family:'Pretendard Variable'}'''
 return f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>Skylight replica {i:02d}</title><link rel="stylesheet" href="../fonts/fonts.css"><style>{css}</style></head><body><section class="slide">{s}</section></body></html>'
P={}
P[1]=shell(1,mode='cover',content=text(80,103,400,'Workplace<br>Improvement Plan',21,color='#bbb',line=1.08)+text(77,153,670,'바로 통과되는',80,400,color='#626262',extra='letter-spacing:-4px;')+text(77,249,700,'업무환경 개선안',80,700,color=BLUE,extra='letter-spacing:-4px;'))
cs='';names=['추진 배경 및<br>현황 분석','문제점 도출 및<br>개선 목표','개선 방안','타사 사례 및<br>기대효과','추진 일정 및<br>예산 계획'];bgs=['linear-gradient(#65b7fa,#e7f4fd 72%)','linear-gradient(#c1f0fb,#e7f4fd 72%)','linear-gradient(#f1f1f1,#e7f4fd 72%)']
for i,n in enumerate(names):
 x=66+i*233;cs+=box(x,206,212,392,bgs[i%3],1)+text(x,250,212,f'0{i+1}',28,800,align='center')+text(x+12,294,188,n,21,700,align='center')+line(x+21,441,170)+text(x+20,481,172,'해당 목차에 대한 간략한<br>내용을 입력해주세요.',17,align='center',line=1.7)
P[2]=shell(2,'CONTENTS','목차를 입력하세요',content=cs)
P[3]=shell(3,mode='chapter',content=box(563,225,154,40,BLUE,5,'display:flex;align-items:center;justify-content:center;color:white;font-size:20px;font-weight:700;','CHAPTER 01.')+text(150,274,980,'추진 배경 및 현황 분석',72,700,align='center',extra='letter-spacing:-3px;')+text(240,390,800,'해당 항목의 핵심 내용을 입력해 보세요. 구체적인 실행 방법이나 목표를 포함해 보세요.',20,color='#888',align='center'))
cs=box(66,210,154,390,'linear-gradient(#66b8fa,#e8f5fd)',8,'display:flex;align-items:center;justify-content:center;text-align:center;font-size:21px;font-weight:700;line-height:1.4;','제안<br>내용<br>요약')+line(238,413,29)+box(276,257,56,312,extra='border:2px solid #e6e6e6;border-right:0;border-radius:23px 0 0 23px;')
for j,n in enumerate(['현황','개선 방안','기대 효과']):
 y=210+137*j;cs+=box(339,y,868,116,'linear-gradient(90deg,#f0f0f0,#e8f5fd)',9)+banner(359,y+17,145,82,n,'#627f96')+bullets(551,y+29,630,['해당 항목의 핵심 내용을 입력해 보세요.','구체적인 실행 방법이나 목표를 포함해 보세요.'],18)
P[4]=shell(4,'제안 배경','해당 제안을 추진하게 된 배경과 제안의 필요성을 입력해 보세요.',content=cs)
cs=box(69,240,473,278,'linear-gradient(#eaeaea,#f2f2f2)',10)+text(87,268,110,'연도별<br>업무 환경<br>개선 투자액',19,700)+svgchart(188,255,333,254,[1900,1700,1500,1300,1200],['2075','2076','2077','2078','2090'],2000)+box(555,240,415,278,'linear-gradient(#eaeaea,#f2f2f2)',5)+text(575,267,110,'변화 추이<br>그래프',19,700)+svgchart(656,255,308,254,[15,12,8,6,3],['2075','2076','2077','2078','2079'],15,'line',pct=True)+box(984,240,222,278,'linear-gradient(#eaeaea,#f2f2f2)',5)+text(1002,268,100,'핵심<br>키워드',19,700)
for j,c in enumerate(['#a7b3be','#8094a7','#506f89']):cs+=box(1065,269+68*j,121,50,c,25,'display:flex;align-items:center;justify-content:center;color:white;font-weight:700;font-size:17px;','#핵심 키워드')
cs+=box(316,537,636,68,'linear-gradient(90deg,#008ff3,#66b8fa)',36,'display:flex;align-items:center;justify-content:center;color:white;font-size:22px;font-weight:700;','임직원 생산성 향상과 조직 경쟁력 확보를 위한 선제적 투자 시점')+arrow(616,500,48,48,d='d')
P[5]=shell(5,'추진 배경','2060년 이후 업무 환경 개선 투자가 감소하며 시설 노후화 심화','이곳에 상위 문제나 원인을 입력해 보세요.',cs)
cs=''
for x,n in zip([70,457,844],['분석 키워드','디지털 환경','업무 문화']):cs+=box(x,246,364,353,'linear-gradient(#f0f0f0,#f7f7f7)',8)+banner(x,246,364,47,n)
cs+=box(100,325,101,103,'#9faeba',22,'text-align:center;display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:700;','부족한<br>회의실<br>XX %')+box(214,322,191,44,'#cad1d7',15,'display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:700;','열악한 휴게실 XX %')+box(100,441,101,46,'#cad1d7',15,'display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:700;','키워드 XX %')+box(214,383,191,104,'#8498ac',22,'display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:700;','노후 사무공간 XX %')+text(116,522,270,'현재 업무 환경에 대한<br>구체적인 설명을 입력해 보세요.',17,align='center')
cs+=svgchart(496,303,286,165,[40,70],['현재','필요수준'],80,colors=['#a3a3a3','#6287aa'])+bullets(472,492,335,['환경1  레거시 시스템 의존도가 높아\n            업무 효율성 저하','환경2  협업 툴 부재로 비효율 발생'],18,60)
for j,n in enumerate(['경직된 회의 문화','부족한 자율성','키워드 입력란']):
 y=322+j*94;cs+=text(871,y,310,'• &nbsp;'+n,19,600)+text(888,y+27,295,'해당 키워드에 관한 현황 설명',17)
 if j<2:cs+=line(874,y+70,300,dotted=True)
P[6]=shell(6,'현황 분석','현재 업무 환경 실태','이곳에 상위 문제나 원인을 입력해 보세요.',cs)
cs=''
for j,(v,n) in enumerate([(72,'업무 환경<br>개선 필요'),(64,'조사<br>항목명')]):
 y=257+181*j;cs+=box(68,y,544,160,'#f3f3f3',3)+box(68,y,544*(78 if j==0 else v)/100,160,'linear-gradient(90deg,#194d74,#96a4ae)',3)+text(123,y+43,170,str(v)+'%',52,800,'white')+text(238,y+51,200,n,22,600,'white')+arrow(642,y+65,28,28,NAVY)+text(696,y+25,170,['가장 불편한 요소','세부 분석 제목'][j],21,500,align='center')+text(693,y+65,180,'위 데이터에 대한<br>구체적인 설명이나<br>세부 내용을 입력해보세요.',17,align='center')
cs+=box(913,246,295,353,'linear-gradient(#f7fbfd,#e7f4fd)',6)+banner(913,246,295,43,'조사결과')
for j,s in enumerate(['“업무 툴의 불편함으로 효율적인<br>소통에 제약이 있어요.”','“회의 공간이 부족해<br>원활한 협업이 어려워요.”','“구체적이고 공감 가능한 불편사항<br>을 표현해 보세요.”']):
 cs+=text(935,317+j*105,249,s,17,align='center')
 if j<2:cs+=line(948,393+j*105,225,dotted=True)
P[7]=shell(7,'현황 분석','직원 만족도 조사 결과','직원 만족도 조사의 핵심 결과를 간단하게 요약해 보세요.',cs)
cs=''
for j,(n,c) in enumerate([('환경적 요인','#9aabb8'),('제도적 요인','#6b849c')]):
 y=212+202*j;cs+=box(68,y,260,185,'#f8f8f8',12)+banner(68,y,260,43,n,c)
 for k,s in enumerate(['10년 이상 노후 공간이<br>70% 차지' if j==0 else '제도적 요인으로 인한 주요<br>문제점을 입력하세요.','환경적 요인으로 인한 주요<br>문제점을 입력하세요.' if j==0 else '제도적 요인으로 인한 주요<br>문제점을 입력하세요.']):cs+=circle(84,y+53+74*k,20,NAVY,str(k+1),12,'white')+text(116,y+53+74*k,200,s,17)
 cs+=line(91,y+112,220,dotted=True)
cs+=box(350,212,487,387,'#f8f8f8',10)+banner(350,212,487,43,'핵심 문제점')
for j,n in enumerate(['공간 효율성 저하','시스템 노후화','경직된 근무 방식']):
 y=289+j*110;cs+=circle(365,y+3,20,NAVY,str(j+1),12,'white')+text(396,y,170,n,19,600)+bullets(537,y,283,[['1인당 근무 면적 권장 기준 미달','문제의 구체적인 내용을 설명해 보세요.'],['업데이트 없는 업무 시스템 다수','문제의 구체적인 내용을 설명해 보세요.'],['문제의 구체적인 내용을 설명해 보세요.','문제의 구체적인 내용을 설명해 보세요.']][j],16,30)
 if j<2:cs+=line(369,y+81,448,dotted=True)
cs+=hugearrow(875,313,144,167).replace('#64cde8','#a3a3a3').replace('#f7f3ff','#ffffff')+box(1035,261,174,288,'#4b4b4b',10,'display:flex;align-items:center;justify-content:center;text-align:center;color:white;font-size:23px;font-weight:800;line-height:1.4;','생산성<br>저하로<br>이어지는<br>악순환<br>구조 형성')
P[8]=shell(8,'문제점 도출','도출된 문제점의 핵심을 간단하게 요약해 보세요.',content=cs)
cs='';heads=['쾌적한 물리적 환경 조성','디지털 업무 환경 고도화','세 번째 개선 목표']; notes=[['노후 시설 교체 및 현대화','구체적인 목표 내용 입력란'],['통합 협업 플랫폼 구축','구체적인 목표 내용 입력란'],['수평적 소통 문화 확립','구체적인 목표 내용 입력란']]
for j in range(3):
 x=116+356*j;cs+=box(x,213,337,126,'#f9f9f9',8)+banner(x,213,337,43,heads[j],['#8ba8bf','#6287aa',NAVY][j])+bullets(x+67,277,258,notes[j],16,27)
cs+=box(512,369,256,105,content='<svg viewBox="0 0 256 105" width="256" height="105"><defs><linearGradient id="down" x1="0" y1="0" x2="0" y2="1"><stop stop-color="white"/><stop offset=".65" stop-color="#77b5f3"/><stop offset="1" stop-color="#64d3ed"/></linearGradient></defs><path d="M0 0 C30 8 51 35 66 66 L26 66 L128 105 L230 66 L190 66 C205 35 226 8 256 0 Z" fill="url(#down)"/></svg>')+box(352,485,576,113,BLUE,23,'text-align:center;color:white;',text(0,25,576,'VISION',19,800,'#fff6c5',align='center')+text(0,58,576,'최종적으로 달성하고자 하는 비전을 입력해 보세요.',23,700,'white',align='center'))
P[9]=shell(9,'개선 목표','개선을 통해 달성하고자 하는 최종 목표를 간단하게 요약해 보세요.',content=cs)
cs=text(100,236,310,'물리적 환경 개선의 핵심 방향',22,500,align='center')+box(100,292,305,117,'#b7d9f8',60,'display:flex;align-items:center;justify-content:center;text-align:center;font-size:17px;','고정 좌석제를 자율 좌석제로<br>전환해 공간 활용도 향상')+circle(242,420,21,BLUE,'+',20,'white')+box(131,450,244,125,'#dce5ec',64,'display:flex;align-items:center;justify-content:center;text-align:center;font-size:17px;','협업 공간 30% 확충 및<br>다양한 업무 존 구성')+box(454,212,754,387,PALE,8)+banner(454,212,754,47,'공간별 개선 계획',BLUE)
for j,n in enumerate(['오픈 협업존','포커스존','라운지존']):
 x=476+j*252;cs+=ph(x,281,212,203,j+1)+text(x,503,212,n,22,700,BLUE,align='center')+text(x,537,212,'해당 공간에 대한<br>설명을 입력해주세요.',17,align='center')
 if j<2:cs+=box(x+230,287,1,299,extra='border-right:2px dotted #aebbc7;')
P[10]=shell(10,'개선 방안 : 물리적 환경','물리적 환경 개선의 핵심 방향과 목표를 간단하게 요약해 보세요.',content=cs)
cs=hugearrow(590,365,109,115)
for j,(x,title) in enumerate([(69,'레거시 시스템'),(717,'통합 협업 플랫폼')]):
 cs+=box(x,212,495,386,'linear-gradient(#f6f6f6,#f6f6f6)' if j==0 else 'linear-gradient(#f6fafc,#e7f4fd)',8)+banner(x,212,495,47,title,NAVY if j==0 else BLUE)+box(x+246,286,1,296,extra='border-left:2px dotted #b8c4ce;')+line(x+20,423,455,dotted=True)
 names2=[['일반 메신저 사용','파일 공유 시 이메일 의존','개선 전 문제점 설명','개선 전 문제점 설명'],['메신저, 문서 통합 환경','개선 후 변화 내용 설명','클라우드 기반 실시간 협업','개선 후 변화 내용 설명']][j]
 for k,n in enumerate(names2):
  xx=x+(k%2)*247;yy=277+(k//2)*168;cs+=text(xx,yy,247,f'0{k+1}',19,700,'#6689a8' if j==0 else BLUE,align='center')+text(xx+10,yy+34,227,n,19 if len(n)>12 else 21,700,align='center')+text(xx+20,yy+78,207,'해당 내용에 대한 설명을<br>간략하게 입력해주세요.',18,align='center')
P[11]=shell(11,'개선 방안 : 디지털 환경','디지털 환경 개선의 핵심 방향과 목표를 간단하게 요약해 주세요.',content=cs)
cs=box(68,213,112,385,'#315571',15,'display:flex;align-items:center;justify-content:center;text-align:center;color:white;font-size:22px;font-weight:700;','개선<br>사항')+box(652,213,112,385,BLUE,15,'display:flex;align-items:center;justify-content:center;text-align:center;color:white;font-size:22px;font-weight:700;','개선 후<br>모습')+arrow(603,392,28,28)
for j,n in enumerate(['회의 문화','의사결정','근무 방식','사내 복지','지원금 제도']):
 y=213+j*82;cs+=box(194,y,381,57,'#f8f8f8',3)+box(779,y,430,57,'#dfedfc',5)+text(218,y+16,85,n,17,700)+text(300,y+17,275,['주 평균 15시간의 비효율적 회의','다단계 결재로 처리 지연 (평균 X일)','이곳에 현재의 업무 문화를 설명해 보세요.','이곳에 현재의 업무 문화를 설명해 보세요.','이곳에 현재의 업무 문화를 설명해 보세요.'][j],16)+text(797,y+16,90,n,17,700,BLUE)+text(889,y+17,310,['회의 시간 50% 단축 및 사전 아젠다 필수화','결재 단계 축소 및 권한 위임 확대','이곳에 개선 후 변화 내용을 입력해 보세요.','이곳에 현재의 업무 문화를 설명해 보세요.','이곳에 현재의 업무 문화를 설명해 보세요.'][j],16)
P[12]=shell(12,'개선 방안 : 업무 문화 개선','업무 문화 개선의 핵심방향과 목표를 간단하게 요약해 보세요.',content=cs)
cs=box(68,213,299,385,'#f6f6f6',17)+box(418,213,791,385,'linear-gradient(#eaf6fe,#cdecff)',17)+banner(162,225,112,41,'개선 전')+banner(768,225,112,41,'개선 후',BLUE)+arrow(377,392,28,28)
for j,(x,w) in enumerate([(85,265),(435,230),(698,230),(961,230)]):
 cs+=ph(x,286,w,199,j+1)+text(x,504,w,'이곳에 개선 전 환경을 설명해 보세요. 업무 비효율이 발생한 원인과 개선이 필요한 여지에 대해 서술해 보세요.',16,align='center',line=1.6)
 if 0<j<3:cs+=box(x+w+16,282,1,300,extra='border-right:2px dotted #aebbc7;')
P[13]=shell(13,'개선 전후 비교 예상','개선 전후 비교의 핵심 변화를 간단하게 요약해 보세요.',content=cs)
cs=text(288,236,120,'협업 효율성<br>변화율',22,700,align='center')+box(430,215,458,45,extra='border:4px dashed #d8eaf6;')+box(430,215,233,45,'#8ca8c0',content=text(0,8,233,'58%',23,700,'white',align='center'))+box(430,274,458,45,'linear-gradient(#008cf2,#65b9fa)',content=text(0,7,458,'86%',23,700,'white',align='center'))+text(960,236,80,'XX%<br>차이',22,700,'#6c8eaa',align='center')+box(287,349,805,40,extra='border:1px solid #c8ced2;border-bottom:0;border-radius:17px 17px 0 0;')+box(898,215,36,104,extra='border:1px solid #c8ced2;border-left:0;border-radius:0 17px 17px 0;')+box(690,328,1,18,extra='border-left:1px solid #c8ced2;')
for j,(x,w,title) in enumerate([(69,439,'정량적<br>변화'),(531,419,'정성적<br>변화')]):
 cs+=box(x,379,w,219,'linear-gradient(#bee5fb,#effaff)',12)+box(x,379,96,219,BLUE,10,'display:flex;align-items:center;justify-content:center;text-align:center;color:white;font-size:21px;font-weight:700;',title)
 for k in range(3):
  yy=400+k*70
  if j==0:cs+=circle(x+114,yy,28,'white',str(1 if k==0 else 2),18,BLUE)+text(x+151,yy,w-160,['업무 처리 속도 평균 40% 단축','정량적 변화를 입력해주세요.','정량적 변화를 입력해주세요.'][k],19,700,'#0a5788')+text(x+151,yy+31,w-160,'구체적인 변화 내용을 입력해 보세요.',16)
  else:cs+=box(x+116,yy,104,38,'white',19,'display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:700;color:#58a4ee;','keyword')+text(x+241,yy-1,w-250,'눈에 보이는 변화에 대해<br>설명해 보세요.',16)
cs+=arrow(960,478,28,28)+box(1001,379,207,219,'#00518f',12,'display:flex;align-items:center;justify-content:center;text-align:center;color:white;font-size:23px;font-weight:800;line-height:1.5;','“일하고 싶은<br>직장으로 거듭나는<br>실질적 변화”')
P[14]=shell(14,'개선 전후 비교 예상','개선 전후 비교의 핵심 변화를 간단하게 요약해 보세요.',content=cs)
cs=box(103,238,1071,360,extra='border:1px solid #aebdca;border-radius:190px;')+box(381,215,515,55,BLUE,28,'display:flex;align-items:center;justify-content:center;color:white;font-size:20px;font-weight:700;','연쇄적인 효과들이 만들어내는 궁극적 결과를 입력해 보세요.')
for x,n,note in [(321,'생산성 향상','효율적인 업무 환경으로 직<br>원 1인당 생산성 20% 향상'),(580,'인재 경쟁력','우수 인재 유치 및<br>이직률 30% 감소 예상')]:cs+=box(x,291,321,142,'#d7eafb' if x==321 else '#d6f5fb',75)+text(x,313,321,n,20,700,'#00518f',align='center')+text(x,354,321,note,17,align='center')
for j,n in enumerate(['업무 효율<br>증대','직원<br>만족도 향상','조직<br>경쟁력 강화']):cs+=circle(360+j*214,447,137,'linear-gradient(#66b8fa,#e2f5fe)',n,20,'#05598f')
cs+=hugearrow(512,498,38,37)+hugearrow(728,498,38,37)
P[15]=shell(15,'기대효과','기대효과의 핵심 내용을 간단하게 요약해 보세요.',content=cs)
cs=''
ns=['직원 만족도 향상','운영 효율성 확대','기업 이미지 및 브랜드 가치 향상','효과 영역 키워드'];nts=['쾌적한 환경으로 업무 몰입도 증가<br>직원 만족도 지수 35% 향상','디지털화를 통한 프로세스 간소화<br>행정 업무 시간 30% 단축','혁신적 업무 환경으로 브랜드 가치 향상<br>ESG 경영 실천 사례로 대외 인지도 제고','해당 영역의 기대효과에 대한 설<br>명을 간략하게 입력해주세요.']
for j in range(4):
 x=69+(j%2)*584;y=216+(j//2)*199;cs+=box(x,y,569,184,'#edf9fd' if j%3==0 else '#e0edfc',8)
 if j%2==0:tx=x+24;px=x+296
 else:tx=x+286;px=x+20
 cs+=ph(px,y+13,259,154,j+1)+text(tx,y+15,265,ns[j],18,700,align='center' if j%2 else 'left')+line(tx,y+55,265,dotted=True)+text(tx,y+91,265,nts[j],17,align='center' if j%2 else 'left')
cs+=box(562,325,156,118,BLUE,59,'display:flex;align-items:center;justify-content:center;text-align:center;color:white;font-size:23px;font-weight:700;','통합적<br>시너지 효과')+text(1023,608,186,'페이지 내 인물 사진은 샘플 이미지 입니다.',9,color='#bbb',align='right')
P[16]=shell(16,'기대효과','기대효과의 핵심 내용을 간단하게 요약해 보세요.',content=cs)
cs=box(68,217,1140,90,'#f8f8f8',3)+banner(68,217,122,90,'추진<br>일정','#aaa')+box(68,327,122,195,'linear-gradient(90deg,#008ff3,#68bafb)',4,'display:flex;align-items:center;justify-content:center;text-align:center;color:white;font-size:20px;font-weight:700;','추진<br>일정')+banner(68,548,122,50,'점검 사항',BLUE)+line(281,275,825,dotted=True)
for j,n in enumerate(['Q1','Q2','Q3','Q4','다음해 상반기']):
 x=191+j*206;cs+=text(x,233,193,n,18,600,align='center')+circle(x+85,268,12,NAVY,'',12)+box(x,327,193,195,'linear-gradient(#eff9ff,#daedff)',8)+label(x+58 if j<4 else x+58,344,['계획 수립','설계 및 준비','단계별 키워드','단계별 키워드','안정화'][j],83 if j in (0,4) else 100)+text(x+13,395,167,'업무 환경 개선<br>TF 구성' if j==0 else '주요 추진 내용<br>입력란',20,700,align='center')+line(x+16,461,161,dotted=True)+text(x+4,481,185,'직원 의견 수렴 및 요구 분석',15,align='center',extra='white-space:nowrap;')+box(x,548,193,50,'#b8d9fa',1,content=text(8,13,177,['직원 의견 수렴 및 요구 분석','예산 확정 및 업체 선정','주의 및 점검 사항 입력','주의 및 점검 사항 입력','주의 및 점검 사항 입력'][j],15,align='center'))+box(x+96,529,1,14,extra='border-left:2px dotted #aebbc7;')
P[17]=shell(17,'추진 일정','추진 일정의 전체 기간과 목표를 간단하게 요약해 보세요.',content=cs)
cs=''
for j,(n,note) in enumerate([('예산 분배','공간 개선에 전체 예산의 40% 집중 투자'),('예산 규모','예산 배분 원칙이나 방향을 입력해 보세요.'),('투자 방향','예산 배분 원칙이나 방향을 입력해 보세요.')]):
 y=215+j*69;cs+=box(69,y,757,58,'#f8f8f8',1)+text(94,y+17,35,f'0{j+1}',17,700,BLUE)+text(128,y+16,110,n,19,700)+text(224,y+17,590,note,16)
cs+=table(69,430,757,168,['항목','예산','비고'],[['텍스트공간개선','X억원','-'],['디지털 인프라 구축','X억원','-'],['','','']])+box(843,213,345,386,'#f5fafd',1)+text(843,236,345,'예산 분배',20,700,align='center')+text(860,269,310,'공간 개선에 전체 예산의 40% 집중 투자',16,align='center')
cs+=box(890,308,250,250,'conic-gradient(#d7eafa 0 30%,#8dc8ff 30% 60%,#59a8ef 60% 90%,#6485a4 90% 100%)',125)+circle(965,383,100,'#f5fafd','',20)
for x,y,v in [(979,335,'10'),(1077,367,'30'),(979,507,'30'),(915,420,'30')]:cs+=text(x,y,40,v,19,700,'#00518f',align='center')
cs+=text(885,564,266,'▪ 공간 개선  ▪ 디지털 인프라  ▪ 제도 및 운영  ▪ 예비비',9,color='#6a8ba9',align='center')
P[18]=shell(18,'예산 계획','예산 규모와 투자 방향을 간단하게 요약해 보세요.',content=cs)
cs=''
for j,n in enumerate(['김미리','이미리','최미리','박미리','권미리','심미리']):
 x=69+j*193;cs+=box(x,236,175,363,'#ecf8fe',1)+ph(x,236,175,209,j+1)+text(x+18,461,105,n,25,700)+text(x+97,472,70,['상무','팀장','직책','직책','직책','직책'][j],13)+line(x+14,514,145,dotted=True)+text(x+18,530,142,['전체 총괄 및 의사결정,<br>예산 승인','물리적 환경 설계 및<br>시공 관리','이곳에 담당 역할을<br>설명해 보세요.','이곳에 담당 역할을<br>설명해 보세요.','이곳에 담당 역할을<br>설명해 보세요.','이곳에 담당 역할을<br>설명해 보세요.'][j],16,line=1.6)
cs+=text(1023,608,186,'페이지 내 인물 사진은 샘플 이미지 입니다.',9,color='#bbb',align='right')
P[19]=shell(19,'담당 조직 및 역할','업무 환경 개선 TF',content=cs+text(370,147,700,'담당 조직 구성과 운영 방식을 간단하게 요약해 보세요.',16))
cs=box(68,215,512,384,'#f8f8f8',18)+box(68,215,146,384,'#8aa8bf',16,'display:flex;align-items:center;justify-content:center;text-align:center;color:white;font-size:22px;font-weight:700;line-height:1.4;','B사 스마트<br>오피스 전환<br>프로젝트<br><small style="font-size:15px;color:#fff6cc">6개월 프로젝트<br>투자비 X억 원</small>')+box(596,215,612,384,'#f7f7f7',18)
for j,n in enumerate(['2078년 본사 업무 공간 전면 리뉴얼','6개월 만에 생산성 28% 향상 달성','개선 세부 내용']):
 cs+=circle(231,235+j*69,27,'#90c7fc',str(j+1),16,'white')+text(268,236+j*69,305,n,17,700,'#444')+text(268,265+j*69,305,'구체적인 변화 내용을 입력해 보세요.',16,color='#555')
cs+=banner(268,433,109,92,'고정 좌석,<br>칸막이 사무실','#5b5b5b',15)+hugearrow(391,460,39,39)+banner(440,433,120,92,'자율좌석,<br>개방형 협업 공간','#8dc7fb',15)+text(675,236,480,'B사 생산성 및 퇴사자 추이',19,700,'#444',align='center')+text(990,241,70,'단위: %',10,color='#aaa')+svgchart(627,260,550,170,[50,40,30,20,15],['1Q','2Q','3Q','4Q','5Q'],50,'both',colors=['#90c7fc']*5)
for j in range(3):cs+=ph(613+j*199,459,183,125,j+1)
P[20]=shell(20,'타사 환경 개선 사례','타사 사례 분석의 목적과 핵심 내용을 간단하게 요약해 보세요.',content=cs)
cs=text(129,116,700,'THANK YOU',18,800,BLUE)+text(122,135,800,'감사합니다.',88,700,extra='letter-spacing:-4px;')+text(122,272,950,'프로젝트의 의미와 당부를 담은 두세줄 정도의 마무리 문장을 입력해 보세요.',17)
for j,(n,note) in enumerate([('TEL.','02-0000-0000'),('E-MAIL','CONTACT@MIRIDIH.COM'),('ADDRESS','미리시 미리구 미리로 123'),('HOME','WWW.MIRIDIH.COM')]):
 y=371+j*76;cs+=box(766,y,404,57,'#f8f8f8',3)+text(791,y+17,100,n,16,800,BLUE)+text(880,y+18,280,note,15)
P[21]=shell(21,mode='closing',content=cs)
for i,html in P.items():(R/f'slide_{i:02d}.html').write_text(html)
(R/'index.html').write_text('<!doctype html><meta charset="utf-8"><h1>Skylight replicas</h1>'+''.join(f'<p><a href="slide_{i:02d}.html">Slide {i:02d}</a></p>' for i in P))
print('WROTE',len(P))
