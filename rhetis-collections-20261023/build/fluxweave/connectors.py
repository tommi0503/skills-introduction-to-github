from pathlib import Path
O=Path('/workspace/output/fluxweave')
for f in ['flowchart','swimlane']:
 r=f'[data-el="fluxweave-{f}"]';s='''
ROOT>.node.to-r::after,ROOT>.node.to-l::after{content:"";position:absolute;left:100%;right:auto;top:calc(50% - 6px);bottom:auto;width:var(--gap-lg);height:12px;border:0;background:var(--a1);clip-path:polygon(0 40%,75% 40%,75% 0,100% 50%,75% 100%,75% 60%,0 60%);transform:none;}
ROOT>.node.to-l::after{left:auto;right:100%;transform:rotate(180deg);}
ROOT>.node.to-d::before,ROOT>.node.to-u::before{content:"";position:absolute;left:calc(50% - 6px);right:auto;top:100%;bottom:auto;width:12px;height:var(--gap-lg);border:0;background:var(--a1);clip-path:polygon(40% 0,60% 0,60% 75%,100% 75%,50% 100%,0 75%,40% 75%);transform:none;}
ROOT>.node.to-u::before{top:auto;bottom:100%;transform:rotate(180deg);}
@container(max-width:600px){ROOT>.node.to-r::after,ROOT>.node.to-l::after{width:var(--gap);}ROOT>.node.to-d::before,ROOT>.node.to-u::before{height:var(--gap);}}
'''.replace('ROOT',r)
 p=O/'elements'/f/'element.css';p.write_text(p.read_text()+s)
f='slope';r='[data-el="fluxweave-slope"]';s='''
ROOT.dumbbell{display:flex;flex-direction:column;justify-content:center;gap:var(--gap);padding:var(--gap-lg) var(--gap) var(--gap);}
ROOT.dumbbell>.pair{position:relative;inset:auto;flex:1;min-height:0;max-height:100px;margin-left:22%;margin-right:8%;}
ROOT.dumbbell>.pair>.name{right:calc(100% + var(--gap));top:50%;bottom:auto;transform:translateY(-50%);font-size:var(--type-16);white-space:normal;width:25%;text-align:right;}
ROOT.dumbbell>.pair>.a,ROOT.dumbbell>.pair>.b{position:absolute;left:calc(var(--a)/var(--max)*90%);top:50%;bottom:auto;transform:translate(-50%,-140%);font-size:var(--type-18);line-height:var(--body-line);}
ROOT.dumbbell>.pair>.b{left:calc(var(--b)/var(--max)*90%);}
ROOT.dumbbell>.pair>.a::after,ROOT.dumbbell>.pair>.b::after{content:"";position:absolute;width:10px;height:10px;left:calc(50% - 5px);top:calc(100% + var(--gap-sm)*.4);border-radius:50%;background:var(--n-6);}
ROOT.dumbbell>.pair>.b::after{background:var(--a1);}
ROOT.dumbbell>.pair::after{content:"";position:absolute;left:calc(min(var(--a),var(--b))/var(--max)*90%);right:auto;top:50%;bottom:auto;width:calc(abs(var(--b) - var(--a))/var(--max)*90%);height:3px;background:var(--n-4);rotate:none;transform:none;}
ROOT.dumbbell>.pair.on::after{background:var(--a1);}
@container(max-width:650px){ROOT.dumbbell>.pair>.name{font-size:var(--type-14);}ROOT.dumbbell>.pair>.a,ROOT.dumbbell>.pair>.b{font-size:var(--type-14);}}
'''.replace('ROOT',r)
p=O/'elements'/f/'element.css';p.write_text(p.read_text()+s)
print('4-way connectors + dumbbell done')
