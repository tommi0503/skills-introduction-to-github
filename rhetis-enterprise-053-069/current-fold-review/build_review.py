from pathlib import Path
import json,re,sys,html
B=Path(__file__).parent;C=B.parent/'current-fold';REF=B.parent;sys.path.insert(0,str(REF/'tools'));import preview
steps=json.load(open(REF/'contract/type-steps.json'));pal=json.load(open(REF/'contract/palette.json'))
for dark,mode in [(False,'light'),(True,'dark')]:
 out=preview.sheet(C,steps,pal,dark,'../fonts/fonts.css')
 (B/'library'/f'{mode}.html').write_text(out)
# Reassembly uses collection CSS without page-specific declarations; only palette/type/font plumbing is supplied.
style=''.join((C/'kit/css/tokens.css').read_text())+(C/'foundation/foundation.css').read_text()+''.join(p.read_text() for p in sorted((C/'elements').glob('*/element.css')))
style+=preview._palette(pal)+'.slide{--page:#ffffff;--ink:#343b69;--a1:#329deb;--a1-on:#ffffff;--a1-1-soft:#eff9fd;--a1-2-soft:#dcf0fb;--a1-3-soft:#b5def5;--a1-4-soft:#89c8ec;--a1-5-soft:#5bb1df;--a1-6:#3297d2;--a1-7:#245ba8;--a1-8:#173c80;--n-1:#f6f6f6;--n-2:#edf0f2;--n-8:#353a42;}' + '.slide{'+''.join(f'--type-{n}:{n}px;' for n in steps)+'}'
(B/'reassembled'/'collection.css').write_text(style)
def el(k,cls,inside='',slot=None,extra=''):
 st=(' style="'+slot+'"') if slot else ''
 return f'<div class="{cls}" data-el="current-fold-{k}"{st}{extra}>{inside}</div>'
def slot(x,y,w,h):return f'grid-column:{x} / span {w}; grid-row:{y} / span {h}'
def card(n,note='',fig='',cls='card',kick=''):
 return el('card',cls,'<div class="parts">'+(f'<p class="kick">{kick}</p>' if kick else '')+(f'<p class="fig">{fig}</p>' if fig else '')+f'<p class="name">{n}</p><p class="note">{note}</p></div>')
def group(contents,x,y,w,h,cls='group'):return f'<div class="{cls}" style="{slot(x,y,w,h)}">'+''.join(contents)+'</div>'
def prose(s,x,y,w,h):return el('prose','prose',''.join('<p>'+p+'</p>' for p in s.split('\n')),slot(x,y,w,h))
def stat(fig,n,note=''):return el('metric','stat',f'<div class="parts"><p class="fig">{fig}</p><p class="name">{n}</p><p class="note">{note}</p></div>')
def hub(labels,core):return el('hub','hub','<div class="core">'+core+'</div>'+''.join(f'<div class="spoke"><p class="name">{a}</p><p class="note">{b}</p></div>' for a,b in labels))
def lst(items):return el('list','list check',''.join(f'<div class="item"><p class="name">{a}</p><p class="note">{b}</p></div>' for a,b in items))
def picture(n,x,y,w,h):return el('image-frame','frame',f'<div class="seat" data-ph="{n}"></div>',slot(x,y,w,h))
data=json.load(open(B/'page-data.json'));pages={}
pages[2]=el('agenda','agenda',''.join(f'<div class="entry"><span class="mark">0{i+1}</span><p class="name">{a}</p><p class="note">{b}</p></div>' for i,(a,b) in enumerate([('미리컴퍼니 소개','인사말 · 일반 현황<br>미션&비전 · 연혁 · 조직 구성'),('사업 소개','사업 개요 · 주력사업<br>제품 및 서비스'),('경쟁력과 신뢰','핵심 경쟁력 · 고객사 실적<br>인증·특허·수상 · 파트너십'),('성장과 미래','성장 전략')])) ,slot(1,1,12,6))
pages[4]=prose('미리컴퍼니는 고객의 비즈니스가 가진 가능성을 발견하고 더 나은 결과로 연결하기 위해 항상 고민해 왔습니다. 변화하는 시장과 다양한 환경 속에서도 고객에게 필요한 가치를 먼저 생각하며, 각자의 방향과 목표에 맞는 최적의 해답을 찾기 위해 노력합니다.\n축적된 전문성과 실행력을 바탕으로 고객이 신뢰할 수 있는 솔루션을 제공하고 실질적인 성과와 지속적인 성장으로 이어질 수 있도록 함께하겠습니다.\n앞으로도 고객과 파트너, 구성원이 함께 성장할 수 있는 기반을 만들어가겠습니다. 감사합니다.',1,1,8,6)+picture(1,9,1,4,6)
rows=[('회사명','주식회사 미리컴퍼니'),('대표이사','김미리'),('설립일','2080년 3월 15일'),('자본금','50억 원'),('임직원','180명'),('주요 사업','기업 솔루션·컨설팅·운영 서비스'),('본사','미리시 미리구 미리로 00'),('대표전화','00-0000-0000'),('이메일','kimmiri@miridih.com')]
pages[5]=picture(1,1,1,6,6)+el('table','tablebox','<table class="table"><thead><tr><th>구분</th><th>일반 현황</th></tr></thead><tbody>'+''.join(f'<tr><th>{a}</th><td>{b}</td></tr>' for a,b in rows)+'</tbody></table>',slot(7,1,6,6))
pages[6]=group([lst([('MISSION','비즈니스의 가능성을 발견하고 고객의 성장을 연결합니다.'),('VISION','고객과 가장 오래 함께하고 싶은 비즈니스 파트너'),('STRATEGY','전문성과 실행력으로 고객 맞춤 솔루션 제공'),('CORE VALUE','고객을 최우선으로 생각하며 신뢰를 만들어갑니다.')]),hub([('MISSION','가능성 발견'),('STRATEGY','성장 전략'),('VISION','고객과 함께'),('CORE VALUE','신뢰와 혁신')],'CORE VALUE')],1,1,12,6)
pages[7]=''.join(el('card','card'+(' on' if i==3 else ''),f'<div class="parts"><p class="fig">{2081+i}</p><p class="name">{a}</p><p class="note">{b}</p></div>',slot(1+i*3,4-i,3,3)) for i,(a,b) in enumerate([('창업','법인 설립<br>기업 솔루션 사업 시작'),('기반 확대','솔루션 라인업 확장<br>고객사 30개 돌파'),('조직 성장','전문 조직·R&D 확대<br>프로젝트 100건 달성'),('글로벌','해외 파트너 구축<br>글로벌 고객 확보')]))
org='<div class="root">대표이사</div>'+''.join(f'<div class="branch"><div class="node">{a}</div>'+''.join(f'<div class="leaf">{l}</div>' for l in ls)+'</div>' for a,ls in [('경영지원본부',['인사팀','재무팀','총무팀']),('사업본부',['영업팀','고객지원팀','사업운영팀']),('기술본부',['서비스개발팀','기술지원팀','품질관리팀'])])
pages[8]=el('hierarchy','org',org,slot(1,1,6,6))+el('chart-bar','bars',''.join(f'<div class="bar"><b>{v}</b><span>{2080+i}</span></div>'.replace('class="bar"',f'class="bar" style="--v:{v}"') for i,v in enumerate([120,135,178,220,252,280])),slot(7,1,6,6)+';--max:300')
pages[9]=el('hub','hub','<div class="core">MIRICOMPANY</div>'+''.join(f'<div class="spoke"><p class="name">{a}</p><p class="note">{b}</p></div>' for a,b in [('솔루션','맞춤형 업무 효율화'),('컨설팅','데이터 기반 성장 방향'),('운영지원','안정적인 서비스 운영')]),slot(1,1,8,6))+picture(1,9,1,4,6)
pages[10]=group([card('업무 프로세스 개선','업무 구조를 분석하고 효율적인 프로세스로 개선'),card('시스템 구축','기업 환경에 맞는 맞춤형 업무 시스템 구축'),card('데이터 활용','비즈니스 데이터를 분석해 의사결정을 지원')],1,1,8,6)+group([stat('35%','업무 효율 향상','불필요한 프로세스 최소화'),stat('40%','운영 안정성 강화','표준화된 운영과 오류 감소')],9,1,4,6,'stack')
pages[11]=el('chart-area','areas','<div class="series tone-1"><span class="name">프로젝트 수(건)</span>'+''.join(f'<div class="pt" style="--v:{v}"><b>{v}</b></div>' for v in [12,21,35,48,64,70])+'</div><div class="series tone-2"><span class="name">재계약률(%)</span>'+''.join(f'<div class="pt" style="--v:{v}"><b>{v}</b></div>' for v in [58,63,69,74,80,90])+'</div><div class="axis">'+''.join(f'<span>{i}</span>' for i in range(2080,2086))+'</div>',slot(1,1,12,4)+';--max:100')+group([stat('95%','사업 목표 달성률'),stat('35%','업무 처리시간 단축'),stat('120+','시장·고객 데이터 분석'),stat('45+','신규 사업 기회 발굴')],1,5,12,2)
pages[12]=group([el('pricing','plan'+(' on' if i==2 else ''),f'<p class="name">{n}</p><p class="price"><span class="fig">{i+1}</span><small>단계</small></p>'+lst([('핵심 업무 기능','기업 환경 맞춤 설계'),('운영 지원','효율적인 업무 관리'),('통합 서비스','지속적인 개선')])) for i,n in enumerate(['BASIC','PROFESSIONAL','ENTERPRISE','PREMIUM'])],1,1,12,6)
pages[13]=el('hub','hub',hub([('풍부한 프로젝트 경험','축적된 경험과 실행력'),('분야별 전문 역량','기획·기술·운영 전문가'),('맞춤형 프로젝트 대응','기업별 최적의 해법'),('지속적인 고객 파트너십','장기적인 협력'),('안정적인 운영 지원','도입부터 운영까지'),('기술 기반 혁신','AI·데이터 활용')],'CORE COMPETENCIES').split('>',1)[1].rsplit('</div>',1)[0],slot(1,1,12,6))
pages[14]=group([card('통합 업무관리 혁신 프로젝트','분산 업무 데이터 통합<br>주요 업무 프로세스 표준화','MIRITECH'),card('글로벌 운영 프로세스 개선','해외 거점 운영 체계 표준화<br>운영 비용 28% 절감','MIRI GLOBAL')],1,1,6,6,'stack')+el('logo-group','logos',''.join(f'<div class="seat logo" data-ph="{i}"></div>' for i in range(1,10)),slot(7,1,6,6))
pages[15]=group([el('card','card',f'<div class="parts"><p class="kick">{a}</p><p class="name">{b}</p><p class="note">{c}</p><div class="seat" data-ph="{i+1}"></div></div>') for i,(a,b,c) in enumerate([('BUSINESS REG','사업자 등록 인증','기업 솔루션·컨설팅·운영 서비스'),('CERTIFICATION','ISO9001 품질경영시스템 인증','체계적인 품질 관리 프로세스'),('CERTIFICATE','MRCC 정식 기관 인증','규정된 평가 기준 준수'),('QUALITY CERTIFICATION','국제 품질경영시스템 인증','글로벌 품질 관리 체계 수립')])],1,1,12,6)
pages[16]=group([card(b,c,a) for a,b,c in [('60+','기술·솔루션 파트너','전문 역량을 기반으로 안정적 서비스 구축'),('40+','비즈니스·전략 파트너','전략적 협력으로 시장 확대'),('260+','협업 프로젝트','공동 개발과 다양한 협업 추진')]],1,1,12,3)+group([card(b,c,a) for a,b,c in [('8 Fields','협력 분야','기술·데이터·인프라 등 다양한 분야'),('12 Industries','산업 네트워크','다양한 산업의 전문 기업과 협력'),('10+','글로벌 협력 네트워크','해외 파트너와 새로운 시장 기회')]],1,4,12,3)
pages[17]=el('steps','steps',''.join(f'<div class="step"><span class="mark">STEP {i+1}</span><p class="name">{a}</p><p class="note">{b}</p></div>' for i,(a,b) in enumerate([('사업 기반 구축','핵심 사업의 경쟁력과 성장 기반을 확보합니다.'),('시장 경쟁력 강화','고객 접점과 사업 경쟁력을 확대합니다.<br>신규 고객 확보'),('사업 영역 확장','사업 영역을 넓히고 새로운 기회를 발굴합니다.<br>신규 제품·서비스 출시<br>사업 영역 다각화<br>전략적 파트너십 확대'),('시장 확대 가속화','다양한 채널과 시장으로 사업을 확장합니다.<br>유통 채널 다변화<br>신규 시장 진출<br>온·오프라인 채널 확대<br>사업 포트폴리오 강화'),('글로벌 사업 도약','글로벌 경쟁력을 확보하고 해외 사업을 확대합니다.<br>해외 시장 진출<br>글로벌 네트워크 구축<br>현지 고객 기반 확대<br>AI·디지털 서비스 개발')])),slot(1,1,12,6))

for d in data:
 i=d['n'];title=d['title'];kick=d['kick']
 if i in [1,3,18]:
  if i==1:content='<div class="lockup at-top-left"><p class="kicker">스마트 다이어그램 활용</p><h1 class="title">한눈에 정리한<br><b>비즈니스 회사소개서</b></h1></div><div class="meta">MIRI COMPANY · 2080.09</div>'
  elif i==3:content='<div class="lockup at-left"><p class="kicker">01</p><h1 class="title">ABOUT US</h1><p class="lead">미리컴퍼니 소개</p></div>'
  else:content='<div class="lockup at-bottom-left"><h1 class="title">THANK YOU</h1><p class="lead">함께 성장하는 비즈니스 파트너</p></div>'
  body='<section class="slide cover'+(' on' if i in [3,18] else '')+'"><div class="page">'+content+'<div class="deco"></div></div></section>'
 else:body=f'<section class="slide"><div class="page"><header class="head"><p class="kicker">{kick}</p><h1 class="title">{title}</h1></header><div class="body">{pages[i]}</div></div></section>'
 (B/'reassembled'/f'slide_{i:02}.html').write_text('<!doctype html><html lang="ko"><meta charset="utf-8"><link rel="stylesheet" href="../fonts/fonts.css"><link rel="stylesheet" href="collection.css"><body style="margin:0">'+body+'</body></html>')
print('review built')
