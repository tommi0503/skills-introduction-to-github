from pathlib import Path
import re
C=Path('/workspace/output/nightchamfer')
# Mini line and mini bars are separate views of the same declared values.
s='[data-el="nightchamfer-sparkline"]';p=C/'elements/sparkline/element.css';css=f'''\n{s}{{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);grid-template-rows:1fr;align-items:start;anchor-scope:all;--nightchamfer-spark-stroke:var(--a1)}}{s}.up{{--nightchamfer-spark-stroke:var(--good)}}{s}.down{{--nightchamfer-spark-stroke:var(--bad)}}
{s}>span{{display:block;position:static;justify-self:center;align-self:start;flex:none;width:0;height:0;min-height:0;margin-top:calc(100cqh*(1 - var(--v)/var(--max)));background:none;border:0;anchor-name:var(--nightchamfer-self)}}
{s}>span:not(:first-child)::before,{s}>span:not(:first-child)::after{{content:"";position:absolute;left:anchor(var(--nightchamfer-prev) center);right:anchor(var(--nightchamfer-self) center);pointer-events:none}}
{s}>span:not(:first-child)::before{{top:calc(anchor(var(--nightchamfer-prev) top) - 1px);bottom:calc(anchor(var(--nightchamfer-self) top) - 1px);background:linear-gradient(to top right,color-mix(in srgb,var(--page) 0%,var(--ink) .001%) calc(50% - 1px),var(--nightchamfer-spark-stroke) 50%,color-mix(in srgb,var(--page) 0%,var(--ink) .001%) calc(50% + 1px))}}
{s}>span:not(:first-child)::after{{top:calc(anchor(var(--nightchamfer-self) top) - 1px);bottom:calc(anchor(var(--nightchamfer-prev) top) - 1px);background:linear-gradient(to bottom right,color-mix(in srgb,var(--page) 0%,var(--ink) .001%) calc(50% - 1px),var(--nightchamfer-spark-stroke) 50%,color-mix(in srgb,var(--page) 0%,var(--ink) .001%) calc(50% + 1px))}}
{s}.bars{{display:flex;align-items:flex-end}}{s}.bars>span{{position:relative;flex:1;min-width:0;width:auto;height:calc(var(--v)/var(--max)*90%);min-height:1px;margin:0;background:var(--nightchamfer-spark-stroke);border:0}}{s}.bars>span::before,{s}.bars>span::after{{display:none}}
'''
for i in range(1,25):css+=f'{s}>span:nth-child({i}){{--nightchamfer-self:--nc-spark-{i};--nightchamfer-prev:--nc-spark-{i-1};}}\n'
p.write_text(p.read_text()+css)
# Both dumbbell endpoints and the connecting interval follow the values, not fixed row ends.
s='[data-el="nightchamfer-slope"]';p=C/'elements/slope/element.css';p.write_text(p.read_text()+f'''\n{s}.dumbbell>.pair{{display:block;padding:0;min-height:0}}{s}.dumbbell>.pair>.name{{position:absolute;left:0;top:50%;transform:translateY(-50%);width:24%;font-size:var(--type-16)}}
{s}.dumbbell>.pair::before{{left:calc(28% + min(var(--a),var(--b))/var(--max)*64%);right:auto;width:calc(abs(var(--b) - var(--a))/var(--max)*64%);top:50%;height:2px;transform:none}}
{s}.dumbbell>.pair .a,{s}.dumbbell>.pair .b{{position:absolute;width:auto;padding:0;font-size:var(--type-14);line-height:var(--label-line);white-space:nowrap;background:none}}
{s}.dumbbell>.pair .a{{left:calc(28% + var(--a)/var(--max)*64%);top:calc(50% - var(--gap-sm));transform:translate(-50%,-100%);color:var(--n-8)}}
{s}.dumbbell>.pair .b{{left:calc(28% + var(--b)/var(--max)*64%);top:calc(50% + var(--gap-sm));transform:translateX(-50%);color:var(--a1-7)}}
{s}.dumbbell>.pair .a::after,{s}.dumbbell>.pair .b::after{{content:"";position:absolute;left:50%;transform:translateX(-50%);width:10px;height:10px;border-radius:50%;background:var(--n-5)}}
{s}.dumbbell>.pair .a::after{{top:calc(100% + var(--gap-sm) - 5px)}}{s}.dumbbell>.pair .b::after{{bottom:calc(100% + var(--gap-sm) - 5px);background:var(--a1)}}\n''')
# A genuine alternate timeline: odd entries above, even entries below the shared centreline.
s='[data-el="nightchamfer-timeline"]';p=C/'elements/timeline/element.css';css=f'''\n{s}.alt{{display:grid;grid-template-columns:repeat(var(--nightchamfer-stops,6),minmax(0,1fr));grid-template-rows:repeat(2,minmax(0,1fr));grid-auto-flow:row;gap:var(--gap);position:relative}}{s}.alt::before{{content:"";position:absolute;left:var(--gap-sm);right:var(--gap-sm);top:50%;height:1px;background:var(--n-4)}}
{s}.alt>.stop{{grid-row:1;align-self:stretch;height:auto;min-height:0;border:0;justify-content:flex-end;padding:0 var(--gap-sm) calc(var(--gap)*1.5);text-align:center}}
{s}.alt>.stop:nth-child(even){{grid-row:2;justify-content:flex-start;padding:calc(var(--gap)*1.5) var(--gap-sm) 0}}
{s}.alt>.stop::after{{display:none}}{s}.alt>.stop::before{{top:auto;bottom:calc(var(--gap)/-2 - 6px);left:50%;transform:translateX(-50%);width:12px;height:12px}}
{s}.alt>.stop:nth-child(even)::before{{bottom:auto;top:calc(var(--gap)/-2 - 6px)}}
'''
for i in range(1,13):css+=f'{s}.alt>.stop:nth-child({i}){{grid-column:{i}}}\n{s}.alt:has(>.stop:nth-child({i}):last-child){{--nightchamfer-stops:{i}}}\n'
p.write_text(p.read_text()+css)
for file,size in [('slope/dumbbell-6.html','6x5'),('timeline/track-alt-6.html','8x4')]:
 n,f=file.split('/');p=C/'elements'/n/'fixtures'/f
 if p.exists():p.write_text(re.sub(r'<!-- min:.*?-->','<!-- min: '+size+' -->',p.read_text(),count=1))
# Keep portrait and logo seats square instead of allowing a max-height to squash them.
s='[data-el="nightchamfer-person"]';p=C/'elements/person/element.css';p.write_text(p.read_text()+f'''\n{s} .seat.avatar{{width:min(50%,50cqh);height:auto;max-height:none;aspect-ratio:1;flex:none}}{s} .seat.portrait{{width:min(45%,38cqh);height:auto;max-height:none;aspect-ratio:3/4;flex:none}}\n''')
