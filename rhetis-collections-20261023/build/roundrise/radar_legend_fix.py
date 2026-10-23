from pathlib import Path
p=Path('/workspace/output/roundrise/elements/radar/element.css');s=p.read_text();r='.radar[data-el="roundrise-radar"]'
s+=r+'''>.series{clip-path:none;border:0;background:none}'''+r+'''>.series:before{content:'';position:absolute;inset:0;background:color-mix(in srgb,var(--a1) 24%,var(--page));border:var(--stroke) solid var(--a1)}'''+r+'''>.series.tone-2:before{background:color-mix(in srgb,var(--a2) 20%,var(--page))}'''+r+'''>.series.tone-3:before{background:color-mix(in srgb,var(--a3) 20%,var(--page))}'''+r+'''>.series>.name{position:absolute;left:0;top:calc(var(--gap-lg)*-1);font-size:var(--type-16);font-weight:var(--label-weight);line-height:var(--label-line);color:var(--ink);white-space:nowrap}'''+r+'''>.series:nth-child(2 of .series)>.name{left:38%}'''+r+'''>.series:nth-child(3 of .series)>.name{left:76%}'''
for n in range(3,9):
 root=r+f':has(>.axis:nth-child({n} of .axis)):not(:has(>.axis:nth-child({n+1} of .axis)))'
 pts=[f'calc(50% + sin({i*360/n}deg)*var(--v{i+1})/var(--max)*50%) calc(50% - cos({i*360/n}deg)*var(--v{i+1})/var(--max)*50%)' for i in range(n)]
 s+=root+'>.series{clip-path:none}'+root+'>.series:before{clip-path:polygon('+','.join(pts)+')}'
p.write_text(s)
