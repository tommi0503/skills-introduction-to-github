from pathlib import Path
import json,re,sys,importlib.util
R=Path(__file__).parent;C=R.parent/'halo-field';REF=Path('/workspace/work/ref'); ID='halo-field';F='http://127.0.0.1:8765/fonts/fonts.css'
spec=importlib.util.spec_from_file_location('preview',REF/'tools/preview.py');pr=importlib.util.module_from_spec(spec);spec.loader.exec_module(pr)
steps=json.load(open(REF/'contract/type-steps.json'));palette=json.load(open(REF/'contract/palette.json'))
L=R/'library';L.mkdir(exist_ok=True)
for mode in ['light','dark']:
 sheet=pr.sheet(C,steps,palette,dark=mode=='dark',fonts_href=F)
 (L/(mode+'.html')).write_text(sheet)
 articles=re.findall(r'<article>.*?</article>',sheet,re.S)
 head=sheet.split('<body>')[0]
 for folder in ['foundation']+[p.name for p in sorted((C/'elements').iterdir())]:
  aa=[a for a in articles if re.search(r'<h2>'+re.escape(folder)+r' /',a)]
  expanded=[]
  for a in aa:
   expanded.append(a.replace('</h2>',' · 12×6</h2>'))
   if folder!='foundation':
    mn=re.search(r'min (\d+)x(\d+)',a)
    if mn:
     small=re.sub(r'grid-column:[^;\"]+',f'grid-column:1 / span {mn[1]}',a,count=1)
     small=re.sub(r'grid-row:[^;\"]+',f'grid-row:1 / span {mn[2]}',small,count=1)
     expanded.append(small.replace('</h2>',' · minimum</h2>'))
  aa=expanded
  out=L/folder;out.mkdir(exist_ok=True)
  override='<style>body{width:1280px;height:720px;overflow:hidden;padding:0;gap:0;grid-template-columns:repeat(4,320px);align-content:start}article{padding:8px}h2{margin:0;height:22px;font-size:11px}.frame{width:304px;height:171px}.frame>.slide{transform:scale(.2375)}</style>'
  (out/(mode+'.html')).write_text(head+override+'<body>'+''.join(aa)+'</body></html>')
# separate user style: colors are not part of collection
p=palette['light'].copy();p={k:(re.sub(r' [0-9.]+\)$',' 165)',v) if k.startswith('--a1-') and v.startswith('oklch') else v) for k,v in p.items()};p.update({'--a1':'#00c79b','--a1-on':'#092b20','--page':'#ffffff','--ink':'#080e0b'})
style='.slide{'+''.join(f'{k}:{v};' for k,v in p.items())+''.join(f'--type-{x}:{x}px;' for x in steps)+'}'
(R/'reassembled').mkdir(exist_ok=True)
(R/'reassembled'/'style-palette.css').write_text(style)
links='<link rel="stylesheet" href="'+F+'"><link rel="stylesheet" href="style-palette.css"><link rel="stylesheet" href="../../halo-field/kit/css/tokens.css"><link rel="stylesheet" href="../../halo-field/foundation/foundation.css">'+''.join(f'<link rel="stylesheet" href="../../halo-field/elements/{d.name}/element.css">' for d in sorted((C/'elements').iterdir()))
# put palette after kit so only user color takes precedence
links=links.replace('<link rel="stylesheet" href="style-palette.css">','')+'<link rel="stylesheet" href="style-palette.css">'
def E(folder,cls,inside,style='',extra=''):
 return f'<div class="{cls}" data-el="{ID}-{folder}"'+(f' style="{style}"' if style else '')+f' {extra}>{inside}</div>'
def pos(col=1,w=12,row=1,h=6):return f'grid-column:{col} / span {w}; grid-row:{row} / span {h}'
def group(items,style=pos(),cls='group'):return f'<div class="{cls}" style="{style}">'+''.join(items)+'</div>'
def parts(k,n,note,fig='',mark=''):
 return '<div class="parts">'+(f'<p class="kick">{k}</p>' if k else '')+(f'<b class="fig">{fig}</b>' if fig else '')+(f'<span class="mark">{mark}</span>' if mark else '')+f'<p class="name">{n}</p><p class="note">{note}</p></div>'
def card(k,n,note):return E('card','card',parts(k,n,note))
def cover(title,kicker,lead,at='at-left'):
 return f'<section class="slide cover"><div class="page"><div class="deco"></div><div class="lockup {at}"><p class="kicker">{kicker}</p><h1 class="title">{title}</h1><p class="lead">{lead}</p></div></div></section>'
D={1:cover('브랜드 가치를 높이는<br>마케팅 전략','Integrated Marketing Solution','지속 가능한 성장을 위한 맞춤형 통합 마케팅<br>솔루션을 제안합니다.'),3:cover('시장 환경 분석 및<br>제안 배경','Marketing Proposal','01','at-top-left')}
contents=[('분석 및 기획','시장 환경의 변화<br>마케팅 목표 및 추진 방향<br>기업 및 프로젝트 팀 소개<br>우리만의 핵심 차별화'),('마케팅 전략','타겟 세분화 및 계층 구조<br>마케팅 실행 분야<br>연간 실행 로드맵<br>프로젝트 운영 프로세스'),('커리큘럼 & 실행','세부 실행 프로그램<br>채널별 집행 가이드<br>프로젝트 전담 인력'),('성과 및 계획','프로젝트 기대 효과')]
D[2]=E('agenda','agenda',''.join(f'<div class="entry"><span class="mark">0{i+1}</span><p class="name">{n}</p><p class="note">{d}</p></div>' for i,(n,d) in enumerate(contents)),pos())
D[4]=E('prose','prose','<p><b>마케팅 투자 비중과 매출 성장률</b></p><p>통합 마케팅을 지속한 기업일수록 브랜드 전환율과 장기 매출 성장세가 뚜렷하게 나타납니다.</p>',pos(1,4,row=1,h=4))
D[4]+=E('chart-bar','bars',''.join(f'<div class="bar" style="--v:{v}"><b>{v}</b><span>{2023+i}</span></div>' for i,v in enumerate([120,200,310,580])),pos(5,8,row=3,h=4)+';--max:650')+E('headline','headline','<h2>연도별 마케팅 투자 대비 매출 성과 추이</h2>',pos(5,8,row=1,h=1))+E('legend','legend','<span class="key tone-1">마케팅 성과 매출액</span><span class="key tone-2">평균 고객 전환율</span>',pos(5,8,row=2,h=1))+E('chart-line','lines',''.join(f'<div class="pt" style="--v:{v}"><b>{v}</b><span></span></div>' for v in [180,240,350,650]),pos(5,8,row=3,h=4)+';--max:800')
D[5]=group([card(f'Goal 0{i+1}.',n,d) for i,(n,d) in enumerate([('브랜드 인지도 제고','타겟 고객 접점 확대 및 차별적 브랜드 이미지 구축.<br><br>다양한 디지털 채널을 통해 브랜드 노출을 확대합니다.'),('전환율 극대화','데이터 기반의 정밀 타겟팅을 통한 실질적 구매 전환.<br><br>사용자 행동 데이터를 분석하여 최적의 경험을 제공합니다.'),('팬덤 형성','지속적인 소통 및 커뮤니티 운영을 통한 재구매율 향상.<br><br>고객과의 유대감을 형성합니다.')])])
D[6]=E('cycle','cycle','<div class="core">핵심 가치</div>'+''.join(f'<div class="node"><p class="name">{n}</p><p class="note">{en}</p></div>' for n,en in [('실용성','PRACTICAL'),('전문성','PROFESSIONAL'),('협력','PARTNERSHIP')]),pos(1,5))+E('image-frame','frame','<div class="seat" data-ph="1"></div>',pos(6,7))
cs=[('맞춤형 전략 수립','정밀한 데이터 분석 기반의 미디어 믹스 설계'),('실무 중심 실행','검증된 채널과 매체를 활용한 신속한 운영'),('크리에이티브 마케팅','시선을 사로잡는 독창적 콘텐츠 제작'),('성과 및 ROI 관리','실시간 리포팅을 통한 실행 성과 측정 및 최적화')]
D[7]=group([card(f'0{i+1}',n,d) for i,(n,d) in enumerate(cs[:2])],pos(row=1,h=3))+group([card(f'0{i+3}',n,d) for i,(n,d) in enumerate(cs[2:])],pos(row=4,h=3))
D[8]=E('pyramid','pyramid',''.join(f'<div class="level"><p class="name">{n}</p><p class="note">{d}</p></div>' for n,d in [('VIP','충성 고객'),('LOYAL','재구매 고객'),('POTENTIAL','잠재 고객'),('NEW','신규 유입')]),pos(1,5))+group(['<div class="split">'+E('pill','pill on',parts('',n,''))+E('prose','prose',f'<p>{d}</p>')+'</div>' for n,d in [('VIP (충성 고객)','브랜드 앰배서더 및 전용 혜택 제공'),('LOYAL (재구매 고객)','리텐션 마케팅 및 리워드 프로그램'),('POTENTIAL (잠재 고객)','프로모션 및 개인화 콘텐츠 연결'),('NEW (신규 유입)','대중 노출 캠페인 및 인지도 확보')]],pos(6,7),cls='stack')
D[9]=E('steps','steps',''.join(f'<div class="step"><span class="mark">STEP 0{i+1}</span><p class="name">{n}</p><p class="note">{d}</p></div>' for i,(n,d) in enumerate([('퍼포먼스 광고','정밀 타겟 캠페인'),('SNS 브랜딩','브랜드 소통 강화'),('SEO 최적화','검색 노출 개선'),('콘텐츠 제작','가치 있는 정보 전달'),('바이럴 마케팅','자발적 참여 확산'),('CRM 관리','지속적인 관계 구축')])),pos())
D[10]=E('timeline','track',''.join(f'<div class="stop"><p class="kick">{i+1}Q</p><p class="name">{n}</p><p class="note">{d}</p></div>' for i,(n,d) in enumerate([('기반 구축','시장 현황 진단 및 경쟁사 미디어 전략 분석. 타겟 페르소나 정의 및 핵심 메시지 도출.'),('인지도 확산','주요 매체 중심의 검색 및 디스플레이 광고 집행. 브랜드 콘텐츠와 숏폼 캠페인 운영.'),('전환 극대화','시즌 프로모션 및 CRM 연동. 고객 행동 데이터에 기반한 리타겟팅 운영.'),('성과 분석 & 재정비','연간 데이터 리포트 도출 및 차년도 기획. 고객 피드백을 기반으로 성과 개선.') ])),pos())
D[11]=E('steps','steps',''.join(f'<div class="step"><span class="mark">{i+1}</span><p class="name">{n}</p><p class="note">{d}</p></div>' for i,(n,d) in enumerate([('니즈 분석','사전 진단 인터뷰 진행 및 브랜드 과제 파악'),('전략 기획','맞춤형 미디어 믹스 및 예산 배분안 수립'),('캠페인 집행','광고 소재 제작 및 주요 매체 라이브 집행'),('성과 평가','주간·월간 핵심 지표 측정'),('사후 관리','픽셀 데이터 기반의 리타겟팅 운영')])),pos())
D[12]=E('callout','callout','<p>온라인 매출 전년 대비 <b>150% 증대</b> 및 브랜드 인지도 강화</p>',pos(row=1,h=1))+group([E('headline','headline',f'<p class="kick">0{i+1}</p><h2>{n}</h2>') for i,n in enumerate(['검색 광고','디스플레이','숏폼 콘텐츠','체험단 운영'])],pos(row=2,h=2))+group([E('image-frame','frame',f'<div class="seat" data-ph="{i+1}"></div>') for i in range(4)],pos(row=4,h=3))
rows=[('SNS 매체','2030 세대 / 감성 소비층','트렌디한 숏폼 및 카드뉴스 기반 브랜드 브랜딩','매일 상시'),('검색 매체','구매 의도가 명확한 유저','검색 키워드를 통한 전환 및 구매 유도','상시 집행'),('디스플레이','넓은 대중 유저층','핵심 소구 메시지를 통한 관심 유발','주 3–4회'),('영상 매체','전 연령층 / 고관여 타겟','브랜드 스토리텔링 및 제품정보 콘텐츠 활용','주 2회'),('커뮤니티','정보 탐색형 유저','실제 사용 후기 기반 신뢰도 제고','주 4–8회'),('CRM 채널','기존 충성 및 재구매 고객','개인화 쿠폰 및 시즌 프로모션 알림 발송','격주/월 2회')]
D[13]=E('table','tablebox','<table class="table"><thead><tr>'+''.join(f'<th>{x}</th>' for x in ['주요 매체','주 타겟층','핵심 집행 전략','집행 주기'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{x}</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>',pos())
D[14]=E('person','people',''.join(E('person','person',f'<div class="seat portrait" data-ph="{i+1}"></div><p class="name">{n}</p><p class="note">{d}</p>') for i,(n,d) in enumerate([('김미리','총괄 디렉터 · 퍼포먼스 마케팅 10년 차 / 대기업 캠페인 총괄'),('박미리','수석 매니저 · 콘텐츠 기획 및 바이럴 전문가 / 누적 집행 300억+'),('이미리','데이터 분석가 · ROI 극대화 및 데이터 트래킹 전담')])),pos())
D[15]=E('chart-donut','donuts',''.join(E('chart-donut','donut',f'<b class="fig">{fig}</b><p class="name">{n}</p>',f'--v:{v}') for n,fig,v in [('ROI','320%',80),('전환율','4.5%',4.5),('신규 유입','10만+',100)]),pos(row=1,h=4))+group([E('prose','prose',f'<p>{n}</p>') for n in ['브랜드 인지도 및 선호도 상승','신규 고객 유입량 및 구매 전환율 대폭 개선','자사몰 데이터 확보를 통한 장기적 자산화']],pos(row=5,h=2))
titles=json.load(open(R/'slides.json'))
for n,body in D.items():
 if n not in [1,3]:
  k,t,lead=titles.get(str(n),['목차','CONTENTS',''])
  body=f'<section class="slide"><div class="page"><header class="head"><p class="kicker">{k}</p><h1 class="title">{t}</h1><p class="lead">{lead}</p></header><div class="body">{body}</div></div></section>'
 (R/'reassembled'/f'slide_{n:02}.html').write_text('<!doctype html><html lang="ko"><head><meta charset="utf-8">'+links+'</head><body style="margin:0">'+body+'</body></html>')
print('review pages generated')
