from pathlib import Path
import json,re,html,importlib.util
B=Path(__file__).parent;C=B.parent/'cinder-pulse';R=Path('/workspace/work/ref');O=B/'reassembled';O.mkdir(exist_ok=True)
ID='cinder-pulse';D=json.loads((B/'slides.json').read_text())
# Exact source CSS only: palette/type values supplied as style tokens, no page-specific rules.
style=(C/'kit/css/tokens.css').read_text()+'\n'+(C/'foundation/foundation.css').read_text()+'\n'+''.join(p.read_text() for p in sorted((C/'elements').glob('*/element.css')))
pal=json.loads((R/'contract/palette.json').read_text());steps=json.loads((R/'contract/type-steps.json').read_text())
style+='\n.slide{'+''.join(f'{k}:{v};' for k,v in pal['light'].items())+''.join(f'--type-{n}:{n}px;' for n in steps)+'}'
(O/'collection.css').write_text(style)
attrs=lambda name:f'data-el="{ID}-{name}"'
def el(name,cls,body,place='',values=''):
 return f'<div class="{cls}" {attrs(name)}'+(f' style="{place}'+(';' if values else '')+values+'"' if place or values else '')+'>'+body+'</div>'
def pl(c,r,w,h):return f'grid-column:{c} / span {w}; grid-row:{r} / span {h}'
def tag(cl,t):return f'<p class="{cl}">{t}</p>'
def card(name,note='',kick='',fig='',cls='',place=''):
 return el('card','card '+cls,'<div class="parts">'+(tag('kick',kick) if kick else '')+(tag('fig',fig) if fig else '')+tag('name',name)+(tag('note',note) if note else '')+'</div>',place)
def headline(name,note='',kick='',place=''):
 return el('headline','headline',tag('kick',kick)+f'<h2>{name}</h2>'+tag('note',note),place)
def call(t,place):return el('callout','callout',f'<p>{t}</p>',place)
def listing(items,place='',cls=''):
 return el('list','list '+cls,''.join('<div class="item">'+tag('name',a)+tag('note',b)+'</div>' for a,b in items),place)
def stats(items,place=''):
 return el('metric','stats',''.join(el('metric','stat','<div class="parts">'+tag('fig',f)+tag('name',n)+tag('note',a)+'</div>') for f,n,a in items),place)
def table(heads,rows,place):return el('table','tablebox','<table class="table"><thead><tr>'+''.join(f'<th>{t}</th>' for t in heads)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{x}</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>',place)
def circ(name,core,nodes,place):return el(name,'cycle' if name=='cycle' else 'hub','<div class="core">'+core+'</div>'+''.join('<div class="'+('node' if name=='cycle' else 'spoke')+'">'+tag('name',a)+tag('note',b)+'</div>' for a,b in nodes),place)
def steps(items,place='',cls='steps'):
 return el('steps',cls,''.join('<div class="step">'+tag('mark',a)+tag('name',b)+tag('note',c)+'</div>' for a,b,c in items),place)
def track(items,place='',cls='track'):
 return el('timeline',cls,''.join('<div class="stop">'+tag('kick',a)+tag('name',b)+tag('note',c)+'</div>' for a,b,c in items),place)
def venn(items,core,place):return el('venn','venn',''.join('<div class="set">'+tag('name',a)+tag('note',b)+'</div>' for a,b in items)+(f'<div class="core">{core}</div>' if core else ''),place)
def prose(txt,place,cls='prose'):return el('prose',cls,''.join(f'<p>{p}</p>' for p in txt),place)
def head(n,side=False):
 part=1 if n<10 else 2 if n<15 else 3 if n<19 else 4
 title={4:'미션과 비전,<br>핵심 가치',5:'미리컴퍼니<br>대표 인사말',8:'조직문화와<br>인재상',10:'사업 성과<br>한눈에 보기',13:'미리컴퍼니<br>주력 사업',16:'표준 프로젝트<br>일정',19:'성장 전략과<br>향후 계획'}.get(n,D[n-1]['title']);k=f'PART {part}.<br>'+['우리는 어떤 회사인가','무엇을 하는가','어떻게 하는가','어디로 가는가'][part-1]
 note={4:'미션과 비전이 겹치는 지점에 우리가 지키는 원칙이 있습니다.',8:'전문성을 기반으로 자율적으로 실행하고, 협업을 통해 성과를 만드는 조직을 지향합니다.',10:'사업 성과에 대한 설명을 적어주세요. 차트와 표 형식을 이용하면 한눈에 보기 쉽습니다.',13:'사업 성과에 대한 설명을 적어주세요. 차트와 표 형식을 이용하면 한눈에 보기 쉽습니다.',16:'표준 소요 기간 14주<br>프로젝트 일정은 규모에 따라 조정됩니다.',19:'표준 소요 기간 14주<br>프로젝트 일정은 규모에 따라 조정됩니다.'}.get(n,'')
 return ('<div class="rail"></div>' if side else '')+f'<header class="head"><p class="kicker">{k}</p><h1 class="title">{title}</h1><p class="lead">{note}</p></header>'
P={}
P[1]=None;P[3]=None;P[20]=None
ag=[('01','우리는 어떤 회사인가','미리컴퍼니 미션과 비전 · 대표 인사말 · 일반 현황 · 연혁 · 조직 구성 · 성장 단계'),('02','무엇을 하는가','미리컴퍼니 사업 영역 · 사업 간 시너지 · 주력 사업 · 제품·서비스 라인업'),('03','어떻게 하는가','프로젝트 일정 · 핵심 경쟁력 · 고객사와 파트너십'),('04','어디로 가는가','성장 전략 · 오시는 길 / 문의')]
P[2]=headline('Contents<br>목차',place=pl(1,1,5,6))+el('agenda','agenda',''.join('<div class="entry">'+tag('mark','PART '+a+'.')+tag('name',b)+tag('note',c)+'</div>' for a,b,c in ag),pl(6,1,7,6))
P[4]=venn([('MISSION','데이터에 숨겨진 가치를 발견하여 인류의 일상을 혁신<br>복잡한 비즈니스 문제를 AI 기술로 명쾌하게 해결'),('VISION','아시아 최고의 엔터프라이즈 AI 데이터 플랫폼 기업으로 도약<br>2030년까지 Global Unicorn AI Enterprise 진입')],'CORE<br>VALUE',pl(1,1,12,5))+stats([('기술 우위','Technological Excellence',''),('고객 중심','Customer First',''),('지속 가능한 혁신','Sustainable Innovation','')],pl(1,6,12,1))
P[5]=headline('고객사와의 <b>장기적인 신뢰 관계</b>를<br>최우선 가치로 생각합니다',place=pl(1,1,12,2))+prose(['안녕하십니까, 미리컴퍼니 대표 김미리입니다.','미리컴퍼니는 2018년, 데이터를 통해 세상의 모든 기업이 더 똑똑하게 일할 수 있도록 돕겠다는 작은 꿈에서 출발했습니다. 지난 8년간 끝없는 기술 도전과 연구개발을 거쳐, 이제는 국내외 200여 개 주요 기업의 디지털 전환을 책임지는 데이터 솔루션 리더로 성장하였습니다.','우리는 단기적인 수익보다 고객사와의 장기적인 신뢰 관계를 최우선 가치로 생각합니다. 최첨단 AI 기술력과 철저한 사후 관리를 바탕으로, 고객의 성공이 곧 미리컴퍼니의 성장이라는 약속을 반드시 지켜나가겠습니다.'],pl(1,3,12,3))+prose(['미리컴퍼니 대표이사　김미리'],pl(1,6,12,1))
org=[['경영진','CEO / COO / CTO / CPO / CFO','6명'],['사업전략본부','사업기획 / 국내 / 글로벌','28명'],['AI·데이터본부','AI모델링 / 엔지니어링 / 분석','52명'],['제품개발본부','Product Manager / 개발 / QA','45명'],['디자인·CX본부','Product Design / UX / CX','19명'],['마케팅·세일즈본부','B2B / 브랜드 / 글로벌 마케팅','18명'],['경영지원본부','재무·회계 / HR / 법무·총무','12명'],['합계','국내 본사·R&D·해외 지사','180명']]
fin=[['매출액','320억','390억','450억'],['영업이익','38억','47억','62억'],['영업이익률','11.9%','12.1%','13.8%'],['당기순이익','27억','34억','46억'],['유동자산','145억','183억','215억'],['부채','82억','96억','108억'],['자기자본','118억','151억','193억']]
P[6]=table(['조직 구성','담당 업무','인원'],org,pl(1,1,7,6))+table(['재무 현황','2024','2025','2026 예상'],fin,pl(8,1,5,6))
P[7]=track([('2058','설립기','미리컴퍼니 법인 설립<br>MiriData v1.0 출시'),('2060','성장기','시리즈 A 50억 원 투자 유치<br>임직원 50명 돌파<br>미리 R&D 센터 개소'),('2062','성과 창출','MiriAI 출시<br>주요 보안 인증 취득<br>주요 기업 고객 50개사 확보'),('2064 - 현재','목표 달성','시리즈 B 150억 원 투자 유치<br>누적 매출 400억 원 돌파<br>해외 법인 설립')],pl(1,1,12,4))+call('지금까지 쌓아온 경험과 혁신을 바탕으로, 앞으로도 여러분과 함께 더 큰 미래를 만들어 나가겠습니다.',pl(1,5,12,2))
P[8]=circ('cycle','MIRI<br>PEOPLE',[('AUTONOMY','자율과 책임<br>스스로 판단하고 실행'),('CURIOSITY','끊임없는 탐구<br>WHY에서 시작하는 문제 해결'),('SYNERGY','집단지성 시너지<br>서로 다른 전문성을 연결'),('EXECUTION','빠른 실행<br>실행 결과를 데이터로 검증'),('GROWTH','함께 성장<br>피드백을 통한 지속적인 개선')],pl(1,1,12,6))
P[9]=steps([('STAGE 1','창업기','2058~2059<br>AI데이터 엔진 알고리즘 개발<br>초기 금융권 고객 5개사 확보'),('STAGE 2','성장기','2060~2062<br>연 매출 150억 원 달성<br>R&D 중심 연구소 확충'),('STAGE 3','확장기','2063~현재<br>글로벌 SaaS 시장 진출<br>해외 사업 기반 확대'),('STAGE 4','성숙기','2067~<br>글로벌 Enterprise AI 확립<br>IPO 추진')],pl(1,1,12,4))+call('현재 우리는 STAGE 3 · 확장기에 있습니다.<br>기술과 고객 기반을 바탕으로 글로벌 시장 확장을 본격화하는 단계',pl(1,5,12,2))
P[10]=el('chart-bar','bars',''.join(f'<div class="bar" style="--v:{v}"><b>{v}</b><span>{2060+i}</span></div>' for i,v in enumerate([28,65,140,248,380,450])),pl(1,1,12,3),'--max:500')+table(['사업 영역','주요 서비스','매출 비중','고객사 수'],[['Miri Intelligence','AI 플랫폼·예측 솔루션','45%','120개사'],['Miri Cloud','SaaS·클라우드 스토리지','30%','85개사'],['DX Consulting','데이터 파이프라인·DX 자문','15%','32개사'],['M&O','24/7 유지보수·AI 튜닝','10%','210개사(유지)']],pl(1,4,12,3))
P[11]=circ('hub','MIRI<br>COMPANY',[('사업 01 · Miri Intelligence','AI PLATFORM<br>데이터 통합 수집<br>실시간 AI 예측<br>대규모 데이터 분석 자동화'),('사업 02 · Miri Cloud','SaaS SERVICE<br>구독형 클라우드 기반<br>데이터 저장·관리·분석 환경 통합 제공'),('사업 03 · DX Consulting','ENTERPRISE CONSULTING<br>맞춤형 데이터 파이프라인 설계<br>DX 전략 및 실행 로드맵 자문'),('사업 04 · Maintenance & Operation','OPERATION SUPPORT<br>24/7 시스템 유지보수<br>성능 모니터링')],pl(1,1,12,5))+call('Miri Intelligence · 45%　|　Miri Cloud · 30%　|　DX Consulting · 15%　|　M&O · 10%',pl(1,6,12,1))
P[12]=venn([('Miri Intelligence','고성능 AI 예측 알고리즘 기술'),('Miri Cloud','대용량 데이터 클라우드 인프라'),('DX Consulting','산업별 도메인 전문성')],'D',pl(1,1,5,6))+listing([('교집합 A','클라우드 환경에서 즉시 동작하는 AI SaaS 모델 구축'),('교집합 B','기업 맞춤형 클라우드 데이터 파이프라인 구현'),('교집합 C','해당 교집합에 해당하는 내용을 적어주세요'),('교집합 D','고객 맞춤형 데이터 생태계 구축 및 자동화 완성')],pl(6,1,7,5),'divided')+call('사업은 나뉘어 있지만 역량은 하나로 모입니다.',pl(6,6,7,1))
P[13]=card('Miri Intelligence','기업 내 유기적으로 흩어져 있는 비정형 데이터를 실시간으로 수집하고 분석하는 AI 솔루션입니다. 고도화된 예측 알고리즘을 통해 의사결정 시간을 70% 이상 단축시킵니다.','주력 사업 1.','180건 <small>프로젝트 · 120개 사 고객</small>',place=pl(1,1,12,3))+card('Miri Cloud','초기 구축 비용 부담 없이 월 구독 형태로 이용할 수 있는 보안 특화 클라우드 플랫폼입니다. 엔터프라이즈급 보안 환경을 바탕으로 데이터 시각화 리포트를 제공합니다.','주력 사업 2.','95건 <small>프로젝트 · 85개 사 고객</small>',place=pl(1,4,12,3))
products=[('MiriData Engine','초고속 실시간 데이터 수집·정제<br>대용량 데이터 처리 최적화<br>주요 고객 · 대기업 데이터 조직'),('MiriAI Insights','머신러닝 기반 비즈니스 지표 자동 예측<br>전략 수립을 위한 인사이트 제공<br>주요 고객 · 전략기획팀·경영진'),('Miri Cloud Hub','멀티 클라우드 환경의 데이터를 안전하게 통합·관리<br>주요 고객 · IT 인프라·보안 관리팀'),('Miri BI Dashboard','Drag & Drop으로 완성하는 데이터 툴<br>실시간 리포트 공유<br>주요 고객 · 마케팅·영업팀'),('Miri Security Shield','개인정보·민감 데이터 자동 탐지 마스킹<br>금융·의료 기관 중심'),('Miri Ops Agent','데이터 파이프라인 자동화<br>24/7 운영 모니터링<br>주요 고객 · DevOps·데이터 엔지니어')]
P[14]=''.join(card(a,b,f'{i+1:02}',place=pl((i%3)*4+1,(i//3)*3+1,4,3)) for i,(a,b) in enumerate(products))
process=[('문의·상담','고객 요구사항 정의<br>도입 목적 및 핵심 과제 파악'),('분석·제안','데이터 인프라 현황 진단<br>고객 환경에 맞춘 솔루션 제안'),('계약·설계','최종 사업 범위 확정<br>PoC 실행 및 세부 일정 수립'),('제작·구축','AI 모델링 개발 및 데이터 연동<br>실사용 환경 기준 성능 최적화'),('검수·납품','시스템 최종 통합 테스트<br>보안 점검 및 사용자 교육 후 인도'),('운영·고도화','24/7 장애 대응 및 주기적 AI 모델 재학습<br>다음 과제 발굴로 연결')]
P[15]='<div class="group col" style="'+pl(1,1,3,6)+'">'+''.join(card(a,b,f'STEP {i+1}.') for i,(a,b) in enumerate(process[:3]))+'</div>'+circ('cycle','고객 성공',[(a,'') for a,b in process],pl(4,1,6,6))+'<div class="group col" style="'+pl(10,1,3,6)+'">'+''.join(card(a,b,f'STEP {i+4}.') for i,(a,b) in enumerate(process[3:]))+'</div>'
P[16]=track([('1~2주차','프로젝트 착수','프로젝트 킥오프 워크숍 진행 및 기본 데이터 및 요구사항 확정'),('3~4주차','프로젝트 설계','시스템 데이터 구조 설계 및 AI 알고리즘 모델링 기획안 확정'),('5~10주차','제작','데이터 파이프라인 구축, AI 학습 및 기능 개발 (중간보고회 개최)'),('11~12주차','검수','내부 QA 수행, 데이터 정확도 테스트 및 고객 피드백 반영'),('13~14주차','납품','최종 솔루션 운영 환경 이관, 사용자 매뉴얼 전달 및 인수인계')],pl(1,1,12,6),'track col')
P[17]=circ('hub','재계약률<br>94%',[('기술력','독자 개발 AI 특허 34건 보유<br>고도화된 데이터 처리 품질 확보'),('전문 인력','석·박사급 전문 엔지니어 85명<br>안정적 기술의 전문 조직'),('사후 지원','24시간 실시간 모니터링<br>주기적인 AI 모델 업데이트'),('검증된 실적','누적 프로젝트 300건 이상<br>다양한 산업 경험 축적')],pl(1,1,12,6))
P[18]=stats([('320건','프로젝트',''),('210개 사','고객사',''),('94%','재계약률','')],pl(1,1,3,4))+el('logo-group','logos',''.join(f'<div class="seat logo" data-ph="{i+1}"></div>' for i in range(6)),pl(4,1,6,4))+card('대표 구축 사례','스마트 팩토리 불량률 예측 AI 구축<br>공정 불량률 35% 감소<br>연간 비용 120억 원 절감','Miri Tech',place=pl(10,1,3,4))+'<div class="group" style="'+pl(1,5,12,2)+'">'+''.join(listing([item]) for item in [('기술 파트너','미리테크 : 공식 클라우드 MSP<br>미리클라우드 : AI 기술 협력'),('유통·판매 파트너','미리솔루션 · 미리시스템 솔루션 총판 계약'),('연구·기관 협력','미리대학교 AI 연구원 산학 협력<br>미리기술연구원 공동 연구')])+ '</div>'
P[19]=steps([('STEP 1.','단기','2026<br>생성형 AI MiriAI v3.0 출시<br>주요 그룹사 도메인 확장'),('STEP 2.','중기','2027~2028<br>글로벌 거점 확보<br>B2B SaaS 시장 본격 진출<br>해외 고객·파트너십 확대'),('STEP 3.','장기','2029~2030<br>글로벌 Top 10 진입<br>미리닥 IPO 추진<br>매출 2,000억 원<br>임직원 500명<br>글로벌 매출 비중 40% 달성')],pl(1,1,12,6))
sourcecolors='--a1:#ff3e0c;--a1-on:#ffffff;--a1-8:#b92b06;--a1-1-soft:#fff2ee;--a1-2-soft:#ffe5dc;--n-1:#f0f0f0;--n-2:#e5e5e5;--n-3:#d8d8d8;--n-4:#bcbcbc;--n-5:#999999;--n-6:#777777;--n-7:#555555;--n-8:#333333;--n-9:#30302f'
for n in range(1,21):
 if n in [1,3,20]:
  title={1:'<b>다이어그램 중심</b><br>회사소개서',3:'우리는<br><b>어떤 회사</b>인가?',20:'<b>Thank you</b>'}[n];lead={1:'이 프레젠테이션은 다양한 다이어그램을 활용해<br>회사를 소개하는 회사소개서입니다.',3:'인공지능 기반 데이터 솔루션으로 기업의<br>디지털 혁신을 선도하는 미리컴퍼니입니다.',20:'미리컴퍼니는 고객과 파트너의 성장을<br>함께 만들어가겠습니다.'}[n]
  body=f'<section class="slide cover" style="{sourcecolors}"><div class="page"><div class="lockup '+('at-center' if n==20 else 'at-left')+f'"><p class="kicker">'+('PART 1' if n==3 else 'MIRI Company')+f'</p><h1 class="title">{title}</h1><p class="lead">{lead}</p></div><div class="deco"></div><p class="meta">'+('Addr. 미리시 미리구 미리로 100, 미리타워 15층<br>Tell. 02-555-1234<br>E-mail. contact@miri.com<br>Web. www.miri.com' if n==20 else '2080.10.22<br>경영기획팀 김미리 과장' if n==1 else '')+'</p></div></section>'
 else:body=f'<section class="slide" style="{sourcecolors}"><div class="page">'+('' if n==2 else head(n,n in [4,5,8,10,13,16,19]))+f'<div class="body">{P[n]}</div></div></section>'
 (O/f'slide_{n:02}.html').write_text(f'<!doctype html><html lang="ko"><meta charset="utf-8"><title>Cinder Pulse reassembled {n}</title><link rel="stylesheet" href="../fonts/fonts.css"><link rel="stylesheet" href="collection.css"><body style="margin:0">{body}</body></html>')
print('reassembled',len(P))
