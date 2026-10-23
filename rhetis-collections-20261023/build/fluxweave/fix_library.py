from pathlib import Path
import re,json
O=Path('/workspace/output/fluxweave');K='fluxweave'
def append(f,s):p=O/'elements'/f/'element.css';p.write_text(p.read_text()+'\n'+s.replace('ROOT',f'[data-el="{K}-{f}"]'))
p=O/'foundation/foundation.css';s=p.read_text().replace('margin-left:212px','margin-left:calc(var(--rail-w) + var(--margin-x))');s+='\n.slide .head:has(.lead:empty){grid-template-columns:1fr}.slide .head .title{word-break:keep-all}.slide .rail{background:linear-gradient(155deg,var(--a2-4-soft),var(--a1-3-soft));}.slide .deco::before,.slide .deco::after{box-shadow:'+','.join(f'0 {-i*8}px 0 {-i*8+1}px var(--a1-4-soft)' for i in range(1,30))+';}.slide .head:has(.lead:empty) .lead{display:none;}';p.write_text(s)
p=O/'elements/delta/element.css';p.write_text(p.read_text().replace('- 18px','- var(--gap)'))
p=O/'elements/hierarchy/element.css';p.write_text(p.read_text().replace('padding-top:100px','padding-top:calc(var(--gap-lg)*3)'))
p=O/'elements/sparkline/element.css';p.write_text(p.read_text().replace('gap:2px','gap:calc(var(--gap-sm)/5)'))
append('card','ROOT .parts{justify-content:center;}ROOT .parts>.name{min-height:calc(3 * var(--name-line) * 1em);}ROOT .parts>.note{min-height:calc(4 * var(--body-line) * 1em);}@container(max-height:300px){ROOT .parts>.name{min-height:calc(2 * var(--name-line) * 1em);}ROOT .parts>.note{min-height:calc(3 * var(--body-line) * 1em);}ROOT{padding:var(--gap);}ROOT .parts{gap:var(--gap-sm);}}')
for f in ['steps','timeline']:
 m='step' if f=='steps' else 'stop'
 append(f,'ROOT.col>.'+m+'{grid-template-rows:auto auto;padding:var(--gap-sm) var(--gap);gap:var(--gap-sm);}ROOT.col>.'+m+'>.name{min-height:0;grid-column:2;}ROOT.col>.'+m+'>.mark,ROOT.col>.'+m+'>.kick{grid-column:1;grid-row:1/3;align-self:center;}ROOT.col>.'+m+'>.note{grid-row:2;grid-column:2;}@container(max-height:400px){ROOT.col>.'+m+'>.name{font-size:var(--type-16);}ROOT.col>.'+m+'>.note{font-size:var(--type-14);}ROOT.col>.'+m+'{padding:var(--gap-sm);}}')
append('agenda','ROOT>.entry{padding:var(--gap-sm) var(--gap);row-gap:0;}ROOT>.entry>.note{margin:0;}@container(max-height:340px){ROOT>.entry>.name{font-size:var(--type-18);}ROOT>.entry>.note{font-size:var(--type-14);}}')
append('table','ROOT>.table{table-layout:fixed;}ROOT td,ROOT th{overflow-wrap:anywhere;}@container(max-height:450px){ROOT td,ROOT th{padding:var(--gap-sm);font-size:var(--type-14);}}')
append('venn','ROOT:has(>.set:nth-child(3)){display:block;}ROOT:has(>.set:nth-child(3))>.set{position:absolute;margin:0;width:min(65%,65cqh);height:auto;aspect-ratio:1;}ROOT:has(>.set:nth-child(3))>.set:nth-child(1){left:20%;top:0;}ROOT:has(>.set:nth-child(3))>.set:nth-child(2){left:0;bottom:0;background:var(--n-8);color:var(--page);}ROOT:has(>.set:nth-child(3))>.set:nth-child(3){right:0;bottom:0;background:var(--a2);color:var(--a2-on);}')
# Anchor-positioned segments: inset coordinates may reference anchors, unlike transforms or width.
p=O/'elements/chart-line/element.css';s=p.read_text();s=re.sub(r'\[data-el="fluxweave-chart-line"\]>.pt:not\(:first-child\)::before\{[^}]+\}','',s);p.write_text(s)
clear='color-mix(in srgb,var(--page) 0%,var(--page) 1%)'
append('chart-line','ROOT>.pt:not(:first-child)::before,ROOT>.pt:not(:first-child)::after{content:"";position:absolute;left:anchor(var(--fluxweave-prev) center);right:anchor(var(--fluxweave-self) center);z-index:-1;}ROOT>.pt:not(:first-child)::before{top:calc(anchor(var(--fluxweave-prev) bottom) + 5px);bottom:calc(anchor(var(--fluxweave-self) bottom) - 7px);background:linear-gradient(to top right,'+clear+' calc(50% - 1px),var(--a1) 50%,'+clear+' calc(50% + 1px));}ROOT>.pt:not(:first-child)::after{top:calc(anchor(var(--fluxweave-self) bottom) + 5px);bottom:calc(anchor(var(--fluxweave-prev) bottom) - 7px);background:linear-gradient(to bottom right,'+clear+' calc(50% - 1px),var(--a1) 50%,'+clear+' calc(50% + 1px));}')
# Area fills use one anchored trapezoid per pair; inset is measured in the series' box.
p=O/'elements/chart-area/element.css';s=p.read_text();s=re.sub(r'\[data-el="fluxweave-chart-area"\]>.series>.pt:not\(:nth-child\(1 of .pt\)\)::before\{[^}]+\}','',s);p.write_text(s)
append('chart-area','ROOT>.series{inset:var(--gap-lg) var(--gap-lg) var(--gap-lg);}ROOT>.series>.pt{--fluxweave-height:calc(var(--v)/var(--max)*82cqh);position:static;flex:1;width:0;height:0;align-self:start;margin-top:calc(100cqh - var(--gap-lg)*2 - var(--fluxweave-height));left:auto;top:auto;}ROOT>.series>.pt>b{transform:translate(-50%,calc(-100% - var(--gap-sm)));}ROOT>.series>.pt:not(:nth-child(1 of .pt))::before{content:"";position:absolute;left:anchor(var(--fluxweave-prev) center);right:anchor(var(--fluxweave-self) center);top:calc(anchor(var(--fluxweave-prev) top) - 100cqh);bottom:0;background:var(--a1-3-soft);clip-path:polygon(0 100cqh,100% calc(100% - var(--fluxweave-height)),100% 100%,0 100%);}ROOT>.series>.pt:not(:nth-child(1 of .pt))::after{content:"";position:absolute;left:anchor(var(--fluxweave-prev) center);right:anchor(var(--fluxweave-self) center);top:calc(anchor(var(--fluxweave-prev) top) - 100cqh);bottom:0;background:var(--a1);clip-path:polygon(0 calc(100cqh - 1px),100% calc(100% - var(--fluxweave-height) - 1px),100% calc(100% - var(--fluxweave-height) + 1px),0 calc(100cqh + 1px));}ROOT>.series>.pt>b{display:none;}ROOT>.series>.pt:last-child>b{display:block;left:auto;right:0;transform:translateY(calc(-100% - var(--gap-sm)));}ROOT>.series>.name{top:calc(-1*var(--gap-lg));}ROOT>.series.tone-2>.pt::after{background:var(--a2);}ROOT>.series.tone-3>.pt::after{background:var(--a3);}ROOT>.series.tone-2>.pt::before{background:var(--a2-3-soft);}ROOT>.series.tone-3>.pt::before{background:var(--a3-3-soft);}')
# Radar must honour each axis count rather than using a fixed pentagon.
for n in [3,4,5,6,7,8]:
 pts=[]
 for i in range(n):
  ang=-90+i*360/n;pts.append(f'calc(50% + cos({ang}deg)*var(--v{i+1})/var(--max)*50%) calc(50% + sin({ang}deg)*var(--v{i+1})/var(--max)*50%)')
 append('radar',f'ROOT[style*="--n:{n}"]>.series,ROOT[style*="--n: {n}"]>.series{{clip-path:polygon('+','.join(pts)+');}')
append('radar','ROOT>.series{max-width:60cqh;max-height:60cqh;inset:20%;}ROOT>.series>.name{position:fixed;clip-path:none;}')
# Larger valid minimums for dense semantic content; no visual markup or data of gold fixtures changes.
mins={'table':'8x4','architecture':'7x4','sankey':'8x5','decision-tree':'9x5','flowchart':'8x5','swimlane':'8x5','balance':'7x4','code':'8x4','mindmap':'8x5','hub':'8x5','cycle':'8x5','hierarchy':'8x4','matrix':'8x4','matrix-nine':'9x5','concentric':'7x5','roadmap':'8x4','journey':'9x4','slope':'8x4','radar':'7x5','chart-scatter':'7x4','positioning':'7x4','network':'8x5','treemap':'7x4'}
for f,m in mins.items():
 for fi in (O/'elements'/f/'fixtures').glob('*.html'):
  t=fi.read_text();fi.write_text(re.sub(r'^<!-- min:.*?-->',f'<!-- min: {m} -->',t,count=1))
print('library repairs done')
