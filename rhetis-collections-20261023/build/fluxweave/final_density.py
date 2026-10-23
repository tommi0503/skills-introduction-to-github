from pathlib import Path
import re
O=Path('/workspace/output/fluxweave')
mins={'architecture':'8x5','bullet':'7x5','gauge':'6x4','delta':'5x3','list':'7x5','metric':'8x3','prose':'7x5','pyramid':'7x4','sankey':'9x6','steps':'8x5','tag':'7x3','treemap':'10x6','waffle':'7x4','chart-area':'6x4'}
for f,m in mins.items():
 for p in (O/'elements'/f/'fixtures').glob('*.html'):
  p.write_text(re.sub(r'^<!-- min:.*?-->',f'<!-- min: {m} -->',p.read_text(),count=1))
def ap(f,s):p=O/'elements'/f/'element.css';p.write_text(p.read_text()+s.replace('ROOT',f'[data-el="fluxweave-{f}"]'))
ap('architecture','\nROOT>.layer{padding:var(--gap-sm);gap:var(--gap-sm);}ROOT .chip{font-size:var(--type-16);}')
ap('list','\nROOT{gap:var(--gap-sm);}ROOT.divided>.item{padding-bottom:var(--gap-sm);}ROOT>.item>.name{font-size:var(--type-20);}ROOT>.item>.note{margin-top:calc(var(--gap-sm)/2);font-size:var(--type-16);}')
ap('delta','\nROOT .from,ROOT .to{font-size:var(--type-36);}@container(max-width:600px){ROOT .from,ROOT .to{font-size:var(--type-28);}}')
ap('pyramid','\nROOT>.level{flex-direction:column;gap:var(--gap-sm);padding:var(--gap-sm);}ROOT .level .name{font-size:var(--type-18);}ROOT .level .note{font-size:var(--type-14);}')
ap('treemap','\nROOT .tile{padding:var(--gap-sm);gap:var(--gap-sm);}ROOT .tile .fig{font-size:var(--type-18);}ROOT .tile .name{font-size:var(--type-16);}ROOT>.branch:only-child{flex-direction:row;}ROOT>.branch:only-child>.name{left:0;}@container(max-width:1000px){ROOT .tile{padding:calc(var(--gap-sm)/2);gap:calc(var(--gap-sm)/2);}ROOT .tile .fig{font-size:var(--type-16);}ROOT .tile .name{font-size:var(--type-14);}}')
ap('sankey','\nROOT{gap:var(--gap);align-content:stretch;}ROOT>.branch{padding:var(--gap-sm);gap:var(--gap-sm);}ROOT .branch>.branch{padding:calc(var(--gap-sm)/2);gap:var(--gap-sm);}ROOT .branch .name{font-size:var(--type-16);}ROOT .fig{font-size:var(--type-20);}')
ap('steps','\nROOT.col>.step{padding:var(--gap-sm);}ROOT.col>.step>.mark{font-size:var(--type-28);}ROOT.col>.step>.note{font-size:var(--type-14);}ROOT.col>.step>.name{font-size:var(--type-18);}')
ap('matrix','\nROOT.swot>.cell{padding:var(--gap-sm);gap:var(--gap-sm);}ROOT.swot .list{gap:var(--gap-sm);}ROOT.swot .list .item>.name{font-size:var(--type-16);}ROOT.swot .kick{font-size:var(--type-14);}')
for p in (O/'elements/tag/fixtures').glob('*.html'):
 s=p.read_text();s=s.replace('class="prose" style="grid-column:1 / span 8; grid-row:2 / span 2; font-size:var(--type-20); line-height:1.8"','class="prose" data-el="fluxweave-prose" style="grid-column:1 / span 12; grid-row:1 / span 6"');p.write_text(s)
# Default reference palette semantic green is too light for code text; retain its meaning with a deep neutral text tone.
p=O/'elements/code/element.css';p.write_text(p.read_text().replace('color:var(--good)','color:var(--a1-7)'))
print('density final')
