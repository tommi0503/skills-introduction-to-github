from pathlib import Path
import json,re
C=Path('/workspace/output/nightchamfer');R=Path('/workspace/output/nightchamfer-review');P=R/'reassembled';P.mkdir(exist_ok=True)
css=(C/'kit/css/tokens.css').read_text()+(C/'foundation/foundation.css').read_text()+''.join(p.read_text()for p in sorted(C.glob('elements/*/element.css')))
steps=json.loads(Path('/workspace/work/reference/contract/type-steps.json').read_text());css+='\n.slide{'+''.join(f'--type-{n}:{n}px;'for n in steps)+'}\n'
(P/'collection.css').write_text(css)
pal=json.loads(Path('/workspace/work/reference/contract/palette.json').read_text())['dark'];pal.update({'--page':'#000000','--ink':'#FFFFFF','--a1':'#3982FB','--a1-on':'#FFFFFF'})
for s in range(1,10):
 for suf in ['', '-soft','-muted']:
  # A style supplies ranked accent depth. Layout and element CSS are copied unchanged.
  l=.18+s*.075;ch=.012+s*.013
  pal[f'--a1-{s}{suf}']=f'oklch({l:.3f} {ch*(.6 if suf else 1):.3f} 258)'
pal.update({f'--n-{i}':v for i,v in enumerate(['#111111','#222222','#333333','#606060','#888888','#AAAAAA','#CCCCCC','#DDDDDD','#FFFFFF'],1)})
for i,v in enumerate(['#07111E','#0C1B37','#143263','#173B88','#2874E6','#276BCD','#3982FB','#6CA5FF','#AFCEFF'],1):
 for suf in ['', '-soft','-muted']:pal[f'--a1-{i}{suf}']=v
pal['--a1-6-muted']='#4082F0'
pal['--a2']='#0096FF'
pal['--a1-9-muted']='#73A0C4'
PAL=';'.join(f'{k}:{v}'for k,v in pal.items())
def grid(x,y,w,h):return f'grid-column:{x} / span {w}; grid-row:{y} / span {h}'
def el(folder,cls,inner,x=1,y=1,w=12,h=6,data=''):
 return f'<div class="{cls}" data-el="nightchamfer-{folder}" style="{grid(x,y,w,h)}{data}">{inner}</div>'
def parts(n,note='',fig='',kick='',mark=''):
 return '<div class="parts">'+(f'<p class="kick">{kick}</p>'if kick else '')+(f'<b class="fig">{fig}</b>'if fig else '')+f'<b class="name">{n}</b>'+(f'<p class="note">{note}</p>'if note else '')+(f'<span class="mark">{mark}</span>'if mark else '')+'</div>'
def card(n,d='',fig='',kick='',on='',x=1,y=1,w=12,h=6):return el('card','card '+on,parts(n,d,fig,kick),x,y,w,h)
def items(vals,cls='list',x=1,y=1,w=12,h=6):return el('list',cls,''.join(f'<div class="item"><b class="name">{n}</b><p class="note">{d}</p></div>'for n,d in vals),x,y,w,h)
def headline(n,d='',x=1,y=1,w=12,h=6):return el('headline','headline big',f'<h2>{n}</h2><p class="note">{d}</p>',x,y,w,h)
def bar(vals,labs,x,y,w,h,maxv):return el('chart-bar','bars',''.join(f'<div class="bar {"on"if i==len(vals)-1 else ""}" style="--v:{v}"><b>{v:,}</b><span>{l}</span></div>'for i,(v,l)in enumerate(zip(vals,labs))),x,y,w,h,f';--max:{maxv}')
def callout(s,x=1,y=5,w=12,h=2):return el('callout','callout',f'<p>{s}</p>',x,y,w,h)
def group(cards,x=1,y=1,w=12,h=6):
 return f'<div class="group" style="{grid(x,y,w,h)}">'+''.join(cards)+'</div>'
def innercard(n,d='',fig='',kick='',cl=''):
 return f'<div class="card {cl}" data-el="nightchamfer-card">{parts(n,d,fig,kick)}</div>'
contents=[]
contents.append(None)
contents.append(headline('Contents','이곳에 프레젠테이션 목차에 관한<br>내용을 간략하게 작성해보세요.',1,1,6,3)+el('agenda','agenda',''.join(f'<div class="entry"><span class="mark">0{i}</span><b class="name">{n}</b><p class="note">{d}</p></div>'for i,(n,d)in enumerate([('사업 현황','현재 주요 사업 (미리워크)<br>신규 사업 추진 배경'),('시장·고객 분석','AI 시장 규모와 성장성<br>고객 타깃과 페인포인트'),('신규 사업 개요','미리AI 제품 개요<br>핵심 가치와 차별성'),('사업 전략','비즈니스 모델<br>시장 진입 전략 및 포지션')],1)),8,1,5,6)+el('image-frame','frame','<div class="seat" data-ph="1"></div>',1,4,4,3))
contents.append(el('hub','hub','<div class="core"><b class="name">UNIFIED<br>SERVICE</b></div>'+''.join(f'<div class="spoke"><b class="name">{n}</b><p class="note">{d}</p></div>'for n,d in [('할 일·프로젝트','문서·노트를 한 곳에서 작성·공유'),('팀 메신저','칸반·일정으로 팀 업무 진행 관리'),('유연한 연동','채널 기반 소통으로 대화와 업무 연결'),('서비스 관련 키워드','이곳에 상세 내용을 입력해 보세요.')])) )
contents.append(callout('<b>고객 수요 충족 목적</b><br>AI 성능 향상과 고객 요구 증대에 따른 실서비스 적용 시점이 도래',1,1,12,6)+el('headline','headline center','<h2>다음 성장 동력 발굴</h2><p class="note">쌓인 업무 데이터와 생성형 AI 기술을 결합해,<br>자연스러운 신규 성장 기회를 확보합니다.</p>',1,5,6,2)+el('headline','headline center','<h2>고객의 요구</h2><p class="note">사용자의 약 70%가 ‘반복 업무 자동화’ 기능을 요청<br>(회의록 정리·문서 작성에 주당 평균 5시간 소모)</p>',7,5,6,2))
contents.append(el('headline','headline center','<h2>국내 생산성 도구 시장 규모 추이</h2>',1,1,6,1)+el('chart-bar','bars',''.join(f'<div class="bar {"on"if i==3 else ""}" style="--v:{v}"><b>{v:,}억</b><span>{l}</span></div>'for i,(v,l)in enumerate(zip([300,520,820,1300],['1Q','2Q','3Q','4Q']))),1,1,6,4,';--max:1500')+el('headline','headline center','<h2>국내 시장 성장성 포인트</h2>',7,1,6,1)+items([('AI 대중화','업무에 AI를 쓰는 것이 당연한 환경으로 전환'),('기업 도입 확대','생산성 향상을 위한 기업의 AI 도구 도입이 가속'),('자동화 ROI 입증','업무 시간 절감 효과가 수치로 증명되며 수요 견인')],'list divided',7,2,6,4)+callout('AI 업무 도구 시장은 <b>연 60% 이상 고성장</b> 중이며, 협업툴 시장 대비 성장률이 2배를 넘습니다.'))
contents.append('<div class="split wide-left" style="'+grid(1,1,12,6)+'">'+el('card','card','<div class="parts"><b class="name">미리AI (MiriAI)</b><div class="note"><p>미리워크에 내장되는 AI 비서로 회의록 요약, 문서 초안,<br>할 일 추출, 업무 검색을 대화 한 번으로 처리합니다.</p>'+items([('회의록 자동 요약','녹취·메모를 핵심 요약과 할 일로 자동 변환'),('문서 초안 작성','주제만 입력하면 보고서·기획서 초안을 생성'),('업무 검색·질문','흩어진 문서·대화를 물어보면 AI가 즉시 답변')])+'</div></div>')+el('image-frame','frame','<div class="seat" data-ph="1"></div>')+'</div>')
contents.append(el('card','card','<div class="parts"><span class="mark"><span class="seat logo" data-ph="1"></span></span><b class="name">미리워크 사용 팀</b><b class="fig">120,000</b><div class="note">'+el('gauge','meter','<b class="name">AI 미사용 고객</b><b class="fig"></b>',data=';--v:50')+el('gauge','meter','<b class="name">AI 사용 고객</b><b class="fig"></b>',data=';--v:100')+'</div></div>',1,1,12,3)+el('card','card quiet','<div class="parts"><b class="name">주요 타깃: 반복 업무가 많은 운영·기획 팀</b><div class="note">'+items([('회의·문서 작업 비중이 높음',''),('인력 대비 업무량이 과다',''),('AI 도입 의향은 높으나 진입 장벽을 느낌',''),('이곳에 주요 타깃 특징에 대한 내용을 작성해주세요.','')])+'</div></div>',1,3,6,4)+el('card','card quiet','<div class="parts"><b class="name">이곳에 고객 분석 페인포인트를 작성하세요.</b><div class="note">'+items([('시간 낭비','회의록·보고서 정리에 반복적으로<br>시간 소모된 시간을 작성해보세요'),('도구 이중화','별도 AI 툴을 따로 쓰며 미리워크와는<br>단절된 데이터 도출')])+'</div></div>',7,3,6,4))
contents.append(group([f'<div class="card" data-el="nightchamfer-card"><div class="parts"><span class="mark"><span class="seat icon" data-ph="{i}"></span></span><b class="name">{n}</b><p class="note">{d}</p></div></div>' for i,(n,d) in enumerate([('업무 맥락 이해','우리 팀의 문서·대화를 바탕으로<br>맥락에 맞게 답변'),('끊김 없는 통합','업무 데이터를 외부 학습에<br>쓰지 않고 격리 처리'),('안전한 보안','미리워크 안에서 앱 전환 없이<br>곧바로 사용')],1)]))
contents.append(el('architecture','arch','<div class="layer"><b class="name">시장의 문제</b><span class="chip">범용 AI 도구는 업무 맥락을 모르고, 별도 구독·보안<br>우려로 기업 도입이 어렵습니다.</span></div><div class="layer"><b class="name">당사 전략</b><span class="chip">미리워크 유료 플랜에 ‘미리AI’를 추가로 제공해,<br>기존 고객 기반에서 즉시 매출을 확장합니다.</span></div>',1,1,6,6)+el('architecture','arch','<div class="layer"><b class="name">미리 AI 추가 제공</b></div><div class="layer"><b class="name">기존 플랜에 추가 과금</b><span class="chip">사용량<br>기반</span><span class="chip">팀 단위<br>정액</span><span class="chip">엔터프라<br>이즈 맞춤</span></div>',7,1,6,6))
contents.append(el('pyramid','pyramid',''.join(f'<div class="level"><b class="name">{n}</b><p class="note"><b>{k}</b> |　{d}</p></div>'for n,k,d in [('4단계','외부 확장','레퍼런스와 입소문을 지렛대로 신규, 기업 고객까지 확대'),('3단계','조직 표준화','팀을 넘어 회사 표준 도구로 정착시켜 객단가 상승'),('2단계','팀 확산','한 명의 사용 경험이 팀 전체로 번지는 협업 기반 자연 확산'),('1단계','내부 침투','기존 유저에게 무료로 노출해 진입 비용 최소화')])))
contents.append(el('positioning','posmap','<div class="axis-x"><span>업무 맥락 이해도 낮음</span><span>업무 맥락 이해도 높음</span></div><div class="axis-y"><span>협업툴 통합도 낮음</span><span>협업툴 통합도 높음</span></div>'+''.join(f'<div class="mark {"on"if n=="미리 AI"else "tone-1"if n=="경쟁사 C"else ""}" style="--x:{x};--y:{y}"><b class="name">{n}{"<small>높은 맥락 이해 +<br>완전 통합으로 차별화</small>"if n=="미리 AI"else ""}</b></div>'for n,x,y in [('경쟁사 A',24,73.65),('경쟁사 B',38.22,26.69),('경쟁사 C',69.33,65.87),('경쟁사 D',76.78,12.16),('미리 AI',95.28,89.53)])))
contents.append(el('timeline','track',''.join(f'<div class="stop {"on"if i==4 else ""}"><p class="kick">{i}분기</p><b class="name">{n}</b><p class="note">{d}</p></div>'for i,(n,d)in enumerate([('AI 베타 오픈','기존 고객을 대상으로 회의록·<br>문서 요약 기능을 우선 공개합<br>니다.'),('유료 서비스 출시','사용량 기반 과금 모델을 적용<br>한 정식 서비스를 출시합니다.<br><br>핵심 기능을 고도화하고 안정<br>적인 수익 모델을 구축합니다.'),('신규 고객 확대','AI 기능을 활용한 마케팅을 강화<br>하여 신규 가입을 확대합니다.<br><br>다양한 프로모션과 콘텐츠를 통<br>해 서비스 이용률을 높입니다.'),('엔터프라이즈 진출','본격적으로 기업 전용 모델과 보<br>안 패키지를 기반으로 B2B 시장<br>을 공략합니다.<br><br>대규모 고객사를 확보하며 엔터프<br>라이즈 사업을 본격 확대합니다.')],1))))
contents.append('<div class="stack" style="'+grid(1,1,5,6)+'">'+innercard('AI 서비스 신규 매출','이곳에 해당 수치<br>관련 상세 내용을<br>입력해 보세요.','30억 원')+innercard('유료 고객 비율','이곳에 해당 수치<br>관련 상세 내용을<br>입력해 보세요.','25%')+'</div>'+el('card','card','<div class="parts"><b class="name">객단가 상승</b><div class="note"><p>AI 도입 전 대비<br>330% 상승</p>'+el('chart-bar','bars','<div class="bar" style="--v:15"><b>월 약1.5만 원</b><span>도입 전</span></div><div class="bar on" style="--v:50"><b>월 약5만 원</b><span>도입 후</span></div>',data=';--max:50')+'</div></div>',6,1,7,6))
contents.append(el('hierarchy','org','<div class="root">대표이사<br>(CEO)</div>'+''.join(f'<div class="branch"><div class="node">{n}</div><div class="leaf">{d}</div></div>'for n,d in [('AI 연구팀','LLM·ML 엔지니어<br>10명'),('프로덕트팀','AI 기능 기획·UX<br>8명'),('영업·마케팅팀','B2B 영업·그로스<br>8명'),('고객성공팀 (CS)','온보딩·기술지원<br>5명')])))
contents.append(group([f'<div class="card" data-el="nightchamfer-card"><div class="parts"><p class="kick">Benefit 0{i}</p><b class="name">{n}</b><span class="mark"><span class="seat icon" data-ph="{i}"></span></span><p class="note">{d}</p></div></div>' for i,(n,d) in enumerate([('신규 매출','기존 유료 고객의 25%가 AI 애드온을<br>추가 구독해, 신규 획득 비용 없이 하반기<br>30억 원의 추가 매출을 확보합니다.'),('고객 생산성 향상','반복 업무를 자동화해 팀당 주 5시간<br>이상을 절감합니다. 고객 만족도와<br>재구독률 (리텐션) 상승으로 이어집니다.'),('경쟁 우위',"'AI가 내장된 협업툴'이라는 차별화로 신규<br>가입 전환을 끌어올리고, 전환 비용을 높여<br>고객 이탈을 방어합니다.")],1)]))
contents.append(el('versus','versus','<div class="side"><b class="name">위험 요인</b>'+items([('AI 정확도','부정확한 답변(환각)으로 인한 신뢰 저하 우려'),('AI 비용','LLM 호출 비용이 수익성을 압박할 가능성 존재'),('데이터 보안','업무 데이터 외부 유출에 대한 고객 우려')],'list divided')+'</div><b class="vs">→</b><div class="side on"><b class="name">대응 방안</b>'+items([('','출처 표기·검증 단계·사용자 피드백 루프로 보완'),('','사용량 과금·경량 모델 병행으로 마진 확보'),('','데이터 격리·미학습 정책·보안 인증으로 신뢰 확보')],'list divided')+'</div>'))
contents.append(el('delta','delta','<span class="from"><b>협력사</b><small>사용자 접점·도메인</small></span><span class="to"><b>미리컴퍼니</b><small>기타 인프라 지원</small></span>',1,1,12,4)+callout('클라우드 파트너에게는 <b>대규모 실사용 환경을 제공</b>하고, 미리컴퍼니는 <b>안정적 인프라와 기술을 확보</b>합니다.'))
contents.append(None)
titles=[('',''),('',''),('현재 주요 사업',"미리컴퍼니는 협업 SaaS '미리워크'를 운영하며 누적 12만 팀, 유료 고객 3,200곳을 확보했습니다."),('사업 추진 배경','이곳에 사업 추진 배경 방향성에 대한 내용을 간략하게 정리하여 작성해보세요.'),('시장 분석','AI 업무 도구 시장이 협업툴보다 2배 이상 빠르게 성장하고 있습니다.'),('사업 개요','미리워크 안에서 바로 쓰는 AI 생산성 서비스'),('고객 분석','1차 타깃은 이미 미리워크를 쓰는 12만 팀입니다.'),('핵심 가치와 차별성',"미리AI는 맥락·통합·보안에서 범용 AI 도구와 다릅니다."),('비즈니스 모델','기존 구독에 얹는 AI 프리미엄 서비스로 고객 객단가를 높입니다.'),('시장 진입 전략','기존 고객에서 시작해 신규·기업 시장으로 확장합니다.'),('경쟁 환경 및 자사 포지션',"범용 AI와 협업툴 사이, 미리AI는 업무 맥락 특화 영역을 차지합니다."),('추진 로드맵','하반기 베타부터 엔터프라이즈 출시까지 분기별로 추진합니다.'),('매출 및 성과 목표','미리AI는 하반기 신규 매출의 핵심 동력입니다.'),('팀 조직 역량','미리AI는 전담 AI 조직이 책임지고 실행합니다.'),('기대 효과','미리AI는 매출·고객·경쟁력 세 측면에서 효과를 만듭니다.'),('위험 요인 및 대응 방안','신규 AI 사업의 핵심 리스크에 대응 체계를 갖췄습니다.'),('협력 제안','AI 모델·인프라 파트너와 함께 미리AI를 성장시킵니다.'),('','')]
for i,content in enumerate(contents,1):
 top='<div class="top"><span class="deck"><svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M3 18V7c0-3 3-3 5 0l4 7 4-7c2-3 5-3 5 0v11"/></svg>MiRi COMPANY</span></div>'
 if content is None:
  body=top+('<div class="lockup at-top-left"><p class="kicker">MIRIAI, 2080’S NEW GROWTH ENGINE</p><h1 class="title">MIRICOMPANY</h1><p class="lead">사업 계획 설명회</p></div><p class="meta">2080. 07. 11<br>www.miricompany.com</p>'if i==1 else '<div class="lockup at-top-left"><h1 class="title">Thank you</h1><p class="lead">경청해 주셔서 감사합니다.</p></div><p class="meta"><svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="m2 11 10-9 10 9-2 2-2-2v11h-6v-7H9v7H4V11Z"/></svg>　미리컴퍼니 사업개발팀<br><svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 3h4l2 5-3 2a15 15 0 0 0 6 6l2-3 5 2v4c-1 6-20-4-18-14Z"/></svg>　02.1234.5678<br><svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M2 4h20v16H2Zm1 1 9 8 9-8M3 19l6-7m12 7-6-7"/></svg>　제휴·투자 문의 partner@miridih.com<br>　　일반 문의 hello@miridih.com</p>')+'<div class="seat back" data-ph="1"></div>';cover=' cover'
 else:
  t,l=titles[i-1]
  if i==6:content=re.sub(r'(<div class="(?:card|frame)" data-el="[^"]*") style="[^"]*"',r'\1',content)
  body=top+(f'<header class="head"><p class="kicker"><span class="seat avatar" data-ph="1"></span></p><h1 class="title">{t}</h1><p class="lead">{l}</p></header>'if t else '')+f'<div class="body">{content}</div>';cover=''
 if i in (7,13):
  old=f'<header class="head"><p class="kicker"><span class="seat avatar" data-ph="1"></span></p><h1 class="title">{t}</h1><p class="lead">{l}</p></header>'
  new=f'<header class="head"><p class="kicker"><span class="seat avatar" data-ph="1"></span></p><h1 class="title">{t} <span class="label">{l}</span></h1></header>'
  body=body.replace(old,new)
 html=f'<!doctype html><html lang="ko"><meta charset="utf-8"><link rel="stylesheet" href="../fonts/fonts.css"><link rel="stylesheet" href="collection.css"><section class="slide dark{cover}" style="{PAL}"><div class="page">{body}</div></section></html>'
 # Browser default page margin is reset by a standalone stylesheet identical to preview framing; it does not style slide contents.
 html=html.replace('<section','<body style="margin:0"><section',1)+'</body>'
 html=re.sub(r'data-ph="[^"]*"','data-ph=""',html)
 (P/f'slide_{i:02}.html').write_text(html)
print('reassembled',len(contents))
