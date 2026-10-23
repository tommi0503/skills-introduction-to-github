from pathlib import Path
import json,re
C=Path('/workspace/output/cyanloop')
def append(n,s):
 p=C/'elements'/n/'element.css';p.write_text(p.read_text()+'\n'+s)
s='''
.spark[data-el="cyanloop-sparkline"]:not(.bars)>span{position:relative;background:none;border-radius:0;}
.spark[data-el="cyanloop-sparkline"]:not(.bars)>span::before{content:'';position:absolute;left:50%;top:0;width:4px;height:4px;border-radius:50%;background:var(--a1-7);transform:translate(-50%,-50%);}
.spark[data-el="cyanloop-sparkline"]:not(.bars)>span:not(:last-child)::after{content:'';position:absolute;left:50%;top:0;height:2px;background:var(--a1-7);width:hypot(calc((100cqw - var(--gap-sm)) / var(--cyanloop-spark-n)),calc((var(--v) - var(--cyanloop-spark-next)) / var(--max) * (100cqh - var(--gap-sm))));transform:rotate(atan2(calc((var(--v) - var(--cyanloop-spark-next)) / var(--max) * (100cqh - var(--gap-sm))),calc((100cqw - var(--gap-sm)) / var(--cyanloop-spark-n))));transform-origin:left center;}
.spark[data-el="cyanloop-sparkline"].up:not(.bars)>span::before,.spark[data-el="cyanloop-sparkline"].up:not(.bars)>span::after{background:var(--good);}
.spark[data-el="cyanloop-sparkline"].down:not(.bars)>span::before,.spark[data-el="cyanloop-sparkline"].down:not(.bars)>span::after{background:var(--bad);}
'''
for n in range(2,49):s+=f'.spark[data-el="cyanloop-sparkline"]:has(>span:nth-child({n}):last-child){{--cyanloop-spark-n:{n};}}\n'
for v in range(201):s+=f'.spark[data-el="cyanloop-sparkline"]>span:has(+span[style="--v:{v}"]){{--cyanloop-spark-next:{v};}}\n'
append('sparkline',s)
p=C/'elements/sparkline/element.json';j=json.loads(p.read_text());j['tokenDefaults']={'--cyanloop-spark-n':'12','--cyanloop-spark-next':'0'};p.write_text(json.dumps(j,indent=2))
append('slope','''
.slope[data-el="cyanloop-slope"].dumbbell .pair{min-height:44px;}
.slope[data-el="cyanloop-slope"].dumbbell .pair .name{left:0;top:50%;transform:translateY(-50%);width:26%;padding:0;font-size:var(--type-14);}
.slope[data-el="cyanloop-slope"].dumbbell .pair::before{left:calc(30% + min(var(--a),var(--b)) / var(--max) * 65%);right:auto;top:50%;width:calc(abs(var(--b) - var(--a)) / var(--max) * 65%);height:2px;transform:none;background:var(--n-5);}
.slope[data-el="cyanloop-slope"].dumbbell .pair .a,.slope[data-el="cyanloop-slope"].dumbbell .pair .b{position:absolute;left:calc(30% + var(--a) / var(--max) * 65%);top:calc(50% - var(--gap));transform:translateX(-50%);background:none;font-size:var(--type-14);padding:0;}
.slope[data-el="cyanloop-slope"].dumbbell .pair .b{left:calc(30% + var(--b) / var(--max) * 65%);top:calc(50% + var(--gap-sm));}
.slope[data-el="cyanloop-slope"].dumbbell .pair .a::before,.slope[data-el="cyanloop-slope"].dumbbell .pair .b::before{content:'';position:absolute;width:10px;height:10px;left:calc(50% - 5px);top:calc(var(--gap) - 5px);border-radius:50%;border:2px solid var(--a1-7);background:var(--page);}
.slope[data-el="cyanloop-slope"].dumbbell .pair .b::before{top:calc(0px - var(--gap-sm) - 5px);background:var(--a1-7);}
@container(max-height:400px){.slope[data-el="cyanloop-slope"].dumbbell{gap:0;}.slope[data-el="cyanloop-slope"].dumbbell .pair{min-height:38px;}.slope[data-el="cyanloop-slope"].dumbbell .pair .a,.slope[data-el="cyanloop-slope"].dumbbell .pair .b{font-size:var(--type-12);}}
''')
append('timeline','''
.track[data-el="cyanloop-timeline"].alt{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);grid-template-rows:minmax(0,1fr) minmax(0,1fr);align-items:stretch;column-gap:var(--gap-sm);row-gap:var(--gap-lg);}
.track[data-el="cyanloop-timeline"].alt .stop{transform:none;justify-content:center;padding:var(--gap-sm);gap:var(--gap-sm);}
.track[data-el="cyanloop-timeline"].alt .stop:nth-child(odd){grid-row:1;border-top:0;border-bottom:var(--stroke) solid var(--a1);}
.track[data-el="cyanloop-timeline"].alt .stop:nth-child(even){grid-row:2;}
.track[data-el="cyanloop-timeline"].alt .stop:nth-child(odd)::before{top:auto;bottom:-27px;}
.track[data-el="cyanloop-timeline"].alt .stop:nth-child(even)::before{top:-27px;}
.track[data-el="cyanloop-timeline"].alt .stop .name{font-size:var(--type-18);}
.track[data-el="cyanloop-timeline"].alt .stop .note{font-size:var(--type-14);}
@container(max-height:350px){.track[data-el="cyanloop-timeline"].alt .stop .name{font-size:var(--type-16);}.track[data-el="cyanloop-timeline"].alt .stop .note{font-size:var(--type-12);}.track[data-el="cyanloop-timeline"].alt .stop{gap:calc(var(--gap-sm)/2);}}
''')
for folder,root in [('flowchart','flowchart'),('swimlane','swimlane')]:
 s=''
 for direction,rule,angle in [('r','left:calc(100% + var(--gap) - 8px);top:calc(50% - 4px);',0),('l','right:calc(100% + var(--gap) - 8px);top:calc(50% - 4px);',180),('d','top:calc(100% + var(--gap) - 8px);left:calc(50% - 4px);',90),('u','bottom:calc(100% + var(--gap) - 8px);left:calc(50% - 4px);',270)]:
  s+=f'.{root}[data-el="cyanloop-{folder}"] .to-{direction}::before{{content:"";position:absolute;width:8px;height:8px;background:var(--a1);clip-path:polygon(0 0,100% 50%,0 100%);transform:rotate({angle}deg);{rule}}}\n'
 append(folder,s)
# Dotted leader lines beneath the leadership circles.
s='''\n.hub[data-el="cyanloop-hub"].on .spoke::before{content:'';display:block;position:absolute;left:50%;right:auto;top:50%;width:500px;height:0;border-top:1px dotted var(--n-5);background:none;transform-origin:left center;z-index:-1;}\n'''
for i,a in enumerate([14.5,42.3,75,105,137.7,165.5],2):s+=f'.hub[data-el="cyanloop-hub"].on .spoke:nth-child({i})::before{{transform:rotate({a}deg);}}\n'
append('hub',s)
