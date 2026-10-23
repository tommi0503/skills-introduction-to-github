"""Source 25–29 fidelity compositions; merge into collection, never page-local CSS.
Owned by integration QA. Main collection owner merges/normalizes CSS and adds fixtures.
All markup uses existing foundation and element contracts. No page IDs/classes.
"""
from pathlib import Path
from html import escape
PROJECT=Path(__file__).resolve().parent
TOKEN_DEFAULTS={'--meridian-deck-tail-ring':'var(--n-4)'}
ELEMENT_PATCHES={}
FIXTURES={}

def el(cls,typ,inner,style=''):
 return f'<div class="{cls}" data-el="meridian-deck-{typ}"'+(f' style="{style}"' if style else '')+'>'+inner+'</div>'
def pill(text,variant='quiet'):
 return el('pill '+variant,'pill','<div class="parts"><p class="name">'+text+'</p></div>')
def lis(texts):
 return el('list','list',''.join('<div class="item"><p class="name">'+t+'</p><p class="note"></p></div>' for t in texts))
def headline(text,variant='center',style='grid-column:1 / span 12;grid-row:1 / span 1'):
 return el('headline '+variant,'headline','<h2>'+text+'</h2>',style)
def prose(text,variant='',style=''):
 return el('prose '+variant,'prose','<p>'+text+'</p>',style)
def grid(inner,cls='group',c='1 / span 12',r='1 / span 6'):
 return f'<div class="{cls}" style="grid-column:{c};grid-row:{r}">'+inner+'</div>'

BODIES={}
left25=[]
for title,items in [
 ('배송 시스템 개선',['물류사 협업 체계 강화','실시간 배송 추적 시스템 고도화','성수기 물량 대응 프로세스 구축']),
 ('응대 표준화',['관련 내용을 이곳에 입력하세요']*3),
 ('결제 오류 해결',['간편결제 연동 안정화','결제 오류 시 즉시 복구 시스템 구축','오류 발생 시 안내 메시지 개선']),
 ('반품 과정 간소화',['관련 내용을 이곳에 입력하세요']*3)]:
 left25.append('<div class="group">'+pill(title)+lis(items)+'</div>')
marks25=[]
# Data describes the source's true 0–100 coordinates; CSS no longer compresses the domain.
for x,y,t in [(86.65,92.0,'배송 시스템<br>개선'),(54.4,77.3,'간편 결제<br>오류 해결'),(74.65,61.5,'CS 응대<br>표준화'),(46.5,47.5,'반품 프로세스<br>간소화')]:
 marks25.append(f'<div class="mark on" style="--x:{x};--y:{y}"><b class="name">{t}</b></div>')
pos=el('posmap','positioning','<div class="axis-x"><span></span><span>높음</span></div><div class="axis-y"><span>높음</span><span>낮음</span></div>'+''.join(marks25))
BODIES[25]=grid('<div class="stack">'+''.join(left25)+'</div><div class="stack">'+pill('실행용이성 사분면','on')+pos+prose('실행용이성')+prose('영향도')+'</div>','split')

cols26=[]
for value in [80,70,75,91]:
 donut=el('donut','chart-donut',f'<p class="fig">{value}<small>%</small></p><p class="name"></p>',f'--v:{value}')
 cols26.append('<div class="stack">'+pill('키워드','on' if value==91 else 'quiet')+prose('업무별 성과 달성률이나<br>예산 집행률 표현에 좋아요.')+donut+'</div>')
BODIES[26]=headline('프로젝트와 관련된 내용을 기재하고<br><b>강조할 내용은 포인트 컬러를 활용하세요</b>')+grid(''.join(cols26),'group','1 / span 12','2 / span 5')

cols27=[]
for i in range(1,4):
 frame=el('frame','image-frame',f'<div class="seat" data-ph="{i}"></div>')
 card=el('card quiet','card','<div class="parts"><p class="name">타이틀 텍스트 입력</p><p class="note">내용을 텍스트로 간략하게 입력해주세요.<br>관련 내용을 텍스트로 간략하게 입력해주세요.<br>내용을 텍스트로 간략하게 입력해주세요.</p></div>')
 cols27.append('<div class="stack">'+frame+card+'</div>')
BODIES[27]=grid(''.join(cols27),'group three')

names28=['물류 중계 거점 확대','AI 기반 배송 최적화','멀티 물류사 통합 관리','고객 맞춤 배송 서비스']
row28=el('flowchart','flowchart',''.join(f'<div class="node to-r" style="grid-column:{i};grid-row:1">{n}</div>' for i,n in enumerate(names28,1)))
panels28=[]
for i in range(4):
 text=lis(['개선과제의 상세내용을 넣어보세요.']*2)
 if i==0:
  content=el('delta','delta','<span class="from">2개소</span><span class="to">5개소</span>')
 elif i==1:
  content='<div class="stack">'+pill('AI 활용')+pill('AI 활용')+'</div>'
 elif i==2:
  content=el('org','hierarchy','<div class="root">물류사 A</div>'+''.join('<div class="branch"><div class="node">'+x+'</div></div>' for x in ['A','B','C']))
 else:
  content='<div class="stack">'+pill('배송 서비스','on')+pill('배송 서비스','on')+'</div>'
 panels28.append('<div class="stack">'+text+content+'</div>')
top28='<div class="group">'+pill('물류·배송 인프라 혁신')+pill('디지털 플랫폼 고도화','on')+'</div>'
bottom28=el('callout','callout','<p>전체 예상 투자 규모: <b>XX억원</b>　│　연간 기대 효과: <b>매출 증대 XX억원, 비용 절감 XX억원</b></p>')
BODIES[28]=grid(top28+row28+'<div class="group">'+''.join(panels28)+'</div>'+bottom28,'stack')

people29=[]
for i in range(1,5):
 person=el('person','person',f'<div class="seat portrait" data-ph="{i}"></div><p class="name">부서명</p><p class="note">김미리 대리<span>프로젝트 내 역할과 담당 분야를 명시해<br>책임 소재를 밝혀주세요.</span></p>')
 people29.append(person)
BODIES[29]=headline('부서별 인재에 대해 상세 설명을 기재해주세요')+prose('* 페이지 내 인물 사진은 샘플 이미지입니다.','quiet','grid-column:10 / span 3;grid-row:1 / span 1')+el('people','person',''.join(people29),'grid-column:1 / span 12;grid-row:2 / span 5')

# Wrapper-only rules: foundation never selects an element root class.
FOUNDATION_PATCH=r'''
/* Source tail compositions: comparison/list map, four gauges, three media cards, four process panels. */
.slide .body>.split:has(>.stack>.group:nth-child(4)){display:grid;grid-template-columns:423px 633px;gap:34px;transform:translate(36px,28px);width:1090px;height:423px}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:first-child{display:grid;grid-template-rows:repeat(4,118px);gap:0}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:first-child>.group{display:grid;grid-template-columns:137px 270px;column-gap:16px;align-items:start;position:relative;height:118px;min-height:0}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:first-child>.group:not(:last-child)::after{content:"";position:absolute;left:0;top:95px;width:360px;height:1px;background:var(--n-3)}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:last-child{position:relative;display:block;min-height:423px}
.slide .body>.group:has(>.stack:nth-child(4):last-child){display:grid;grid-template-columns:repeat(4,294px);gap:0;width:1176px;transform:translateX(-7px);padding-top:52px}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack{display:flex;flex-direction:column;align-items:center;gap:0;min-width:0}
.slide .body>.group.three:has(>.stack>[data-el="meridian-deck-image-frame"]){display:grid;grid-template-columns:repeat(3,350px);gap:27px;width:1104px;height:375px;box-sizing:border-box;padding:0;margin:0;border:0;background:none;transform:translate(37px,54px)}
.slide .body>.group.three:has(>.stack>[data-el="meridian-deck-image-frame"])>.stack{display:grid;grid-template-rows:203px 164px;gap:8px;width:350px;height:375px;min-height:375px;padding:0;margin:0;transform:none;background:none;border:0;border-radius:0;overflow:visible}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child){display:flex;flex-direction:column;gap:0;width:1115px;height:449px;transform:translate(25px,10px);padding:0}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:first-child{position:relative;display:block;flex:none;height:26px;min-height:26px}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:first-child::before{content:"";position:absolute;left:0;right:0;top:11px;height:4px;background:linear-gradient(to right,var(--n-7) 74.2%,var(--a1) 74.2%)}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:first-child::after{content:"";position:absolute;right:0;top:4px;width:16px;height:18px;background:var(--a1);clip-path:polygon(0 0,100% 50%,0 100%)}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3){display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:7px;height:275px;min-height:275px;flex:none;margin-top:9px}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack{position:relative;display:flex;flex-direction:column;align-items:center;gap:0;background:color-mix(in srgb,var(--n-1) 98%,var(--ink));height:275px;padding:0}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>.stack{flex:none;display:flex;flex-direction:column;gap:12px;align-items:center;width:147px;height:112px;padding:0}
'''

# Elements retain their contracted markup; selectors describe reusable compositions.
ELEMENT_PATCHES['list']=r'''
/* Compact business checklists beside neutral category capsules. */
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack>.group>[data-el="meridian-deck-list"]{padding:0;margin:0;display:flex;flex-direction:column;gap:0;align-self:start;height:auto;font-size:var(--type-14)}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack>.group>[data-el="meridian-deck-list"]>.item{display:block;position:relative;margin:0;padding:0 0 0 12px;min-height:0;border:0;line-height:1.6}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack>.group>[data-el="meridian-deck-list"]>.item::before{content:"";position:absolute;left:1px;top:9px;width:4px;height:4px;background:var(--n-7);border-radius:50%;margin:0;transform:none}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack>.group>[data-el="meridian-deck-list"] .name{font-size:var(--type-14);font-weight:var(--body-weight);line-height:1.6;color:var(--n-7);margin:0}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack>.group>[data-el="meridian-deck-list"] .note{display:none}
/* Two observations remain visible above each process detail. */
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-list"]{flex:none;display:block;width:240px;height:62px;margin:31px 0 12px;padding:0;font-size:var(--type-14)}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-list"]>.item{position:relative;display:block;padding:0 0 0 12px;margin:0;min-height:25px;border:0}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-list"]>.item::before{content:"";position:absolute;left:0;top:10px;width:4px;height:4px;border-radius:50%;background:var(--n-7);margin:0;transform:none}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-list"] .name{font-size:var(--type-14);font-weight:var(--body-weight);line-height:1.8;color:var(--n-7);margin:0;white-space:nowrap}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-list"] .note{display:none}
'''
ELEMENT_PATCHES['pill']=r'''
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack>.group>[data-el="meridian-deck-pill"]{height:27px;width:137px;padding:0;margin-top:3px;min-height:0;border:0;background:var(--n-7);color:var(--page);border-radius:999px;flex:none}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack>.group>[data-el="meridian-deck-pill"] .parts{display:flex;align-items:center;justify-content:center;padding:0;width:100%;height:100%}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack>.group>[data-el="meridian-deck-pill"] .name{font-size:var(--type-14);line-height:1.2;font-weight:var(--body-weight);color:inherit;margin:0}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:last-child>[data-el="meridian-deck-pill"]{position:absolute;left:216px;top:0;width:188px;height:39px;min-height:0;padding:0;background:var(--a1);color:var(--a1-on);border:0;border-radius:999px}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:last-child>[data-el="meridian-deck-pill"] .parts{padding:0;display:flex;align-items:center;justify-content:center;height:100%}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:last-child>[data-el="meridian-deck-pill"] .name{font-size:var(--type-20);font-weight:var(--body-weight);line-height:1.2;color:inherit;margin:0}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack>[data-el="meridian-deck-pill"]{flex:none;width:192px;height:41px;min-height:0;border:0;padding:0;background:var(--n-4);color:var(--page);border-radius:999px}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack:nth-child(2)>[data-el="meridian-deck-pill"]{background:var(--n-6)}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack:nth-child(3)>[data-el="meridian-deck-pill"]{background:var(--n-7)}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack:nth-child(4)>[data-el="meridian-deck-pill"]{background:var(--a1);color:var(--a1-on)}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack>[data-el="meridian-deck-pill"] .parts{display:flex;align-items:center;justify-content:center;height:100%;padding:0}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack>[data-el="meridian-deck-pill"] .name{font-size:var(--type-20);font-weight:var(--name-weight);line-height:1.2;color:inherit;margin:0}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:first-child>[data-el="meridian-deck-pill"]{position:absolute;top:0;left:285px;width:257px;height:26px;min-height:0;z-index:1;border:0;padding:0;background:var(--n-7);color:var(--page);border-radius:999px}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:first-child>[data-el="meridian-deck-pill"]:nth-child(2){left:904px;width:151px;background:var(--a1);color:var(--a1-on)}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:first-child>[data-el="meridian-deck-pill"] .parts{display:flex;align-items:center;justify-content:center;padding:0;height:100%}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:first-child>[data-el="meridian-deck-pill"] .name{font-size:var(--type-14);font-weight:var(--body-weight);line-height:1.2;color:inherit;margin:0}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>.stack>[data-el="meridian-deck-pill"]{flex:none;width:147px;height:50px;min-height:0;border:0;padding:0;background:var(--n-7);color:var(--page);border-radius:999px}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>.stack>[data-el="meridian-deck-pill"].on{background:var(--a1);color:var(--a1-on)}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>.stack>[data-el="meridian-deck-pill"] .parts{display:flex;align-items:center;justify-content:center;height:100%;padding:0}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>.stack>[data-el="meridian-deck-pill"] .name{font-size:var(--type-18);font-weight:var(--body-weight);line-height:1.2;color:inherit;margin:0}
'''
ELEMENT_PATCHES['positioning']=r'''
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:last-child>[data-el="meridian-deck-positioning"]{position:absolute;left:0;top:71px;width:633px;height:324px;margin:0;background:linear-gradient(to right,var(--a1-1-soft),var(--page) 49%,var(--a1-2-soft) 49%,var(--page));border:0}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:last-child>[data-el="meridian-deck-positioning"]::before{left:49%;border-color:var(--n-3)}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:last-child>[data-el="meridian-deck-positioning"]::after{top:50%;border-color:var(--n-3)}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:last-child>[data-el="meridian-deck-positioning"] .mark{left:calc(var(--x)*1%);bottom:calc(var(--y)*1%);width:89px;height:40px;min-width:0;padding:0;translate:-50% 50%;border-radius:999px;background:var(--a1);color:var(--a1-on)}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:last-child>[data-el="meridian-deck-positioning"] .mark .name{font-size:var(--type-12);line-height:1.2;font-weight:var(--body-weight);max-width:none;color:inherit}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:last-child>[data-el="meridian-deck-positioning"] .axis-x{left:0;right:0;bottom:-39px;font-size:var(--type-14);line-height:1.55;font-weight:var(--body-weight);color:var(--n-7)}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:last-child>[data-el="meridian-deck-positioning"] .axis-x>span:nth-child(2){position:static}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:last-child>[data-el="meridian-deck-positioning"] .axis-y{left:-64px;top:-3px;bottom:0;font-size:var(--type-14);line-height:1.55;font-weight:var(--body-weight);color:var(--n-7)}
'''
ELEMENT_PATCHES['headline']=r'''
.slide .body>[data-el="meridian-deck-headline"].center:has(+.group>.stack:nth-child(4)),.slide .body>[data-el="meridian-deck-headline"].center:has(~[data-el="meridian-deck-person"].people){padding:0;margin:7px 0 0;display:block;text-align:center;background:none;border:0}
.slide .body>[data-el="meridian-deck-headline"].center:has(+.group>.stack:nth-child(4)) h2,.slide .body>[data-el="meridian-deck-headline"].center:has(~[data-el="meridian-deck-person"].people) h2{font-size:var(--type-32);font-weight:var(--meridian-deck-font-weight-700);line-height:1.4;color:var(--n-7);margin:0}
.slide .body>[data-el="meridian-deck-headline"].center:has(+.group>.stack:nth-child(4)) h2 b{color:var(--a1-7);font-weight:inherit}
'''
ELEMENT_PATCHES['headline'] += r'''
.slide .body>[data-el="meridian-deck-headline"].center:has(~[data-el="meridian-deck-person"].people) h2{line-height:1.55}
'''
ELEMENT_PATCHES['prose']=r'''
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack>[data-el="meridian-deck-prose"]{flex:none;width:232px;height:47px;margin:17px 0 25px;padding:0;text-align:center;color:var(--n-7)}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack>[data-el="meridian-deck-prose"] p{font-size:var(--type-18);line-height:1.3;font-weight:var(--body-weight);margin:0}
.slide .body>[data-el="meridian-deck-prose"].quiet:has(+[data-el="meridian-deck-person"].people){display:block;justify-content:start;padding:0;margin:54px 0 0;text-align:left;color:var(--n-7)}
.slide .body>[data-el="meridian-deck-prose"].quiet:has(+[data-el="meridian-deck-person"].people) p{width:157px;font-size:var(--type-8);line-height:1.55;margin:0 0 0 auto;font-weight:var(--body-weight);color:var(--n-7)}
'''
ELEMENT_PATCHES['prose'] += r'''
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:last-child>[data-el="meridian-deck-prose"]{position:absolute;display:block;left:274px;top:410px;width:100px;height:22px;margin:0;padding:0;background:none;text-align:left;container-type:inline-size}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:last-child>[data-el="meridian-deck-prose"]:last-child{left:-64px;top:221px;width:60px}
.slide .body>.split:has(>.stack>.group:nth-child(4))>.stack:last-child>[data-el="meridian-deck-prose"] p{font-size:var(--type-14);line-height:1.55;font-weight:var(--body-weight);color:var(--n-7);margin:0;padding:0;white-space:nowrap}
'''
ELEMENT_PATCHES['chart-donut']=r'''
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack>[data-el="meridian-deck-chart-donut"]{flex:none;position:relative;width:192px;height:192px;max-width:none;max-height:none;border:0;border-radius:50%;display:grid;place-items:center;padding:0;margin:0;aspect-ratio:1;--meridian-deck-tail-ring:var(--n-4);background:conic-gradient(var(--meridian-deck-tail-ring) calc(var(--v)*1%),var(--n-1) 0)}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack:nth-child(2)>[data-el="meridian-deck-chart-donut"]{--meridian-deck-tail-ring:var(--n-6)}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack:nth-child(3)>[data-el="meridian-deck-chart-donut"]{--meridian-deck-tail-ring:var(--n-7)}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack:nth-child(4)>[data-el="meridian-deck-chart-donut"]{--meridian-deck-tail-ring:var(--a1)}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack>[data-el="meridian-deck-chart-donut"]::before{content:"";position:absolute;inset:14px;width:auto;height:auto;background:var(--page);border-radius:50%;border:0;transform:none;translate:none;clip-path:none}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack>[data-el="meridian-deck-chart-donut"]::after{content:none}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack>[data-el="meridian-deck-chart-donut"] .fig{position:relative;inset:auto;width:auto;height:auto;margin:0;display:block;font-size:var(--type-60);font-weight:var(--meridian-deck-font-weight-650);line-height:1.3;color:var(--n-7);z-index:1}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack:nth-child(4)>[data-el="meridian-deck-chart-donut"] .fig{color:var(--a1-7)}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack>[data-el="meridian-deck-chart-donut"] .fig small{font-size:var(--type-28);color:inherit;margin:0}
.slide .body>.group:has(>.stack:nth-child(4):last-child)>.stack>[data-el="meridian-deck-chart-donut"] .name:empty{display:none}
'''
ELEMENT_PATCHES['image-frame']=r'''
.slide .body>.group.three:has(>.stack>[data-el="meridian-deck-image-frame"])>.stack>[data-el="meridian-deck-image-frame"]{position:relative;display:block;width:350px;height:203px;min-height:0;max-height:none;padding:5px;border:1px solid var(--a1-4-muted);background:var(--page);border-radius:0;overflow:visible}
.slide .body>.group.three:has(>.stack>[data-el="meridian-deck-image-frame"])>.stack>[data-el="meridian-deck-image-frame"]>.seat{display:block;width:338px;height:191px;max-width:none;max-height:none;aspect-ratio:auto;background:var(--n-2);border-radius:0}
.slide .body>.group.three:has(>.stack>[data-el="meridian-deck-image-frame"])>.stack>[data-el="meridian-deck-image-frame"]>.seat::before{content:attr(data-ph);position:absolute;left:50%;top:50%;translate:-50% -50%}.slide .body>.group.three:has(>.stack>[data-el="meridian-deck-image-frame"])>.stack>[data-el="meridian-deck-image-frame"]>.seat::after{content:none}
.slide .body>.group.three:has(>.stack>[data-el="meridian-deck-image-frame"])>.stack>[data-el="meridian-deck-image-frame"]::before{content:"";position:absolute;left:-5px;top:-7px;width:33px;height:33px;border:0;border-radius:50%;background:var(--a1);z-index:2}
.slide .body>.group.three:has(>.stack>[data-el="meridian-deck-image-frame"])>.stack>[data-el="meridian-deck-image-frame"]::after{content:"";position:absolute;left:5px;top:3px;width:13px;height:13px;z-index:3;background:linear-gradient(var(--a1-on),var(--a1-on)) center/2px 13px no-repeat,linear-gradient(var(--a1-on),var(--a1-on)) center/13px 2px no-repeat;transform:none}
'''
ELEMENT_PATCHES['card']=r'''
.slide .body>.group.three:has(>.stack>[data-el="meridian-deck-image-frame"])>.stack>[data-el="meridian-deck-card"].quiet{position:relative;display:block;width:350px;height:164px;min-height:0;padding:17px 20px 0;background:var(--n-1);border:0;border-radius:0;box-shadow:none;text-align:center}
.slide .body>.group.three:has(>.stack>[data-el="meridian-deck-image-frame"])>.stack>[data-el="meridian-deck-card"].quiet>.parts{display:flex;flex-direction:column;align-items:center;gap:0;height:auto;padding:0}
.slide .body>.group.three:has(>.stack>[data-el="meridian-deck-image-frame"])>.stack>[data-el="meridian-deck-card"].quiet .name{font-size:var(--type-24);font-weight:var(--meridian-deck-font-weight-650);line-height:1.55;color:var(--a1-7);width:296px;min-height:0;height:35px;flex:none;border-bottom:1px solid var(--a1-4-muted);margin:0;padding:0;display:block}
.slide .body>.group.three:has(>.stack>[data-el="meridian-deck-image-frame"])>.stack>[data-el="meridian-deck-card"].quiet .note{font-size:var(--type-16);font-weight:var(--body-weight);line-height:1.6;color:var(--n-7);width:310px;min-height:0;height:auto;flex:none;display:block;margin:16px 0 0;padding:0}
'''
ELEMENT_PATCHES['flowchart']=r'''
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>[data-el="meridian-deck-flowchart"]:has(>.node:nth-child(4):last-child){flex:none;display:grid;grid-template-columns:277px 275px 275px 288px;grid-template-rows:44px;gap:0;padding:0;margin:17px 0 0;width:1115px;height:44px;min-height:44px;background:none;border:0}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>[data-el="meridian-deck-flowchart"]:has(>.node:nth-child(4):last-child)>.node{display:flex;align-items:center;justify-content:center;position:relative;padding:0;margin:0;min-height:0;min-width:0;width:calc(100% + 15px);height:44px;border:0;border-radius:0;box-shadow:none;clip-path:polygon(0 0,calc(100% - 15px) 0,100% 50%,calc(100% - 15px) 100%,0 100%,15px 50%);font-size:var(--type-16);font-weight:var(--body-weight);line-height:1.55;background:var(--n-7);color:var(--page)}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>[data-el="meridian-deck-flowchart"]:has(>.node:nth-child(4):last-child)>.node:first-child{background:color-mix(in srgb,var(--n-1) 98%,var(--ink));color:var(--n-7);clip-path:polygon(0 0,calc(100% - 15px) 0,100% 50%,calc(100% - 15px) 100%,0 100%)}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>[data-el="meridian-deck-flowchart"]:has(>.node:nth-child(4):last-child)>.node:nth-child(3){background:var(--n-8)}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>[data-el="meridian-deck-flowchart"]:has(>.node:nth-child(4):last-child)>.node:nth-child(4){background:var(--a1);color:var(--a1-on);width:100%}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>[data-el="meridian-deck-flowchart"]:has(>.node:nth-child(4):last-child)>.node::before,.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>[data-el="meridian-deck-flowchart"]:has(>.node:nth-child(4):last-child)>.node::after{content:none}
'''
ELEMENT_PATCHES['delta']=r'''
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-delta"]{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;gap:40px;flex:none;width:147px;height:140px;margin:0;padding:0}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-delta"]>.from,.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-delta"]>.to{display:flex;align-items:center;justify-content:center;width:147px;height:50px;flex:none;border-radius:999px;background:var(--n-7);color:var(--page);font-size:var(--type-18);font-weight:var(--body-weight);line-height:1.2;padding:0;border:0}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-delta"]>.to{background:var(--a1);color:var(--a1-on)}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-delta"]::before{content:"";position:absolute;left:33px;top:55px;width:80px;height:30px;background:linear-gradient(to bottom,var(--page),var(--a1-3-soft));clip-path:polygon(0 0,100% 0,50% 100%);border:0;transform:none}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-delta"]::after{content:none}
'''
ELEMENT_PATCHES['delta'] += r'''
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-delta"]>.to::before{content:none}
'''
ELEMENT_PATCHES['hierarchy']=r'''
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-hierarchy"]{position:relative;display:grid;grid-template-columns:repeat(3,50px);grid-template-rows:50px 43px;column-gap:20px;row-gap:47px;align-content:start;justify-content:center;flex:none;width:240px;height:140px;margin:0;padding:0;background:none;border:0}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-hierarchy"]>.root{grid-column:1 / span 3;grid-row:1;display:flex;align-items:center;justify-content:center;justify-self:center;width:147px;height:50px;padding:0;border:0;border-radius:999px;background:var(--n-8);color:var(--page);font-size:var(--type-18);font-weight:var(--body-weight);line-height:1.2;margin:0}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-hierarchy"]>.branch{position:relative;grid-row:2;display:block;width:50px;height:43px;margin:0;padding:0;border:0}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-hierarchy"]>.branch>.node{display:flex;align-items:center;justify-content:center;width:50px;height:43px;padding:0;border:0;border-radius:var(--radius-sm);background:var(--a1);color:var(--a1-on);font-size:var(--type-22);font-weight:var(--body-weight);line-height:1.55}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-hierarchy"]::before{content:"";position:absolute;left:50%;top:60px;height:20px;border-left:1px solid var(--n-4);transform:none}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-hierarchy"]::after{content:"";position:absolute;left:50px;right:50px;top:70px;height:10px;border:1px solid var(--n-4);border-bottom:0;transform:none}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-hierarchy"]>.branch::before,.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-hierarchy"]>.branch::after,.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>.group:nth-child(3)>.stack>[data-el="meridian-deck-hierarchy"]>.root::after{content:none}
'''
ELEMENT_PATCHES['callout']=r'''
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>[data-el="meridian-deck-callout"]:last-child{display:flex;align-items:center;justify-content:center;flex:none;width:1115px;height:72px;min-height:72px;margin:6px 0 0;padding:0;background:var(--a1);color:var(--a1-on);border:0;border-radius:0;text-align:center}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>[data-el="meridian-deck-callout"]:last-child p{font-size:var(--type-20);font-weight:var(--body-weight);line-height:1.55;color:inherit;margin:0}
.slide .body>.stack:has(>.group:first-child+:nth-child(2)+.group:nth-child(3)+:last-child)>[data-el="meridian-deck-callout"]:last-child b{font-weight:var(--name-weight);color:inherit}
'''
ELEMENT_PATCHES['person']=r'''
.slide .body>[data-el="meridian-deck-person"].people:has(>.person:nth-child(4):last-child){display:grid;grid-template-columns:repeat(4,minmax(0,1fr));grid-template-rows:minmax(0,1fr);gap:37px;align-content:start;align-items:start;width:calc(100% - 5px);height:min(390px,100%);container-name:meridian-tail-people;container-type:size;padding:0;margin:-7px 0 0 4px}
.slide .body>[data-el="meridian-deck-person"].people:has(>.person:nth-child(4):last-child)>[data-el="meridian-deck-person"].person{display:block;position:relative;width:100%;height:100%;min-width:0;padding:0;margin:0;background:none;border:0}
.slide .body>[data-el="meridian-deck-person"].people:has(>.person:nth-child(4):last-child)>[data-el="meridian-deck-person"].person>.seat.portrait{position:relative;left:auto;top:auto;width:100%;height:auto;max-height:none;max-width:none;aspect-ratio:262 / 218;padding:0;background:var(--n-2);border:0;border-radius:0}
.slide .body>[data-el="meridian-deck-person"].people:has(>.person:nth-child(4):last-child)>[data-el="meridian-deck-person"].person>.seat.portrait::before{content:attr(data-ph)}
.slide .body>[data-el="meridian-deck-person"].people:has(>.person:nth-child(4):last-child)>[data-el="meridian-deck-person"].person>.name{position:relative;inset:auto;width:auto;padding:0;margin:29px 0 0;font-size:var(--type-20);line-height:1.4;font-weight:var(--name-weight);color:var(--a1-7)}
.slide .body>[data-el="meridian-deck-person"].people:has(>.person:nth-child(4):last-child)>[data-el="meridian-deck-person"].person>.note{position:relative;inset:auto;width:auto;height:auto;padding:0;margin:0;font-size:var(--type-20);line-height:1.4;font-weight:var(--body-weight);color:var(--n-7);white-space:normal;border:0}
.slide .body>[data-el="meridian-deck-person"].people:has(>.person:nth-child(4):last-child)>[data-el="meridian-deck-person"].person>.note>span{display:block;border-top:1px solid var(--n-3);margin-top:15px;padding-top:15px;font-size:var(--type-18);font-weight:var(--body-weight);line-height:1.4}
'''

ELEMENT_PATCHES['person'] += r'''
@container meridian-tail-people (max-width:1000px){
[data-el="meridian-deck-person"].people:has(>.person:nth-child(4):last-child)>[data-el="meridian-deck-person"].person>.name{font-size:var(--type-18);margin-top:20px}
[data-el="meridian-deck-person"].people:has(>.person:nth-child(4):last-child)>[data-el="meridian-deck-person"].person>.note{font-size:var(--type-18)}
[data-el="meridian-deck-person"].people:has(>.person:nth-child(4):last-child)>[data-el="meridian-deck-person"].person>.note>span{font-size:var(--type-16);margin-top:10px;padding-top:10px}
}
'''

# Composition fixtures are supplied to the collection owner for contract-preserving merge.
for n,body in BODIES.items():
 FIXTURES[f'foundation/fixtures/source-tail-{n}.html']='<!-- min: 12x6 -->\n<section class="slide"><div class="page"><header class="head"><p class="kicker">2090 BUSINESS PROJECT</p><h1 class="title">PROJECT NAME</h1></header><div class="body">'+body+'</div></div></section>\n'

LEADS={25:'사분면을 나타내는 레이아웃',26:'그래프를 나타내는 레이아웃',27:'3개의 사진과 텍스트',28:'단계별 프로세스 레이아웃',29:'4개 이미지 레이아웃'}
def write_html():
 for n,body in BODIES.items():
  p=PROJECT/'reassembled'/f'slide_{n}.html';old=p.read_text();head=old.split('<body',1)[0]
  page='<section class="slide"><div class="page"><header class="head"><p class="kicker"><b>2090</b> BUSINESS PROJECT</p><h1 class="title">PROJECT NAME</h1><p class="lead">'+LEADS[n]+'</p></header><div class="body">'+body+'</div><footer class="foot">PRESENTATION · '+('07' if n<28 else '08')+'</footer></div></section>'
  scripts='<script src="../assets/lucide.min.js"></script><script src="../assets/render-icons.js"></script>'
  p.write_text(head+'<body style="margin:0">'+page+scripts+'</body></html>')
if __name__=='__main__':write_html()
