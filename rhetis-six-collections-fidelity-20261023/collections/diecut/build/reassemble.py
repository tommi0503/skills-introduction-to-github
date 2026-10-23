from pathlib import Path
import json,re,html,shutil,runpy
R=Path('/workspace/work/deliverables/diecut');V=R/'review';C=R/'collection/diecut';P=V/'reassembled';P.mkdir(exist_ok=True)
M=runpy.run_path(str(R/'build/replica.py'))
# Runtime only: local font loading, provided palette, and discrete type-step values. All layout rules come from collection files.
fonts="@font-face{font-family:'Pretendard Variable';src:url('PretendardVariable.woff2');font-weight:100 900}html,body{margin:0;width:1280px;height:720px}"+''.join(f"@font-face{{font-family:'SUITE';src:url('SUITE-{name}.woff2');font-weight:{w};}}"for name,w in [('Light',300),('Regular',400),('Medium',500),('SemiBold',600),('Bold',700),('ExtraBold',800),('Heavy',900)])
palette=json.load(open('/workspace/work/reference/contract/palette.json'))
style=''.join(('.slide.dark' if k=='dark'else'.slide')+'{'+''.join(f'{a}:{b};'for a,b in v.items())+'}'for k,v in palette.items())
style+='.slide{'+''.join(f'--type-{n}:{n}px;'for n in json.load(open('/workspace/work/reference/contract/type-steps.json')))+'--page:#f6f6f6;--ink:#000;--n-1:#fff;--n-2:#e0e0e0;--n-3:#ddd;--n-4:#c9c9c9;--n-5:#aaa;--n-6:#888;--n-7:#666;--n-8:#333;--n-9:#000;--a2:#198aba;--bad:#c00;--good:#49c500;--a1:#deff3c;--a1-on:#000000;--a1-2-soft:#f0ffba;--a1-3-soft:#e9ff8a;}'
(V/'assets/runtime.css').write_text(fonts+style)
shutil.copytree(C,V/'assets/collection',dirs_exist_ok=True)
shutil.copy('/workspace/work/tools/icons-runtime.js',V/'assets/icons-runtime.js')
shutil.copy('/workspace/work/tools/LUCIDE-LICENSE.txt',V/'assets/LUCIDE-LICENSE.txt')
links='<link rel="stylesheet" href="../assets/runtime.css">'+''.join(f'<link rel="stylesheet" href="../assets/collection/{p.relative_to(C)}">'for p in [C/'kit/css/tokens.css',C/'foundation/foundation.css']+sorted(C.glob('elements/*/element.css')))
def pos(c,r,w,h):return f'grid-column:{c} / span {w}; grid-row:{r} / span {h}'
def el(n,cl,b,c=1,r=1,w=12,h=6,style=''):
 return f'<div class="{cl}" data-el="diecut-{n}" style="{pos(c,r,w,h)}{(";"+style)if style else ""}">{b}</div>'
def txt(n,c,r,w,h,head,note='',cl='headline',big=False):
 if n=='prose' and cl=='headline':cl='prose'
 if n=='headline':b=f'<h2>{head}</h2>'+f'<p class="note">{note}</p>'if note else f'<h2>{head}</h2>'
 else:b=f'<p>{head}</p>'+(f'<p>{note}</p>'if note else'')
 return el(n,cl+(' big'if big else''),b,c,r,w,h)
def card(head,note='',fig='',kick='',cl='card',data=''):
 return f'<div class="{cl}" data-el="diecut-card"><div class="parts">'+(f'<div class="kick">{kick}</div>'if kick else'')+(f'<b class="fig">{fig}</b>'if fig else'')+f'<b class="name">{head}</b>'+ (f'<p class="note">{note}</p>'if note else'')+data+'</div></div>'
def group(parts,c,r,w,h,cl='group'):
 return f'<div class="{cl}" style="{pos(c,r,w,h)}">'+''.join(parts)+'</div>'
def lst(items,c=1,r=1,w=12,h=6,cl='list',nested=False):
 b=''.join(f'<div class="item"><b class="name">{x}</b></div>'for x in items)
 return f'<div class="{cl}" data-el="diecut-list">{b}</div>'if nested else el('list',cl,b,c,r,w,h)
def frame(c,r,w,h,n=1):return el('image-frame','frame',f'<div class="seat" data-ph="{n}"></div>',c,r,w,h)
def pill(head,c,r,w,h,on=True):return el('pill','pill'+(' on'if on else' line'),f'<div class="parts"><b class="name">{head}</b></div>',c,r,w,h)
chap=['회사 소개','로봇 자동화의 필요성','솔루션 개요','협동로봇 라인업','산업용 로봇 라인업','적용 공정 ① 조립·검사','적용 공정② 용접·도장','적용 공정③ 포장·물류','도입 효과','구축 프로세스','고객 성공 사례','인증','파일럿 제안','문의&마무리']
def page(n,body,title='',active=None,rail=''):
 if n in [3,5,8,13,18,19]:body=re.sub(r'grid-column:\d+ / span \d+; grid-row:\d+ / span \d+',pos(1,1,12,6),body)
 top='' if n==1 else '<div class="top"><span class="deck">MIRIROBOTICS</span><span class="sec">SOLUTION PROPOSAL</span></div>'
 head=''
 if active is not None:
  nav=''.join(([f'<span class="label">{active:02}. {chap[active-1]}</span>']if active else[])+[f'<span class="on">{active+1:02}. {chap[active]}</span>']+([f'<span class="label">{active+2:02}. {chap[active+1]}</span>']if active<13 else[]))
  head=f'<header class="head{" center"if n in [4,6,12,16,18]else""}"><p class="kicker">{nav}</p>'+ (f'<h1 class="title">{title}</h1>'if title else'')+('<p class="lead">전체 기간 : 총 약 10~16주 (공정 규모에 따라 조정)</p>'if n==15 else'')+'</header>'
 elif title:head=f'<header class="head"><h1 class="title">{title}</h1></header>'
 railhtml=f'<aside class="rail"><span class="label">{rail}</span></aside>'if rail else''
 P.joinpath(f'slide-{n:02}.html').write_text(f'<!doctype html><html lang="ko"><meta charset="utf-8"><title>Diecut reassembled {n:02}</title>{links}<body><section class="slide"><div class="page">{top}{head}{railhtml}<div class="body">{body}</div>{'<footer class="foot"><span class="src">© 2055 미리로보틱스 주식회사. All rights reserved.</span></footer>'if n==19 else''}</div></section><script src="../assets/icons-runtime.js"></script></body></html>')
# 01 split image cover from foundation lockup contract.
cover='<div class="seat back" data-ph="1"></div><div class="lockup at-left" style="grid-column:1 / span 12;grid-row:1 / span 6"><p class="kicker"><span>작업은 스마트하게</span><span>성과는 압도적으로</span></p><h1 class="title">MIRIROBOTICS</h1><p class="lead">사람과 함께 일하는 로봇</p><div class="meta"><b>미리로보틱스</b><br><b>협동로봇 솔루션 제안서</b></div></div>'
P.joinpath('slide-01.html').write_text(f'<!doctype html><html lang="ko"><meta charset="utf-8"><title>Diecut reassembled 01</title>{links}<body><section class="slide cover"><div class="page"><div class="body">{cover}</div><footer class="foot"><b>2055. 00. 00.</b><br>미리로보틱스 마케팅팀 김미리</footer></div></section></body></html>')
# 02 timeline-like contents, ten numbered nodes.
labels=['회사 소개','로봇 자동화의 필요성','솔루션 개요','협동로봇 라인업','산업용 로봇 라인업','적용 공정 ① 조립·검사','적용 공정 ② 용접·도장','적용 공정 ③ 포장·물류','도입 효과 (ROI 포함)','파일럿 제안 & 문의']
b=el('agenda','agenda',''.join(f'<div class="entry"><span class="mark">{i+1:02}</span><b class="name">{x}</b></div>'for i,x in enumerate(labels)))
page(2,b,rail='CONTENTS')
# 03 company/metric graph.
b=txt('headline',1,1,6,1,'MIRIROBOTICS',big=True)+pill('핵심 사업 영역',2,2,4,1)+lst(['협동로봇·산업용 로봇 시스템 통합(SI)','자동화 라인 설계·구축 컨설팅','로봇 비전·AI 통합 솔루션','원격 모니터링·유지보수·A/S'],2,3,4,2)+frame(7,1,6,4)
b+=group([card(a,fig=f,cl='card tone-1')for a,f in [('납품','3,500<small>대+</small>'),('고객사','280<small>개사+</small>'),('업력','14년'),('고객만족도','98%')]],1,5,7,2)
b+=''.join(el('pill','pill quiet',f'<div class="parts"><span class="mark"><span class="icon" data-icon="{ic}"></span></span><b class="name">{t}</b></div>')for ic,t in [('building-2','설립 2050년'),('users','임직원 120명'),('map-pin','본사 미리도 미리시 미래산업단지')])
page(3,b,active=0)
# 04 problem cards.
items=[('제조 인력난','심화되는 제조 인력난<br>• 제조업 취업자 지속 감소 추세<br>• 3D 업종 기피로 숙련공 확보 난항<br>• 생산직 채용비·교육 기간 급증<br>• 납기 지연 반복 발생<br><br>핵심 수치: 미충원율 18.7%'),('품질 기준 상승','초정밀 품질 기준 요구<br>• 고부가 산업 확대<br>• 0ppm 불량 기준 요구 증가<br>• 반복·정밀 작업 증가<br>• 품질 이슈는 거래선 상실 리스크<br><br>주요 OEM 허용 3ppm 이하'),('인건비·운영비 급등','인건비·운영비 구조적 상승<br>• 최저임금 연평균 5.2% 인상<br>• 실질 인건비 부담 가중<br>• 경제성 역전 시점 도래<br>• 24시간 가동 실현 가능<br><br>핵심 수치: 미충원율 18.7%')]
b=group([card(a,x,cl='card line',kick=k)for k,a,ls,f in M['items'] for x in ['<br>'.join('• '+q for q in ls)+'<b>'+f+'</b>']],1,1,12,6)
page(4,b,'왜 지금 자동화인가?',1)
# 05 market bar and line charts are separate contract charts; both retain all source values.
vals=[38.4,51.7,55.3,59.1,63.5,68,73.2,79];line=[44,58,68,78,91,107,124,145]
insights=['글로벌 로봇 시장 CAGR 13.2%','협동로봇 특히 CAGR 27.5% 성장','한국, 로봇 밀도 세계 1위<br>(제조업 1만 명당 1,012대)','자동차·전자·물류 도입 급증','소형 협동로봇 가격 하락세 지속','2027년 시장 규모 145B$ 전망']
b=txt('headline',1,1,5,2,'글로벌 로봇 시장 현황','글로벌 산업용 로봇 설치 대수 & 시장 규모 추이<br>(2020~2027E)')+el('card','card line','<div class="parts"><div class="kick">핵심 인사이트</div>'+lst(insights,nested=True)+'</div>')
market_line=el('chart-line','lines',''.join(f'<div class="pt" style="--v:{v}"><b>{v}</b><span></span></div>'for i,v in enumerate(line)),6,1,7,6,'--max:150')
market_bar=el('chart-bar','bars',''.join(f'<div class="bar" style="--v:{v}"><b>{v:g}</b><span>{"2080E"if i==5 else str(2020+i)+("E"if i>3 else"")}</span></div>'for i,v in enumerate(vals)),6,1,7,6,'--max:150')
b+=market_bar+market_line
page(5,b,active=1)
# 06 six sequential capabilities.
heads=['협동로봇 공급','산업용 로봇 공급','자동화 라인 설계','비전·AI 시스템','안전 시스템 통합','유지보수·A/S'];notes=['공식 파트너<br>3kg~25kg 풀 라인업','6축·스카라·델타·갠트리<br>맞춤 선정 공급','공정 분석·레이아웃·3D CAD<br>안전 설계 포함','2D·3D 비전<br>AI 검사 통합','안전 펜스·스캐너<br>ISO 10218-2','24시간 원격 모니터링<br>현장 출동·예방 PM']
icons=['bot','factory','workflow','shield-check','atom','wrench']
marks=[f'<span class="mark"><div class="seat" data-ph="{i+1}"></div></span>'if i<3 else f'<span class="mark"><span class="icon" data-icon="{icons[i]}"></span></span>'for i in range(6)]
b=group([f'<div class="card quiet" data-el="diecut-card"><div class="parts">{marks[i]}<b class="name">{a.replace(chr(10),"<br>")}</b><p class="note">{q.replace(chr(10),"<br>")}</p><b class="fig">{i+1:02}</b></div></div>'for i,(a,q,k)in enumerate(M['data'])],1,1,12,6)
page(6,b,'ONE-STOP 자동화 솔루션',2)
# 07 four robot catalogue panels.
products=[('MR-Cobot '+m,f'가반하중: {p} / 도달거리: {r}<br>반복정밀도: {pr} / 자유도: 6축 / IP등급: IP54<br>특징: '+t.replace(chr(10),'<br>'),str(i+1))for i,(m,p,r,pr,t)in enumerate(M['products'])]
b=group([card(h.replace('MR-Cobot ','MR-Cobot<br>'),t,kick='BEST SELLER'if i==1 else'',cl='card line',data=f'<div class="seat" data-ph="{i+1}"></div>')for i,(h,t,ph)in enumerate(products)],1,1,12,6,cl='group two')
page(7,b,'코봇 제품 라인업',3)
# 08 comparison table.
rows=[['모델명','MR-Cobot<br>3e','MR-Cobot<br>10e','MR-Cobot<br>16e','MR-Cobot<br>25e','MR-Cobot<br>Pro'],['가반 하중','3 kg','10 kg','16 kg','25 kg','30 kg'],['도달 거리','500 mm','1,300 mm','900 mm','1,700 mm','1,850 mm'],['반복 정밀도','±0.03 mm','±0.03 mm','±0.05 mm','±0.05 mm','±0.02 mm'],['자유도','6축','6축','6축','6축','7축'],['TCP 최고속도','1.0 m/s','1.5 m/s','1.5 m/s','1.0 m/s','2.0 m/s'],['동작 온도','0~50°C','0~50°C','0~50°C','0~50°C','-10~55°C'],['IP등급','IP54','IP54','IP54','IP54','IP67'],['협동 인증']+['ISO/TS 15066']*5]
table='<table class="table"><thead><tr>'+''.join('<th>'+a+'</th>'for a in rows[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+a+'</td>'for a in row)+'</tr>'for row in rows[1:])+'</tbody></table>'
b=txt('headline',1,1,5,2,'코봇 모델별 스펙 비교표')+txt('prose',1,4,4,3,'<b>공정별 추천 가이드</b>소형 정밀 작업(납땜·PCB 조립) → 3e 추천<br>범용 조립·포장 공정 → 10e 추천 <span class="icon" data-icon="star"></span><br>중량물 머신텐딩·프레스 공정 → 16e 추천<br>팔레타이징·물류·고하중 협동 → 25e / Pro 추천')+el('table','tablebox',table,6,1,7,6)
page(8,b,active=3)
# 09 industrial robots.
b=group([card(h,t.replace(chr(10),'<br>'),data=f'<div class="seat" data-ph="{i+1}"></div>')for i,(h,t)in enumerate(M['prods'])],1,1,12,6)
page(9,b,'산업용 로봇 제품 라인업',4)
# 10 assembly process.
heads=['부품 공급·정렬','정밀 조립','비전 외관 검사','자동 마킹·이력 추적','완제품 팔레타이징'];notes=['비전 카메라 + 델타로봇 연동.<br>무작위 부품 인식·정렬.','MR-Cobot 10e 힘제어 조립.<br>체결 토크 실시간 모니터링.','2D+3D 비전과 AI 검사.<br>불량품 자동 배출.','레이저 마킹·RFID/바코드.<br>MES 품질 이력 DB 연동.','MR-Cobot 25e 혼재 적재.<br>WMS 출고 데이터 연동.']
b=el('steps','steps',''.join(f'<div class="step"><span class="mark"><span>STEP {i+1:02}.</span></span><b class="name">{a}</b><p class="note">{q.replace(chr(10),"<br>")}</p></div>'for i,(a,q)in enumerate(M['stept'])))
page(10,b,'조립·검사 공정 자동화',5)
# 11 paired solution panels.
side=[]
for h,q,ls in [('용접 자동화','아크용접 로봇 셀 (MR-Arc 200)',['3D 시임 트래킹 → 모재 변형 실시간 보정','용접 파라미터(전류·전압·속도) 자동 최적화','스패터·흄 흡진 시스템 통합','용접 비드 품질 비전 자동 검사','다층 용접·위빙 패턴 자동 생성','MES 용접 이력 실시간 DB 연동','적용 업종: 자동차 부품·철구조물·압력용기·선박부재·건설기계']),('도장 자동화','도장 로봇 시스템 (7축 MR-Cobot Pro)',['3D 포인트클라우드 기반 경로 자동 생성','도막 두께 실시간 측정·피드백 제어','분체·수성·UV 도료 건 자동 교체','도장 부스 연동 음압·온습도 자동 제어','도장 영역 3D 비전 사전 스캔·검증','도장 후 외관 자동 비전 검사 통합','적용 업종: 가전 외장·자동차 차체·산업기계·가구·건자재'])]:
 side.append('<div class="side"><b class="name">'+h+'</b><p class="note">'+q+'</p>'+lst(ls,nested=True,cl='list check')+'</div>')
b=el('versus','versus',side[0]+'<b class="vs">SOLUTION</b>'+side[1]);page(11,b,active=6)
# 12 continuous cycle stages.
heads=['제품 도착','비전 인식','픽앤플레이스','자동 포장·실링','라벨링','팔레타이징','출고'];b=el('timeline','track alt',''.join(f'<div class="stop"><span class="kick">{i+1:02}</span><b class="name">{x}</b></div>'for i,x in enumerate(heads)),1,1,12,6)
page(12,b,'포장·물류 공정 자동화',7)
# 13 before/after data.
b=txt('headline',1,1,5,2,'로봇 도입 정량 효과','로봇 자동화 도입 전후 핵심 KPI 비교<br>(실제 고객사 평균값 기준)')
rows=[('생산 UPH','120개','218개','+82%'),('불량률','3.2%','0.4%','-87.5%'),('설비 가동률','72%','97%','+25%p'),('야간 가동 시간','','16시간',''),('공정 리드타임','48시간','28시간','-42%'),('산재 발생','연4.2건','0건','')]
norm=[(120,218),(320,40),(145,195),(0,320),(240,140),(335,0)]
body=''.join(f'<div class="sbar"><span>{a}</span><div class="seg tone-2" style="--v:{norm[i][0]}"><b>{v}</b></div><div class="seg tone-1" style="--v:{norm[i][1]}"><b>{z}</b></div></div>'for i,(a,v,z,d)in enumerate(rows))
b+=el('chart-stack','stacks h line',body,5,1,6,6,'--max:530')
for i,(a,v,z,d)in enumerate(rows):
 if d:b+=pill(d,11,i+1,2,1)
b+=el('legend','legend','<span class="key tone-1">Before</span><span class="key tone-2">After</span>')
page(13,b,active=8)

# 14 ROI ellipses reinterpret through three overlap sets.
b=el('venn','venn',''.join(f'<div class="set"><div><b class="name">{a}</b><p class="note">{t}</p></div></div>'for a,t in [('투자 가치','초기 투자비 8,000만원<br>(협동로봇 4대 패키지)'),('회수 기간','18개월 후 투자비 회수<br>(업계 평균 대비 6개월 단축)'),('기대 수익','5년 누적 순익 1.86억원<br>(투자 대비 수익률 233%)')]))
page(14,b,'투자 수익성(ROI) 분석',8)
# 15 implementation phases.
heads=['현장 진단·컨설팅','솔루션 설계','제작·조달','설치·통합','시운전·교육','유지보수·A/S'];notes=['1~2주<br>현황 분석·병목 파악<br>사전 ROI 시뮬레이션','2~3주<br>로봇·주변기기 선정<br>레이아웃·안전 설계','4~8주<br>제어반·전장 제작<br>PLC·비전 개발·테스트','1~2주<br>현장 설치·배선·배관<br>PLC·MES·ERP 연동','1주<br>양산 조건 성능 확인<br>운전자·관리자 교육','상시<br>24시간 원격 모니터링<br>예방 PM·SW 업데이트']
b=el('steps','steps',''.join(f'<div class="step"><span class="mark"><span>STEP {i+1:02}.</span></span><b class="name">{x}<br>{d}</b><p class="note">{t.replace(chr(10),"<br>")}</p></div>'for i,(x,d,t)in enumerate(M['step'])))
page(15,b,'로봇 자동화 구축 프로세스',9)
# 16 quotations retain the source wording.
b=group([card(sol,'<em>'+q+'</em>',kick=h,cl='card line')for h,sol,q in [('사례 1 : 자동차 부품 제조사','도입 솔루션: MR-Delta 2 ×6대<br>+ MR-Cobot 25e ×2대 + AGV 연동','"야간 무인 운전으로 납기 지연 Zero,<br>OEM 품질 기준 완벽 충족했습니다."<br>— A자동차부품 생산기술팀장 (가명)'),('사례 2 : 식음료 포장·물류 기업','도입 솔루션: MR-Arc 200 ×4대<br>+ MR-Cobot 10e ×2대<br>+ AI 비전 검사 시스템','"계절 피크에도 풀가동, 납기 100% 달성.<br>식품안전 인증까지 획득했습니다."<br>— B식품 SCM본부장 (가명)')]],3,1,8,6)
page(16,b,'고객사 도입 성공 사례',10)
# 17 all certificate labels; original graphic laurels are placeholders.
cert=['ISO 9001:2015<br>품질경영시스템','ISO 45001:2018<br>안전보건경영시스템','CE 마킹 기계지침<br>2006/42/EC','KS Q ISO 10218-2<br>로봇 안전 설계·통합 인증','산업통상자원부<br>로봇전문기업 지정','고용노동부 스마트공장<br>구축지원 파트너']
b=''
for i,a in enumerate(cert):
 crd=card(a,cl='card quiet',data=f'<div class="mark"><div class="seat" data-ph="{i+1}"></div></div>');crd=crd.replace('class="card quiet"',f'class="card quiet" style="{pos(1+(i%3)*4,1+(i//3)*3,4,3)}"',1);b+=crd
page(17,b,'인증 현황',11)
# 18 pilot offer.
b=txt('headline',4,1,6,1,'패키지 안내')+lst(['타깃: 자동화 첫 도입·ROI 검증 기업','구성: 협동로봇 1대 + 그리퍼 + 기본 S/W','기간: 2주 현장 무상 체험 후 도입 결정','포함 서비스: 현장 진단 컨설팅 1회, 실제 공정 데모 운전 실시, 기본 프로그래밍 교육 (1일)','특징: 초기 투자 최소화, 효과 검증 후 확장 결정','가격: 별도 협의'],2,2,10,3)+pill('지금 무료 현장 진단 신청하기',4,5,6,1)+txt('prose',4,6,6,1,'02-1234-5678 | robot@mirirobotics.com')
page(18,b,'파일럿 도입 패키지 제안',12)
# 19 closing.
b=txt('headline',2,1,10,2,'자동화의 첫 걸음,<br>미리로보틱스와 함께 시작하세요.',cl='headline center')+txt('prose',3,3,8,1,'현장 진단부터 ROI 시뮬레이션까지 전문 엔지니어가 무상으로 지원합니다.<br>도입 결정 전, 부담 없이 문의하세요.')+txt('prose',4,4,6,1,'<b>영업 문의</b>: 영업팀 | 기술 문의: 솔루션사업팀<br><b>담당자</b>: [이름] | [직책] | [직통번호]')+group([f'<div class="pill line" data-el="diecut-pill"><div class="parts"><b class="name">{a}</b></div></div>'for a in ['MiriIn','Miritube','Blog']],3,6,8,1)
page(19,b,active=13)
print('Assembled 19 pages from collection CSS')
