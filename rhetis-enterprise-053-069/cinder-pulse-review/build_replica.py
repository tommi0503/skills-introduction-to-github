from pathlib import Path
import json,html
BASE=Path(__file__).parent
OUT=BASE/'replica';OUT.mkdir(exist_ok=True)
FONT='../fonts/fonts.css'
CSS='''*{box-sizing:border-box}html,body{margin:0;width:1280px;height:720px}body{font-family:'Pretendard Variable';color:#0a0a0a;font-weight:400}p,h1,h2,h3{margin:0} .slide{position:relative;width:1280px;height:720px;overflow:hidden;background:#30302f}.box{position:absolute;background:#fff;border-radius:11px}.text{position:absolute;white-space:normal;line-height:1.45}.soft{background:#f0f0f0;border:1px solid #dadada;border-radius:8px}.accent{color:#ff3e0c}.bar{background:#ff3e0c}.cap{border-radius:999px}.seat{background:#e6e6e6;position:absolute;display:flex;align-items:center;justify-content:center;color:#999}.arrow{position:absolute;display:grid;place-items:center;background:#ff3e0c;border-radius:50%;font-size:48px}.arrow svg{width:65%;height:65%} .sig{font-family:'Nanum Pen';font-size:70px}.small{font-size:16px;color:#555}table{border-collapse:collapse;width:100%;font-size:16px;line-height:1.4}th{background:#ff3e0c;color:#0a0a0a;font-weight:600;padding:12px 5px}td{border-bottom:1px solid #bbb;padding:10px 5px}tbody tr:last-child td{background:#f0f0f0} .mark{display:flex;align-items:center;justify-content:center}.labeled{border-left:2px solid #ff3e0c;padding-left:10px}'''
S=[]
def box(x,y,w,h,extra='',content=''):return f'<div class="box {extra}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">{content}</div>'
def text(x,y,w,txt,size=20,color='',weight=400,line=1.45):return f'<div class="text" style="left:{x}px;top:{y}px;width:{w}px;font-size:{size}px;font-weight:{weight};line-height:{line};'+(f'color:{color};' if color else '')+f'">{txt}</div>'
def soft(x,y,w,h,txt='',sz=18):return box(x,y,w,h,'soft',text(20,18,w-40,txt,sz))
def pill(x,y,w,h,txt,fill='#ff3e0c',color='#fff',sz=18):return f'<div class="text cap mark" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{fill};color:{color};font-size:{sz}px;font-weight:600"><div style="text-align:center">{txt}</div></div>'
def arrow(x,y,sz=52):return f'<div class="arrow" style="left:{x}px;top:{y}px;width:{sz}px;height:{sz}px"><svg viewBox="0 0 48 48" fill="none" stroke="#161616" stroke-width="3"><path d="M9 9L38 38M10 38H38V10"/></svg></div>'
def part(part=1):return text(70,70,275,f'<div class="labeled"><span class="accent" style="font-size:16px">PART {part}.</span><br><b>{["우리는 어떤 회사인가","무엇을 하는가","어떻게 하는가","어디로 가는가"][part-1]}</b></div>',20)
def panel(title,partn=1,side=False,note=''):
 if side:return box(34,34,355,652)+box(400,34,846,652)+part(partn)+text(80,167,270,title,42,'#080808',400,1.3)+text(80,549,270,note,21,'#555',500)
 return box(34,34,1212,123)+box(34,167,1212,519)+part(partn)+text(370,73,820,title,42,'#080808',400,1.25)
def logo(x,y):return f'<div style="position:absolute;left:{x}px;top:{y}px;width:30px;height:30px;border-radius:50%;background:repeating-linear-gradient(0deg,#ff3e0c 0 1px,transparent 1px 3px)"></div>'+text(x+38,y+2,230,'MIRI Company',18,'#fff',700)
def caps(positions,color='#484847',width=112):return ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:{width}px;height:{h}px;background:{color if i<len(positions)-1 else "#ff3e0c"};border-radius:999px"></div>' for i,(x,y,h) in enumerate(positions))
def table(x,y,w,heads,rows,sz=16):return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px"><table style="font-size:{sz}px"><thead><tr>'+''.join(f'<th>{h}</th>' for h in heads)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{v}</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table></div>'
def bullets(lines):return '<br>'.join('· '+l for l in lines)
# 01
s=logo(60,45)+text(60,151,560,'<span class="accent">다이어그램 중심</span><br>회사소개서',72,'#fff',300,1.2)+text(60,346,480,'이 프레젠테이션은 다양한 다이어그램을 활용해<br>회사를 소개하는 회사소개서입니다.',20,'#fff')+text(60,604,360,'<div class="labeled">2080.10.22<br>경영기획팀 김미리 과장</div>',16,'#fff')
for i,(x,y,h) in enumerate([(629,153,500),(749,60,500),(869,160,500),(989,100,500),(1109,152,500)]):s+=f'<div class="seat cap" style="left:{x}px;top:{y}px;width:111px;height:{h}px"></div>'
s+=arrow(1117,548,94);S.append(s)
#02
s=text(60,68,500,'Contents',72,'#fff',300)+text(68,151,300,'목차',36,'#fff',300)+caps([(-15,412,290),(65,331,290),(144,381,290),(223,279,290),(302,341,290)],width=74)
ag=[('우리는 어떤 회사인가',['미리컴퍼니 미션과 비전','대표 인사말','일반 현황','미리컴퍼니 연혁','미리컴퍼니 조직 구성','성장 단계']),('무엇을 하는가',['미리컴퍼니 사업 영역','사업 간 시너지','미리컴퍼니 주력 사업','제품·서비스 라인업']),('어떻게 하는가',['프로젝트 일정','핵심 경쟁력','고객사와 파트너십','목차 키워드 입력','목차 키워드 입력']),('어디로 가는가',['성장 전략','오시는 길 / 문의'])]
for i,(name,ls) in enumerate(ag):
 x=588+(i%2)*325;y=57+(i//2)*311;s+=box(x,y,310,296)+text(x+21,y+28,265,f'<div class="labeled"><span class="accent" style="font-size:16px">PART {i+1}.</span><br><b>{name}</b></div>',24)+text(x+32,y+107,260,bullets(ls),18,'#111',400,1.6)
S.append(s)
#03
s=pill(60,57,157,44,'PART 1','#f0f0f0','#000',22)+text(60,151,600,'우리는<br><span class="accent">어떤 회사</span>인가?',72,'#fff',300,1.2)+arrow(60,371)+text(132,371,500,'인공지능 기반 데이터 솔루션으로 기업의<br>디지털 혁신을 선도하는 미리컴퍼니입니다.',20,'#fff')+caps([(629,614,440),(749,475,440),(869,336,440),(989,196,440),(1109,57,440)]);S.append(s)
#04
s=panel('미션과 비전,<br>핵심 가치',side=True,note='미션과 비전이 겹치는 지점에<br>우리가 지키는 원칙이 있습니다.')
s+='<svg style="position:absolute;left:455px;top:83px" width="736" height="422"><circle cx="211" cy="211" r="210" fill="#f0f0f0" stroke="#ddd"/><circle cx="525" cy="211" r="210" fill="#f0f0f0" stroke="#ddd"/><path d="M368 72 A210 210 0 0 1 368 350 A210 210 0 0 1 368 72" fill="#ff3e0c"/></svg>'
s+=text(490,229,244,'MISSION',28,weight=600)+text(496,270,240,'- 데이터에 숨겨진 가치를<br>발견하여 인류의 일상을 혁신<br>- 복잡한 비즈니스 문제를 AI 기술로<br>명쾌하게 해결하는 큰 가치 제공',16,'#555')+text(780,263,86,'CORE<br>VALUE',28,weight=600,line=1.1)+text(955,229,224,'VISION',28,weight=600)+text(918,270,260,'- 아시아 최고의 엔터프라이즈<br>AI 데이터 플랫폼 기업으로 도약<br>- 2030년까지 Global Unicorn<br>AI Enterprise 진입',16,'#555')+box(437,550,772,98,'soft')
for i,(a,b) in enumerate([('기술 우위','Technological Excellence'),('고객 중심','Customer First'),('지속 가능한 혁신','Sustainable Innovation')]):s+=text(455+i*250,578,236,a,18)+text(455+i*250,605,236,b,16,'#555')
s+='<svg style="position:absolute;left:822px;top:369px" width="2" height="182"><path d="M1 0V182" stroke="#111" stroke-dasharray="2 2"/></svg>';S.append(s)
#05
s=panel('미리컴퍼니<br>대표 인사말',side=True)+f'<div class="seat" style="left:70px;top:357px;width:283px;height:283px;border-radius:50%"></div>'+text(127,654,200,'*페이지 내 인물사진은 샘플이미지입니다.',10,'#666')+text(468,98,720,'고객사와의 <span class="accent">장기적인 신뢰 관계</span>를<br>최우선 가치로 생각합니다',34,'#555',500,1.4)+text(468,253,720,'안녕하십니까, 미리컴퍼니 대표 김미리입니다.<br><br>미리컴퍼니는 2018년, 데이터를 통해 세상의 모든 기업이 더 똑똑하게 일할 수 있도록 돕겠다는 작은 꿈에서 출발했습니다. 지난 8년간 끝없는 기술 도전과 연구개발을 거쳐,<br>이제는 국내외 200여 개 주요 기업의 디지털 전환을 책임지는 데이터 솔루션 리더로<br>성장하였습니다.<br><br>우리는 단기적인 수익보다 고객사와의 장기적인 신뢰 관계를 최우선 가치로 생각합니다.<br>최첨단 AI 기술력과 철저한 사후 관리를 바탕으로, 고객의 성공이 곧 미리컴퍼니의 성장이라는 약속을 반드시 지켜나가겠습니다.',18,'#555',400,1.38)+text(468,575,260,'미리컴퍼니 대표이사　<b style="font-size:24px">김미리</b>',16)+text(680,552,200,'<span class="sig">김미리</span>',60);S.append(s)
#06
org=[['경영진','CEO / COO / CTO / CPO / CFO /<br>해외사업 총괄','6명','경영 전략·사업·기술·제품·재무 총괄'],['사업전략본부','사업기획팀 / 국내사업팀 / 글로벌사업팀','28명','사업 전략 수립·국내외 사업 개발'],['AI·데이터본부','AI모델링팀 / 데이터 엔지니어링팀 /<br>데이터 분석팀 / AI Research','52명','AI 모델 개발·데이터 분석·연구'],['제품개발본부','Product Manager / 프론트엔드 /<br>백엔드 / Cloud·DevOps / QA','45명','제품 기획·개발·품질 관리'],['디자인·CX본부','Product Design / UX Research /<br>CX 운영','19명','UX·UI 설계·고객 경험 개선'],['마케팅·세일즈본부','B2B Sales / 브랜드 마케팅 / 글로벌 마케팅','18명','고객 확보·브랜드·글로벌 마케팅'],['경영지원본부','재무·회계 / HR / 법무·총무','12명','재무·인사·법무·조직 운영'],['합계','','180명','국내 본사·R&D 센터·해외 지사 포함']]
fin=[['매출액','320억 원','390억 원','450억 원'],['영업이익','38억 원','47억 원','62억 원'],['영업이익률','11.9%','12.1%','13.8%'],['당기순이익','27억 원','34억 원','46억 원'],['유동자산','145억 원','183억 원','215억 원'],['부채','82억 원','96억 원','108억 원'],['자기자본','118억 원','151억 원','193억 원']]
s=panel('조직구성 및 재무현황')+text(70,203,670,'<div style="text-align:center;background:#ff3e0c;border-radius:7px 7px 0 0;padding:9px">조직 구성</div>',22,weight=600)+table(70,247,670,[],org,14)+text(760,203,450,'<div style="text-align:center;background:#ff3e0c;border-radius:7px 7px 0 0;padding:9px">재무 현황</div>',22,weight=600)+table(760,247,450,['구분','2024','2025','2026 예상'],fin,16);S.append(s)
#07
s=panel('회사 연혁')+'<div style="position:absolute;left:70px;top:282px;width:1140px;height:6px;background:#ff3e0c"></div>'
for i,(yr,name,ls) in enumerate([('2058','설립기',['미리컴퍼니 법인 설립','MiriData v1.0 출시','이곳에 핵심 내용을 입력해주세요.']),('2060','성장기',['시리즈 A 50억 원 투자 유치','임직원 50명 돌파','미리 R&D 센터 개소','기업용 데이터 솔루션 사업 본격 확대']),('2062','성과 창출',['MiriAI 출시','주요 보안 인증 취득','주요 기업 고객 50개사 확보','이곳에 핵심 내용을 입력해주세요.']),('2064 - 현재','목표 달성',['시리즈 B 150억 원 투자 유치','누적 매출 400억 원 돌파','해외 법인 설립','글로벌 사업 본격화','국내 중심 사업 구조에서 해외 시장까지 사업 영역 확대'])]):
 x=70+i*285;s+=pill(x+100,204,85 if i<3 else 132,54,yr)+f'<div style="position:absolute;left:{x+131}px;top:273px;width:24px;height:24px;border:5px solid #ff3e0c;border-radius:50%;background:#fff"></div>'+text(x+20,329,244,f'<div style="text-align:center">{name}</div>',22)+text(x+28,371,245,bullets(ls),16,'#555',400,1.65)
s+=soft(70,567,1139,82,'<div style="text-align:center">지금까지 쌓아온 경험과 혁신을 바탕으로, 앞으로도 여러분과 함께 더 큰 미래를 만들어 나가겠습니다.</div>',23);S.append(s)
#08
s=panel('조직문화와<br>인재상',side=True,note='전문성을 기반으로 자율적으로<br>실행하고, 협업을 통해 성과를<br>만드는 조직을 지향합니다.')+'<svg style="position:absolute;left:450px;top:80px" width="750" height="570"><path d="M370 90L600 260L525 500L220 500L130 260Z" fill="none" stroke="#999" stroke-dasharray="6 4"/><path d="M370 193L478 271L437 398H303L262 271Z" fill="#ff3e0c"/></svg>'+text(764,355,120,'MIRI<br>PEOPLE',28,weight=600,line=1.2)
for x,y,name,ls in [(739,89,'AUTONOMY',['자율과 책임','스스로 판단하고 실행','맡은 업무의 결과까지 책임']),(965,253,'CURIOSITY',['끊임없는 탐구','WHY에서 시작하는 문제 해결','새로운 기술에 대한 지속적 학습']),(878,519,'SYNERGY',['집단지성 시너지','서로 다른 전문성을 연결','정보와 경험을 적극적으로 공유']),(598,519,'EXECUTION',['빠른 실행','아이디어를 신속하게 실행','실행 결과를 데이터로 검증']),(512,253,'GROWTH',['함께 성장','피드백을 통한 지속적인 개선','개인의 성장을 통한 조직성장'])]:
 s+=box(x,y,161,39,'soft',text(0,5,161,f'<div style="text-align:center">{name}</div>',22))+text(x-40,y+49,241,f'<div style="text-align:center">{bullets(ls)}</div>',16,'#555')
S.append(s)
#09
s=panel('성장 단계와 현재 위치')
for i,(yr,name,ls) in enumerate([('2058~2059','창업기',['AI데이터 엔진 알고리즘 개발','초기 금융권 고객 5개사 확보']),('2060~2062','성장기',['연 매출 150억 원 달성','R&D 중심 연구소 확충','전문 인력 채용 확대','조직 규모 100명으로 성장']),('2063~현재','확장기',['글로벌 SaaS 시장 진출','해외 사업 기반 확대','파트너 네트워크 150개 구축']),('2067~','성숙기',['글로벌 Enterprise AI 확립','글로벌 매출 비중 50% 달성','안정적인 글로벌 수익 구조','IPO 추진'])]):
 x=78+i*297;y=254-i*16;h=280+i*16;s+=box(x,y,232,h,'soft')+text(x+10,y+17,212,f'<div style="text-align:center">STAGE {i+1}</div>',16,weight=600)+f'<div class="bar" style="position:absolute;left:{x+14}px;top:{y+39}px;width:204px;height:17px"></div>'+text(x+10,y+76,212,f'<div style="text-align:center">{yr}</div>',18,'#555')+text(x+10,y+121,212,f'<div style="text-align:center">{name}</div>',22)+text(x+22,y+172,194,bullets(ls),16,'#555')
 if i<3:s+='<svg style="position:absolute;left:'+str(x+257)+'px;top:'+str(363-i*15)+'px" width="24" height="30"><path d="M3 3L15 15L3 27" stroke="#ff3e0c" stroke-width="6" fill="none"/></svg>'
s+=soft(70,552,1140,95,'<div style="text-align:center">현재 우리는 STAGE 3 · 확장기에 있습니다.<br>기술과 고객 기반을 바탕으로 글로벌 시장 확장을 본격화하는 단계</div>',23);S.append(s)
#10
s=panel('사업 성과<br>한눈에 보기',2,True,'사업 성과에 대한 설명을 적어주세요. 차트와 표 형식을 이용하면 한눈에 보기 쉽습니다.')+text(437,76,700,'연도별 성장 추이 콤보차트',22)
pts=[]
for i,v in enumerate([28,65,140,248,380,450]):
 x=492+i*121;y=303-v*.35;s+=f'<div style="position:absolute;left:{x}px;top:{y}px;width:80px;height:{v*.35}px;background:#a2a2a2"></div>'+text(x+3,307,80,str(2060+i),14)
for j,v in enumerate([0,100,200,300,400,500]):s+=text(445,294-j*35,30,str(v),12,'#555')+f'<div style="position:absolute;left:472px;top:{303-j*35}px;width:729px;border-top:1px dotted #ccc"></div>'
s+='<svg style="position:absolute;left:472px;top:125px" width="730" height="180"><polyline points="60,156 181,147 302,150 423,144 544,110 665,86" fill="none" stroke="#ff3e0c" stroke-width="2"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="#ff3e0c"/>' for x,y in [(60,156),(181,147),(302,150),(423,144),(544,110),(665,86)])+'</svg>'+text(742,342,300,'<span style="color:#999">●</span>매출(억·원) <span class="accent">●</span>재계약률(%)',14)+text(437,389,700,'사업 영역별 매출 비중 표',22)+table(437,427,772,['사업 영역','주요 서비스','매출 비중','고객사 수'],[['Miri Intelligence','AI 플랫폼·예측 솔루션','45%','120개사'],['Miri Cloud','SaaS·클라우드 스토리지','30%','85개사'],['DX Consulting','데이터 파이프라인·DX 자문','15%','32개사'],['M&O','24/7 유지보수·AI 튜닝','10%','210개사(유지)']],16);S.append(s)
#11
s=panel('사업 영역 한눈에 보기',2)+pill(543,278,197,197,'MIRI<br>COMPANY','#ff3e0c','#000',28)
for i,(name,ls) in enumerate([('사업 01 · Miri Intelligence',['AI PLATFORM','데이터 통합 수집','실시간 AI 예측','대규모 데이터 분석 자동화']),('사업 02 · Miri Cloud',['SaaS SERVICE','구독형 클라우드 기반','데이터 저장·관리·분석 환경을 통합 제공','Cloud Data Storage']),('사업 03 · DX Consulting',['ENTERPRISE CONSULTING','맞춤형 데이터 파이프라인 설계','DX 전략 및 실행 로드맵 자문','시스템 도입·전환 지원']),('사업 04 · Maintenance & Operation',['OPERATION SUPPORT','24/7 시스템 유지보수','성능 모니터링','지속적인 운영 최적화'])]):
 x=102+(i%2)*660;y=203+(i//2)*181;s+=soft(x,y,417,168,'<b style="color:#000">'+name+'</b><br><div style="margin-top:10px">'+bullets(ls)+'</div>',18)
s+=soft(70,570,1139,79,'<b class="accent">매출 비중</b>　Miri Intelligence · 45%　|　Miri Cloud · 30%　|　DX Consulting · 15%　|　Maintenance & Operation · 10%',21);S.append(s)
#12
s=panel('사업 간 시너지 구조',2)+'<svg style="position:absolute;left:100px;top:209px" width="465" height="438"><circle cx="232" cy="140" r="140" fill="#f0f0f0"/><circle cx="140" cy="298" r="140" fill="#c4c4c4"/><circle cx="324" cy="298" r="140" fill="#a1a1a1"/><path d="M232 190Q286 221 282 273Q232 288 182 273Q181 220 232 190" fill="#ff3e0c"/></svg>'+text(252,278,160,'Miri<br>Intelligence',22,weight=600)+text(174,502,150,'Miri<br>Cloud',22,weight=600)+text(411,502,140,'DX<br>Consulting',22,weight=600)+text(325,441,80,'D',18,weight=600)+text(241,394,80,'A',18,weight=600)+text(411,394,80,'C',18,weight=600)+text(325,540,80,'B',18,weight=600)+soft(615,204,594,349)
for i,(name,desc) in enumerate([('Miri Intelligence','독자 개발한 고성능 AI 예측 알고리즘 기술'),('Miri Cloud','대용량 데이터를 유연하게 처리하는 클라우드 인프라'),('DX Consulting','각 산업 분야별 도메인 전문성과기획 역량')]):s+=text(646,232+i*35,180,name,22,weight=500)+text(824,234+i*35,365,'|　'+desc,16,'#555')
for i,desc in enumerate(['클라우드 환경에서 즉시 동작하는 AI SaaS 모델 구축','기업 맞춤형 클라우드 데이터 파이프라인 구현','해당 교집합에 해당하는 내용을 적어주세요','고객 맞춤형 데이터 생태계 구축 및 자동화 완성']):s+=box(644,349+i*46,541,40,'',text(10,8,530,f'<b>● 교집합 {chr(65+i)}</b>　　　<span style="color:#555">{desc}</span>',16))
s+=soft(615,566,594,83,'<div style="text-align:center">사업은 나뉘어 있지만 역량은 하나로 모입니다.</div>',23);S.append(s)
#13
s=panel('미리컴퍼니<br>주력 사업',2,True,'사업 성과에 대한 설명을 적어주세요. 차트와 표 형식을 이용하면 한눈에 보기 쉽습니다.')
for i,(name,desc,serv,pr,cl) in enumerate([('Miri Intelligence','기업 내 유기적으로 흩어져 있는 비정형 데이터를 실시간으로 수집하고 분석하는 AI 솔루션입니다. 고도화된 예측 알고리즘을 통해 의사결정 시간을 70% 이상 단축시킵니다.','AI 데이터 분석, 실시간 이상 탐지, 미래 매출 예측 모델','180건','120개 사'),('Miri Cloud','초기 구축 비용 부담 없이 월 구독 형태로 이용할 수 있는 보안 특화 클라우드 플랫폼입니다. 엔터프라이즈급 보안 환경을 바탕으로 데이터 시각화 리포트를 제공합니다.','SaaS 데이터 스토리지, Auto-DashBoard, 데이터 암호화','95건','85개 사')]):
 y=72+i*295;s+=soft(437,y,772,281)+text(465,y+27,720,f'<span class="accent" style="font-size:18px">주력 사업 {i+1}.</span>　{name}',28,weight=500)+text(465,y+68,720,desc,18,'#555')+box(465,y+125,715,40,'',text(15,8,685,'<b>주요 서비스</b>　　　'+serv,17))+box(465,y+175,715,84)+pill(486,y+190,56,56,'<svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="currentColor" stroke-width="1"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="3"/><path d="M12 12L22 2M16 2H22V8"/></svg>','#c4c4c4','#fff',30)+text(560,y+203,180,'주요 성과',22)+text(778,y+190,150,f'<div style="text-align:center">프로젝트<br><b class="accent" style="font-size:28px">{pr}</b></div>',18)+text(1018,y+190,150,f'<div style="text-align:center">고객<br><b class="accent" style="font-size:28px">{cl}</b></div>',18)
S.append(s)
#14
s=panel('제품·서비스 라인업',2)
products=[('MiriData Engine',['초고속 실시간 데이터 수집·정제','대용량 데이터를 처리하는 데 최적화','엔터프라이즈 솔루션'],'대기업 데이터 조직'),('MiriAI Insights',['머신러닝 기반 비즈니스 지표 자동 예측','데이터 기반 의사결정 지원','전략 수립을 위한 인사이트 제공'],'전략기획팀·경영진'),('Miri Cloud Hub',['멀티 클라우드 환경의 데이터를','안전하게 통합·관리하는 데이터 저장소'],'IT 인프라·보안 관리팀'),('Miri BI Dashboard',['코딩 없이 Drag & Drop으로 완성하는 데이터 툴','성과 지표 모니터링','실시간 리포트 공유'],'마케팅·영업팀'),('Miri Security Shield',['AI 기반 개인정보·민감 데이터 자동 탐지 마스킹','보안이 중요한 데이터 환경에 특화','금융·의료 기관 중심'],'해당 키워드 입력'),('Miri Ops Agent',['데이터 파이프라인 자동화','24/7 운영 모니터링','반복 운영 업무 자동화'],'DevOps·데이터 엔지니어')]
for i,(name,ls,who) in enumerate(products):
 x=70+(i%3)*385;y=204+(i//3)*229;s+=soft(x,y,369,215)+text(x+29,y+28,320,f'<span class="accent">{i+1:02}</span> {name}',22,weight=500)+text(x+28,y+70,318,bullets(ls),16,'#555')+box(x+28,y+153,313,40,'',text(15,8,290,'<b>주요 고객</b>　　'+who,16))
S.append(s)
#15
s=panel('서비스 제공 프로세스',3)+pill(556,341,168,168,'고객 성공','#ff3e0c','#000',22)+'<svg style="position:absolute;left:474px;top:258px" width="330" height="330"><circle cx="165" cy="165" r="164" fill="none" stroke="#bbb"/></svg>'
stepls=[('문의·상담',['고객 요구사항 정의','도입 목적 및 핵심 과제 파악']),('분석·제안',['데이터 인프라 현황 진단','고객 환경에 맞춘 솔루션 제안']),('계약·설계',['최종 사업 범위 확정','PoC 실행 및 세부 일정 수립']),('제작·구축',['AI 모델링 개발 및 데이터 연동','실사용 환경 기준 성능 최적화']),('검수·납품',['시스템 최종 통합 테스트','보안 점검 및 사용자 교육 후 인도']),('운영·고도화',['24/7 장애 대응 및 주기적 AI 모델 재학습','개선 성과를 다음 과제 발굴로 연결'])]
for i,(name,ls) in enumerate(stepls):
 x=70 if i<3 else 886;y=204+(i%3)*155;s+=soft(x,y,324,133)+text(x+26,y+25,290,f'<span class="accent" style="font-size:18px">STEP {i+1}.</span>　{name}',22,weight=500)+text(x+25,y+65,280,bullets(ls),16,'#555')
for i,(x,y) in enumerate([(582,204),(724,286),(724,450),(582,532),(440,450),(440,286)]):s+=pill(x,y,116,116,'<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8H16M8 12H16M8 16H13"/></svg><br>'+stepls[i][0],'#f0f0f0','#000',18)
S.append(s)
#16
s=panel('표준 프로젝트<br>일정',3,True,'표준 소요 기간 14주<br>프로젝트 일정은 규모에 따라 조정됩니다.')+'<div style="position:absolute;left:601px;top:72px;height:575px;width:4px;background:#ff3e0c"></div>'
for i,(date,name,desc) in enumerate([('1~2주차','프로젝트 착수','프로젝트 킥오프 워크숍 진행 및 기본 데이터 및 요구사항 확정'),('3~4주차','프로젝트 설계','시스템 데이터 구조 설계 및 AI 알고리즘 모델링 기획안 확정'),('5~10주차','제작','데이터 파이프라인 구축, AI 학습 및 기능 개발 (중간보고회 개최)'),('11~12주차','검수','내부 QA 수행, 데이터 정확도 테스트 및 고객 피드백 반영'),('13~14주차','납품','최종 솔루션 운영 환경 이관, 사용자 매뉴얼 전달 및 인수인계')]):
 y=103+i*115;s+=pill(437,y,141,54,date)+pill(595,y+18,17,17,'')+text(628,y-4,550,name,23,weight=500)+text(628,y+35,550,desc,16,'#555')
S.append(s)
#17
s=panel('핵심 경쟁력의 선순환',3)+pill(544,330,192,192,'재계약률<br>94%','#ff3e0c','#000',28)+'<svg style="position:absolute;left:436px;top:222px" width="407" height="407"><circle cx="203" cy="203" r="202" stroke="#bbb" stroke-dasharray="6 4" fill="none"/></svg>'
for i,(name,desc,icon) in enumerate([('기술력','독자 개발 AI 특허 34건 보유<br>고도화된 데이터 처리 품질 확보','layers'),('전문 인력','석·박사급 전문 엔지니어 85명<br>안정적 기술의 전문 조직','user'),('사후 지원','24시간 실시간 모니터링<br>주기적인 AI 모델 업데이트','globe'),('검증된 실적','누적 프로젝트 300건 이상<br>다양한 산업 경험 축적','network')]):
 x=182 if i%2==0 else 843;y=227 if i<2 else 509;s+=soft(x,y,255,120,f'<div style="text-align:center;color:#000;font-size:22px">{name}</div><div style="text-align:center;margin-top:10px">{desc}</div>',16)+pill(451 if i%2==0 else 736,237 if i<2 else 522,92,92,'<svg viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="currentColor" stroke-width=".7"><circle cx="12" cy="12" r="10"/><ellipse cx="12" cy="12" rx="4" ry="10"/><path d="M2 12H22M4 6H20M4 18H20"/></svg>','#c4c4c4','#111',38)
S.append(s)
#18
s=panel('주요 고객사와 파트너십',3)+soft(70,204,291,287)+soft(375,204,531,287)+soft(919,204,290,287)+text(176,228,200,'누적 실적',22)+text(591,228,220,'주요 고객사',22)+text(990,228,220,'대표 구축 사례',22)
for i,(n,v) in enumerate([('프로젝트','320건'),('고객사','210개 사'),('재계약률','94%')]):s+=text(110,286+i*67,220,f'{n}　　<b class="accent" style="font-size:24px">{v}</b>',20)
for i,name in enumerate(['Miri Tech','Miri IT','Miri Finance','Miri Shop','Miri Soft','Miri News']):
 x=403+(i%3)*162;y=270+(i//3)*104;s+=box(x,y,149,95)+text(x,y+30,149,f'<div style="text-align:center">{name}</div>',18,'#555',600)
s+=box(948,274,232,96)+text(948,309,232,'<div style="text-align:center">Miri Tech</div>',22,'#555',600)+text(948,393,250,bullets(['스마트 팩토리 불량률 예측 AI 구축','공정 불량률 35% 감소','연간 비용 120억 원 절감']),16,'#555')+soft(70,505,1139,143)
for i,(n,desc) in enumerate([('기술 파트너','미리테크 : 공식 클라우드 MSP<br>미리클라우드 : AI 기술 협력'),('유통·판매 파트너','미리솔루션<br>미리시스템 : 엔터프라이즈 솔루션 총판 계약'),('연구·기관 협력','미리대학교 AI 연구원 산학 협력<br>미리기술연구원 공동 연구')]):s+=text(98+i*385,530,340,n,23)+text(98+i*385,576,340,desc,16,'#555')
S.append(s)
#19
s=panel('성장 전략과<br>향후 계획',4,True,'표준 소요 기간 14주<br>프로젝트 일정은 규모에 따라 조정됩니다.')
for i,(name,yr,ls) in enumerate([('단기','2026',['생성형 AI MiriAI v3.0 출시','주요 그룹사 도메인 확장','핵심 키워드 입력']),('중기','2027~2028',['글로벌 거점 확보','B2B SaaS 시장 본격 진출','해외 고객·파트너십 확대']),('장기','2029~2030',['AI 데이터 오케스트레이션 분야 경쟁력 강화','글로벌 Top 10 진입','미리닥 IPO 추진','글로벌 사업 구조 고도화','2030 TARGET','매출 2,000억 원','임직원 500명','글로벌 매출 비중 40% 달성'])]):
 x=440+i*260;y=248-i*88;s+=box(x,y,249,400+i*88,'soft')+text(x+6,y+6,237,f'<div style="background:#ff3e0c;color:#fff;text-align:center;padding:12px">STEP {i+1}.</div>',18,weight=600)+text(x+28,y+80,200,name,24)+text(x+28,y+121,200,yr,20,'#555')+text(x+28,y+155,200,bullets(ls),16,'#555')
S.append(s)
#20
s=caps([(-17,137,440),(103,214,440),(223,57,440),(343,151,440),(1054,-222,440),(1174,-128,440)],color='#484847').replace('#ff3e0c','#484847')+logo(533,236)+text(533,293,700,'Thank you',88,'#ff3e0c',300)+text(533,423,690,'미리컴퍼니는 고객과 파트너의 성장을<br>함께 만들어가겠습니다.',40,'#fff',300,1.25)+text(533,568,650,'<div class="labeled"><span class="accent">Addr.</span> 미리시 미리구 미리로 100, 미리타워 15층<br><span class="accent">Tell.</span> 02-555-1234<br><span class="accent">E-mail.</span> contact@miri.com<br><span class="accent">Web.</span> www.miri.com</div>',16,'#fff');S.append(s)
for i,s in enumerate(S,1):
 
 if i==6:s+='<style>table thead th{background:#f5f5f5}table td{height:51px}table:nth-child(1) td:last-child{background:inherit}</style>'
 if i==10:s+='<style>table td{height:42px}table th{font-size:20px}table tbody tr:nth-child(even){background:#f0f0f0}</style>'
 (OUT/f'slide_{i:02}.html').write_text(f'<!doctype html><html lang="ko"><meta charset="utf-8"><title>Cinder Pulse replica {i}</title><link rel="stylesheet" href="{FONT}"><style>{CSS}</style><body><main class="slide">{s}</main></body></html>')
(OUT/'replica.css').write_text(CSS)
# inventory
names=['다이어그램 중심 회사소개서','Contents 목차','우리는 어떤 회사인가?','미션과 비전, 핵심 가치','미리컴퍼니 대표 인사말','조직구성 및 재무현황','회사 연혁','조직문화와 인재상','성장 단계와 현재 위치','사업 성과 한눈에 보기','사업 영역 한눈에 보기','사업 간 시너지 구조','미리컴퍼니 주력 사업','제품·서비스 라인업','서비스 제공 프로세스','표준 프로젝트 일정','핵심 경쟁력의 선순환','주요 고객사와 파트너십','성장 전략과 향후 계획','Thank you']
types=['표지','목차','섹션 표지','교집합','대표 인사말','표','연혁','문화 순환','성장 단계','차트·표','허브','교집합','사업 카드','제품 카드','프로세스 순환','세로 타임라인','선순환','지표·로고','성장 단계','마침']
contracts=['foundation cover, image-frame, headline','agenda, card, list','foundation cover, pill, callout','venn, metric, callout','person, headline, prose','table','timeline, callout','cycle, hub','steps, card, callout','chart-bar, chart-line, table','hub, card, pill','venn, list, callout','card, metric, pill','card, list','cycle, steps','timeline','cycle, metric, card','metric, logo-group, card','steps, card','foundation cover, prose']
(BASE/'inventory.md').write_text('# 054 — Cinder Pulse 이미지 목록\n\n20장, 전부 1280×720. 서로 다른 7덱 중 검정 모던 회사소개서 하나에 대응하는 컬렉션이다.\n\n|이미지|페이지 유형|제목|계약 대응|\n|---|---|---|---|\n'+''.join(f'|slide_{i:02}.png|{types[i-1]}|{names[i-1]}|{contracts[i-1]}|\n' for i in range(1,21)))
(BASE/'slides.json').write_text(json.dumps([dict(number=i,title=n,type=types[i-1],contracts=contracts[i-1]) for i,n in enumerate(names,1)],ensure_ascii=False,indent=2))
print('replica sources',len(S))
