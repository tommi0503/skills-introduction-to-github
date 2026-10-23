from pathlib import Path
import json,html
R=Path(__file__).parent; D=next(Path('/workspace/work/deck/miricanvas_기업_selected').glob('067*'))
B='#0066cf'; G='#5e5e5e'; BG='#f0f1f2'
titles=['MIRICOMPANY IR DECK.','TABLE OF CONTENTS','INFORMATION','Vision & Mission','Problem','Solution','Market Size & Opportunity','Market Volume','Product Deep Dive','Business Model','Business Model','Revenue Model','Traction','Traction','Competitive Landscape','Competitive Landscape','Growth Strategy','Technology & IP','Team','The Ask & Financials','Fundraising & Financial Plan']
notes=['','목차 순서를 위한 목차 설명입니다.\n이 페이지는 전체 흐름을 한눈에 정리하여 보여주세요.','우리는 기술과 서비스의 혁신으로 더 나은 비즈니스를 만듭니다.\n고객에게 가치의 시작을 제안합니다.','','고객이 겪는 가장 큰 Pain Point 3가지를 시각적으로 정리해주세요.\n각 항목마다 문제의 핵심과 그 중요도를 설명해 주세요.','앞서 제시한 문제를 해결하는 핵심 솔루션을 단계적으로 정리한\n프로세스입니다.','시장의 규모와 TAM, SAM, SOM으로 나누어 설명해 주세요.\n우리의 사업이 시장의 어디에 위치하는지 확인합니다.','시장의 세부 규모와 성장 가능성을 시각적으로 제시해 주세요.\n우리가 속하는 시장의 범위와 미래 가치를 보여줍니다.','제품의 핵심 기능과 사용자의 편의를 한눈에 확인할 수 있습니다.\n다양한 강점을 상세하게 설명해 주세요.','회사의 수익 구조와 핵심 비즈니스 모델을 보여주세요. 고객이 어떤 가치를\n느끼고 비용을 지불하는지 명확하게 설명해 주세요.','회사의 핵심 수익모델과 구독, 수수료, 광고 수익을 설명해주세요. 비즈니스 모델은 어떻게\n지속 가능한 성장을 만들어내는지 구체적으로 보여주세요.','비즈니스 모델에서 발생하는 세 가지의 수익 구조를 정리해 주세요.\n고객과 시장으로부터 창출하는 실질적 매출 성장의 방향을 확인합니다.','핵심 성과 지표(KPI)와 제품의 성장을 구체적인 숫자로 보여주세요.\n확보한 고객, 매출 그리고 누적 지표를 한눈에 볼 수 있습니다.','지속적으로 증가하는 핵심 지표를 여러 관점에서 보여주세요.\n비즈니스 모델의 성장 가능성과 시장 반응을 확인합니다.','경쟁사 대비 기술과 비용 경쟁력 및 차별점을 설명해 주세요.\n시장에서 우리 제품이 차지하는 위치와 강점이 무엇인지 확인합니다.','경쟁사 대비 우리 제품과 서비스의 핵심 경쟁력을 비교해 주세요.\n고객의 선택을 이끄는 차별화된 가치를 명확히 설명합니다.','회사의 성장 전략을 단계별로 정리해 주세요. 국내 시장의 성장과\n장기적인 글로벌 확장 계획을 구체적으로 확인합니다.','회사의 기술 경쟁력과 핵심 지식재산권을 설명합니다. 보유한 기술력과 특허를\n기반으로 지속 가능한 성장을 만들어갑니다.','회사를 성장시키는 핵심 인력과 전문성을 보여주세요.\n각 분야의 경험과 역량을 가진 멤버가 함께합니다.','투자 유치 규모 및 자금 활용 계획을 명확히 설명해 주세요.\n사업의 지속 가능성과 앞으로의 성장 계획을 보여줍니다.','회사의 재무 성장 계획과 투자금 활용 전략을 단계별로 설명해 주세요.\n기술과 제품 개발을 통한 지속적인 성장의 방향을 확인합니다.']
notes=['', '투자 유치를 위한 IR 덱 상세 템플릿\n이 페이지에 대한 설명을 1~2 문장으로 명확하게 서술하세요.', '우리는 [제품/서비스명]을 통해 [고객]의 [문제점]을 해결하고,\n[구체적인 혜택]을 제공합니다.', '회사의 존재 이유와 장기적인 목표를 1~2 문장으로 명확하게 서술하세요. 이 슬라이드는\n회사의 왜(Why)를 전달하며 투자자와의 감성적 연결고리를 만드는 공간입니다.', '고객이 겪는 가장 큰 고통(Pain Point) 3가지를 아이콘과 함께 제시하세요.\n각 문제점의 심각한 점을 1~2 문장으로 설명합니다.', '앞서 제시한 문제들을 우리의 제품/서비스가 어떻게 해결하는지 직관적인\n프로세스나 핵심 기능 레이아웃으로 보여주세요.', '시장의 규모를 TAM, SAM, SOM으로 나누어 깔때기형 다이어그램으로\n시각화하세요. 각 시장의 규모와 근거를 명확히 제시합니다.', '공략할 시장의 크기와 성장 가능성을 숫자로 보여주세요.\n신뢰할 수 있는 데이터와 함께 제시하여 시장의 매력도를 증명하세요.', '제품의 실물 이미지나 핵심 UI 화면을 중앙에 배치하고, 주요 기능들을\n선으로 연결하여 설명하는 레이아웃으로 활용하세요.', '회사의 핵심 수익 모델을 명확하게 구분하여 제시하세요. 고객이 어떤 가치에\n비용을 지불하는지 투자자가 쉽게 이해할 수 있어야 합니다.', '회사의 핵심 수익 모델(예: 구독, 수수료, 광고)을 명확히 설명하세요. 투자자가 회사가 어떻게\n돈을 버는지 쉽고 명확하게 이해할 수 있도록 가격 정책 표 등을 활용하는 것이 좋습니다.', '비즈니스 모델이 구체적으로 어떻게 돈으로 연결되는지를 명확하게 보여주세요.\n투자자는 이 페이지를 통해 우리 사업의 경제적 생존 가능성과 성장성을 판단합니다.', '핵심 성과 지표(KPI)를 대시보드 형태로 구성하여 성과를 한눈에\n보여주세요. 가장 자신 있는 지표는 가장 크게 강조합니다.', '단순히 몸집만 불리는 성장이 아닌, 효율성과 수익성을 동시에\n확보하고 있음을 증명합니다.', '경쟁사 포지셔닝 맵을 통해 시장 내 회사의 독보적인 위치를 시각적으로 보여주세요.\nX축과 Y축은 시장의 핵심 경쟁 요소를 기준으로 설정합니다.', '경쟁이 치열한 시장에서 어떻게 살아남을지를 넘어,\n어떻게 시장을 지배할 것인지에 대한 명확한 답을 제시하세요.', '회사의 성장 계획을 구체적인 마일스톤이 담긴 타임라인으로 제시하여 미래에 대한\n청사진을 보여주세요.', '회사의 기술적 깊이와 방어력을 증명하여, 투자가 단기적인 성과를 넘어 장기적으로\n지속 가능한 가치를 가질 것임을 설득하세요.', '핵심 팀원들의 사진, 이름, 직책, 그리고 이 사업을 성공시킬 수밖에 없는\n핵심 경력과 전문성을 간결하게 소개하세요.', '투자금 사용 계획은 파이 차트로, 향후 5년간의 매출 목표는 막대그래프로\n시각화하여 투자자에게 성장 계획을 명확히 전달하세요.', '발표의 마무리입니다. 이번 투자 유치의 목표와 계획을 명확하고\n자신감 있게 전달해야 합니다.']
def e(tag,s,cls='',style=''):return f'<{tag} class="{cls}" style="{style}">{s}</{tag}>'
def pos(s,x,y,w,h='',cls=''):
 return e('div',s,cls,f'left:{x}px;top:{y}px;width:{w}px;'+(f'height:{h}px;' if h else ''))
def tx(s,x,y,w,size=18,color='#222',weight=400,lh=1.5):return pos(e('div',s.replace('\n','<br>'),'',f'font-size:{size}px;color:{color};font-weight:{weight};line-height:{lh}'),x,y,w)
def ph(x,y,w,h):return pos('',x,y,w,h,'ph')
def panel(x,y,w,h,body='',on=False,gray=False):return pos(body,x,y,w,h,'panel '+('on' if on else 'gray' if gray else ''))
def corner(x,y,w,h,body='',on=False,gray=False):return pos(body,x,y,w,h,'corner '+('on' if on else 'gray' if gray else ''))
def local(s,x,y,w,size=18,color='#222',weight=400):return tx(s,x,y,w,size,color,weight)
def paras(n=3):return '<br>'.join(['핵심 기술과 고객의 요구를 연결하여 새로운 가치를 만듭니다.','효율적인 운영과 차별화된 서비스를 통해 지속 성장합니다.','시장 변화에 빠르게 대응하고 고객과 함께 발전합니다.'][:n])
def donut(v,c=B):return f'<div class="donut" style="background:conic-gradient({c} {v}%,#b9babc 0)"><div>{v}%</div></div>'
def bars(vals,labels=None,w=800,h=300):
 labels=labels or [str(2020+i) for i in range(len(vals))]
 return '<div class="r-bars">'+''.join(f'<div><b style="bottom:{v/max(vals)*65}%">{v:,}</b><i style="height:{v/max(vals)*82}%"></i><span>{lb}</span></div>' for v,lb in zip(vals,labels))+'</div>'
def line(vals,w=600,h=250,area=False):
 pts=[(30+i*(w-60)/(len(vals)-1),h-30-v/max(vals)*(h-65)) for i,v in enumerate(vals)]
 svg=f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><path d="M30 20V{h-30}H{w-10}" fill="none" stroke="#bbb"/>'
 if area:svg+=f'<polygon points="30,{h-30} '+ ' '.join(f'{x},{y}' for x,y in pts)+f' {w-30},{h-30}" fill="#a9c7f0"/>'
 svg+='<polyline points="'+' '.join(f'{x},{y}' for x,y in pts)+f'" fill="none" stroke="{B}" stroke-width="2"/>'
 for i,((x,y),v) in enumerate(zip(pts,vals)):svg+=f'<circle cx="{x}" cy="{y}" r="3" fill="{B}"/><text x="{x}" y="{y-12}" fill="#777" font-size="12" text-anchor="middle">{v}</text><text x="{x}" y="{h-7}" fill="#777" font-size="12" text-anchor="middle">{2020+i}</text>'
 return svg+'</svg>'
def base(i):
 title=titles[i-1]; cut={3:1,5:1,6:1,7:11,13:1,14:1,19:1,20:7}.get(i,len(title.split(' ')[0]));t='<b>'+title[:cut]+'</b>'+title[cut:]
 return tx(t,76,54,1120,56,'#222',500,1.1)+tx(notes[i-1],76,138,1050,13,'#737679',400,1.4)+tx('Miricompany Investor Relations Deck',76,676,600,10,'#adb0b3')+tx(str(i),1210,676,25,10,'#adb0b3')
pages={}
# 1
pages[1]=tx('◼ MIRI COMPANY',76,70,400,16,'#222',700)+tx('MIRICOMPANY',76,125,1100,104,B,800,1)+pos('IR DECK.',76,239,530,130,'cover-title')+tx('빠른 투자 유치를 위한 IR 문서',76,391,650,20,'#747474')+tx('성공 기업의 가능성 MIRI\nContact ir | miri@miricompany.com',76,603,500,14,'#777')+ph(690,237,590,483)
# 2
p=base(2)+ph(76,394,260,220)
for k in range(2):
 items=['회사소개','문제점','솔루션','시장 규모','자사 서비스'] if k==0 else ['비즈니스 모델','경쟁 우위','성장 전략','팀 소개','투자 유치 계획']
 content=''.join(pos(f'<span>{j+1+k*5:02}</span>　{a}',38,45+j*66,295,48,'agenda-line') for j,a in enumerate(items))
 p+=panel(462+k*385,250,360,410,content,on=False)
pages[2]=p
# 3
pages[3]=base(3)+panel(76,229,660,390,tx('비전을 현실로 만드는 리더, CEO 김미리입니다.',20,50,620,24)+tx(paras(3)+'<br><br>'+paras(3),32,135,600,15,'#666'))+tx('대표이사\n김미리',775,278,170,18,'#888')+ph(835,70,420,650)
#4
pages[4]=tx('Vision & Mission',76,54,1000,56,'white',500)+tx('회사의 핵심 비전과 미션에 대해 간결하고 명확하게 작성해 주세요.\n우리가 만들어갈 미래와 고객에게 제공하는 가치를 보여줍니다.',76,138,1000,13,'#a9bfd9')+tx('회사가 궁극적으로 만들고 싶은 미래상을 압축한\n슬로건을 여기에 입력해 주세요.',170,320,940,38,'#96afd2',400,1.6)+tx('MIRI COMPANY',550,485,300,18,'white',700)+ph(76,560,1128,160)
# 5-6 cards
p=base(5)
for k in range(3):
 p+=corner(76+k*380,250,360,386,tx('Pain Point 0'+str(k+1),42,36,270,22, 'white' if k<2 else '#222')+pos('<span class="simple-icon">'+['<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2"><path d="M2 7 6 3l5 2 4-2 7 5-4 11-3 2-7-7-3 2-3-9Zm4 4 5-6m-2 8 6 6m-3-9 6 6M4 9l4 4"/></svg>','<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2"><path d="M10 5h12M10 12h12M10 19h12"/><path d="M2 2h4v4H2zM2 9h4v4H2zM2 16h4v4H2z"/></svg>','<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2"><circle cx="12" cy="12" r="4"/><path d="m9 2 6 0 1 3 3 1 3 3-2 3 2 3-3 3-3 1-1 3H9l-1-3-3-1-3-3 2-3-2-3 3-3 3-1Z"/></svg>'][k]+'</span>',42,170,90,90)+tx(paras(2),42,278,278,14,'white' if k<2 else '#777'),k==0,k==1)
pages[5]=p
p=base(6)
for k in range(4):
 p+=corner(76+k*287,250,273,386,tx(f'PROCESS {k+1}',32,20,220,16,'white' if k==0 else B,700)+pos('<div class="arrow"></div>',32,64,210,1)+tx(['문제 정의\n및 솔루션 제안','핵심 솔루션의\n기술 실행','핵심 솔루션\n검증 구축','성과 측정 및\n모니터링 제공'][k],32,180,220,22,'white' if k==0 else '#222',500)+tx(paras(2),32,275,220,13,'white' if k==0 else '#777'),k==0)
pages[6]=p
#7 polygon inclusion
p=base(7)+panel(76,240,420,400,tx('이 시장은 00% 성장하는\n00조 원의 기회가 있습니다.',32,44,355,25)+tx('20M+　 TAM 전체 시장\n\n18M+　 SAM 유효 시장\n\n9M+　 SOM 목표 시장',32,158,355,24,B))
for x,y,w,h,col,label in [(650,28,640,610,'#afc9ee','TAM'),(760,149,420,391,'#5e99e6','SAM'),(855,269,230,177,B,'SOM')]:p+=pos(f'<span>{label}<small>시장의 규모</small></span>',x,y,w,h,'pent '+('light' if col!=B else '')) .replace('class="pent','style-x="'+col+'" class="pent',1) if False else pos(f'<span>{label}<small>시장의 규모</small></span>',x,y,w,h,'pent').replace('height:'+str(h)+'px;','height:'+str(h)+'px;background:'+col+';')
pages[7]=p
#8
p=base(8)+panel(76,240,400,400,tx('시장은 [성장 원인]에 의해 더욱\n빠르게 확장하고 있습니다.',32,48,340,24)+tx(paras(3)+'<br><br>'+paras(2),32,153,340,16,'#888'))
for k,(lab,val) in enumerate([('SOM','500B'),('SAM','50T'),('TAM','500T')]):
 p+=pos(f'<span>{val}<small>{lab} 전체 시장</small></span>',530+k*175,460-k*155,260+k*90,220+k*90,'pent').replace('height:'+str(220+k*90)+'px;','height:'+str(220+k*90)+'px;background:'+['#0066cf','#5e99e6','#afc9ee'][k]+';')
pages[8]=p
#9
p=base(9)+ph(390,283,500,345)
for k in range(6):
 x=76 if k<3 else 956;y=235+(k%3)*133
 p+=corner(x,y,290,58,tx(f'{k+1}. 차별화된 기술력' if k!=1 else '2. 차별화된 사용자 경험',15,14,260,16,'white',600),k<3,k>=3)+tx(paras(1),x+10,y+65,272,12,'#888')
pages[9]=p
#10
p=base(10)+ph(1000,236,170,160)
for k in range(4):
 x=76+k*290;y=224+(k%2)*113;p+=pos(tx(str(k+1),115,20,30,20,'white',700)+tx(['핵심','확장','잠재적','부가'][k]+'\n수익 모델',45,98,190,24,'white' if k==0 else '#222',600)+tx(paras(1),45,180,185,12,'white' if k==0 else '#888'),x,y,270,290,'pent '+('blue' if k==0 else 'white'))
pages[10]=p
#11
p=base(11)
for k in range(3):
 p+=corner(76+k*380,250,360,386,tx(f'Model {k+1} ⌄',36,20,280,22,'white' if k==0 else B)+tx(['구독료 (SaaS)','중개 수수료','기타 부가 수익'][k],36,132,280,25,'white' if k==0 else '#222')+tx(paras(1),36,183,280,15,'white' if k==0 else '#777')+tx('Basic Plan: 월 300만 원\n\nPro Plan: 월 500만 원',36,258,280,16,'white' if k==0 else '#777'),k==0)
pages[11]=p
#12
p=base(12)+panel(76,218,720,430,tx('수익 모델의 핵심을 한줄로 설명해주세요.',30,35,650,25,B))+panel(815,218,389,430,tx('매출 전망 00% 성장',30,35,330,22,B)+pos(line([18,39,58,72,100],330,280,True),20,110,330,280))
for k,v in enumerate([50,30,20]):p+=pos(donut(v),110+k*220,360,180,180)+tx('수익원 '+str(k+1),135+k*220,555,160,22)+tx('고객의 성장을 위한 가치\n핵심 매출 창출 전략',125+k*220,591,175,13,'#777')
pages[12]=p
#13
p=base(13)
for k,(v,lb) in enumerate([('1200','누적 판매량'),('40%','성장률'),('60M','확보한 매출'),('35%','기술 차별화')]):p+=corner(76+k*282,240,274,92,tx(v,20,14,190,42,'white' if k==0 else '#999',600)+tx(lb,130,28,130,14,'white' if k==0 else '#999'),k==0)
p+=panel(76,340,1128,320,tx('누적 판매량 000만 개\n전년 대비 00% 성장',35,25,650,23,B)+pos(bars([200,400,600,700,900,1200]),25,78,1080,230));pages[13]=p
#14
p=base(14)
for k in range(3):
 content=tx(['MRR·월간 반복 매출','GMV·총 거래액','ARPU·고객당 평균 수익'][k]+'\n전년도 대비 00% 성장',30,30,300,23,B)+pos(line([12,25,38,53,80],300,250,k==1) if k<2 else bars([20,35,60,90]),30,135,300,245)+tx('● Model 1　● Model 2',40,390,270,13,B)
 p+=panel(76+k*380,215,360,433,content)
pages[14]=p
#15
p=base(15)+panel(76,245,710,415)+panel(805,245,399,415,tx('경쟁사 대비\n우리의 명확한 차별점',30,32,345,25,B)+tx(paras(3)+'<br><br>'+paras(3),30,120,340,16,'#888'))
p+=pos('<div class="cross"></div>',76,245,710,415)
for k,(x,y,name) in enumerate([(195,350,'company'),(330,390,'MIRI company'),(500,390,'MIRI company'),(630,340,'MIRI COMPANY'),(195,560,'MIRI company'),(340,545,'MIRI company'),(550,530,'company')]):p+=pos(name,x-48,y-48,96,96,'bubble '+('blue' if k==3 else ''))
pages[15]=p
#16
p=base(16)+panel(76,215,480,420,tx('MIRICOMPANY',135,25,310,24,B))+panel(720,215,484,420,tx('COMPANY',135,25,310,24,'#555'))+pos('VS',574,240,128,420,'vs')
for k in range(4):
 y=366+k*78;p+=pos('<span>00%</span>',106,y,420,54,'hbar blue')+pos('<span>00%</span>',750,y,[210,270,240,120][k],54,'hbar gray')+tx('OPTION '+str(k+1),592,y+18,100,14,'white')
pages[16]=p
#17
p=base(17)
for k in range(4):
 x=76+k*282;y=392-k*57;p+=tx('PHASE '+str(k+1),x+30,y-45,210,20,B if k==0 else '#aaa')+pos(tx(['~2026','~2027','~2028','~2029'][k],30,18,220,25,'white' if k<3 else '#222',500)+tx(['국내 시장 선점','아시아 시장 진출','글로벌 리더십 확보','글로벌 시장 진출'][k],30,58,220,22,'white' if k<3 else '#222'),x,y,280,110,'chev '+('blue' if k==0 else 'gray' if k<3 else 'white'))+tx(paras(3),x+15,y+127,245,14,'#999')
pages[17]=p
#18
p=base(18)+ph(864,245,416,440)
for k in range(3):
 x=76+k*260;p+=pos(['사업 시스템','핵심 설계 시스템','분산 시스템'][k],x,240,225,64,'chev '+('blue' if k==0 else 'gray'))+panel(x,320,225,310,tx(['기술 아키텍처','분산 시스템\n그래프 알고리즘','데이터 처리\n프로토콜'][k],25,80,180,22,'#777')+tx(paras(1),25,190,180,13,'#999'))
pages[18]=p
#19
p=base(19)
for k in range(5):
 x=76+k*228;p+=ph(x,240,215,175)+panel(x,420,215,220,tx(['CEO','Engineer','Developer','Marketer','Marketer'][k],25,15,170,15,'white' if k==0 else B)+tx(['김미리','최미리','이미리','조미리','강미리'][k],25,45,170,28,'white' if k==0 else '#555')+tx(paras(2),25,107,170,13,'white' if k==0 else '#888'),k==0)
pages[19]=p
#20
p=base(20)+panel(76,218,720,430)+panel(815,218,389,430,tx('5개년 매출 목표: 60% 성장',25,25,340,23,B)+pos(bars([200,320,420,560,720]),25,100,340,285))
p+=pos('<div class="multi-donut"><span>투자유치 목표<br><b>000억 원</b></span></div>',110,270,360,350)+tx('투자 유치 목표',510,270,250,23)+tx('000억 원',510,310,250,39,B)+tx('자금 사용 계획',510,385,250,25)+tx('제품 개발: 30%\n\n기술 고도화: 30%\n\n글로벌 확장: 40%',510,440,250,18,'#999');pages[20]=p
#21
p=base(21)+pos('<div class="arrow"></div>',76,253,1128,1)
for k in range(4):
 p+=tx(f'0{k+1}\n'+['THE ASK','USE OF FUNDS','NEXT-LEVEL','GROWTH'][k],76+k*287,269,260,18,B,600)+corner(76+k*287,360,273,273,tx(['투자금\n매출 규모와 숫자','R&D & 마케팅\n인재 영입 투자','제품 고도화\n고객 확보','매출 성장\n기업 가치 증대'][k],30,130,220,21,'white' if k==0 else '#222')+tx(paras(1),30,215,220,12,'white' if k==0 else '#777'),k==0)
pages[21]=p
css='''.agenda-line{font-size:22px;border-bottom:1px solid #ddd;padding-bottom:22px}.agenda-line>span{color:#0066cf;font-size:26px}.corner:after{content:'';position:absolute;bottom:22px;left:34px;right:34px;border-bottom:1px solid #aaa}body:has(.cover-title){background:white}body:has(.cover-title) main{background:white}*{box-sizing:border-box}html,body{margin:0;width:1280px;height:720px;overflow:hidden}body{font-family:'Pretendard Variable',sans-serif;background:#f0f1f2;color:#222}body>main{width:1280px;height:720px;position:relative;overflow:hidden}div{position:absolute}div div{position:relative}main>div{position:absolute}.panel>div,.corner>div,.pent>div{position:absolute}b{color:#0066cf;font-weight:600}.cover-title{background:#0066cf;color:white;font-size:104px;font-weight:800;padding:5px 12px;line-height:1.05;clip-path:polygon(0 0,91% 0,100% 33%,100% 100%,0 100%)}.ph{background:#e2e3e4}.panel{background:white;border-top:9px solid #0066cf}.panel:before{content:'';position:absolute;top:0;left:0;border-top:48px solid #0066cf;border-right:48px solid transparent}.panel.on,.corner.on{background:#0066cf;color:white}.panel.gray,.corner.gray{background:#5e5e5e;color:white}.corner{background:white;clip-path:polygon(0 0,82% 0,100% 18%,100% 100%,0 100%)}.simple-icon{display:flex;width:83px;height:83px;align-items:center;justify-content:center;border-radius:50%;background:white;color:#0066cf;font-size:48px}.arrow{width:100%;height:1px;background:#7ea1b8;position:relative}.arrow:after{content:'';position:absolute;right:0;top:-5px;border-left:8px solid #4f7e96;border-top:5px solid transparent;border-bottom:5px solid transparent}.pent{clip-path:polygon(50% 0,100% 38%,81% 100%,19% 100%,0 38%);background:white;text-align:center}.pent>span{position:absolute;top:72%;left:15%;width:70%;font-size:28px;color:white}.pent small{display:block;font-size:13px;margin-top:10px}.pent.blue{background:#0066cf}.pent.white{background:white}.blue{background:#0066cf;color:white}.gray{background:#5e5e5e;color:white}.white{background:white}.donut{width:180px;height:180px;border-radius:50%;display:flex;align-items:center;justify-content:center}.donut>div{width:153px;height:153px;border-radius:50%;background:white;display:flex;align-items:center;justify-content:center;font-size:44px;color:#70a5d6}.r-bars{position:relative!important;width:100%;height:100%;display:flex;align-items:flex-end;gap:10px;border-bottom:1px solid #bbb;padding-bottom:24px}.r-bars>div{position:relative;width:100%;height:100%;display:flex;align-items:center;justify-content:flex-end;flex-direction:column}.r-bars i{background:#609be6;width:100%;display:block}.r-bars b{position:absolute;bottom:35%;color:white;font-size:24px;font-weight:400}.r-bars span{position:absolute;bottom:-20px;color:#999;font-size:12px}.bubble{border-radius:50%;background:#eee;font-size:10px;color:#555;display:flex;justify-content:center;align-items:center}.bubble.blue{background:#99c5f1;color:#0066cf}.cross{width:100%;height:100%;background:linear-gradient(transparent calc(50% - .5px),#eee 0, #eee calc(50% + .5px),transparent 0),linear-gradient(90deg,transparent calc(50% - .5px),#eee 0, #eee calc(50% + .5px),transparent 0)}.vs{background:#555;color:white;text-align:center;padding-top:45px;font-size:28px}.hbar span{position:absolute;right:10px;top:16px;color:white;font-size:15px}.chev{clip-path:polygon(0 0,90% 0,100% 50%,90% 100%,0 100%);padding:20px;text-align:center;font-size:20px}.chev>div{position:absolute}.multi-donut{width:350px;height:350px;border-radius:50%;background:conic-gradient(#003a82 40%,#0066cf 0 70%,#68a3e8 0 90%,#a6cbed 0);display:flex;align-items:center;justify-content:center}.multi-donut span{background:white;border-radius:50%;width:135px;height:135px;display:flex;align-items:center;justify-content:center;flex-direction:column;text-align:center;font-size:15px}'''
(R/'replica/replica.css').write_text(css)
for i,body in pages.items():
 html=f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><link rel="stylesheet" href="../../fonts/fonts.css"><link rel="stylesheet" href="replica.css"></head><body'+(' style="background:#07428d"' if i==4 else ' style="background:white"' if i==1 else '')+f'><main>{body}</main></body></html>'
 (R/f'replica/slide_{i:02}.html').write_text(html)
(R/'page-data.json').write_text(json.dumps(dict(titles=titles,notes=notes),ensure_ascii=False,indent=2))
rows=['# 067 이미지 전체 목록\n','|원본|페이지 유형|계약 대응|','|---|---|---|']
contracts=['foundation cover, image-frame','agenda','prose, person, headline','headline, quote','card','steps, card','concentric, metric','concentric, prose','image-frame, card','pyramid, card','pricing, card','chart-donut, chart-area','metric, chart-bar','chart-line, chart-area, chart-bar','positioning, list','versus, gauge','roadmap, steps','architecture, image-frame','person','chart-donut, chart-bar, list','steps, card']
for i,t in enumerate(titles):rows.append(f'|slide_{i+1:02}.png|{t}|{contracts[i]}|')
(R/'inventory.md').write_text('\n'.join(rows)+'\n\n원본 21장, 모두 1280×720. 복잡한 기계·인물·세계지도 이미지는 연회색 자리로 대체. 나머지 요소는 아래 디자인 언어에 따라 확장.\n')
print('replica sources',len(pages))
