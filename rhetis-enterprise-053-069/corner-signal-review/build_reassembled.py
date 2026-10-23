from pathlib import Path
import json
R=Path(__file__).parent;C=R.parent/'corner-signal';REF=Path('/workspace/work/ref');data=json.loads((R/'page-data.json').read_text());P={}
def root(k,cls,body,col=1,cols=12,row=1,rows=6,extra=''):return f'<div class="{cls}" data-el="corner-signal-{k}" style="grid-column:{col} / span {cols};grid-row:{row} / span {rows};{extra}">{body}</div>'
def card(title,note='',kick='',on=False,fig='',col=1,cols=4,row=1,rows=6,extra=''):
 return root('card','card'+(' on' if on else ''),'<div class="parts">'+(f'<p class="kick">{kick}</p>' if kick else '')+(f'<b class="fig">{fig}</b>' if fig else '')+f'<p class="name">{title}</p><p class="note">{note}</p></div>',col,cols,row,rows,extra)
def head(title,note='',col=1,cols=12,row=1,rows=6,on=False):return root('headline','headline'+(' on' if on else ''),f'<h2>{title}</h2><p class="note">{note}</p>',col,cols,row,rows)
def frame(col,cols,row=1,rows=6):return root('image-frame','frame','<div class="seat" data-ph="1"></div>',col,cols,row,rows)
def prose(txt,col=1,cols=12,row=1,rows=6):return root('prose','prose',f'<p>{txt}</p>',col,cols,row,rows)
def bars(vals,col=1,cols=12,row=1,rows=6):return root('chart-bar','bars',''.join(f'<div class="bar'+(' on' if j==len(vals)-1 else '')+f'" style="--v:{v}"><b>{v:,}</b><span>{2050+j}</span></div>' for j,v in enumerate(vals)),col,cols,row,rows,'--max:'+str(max(vals)*1.2))
def line(vals,col=1,cols=12,row=1,rows=6):return root('chart-line','lines',''.join(f'<div class="pt" style="--v:{v}"><b>{v}</b><span>{2050+j}</span></div>' for j,v in enumerate(vals)),col,cols,row,rows,'--max:'+str(max(vals)*1.2))
def area(vals,col=1,cols=12,row=1,rows=6):return root('chart-area','areas','<div class="series tone-1"><p class="name">매출 성장 추이</p>'+''.join(f'<div class="pt" style="--v:{v}"><b>{v}</b></div>' for v in vals)+'</div><div class="axis">'+''.join(f'<span>{2050+j}</span>' for j in range(len(vals)))+'</div>',col,cols,row,rows,'--max:'+str(max(vals)*1.2))
def donut(vals,col=1,cols=12,row=1,rows=6):return root('chart-donut','donuts',''.join(f'<div class="donut" data-el="corner-signal-chart-donut" style="--v:{v}"><b class="fig">{v}%</b><p class="name">수익원 {j+1}</p></div>' for j,v in enumerate(vals)),col,cols,row,rows)
def lst(items,col=1,cols=12,row=1,rows=6):return root('list','list divided',''.join(f'<div class="item"><p class="name">{a}</p><p class="note">핵심 기술과 고객의 요구를 연결하여 새로운 가치를 만듭니다.</p></div>' for a in items),col,cols,row,rows)
# Each original page is rebuilt only with registered roots and foundation placement.
P[2]=''
for k in range(2):P[2]+=root('agenda','agenda',''.join(f'<div class="entry"><b class="mark">{j+1+k*5:02}</b><p class="name">{x}</p><p class="note"></p></div>' for j,x in enumerate(['회사소개','문제점','솔루션','시장 규모','자사 서비스'] if k==0 else ['비즈니스 모델','경쟁 우위','성장 전략','팀 소개','투자 유치 계획'])),5+k*4,4,1,6)
P[2]+=frame(1,3,3,4)
P[3]=head('비전을 현실로 만드는 리더, CEO 김미리입니다.',col=1,cols=7,row=1,rows=2)+prose('저는 기업의 CEO 김미리입니다. 핵심 경력과 전문성을 바탕으로 고객이 겪는 가장 큰 문제를 해결합니다.<br><br>저희 팀은 고객의 요구에 귀를 기울이고 기술의 혁신으로 지속 가능한 가치를 만들어갑니다.',1,7,3,4)+frame(9,4)
P[4]=head('회사가 궁극적으로 만들고 싶은 미래상을 압축한<br>슬로건을 여기에 입력해 주세요.','MIRI COMPANY',2,10,2,3,False)+frame(1,12,5,2)
P[5]=''.join(root('card','card'+(' on' if i==0 else ' tone-2' if i==1 else ''),'<div class="parts"><p class="kick">Pain Point 0'+str(i+1)+'</p><span class="mark"><span class="icon" data-icon="'+['handshake','list-checks','settings'][i]+'"></span></span><p class="name"></p><p class="note">이 문제를 겪는 고객이 어떤 불편함을 겪는지 보여주세요. 각 문제점의 핵심을 구체적으로 설명합니다.</p></div>',1+i*4,4) for i in range(3))
P[6]=root('steps','steps',''.join(f'<div class="step"><b class="mark">PROCESS {i+1}</b><p class="name">{t}</p><p class="note">고객이 겪는 어려움을 이해하고 검증된 솔루션으로 사업의 성과를 만들어갑니다.</p></div>' for i,t in enumerate(['문제 정의 및 솔루션 제안','핵심 솔루션의 자동 실행','핵심 솔루션 성과 측정','성과 측정 및 인사이트 제공'])))
P[7]=card('이 시장은 00% 성장하는<br>00조 원의 기회가 있습니다.','TAM 전체 시장 / SAM 유효 시장 / SOM 목표 시장',col=1,cols=4)+root('concentric','orbit',''.join(f'<div class="ring"><p class="name">{a}</p><b class="fig">{v}</b><p class="note">시장의 규모</p></div>' for a,v in [('TAM','20M+'),('SAM','18M+'),('SOM','9M+')]),5,8)
P[8]=card('시장은 [성장 원인]에 의해 더욱 빠르게 확장하고 있습니다.','국내 중소기업 대상 시장 5,000억 원. 아시아 시장 50조 원. 글로벌 시장 500조 원.',col=1,cols=4)+root('concentric','orbit',''.join(f'<div class="ring"><p class="name">{a}</p><b class="fig">{v}</b></div>' for a,v in [('TAM','500T'),('SAM','50T'),('SOM','500B')]),5,8)
P[9]=frame(4,6)
for i,t in enumerate(['기술력','사용자 경험','만족도','품질','신뢰도','서비스']):P[9]+=card(f'{i+1}. 차별화된 {t}','고객과 시장의 성장을 만드는 핵심 가치입니다.',on=i<3,col=1 if i<3 else 10,cols=3,row=1+(i%3)*2,rows=2)
P[10]=''.join(card(t,'고객에게 가치를 제공하고 지속 가능한 수익을 만듭니다.',kick=str(i+1),on=i==0,col=1+i*3,cols=3,row=1+(i%2),rows=5) for i,t in enumerate(['핵심 수익 모델','확장 수익 모델','잠재적 수익 모델','부가 수익 모델']))
P[11]=''.join(card(t,'Basic Plan: 월 10만 원<br>Pro Plan: 월 50만 원',kick='Model '+str(i+1),on=i==0,col=1+i*4,cols=4) for i,t in enumerate(['구독료 (SaaS)','중개 수수료','기타 부가 수익']))
P[12]=head('수익 모델의 핵심을 한줄로 설명해주세요.',col=1,cols=8,row=1,rows=1)+donut([50,30,20],1,8,2,5)+area([20,40,60,70,90],9,4,1,6)
P[13]=''.join(root('metric','stat','<div class="parts"><b class="fig">'+v+'</b><p class="name">'+t+'</p><p class="note">'+n+'</p></div>',1+i*3,3,1,2) for i,(v,t,n) in enumerate([('1200','누적 판매량','000만 개'),('40%','월간 활성 사용자','40% 증가'),('60M','월간 반복 매출','000억 원'),('35%','고객 재구매율','35% 증가')]))+bars([200,400,600,700,900,1200],1,12,3,4)
P[14]=line([30,40,60,70,100],1,4)+area([20,40,60,70,90],5,4)+bars([20,25,40,35],9,4)
P[15]=root('positioning','posmap','<div class="axis-x"><span>low response rate</span><span>High response rate</span></div><div class="axis-y"><span>low cost</span><span>High cost</span></div>'+''.join(f'<div class="mark'+(' on' if i==3 else '')+f'" style="--x:{x};--y:{y}"><p class="name">{n}</p></div>' for i,(x,y,n) in enumerate([(15,75,'Miri Company'),(35,65,'Miri Company'),(65,65,'Miri Company'),(85,80,'MIRI COMPANY'),(20,15,'Miri Company'),(40,25,'Miri Company'),(70,30,'Miri Company')])),1,8)+root('card','card line','<div class="parts"><p class="name">경쟁사 대비<br>우리의 명확한 차별점</p><p class="note">타사 응답 서비스 대비 저렴한 비용과 높은 응답 빈도<br><br>경쟁사가 따라오기 어려운 핵심 기술과 전문성<br><br>우리만의 독보적인 기술과 특허<br><br>경쟁 환경 및 시장에서의 위치</p></div>',9,4)
P[16]=root('versus','versus','<div class="side on"><p class="name">MIRICOMPANY</p>'+''.join(root('gauge','meter',f'<p class="name">OPTION {i+1}</p><b class="fig">100%</b>',extra='--v:100') for i in range(4))+'</div><b class="vs">VS</b><div class="side"><p class="name">COMPANY</p>'+''.join(root('gauge','meter',f'<p class="name">OPTION {i+1}</p><b class="fig">{v}%</b>',extra=f'--v:{v}') for i,v in enumerate([50,65,75,40]))+'</div>')
P[17]=''.join(card(t,'목표: 이 단계의 구체적인 목표를 작성합니다.<br>전략: 목표 달성을 위한 구체적인 액션을 제시합니다.',kick='PHASE '+str(i+1),on=i==0,col=1+i*3,cols=3,row=4-i,rows=3) for i,t in enumerate(['~2026<br>국내 시장 선점','~2027<br>아시아 시장 진출','~2028<br>글로벌 리더십 확보','~2029<br>글로벌 시장 진출']))
P[18]=root('architecture','arch',''.join(f'<div class="layer"><p class="name">{t}</p><span class="chip">핵심 기술</span><span class="chip">데이터 제어</span></div>' for t in ['시각 시스템','객체 식별 시스템','포장 시스템']),1,8)+frame(9,4)
P[19]=root('person','people',''.join(f'<div class="person" data-el="corner-signal-person"><div class="seat portrait" data-ph="{i+1}"></div><p class="name">{n}</p><p class="note">{r}<br>현재 직책을 적어주세요.<br>업계 경험과 전문 분야를 소개합니다.</p></div>' for i,(n,r) in enumerate([('김미리','CEO'),('최미리','Engineer'),('이미리','Developer'),('조미리','Marketer'),('강미리','Marketer')])))
P[20]=donut([40,30,20,10],1,6)+lst(['투자 유치 목표 000억 원','R&D 및 기술 고도화','마케팅 및 고객 확보','핵심 인재 영입'],7,3)+bars([20,40,60,70,90],10,3)
P[21]=root('steps','steps',''.join(f'<div class="step"><b class="mark">0{i+1}<br>{k}</b><span class="icon" data-icon="{ic}"></span><p class="name">{t}</p><p class="note">핵심 제품과 고객의 성장을 위한 구체적인 목표를 제시합니다.</p></div>' for i,(k,t,ic) in enumerate([('THE ASK','투자금 목표 금액 유치','file-text'),('USE OF FUNDS','R&D & 마케팅 인재 영입 투자','contact-round'),('NEXT-LEVEL','제품 고도화 고객 확보','network'),('GROWTH','매출 성장 기업 가치 증대','flag')])) )
# Only runtime style inputs: supplied palette + declared type-step values. No layout rules here.
palette=json.loads((REF/'contract/palette.json').read_text());palette['light'].update({'--page':'#f0f1f2','--ink':'#222222','--a1':'#0066cf','--a1-on':'#ffffff','--a2':'#659de7','--a2-on':'#111111','--a3':'#aaaaaa','--a3-on':'#111111','--a4':'#555555','--a4-on':'#ffffff'});
for j in range(1,10):
 for suffix in ['', '-soft','-muted']:
  t=j/5 if j<=5 else (j-5)/4;rgb=[round(240*(1-t)+c*t) for c in [0,102,207]] if j<=5 else [round(c*(1-t)+d*t) for c,d in zip([0,102,207],[0,42,90])];palette['light'][f'--a1-{j}{suffix}']='#'+''.join(f'{c:02x}' for c in rgb)
steps=json.loads((REF/'contract/type-steps.json').read_text());runtime=''.join(('.slide.dark' if m=='dark' else '.slide')+'{'+''.join(f'{k}:{v};' for k,v in p.items())+'}' for m,p in palette.items())+'.slide{'+''.join(f'--type-{n}:{n}px;' for n in steps)+'}'
(R/'reassembled/runtime.css').write_text(runtime)
links='<link rel="stylesheet" href="../../fonts/fonts.css"><link rel="stylesheet" href="../corner-signal/kit/css/tokens.css">'
# Correct relative from reassembled/ to collection/ is ../../corner-signal/.
links='<link rel="stylesheet" href="../../fonts/fonts.css"><link rel="stylesheet" href="../../corner-signal/kit/css/tokens.css"><link rel="stylesheet" href="runtime.css"><link rel="stylesheet" href="../../corner-signal/foundation/foundation.css">'+''.join(f'<link rel="stylesheet" href="../../corner-signal/elements/{p.name}/element.css">' for p in sorted((C/'elements').iterdir()))
for i in range(1,22):
 if i==1:body='<section class="slide cover"><div class="page"><div class="lockup at-top-left"><p class="kicker">MIRI COMPANY</p><h1 class="title">MIRICOMPANY<br><b>IR DECK.</b></h1><p class="lead">빠른 투자 유치를 위한 핵심 문서</p></div><div class="seat back" data-ph="1"></div><p class="meta">경영 기획팀 | 김미리 팀장<br>Contact us | miri@miricompany.com</p></div></section>'
 else:
  t=data['titles'][i-1];cut={3:1,5:1,6:1,7:11,13:1,14:1,19:1,20:7}.get(i,len(t.split(' ')[0]));t='<b>'+t[:cut]+'</b>'+t[cut:]
  body=f'<section class="slide {"on" if i==4 else ""}"><div class="page"><header class="head"><h1 class="title">{t}</h1><p class="lead">{data["notes"][i-1].replace(chr(10),"<br>")}</p></header><div class="body">{P[i]}</div><footer class="foot"><span>Miricompany Investor Relations Deck</span><span>{i-1}</span></footer></div></section>'
 (R/f'reassembled/slide_{i:02}.html').write_text('<!doctype html><html lang="ko"><head><meta charset="utf-8">'+links+'</head><body style="margin:0">'+body+'</body></html>')
print('reassembled',21)
