from pathlib import Path
import json
C=Path('/workspace/work/deliverables/nocturne/collection/nocturne')
for p in C.glob('elements/*/element.json'):
 x=json.loads(p.read_text());x['registrations']={};x['tokenDefaults']={};p.write_text(json.dumps(x,indent=2))
for p in list(C.glob('elements/*/element.css'))+[C/'foundation/foundation.css']:
 s=p.read_text().replace('color:var(--a1)','color:var(--a1-7)').replace('color:var(--a2)','color:var(--a2-7)').replace('color:var(--n-6)','color:var(--n-7)');p.write_text(s)
def patch(name,css):
 p=C/'elements'/name/'element.css';p.write_text(p.read_text()+css.replace('R',f'[data-el="nocturne-{name}"]')+'\n')
patch('pill','''R.pill.pill{height:68px;min-height:68px;max-height:68px;flex:0 0 auto}R .parts{padding:0;line-height:var(--label-line)}''')
patch('tag','''R.tag,R.hl{container-type:normal}''')
patch('chart-area','''R .series>.name,R .pt>b{color:var(--a1-7)}R .series:nth-of-type(2)>.name,R .series:nth-of-type(2) .pt>b{color:var(--a2-7)}R .series:nth-of-type(3)>.name,R .series:nth-of-type(3) .pt>b{color:var(--a3-7)}''')
print('Applied contrast and inline-atom adjustments')
# Normalize legacy list fixtures to the current contract; nested lists must retain natural block height.
import re
mandatory={'card','callout','chart-area','chart-bar','chart-donut','chart-line'}
for p in C.glob('elements/*/fixtures/*.html'):
 if p.parent.parent.name in mandatory:continue
 s=p.read_text()
 s=re.sub(r'<li>(.*?)</li>',r'<li class="item"><p class="name">\1</p></li>',s,flags=re.S)
 p.write_text(s)
patch('list','''R.list{container-type:inline-size;width:100%}''')
patch('matrix','''R.swot .cell>.list{width:100%;container-type:inline-size;gap:calc(var(--gap-sm)/2)}R.swot .cell>.list .item{padding-left:var(--gap)}R.swot .cell>.list .item::before{left:0;width:6px;height:6px}R.swot .cell>.list .name{font-size:var(--type-16)}R .axis-y{writing-mode:horizontal-tb;flex-direction:column;align-items:center;width:var(--type-20)}R .axis-y>span{writing-mode:vertical-rl;white-space:nowrap}@container(max-width:800px){R.swot .cell>.kick{font-size:var(--type-24)}R.swot .cell>.name{font-size:var(--type-18)}R.swot .cell{gap:calc(var(--gap-sm)/2)}R.swot .cell>.list .name{font-size:var(--type-14)}}''')
patch('matrix-nine','''R .axis-y{writing-mode:horizontal-tb;flex-direction:column;align-items:center;width:var(--type-20)}R .axis-y>span{writing-mode:vertical-rl;white-space:nowrap}''')
patch('positioning','''R .axis-y{writing-mode:horizontal-tb;flex-direction:column;align-items:center;width:var(--type-20)}R .axis-y>span{writing-mode:vertical-rl;white-space:nowrap}''')
patch('hub','''R{--nocturne-spoke-count:4}R:has(>.spoke:nth-of-type(4):last-child){--nocturne-spoke-count:3}R:has(>.spoke:nth-of-type(6):last-child){--nocturne-spoke-count:5}R:has(>.spoke:nth-of-type(7):last-child){--nocturne-spoke-count:6}R::after{content:'';position:absolute;inset:15%;background:repeating-conic-gradient(from -90deg,var(--n-4) 0deg .18deg,transparent .18deg calc(360deg/var(--nocturne-spoke-count)));border-radius:50%;z-index:-1}''')
patch('card','''R .parts{height:100%}R .parts>.name{min-height:calc(var(--type-28)*var(--name-line)*2);display:flex;justify-content:center;align-items:flex-start;width:100%}R .parts>.note{min-height:calc(var(--type-18)*var(--body-line)*3)}@container(max-width:280px){R .parts>.name{min-height:calc(var(--type-22)*var(--name-line)*2)}R .parts>.note{min-height:calc(var(--type-16)*var(--body-line)*3)}}''')
print('Normalized nested lists, aligned card titles, refined axes and hub spokes')
# Compact atoms retain practical allocations; only their multi-member stacks need more rows.
mins={'pill':{'pill':'4x1','pill-stack':'5x3'},'delta':{'delta':'4x1','delta-stack':'5x3'},'tag':{'tag-hl':'5x2','extended':'5x2'},'legend':{},'gauge':{'meter':'4x1','meter-4':'6x4'}}
for folder,fixtures in mins.items():
 for p in (C/'elements'/folder/'fixtures').glob('*.html'):
  m=fixtures.get(p.stem,'6x1' if folder=='legend' else '4x1');p.write_text(re.sub(r'<!-- min: [^>]+ -->',f'<!-- min: {m} -->',p.read_text(),count=1))
patch('callout','''@container(max-height:100px){R p{font-size:var(--type-18)}R .icon{width:28px;height:28px}}''')
patch('sankey','''R{anchor-scope:all}R .source{anchor-name:--nocturne-sankey-source}R>.branch::before{left:anchor(--nocturne-sankey-source right);right:100%;width:auto;top:calc(anchor(--nocturne-sankey-source center) - 100cqh);bottom:0;border-radius:0;clip-path:polygon(0 calc(100cqh - var(--v)*.15cqh),100% calc(100% - var(--v)*1cqh + var(--gap-sm)),100% 100%,0 calc(100cqh + var(--v)*.15cqh));z-index:-1}R>.branch:has(>.branch){display:grid;grid-template-columns:30% 1fr;grid-auto-rows:minmax(0,1fr);column-gap:var(--pad);row-gap:var(--gap-sm);padding:var(--gap-sm)}R>.branch:has(>.branch)>.name{grid-column:1;grid-row:1;align-self:end}R>.branch:has(>.branch)>.fig{grid-column:1;grid-row:2;align-self:start}R>.branch>.branch{grid-column:2;margin:0;min-height:0;padding:calc(var(--gap-sm)/3);border:1px solid var(--n-4);border-radius:var(--radius-sm);background:var(--page)}R>.branch>.branch:nth-of-type(1){grid-row:1}R>.branch>.branch:nth-of-type(2){grid-row:2}R>.branch>.branch:nth-of-type(3){grid-row:3}R>.branch>.branch::before{content:'';position:absolute;right:100%;top:20%;bottom:20%;width:var(--pad);background:var(--a1-3-soft);clip-path:polygon(0 35%,100% 0,100% 100%,0 65%);z-index:-1}''')
print('Compact allocations and connected Sankey branches applied')
patch('pill','''R.pill.pill{width:100%}''')
patch('metric','''R.stat .fig{white-space:nowrap}@container(max-width:300px){R.stat .parts{padding:var(--gap-sm)}}''')
patch('hierarchy','''R .root{align-self:end}R .branch:nth-child(2)::before{left:50%}R .branch:last-child::before{right:50%}''')
patch('mindmap','''R::before{content:'';position:absolute;inset:0;background:var(--n-4);clip-path:polygon(16.5% 16.5%,50% 49.8%,83.5% 16.5%,83.5% 16.9%,50.2% 50%,83.5% 83.1%,83.5% 83.5%,50% 50.2%,16.5% 83.5%,16.5% 83.1%,49.8% 50%,16.5% 16.9%);z-index:-1}R::after{content:'';position:absolute;left:16.5%;right:16.5%;top:50%;height:var(--stroke);background:var(--n-4);z-index:-1}R:has(>.branch:nth-child(3):last-child)::before{clip-path:polygon(16.5% 16.5%,50% 49.8%,83.5% 16.5%,83.5% 16.9%,50% 50.2%,16.5% 16.9%)}R:has(>.branch:nth-child(3):last-child)::after{content:none}R:has(>.branch:nth-child(5):last-child)::before{clip-path:polygon(16.5% 16.5%,50% 49.8%,83.5% 16.5%,83.5% 16.9%,50% 50.2%,16.5% 16.9%)}R .branch::before{content:none}''')
for name in ['flowchart','swimlane']:
 patch(name,'''R .node.to-r::after,R .node.to-l::after{top:calc(50% - 5px);height:10px;clip-path:polygon(0 40%,calc(100% - 8px) 40%,calc(100% - 8px) 0,100% 50%,calc(100% - 8px) 100%,calc(100% - 8px) 60%,0 60%)}R .node.to-l::after{transform:rotate(180deg)}R .node.to-d::before,R .node.to-u::before{left:calc(50% - 5px);width:10px;clip-path:polygon(40% 0,60% 0,60% calc(100% - 8px),100% calc(100% - 8px),50% 100%,0 calc(100% - 8px),40% calc(100% - 8px))}R .node.to-u::before{transform:rotate(180deg)}''')
print('Compact atom width, unbroken figures and continuous relationship connectors applied')
# Radar uses numeric style queries, independent of style-attribute whitespace after browser serialization.
import math
rad='R .series{clip-path:none;background:none;border:0}R .series::before{content:"";position:absolute;inset:0;background:color-mix(in srgb,var(--a1) 25%,transparent)}R .series:nth-of-type(2)::before{background:color-mix(in srgb,var(--a2) 20%,transparent)}R .series:nth-of-type(3)::before{background:color-mix(in srgb,var(--a3) 16%,transparent)}R .series:nth-of-type(3)>.name{left:78%;color:var(--a3-7)}'
for n in range(3,9):
 rad+=f'@container style(--n: {n})'+'{'
 coords=[]
 for i in range(n):
  a=-math.pi/2+2*math.pi*i/n;x=50+48*math.cos(a);y=50+48*math.sin(a)
  rad+=f'R .axis:nth-child({i+1})'+'{'+f'left:{x:.2f}%;top:{y:.2f}%;'+'}'
  coords.append(f'calc(50% + {math.cos(a)*50:.5f}% * var(--v{i+1}) / var(--max)) calc(50% + {math.sin(a)*50:.5f}% * var(--v{i+1}) / var(--max))')
 rad+='R .series::before{clip-path:polygon('+','.join(coords)+');}}'
patch('radar',rad)
patch('slope','''R:not(.dumbbell) .pair:last-child:nth-child(n+6) .a{margin-left:var(--type-40)}R:not(.dumbbell) .pair:last-child:nth-child(n+6) .b{margin-right:var(--type-40)}R:not(.dumbbell) .pair:last-child:nth-child(n+6) .a::after{content:'';position:absolute;right:100%;top:50%;width:var(--type-40);border-top:1px dotted var(--n-4)}R:not(.dumbbell) .pair:last-child:nth-child(n+6) .b::after{content:'';position:absolute;left:100%;top:50%;width:var(--type-40);border-top:1px dotted var(--n-4)}R.dumbbell .pair .a{transform:translate(-50%,-10%)}R.dumbbell .pair .b{transform:translate(-50%,110%)}''')
for p in C.glob('elements/*/fixtures/*.html'):
 if p.parent.parent.name in mandatory:continue
 s=p.read_text().replace('TEXT HERE','전사 실행 원칙').replace('TEXT 기획','전사 기획')
 if p.parent.parent.name=='prose':
  s=s.replace('인간이 식물을 경작하는 일은 문명의 토대인 농업의 일부로 되어 있다.','전사 고객 지원 기록을 하나의 업무 시스템에 모았습니다.').replace('식물 경작은 농업 경제학, 원예, 임업으로 나뉜다.','각 팀이 고객의 요청을 빠짐없이 확인하고 해결 상태를 공유합니다.').replace('사람들이 식물을 연구하면서 경제식물학이나 민족식물학이라는 용어가 생겨나기 시작하였다.','운영팀은 고객 상담 기록을 분석해 반복되는 불편을 찾았습니다.').replace('어떠한 사람들은 경제식물학 대신 원예 식물에 초점을 둔다고 여긴다.','개선 과제는 매주 담당자와 완료 일정을 정해 점검합니다.')
 p.write_text(s)
print('Radar whitespace, slope label separation, and business fixture content refined')
# Body and component choices used by the source-backed reassembly are reusable variants.
f=C/'foundation/foundation.css';f.write_text(f.read_text()+'''.slide .page{gap:calc(var(--gap-lg)*.75)}.slide .page:has(>.head.center){padding-left:0;padding-right:0;padding-bottom:0}.slide.cover .title{font-size:var(--type-104)}.slide.cover .lead{font-size:var(--type-32)}.slide.cover .deco{left:0;bottom:0;width:430px;height:286px;border:0;border-top-right-radius:100%;border-bottom-right-radius:0;border-top-left-radius:0;border-bottom-left-radius:0;background:var(--n-1)}.slide.cover .deco::after{content:'';position:absolute;left:920px;top:-434px;width:360px;height:186px;background:var(--n-1);border-bottom-left-radius:100%}\n''')
p=C/'foundation/fixtures/cover.html';p.write_text(p.read_text().replace('<p class="meta">','<div class="deco"></div><p class="meta">'))
patch('image-frame','''R.frame{width:100%;height:100%;max-width:100%;max-height:100%}''')
patch('metric','''R.stats{align-items:flex-start;gap:var(--gap-lg)}R.stats>.stat{aspect-ratio:1;align-self:flex-start;height:auto}R.stat .name{font-size:var(--type-36)}@container(max-width:300px){R.stat .name{font-size:var(--type-24)}}''')
patch('prose','''R.lead{padding:calc(var(--pad)*0);text-align:center}R.lead p{font-size:var(--type-24);line-height:var(--lead-line)}R.quiet{text-align:center}''')
patch('callout','''R{min-height:0;padding:calc(var(--gap-sm)/2)}@container(max-height:100px){R p{font-size:var(--type-24);line-height:var(--label-line)}}''')
patch('list','''R.divided{border:var(--stroke) solid var(--n-4);border-radius:var(--radius);padding:var(--gap-sm);background:var(--n-1);gap:0}R.divided .item{flex:1;width:100%;display:flex;flex-direction:column;justify-content:center;text-align:center;padding:calc(var(--gap-sm)/2);border-bottom:1px dotted var(--n-4)}R.divided .item:last-child{border:0}R.divided .item::before{content:none}R.divided .item>.name{font-size:var(--type-32)}@container(max-width:800px){R.divided .item>.name{font-size:var(--type-24)}}''')
patch('headline','''R.big:not(:has(h2>b)) h2{font-size:var(--type-128)}R.big:has(h2>b) h2{font-size:var(--type-88)}@container(max-width:650px){R.big:not(:has(h2>b)) h2{font-size:var(--type-88)}R.big:has(h2>b) h2{font-size:var(--type-60)}}''')
patch('card','''R.quiet:has(.mark>.seat){border:0;border-radius:0;padding:0;background:var(--n-1)}R.quiet:has(.mark>.seat) .parts{position:relative;isolation:isolate;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:var(--gap-sm)}R.quiet:has(.mark>.seat) .mark{position:absolute;inset:0;width:100%;height:100%;border:0;border-radius:0;z-index:-1}R.quiet:has(.mark>.seat) .mark>.seat{position:absolute;inset:0;width:100%;height:100%;aspect-ratio:auto;border:0;border-radius:0}R.quiet:has(.mark>.seat) .mark>.seat::after{display:none}R.quiet:has(.mark>.seat) .kick{position:absolute;top:14%;font-size:var(--type-18);color:var(--ink)}R.quiet:has(.mark>.seat) .name{font-size:var(--type-44);line-height:var(--lead-line);min-height:0;display:block}R.quiet:has(.mark>.seat) .note{position:absolute;bottom:14%;font-size:var(--type-18);min-height:0}@container(max-width:320px){R.quiet:has(.mark>.seat) .name{font-size:var(--type-28)}}''')
print('Reassembly-compatible reusable foundation and source-derived variants added')
patch('pill','''R.pill.pill{flex:1 1 0;padding:calc(var(--gap-sm)/2) var(--gap-sm)}R .name{font-size:var(--type-26);white-space:nowrap}R.line{background:var(--n-1)}''')
p=C/'elements/pill/fixtures/pill-stack.html';p.write_text(p.read_text().replace('min: 5x3','min: 5x4'))
patch('card','''R.quiet:has(.mark>.seat) .mark>.seat{background:color-mix(in srgb,var(--ink) 85%,var(--page))}R.quiet:has(.mark>.seat) :is(.kick,.name,.note){color:var(--page)}''')
patch('list','''R.divided .item>.name{font-weight:var(--lead-weight)}''')
patch('headline','''R.center:not(.big):not(.on) h2{font-size:var(--type-32);font-weight:var(--lead-weight)}R.center:not(.big):not(.on) h2 b{font-weight:var(--lead-weight)}''')
f=C/'foundation/foundation.css';f.write_text(f.read_text()+'''.slide .body{position:relative;isolation:isolate}.slide .seat.back{background:color-mix(in srgb,var(--ink) 85%,var(--page));color:var(--page)}.slide.cover .deco,.slide.cover .deco::after{background:color-mix(in srgb,var(--ink) 85%,var(--page))}.slide.cover .title b{color:var(--a1-7);font-weight:var(--title-weight)}.slide .top{font-size:var(--type-16)}.slide .top .sec{font-size:var(--type-14)}.slide .top .deck{display:flex;align-items:center;gap:calc(var(--gap-sm)*.75)}.slide .top .deck .icon{width:var(--type-16);height:var(--type-16);color:var(--a1-7)}\n''')
for p in C.glob('elements/*/element.css'):
 s=p.read_text();scope=f'[data-el="nocturne-{p.parent.name}"]';s+=scope+' small{color:inherit;margin-left:0}\n';p.write_text(s)
for p in (C/'elements/tag/fixtures').glob('*.html'):
 s=p.read_text().replace('class="prose" style=','class="prose" data-el="nocturne-prose" style=');s=re.sub(r';\s*font-size:[^;"\n]+','',s);s=re.sub(r';\s*line-height:[^;"\n]+','',s);p.write_text(s)
print('Reassembly overflow, placeholder contrast, running furniture and unit contrast adjusted')
patch('sankey','''R>.branch{flex-direction:row;align-items:center;justify-content:space-between;padding:calc(var(--gap-sm)/2) var(--pad)}@container(max-height:500px){R>.branch{padding:calc(var(--gap-sm)/4) var(--gap-sm)}R>.branch>.name{font-size:var(--type-18)}R>.branch>.fig{font-size:var(--type-18)}}''')
for n in ['sankey-6','sankey-nested']:
 p=C/'elements/sankey/fixtures'/f'{n}.html';p.write_text(p.read_text().replace('min: 8x4','min: 10x5'))
p=C/'kit/css/tokens.css';s=p.read_text().replace('--title-line: 1.12;','--title-line: 1.2;').replace('--figure-line: 1.05;','--figure-line: 1.15;');p.write_text(s)
f=C/'foundation/foundation.css';f.write_text(f.read_text()+'''.slide *::before,.slide *::after{box-sizing:border-box}.slide .top{height:auto;line-height:var(--label-line)}.slide .top .deck{line-height:var(--label-line)}.slide .top .deck .icon{display:flex;align-items:center;justify-content:center}.slide .icon>svg{display:block}.slide.cover .deco{inset:0;width:auto;height:auto;background:none;border-radius:0}.slide.cover .deco::before{content:'';position:absolute;left:0;bottom:0;width:430px;height:286px;background:color-mix(in srgb,var(--ink) 85%,var(--page));border-top-right-radius:100%}.slide.cover .deco::after{left:auto;right:0;top:0;width:360px;height:186px}\n''')
print('Final glyph metrics and decoration bounds normalized')
# Anchor the complete Sankey band to the root; a sibling anchor is not resolvable inside a positioned branch box.
sank='''R>.branch{position:static}R>.branch::before{left:anchor(--nocturne-sankey-source right);right:calc(100% - anchor(var(--nocturne-branch-anchor) left));top:calc(anchor(--nocturne-sankey-source center) - 100cqh);bottom:calc(100% - anchor(var(--nocturne-branch-anchor) bottom));z-index:0}R .source{z-index:2}R>.branch>.branch::before{z-index:0}'''
for i in range(1,7):sank+=f'R>.branch:nth-child({i+1})'+'{'+f'anchor-name:--nocturne-sankey-{i};--nocturne-branch-anchor:--nocturne-sankey-{i};'+'}'
patch('sankey',sank)
rad='''R::before{inset:auto;left:50%;top:50%;width:min(70cqw,70cqh);height:min(70cqw,70cqh);transform:translate(-50%,-50%)}R .series:nth-of-type(n){inset:auto;left:50%;top:50%;width:min(70cqw,70cqh);height:min(70cqw,70cqh);transform:translate(-50%,-50%);clip-path:none;background:none;border:0}R .series:nth-of-type(n)>.name{color:var(--ink);font-size:var(--type-14)}'''
for n in range(3,9):
 rad+=f'@container style(--n: {n})'+'{'
 for i in range(n):
  a=-math.pi/2+2*math.pi*i/n;rad+=f'R .axis:nth-child({i+1})'+'{'+f'left:calc(50% + {math.cos(a):.5f}*min(44cqw,44cqh));top:calc(50% + {math.sin(a):.5f}*min(44cqw,44cqh));'+'}'
 rad+='}'
patch('radar',rad)
print('Sankey root anchor geometry and circular radar contrast finalized')
sank='''R{--nocturne-branch-count:3}R>.branch{--nocturne-band-pad:calc(var(--gap-sm)/2);--nocturne-band-height:calc((100cqh - var(--gap-sm)*(var(--nocturne-branch-count) - 1) - (var(--nocturne-band-pad)*2 + 2px)*var(--nocturne-branch-count))*var(--v)/100 + var(--nocturne-band-pad)*2 + 2px)}R>.branch:has(>.branch){--nocturne-band-pad:var(--gap-sm)}R>.branch::before{right:anchor(var(--nocturne-branch-anchor) left);bottom:anchor(var(--nocturne-branch-anchor) bottom);top:calc(anchor(--nocturne-sankey-source top) + anchor(var(--nocturne-branch-anchor) top)*.3 - 100cqh);clip-path:polygon(0 100cqh,100% calc(100% - var(--nocturne-band-height)),100% 100%,0 calc(100cqh + var(--nocturne-band-height)*.3))}R>.branch:has(>.branch)::after{content:'';position:absolute;left:calc(anchor(var(--nocturne-branch-anchor) left) + var(--gap-sm));top:calc(anchor(var(--nocturne-branch-anchor) top) + var(--gap-sm));bottom:calc(anchor(var(--nocturne-branch-anchor) bottom) + var(--gap-sm));width:calc((68cqw - var(--gap-sm)*2 - var(--pad))*.3);border:1px solid var(--n-4);border-radius:var(--radius-sm)}R>.branch:has(>.branch)>.name,R>.branch:has(>.branch)>.fig{text-align:center}R>.branch>.branch{height:calc(var(--type-20) + var(--v)*.4px)}@container(max-height:500px){R>.branch:not(:has(>.branch)){--nocturne-band-pad:calc(var(--gap-sm)/4)}}'''
for count in range(2,7):sank+=f'R:has(>.branch:nth-child({count+1}):last-child)'+'{'+f'--nocturne-branch-count:{count};'+'}'
patch('sankey',sank)
print('Sankey bands now use exact root anchor insets and ordered source ports')
patch('sankey','''R>.branch>.branch::before{width:calc(var(--pad) + var(--gap-lg));z-index:0}R>.branch:has(>.branch)::after{background:var(--n-1);z-index:1}R>.branch:has(>.branch)>.name,R>.branch:has(>.branch)>.fig{position:relative;z-index:2}''')
patch('chart-line','''R{--nocturne-line-plot:calc(100cqh - var(--type-32) - var(--type-48))}R .pt{--nocturne-line-height:calc(var(--v)/var(--max)*var(--nocturne-line-plot))}R .pt::before{top:calc(anchor(var(--nocturne-prev) bottom) - var(--nocturne-line-plot));bottom:calc(var(--pad) + var(--type-32) + var(--stroke));background:var(--a1);clip-path:polygon(0 calc(var(--nocturne-line-plot) - 1px),100% calc(100% - var(--nocturne-line-height) - 1px),100% calc(100% - var(--nocturne-line-height) + 1px),0 calc(var(--nocturne-line-plot) + 1px))}R .pt::after{content:none}''')
print('Nested Sankey connections and equal-valued line intervals completed')
