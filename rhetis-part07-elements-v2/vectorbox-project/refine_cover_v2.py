"""Author the named foundation.cover base from immutable13 measurements."""
from pathlib import Path
import json,re
P=Path(__file__).parent
p=P/'write_elements_v2.py';s=p.read_text()
start=s.index('.slide.cover .page{');end=s.index('.slide .meta{',start)
new='''.slide.cover .page{display:flex;align-items:center;justify-content:center;padding:calc(var(--margin-y) + var(--gap-sm) + var(--stroke)) var(--margin-x) 0}.slide.cover .lockup{position:relative;width:76%;text-align:center}.slide.cover .lockup:before{content:'';position:absolute;left:calc(-1*var(--gap-sm) - 2*var(--stroke));top:calc(-1*var(--gap-sm) + 2*var(--stroke));width:var(--rail-w);height:var(--top-h);background:var(--a1)}.slide.cover .lockup>.kicker{padding-left:calc(var(--gap) - 2*var(--stroke));font:var(--label-weight) var(--type-20)/var(--label-line) var(--vectorbox-font-latin);letter-spacing:var(--label-track-latin)}.slide.cover .lockup>.title{margin-top:calc(2*var(--gap-lg) + var(--gap-sm) + 4*var(--stroke));font:var(--vectorbox-weight-black) var(--type-104)/var(--title-line) var(--font-display);letter-spacing:var(--vectorbox-cover-track)}.slide.cover .lockup>.title>b{display:block;font-size:var(--type-76);font-weight:var(--title-weight);color:var(--a1-7)}.slide.cover .lockup>.lead{margin-top:calc(var(--gap) - 3*var(--stroke));font:var(--lead-weight) var(--type-24)/var(--label-line) var(--font-body);letter-spacing:var(--label-track)}.slide.cover .at-left,.slide.cover .at-top-left,.slide.cover .at-bottom-left{text-align:left;margin-right:auto}.slide.cover .at-top-left{align-self:flex-start}.slide.cover .at-bottom-left{align-self:flex-end;margin-bottom:calc(4*var(--gap-lg) + var(--gap-sm))}.slide.cover .meta{position:absolute;left:var(--margin-x);bottom:calc(var(--gap-lg) + var(--gap));font:var(--body-weight) clamp(var(--type-20),1.640625cqw,var(--type-22))/var(--vectorbox-loose-line) var(--font-body);letter-spacing:var(--label-track);color:var(--n-7)}'''
s=s[:start]+new+s[end:]
# .deco is expressly the named cover graphic; normal-page decorative backgrounds
# have no such named slot in foundation.page@1 and are recorded as gaps.
a=s.index('.slide .deco{');b=s.index('.slide.cover .page{',a)
s=s[:a]+s[b:]
# Remove the compact-body misuse;13 is represented by the named cover structure.
s=s.replace('.slide .page.overrides{grid-template-rows:calc(2*var(--gap-lg) + var(--gap-sm) + 6*var(--stroke)) minmax(0,1fr)}','')
def cw(v):return f'{v/12.8:.6f}cqw'
def ch(v):return f'{v/7.2:.6f}cqh'
def fill(x,y,w,h,c):return f'linear-gradient({c},{c}) {cw(x)} {ch(y)}/{cw(w)} {ch(h)} no-repeat'
def frame(x,y,w,h):
 col='var(--a1)';out=[]
 for xx,yy,ww,hh in [(x-3,y-3,14,6),(x-3,y-3,6,14),(x+w-11,y-3,14,6),(x+w-3,y-3,6,14),(x-3,y+h-3,14,6),(x-3,y+h-11,6,14),(x+w-11,y+h-3,14,6),(x+w-3,y+h-11,6,14)]:out.append(fill(xx,yy,ww,hh,col))
 for xx,yy,ww,hh in [(x,y,w,1),(x,y+h-1,w,1),(x,y,1,h),(x+w-1,y,1,h)]:out.append(fill(xx,yy,ww,hh,'var(--a1-4-soft)'))
 return out
layers=frame(974,18,264,508)+frame(800,410,341,261)+frame(-65,544,400,260)+[fill(975,87,198,253,'var(--n-1)'),fill(801,550,154,120,'var(--n-1)')]
graphic='.slide.cover .deco{position:absolute;inset:0;z-index:-1;pointer-events:none;background:'+','.join(layers)+'}'
s=s.replace("(f/'foundation.css').write_text", "foundation += "+repr(graphic)+"\n(f/'foundation.css').write_text")
# The source-shaped foundation example uses fresh business text and one bare.deco.
fixture='<!-- min: 12x6 -->\n<section class="slide cover"><div class="page"><div class="lockup at-top-left"><p class="kicker">BRANCH OPERATIONS</p><h1 class="title"><b>기록을 연동해</b>납기를 지킵니다</h1><p class="lead">증빙의 중복 등록을 줄이고 담당 부서에 같은 거래 정보를 전달합니다.</p></div><p class="meta">지점 정산 지원실<br>partners@branch.co</p><div class="deco"></div></div></section>'

s=re.sub(r"\(f/'fixtures/cover.html'\)\.write_text\([^\n]+", lambda m:"(f/'fixtures/cover.html').write_text("+repr(fixture)+")",s)
p.write_text(s)
# Map the gratitude page by its actual cover function, not a body-grid look-alike.
p=P/'map.json';x=json.loads(p.read_text())
for v in x['instances']:
 if v['page']=='13' and v['use']!='background':
  v['leaf']=None;v['use']='furniture';v['variant']=None;v['fixture']='foundation/fixtures/cover.html';v['foundationContract']='foundation.page@1'
  if v['id'].endswith('statement'):v['foundationParts']=['.cover .lockup > .title','.cover .lockup > .lead']
  elif v['id'].endswith('footer'):v['foundationParts']=['.cover .meta']
  elif v['id'].endswith('head'):v['foundationParts']=['.cover .lockup > .kicker','.cover .lockup::before']
  else:v['foundationParts']=['.cover .deco']
for page,ids in [('02',['02-decor-20','02-decor-21']),('11',['11-decor-4','11-decor-5'])]:
 rows=[v for v in x['instances'] if v['id'] in ids];x['instances']=[v for v in x['instances'] if v['id'] not in ids]
 left=min(v['bbox'][0] for v in rows);top=min(v['bbox'][1] for v in rows);right=max(v['bbox'][0]+v['bbox'][2] for v in rows);bottom=max(v['bbox'][1]+v['bbox'][3] for v in rows)
 x['instances'].append({'id':page+'-normal-background','page':page,'leaf':None,'use':'unexpressible','contract':'foundation.page@1','bbox':[left,top,right-left,bottom-top],'fixture':None,'selectors':sum([v['selectors'] for v in rows],[]),'sourceObjectIds':sum([v['sourceObjectIds'] for v in rows],[]),'sourceMeasurements':sum([v['sourceMeasurements'] for v in rows],[]),'why':'The normal head/body grammar has no decorative background slot; .deco is expressly a cover graphic. Placing these off-grid selection frames with renamed furniture classes would invent an unnamed page variant.','neededMarkup':'A named normal-page background slot that may own its measured vector-frame composition, separately from body content.'})
p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
for leaf in ['headline','prose','image-frame']:
 q=P/'sheets'/f'{leaf}-replica.png'
 if q.exists():q.unlink()
(P/'assets/source-defaults.css').unlink(missing_ok=True)
(P/'GAPS.md').write_text('# 계약으로 표현하지 못한 원본 구조\n\n- 02 / normal background: 비표지 페이지에는 배경 장식 슬롯이 정의되어 있지 않다. 오른쪽으로 잘린 두 선택 프레임을 body 안에 끼워 넣거나 다른 역할 클래스로 위치 분기하지 않았다. 필요한 마크업은 일반 페이지의 명명된 배경 장식 슬롯이다.\n- 04 / grouped bar chart: 연도마다 두 계열을 묶은 막대, 별도의 숫자 축과 값 주석 제어를 flat bar 계약으로 표현할 수 없다. 필요한 마크업은 category group 아래의 series bars, 독립 axis ticks와 annotation 제어다.\n- 10 / multi-sector ring: one-share donut과 row of donuts는 여섯 독립 조각을 가진 하나의 원형 차트와 다르다. 필요한 마크업은 donut 아래의 이름과 수치를 가진 segment 목록이다.\n- 11 / normal background: 비표지의 위쪽 오른쪽 프레임과 왼쪽 아래 프레임 역시 cover 전용 deco 밖의 구조다. 필요한 마크업은 일반 페이지의 명명된 배경 장식 슬롯이다.\n')
print('Authored one named cover base; map reclassified13 and normal-background gaps02/11.')
