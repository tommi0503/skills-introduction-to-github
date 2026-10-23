from pathlib import Path
E=Path('/workspace/output/nightchamfer/elements')
p=E/'venn/element.css';p.write_text(p.read_text()+r'''
[data-el="nightchamfer-venn"]:has(>.set:nth-child(3)){display:block;padding:0}
[data-el="nightchamfer-venn"]:has(>.set:nth-child(3))>.set{position:absolute;left:calc(50% - 18cqmin);top:38%;width:58cqmin;height:58cqmin;max-height:none;flex:none;margin:0;transform:translate(-50%,-50%);padding:var(--gap-sm)}
[data-el="nightchamfer-venn"]:has(>.set:nth-child(3))>.set:nth-child(2){left:calc(50% + 18cqmin)}
[data-el="nightchamfer-venn"]:has(>.set:nth-child(3))>.set:nth-child(3){left:50%;top:65%}
[data-el="nightchamfer-venn"]:has(>.set:nth-child(3))>.set>.name{position:absolute;z-index:2;max-width:70%;top:25%;left:25%;transform:translate(-50%,-50%)}
[data-el="nightchamfer-venn"]:has(>.set:nth-child(3))>.set:nth-child(2)>.name{left:75%}
[data-el="nightchamfer-venn"]:has(>.set:nth-child(3))>.set:nth-child(3)>.name{left:50%;top:78%}
[data-el="nightchamfer-venn"]:has(>.set:nth-child(3))>.core{left:50%;right:auto;top:51%;transform:translate(-50%,-50%);z-index:3;width:max-content;max-width:35%;font-size:var(--type-18)}
''')
p=E/'heatmap/element.css';s=p.read_text()+r'''
[data-el="nightchamfer-heatmap"].calendar{--nightchamfer-calendar-rows:1;--nightchamfer-calendar-gap:calc(var(--gap-sm)/2);--nightchamfer-calendar-cell:min(calc((100cqw - 2*var(--gap-sm) - (var(--cols) - 1)*var(--nightchamfer-calendar-gap))/var(--cols)),calc((100cqh - 2*var(--gap-sm) - var(--type-14)*var(--body-line) - var(--nightchamfer-calendar-rows)*var(--nightchamfer-calendar-gap))/var(--nightchamfer-calendar-rows)));--nightchamfer-calendar-width:calc(var(--cols)*var(--nightchamfer-calendar-cell) + (var(--cols) - 1)*var(--nightchamfer-calendar-gap));align-items:center;justify-content:center}
[data-el="nightchamfer-heatmap"].calendar>.heads{width:var(--nightchamfer-calendar-width);flex:none;margin:0;min-height:calc(var(--type-14)*var(--body-line))}
[data-el="nightchamfer-heatmap"].calendar>.row{display:grid;grid-template-columns:repeat(var(--cols),var(--nightchamfer-calendar-cell));width:var(--nightchamfer-calendar-width);height:var(--nightchamfer-calendar-cell);flex:none;align-items:start}
[data-el="nightchamfer-heatmap"].calendar .cell{width:var(--nightchamfer-calendar-cell);height:var(--nightchamfer-calendar-cell);max-height:none;aspect-ratio:1;flex:none}
'''
for i in range(2,15):s+=f'\n[data-el="nightchamfer-heatmap"].calendar:has(>.row:nth-child({i} of .row)){{--nightchamfer-calendar-rows:{i}}}'
p.write_text(s+'\n')
