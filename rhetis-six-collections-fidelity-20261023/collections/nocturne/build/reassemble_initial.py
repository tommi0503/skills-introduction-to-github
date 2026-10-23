from pathlib import Path
import json,shutil,html
B=Path('/workspace/work/deliverables/nocturne');C=B/'collection/nocturne';R=B/'review';D=R/'reassembled';D.mkdir(exist_ok=True)
A=R/'assets/collection'
for p in C.rglob('*.css'):
 q=A/p.relative_to(C);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy(p,q)
for n in ['icons-runtime.js','LUCIDE-LICENSE.txt']:
 src=Path('/workspace/work/tools')/n
 if src.exists():shutil.copy(src,R/'assets'/n)
palette=json.loads(Path('/workspace/work/reference/contract/palette.json').read_text())['dark'];palette.update({'--page':'#000000','--ink':'#f8fcff','--a1':'#399fee','--a1-on':'#020609','--a1-7':'#399fee','--a1-1-soft':'#08141e','--a1-2-soft':'#153e5c','--n-1':'#14191f','--n-2':'#1c232c','--n-3':'#34404a','--n-4':'#526573','--n-5':'#8695a2','--n-6':'#bfc7cd','--n-7':'#bfc7cd','--n-8':'#d8e2e9','--n-9':'#f1f6f9'})
steps=json.loads(Path('/workspace/work/reference/contract/type-steps.json').read_text())
(R/'assets/source-style.css').write_text('/* Host-supplied style only: original palette and type steps, no layout rules. */\n.slide.dark{'+''.join(f'{k}:{v};' for k,v in palette.items())+''.join(f'--type-{v:g}:{v:g}px;' for v in steps)+'}\n')
links=['../assets/fonts/fonts.css','../assets/collection/kit/css/tokens.css','../assets/collection/foundation/foundation.css']+[f'../assets/collection/elements/{p.name}/element.css' for p in sorted((C/'elements').iterdir())]+['../assets/source-style.css']
head='<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=1280"><title>Nocturne reassembled</title>'+''.join(f'<link rel="stylesheet" href="{x}">' for x in links)+'</head><body>'
# Default browser body margin is a host concern; no page CSS is added here.
head=head.replace('<body>','<body style="margin:0;width:1280px;height:720px;overflow:hidden">')
foot='<script src="../assets/icons-runtime.js"></script></body></html>'
def el(cls,folder,body,col=1,cols=12,row=1,rows=6):return f'<div class="{cls}" data-el="nocturne-{folder}" style="grid-column:{col} / span {cols}; grid-row:{row} / span {rows}">{body}</div>'
def headline(text,col=1,cols=12,row=1,rows=1,big=False):return el('headline center'+(' big' if big else ''),'headline',f'<h2>{text}</h2>',col,cols,row,rows)
def callout(body,row=6,rows=1):return el('callout','callout',f'<p>{body}</p>',1,12,row,rows)
def page(body,kicker='',title='',full=False,year=True):
 top='<div class="top"><span class="deck"><span class="icon" data-icon="hexagon"></span>MIRI COMPANY</span>'+('<span class="sec">2080 Town Hall</span>' if year else '')+'</div>'
 header=f'<header class="head'+(' center' if full else '')+f'"><p class="kicker">{kicker}</p><h1 class="title">{title}</h1></header>' if kicker or title else ''
 return '<section class="slide dark"><div class="page">'+top+header+'<div class="body">'+body+'</div></div></section>'
pages={}
pills=''.join(el('pill line','pill',f'<div class="parts"><b class="name">{x}</b></div>') .replace(' style="grid-column:1 / span 12; grid-row:1 / span 6"','') for x in ['시장진입','파일럿 운영','본격 확장'])
pages[19]=page(headline('<b>New Challenge</b>',row=1,rows=1)+headline('<b>프로젝트</b> 더 미리',row=2,rows=3,big=True)+el('prose lead','prose','<p>하반기 우리가 새롭게 시작하는 도전입니다.<br>이곳에 프로젝트 소개를 입력해 보세요.</p>',row=4,rows=1)+f'<div class="group" style="grid-column:4 / span 6; grid-row:5 / span 2">{pills}</div>')
stat=''.join(f'<div class="stat" data-el="nocturne-metric"><div class="parts"><b class="fig">{v}</b><p class="name">{n}</p></div></div>' for n,v in [('매출','000건'),('신규 고객','000명'),('만족도','000점')])
pages[20]=page(el('stats','metric',stat,row=1,rows=5)+callout('이곳에 2080 하반기 목표에 대한 설명을 입력해 보세요.'),'함께 만들어갈 숫자','2080 하반기 목표')
values=''.join(f'<div class="card quiet" data-el="nocturne-card"><div class="parts"><div class="mark"><div class="seat" data-ph="{i}"></div></div><p class="kick">keyword 0{i}</p><p class="name">{t}</p><p class="note">이곳에 설명을 입력해 보세요.</p></div></div>' for i,t in enumerate(['고객이<br>최우선입니다.','함께 더 멀리<br>갈 수 있습니다.','실행만이<br>증명합니다.'],1))
pages[21]=page(f'<div class="group" style="grid-column:1 / span 12; grid-row:1 / span 6">{values}</div>','함께 만드는 성장','우리가 믿는 것',full=True)
items=''.join(f'<div class="item"><p class="name">{t}</p></div>' for t in ['쉽지 않은 반년이었습니다.','그럼에도 포기하지 않고 달려온 여러분이 있어','우리는 여기까지 올 수 있었습니다.','이곳에 구성원에게 전하는 메시지를 입력해 보세요.'])
pages[22]=page('<div class="seat back" data-ph="1" style="grid-column:1 / span 12; grid-row:3 / span 4"></div>'+el('list divided','list',items,row=1,rows=5),'함께하는 모든 분께','구성원에게 전하는 말')
pages[23]=page(headline('<b>의견과 피드백을 환영합니다!</b>',row=1,rows=1)+headline('Q&amp;A',row=2,rows=3,big=True)+callout('<b>프레젠테이션에 관한 질문을 자유롭게 해주세요.</b><br>이곳에 진행 방식을 입력해 보세요.',row=5,rows=2))
pages[24]='''<section class="slide dark cover"><div class="page"><div class="top"><span class="deck"><span class="icon" data-icon="hexagon"></span>MIRI COMPANY</span></div><div class="lockup at-center"><h1 class="title"><b>MIRI</b> COMPANY</h1><p class="lead">이곳에 <b>회사 슬로건</b>을 입력해 보세요.</p></div><div class="deco"></div><p class="meta">2099.00.00</p></div></section>'''
for n,body in pages.items():(D/f'slide_{n}.html').write_text(head+body+foot)
(R/'reassembly-map.md').write_text('''# 재조립 매핑\n\n|원본|컬렉션 요소|\n|---|---|\n|19|headline / prose / pill|\n|20|foundation head / metric / callout|\n|21|foundation full-width centered head / card.quiet with photo seats|\n|22|foundation head / list.divided / seat.back|\n|23|headline / callout|\n|24|foundation cover lockup / deco / meta|\n\n모든 콘텐츠 요소는 계약 마크업과 nocturne data-el을 사용한다. 본문 직계 배치는 grid-column/grid-row뿐이다. source-style.css는 원본 팔레트와 타입 단계만 공급한다. 요소/배치용 추가 CSS는 없다.\n''')
print('Reassembled six original pages using collection CSS only')
