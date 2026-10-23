from pathlib import Path
p=Path(__file__).parent/'build_library.py';s=p.read_text()
start=s.index("# Area plots retain arbitrary value anchors;")
end=s.index("# Radar polygons",start)
s=s[:start]+'''# Generic interpolated area geometry uses a point's own --v and the already-laid-out previous anchor.
# The oversized anchor rectangle is clipped to the exact two point heights and baseline; b labels remain optional.
put('chart-area',\'''&{height:100%;position:relative;container-type:size;isolation:isolate;anchor-scope:all;border-bottom:var(--stroke) solid var(--n-4);background:repeating-linear-gradient(to top,var(--n-3) 0 1px,var(--page) 1px 25%)}& .series{position:absolute;inset:var(--gap-lg) 0 var(--gap-lg);display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);anchor-scope:all;color:var(--a1);z-index:4}& .series:nth-of-type(2){color:var(--a2);z-index:3}& .series:nth-of-type(3){color:var(--a3);z-index:2}& .series:nth-of-type(4){color:var(--a4);z-index:1}& .series>.name{position:absolute;top:calc(0px - var(--gap-lg));left:var(--gap);font-size:var(--type-14);font-weight:var(--label-weight);color:inherit}& .series:nth-of-type(2)>.name{left:30%}& .series:nth-of-type(3)>.name{left:60%}& .series:nth-of-type(4)>.name{left:80%}& .pt{width:0;height:0;justify-self:center;margin-top:calc((100cqh - var(--gap-lg)*2)*(1 - var(--v)/var(--max)))}& .pt b{display:block;width:max-content;translate:-50% -150%;font-size:var(--type-14);font-weight:var(--label-weight);color:inherit}& .pt::before,& .pt::after{content:'';position:absolute;bottom:0;pointer-events:none}& .pt::before{background:color-mix(in srgb,currentColor 24%,transparent);clip-path:polygon(0 calc(100cqh - var(--gap-lg)*2),100% calc(100% - (100cqh - var(--gap-lg)*2)*var(--v)/var(--max)),100% 100%,0 100%)}& .pt::after{background:currentColor;clip-path:polygon(0 calc(100cqh - var(--gap-lg)*2 - 1px),100% calc(100% - (100cqh - var(--gap-lg)*2)*var(--v)/var(--max) - 1px),100% calc(100% - (100cqh - var(--gap-lg)*2)*var(--v)/var(--max) + 1px),0 calc(100cqh - var(--gap-lg)*2 + 1px))}&.stacked .pt::before{background:currentColor}& .axis{position:absolute;left:0;right:0;bottom:0;height:var(--gap-lg);display:flex;align-items:center;justify-content:space-around;font-size:var(--type-14)}& .axis>span{flex:1;text-align:center}@container(max-width:650px){& .pt b,& .axis,& .series>.name{font-size:var(--type-12)}& .axis>span:nth-child(2n){visibility:hidden}}\''')
''' + s[end:]
a=s.index(" if name=='chart-area':\n",s.index('# Compile tokens'))
b=s.index(" if name=='radar':",a)
s=s[:a]+''' if name=='chart-area':
  for i in range(1,13):
   css+=f'{scope}>.series>.pt:nth-child({i} of .pt){{anchor-name:--od-area-{i}}}'
   if i==1:css+=f'{scope}>.series>.pt:nth-child(1 of .pt)::before,{scope}>.series>.pt:nth-child(1 of .pt)::after{{display:none}}'
   else:css+=f'{scope}>.series>.pt:nth-child({i} of .pt)::before,{scope}>.series>.pt:nth-child({i} of .pt)::after{{left:anchor(--od-area-{i-1} center);right:anchor(--od-area-{i} center);top:calc(anchor(--od-area-{i-1} top) - (100cqh - var(--gap-lg)*2))}}'
''' +s[b:]
# Small cards remain centered without forcing tall full-size tracks into a shallow grid cell.
s=s.replace("put('pill'", "D['card']+='&{container-type:size}& .parts:not(:has(.mark,.fig,.kick)){grid-template-rows:minmax(calc(var(--gap-lg)*2),auto) minmax(calc(var(--gap-lg)*2.6),auto)}@container(max-height:200px){& .parts,& .parts:not(:has(.mark,.fig,.kick)){display:flex;justify-content:center;gap:var(--gap-sm)}& .mark{display:none}& .name{font-size:var(--type-18)}& .note{font-size:var(--type-14)}}@container(max-height:100px){& .note{display:none}}'\nput('pill'")
p.write_text(s)
