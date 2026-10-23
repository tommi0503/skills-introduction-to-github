from pathlib import Path
import json
P=Path(__file__).parent/'crossrail'
def add(t,s):
 p=P/'elements'/t/'element.css'; p.write_text(p.read_text()+'\n/* Final functional review: sizing, data visibility and relationship geometry. */\n'+s+'\n')
def r(t):return '[data-el="crossrail-'+t+'"]'
s=r('balance');add('balance',f'{s} .pan{{transform:translateY(calc(var(--tilt)*-.5px))}}{s} .pan:nth-child(2){{transform:translateY(calc(var(--tilt)*.5px))}}')
s=r('chart-stack');css=''
for i in range(1,6):
 bg=f'--a{i}' if i<5 else '--n-2';fg=f'--a{i}-on' if i<5 else '--ink'
 css+=f'{s} .seg:nth-child({i} of .seg):not([class*="tone-"]){{background:var({bg});color:var({fg})}}'
add('chart-stack',css+f'{s}.h .sbar>span{{width:max-content;white-space:nowrap}}')
s=r('chart-donut');add('chart-donut',f'{s} .name{{width:min(50cqw,50cqh);max-width:min(50cqw,50cqh);white-space:normal;overflow-wrap:anywhere;font-size:var(--type-18)}}@container(max-height:260px){{{s} .name{{font-size:var(--type-14)}}}}')
s=r('concentric');add('concentric',f'{s} .ring:not(:last-child){{flex-direction:row;align-items:flex-start;justify-content:center;padding-top:var(--gap-sm)}}{s} .ring:not(:last-child)>.name{{font-size:var(--type-18);max-width:55%}}{s} .ring:not(:last-child)>.fig{{font-size:var(--type-22);max-width:35%}}{s} .ring:last-child{{align-items:center;justify-content:center;padding:var(--gap-sm)}}{s} .ring>.note{{position:absolute;bottom:var(--gap-sm);left:20%;width:60%;text-align:center;font-size:var(--type-14)}}@container(max-height:350px){{{s} .ring:not(:last-child){{padding-top:0;gap:calc(var(--gap-sm)/2)}}{s} .ring:not(:last-child)>.name{{font-size:var(--type-14)}}{s} .ring:not(:last-child)>.fig{{font-size:var(--type-16)}}{s} .ring:last-child>.name{{font-size:var(--type-16)}}{s} .ring:last-child>.fig{{font-size:var(--type-20)}}{s} .ring>.note{{display:none}}}}')
s=r('bullet');add('bullet',f'{s}.bullet{{align-content:center;min-height:0;padding-bottom:var(--gap-lg)}}{s}.bullet::before,{s} .fig::after{{bottom:calc(50% - var(--gap-lg))}}{s}.bullet::after{{bottom:calc(50% - var(--gap-lg) + 7px)}}@container(max-height:400px){{{s}.bullet::before,{s} .fig::after{{bottom:0}}{s}.bullet::after{{bottom:3px}}}}')
s=r('gauge');add('gauge',f'{s}{{container-type:size}}{s}::before,{s}::after{{bottom:calc(50% - var(--gap-lg))}}@container(max-height:180px){{{s}::before,{s}::after{{bottom:0}}}}')
s=r('heatmap');css=f'{s}{{--crossrail-heat-rows:2;container-type:size}}'
for n in range(2,13):css+=f'{s}:has(>.row:nth-child({n} of .row)){{--crossrail-heat-rows:{n}}}'
css+=f'{s}.calendar .heads,{s}.calendar .row{{width:min(100%,calc((100cqh - var(--type-16)*var(--body-line) - var(--gap-sm)*var(--crossrail-heat-rows))*var(--cols)/var(--crossrail-heat-rows) + var(--gap-sm)*(var(--cols) - 1)));align-self:center}}{s}.calendar .cell{{min-height:0}}{s}:not(.calendar) .row{{flex:1;min-height:64px;max-height:100px}}@container(max-height:400px){{{s}:not(.calendar) .row{{min-height:0;max-height:none}}{s} .cell{{min-height:0}}{s} .cell b{{font-size:var(--type-14)}}}}'
add('heatmap',css)
p=P/'elements/heatmap/element.json';d=json.loads(p.read_text());d['tokenDefaults']['--crossrail-heat-rows']=2;p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
s=r('sparkline');add('sparkline',f'.parts>{s}{{height:calc(var(--gap-lg)*2);flex:none;min-height:calc(var(--gap-lg)*2)}}')
s=r('image-frame');add('image-frame',f'.frame{s}{{width:auto;height:auto;max-width:100%;min-width:0;background:transparent;border-radius:0;overflow:hidden}}')
s=r('venn');z=f'{s}:has(>.set:nth-child(3))';add('venn',f'{z} .set{{position:absolute;margin:0;width:min(42cqw,58cqh);transform:translate(-50%,-50%);left:37%;top:36%}}{z} .set:nth-child(2){{left:63%}}{z} .set:nth-child(3){{left:50%;top:67%}}{z} .set:nth-child(-n+2)>.name{{transform:translateY(calc(var(--gap-lg)*-1))}}{z} .set:nth-child(3)>.name{{transform:translateY(var(--gap-lg))}}{z} .core{{top:52%}}')
s=r('cycle');css=f'{s}{{--crossrail-cycle-count:3}}'
for n in range(3,7):css+=f'{s}:has(>.node:nth-child({n} of .node):last-child){{--crossrail-cycle-count:{n}}}'
css+=f'{s} .node::after{{content:"";position:absolute;left:calc(50% + (cos(calc(var(--crossrail-angle) + 180deg/var(--crossrail-cycle-count))) - cos(var(--crossrail-angle)))*34cqw);top:calc(50% + (sin(calc(var(--crossrail-angle) + 180deg/var(--crossrail-cycle-count))) - sin(var(--crossrail-angle)))*33cqh);width:var(--gap-sm);height:var(--gap-sm);clip-path:polygon(0 0,100% 50%,0 100%);background:var(--n-5);transform:translate(-50%,-50%) rotate(calc(var(--crossrail-angle) + 180deg/var(--crossrail-cycle-count) + 90deg))}}'
add('cycle',css)
p=P/'elements/cycle/element.json';d=json.loads(p.read_text());d['tokenDefaults']['--crossrail-cycle-count']=3;p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
s=r('hub');add('hub',f'{s} .core{{z-index:5}}{s} .spoke::before{{content:"";position:absolute;left:50%;top:50%;width:hypot(calc(cos(var(--crossrail-angle))*34cqw),calc(sin(var(--crossrail-angle))*33cqh));height:1px;background:var(--n-3);transform-origin:left center;transform:rotate(atan2(calc(sin(var(--crossrail-angle))*-33cqh),calc(cos(var(--crossrail-angle))*-34cqw)));z-index:-1}}{s} .spoke>.name,{s} .spoke>.note,{s} .spoke>.mark{{position:relative;z-index:1;background:inherit}}')
# Keep chart labels above the filled areas from every series.
s=r('chart-area');css=f'{s}{{transform:translateX(0);anchor-scope:all;isolation:isolate}}{s} .series{{transform:none;container-type:normal;z-index:auto!important}}{s} .series>.pt{{z-index:auto}}{s} .series>.pt::before{{bottom:calc(var(--gap-lg) + var(--gap-sm))}}{s} .series>.pt b,{s} .series>.name{{z-index:20}}{s} .series>.pt::after{{z-index:21}}'
for i in range(1,5):css+=f'{s} .series:nth-child({i} of .series)>.pt::before{{z-index:{4-i}}}'
add('chart-area',css)
# Bare placeholders in library stacks retain square geometry.
p=P/'foundation/foundation.css';p.write_text(p.read_text()+'\n.slide .stack{container-type:size}.slide .stack>.seat{align-self:center;flex:none;width:min(45cqw,45cqh);height:min(45cqw,45cqh);aspect-ratio:1}\n')
print('final functional CSS batch applied; fixtures preserved')
# Ribbons must touch the source, including branches far below the first row.
s=r('sankey');css=f'{s}{{transform:translateX(0);anchor-scope:all;isolation:isolate}}{s}>.source{{anchor-name:--crossrail-flow-source;z-index:2}}{s}>.branch{{z-index:auto}}{s}>.branch::before{{position:fixed;left:anchor(--crossrail-flow-source right);right:anchor(var(--crossrail-flow-target) left);top:calc(anchor(--crossrail-flow-source center) - 100cqh);bottom:anchor(var(--crossrail-flow-target) center);width:auto;height:auto;min-height:0;transform:none;clip-path:polygon(0 100cqh,100% 100%,100% calc(100% + var(--v)*var(--gap-sm)/40),0 calc(100cqh + var(--v)*var(--gap-sm)/40));background:var(--n-3);z-index:-1}}{s} .branch .branch::before{{display:none}}'
for i in range(1,13):css+=f'{s}>.branch:nth-child({i} of .branch){{anchor-name:--crossrail-flow-{i};--crossrail-flow-target:--crossrail-flow-{i}}}'
add('sankey',css)
# Minimum-cell labels stay inside the tapered shapes.
s=r('funnel');add('funnel',f'@container(max-width:650px){{{s} .stage{{min-width:30%;padding-inline:var(--gap-sm)}}{s} .name{{font-size:var(--type-16);white-space:nowrap}}{s} .fig{{font-size:var(--type-22);white-space:nowrap}}}}@container(max-width:400px){{{s} .stage{{padding-inline:calc(var(--gap-sm)/2);gap:calc(var(--gap-sm)/2)}}{s} .name{{font-size:var(--type-14)}}{s} .fig{{font-size:var(--type-18)}}}}@container(max-height:350px){{{s} .stage{{padding-block:0}}}}')
s=r('pyramid');add('pyramid',f'@container(max-width:550px){{{s} .level:first-child{{width:52%}}{s} .level:first-child>.name{{font-size:var(--type-16)}}{s} .level:first-child>.note{{font-size:var(--type-14)}}}}')
s=r('concentric');add('concentric',f'@container(max-height:450px){{{s} .ring:not(:last-child){{padding-top:calc(var(--gap-sm)/2);gap:calc(var(--gap-sm)/2)}}{s} .ring:not(:last-child)>.name{{font-size:var(--type-14)}}{s} .ring:not(:last-child)>.fig{{font-size:var(--type-16)}}{s} .ring:last-child{{padding:calc(var(--gap-sm)/2);gap:calc(var(--gap-sm)/2)}}{s} .ring:last-child>.name{{font-size:var(--type-14)}}{s} .ring:last-child>.fig{{font-size:var(--type-16);white-space:nowrap}}}}')
