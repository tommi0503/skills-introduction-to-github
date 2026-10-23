from pathlib import Path
import json,re,shutil
R=Path('/workspace/work/deliverables/diecut');C=R/'collection/diecut';REF=Path('/workspace/work/reference')
tax=json.load(open(REF/'contract/taxonomy.json'));byid={c['id']:c for c in tax['contracts']}
def rt(n):
 j=json.load(open(C/'elements'/n/'element.json'));return ':is('+','.join('.'+r+'[data-el="diecut-'+n+'"]'for r in byid[j['contract']]['roots'])+')'
def add(n,s):
 p=C/'elements'/n/'element.css';p.write_text(p.read_text()+'\n/* Final integrated review. */\n'+s.replace('R',rt(n)))
for d in (C/'elements').iterdir():add(d.name,'R small{color:inherit;margin-left:0}R .icon{display:flex;align-items:center;justify-content:center;font-size:var(--type-20);line-height:var(--label-line)}')
add('card','''R .fig{white-space:nowrap}R.quiet:has(.mark):has(.fig){border-radius:999px 999px 0 0;background:var(--n-1)}R.quiet:has(.mark):has(.fig) .mark{background:none}R.quiet:has(.mark):has(.fig) .fig{font-size:var(--type-56);font-weight:var(--weight-body)}R.quiet:has(.mark):has(.fig) .name{font-size:var(--type-22)}@container(max-width:190px){R{padding:var(--gap-sm)}R .fig{font-size:var(--type-24)}R .name{font-size:var(--type-16)}}''')
add('headline','R.big h2{font-weight:var(--weight-body)}')
add('chart-area','R>.series>.pt{margin-top:calc(var(--diecut-plot) + var(--gap-lg) - var(--v)/var(--max)*var(--diecut-plot))}')
add('chart-bar','''R:not(.h)>.bar b{bottom:calc(var(--v)/var(--max)*88% - var(--pad));color:var(--page)}R:not(.h)>.bar.on b{color:var(--a1-on)}@container(max-height:250px){R:not(.h)>.bar b{font-size:var(--type-14);bottom:calc(var(--v)/var(--max)*88% - var(--gap))}}''')
add('radar','''R>.axis{z-index:3}R>.axis .name{background:var(--page);padding:0 var(--gap-sm)}R>.series>.name{background:var(--page)}''')
for i in range(1,9):add('radar',f'R>.axis:nth-child({i}){{--diecut-angle:calc(-90deg + ({i} - 1) * 360deg / var(--n))}}')
add('slope','''R>.pair.on:before{height:auto;background:linear-gradient(to bottom right,transparent calc(50% - 1.5px),var(--a1) calc(50% - 1px),var(--a1) calc(50% + 1px),transparent calc(50% + 1.5px))}R>.pair.on:after{height:auto;background:linear-gradient(to top right,transparent calc(50% - 1.5px),var(--a1) calc(50% - 1px),var(--a1) calc(50% + 1px),transparent calc(50% + 1.5px))}R.dumbbell>.pair.on:before{height:2px;background:var(--a1)}''')
add('sparkline','''R:not(.bars)>span{margin:0;height:calc((1 - var(--v)/var(--max))*(100cqh - var(--gap)));width:100%;background:none;max-height:none;anchor-name:var(--diecut-self)}R:not(.bars)>span:before{top:anchor(var(--diecut-prev) bottom);bottom:anchor(var(--diecut-self) bottom)}R:not(.bars)>span:after{top:anchor(var(--diecut-self) bottom);bottom:anchor(var(--diecut-prev) bottom)}''')
for n,m in [('cycle','node'),('hub','spoke')]:
 add(n,f'R>.{m}:nth-of-type(6):before{{width:hypot(33cqw,33cqh);transform:rotate(atan2(-33cqh,33cqw))}}R>.{m}:nth-of-type(7):before{{width:hypot(33cqw,33cqh);transform:rotate(atan2(33cqh,-33cqw))}}R>.{m} .name{{overflow-wrap:normal;word-break:keep-all}}')
add('steps','''R>.step{padding:var(--gap-sm);gap:var(--gap);justify-content:center}R .mark{height:48px;min-height:48px;width:max-content;min-width:48px;max-width:100%;padding:var(--gap-sm);white-space:nowrap;font-size:var(--type-22)}R .name{min-height:3.75em;display:flex;align-items:center;justify-content:center;text-align:center}R .note{min-height:6em}R:has(>.step:nth-child(5)) .name{font-size:var(--type-18)}R:has(>.step:nth-child(5)) .note{font-size:var(--type-14)}R.col .name,R.col .note{min-height:0;text-align:left;justify-content:flex-start}''')
add('agenda','''@container(max-width:600px){R>.entry{padding:var(--gap-sm);gap:calc(var(--gap-sm)/2)}R .name{font-size:var(--type-16)}R .note{font-size:var(--type-14)}R .mark{font-size:var(--type-28);min-width:40px}}R:has(>.entry:nth-child(10))>.entry{border-top:0;gap:var(--gap)}R:has(>.entry:nth-child(10)) .mark{position:relative;width:100%;font-size:var(--type-56);padding-bottom:var(--gap-lg);border-bottom:var(--stroke) solid var(--ink);font-weight:var(--weight-body)}R:has(>.entry:nth-child(10)) .mark:after{content:'';position:absolute;width:14px;height:14px;border-radius:999px;background:var(--ink);bottom:-7px;left:calc(50% - 7px)}R:has(>.entry:nth-child(10)) .name{font-size:var(--type-14)}''')
add('concentric','''R>.ring:nth-child(3){inset:30%}R>.ring:nth-child(4){inset:41%;padding:var(--gap-sm);justify-content:center}R>.ring:nth-child(4) .name{font-size:var(--type-14)}R>.ring:nth-child(4) .fig{font-size:var(--type-22)}''')
add('prose','''@container(max-height:300px){R.cols{font-size:var(--type-16);column-gap:var(--gap)}}''')
add('person','''R.person>.seat{height:40%;width:auto;max-width:75%;max-height:40%;aspect-ratio:1;flex:0 0 40%}R.person>.list{flex:0 0 auto;height:auto;container-type:normal;padding:var(--gap-sm);gap:var(--gap-sm)}R.person>.list .name{font-size:var(--type-16)}@container(max-height:350px){R.person{gap:var(--gap-sm);padding:var(--gap-sm)}R.person>.seat{height:30%;max-height:30%;flex-basis:30%}R.person>.list .name{font-size:var(--type-14)}}''')
add('logo-group','''R{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));grid-auto-rows:minmax(0,1fr);gap:var(--gap);padding:var(--gap)}R:has(>.seat:nth-child(8)){grid-template-columns:repeat(4,minmax(0,1fr))}R>.seat{width:100%;height:100%;max-height:100%;aspect-ratio:auto}''')
add('legend','''R{gap:var(--gap-sm);padding:var(--gap-sm)}R .key{font-size:var(--type-14)}R .key:before{width:12px;height:12px}''')
p=C/'elements/legend/fixtures/stress-long.html';p.write_text(p.read_text().replace('min: 4x1','min: 6x2'))
add('timeline','''R.col>.stop{padding:var(--gap-sm) var(--gap-lg);gap:calc(var(--gap-sm)/2)}R.col>.stop .name{font-size:var(--type-18)}R.col>.stop .note{font-size:var(--type-14)}''')
add('image-frame','''R.frame{width:100%;height:100%;max-width:100%;max-height:100%}''')
for n,sel in [('pyramid','.level:first-child'),('matrix','.cell.on'),('matrix-nine','.cell.on')]:
 add(n,f'R>{sel} :is(.name,.note,.kick),R>{sel} .list,R>{sel} .list .name{{color:var(--a1-on)}}')
add('chart-scatter','R>.dot>span{background:var(--page);color:var(--ink);padding:0 var(--gap-sm)}')
add('roadmap','R .mile>span{background:var(--page);color:var(--ink)}')
add('heatmap','''.slide.dark R .cell{color:color-mix(in srgb,var(--ink) calc((1 - clamp(0,var(--v) - 60,1))*100%),var(--a1-on))}''')
# Code font extension uses an allowed local family, with no external resource in the collection.
p=C/'kit/kit.json';j=json.load(open(p));j['extensions']['--diecut-font-code']='font';p.write_text(json.dumps(j,indent=2))
p=C/'kit/css/tokens.css';p.write_text(p.read_text()+"\n.slide{--diecut-font-code:'Nanum Gothic Coding'}\n")
add('code','R>.lines{font-family:var(--diecut-font-code)}')
p=C/'foundation/foundation.css';s=p.read_text()+'''\n.slide .head{padding-top:0}.slide .kicker{gap:var(--gap-lg);font-size:var(--type-18);font-weight:var(--body-weight)}.slide .kicker .on{color:var(--a1);font-weight:var(--name-weight)}.slide .kicker .label{color:var(--n-6)}.slide .head.center .title{margin-top:var(--gap-lg)}.slide .rail{width:144px}.slide .rail .label{font-size:var(--type-120);line-height:var(--label-line)}\n''';p.write_text(s)
p=C/'kit/css/tokens.css';p.write_text(p.read_text().replace('--margin-y: 24px','--margin-y: 16px'))
# Replica final check refinements, in the third review wave.
p=R/'build/replica.py';s=p.read_text().replace('803 614v-21h18v21m-14-15h2m5 0h2m-9 5h2m5 0h2m-6 10v-5h4v5','779 614v-21h18v21m-14-15h2m5 0h2m-9 5h2m5 0h2m-6 10v-5h4v5').replace('cx="1064"','cx="1030"').replace('M1059 612v-12h10v12m-8-8v10m6-10v10','M1025 612v-12h10v12m-8-8v10m6-10v10').replace('M852 657','M790 657').replace('l8 11','l8 11').replace('cx="852"','cx="790"')
# map icon path now starts x790, subsequent absolute endpoint before Z is relative, so it remains coherent.
s=s.replace('8-11c5-7 1-16-8-16Z','8-11c5-7 1-16-8-16Z')
p.write_text(s)
print('Final source geometry and fit patches applied')
