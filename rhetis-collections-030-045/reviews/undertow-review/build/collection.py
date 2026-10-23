from pathlib import Path
import json,re,shutil
C=Path('/workspace/work/deliverables/undertow');R=Path('/workspace/work/deliverables/undertow-review');REF=Path('/workspace/work/reference');C.mkdir(exist_ok=True)
def write(p,t):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(t,encoding='utf8')
tokens={'--page':'#f0f0f0','--ink':'#080b09','--font-display':"'Pretendard Variable'",'--font-body':"'Pretendard Variable'",'--weight-display':'500','--weight-body':'400','--tracking-display':'-.035em','--radius':'0px','--radius-sm':'0px','--stroke':'1px','--text-min':'12px','--margin-x':'60px','--margin-y':'36px','--gap':'24px','--gap-sm':'12px','--gap-lg':'36px','--pad':'24px','--furn-edge':'36px','--top-h':'24px','--foot-h':'24px','--furn-gap':'12px','--rail-w':'86px','--rail-gap':'24px','--title-weight':'500','--title-line':'1.2','--title-track':'-.035em','--lead-weight':'400','--lead-line':'1.4','--lead-track':'-.01em','--figure-weight':'750','--figure-line':'1.1','--figure-track':'-.025em','--name-weight':'700','--name-line':'1.25','--name-track':'-.02em','--body-weight':'400','--body-line':'1.45','--body-track':'-.01em','--label-weight':'650','--label-line':'1.2','--label-track':'0em','--label-track-latin':'0em'}
write(C/'kit/kit.json',json.dumps({'schema':'rhetis.kit/2','id':'undertow','label':'Undertow','tokens':'css/tokens.css','description':'description.md','extensions':{}},ensure_ascii=False,indent=2))
write(C/'kit/css/tokens.css','.slide {\n'+'\n'.join(f'  {k}: {v};' for k,v in tokens.items())+'\n}\n.slide.dark { --page:#101715; --ink:#f4f7f5; }\n')
write(C/'kit/description.md','Undertow balances quiet square panels, slender dividing rules and pill-shaped role labels against large circular centres and a severe vertical edge. Clear regular-weight headings leave bold figures and one filled accent centre to carry the argument. It takes its visual grammar from a minimal investor deck rather than a decorative card system.')
foundation='''.slide { width:1280px; height:720px; position:relative; overflow:hidden; background:var(--page); color:var(--ink); font-family:var(--font-body); font-weight:var(--body-weight); line-height:var(--body-line); letter-spacing:var(--body-track); }
.slide,.slide * { box-sizing:border-box; }
.slide p,.slide h1,.slide h2,.slide h3,.slide blockquote { margin:0; }
.slide .page { position:absolute; inset:0; display:flex; flex-direction:column; gap:var(--gap); padding:calc(var(--margin-y) + var(--top-h) + var(--furn-gap)) calc(var(--margin-x) + var(--rail-w)) var(--margin-y) var(--margin-x); }
.slide .page::after { content:""; position:absolute; top:0; right:0; bottom:0; width:var(--rail-w); background:var(--ink); }
.slide .head { text-align:left; flex:0 0 auto; }
.slide .head.center { text-align:center; }
.slide .head .kicker { display:table; margin:0 0 var(--gap-sm); background:var(--ink); color:var(--page); border-radius:999px; padding:calc(var(--gap-sm)/3) var(--gap); font-size:var(--type-12); font-weight:var(--label-weight); line-height:var(--label-line); }
.slide .head.center .kicker { margin-inline:auto; }
.slide .title { font-family:var(--font-display); font-size:var(--type-40); font-weight:var(--title-weight); line-height:var(--title-line); letter-spacing:var(--title-track); }
.slide .lead { font-size:var(--type-16); font-weight:var(--lead-weight); line-height:var(--lead-line); letter-spacing:var(--lead-track); margin-top:var(--gap-sm); }
.slide .body { min-height:0; flex:1; display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); grid-template-rows:repeat(6,minmax(0,1fr)); gap:var(--gap-sm); container-type:size; }
.slide .body > * { min-height:0; min-width:0; }
.slide .group { display:flex; gap:var(--gap); min-height:0; min-width:0; }
.slide .group > * { flex:1 1 0; min-height:0; min-width:0; }
.slide .group.col,.slide .stack { display:flex; flex-direction:column; gap:var(--gap-sm); min-height:0; min-width:0; }
.slide .stack > * { min-height:0; min-width:0; flex:1 1 0; }
.slide .group.two { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); }
.slide .group.three { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); }
.slide .split { display:grid; grid-template-columns:minmax(0,2fr) minmax(0,3fr); gap:var(--gap); min-height:0; }
.slide .split.wide-left { grid-template-columns:minmax(0,3fr) minmax(0,2fr); }
.slide .icon { width:32px; height:32px; display:inline-flex; flex:none; }
.slide .seat { display:flex; align-items:center; justify-content:center; background:var(--n-2); color:var(--n-8); aspect-ratio:1; min-width:0; min-height:0; font-size:var(--type-20); }
.slide .seat::after { content:attr(data-ph); }
.slide .seat.avatar { border-radius:50%; width:64px; height:64px; }
.slide .seat.portrait { aspect-ratio:1; }
.slide .seat.logo { aspect-ratio:1; }
.slide .top { position:absolute; top:var(--margin-y); left:var(--margin-x); right:calc(var(--margin-x) + var(--rail-w)); display:flex; align-items:center; justify-content:space-between; gap:var(--gap); font-size:var(--type-12); font-weight:var(--label-weight); }
.slide .rail { position:absolute; right:calc(var(--rail-w)/2 - var(--gap-sm)/2); top:calc(var(--margin-y)*2); bottom:var(--margin-y); z-index:1; color:var(--page); writing-mode:vertical-rl; font-size:var(--type-12); display:flex; justify-content:space-between; }
.slide .foot { display:flex; align-items:center; gap:var(--gap-lg); font-size:var(--type-12); }
.slide.cover .page { padding:var(--margin-y) var(--margin-x); display:block; }
.slide.cover .page::after { display:none; }
.slide.cover .lockup { position:absolute; z-index:1; max-width:80%; }
.slide.cover .lockup.at-left { left:var(--margin-x); top:25%; }
.slide.cover .lockup.at-top-left { left:var(--margin-x); top:calc(var(--margin-y)*2); }
.slide.cover .lockup.at-center { top:50%; left:50%; transform:translate(-50%,-50%); text-align:center; }
.slide.cover .lockup.at-bottom-left { left:var(--margin-x); bottom:calc(var(--margin-y)*3); }
.slide.cover .kicker { font-size:var(--type-28); margin-bottom:var(--gap-sm); }
.slide.cover .title { font-size:var(--type-108); font-weight:var(--weight-display); line-height:var(--title-line); }
.slide.cover .title b { color:var(--a1); font-weight:var(--figure-weight); }
.slide.cover .meta { position:absolute; bottom:0; left:0; right:0; background:var(--ink); color:var(--page); padding:var(--gap-lg) var(--margin-x); font-size:var(--type-14); }
.slide.cover .deco { position:absolute; right:-10%; top:-35%; width:100%; height:70%; border:var(--stroke) solid var(--a1-3-soft); border-radius:50%; background:var(--n-1); }
.slide.cover .seat.back { position:absolute; inset:0; width:100%; height:100%; aspect-ratio:auto; }
'''
write(C/'foundation/foundation.css',foundation);write(C/'foundation/foundation.json',json.dumps({'schema':'rhetis.design-library-foundation-source/1','kit':'undertow','registrations':{},'tokenDefaults':{}},indent=2));write(C/'foundation/description.md','A regular-weight centre title sits above a twelve-by-six grid, with a severe full-height side rail, small reversed capsule kicker and a discreet upper furniture row. Covers use a left aligned oversized lockup and a low full-width information strip. Square numbered seats reserve photography without pretending to be imagery.')
write(C/'foundation/fixtures/seat.html','<!-- min: 12x6 -->\n<section class="slide"><div class="page"><header class="head center"><p class="kicker">INVESTOR RELATIONS</p><h1 class="title">핵심 기술이 만드는 다음 성장</h1><p class="lead">명확한 문제 정의와 검증된 지표로 미래를 설명합니다.</p></header><div class="body"><div class="seat" data-ph="1" style="grid-column:4 / span 5;grid-row:1 / span 6"></div></div></div></section>')
write(C/'foundation/fixtures/cover.html','<!-- min: 12x6 -->\n<section class="slide cover"><div class="page"><div class="deco"></div><div class="lockup at-top-left"><p class="kicker">투자유치를 위한 설득력 있는</p><h1 class="title">MINIMAL<br><b>IR DECK</b></h1><p class="lead">기술과 사람을 연결하는 다음 성장의 시작</p></div><p class="meta">MIRI COMPANY · Investor Relations Deck</p></div></section>')
tax=json.loads((REF/'contract/taxonomy.json').read_text()); special={'card':'confetti','callout':'annual','chart-area':'annual','chart-bar':'confetti','chart-donut':'amethyst','chart-line':'amethyst'}
# Use contract fixture structure and data, never sample CSS.
for co in tax['contracts']:
 name=co['category'].split('.')[-1];name={'bar':'chart-bar','line':'chart-line','donut':'chart-donut','stack':'chart-stack','waterfall':'chart-waterfall','area':'chart-area','scatter':'chart-scatter','spark':'sparkline','logos':'logo-group','frame':'image-frame'}.get(name,name)
 # folder names directly by contract id mappings
 found=[p for p in (REF/'samples/annual/elements').iterdir() if json.loads((p/'element.json').read_text())['contract']==co['id']];name=found[0].name
 d=C/'elements'/name;write(d/'element.json',json.dumps({'schema':'rhetis.design-library-element-source/1','contract':co['id'],'registrations':{},'tokenDefaults':{}},indent=2));write(d/'description.md',f'The {name} uses Undertow’s square planes, hairline partitions, circular focal forms and short reversed capsules. It gives one accent priority and keeps supporting content quiet, with discrete typography steps for smaller grid allocations.')
 source=REF/'samples'/special.get(name,'annual')/'elements'/name/'fixtures';fs=sorted(source.glob('*.html'))
 for f in fs:
  s=f.read_text();s=re.sub(r'(annual|amethyst|confetti)-','undertow-',s)
  if name not in special:
   s=s.replace('미래홀딩스','미리컴퍼니').replace('2056','2026').replace('2055','2025').replace('2057','2027').replace('TEXT 기획','시장 기획')
   s=re.sub(r'<ul class="list">(.*?)</ul>',lambda m:'<div class="list check" data-el="undertow-list">'+re.sub(r'<li>(.*?)</li>',r'<div class="item"><b class="name">\1</b></div>',m.group(1))+'</div>',s,flags=re.S)
   s=s.replace('class="tag">','class="tag" data-el="undertow-tag">')
   # Correct top-level fixture span to contract standard.
   s=re.sub(r'grid-column:\s*\d+\s*/\s*span\s*\d+','grid-column:1 / span 12',s,count=1);s=re.sub(r'grid-row:\s*\d+\s*/\s*span\s*\d+','grid-row:1 / span 6',s,count=1)
  write(d/'fixtures'/f.name,s)
 if len(fs)<2:
  s=(d/'fixtures'/fs[0].name).read_text().replace('미리컴퍼니','미리컴퍼니 글로벌 사업본부').replace('베이직','성장 지원 플랜').replace('2026','2028').replace('162억 원','180억 원').replace('현장 방문 점검','전 사업장 현장 방문과 매월 개선 과제 점검')
  write(d/'fixtures'/'extended.html',s)
print('collection structure',len(list((C/'elements').iterdir())))
# Each CSS is authored below. $ stands for scoped contract roots.
css={}
def put(n,s):css[n]=s
put('card','''$ { background:var(--page); border-top:calc(var(--stroke)*5) solid var(--n-3); padding:var(--pad); display:flex; align-items:center; justify-content:center; text-align:center; }
$ .parts { display:grid; width:100%; gap:var(--gap-sm); align-content:center; justify-items:center; }
$ .fig { font-size:var(--type-52); }
$ .name { padding-bottom:var(--gap-sm); border-bottom:var(--stroke) solid var(--n-4); width:100%; }
$.on { background:var(--a1); color:var(--a1-on); border-color:var(--a1); }
$.on .note,$.on .kick { color:var(--a1-on); }
$.line { border:var(--stroke) solid var(--n-4); background:var(--page); }
$.quiet { background:var(--n-1); border-color:var(--n-2); }
$ .mark { width:72px; height:72px; border-radius:50%; background:var(--a1-2-soft); color:var(--a1-8); display:flex; align-items:center; justify-content:center; font-size:var(--type-28); }
$ .mark .icon { width:40px; height:40px; }
$ .mark:has(.seat.icon) { width:96px; height:96px; background:none; } $ .seat.icon { width:88px; height:88px; } $ .icon:not([data-icon]) { display:flex; align-items:center; justify-content:center; font-size:var(--type-20); line-height:var(--label-line); }
$.tone-2 { border-color:var(--a2); } $.tone-3 { border-color:var(--a3); } $.tone-4 { border-color:var(--a4); } $.tone-5 { border-color:var(--n-6); }
@container (max-width:260px) { $ .fig { font-size:var(--type-32); } $ .name { font-size:var(--type-20); } $ .note { font-size:var(--type-14); } $ .mark { width:56px; height:56px; } $ .mark .icon { width:30px; height:30px; } }
''')
put('pill','''$ { padding:var(--gap-sm) var(--gap); border-radius:999px; background:var(--n-1); display:flex; align-items:center; justify-content:center; min-height:48px; }
$ .parts { display:flex; align-items:center; justify-content:center; gap:var(--gap-sm); }
$ .name { font-size:var(--type-18); white-space:nowrap; } $ .note { font-size:var(--type-14); }
$ .mark { font-size:var(--type-14); font-weight:var(--label-weight); } $.on { background:var(--a1); color:var(--a1-on); } $.on .note { color:var(--a1-on); } $.line { border:var(--stroke) solid var(--n-5); background:var(--page); } $.quiet { background:var(--n-2); }
@container (max-width:420px) { $ .note { font-size:var(--type-12); } $ .name { font-size:var(--type-16); } }
''')
put('callout','''$ { display:flex; align-items:center; justify-content:center; gap:var(--gap-sm); background:var(--a1); color:var(--a1-on); padding:var(--pad); text-align:center; }
$ p { font-size:var(--type-24); line-height:var(--lead-line); font-weight:var(--lead-weight); } $ b { font-weight:var(--name-weight); } $ .icon { width:32px; height:32px; }
@container (max-width:640px) { $ p { font-size:var(--type-18); } }
@container (max-height:130px) { $ p { font-size:var(--type-18); } }
''')
put('tag','''$.tag { display:inline-flex; align-items:center; justify-content:center; background:var(--ink); color:var(--page); padding:calc(var(--gap-sm)/3) var(--gap-sm); border-radius:999px; font-size:var(--type-12); line-height:var(--label-line); font-weight:var(--label-weight); white-space:nowrap; }
$.hl { background:var(--a1-2-soft); color:var(--ink); font-weight:var(--name-weight); padding-inline:calc(var(--gap-sm)/3); box-decoration-break:clone; }
@container (max-width:300px) { $.tag { font-size:var(--type-10); } }
''')
put('list','''$ { display:flex; flex-direction:column; justify-content:center; gap:var(--gap-sm); counter-reset:item; padding:var(--gap-sm) 0; }
$ .item { position:relative; counter-increment:item; padding-left:var(--gap); } $ .item::before { content:""; position:absolute; left:0; top:.5em; width:6px; height:6px; border-radius:50%; background:var(--a1); }
$ .name { font-size:var(--type-20); } $ .note { font-size:var(--type-16); margin-top:calc(var(--gap-sm)/2); }
$.num .item::before { content:counter(item); top:0; width:var(--gap); height:var(--gap); display:flex; align-items:center; justify-content:center; background:var(--ink); color:var(--page); font-size:var(--type-12); } $.num .item { padding-left:var(--gap-lg); }
$.check .item::before { border-left:2px solid var(--a1); border-bottom:2px solid var(--a1); border-radius:0; background:none; width:10px; height:6px; transform:rotate(-45deg); }
$.divided .item { padding-block:var(--gap-sm); border-bottom:var(--stroke) solid var(--n-3); }
@container (max-width:480px) { $ .name { font-size:var(--type-16); } $ .note { font-size:var(--type-14); } }
''')
put('quote','''$ { display:flex; flex-direction:column; justify-content:center; gap:var(--gap); padding:var(--pad); border-top:calc(var(--stroke)*4) solid var(--a1); background:var(--page); }
$ blockquote { font-family:var(--font-display); font-size:var(--type-32); font-weight:var(--lead-weight); line-height:var(--lead-line); letter-spacing:var(--lead-track); } $ blockquote b { color:var(--a1-8); }
$ .by { display:grid; grid-template-columns:64px 1fr; align-items:center; column-gap:var(--gap-sm); } $ .by .seat { grid-row:1 / span 2; } $ .by .name { font-size:var(--type-18); } $ .by .note { font-size:var(--type-14); }
$.big blockquote { font-size:var(--type-44); }
@container (max-width:480px) { $ blockquote,$.big blockquote { font-size:var(--type-24); } }
''')
put('headline','''$ { display:flex; flex-direction:column; justify-content:center; gap:var(--gap-sm); }
$ .kick { align-self:flex-start; background:var(--ink); color:var(--page); border-radius:999px; padding:calc(var(--gap-sm)/3) var(--gap); }
$ h2 { font-family:var(--font-display); font-size:var(--type-40); font-weight:var(--title-weight); line-height:var(--title-line); letter-spacing:var(--title-track); } $ h2 b { color:var(--a1-8); font-weight:var(--name-weight); }
$.big h2 { font-size:var(--type-64); } $.center { text-align:center; align-items:center; } $.center .kick { align-self:center; } $.on { background:var(--a1); color:var(--a1-on); padding:var(--pad); } $.on h2 b,$.on .note { color:var(--a1-on); }
@container (max-width:600px) { $ h2 { font-size:var(--type-28); } $.big h2 { font-size:var(--type-40); } }
''')
put('prose','''$ { display:flex; flex-direction:column; justify-content:center; gap:var(--gap); } $ p { font-size:var(--type-20); font-weight:var(--body-weight); line-height:var(--body-line); } $ b { font-weight:var(--name-weight); } $.lead p { font-size:var(--type-28); } $.quiet { color:var(--n-8); } $.cols { display:block; columns:2; column-gap:var(--gap-lg); } $.cols p { margin-bottom:var(--gap); }
@container (max-width:540px) { $ p,$.lead p { font-size:var(--type-16); } $.cols { columns:1; } }
''')
put('metric','''$.stats { display:flex; align-items:stretch; justify-content:space-evenly; gap:var(--gap); } $.stats > .stat { flex:1; border-right:var(--stroke) solid var(--n-3); } $.stats > .stat:last-child { border-right:0; } $.stat { display:flex; align-items:center; justify-content:center; text-align:center; } $ .parts { width:100%; display:grid; gap:var(--gap-sm); align-content:center; justify-items:center; } $ .fig { font-size:var(--type-56); } $ .name { font-size:var(--type-20); } $ .note { font-size:var(--type-14); } $ .fig small { font-size:var(--type-24); }
@container (max-width:320px) { $ .fig { font-size:var(--type-36); } $ .name { font-size:var(--type-16); } $ .note { font-size:var(--type-12); } }
''')
put('delta','''$ { display:flex; align-items:center; justify-content:center; gap:var(--gap-lg); font-size:var(--type-36); font-family:var(--font-display); font-weight:var(--figure-weight); } $ .from { color:var(--n-7); } $ .to { color:var(--a1-8); position:relative; padding-left:var(--gap-lg); } $ .to::before { content:""; position:absolute; left:calc(var(--gap-sm)/-2); top:50%; width:22px; border-top:2px solid var(--n-5); } $ .to::after { content:""; position:absolute; left:8px; top:calc(50% - 4px); width:8px; height:8px; border-top:2px solid var(--n-5); border-right:2px solid var(--n-5); transform:rotate(45deg); }
@container (max-width:500px) { $ { font-size:var(--type-28); gap:var(--gap-sm); } }
''')
put('chart-bar','''$ { display:flex; align-items:stretch; justify-content:space-around; gap:var(--gap-sm); padding:var(--gap-lg) var(--gap-sm) var(--gap-lg); border-bottom:var(--stroke) solid var(--n-4); }
$ .bar { position:relative; flex:1; min-width:0; display:flex; align-items:center; justify-content:center; }
$ .bar::before { content:""; position:absolute; bottom:0; left:12%; right:12%; height:calc(var(--v)/var(--max)*100%); background:var(--n-4); }
$ .bar.on::before { background:var(--a1); } $ .bar.tone-2::before { background:var(--a2); } $ .bar.tone-3::before { background:var(--a3); }
$ .bar b { position:absolute; bottom:calc(var(--v)/var(--max)*100% + var(--gap-sm)/2); font-size:var(--type-20); font-weight:var(--figure-weight); white-space:nowrap; }
$ .bar span { position:absolute; top:calc(100% + var(--gap-sm)); left:0; right:0; text-align:center; font-size:var(--type-14); line-height:var(--label-line); white-space:nowrap; }
$.h { flex-direction:column; padding:var(--gap-sm) var(--gap-lg) var(--gap-sm) calc(var(--gap-lg)*3); border-bottom:0; }
$.h .bar { display:block; } $.h .bar::before { top:15%; bottom:15%; left:0; right:auto; width:calc(var(--v)/var(--max)*90%); height:auto; }
$.h .bar span { right:calc(100% + var(--gap-sm)); top:50%; left:auto; transform:translateY(-50%); width:calc(var(--gap-lg)*2.5); text-align:right; white-space:normal; }
$.h .bar b { left:calc(var(--v)/var(--max)*90% + var(--gap-sm)); bottom:auto; top:50%; transform:translateY(-50%); }
@container (max-width:600px) { $ .bar b { font-size:var(--type-14); } $ .bar span { font-size:var(--type-12); } $:has(.bar:nth-child(9)) .bar:nth-child(even) span { visibility:hidden; } }
''')
put('chart-line','''$ { display:grid; grid-auto-flow:column; grid-auto-columns:minmax(0,1fr); grid-template-rows:minmax(0,1fr) var(--gap-lg); padding:var(--gap-lg) var(--gap-sm) 0; isolation:isolate; anchor-scope:all; border-bottom:var(--stroke) solid var(--n-3); }
$ .pt { display:contents; } $ .pt b { grid-row:1; height:calc(100% - var(--v)/var(--max)*(100% - var(--gap-lg))); display:flex; flex-direction:column; align-items:center; justify-content:flex-end; font-size:var(--type-18); anchor-name:var(--undertow-self); font-weight:var(--figure-weight); }
$ .pt b::after { content:""; width:8px; height:8px; border-radius:50%; background:var(--n-5); margin-top:calc(var(--gap-sm)/2); margin-bottom:0; }
$ .pt.on b::after { background:var(--a1); } $ .pt.on b { color:var(--a1-8); }
$ .pt span { grid-row:2; text-align:center; padding-top:var(--gap-sm); font-size:var(--type-14); }
$ .pt::before,$ .pt::after { content:""; position:absolute; left:anchor(var(--undertow-prev) center); right:anchor(var(--undertow-self) center); pointer-events:none; }
$ .pt::before { top:anchor(var(--undertow-prev) bottom); bottom:anchor(var(--undertow-self) bottom); background:linear-gradient(to top right,transparent calc(50% - 1px),var(--n-5) calc(50% - 1px),var(--n-5) calc(50% + 1px),transparent calc(50% + 1px)); }
$ .pt::after { top:anchor(var(--undertow-self) bottom); bottom:anchor(var(--undertow-prev) bottom); background:linear-gradient(to bottom right,transparent calc(50% - 1px),var(--n-5) calc(50% - 1px),var(--n-5) calc(50% + 1px),transparent calc(50% + 1px)); }
$ .pt:first-child::before,$ .pt:first-child::after { content:none; }
@container (max-width:600px) { $ .pt b { font-size:var(--type-14); } $ .pt span { font-size:var(--type-12); } $:has(.pt:nth-child(9)) .pt:nth-child(even) span { visibility:hidden; } }
'''+''.join(f'$ .pt:nth-child({i}) {{ --undertow-self:--undertow-line-{i}; --undertow-prev:--undertow-line-{i-1}; }}\n' for i in range(1,13)))
put('chart-donut','''$.donuts { display:flex; align-items:stretch; gap:var(--gap); } $.donuts > .donut { flex:1; min-width:0; }
$.donut { position:relative; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:var(--gap-sm); padding-bottom:var(--gap-lg); isolation:isolate; }
$.donut::before { content:""; position:absolute; width:min(80%,68cqh); aspect-ratio:1; border-radius:50%; background:conic-gradient(var(--a1) calc(var(--v)*1%),var(--n-3) 0); z-index:-2; }
$.donut::after { content:""; position:absolute; width:min(58%,49cqh); aspect-ratio:1; border-radius:50%; background:var(--page); z-index:-1; }
$ .fig { font-size:var(--type-48); } $ .fig small { font-size:var(--type-22); } $ .name { position:absolute; top:calc(50% + 36cqh); font-size:var(--type-18); text-align:center; }
@container (max-width:300px) { $ .fig { font-size:var(--type-28); } $ .name { font-size:var(--type-14); } }
''')
put('gauge','''$ { position:relative; min-height:64px; padding-bottom:var(--gap); display:flex; justify-content:space-between; align-items:center; gap:var(--gap-sm); }
$ .fig { font-size:var(--type-28); } $ .name { font-size:var(--type-20); }
$::before,$::after { content:""; position:absolute; bottom:0; left:0; height:12px; } $::before { width:100%; background:var(--n-2); } $::after { width:calc(var(--v)*1%); background:var(--a1); }
@container (max-width:450px) { $ .name { font-size:var(--type-16); } $ .fig { font-size:var(--type-22); } }
''')
put('table','''$ { display:flex; align-items:center; } $ .table { width:100%; border-collapse:collapse; table-layout:fixed; font-size:var(--type-18); } $ th { padding:var(--gap-sm); border-block:var(--stroke) solid var(--n-4); background:var(--n-2); color:var(--ink); text-align:left; font-weight:var(--name-weight); } $ td { padding:var(--gap-sm); border-bottom:var(--stroke) solid var(--n-3); } $ .pick { background:var(--a1-2-soft); font-weight:var(--name-weight); } $ .num { text-align:right; font-variant-numeric:tabular-nums; }
@container (max-width:700px) { $ .table { font-size:var(--type-14); } $ th,$ td { padding:calc(var(--gap-sm)/2); } }
''')
put('legend','''$ { display:flex; align-items:center; justify-content:center; gap:var(--gap); flex-wrap:wrap; } $ .key { display:inline-flex; align-items:center; gap:var(--gap-sm); font-size:var(--type-16); font-weight:var(--label-weight); } $ .key::before { content:""; width:12px; height:12px; background:var(--a1); } $ .tone-2::before { background:var(--a2); } $ .tone-3::before { background:var(--a3); } $ .tone-4::before { background:var(--a4); } $ .tone-5::before { background:var(--n-5); }
@container (max-width:450px) { $ .key { font-size:var(--type-12); } }
''')
put('steps','''$ { display:flex; align-items:stretch; justify-content:center; gap:var(--gap-lg); }
$ .step { flex:1; min-width:0; position:relative; display:grid; grid-template-rows:120px auto 1fr; gap:var(--gap-sm); text-align:center; align-content:center; padding-block:var(--gap-lg); }
$ .mark { display:flex; align-items:center; justify-content:center; width:120px; height:120px; border-radius:50%; background:var(--n-2); color:var(--ink); justify-self:center; font-size:var(--type-28); font-weight:var(--name-weight); } $ .mark .icon { width:64px; height:64px; }
$ .step.on .mark { background:var(--a1); color:var(--a1-on); }
$ .step:not(:last-child)::after { content:""; position:absolute; right:calc(var(--gap-lg)/-1); top:calc(var(--gap-lg) + 60px); width:var(--gap-lg); border-top:2px dotted var(--n-5); }
$.col { flex-direction:column; gap:var(--gap-sm); } $.col .step { grid-template-columns:64px 1fr; grid-template-rows:auto auto; padding:var(--gap-sm); text-align:left; align-items:center; } $.col .mark { grid-row:1 / span 2; width:64px; height:64px; } $.col .mark .icon { width:36px; height:36px; } $.col .step:not(:last-child)::after { right:auto; left:44px; top:calc(100% - var(--gap-sm)); height:var(--gap-sm); width:0; border-top:0; border-left:2px dotted var(--n-5); }
@container (max-width:700px) { $ .step { grid-template-rows:72px auto 1fr; } $ .mark { width:72px; height:72px; } $ .mark .icon { width:40px; height:40px; } $ .name { font-size:var(--type-18); } $ .note { font-size:var(--type-14); } $ .step:not(:last-child)::after { top:calc(var(--gap-lg) + 36px); } }
''')
put('timeline','''$ { display:flex; align-items:center; gap:var(--gap); }
$ .stop { flex:1; min-width:0; position:relative; padding-top:var(--gap-lg); border-top:var(--stroke) solid var(--n-4); }
$ .stop::before { content:""; position:absolute; left:0; top:-6px; width:12px; height:12px; border-radius:50%; background:var(--n-4); } $ .stop.on::before { background:var(--a1); } $ .kick { display:block; margin-bottom:var(--gap-sm); } $ .name { display:block; margin-bottom:var(--gap-sm); }
$.alt .stop:nth-child(even) { transform:translateY(calc(var(--gap-lg)*2)); }
$.col { flex-direction:column; align-items:stretch; gap:0; justify-content:center; } $.col .stop { flex:0 1 auto; padding:var(--gap-sm) var(--gap-lg); border-top:0; border-left:var(--stroke) solid var(--n-4); } $.col .stop::before { left:-6px; top:var(--gap); } $.col .stop .kick { position:absolute; right:var(--gap); top:var(--gap-sm); }
@container (max-width:700px) { $ .name { font-size:var(--type-18); } $ .note { font-size:var(--type-14); } }
''')
# Radial relationships use true circular focal centres and thin spokes.
for n,root,member in [('cycle','cycle','node'),('hub','hub','spoke')]:
 put(n,'''$ { position:relative; display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); grid-template-rows:repeat(3,minmax(0,1fr)); gap:var(--gap-sm); padding:var(--gap-sm); }
$ .core { grid-column:2; grid-row:2; justify-self:center; align-self:center; width:min(100%,190px); aspect-ratio:1; border-radius:50%; background:var(--a1); color:var(--a1-on); display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; z-index:2; }
$ .core .name { font-size:var(--type-28); } $ .core .icon { width:64px; height:64px; }
$ .MEM { position:relative; background:var(--page); border-top:var(--stroke) solid var(--n-3); padding:var(--gap-sm); display:flex; flex-direction:column; justify-content:center; gap:calc(var(--gap-sm)/2); text-align:center; z-index:1; }
$ .MEM::after { content:""; position:absolute; width:var(--gap); border-top:var(--stroke) solid var(--n-4); top:50%; left:100%; z-index:-1; }
$ .MEM:nth-child(2) { grid-area:1/1; } $ .MEM:nth-child(3) { grid-area:1/3; } $ .MEM:nth-child(4) { grid-area:2/3; } $ .MEM:nth-child(5) { grid-area:3/3; } $ .MEM:nth-child(6) { grid-area:3/1; } $ .MEM:nth-child(7) { grid-area:2/1; }
$ .MEM.on { background:var(--a1-2-soft); border-color:var(--a1); }
@container (max-width:700px) { $ .name { font-size:var(--type-16); } $ .note { font-size:var(--type-12); } $ .core .name { font-size:var(--type-20); } }
'''.replace('MEM',member))
put('funnel','''$ { display:flex; flex-direction:column; align-items:center; justify-content:center; gap:var(--gap-sm); } $ .stage { width:calc(25% + var(--v)*.75%); flex:1; min-height:0; max-height:100px; background:var(--a1-2-soft); border-top:var(--stroke) solid var(--n-4); display:flex; align-items:center; justify-content:space-between; gap:var(--gap-sm); padding:var(--gap-sm) var(--gap); } $ .stage:last-child { background:var(--a1); color:var(--a1-on); } $ .fig { font-size:var(--type-32); } $ .name { font-size:var(--type-22); }
@container (max-width:600px) { $ .fig { font-size:var(--type-24); } $ .name { font-size:var(--type-16); } }
''')
put('pyramid','''$ { display:flex; flex-direction:column; align-items:center; justify-content:center; gap:calc(var(--gap-sm)/2); } $ .level { width:90%; flex:1; min-height:0; max-height:130px; background:var(--n-2); text-align:center; display:flex; flex-direction:column; justify-content:center; padding:var(--gap-sm); clip-path:polygon(5% 0,95% 0,100% 100%,0 100%); } $ .level:nth-child(1) { width:40%; background:var(--a1); color:var(--a1-on); } $ .level:nth-child(1) .note { color:var(--a1-on); } $ .level:nth-child(2) { width:55%; } $ .level:nth-child(3) { width:70%; } $ .level:nth-child(4) { width:85%; } $ .name { font-size:var(--type-24); } $ .note { font-size:var(--type-16); }
@container (max-width:600px) { $ .name { font-size:var(--type-18); } $ .note { font-size:var(--type-12); } }
''')
for n,grid in [('matrix',2),('matrix-nine',3)]:
 put(n,f'''$ {{ display:grid; grid-template-columns:var(--gap-lg) repeat({grid},minmax(0,1fr)); grid-template-rows:repeat({grid},minmax(0,1fr)) var(--gap-lg); gap:var(--gap-sm); }}
$ .cell {{ background:var(--page); border-top:var(--stroke) solid var(--n-4); padding:var(--pad); display:flex; flex-direction:column; justify-content:center; gap:var(--gap-sm); }} $ .cell.on {{ background:var(--a1-2-soft); border-top:calc(var(--stroke)*4) solid var(--a1); }}
$ .axis-x {{ grid-row:{grid+1}; grid-column:2 / span {grid}; display:flex; justify-content:space-between; font-size:var(--type-14); }} $ .axis-y {{ grid-row:1 / span {grid}; grid-column:1; display:flex; flex-direction:column-reverse; justify-content:space-between; font-size:var(--type-14); }}
$ .kick {{ font-size:var(--type-32); color:var(--a1-8); }} $ .list {{ font-size:var(--type-16); }}
@container (max-width:700px) {{ $ .cell {{ padding:var(--gap-sm); }} $ .name {{ font-size:var(--type-18); }} $ .note {{ font-size:var(--type-14); }} }}
'''+('$.swot { grid-template-columns:repeat(2,minmax(0,1fr)); grid-template-rows:repeat(2,minmax(0,1fr)); }' if grid==2 else ''))
put('venn','''$ { position:relative; display:flex; align-items:center; justify-content:center; isolation:isolate; } $ .set { width:42%; aspect-ratio:1; max-height:90%; border-radius:50%; background:var(--n-2); border:var(--stroke) solid var(--n-4); display:flex; align-items:center; justify-content:center; margin-inline:calc(var(--gap-lg)/-1); opacity:.86; } $ .set.on { background:var(--a1-2-soft); border-color:var(--a1); } $ .name { font-size:var(--type-28); } $ .core { position:absolute; top:53%; left:50%; transform:translate(-50%,-50%); background:var(--a1); color:var(--a1-on); border-radius:999px; padding:var(--gap-sm) var(--gap); font-size:var(--type-18); }
@container (max-width:600px) { $ .name { font-size:var(--type-18); } $ .core { font-size:var(--type-14); } }
''')
put('hierarchy','''$ { display:grid; grid-auto-flow:column; grid-auto-columns:minmax(0,1fr); grid-template-rows:100px minmax(0,1fr); column-gap:var(--gap); row-gap:var(--gap-lg); align-content:center; }
$ .root { grid-column:1 / -1; justify-self:center; width:40%; background:var(--a1); color:var(--a1-on); display:flex; align-items:center; justify-content:center; position:relative; } $ .root::after { content:""; position:absolute; height:var(--gap-lg); border-left:var(--stroke) solid var(--n-4); top:100%; left:50%; }
$ .branch { grid-row:2; position:relative; display:flex; flex-direction:column; gap:var(--gap-sm); border-top:var(--stroke) solid var(--n-4); padding-top:var(--gap-sm); } $ .node { background:var(--n-2); padding:var(--gap-sm); text-align:center; } $ .leaf { padding:var(--gap-sm); text-align:center; border-bottom:var(--stroke) solid var(--n-3); } $ .leaf .name { font-size:var(--type-18); }
@container (max-width:700px) { $ .name { font-size:var(--type-16); } $ .leaf .name { font-size:var(--type-14); } }
''')
for n in ['flowchart','swimlane']:
 put(n,'''$ { display:grid; grid-template-columns:repeat(var(--cols,3),minmax(0,1fr)); grid-auto-rows:minmax(0,1fr); gap:var(--gap-lg); padding:var(--gap); }
$ .node { min-height:0; position:relative; background:var(--page); border:var(--stroke) solid var(--n-4); padding:var(--gap-sm); display:flex; align-items:center; justify-content:center; text-align:center; } $ .node.start,$ .node.end { border-radius:999px; background:var(--a1-2-soft); } $ .node.ask { border-color:var(--a1); background:var(--n-1); }
$ .node.to-r::after { content:""; position:absolute; width:var(--gap-lg); left:100%; top:50%; border-top:var(--stroke) solid var(--n-5); }
$ .node.to-d::before { content:""; position:absolute; height:var(--gap-lg); top:100%; left:50%; border-left:var(--stroke) solid var(--n-5); }
$ .node.to-l::after { content:""; position:absolute; width:var(--gap-lg); right:100%; top:50%; border-top:var(--stroke) solid var(--n-5); }
$ .node.to-u::before { content:""; position:absolute; height:var(--gap-lg); bottom:100%; left:50%; border-left:var(--stroke) solid var(--n-5); }
$ .lane { grid-column:1 / -1; background:var(--n-1); border-block:var(--stroke) solid var(--n-3); padding:var(--gap-sm); z-index:0; } $ .lane .name { font-size:var(--type-14); position:absolute; transform:translateY(-100%); } $ .node { z-index:1; }
@container (max-width:700px) { $ .name { font-size:var(--type-16); } }
''')
put('architecture','''$ { display:flex; flex-direction:column; justify-content:center; gap:var(--gap-sm); } $ .layer { display:flex; align-items:center; gap:var(--gap-sm); flex:1; min-height:0; max-height:120px; padding:var(--gap-sm); background:var(--page); border-bottom:var(--stroke) solid var(--n-3); } $ .layer > .name { align-self:stretch; width:25%; display:flex; align-items:center; justify-content:center; background:var(--a1); color:var(--a1-on); font-size:var(--type-22); flex:none; } $ .chip { flex:1; text-align:center; padding:var(--gap-sm); background:var(--n-1); font-size:var(--type-18); }
@container (max-width:700px) { $ .layer > .name { font-size:var(--type-16); } $ .chip { font-size:var(--type-14); padding:calc(var(--gap-sm)/2); } }
''')
put('versus','''$ { display:flex; gap:var(--gap); align-items:stretch; } $ .side { background:var(--page); flex:1; padding:var(--pad); border-top:calc(var(--stroke)*4) solid var(--n-4); display:flex; flex-direction:column; justify-content:center; gap:var(--gap); } $ .side.on { background:var(--a1-2-soft); border-color:var(--a1); } $ .side > .name { font-size:var(--type-32); text-align:center; } $ .vs { align-self:center; border-radius:50%; width:64px; height:64px; flex:none; background:var(--ink); color:var(--page); display:flex; align-items:center; justify-content:center; font-size:var(--type-20); font-weight:var(--label-weight); }
@container (max-width:700px) { $ .side > .name { font-size:var(--type-24); } $ .vs { width:40px; height:40px; font-size:var(--type-14); } }
''')
put('pricing','''$.plans { display:flex; gap:var(--gap); } $.plans > .plan { flex:1; min-width:0; } $.plan { position:relative; display:flex; flex-direction:column; justify-content:center; gap:var(--gap); padding:var(--pad); background:var(--page); border-top:calc(var(--stroke)*5) solid var(--n-4); } $.plan.on { border-color:var(--a1); background:var(--a1-2-soft); } $.plan > .name { font-size:var(--type-28); text-align:center; } $ .price { display:flex; align-items:baseline; justify-content:center; gap:var(--gap-sm); } $ .price .fig { font-size:var(--type-44); } $ .price small { font-size:var(--type-18); } $ .tag { position:absolute; top:var(--gap-sm); right:var(--gap-sm); } $ .list .name { font-size:var(--type-16); }
@container (max-width:300px) { $.plan > .name { font-size:var(--type-22); } $ .price .fig { font-size:var(--type-32); } $ .price small { font-size:var(--type-14); } }
''')
put('person','''$.people { display:flex; gap:var(--gap); } $.people > .person { flex:1; min-width:0; } $.person { display:flex; flex-direction:column; align-items:center; justify-content:center; gap:var(--gap-sm); padding:var(--pad); background:var(--page); text-align:center; border-bottom:calc(var(--stroke)*5) solid var(--n-4); } $.person.on { background:var(--a1-2-soft); border-color:var(--a1); } $ .seat { width:90%; max-height:52%; aspect-ratio:1; border:var(--stroke) solid var(--n-5); flex:0 1 auto; } $ .seat.avatar { width:112px; height:112px; } $ .name { font-size:var(--type-28); } $ .note { font-size:var(--type-16); } $ .list .name { font-size:var(--type-16); }
@container (max-width:300px) { $ .name { font-size:var(--type-22); } $ .note { font-size:var(--type-14); } }
''')
put('logo-group','''$ { display:flex; align-items:center; justify-content:center; gap:var(--gap); flex-wrap:wrap; } $ .seat.logo { width:min(22%,150px); aspect-ratio:1; border:var(--stroke) solid var(--n-3); background:var(--page); }
@container (max-width:500px) { $ .seat.logo { width:26%; } }
''')
put('image-frame','''$ { display:flex; align-items:center; justify-content:center; padding:var(--gap-sm); background:var(--page); border-top:calc(var(--stroke)*5) solid var(--n-4); } $ .seat { width:min(100%,80cqh); height:auto; aspect-ratio:1; border:var(--stroke) solid var(--n-4); }
@container (max-width:500px) { $ .seat { width:min(100%,86cqh); } }
''')
put('agenda','''$ { display:flex; flex-direction:column; justify-content:center; gap:var(--gap-sm); }
$ .entry { display:flex; align-items:center; gap:var(--gap-sm); background:var(--page); padding:var(--gap-sm); min-height:50px; } $ .mark { display:flex; width:34px; height:34px; border-radius:50%; flex:none; background:var(--ink); color:var(--page); align-items:center; justify-content:center; font-size:var(--type-12); font-weight:var(--label-weight); } $ .name { font-size:var(--type-22); } $ .note { font-size:var(--type-14); margin-left:auto; text-align:right; } $ .entry.on .mark { background:var(--a1); color:var(--a1-on); }
@container (max-width:600px) { $ .name { font-size:var(--type-16); } $ .note { font-size:var(--type-12); } }
''')
put('chart-stack','''$ { display:flex; align-items:stretch; gap:var(--gap-sm); padding:var(--gap-lg) var(--gap-sm); border-bottom:var(--stroke) solid var(--n-4); }
$ .sbar { flex:1; min-width:0; display:flex; flex-direction:column-reverse; position:relative; justify-content:flex-start; } $ .sbar > span { position:absolute; top:calc(100% + var(--gap-sm)); left:0; right:0; text-align:center; font-size:var(--type-14); white-space:nowrap; }
$ .seg { height:calc(var(--v)/var(--max)*100%); flex:none; background:var(--a1-3-soft); display:flex; align-items:center; justify-content:center; border-bottom:var(--stroke) solid var(--page); } $ .seg:nth-of-type(2) { background:var(--n-3); } $ .seg:nth-of-type(3) { background:var(--a2-3-soft); } $ .seg.tone-2 { background:var(--a2-3-soft); } $ .seg.tone-3 { background:var(--a3-3-soft); } $ .seg b { font-size:var(--type-16); font-weight:var(--figure-weight); } $.pct { --max:100; }
$.h { flex-direction:column; padding-left:calc(var(--gap-lg)*3); } $.h .sbar { flex-direction:row; } $.h .seg { width:calc(var(--v)/var(--max)*100%); height:100%; } $.h .sbar > span { right:calc(100% + var(--gap-sm)); left:auto; top:50%; transform:translateY(-50%); width:calc(var(--gap-lg)*2); }
@container (max-width:700px) { $ .seg b { font-size:var(--type-12); } $ .sbar > span { font-size:var(--type-12); } $:has(.sbar:nth-child(9)) .sbar:nth-child(even) > span { visibility:hidden; } }
''')
put('chart-waterfall','''$ { display:flex; align-items:stretch; gap:var(--gap-sm); padding:var(--gap-lg) var(--gap-sm); border-bottom:var(--stroke) solid var(--n-4); } $ .move { position:relative; flex:1; min-width:0; } $ .move::before { content:""; position:absolute; left:10%; right:10%; bottom:calc(min(var(--from),var(--to))/var(--max)*100%); height:calc(abs(var(--to) - var(--from))/var(--max)*100%); background:var(--a1-3-soft); } $ .move.down::before { background:var(--n-4); } $ .move.total::before { bottom:0; height:calc(var(--to)/var(--max)*100%); background:var(--a1); } $ .move::after { content:""; position:absolute; left:90%; width:calc(20% + var(--gap-sm)); bottom:calc(var(--to)/var(--max)*100%); border-top:var(--stroke) dotted var(--n-5); } $ .move:last-child::after { display:none; } $ b { position:absolute; bottom:calc(max(var(--from),var(--to))/var(--max)*100% + var(--gap-sm)/2); width:100%; text-align:center; font-size:var(--type-18); } $ span { position:absolute; top:calc(100% + var(--gap-sm)); width:100%; text-align:center; font-size:var(--type-14); }
@container (max-width:700px) { $ b { font-size:var(--type-14); } $ span { font-size:var(--type-12); } }
''')
put('chart-area','''$ { isolation:isolate; position:relative; border-bottom:var(--stroke) solid var(--n-4); }
$ .series { position:absolute; inset:0 0 var(--gap-lg); display:grid; grid-auto-flow:column; grid-auto-columns:minmax(0,1fr); grid-template-rows:minmax(0,1fr); anchor-scope:all; --undertow-area-color:var(--a1-3-soft); }
$ .series:nth-child(1) { z-index:4; } $ .series:nth-child(2) { z-index:3; --undertow-area-color:var(--n-3); } $ .series:nth-child(3) { z-index:2; --undertow-area-color:var(--a2-3-soft); } $ .series:nth-child(4) { z-index:1; --undertow-area-color:var(--a3-3-soft); }
$ .series > .name { position:absolute; top:0; left:0; font-size:var(--type-14); color:var(--ink); background:var(--page); padding:calc(var(--gap-sm)/3) var(--gap-sm); border-radius:999px; z-index:5; } $ .series:nth-child(2) > .name { left:25%; } $ .series:nth-child(3) > .name { left:50%; } $ .series:nth-child(4) > .name { left:75%; }
$ .pt { position:static; align-self:start; justify-self:center; width:0; height:0; margin-top:calc(var(--gap-lg)*2 + (100cqh - var(--gap-lg)*3)*(1 - var(--v)/var(--max))); anchor-name:var(--undertow-self); }
$ .pt::before { content:none; }
$ .pt::after { content:""; position:absolute; left:anchor(var(--undertow-prev) center); right:anchor(var(--undertow-self) center); top:calc(anchor(var(--undertow-prev) top) - 100cqh); bottom:0; background:var(--undertow-area-color); clip-path:polygon(0 100cqh,100% calc(100% - (100cqh - var(--gap-lg)*3)*var(--v)/var(--max)),100% 100%,0 100%); }
$ .pt:first-of-type::before,$ .pt:first-of-type::after { content:none; } $ .pt b { position:absolute; transform:translate(-50%,-150%); font-size:var(--type-14); color:var(--ink); z-index:6; } $ .axis { position:absolute; left:0; right:0; bottom:0; height:var(--gap-lg); display:flex; justify-content:space-around; align-items:center; font-size:var(--type-14); }
@container (max-width:600px) { $ .pt b,$ .series > .name,$ .axis { font-size:var(--type-12); } $ .axis span:nth-child(even):not(:last-child) { visibility:hidden; } }
'''+''.join(f'$ .pt:nth-child({i} of .pt) {{ --undertow-self:--undertow-area-{i}; --undertow-prev:--undertow-area-{i-1}; }}\n' for i in range(1,13)))
put('chart-scatter','''$ { position:relative; border-left:var(--stroke) solid var(--n-4); border-bottom:var(--stroke) solid var(--n-4); margin:var(--gap-lg); }
$ .axis-x { position:absolute; left:0; right:0; bottom:calc(var(--gap-lg)/-1); text-align:center; font-size:var(--type-14); } $ .axis-y { position:absolute; top:0; left:0; transform:translateY(-150%); font-size:var(--type-14); }
$ .dot { position:absolute; left:calc(8% + var(--x)/var(--xmax)*84%); bottom:calc(8% + var(--y)/var(--ymax)*80%); width:12px; height:12px; border-radius:50%; background:var(--n-5); transform:translate(-50%,50%); } $ .dot.on { background:var(--a1); } $ .dot span { position:absolute; left:50%; top:100%; transform:translateX(-50%); white-space:nowrap; font-size:var(--type-12); padding-top:calc(var(--gap-sm)/2); }
$.bubble .dot { width:calc(12px + var(--r)*.6px); height:calc(12px + var(--r)*.6px); background:var(--a1-3-soft); border:var(--stroke) solid var(--a1); }
@container (max-width:600px) { $ .dot span { font-size:var(--type-10); } }
''')
put('sparkline','''$ { display:flex; align-items:end; gap:calc(var(--gap-sm)/3); padding:var(--gap-sm); } $ > span { display:block; flex:1; height:calc(var(--v)/var(--max)*90%); background:var(--n-4); border-top:2px solid var(--a1); min-height:2px; } $.bars > span { background:var(--a1); } $.up > span { border-color:var(--good); } $.down > span { border-color:var(--bad); }
@container (max-height:120px) { $ > span { border-top-width:1px; } }
''')
put('heatmap','''$ { display:flex; flex-direction:column; justify-content:center; gap:calc(var(--gap-sm)/2); } $ .heads,$ .row { display:grid; grid-template-columns:120px repeat(var(--cols),minmax(0,1fr)); gap:calc(var(--gap-sm)/2); } $ .heads { padding-left:calc(120px + var(--gap-sm)/2); grid-template-columns:repeat(var(--cols),minmax(0,1fr)); } $ .heads span { text-align:center; font-size:var(--type-14); } $ .row { flex:0 1 58px; } $ .row > .name { font-size:var(--type-18); display:flex; align-items:center; } $ .cell { display:flex; align-items:center; justify-content:center; background:color-mix(in srgb,var(--a1-5-soft) calc(var(--v)*1%),var(--page)); border:var(--stroke) solid var(--n-2); } $ .cell b { font-size:var(--type-16); color:var(--ink); } $.calendar .heads { padding-left:0; } $.calendar .row { grid-template-columns:repeat(var(--cols),minmax(0,1fr)); } $.calendar .cell { aspect-ratio:1; }
@container (max-width:700px) { $ .heads span { font-size:var(--type-10); } $ .row > .name,$ .cell b { font-size:var(--type-12); } }
''')
put('waffle','''$ { display:flex; flex-direction:column; align-items:center; justify-content:center; gap:var(--gap-sm); padding:var(--gap-sm); } $ .units { width:min(100%,70cqh); display:grid; grid-template-columns:repeat(10,minmax(0,1fr)); gap:calc(var(--gap-sm)/2); } $ .u { display:block; aspect-ratio:1; background:var(--n-2); } $ .u.on { background:var(--a1); } $ .u.tone-2 { background:var(--a2); } $ .fig { font-size:var(--type-40); } $ .name { font-size:var(--type-20); } $.figures .u { clip-path:polygon(35% 0,65% 0,75% 20%,65% 35%,85% 40%,90% 68%,70% 68%,65% 100%,35% 100%,30% 68%,10% 68%,15% 40%,35% 35%,25% 20%); }
@container (max-width:400px) { $ .fig { font-size:var(--type-28); } $ .name { font-size:var(--type-16); } }
''')
put('treemap','''$ { display:flex; gap:calc(var(--gap-sm)/2); } $ > .branch { flex:var(--v); min-width:0; display:flex; flex-direction:column; gap:calc(var(--gap-sm)/2); background:var(--n-1); } $ > .branch > .name { flex:none; min-height:var(--gap-lg); display:flex; align-items:center; justify-content:center; font-size:var(--type-16); } $ .tile { flex:var(--v); min-height:0; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:calc(var(--gap-sm)/2); background:var(--n-2); padding:calc(var(--gap-sm)/2); text-align:center; } $ .tile.on { background:var(--a1); color:var(--a1-on); } $ .tile .name { font-size:var(--type-18); } $ .tile .fig { font-size:var(--type-28); }
@container (max-width:700px) { $ > .branch > .name,$ .tile .name { font-size:var(--type-12); } $ .tile .fig { font-size:var(--type-18); } }
''')
put('sankey','''$ { display:grid; grid-template-columns:minmax(0,1fr) minmax(0,2fr); grid-auto-rows:minmax(0,1fr); column-gap:calc(var(--gap-lg)*2); row-gap:var(--gap-sm); padding:var(--gap); } $ .source { grid-column:1; grid-row:1 / span 6; align-self:center; background:var(--ink); color:var(--page); padding:var(--pad); display:flex; flex-direction:column; justify-content:center; gap:var(--gap-sm); min-height:40%; } $ > .branch { grid-column:2; display:flex; align-items:center; justify-content:space-between; gap:var(--gap-sm); background:var(--n-2); padding:var(--gap-sm); position:relative; min-height:50px; } $ .branch::before { content:""; position:absolute; right:100%; width:calc(var(--gap-lg)*2); top:20%; bottom:20%; background:var(--a1-2-soft); transform-origin:right center; } $ .branch.on { background:var(--a1-2-soft); border-right:calc(var(--stroke)*4) solid var(--a1); } $ .branch.out { border-right:calc(var(--stroke)*4) solid var(--n-5); } $ .branch .branch { padding:calc(var(--gap-sm)/2); border-left:var(--stroke) solid var(--n-4); } $ .fig { font-size:var(--type-28); }
@container (max-width:700px) { $ .name { font-size:var(--type-16); } $ .fig { font-size:var(--type-20); } }
''')
put('radar','''$ { position:relative; isolation:isolate; }
$::before { content:""; position:absolute; width:min(60%,65cqh); height:min(65cqw,65cqh); left:50%; top:50%; transform:translate(-50%,-50%); border:var(--stroke) solid var(--n-4); border-radius:50%; background:radial-gradient(circle,transparent 30%,var(--n-2) 31%,transparent 32%,transparent 60%,var(--n-2) 61%,transparent 62%); }
$ .axis { position:absolute; left:calc(50% + 43%*sin(var(--undertow-angle))); top:calc(50% - 43%*cos(var(--undertow-angle))); transform:translate(-50%,-50%); font-size:var(--type-16); }
$ .series { position:absolute; width:min(60%,65cqh); height:min(65cqw,65cqh); left:50%; top:50%; transform:translate(-50%,-50%); background:var(--a1-3-soft); opacity:.75; clip-path:polygon(50% calc(50% - var(--v1)/var(--max)*50%),calc(50% + var(--v2)/var(--max)*47.55%) calc(50% - var(--v2)/var(--max)*15.45%),calc(50% + var(--v3)/var(--max)*29.39%) calc(50% + var(--v3)/var(--max)*40.45%),calc(50% - var(--v4)/var(--max)*29.39%) calc(50% + var(--v4)/var(--max)*40.45%),calc(50% - var(--v5)/var(--max)*47.55%) calc(50% - var(--v5)/var(--max)*15.45%)); }
$ .series:nth-last-child(1) { background:var(--n-4); opacity:.45; } $ .series .name { display:none; }
@container (max-width:600px) { $ .axis { font-size:var(--type-12); } }
'''+''.join(f'$ .axis:nth-child({i}) {{ --undertow-angle:calc({i-1}*360deg/var(--n)); }}\n' for i in range(1,9)))
put('bullet','''$.bullets { display:flex; flex-direction:column; justify-content:center; gap:var(--gap); } $.bullet { position:relative; min-height:90px; padding-bottom:var(--gap-lg); display:flex; align-items:center; gap:var(--gap); } $ .name { font-size:var(--type-20); } $ .fig { font-size:var(--type-28); margin-left:auto; } $ .note { font-size:var(--type-14); } $.bullet::before { content:""; position:absolute; left:0; right:0; bottom:var(--gap-sm); height:16px; background:linear-gradient(to right,var(--n-2) calc(var(--low,60)*1%),var(--n-3) 0 calc(var(--high,85)*1%),var(--n-4) 0); } $.bullet::after { content:""; position:absolute; left:0; width:calc(var(--v)*1%); bottom:calc(var(--gap-sm) + 4px); height:8px; background:var(--a1); border-right:3px solid var(--ink); }
@container (max-width:600px) { $ .name { font-size:var(--type-16); } $ .fig { font-size:var(--type-22); } }
''')
put('slope','''$ { position:relative; display:flex; flex-direction:column; justify-content:center; gap:var(--gap-sm); padding-top:var(--gap-lg); }
$ .heads { display:flex; justify-content:space-between; font-size:var(--type-14); }
$ .pair { position:relative; min-height:48px; display:flex; align-items:center; gap:var(--gap); padding:var(--gap-sm); border-bottom:var(--stroke) solid var(--n-3); }
$ .pair .name { width:30%; font-size:var(--type-18); } $ .pair .a { position:absolute; left:calc(32% + var(--a)/var(--max)*55%); font-size:var(--type-16); color:var(--n-8); } $ .pair .b { position:absolute; left:calc(32% + var(--b)/var(--max)*55%); font-size:var(--type-16); color:var(--ink); } $ .pair::before { content:""; position:absolute; left:calc(32% + min(var(--a),var(--b))/var(--max)*55%); width:calc(abs(var(--b) - var(--a))/var(--max)*55%); top:50%; border-top:2px solid var(--n-4); } $ .pair.on::before { border-color:var(--a1); }
@container (max-width:600px) { $ .pair .name { font-size:var(--type-14); } $ .pair .a,$ .pair .b { font-size:var(--type-12); } }
''')
put('roadmap','''$ { display:flex; flex-direction:column; justify-content:center; gap:var(--gap-sm); }
$ .heads { display:grid; grid-template-columns:repeat(var(--cols),minmax(0,1fr)); margin-left:25%; background:var(--n-2); padding:var(--gap-sm); text-align:center; font-size:var(--type-14); }
$ .lane { display:grid; grid-template-columns:25% repeat(var(--cols),minmax(0,1fr)); grid-auto-rows:minmax(40px,1fr); align-items:center; position:relative; gap:calc(var(--gap-sm)/2); padding-block:var(--gap-sm); border-bottom:var(--stroke) solid var(--n-3); }
$ .lane > .name { grid-column:1; grid-row:1 / span 3; font-size:var(--type-18); } $ .bar { grid-column:calc(var(--from) + 2) / calc(var(--to) + 2); min-height:38px; display:flex; align-items:center; justify-content:center; text-align:center; background:var(--a1-2-soft); font-size:var(--type-16); } $ .bar.on { background:var(--a1); color:var(--a1-on); } $ .mile { position:absolute; left:calc(25% + var(--at)/var(--cols)*75%); top:0; bottom:0; width:0; border-left:2px solid var(--n-5); } $ .mile span { position:absolute; top:0; transform:translateX(-50%); background:var(--page); white-space:nowrap; font-size:var(--type-12); }
@container (max-width:700px) { $ .lane > .name,$ .bar { font-size:var(--type-12); } $ .heads { font-size:var(--type-12); } }
''')
put('concentric','''$ { position:relative; display:flex; align-items:end; justify-content:center; isolation:isolate; } $ .ring { position:absolute; bottom:0; left:50%; transform:translateX(-50%); width:min(95%,90cqh); aspect-ratio:1; background:var(--n-1); border-radius:50%; display:flex; flex-direction:column; align-items:center; padding-top:var(--gap-lg); text-align:center; gap:calc(var(--gap-sm)/2); } $ .ring:nth-child(2) { width:min(70%,66cqh); background:var(--n-3); } $ .ring:nth-child(3) { width:min(43%,42cqh); background:var(--n-6); color:var(--page); } $ .ring:nth-child(4) { width:min(22%,22cqh); background:var(--a1); color:var(--a1-on); } $ .ring.on { background:var(--a1); color:var(--a1-on); } $ .name { font-size:var(--type-20); } $ .fig { font-size:var(--type-40); } $ .note { font-size:var(--type-14); }
@container (max-width:500px) { $ .name { font-size:var(--type-16); } $ .fig { font-size:var(--type-28); } }
''')
put('journey','''$ { display:flex; align-items:stretch; gap:var(--gap-sm); padding-top:var(--gap-lg); } $ .stage { flex:1; min-width:0; display:flex; flex-direction:column; justify-content:end; padding:var(--gap-sm); position:relative; background:var(--page); border-top:var(--stroke) solid var(--n-3); gap:var(--gap-sm); } $ .stage::before { content:""; position:absolute; left:50%; top:calc(60% - var(--mood)*.5%); width:12px; height:12px; border-radius:50%; background:var(--n-5); } $ .stage::after { content:""; position:absolute; left:50%; width:calc(100% + var(--gap-sm)); top:calc(60% - var(--mood)*.5% + 6px); height:2px; background:var(--a1); transform:rotate(calc((var(--mood) - var(--next,var(--mood)))*.25deg)); transform-origin:left; } $ .stage:last-child::after { content:none; } $ .stage.on { background:var(--a1-2-soft); } $ .stage.on::before { background:var(--a1); } $ .pain { font-size:var(--type-14); color:var(--bad); } $ .name { font-size:var(--type-20); } $ .note { font-size:var(--type-16); }
@container (max-width:700px) { $ .name { font-size:var(--type-16); } $ .note,$ .pain { font-size:var(--type-12); } }
''')
put('mindmap','''$ { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); grid-template-rows:repeat(3,minmax(0,1fr)); gap:var(--gap); align-items:center; } $ .core { grid-area:2/2; aspect-ratio:1; border-radius:50%; background:var(--a1); color:var(--a1-on); display:flex; align-items:center; justify-content:center; padding:var(--pad); text-align:center; z-index:2; } $ .branch { position:relative; padding:var(--gap-sm); border-bottom:var(--stroke) solid var(--n-4); display:flex; flex-direction:column; gap:calc(var(--gap-sm)/2); background:var(--page); } $ .branch::after { content:""; position:absolute; top:50%; left:100%; width:var(--gap); border-top:var(--stroke) solid var(--n-4); } $ .branch:nth-child(2) { grid-area:1/1; } $ .branch:nth-child(3) { grid-area:1/3; } $ .branch:nth-child(4) { grid-area:2/1; } $ .branch:nth-child(5) { grid-area:2/3; } $ .branch:nth-child(6) { grid-area:3/1; } $ .branch:nth-child(7) { grid-area:3/3; } $ .leaf { font-size:var(--type-16); } $ .branch.on { border-color:var(--a1); background:var(--a1-2-soft); }
@container (max-width:700px) { $ .name { font-size:var(--type-16); } $ .leaf { font-size:var(--type-12); } }
''')
put('decision-tree','''$ { display:flex; flex-direction:column; justify-content:center; align-items:center; gap:var(--gap-lg); } $ .q { padding:var(--pad); background:var(--ink); color:var(--page); text-align:center; position:relative; } $ .q::after { content:""; position:absolute; top:100%; height:var(--gap-lg); left:50%; border-left:var(--stroke) solid var(--n-4); } $ .opts { display:flex; justify-content:center; gap:var(--gap); width:100%; } $ .opt { flex:1; min-width:0; position:relative; display:flex; flex-direction:column; gap:var(--gap-sm); border-top:var(--stroke) solid var(--n-4); padding-top:var(--gap-sm); text-align:center; } $ .cond { font-size:var(--type-14); color:var(--n-8); } $ .end { padding:var(--pad); background:var(--n-1); border-bottom:var(--stroke) solid var(--n-4); } $ .end.on { background:var(--a1); color:var(--a1-on); } $ .name { font-size:var(--type-20); }
@container (max-width:700px) { $ .name { font-size:var(--type-16); } $ .cond { font-size:var(--type-12); } }
''')
put('balance','''$ { position:relative; display:grid; grid-template-columns:1fr 1fr; gap:var(--gap-lg); align-items:center; padding-bottom:calc(var(--gap-lg)*2); } $::before { content:""; position:absolute; left:10%; right:10%; bottom:var(--gap-lg); height:3px; background:var(--ink); transform:rotate(calc(var(--tilt)*.06deg)); } $ .pan { position:relative; padding:var(--pad); background:var(--page); border-bottom:calc(var(--stroke)*3) solid var(--n-4); display:flex; flex-direction:column; gap:var(--gap-sm); text-align:center; transform:translateY(calc(var(--tilt)*-.15px)); } $ .pan:nth-child(2) { transform:translateY(calc(var(--tilt)*.15px)); } $ .pan.on { border-color:var(--a1); background:var(--a1-2-soft); } $ .item { padding:var(--gap-sm); background:var(--n-1); } $ .item .name { font-size:var(--type-18); } $ .fulcrum { position:absolute; bottom:0; left:50%; transform:translateX(-50%); padding:var(--gap-sm) var(--gap); background:var(--ink); color:var(--page); border-radius:999px; font-size:var(--type-14); white-space:nowrap; }
@container (max-width:700px) { $ .name { font-size:var(--type-18); } $ .item .name { font-size:var(--type-14); } }
''')
put('positioning','''$ { position:relative; background:var(--page); margin:var(--gap-lg); } $::before { content:""; position:absolute; left:0; right:0; top:50%; border-top:var(--stroke) solid var(--n-5); } $::after { content:""; position:absolute; top:0; bottom:0; left:50%; border-left:var(--stroke) solid var(--n-5); } $ .axis-x { position:absolute; top:50%; left:0; right:0; display:flex; justify-content:space-between; padding-top:var(--gap-sm); font-size:var(--type-14); } $ .axis-y { position:absolute; left:50%; top:0; bottom:0; display:flex; flex-direction:column-reverse; justify-content:space-between; padding-left:var(--gap-sm); font-size:var(--type-14); } $ .mark { position:absolute; left:calc(10% + var(--x)*.8%); bottom:calc(10% + var(--y)*.8%); transform:translate(-50%,50%); width:12px; height:12px; border-radius:50%; background:var(--n-4); z-index:1; } $ .mark > .name { position:absolute; top:100%; left:50%; transform:translateX(-50%); white-space:nowrap; font-size:var(--type-14); padding-top:calc(var(--gap-sm)/2); } $ .mark.on { width:112px; height:112px; background:var(--a1); color:var(--a1-on); display:flex; align-items:center; justify-content:center; } $ .mark.on > .name { position:static; transform:none; white-space:normal; padding:var(--gap-sm); text-align:center; font-size:var(--type-18); } $ .seat.logo { width:48px; height:48px; border-radius:50%; }
@container (max-width:600px) { $ .mark > .name,$ .axis-x,$ .axis-y { font-size:var(--type-10); } $ .mark.on { width:72px; height:72px; } $ .mark.on > .name { font-size:var(--type-14); } }
''')
put('network','''$ { position:relative; margin:var(--gap-lg); } $ .node { position:absolute; left:calc(var(--x)*1%); top:calc(var(--y)*1%); transform:translate(-50%,-50%); width:88px; height:88px; border-radius:50%; background:var(--n-2); border:var(--stroke) solid var(--n-4); display:flex; align-items:center; justify-content:center; padding:var(--gap-sm); z-index:2; text-align:center; } $ .node.on { background:var(--a1); color:var(--a1-on); border-color:var(--a1); } $ .node .name { font-size:var(--type-16); } $ .link { position:absolute; left:calc(var(--x1)*1%); top:calc(var(--y1)*1%); width:calc(hypot((var(--x2) - var(--x1))*1cqw,(var(--y2) - var(--y1))*1cqh)); height:1px; background:var(--n-4); transform:rotate(atan2(calc((var(--y2) - var(--y1))*1cqh),calc((var(--x2) - var(--x1))*1cqw))); transform-origin:left center; z-index:1; } $ .link.strong { height:2px; background:var(--a1); }
@container (max-width:600px) { $ .node { width:64px; height:64px; } $ .node .name { font-size:var(--type-12); } }
''')
put('code','''$ { display:flex; flex-direction:column; justify-content:center; gap:var(--gap-sm); background:var(--n-1); padding:var(--pad); border-top:calc(var(--stroke)*4) solid var(--ink); } $ > .name { font-size:var(--type-16); padding-bottom:var(--gap-sm); border-bottom:var(--stroke) solid var(--n-3); } $ .lines { counter-reset:line; } $ .lines p { font-family:var(--font-body); font-size:var(--type-18); line-height:var(--body-line); white-space:pre-wrap; overflow-wrap:anywhere; } $.numbered .lines p { counter-increment:line; padding-left:var(--gap-lg); position:relative; } $.numbered .lines p::before { content:counter(line); position:absolute; left:0; width:var(--gap); color:var(--n-7); text-align:right; } $ .k { color:var(--a1-8); font-weight:var(--name-weight); } $ .s { color:var(--a2-8); } $ .c { color:var(--n-8); } $ .n { color:var(--a3-8); }
@container (max-width:600px) { $ .lines p { font-size:var(--type-14); } }
''')
css['sankey'] += "\n$ { grid-template-rows:repeat(var(--undertow-branches,3),minmax(0,1fr)); } $ .source { grid-row:1 / -1; }\n"+''.join(f'$:has(> .branch:nth-child({i} of .branch):last-child) {{ --undertow-branches:{i}; }}\n' for i in range(2,7))
css['radar'] += ''.join('@container style(--n: '+str(k)+') { $ .series { clip-path:polygon('+','.join('calc(50% + var(--v'+str(i+1)+')/var(--max)*'+str(round(50*__import__('math').sin(i*2*__import__('math').pi/k),4))+'%) calc(50% - var(--v'+str(i+1)+')/var(--max)*'+str(round(50*__import__('math').cos(i*2*__import__('math').pi/k),4))+'%)' for i in range(k))+'); } }\n' for k in range(3,9))
for n,mem in [('hub','spoke'),('cycle','node')]:
 css[n] += ''.join(f'$:has(> .{mem}:nth-child(4 of .{mem}):last-child) .{mem}:nth-child({i} of .{mem}) {{ grid-area:{row}/{col}; }}\n' for i,(row,col) in enumerate([(1,1),(1,3),(3,1),(3,3)],1))
 css[n] += ''.join(f'$:has(> .{mem}:nth-child(3 of .{mem}):last-child) .{mem}:nth-child({i} of .{mem}) {{ grid-area:{row}/{col}; }}\n' for i,(row,col) in enumerate([(1,1),(2,3),(3,1)],1))

css['list'] += '$ { container-type:inline-size; }\n'
css['card'] += '@container (min-width:500px) { $ .parts:has(.mark):not(:has(.fig)) { grid-template-columns:110px minmax(0,1fr); text-align:center; } $ .parts:has(.mark):not(:has(.fig)) > .mark { grid-column:1; grid-row:1 / span 3; } $ .parts:has(.mark):not(:has(.fig)) > .name,$ .parts:has(.mark):not(:has(.fig)) > .note { grid-column:2; } }\n'
css['chart-area'] += '$ .series { z-index:auto; overflow:hidden; } $ .pt::after { z-index:2; } $ .series:nth-child(1) .pt::after { z-index:4; } $ .series:nth-child(2) .pt::after { z-index:3; } $ .pt b,$ .series > .name { z-index:20; }\n'
css['bullet'] += '$.bullets { gap:var(--gap-sm); } $.bullet { min-height:0; flex:1; padding-bottom:var(--gap); } $.bullet::after { width:calc(min(var(--v),100)*1%); } $ .fig::before { content:""; position:absolute; width:2px; height:24px; background:var(--ink); bottom:calc(var(--gap-sm) - 4px); left:calc(var(--target)*1%); }\n'
css['gauge'] += '$ { min-height:0; }\n'
css['concentric'] += '$ .ring { padding-top:var(--gap-sm); } @container (max-width:700px) { $ .name { font-size:var(--type-16); } $ .fig { font-size:var(--type-28); } $ .ring:nth-child(4) .fig { font-size:var(--type-22); } $ .ring:nth-child(4) .name { font-size:var(--type-12); } }\n'
css['heatmap'] += '$.calendar { align-items:center; } $.calendar .heads,$.calendar .row { width:min(100%,calc((100cqh - var(--gap-lg))*var(--cols)/var(--undertow-rows,7))); } $.calendar .row { flex:1; min-height:0; } $.calendar .cell { aspect-ratio:auto; height:100%; }\n'+''.join(f'$:has(> .row:nth-child({i} of .row):last-child) {{ --undertow-rows:{i}; }}\n' for i in range(2,13))
css['metric'] += '@container (max-height:130px) { $ .parts { gap:calc(var(--gap-sm)/2); } $ .fig { font-size:var(--type-28); } $ .name { font-size:var(--type-14); } $ .note { font-size:var(--type-12); } $ .fig small { font-size:var(--type-14); } }\n'
css['person'] += '$.person:has(> .list) { display:grid; grid-template-columns:30% minmax(0,1fr); align-content:center; align-items:center; text-align:left; } $.person:has(> .list) > .seat { grid-column:1; grid-row:1 / span 3; width:100%; height:auto; max-height:none; } $.person:has(> .list) > .name,$.person:has(> .list) > .note,$.person:has(> .list) > .list { grid-column:2; width:100%; } $.person > .list { flex:none; }\n'
css['roadmap'] += '$ .heads { flex:none; } $ .lane { flex:1; min-height:0; grid-template-rows:repeat(2,minmax(0,1fr)); grid-auto-rows:minmax(0,1fr); } $ .lane > .name { grid-row:1 / span 2; } $ .bar { min-height:0; height:100%; }\n'
css['slope'] += '$ { gap:calc(var(--gap-sm)/2); padding-top:0; } $ .pair { min-height:0; flex:1; padding:calc(var(--gap-sm)/2); } $ .pair .a { top:0; transform:translateX(-50%); line-height:var(--label-line); } $ .pair .b { bottom:0; top:auto; transform:translateX(-50%); line-height:var(--label-line); }\n'
css['steps'] += '@container (max-width:900px) { $:has(> .step:nth-child(5)) .step { grid-template-rows:56px auto 1fr; } $:has(> .step:nth-child(5)) .mark { width:56px; height:56px; } $:has(> .step:nth-child(5)) .name { font-size:var(--type-16); } $:has(> .step:nth-child(5)) .note { font-size:var(--type-12); } }\n'
css['treemap'] += '$ > .branch:only-child { flex-direction:row; flex-wrap:wrap; } $ > .branch:only-child > .name { flex-basis:100%; min-height:var(--gap-lg); } $ > .branch:only-child > .tile { height:calc(100% - var(--gap-lg) - var(--gap-sm)/2); }\n'
css['venn'] += '$ .core { top:80%; }\n'
css['sankey'] += '$ > .branch::before { height:calc(12px + var(--v)*.5px); top:50%; bottom:auto; transform:translateY(-50%); }\n'
# Prefix all roots; shared text rules remain scoped to each element.
for d in sorted((C/'elements').iterdir()):
 n=d.name;co=next(x for x in tax['contracts'] if x['id']==json.loads((d/'element.json').read_text())['contract']); roots=co['roots'];root=':is('+','.join('.'+x+'[data-el="undertow-'+n+'"]' for x in roots)+')'
 common='''$ { min-width:0; min-height:0; position:relative; container-type:size; font-family:var(--font-body); font-weight:var(--body-weight); line-height:var(--body-line); letter-spacing:var(--body-track); }
$ * { box-sizing:border-box; } $ .name { font-family:var(--font-display); font-size:var(--type-24); font-weight:var(--name-weight); line-height:var(--name-line); letter-spacing:var(--name-track); }
$ .fig { font-family:var(--font-display); font-size:var(--type-40); font-weight:var(--figure-weight); line-height:var(--figure-line); letter-spacing:var(--figure-track); font-variant-numeric:tabular-nums; }
$ .fig small { font-size:var(--type-20); font-weight:var(--label-weight); } $ .note { font-size:var(--type-16); font-weight:var(--body-weight); line-height:var(--body-line); color:var(--n-8); } $ .kick { font-size:var(--type-12); font-weight:var(--label-weight); line-height:var(--label-line); letter-spacing:var(--label-track); color:var(--n-8); }
'''
 if n not in css:raise Exception('Missing '+n)
 write(d/'element.css',(common+css[n]).replace('$',root))
print('authored CSS',len(css))
