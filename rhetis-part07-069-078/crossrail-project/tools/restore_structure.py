from pathlib import Path
import re,html,json
P=Path(__file__).parent;C=P/'crossrail'
def get(n,x,y):
 h=(P/f'replica/slide_{n:02}.html').read_text()
 for st,t in re.findall(r'<div style="([^"]*)">(.*?)</div>',h):
  if f'left:{x}px;' in st and f'top:{y}px;' in st:return re.sub(r'<[^>]+>','',t)
 raise ValueError((n,x,y))
def el(t,cls,body,extra=''):
 return f'<div class="{cls}" data-el="crossrail-{t}"{extra}>{body}</div>'
def slot(h,col=1,span=12,row=1,rows=6):
 a=h.index('>');return h[:a]+f' style="grid-column:{col} / span {span};grid-row:{row} / span {rows}"'+h[a:]
def body(n,h):
 f=P/f'reassembled/slide_{n:02}.html';s=f.read_text();s=re.sub(r'(?s)(<div class="body">).*(</div></div></section>)',lambda m:m[1]+h+m[2],s);f.write_text(s)
def card(name,note,kick='',cl='quiet',fig=''):
 return el('card','card '+cl,'<div class="parts">'+(f'<p class="kick">{kick}</p>' if kick else '')+(f'<p class="fig">{fig}</p>' if fig else '')+f'<p class="name">{name}</p><p class="note">{note}</p></div>')
def prose(t):return el('prose','prose','<p>'+t+'</p>')
def pill(t):return el('pill','pill','<div class="parts"><p class="name">'+t+'</p></div>')
def listing(names):return el('list','list',''.join('<div class="item"><p class="name">'+n+'</p></div>' for n in names))
# Preserve every readable paragraph in the original three vision strips.
cs=[]
for i,x in enumerate([315,606,897],1):cs.append(card(get(5,x,329).replace(' 함께 ',' 함께<br>').replace(' 품질을 ',' 품질을<br>').replace('정직함으로 ','정직함으로<br>'),get(5,x,423),'VISION '+str(i)))
body(5,slot('<div class="group">'+''.join(cs)+'</div>',3,10))
f=P/'reassembled/slide_05.html';s=f.read_text().replace('<h1 class="title">회사 비전</h1>','<h1 class="title">회사<br>비전</h1>');f.write_text(s)
# Four business cells retain all four complete original descriptions.
cs=[]
for i,(x,y) in enumerate([(95,303),(680,303),(95,501),(680,501)],1):cs.append(card(get(11,x,y),get(11,x,y+53),'주요 사업 '+str(i),'line'))
body(11,slot('<div class="group two">'+''.join(cs)+'</div>'))
# Partnership panels: heading, one-line pill, independent prose, and three list items.
sides=[]
for i,x in enumerate([95,668]):
 sx=126+i*573;desc=get(19,sx,450);names=[get(19,sx,y).replace('•　','') for y in [537,573,609]]
 sides.append('<div class="side'+(' on' if i else '')+'"><p class="name">'+get(19,x,277)+'</p>'+pill(get(19,127+i*573,365))+prose(desc)+listing(names)+'</div>')
body(19,slot(el('versus','versus',sides[0]+'<div class="vs"><span class="icon" data-icon="move-right"></span></div>'+sides[1])))
# Complete source achievement paragraphs and retain figure/name/note alignment.
lead=el('metric','stat','<div class="parts"><b class="fig">1위</b><p class="name">업계 순위</p><p class="note">'+get(21,95,494)+'</p></div>')
cs=[]
for i,(x,y,nx,ny) in enumerate([(398,297,557,306),(813,297,972,306),(398,503,557,512),(813,503,972,512)]):cs.append(slot(card(get(21,nx,ny),get(21,x,y+75),cl='quiet',fig=get(21,x,y)),4+(i%2)*4,4 if i%2==0 else 5,1+(i//2)*3,3))
body(21,slot(lead,1,3)+''.join(cs))
# Cards gain source-family semantic layouts; no page selectors or invented classes.
s='[data-el="crossrail-card"].quiet:has(.parts>.kick):not(:has(.mark,.fig))'
f=C/'elements/card/element.css';f.write_text(f.read_text()+f'''\n/* Tall vision strips keep full prose under their numbered heading. */
{s}{{margin-top:calc(var(--gap-lg)*-4 - var(--gap-sm)*5/12);margin-bottom:calc(var(--gap) + var(--gap-sm)*5/6);border:0;background:var(--page)}}
{s} .parts{{padding:calc(var(--gap-lg)*4 - var(--gap-sm)/6) var(--gap) var(--gap);justify-content:flex-start;gap:0}}
{s} .kick{{box-sizing:border-box;flex:none;height:calc(var(--gap-lg) + var(--gap-sm)*13/12);font-size:var(--type-26);font-weight:var(--title-weight);color:var(--n-3);margin-inline:calc(var(--gap)*-1);padding-inline:var(--gap);border-bottom:1px solid var(--n-3)}}
{s} .name{{margin-top:calc(var(--gap) - var(--gap-sm)*5/12);font-size:var(--type-26);line-height:var(--name-line);border:0;padding:0;min-height:calc(var(--type-26)*var(--name-line)*2)}}
{s} .note{{margin-top:var(--gap);font-size:var(--type-18);line-height:var(--body-line);min-height:0}}
@container(max-height:300px){{{s}{{margin:0}}{s} .parts{{padding:var(--gap-sm)}}{s} .kick{{height:auto;font-size:var(--type-18);margin:0;padding:0}}{s} .name{{margin-top:var(--gap-sm);font-size:var(--type-22);min-height:0}}{s} .note{{margin-top:var(--gap-sm);font-size:var(--type-14)}}}}
''')
s='[data-el="crossrail-card"].line:has(.parts>.kick):not(:has(.mark,.fig))'
f.write_text(f.read_text()+f'''\n/* Business cells have a corner tab and a full paragraph. */
{s}{{position:relative;border:0;background:transparent}}
{s} .parts{{padding:var(--gap-lg) 0 0;gap:var(--gap-sm);justify-content:flex-start}}
{s} .kick{{position:absolute;right:0;top:0;box-sizing:border-box;height:calc(var(--gap) + var(--gap-sm)*7/12);min-width:148px;padding-inline:var(--gap-sm);display:flex;align-items:center;justify-content:center;background:var(--a1-7);color:var(--page);font-size:var(--type-18);font-weight:var(--title-weight)}}
{s} .name{{font-size:var(--type-26);padding:0;min-height:0;border:0}}
{s} .note{{font-size:var(--type-18);min-height:0;line-height:var(--body-line)}}
{s}::before{{content:"";position:absolute;left:calc(var(--margin-x)*-1);right:0;top:0;border-top:1px solid var(--n-3)}}
@container(max-height:160px){{{s} .parts{{padding-top:var(--gap)}}{s} .kick{{font-size:var(--type-14);height:var(--gap)}}{s} .name{{font-size:var(--type-22)}}{s} .note{{font-size:var(--type-14)}}}}
''')
f=C/'foundation/foundation.css';f.write_text(f.read_text()+'''\n/* A wrapped sidebar title accompanies the three full-height vision strips. */
.slide:not(.cover):has(.head>.title>br){background:linear-gradient(90deg,var(--page) 39.21875%,var(--a1-7) 0)}.slide:not(.cover):has(.head>.title>br)::before{display:none}.slide:not(.cover):has(.head>.title>br)::after{background:var(--n-3)}.slide:not(.cover):has(.head>.title>br) .head>.title{width:200px;margin-top:var(--gap-sm)}.slide:not(.cover):has(.head>.title>br) .no{color:var(--page)}.slide:not(.cover):has(.head>.title>br) .body>.group{width:calc(100% - var(--gap)*2);margin-left:var(--gap-sm);gap:calc(var(--gap-sm)*4/3)}
''')
s='[data-el="crossrail-versus"]:has(.side>.pill)'
f=C/'elements/versus/element.css';f.write_text(f.read_text()+f'''\n{s}{{grid-template-columns:minmax(0,1fr) 10px minmax(0,1fr);gap:var(--gap);transform:translateY(calc(var(--gap-sm)/-4))}}
{s} .side{{position:relative;display:flex;flex-direction:column;justify-content:flex-start;gap:0;padding:0;border:0;background:transparent}}
{s} .side::before{{content:"";position:absolute;inset:calc(var(--gap-lg)*2) 0 0;background:var(--n-1);z-index:-1}}
{s} .side>.name{{height:65px;min-height:65px;display:flex;align-items:center;justify-content:center;background:var(--a1-6);color:var(--page);font-size:var(--type-26);padding:0;border:0}}
{s} .side.on>.name{{background:var(--a1-7)}}
{s} .side>.pill{{margin:var(--gap-lg) var(--pad) 0;height:65px;min-height:65px}}
{s} .side>.prose{{margin:calc(var(--gap-sm)*4/3) var(--pad) 0;min-height:72px}}
{s} .side>.list{{margin:var(--gap) var(--pad) 0;flex:none;min-height:96px;justify-content:flex-start;gap:var(--gap-sm)}}
{s} .side>.list .name{{font-size:var(--type-18);font-weight:var(--body-weight)}}
{s} .vs{{align-items:flex-start;position:relative;padding-top:calc(var(--gap-sm)*5/3);overflow:visible}}
{s} .vs .icon{{width:52px;height:40px;max-width:none;color:var(--a1-6);stroke-width:6}}
''')
print('readable text and main layouts 05/11/19/21 restored')
