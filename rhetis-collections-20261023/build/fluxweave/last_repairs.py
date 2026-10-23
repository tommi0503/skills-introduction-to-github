from pathlib import Path
O=Path('/workspace/output/fluxweave')
def ap(f,s):p=O/'elements'/f/'element.css';p.write_text(p.read_text()+s.replace('ROOT',f'[data-el="fluxweave-{f}"]'))
for i in range(1,5):ap('matrix',f'ROOT.swot>.cell:nth-child({i} of .cell){{grid-column:{1+(i-1)%2};grid-row:{1+(i-1)//2};}}')
ap('person','''
ROOT.person>.list,ROOT.people>.person>.list{width:90%;}
ROOT .seat{width:min(65%,50cqh);height:min(65cqw,50cqh);max-height:50%;flex-shrink:0;}
''')
ap('tag','\nROOT{container-type:normal;width:max-content;max-width:100%;height:auto;white-space:nowrap;}')
ap('pill','\nROOT{container-type:normal;min-height:60px;height:auto;}')
p=O/'elements/pill/fixtures/pill-stack.html';p.write_text(p.read_text().replace('min: 4x3','min: 5x4'))
clear='color-mix(in srgb,var(--page) 0%,var(--page) 1%)'
ap('sparkline','''
ROOT{--fluxweave-spark-color:var(--a1);display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);align-items:start;gap:0;padding:var(--gap-sm);isolation:isolate;}
ROOT.up{--fluxweave-spark-color:var(--good);}ROOT.down{--fluxweave-spark-color:var(--bad);}
ROOT>span,ROOT.up>span,ROOT.down>span{position:static;align-self:start;justify-self:center;flex:none;width:0;height:calc(100% - var(--v)/var(--max)*(100% - 8px));background:none;border-radius:0;}
ROOT>span:not(:first-child)::before,ROOT>span:not(:first-child)::after{content:"";position:absolute;left:anchor(var(--fluxweave-prev) center);right:anchor(var(--fluxweave-self) center);z-index:-1;}
ROOT>span:not(:first-child)::before{top:calc(anchor(var(--fluxweave-prev) bottom) - 1px);bottom:calc(anchor(var(--fluxweave-self) bottom) - 1px);background:linear-gradient(to top right,CLEAR calc(50% - 1px),var(--fluxweave-spark-color) 50%,CLEAR calc(50% + 1px));}
ROOT>span:not(:first-child)::after{top:calc(anchor(var(--fluxweave-self) bottom) - 1px);bottom:calc(anchor(var(--fluxweave-prev) bottom) - 1px);background:linear-gradient(to bottom right,CLEAR calc(50% - 1px),var(--fluxweave-spark-color) 50%,CLEAR calc(50% + 1px));}
ROOT.bars{display:flex;align-items:end;gap:calc(var(--gap-sm)/5);}
ROOT.bars>span,ROOT.bars.up>span,ROOT.bars.down>span{flex:1;align-self:auto;justify-self:auto;width:auto;height:calc(var(--v)/var(--max)*90%);background:var(--fluxweave-spark-color);border-radius:var(--radius-sm) var(--radius-sm) 0 0;}
ROOT.bars>span::before,ROOT.bars>span::after{content:none;}
'''.replace('CLEAR',clear))
for i in range(1,25):ap('sparkline',f'ROOT>span:nth-child({i}){{--fluxweave-self:--fluxweave-spark-{i};--fluxweave-prev:--fluxweave-spark-{i-1};anchor-name:var(--fluxweave-self);}}')
print('actual containment and implicit-grid causes repaired; default spark is line')
