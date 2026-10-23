from pathlib import Path
O=Path('/workspace/output/glasspulse/elements')
def write(k,css):
 p=O/k/'element.css';s=p.read_text();base=s[:s.index('\n',s.index('.icon{'))];p.write_text(base+'\n'+css+'\n')
def q(k,root):return f'.{root}[data-el="glasspulse-{k}"]'
# Data geometry for proportional flow bands; card placement remains the glass layout.
s=q('sankey','sankey')
css=f'''{s}{{--glasspulse-count:3;display:flex;flex-direction:column;gap:var(--gap-sm);isolation:isolate;padding:0;}}
{s}>.source{{position:absolute;left:0;top:50%;transform:translateY(-50%);width:28%;height:min(36cqh,200px);border:var(--stroke) solid var(--n-4);border-radius:var(--radius);background:linear-gradient(0deg,var(--a1-1-soft),var(--n-1) 28%);padding:var(--gap);display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:2;}}
{s}>.branch{{position:relative;margin-left:45%;width:55%;flex:1;min-height:0;border:var(--stroke) solid var(--n-4);border-radius:var(--radius);background:linear-gradient(0deg,var(--a1-1-soft),var(--n-1) 28%);padding:var(--gap-sm) var(--gap);display:flex;align-items:center;justify-content:space-between;gap:var(--gap-sm);--glasspulse-dx:17cqw;--glasspulse-dy:calc((var(--glasspulse-i) + .5)*(100cqh + var(--gap-sm))/var(--glasspulse-count) - var(--gap-sm)/2 - 50cqh);}}
{s}>.branch::before{{content:"";position:absolute;right:100%;top:50%;width:hypot(var(--glasspulse-dx),var(--glasspulse-dy));height:calc(var(--v)/100*min(36cqh,200px));background:color-mix(in srgb,var(--a1) 28%,var(--page));transform:translateY(-50%) rotate(atan2(var(--glasspulse-dy),var(--glasspulse-dx)));transform-origin:100% 50%;z-index:-1;}}
{s}>.branch.on{{border-color:var(--a1);background:var(--a1-1-soft);}}{s}>.branch.out{{border-style:dashed;}}
{s} .name{{font-size:var(--type-24);font-weight:var(--name-weight);line-height:var(--name-line);}}{s} .fig{{font-size:var(--type-32);font-weight:var(--figure-weight);line-height:var(--figure-line);color:var(--a1-7);}}
{s}>.branch:has(>.branch){{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.4fr);grid-auto-flow:row;gap:calc(var(--gap-sm)/4) var(--gap-sm);padding:calc(var(--gap-sm)/4) var(--gap-sm);}}
{s}>.branch:has(>.branch)>.name{{grid-column:1;grid-row:1;align-self:end;}}{s}>.branch:has(>.branch)>.fig{{grid-column:1;grid-row:2;align-self:start;}}
{s} .branch>.branch{{grid-column:2;position:relative;display:flex;align-items:center;justify-content:space-between;gap:calc(var(--gap-sm)/4);border:var(--stroke) solid var(--n-4);border-radius:var(--radius-sm);background:var(--n-1);padding:0 calc(var(--gap-sm)/4);min-height:0;}}
{s} .branch>.branch::before{{content:"";position:absolute;right:100%;top:50%;width:var(--gap-sm);height:calc(var(--v)/100*min(8cqh,40px));background:var(--a1-2-soft);}}
{s} .branch>.branch>.name{{font-size:var(--type-14);line-height:var(--label-line);}}{s} .branch>.branch>.fig{{font-size:var(--type-16);line-height:var(--label-line);}}
'''
for n in range(2,7):css+=f'{s}:has(>.branch:nth-child({n} of .branch):last-child){{--glasspulse-count:{n};}}\n'
for i in range(6):css+=f'{s}>.branch:nth-child({i+1} of .branch){{--glasspulse-i:{i};}}\n'
css+=f'@container(max-width:700px){{{s} .name{{font-size:var(--type-18);}}{s} .fig{{font-size:var(--type-24);}}}}'
write('sankey',css)
# Curved centre links follow the actual placed cards through local CSS anchors.
for k,root,item in [('mindmap','mindmap','branch'),('hub','hub','spoke')]:
 s=q(k,root);P=f'{s}>.{item}'
 css=f'''{s}{{--glasspulse-rows:3;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr) minmax(0,1fr);grid-template-rows:repeat(var(--glasspulse-rows),minmax(0,1fr));gap:var(--gap);padding:var(--gap);isolation:isolate;anchor-scope:all;}}
{s}>.core{{grid-column:2;grid-row:1/-1;justify-self:center;align-self:center;width:min(100%,65cqh);aspect-ratio:1;min-height:0;border-radius:50%;border:var(--stroke) solid var(--a1);background:var(--a1);color:var(--a1-on);display:flex;align-items:center;justify-content:center;text-align:center;padding:var(--gap);font-size:var(--type-28);font-weight:var(--name-weight);line-height:var(--name-line);anchor-name:--glasspulse-map-core;z-index:1;}}
{P}{{position:static;border:var(--stroke) solid var(--n-4);border-radius:var(--radius);background:linear-gradient(0deg,var(--a1-1-soft),var(--n-1) 28%);box-shadow:inset 0 0 0 1px var(--n-2);padding:var(--gap-sm) var(--gap);display:flex;flex-direction:column;justify-content:center;gap:calc(var(--gap-sm)/2);}}
{P}.on{{border-color:var(--a1);}}
{P}::before{{content:"";position:absolute;width:auto;height:auto;background:none;border:0;z-index:-1;pointer-events:none;}}
{s} .name{{font-size:var(--type-24);font-weight:var(--name-weight);line-height:var(--name-line);}}{s} .leaf{{font-size:var(--type-18);line-height:var(--body-line);color:var(--n-7);padding-left:var(--gap-sm);border-left:var(--stroke) solid var(--n-4);}}{s} .note{{font-size:var(--type-16);line-height:var(--body-line);color:var(--n-7);}}{s} .mark{{font-size:var(--type-20);color:var(--a1-7);}}
'''
 for n in range(2,7):css+=f'{s}:has(>.{item}:nth-child({n} of .{item}):last-child){{--glasspulse-rows:{(n+1)//2};}}\n'
 for i in range(6):
  j=i+1;left=i%2==0;row=i//2+1;self=f'--glasspulse-map-{j}'
  css+=f'{P}:nth-child({j} of .{item}){{grid-column:{1 if left else 3};grid-row:{row};anchor-name:{self};}}\n'
  css+=f'{P}:nth-child({j} of .{item})::before{{left:anchor({self+" right" if left else "--glasspulse-map-core right"});right:anchor({"--glasspulse-map-core left" if left else self+" left"});}}\n'
  # Upper rows curve down into the core; lower rows curve upward.
  for rows in [1,2,3]:
   loc=row-(rows+1)/2
   if row>rows:continue
   pref=f'{s}:has(>.{item}:nth-child({rows*2} of .{item}):last-child)' if rows==1 else f'{s}:is(:has(>.{item}:nth-child({rows*2-1} of .{item}):last-child),:has(>.{item}:nth-child({rows*2} of .{item}):last-child))'
   rule=f'{pref}>.{item}:nth-child({j} of .{item})::before'
   if loc==0:css+=rule+'{top:anchor(--glasspulse-map-core center);bottom:auto;height:var(--stroke);background:var(--n-4);border:0;}\n'
   else:
    top=f'{self} center' if loc<0 else '--glasspulse-map-core center';bottom='--glasspulse-map-core center' if loc<0 else f'{self} center'
    edge='top' if loc<0 else 'bottom';side='right' if left else 'left';radii=('0 100% 0 0' if left else '100% 0 0 0') if loc<0 else ('0 0 100% 0' if left else '0 0 0 100%')
    css+=rule+f'{{top:anchor({top});bottom:anchor({bottom});border-{edge}:var(--stroke) solid var(--n-4);border-{side}:var(--stroke) solid var(--n-4);border-radius:{radii};}}\n'
 css+=f'@container(max-width:700px){{{s} .name{{font-size:var(--type-20);}}{s} .leaf{{font-size:var(--type-14);}}}}\n'
 write(k,css)
# A closed directed polygon surrounds the centre; links are trimmed at card edges.
s=q('cycle','cycle')
css=f'''{s}{{--glasspulse-count:3;--glasspulse-nw:min(27cqw,260px);--glasspulse-nh:min(22cqh,110px);--glasspulse-rx:calc(50cqw - var(--glasspulse-nw)/2 - var(--gap));--glasspulse-ry:calc(50cqh - var(--glasspulse-nh)/2 - var(--gap));isolation:isolate;}}
{s}>.core{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:min(25cqw,35cqh);height:min(25cqw,35cqh);border:var(--stroke) solid var(--a1);border-radius:50%;background:var(--a1-1-soft);display:flex;align-items:center;justify-content:center;text-align:center;padding:var(--gap-sm);}}
{s}>.node{{--glasspulse-angle:calc(-90deg + var(--glasspulse-i)*360deg/var(--glasspulse-count));--glasspulse-next:calc(var(--glasspulse-angle) + 360deg/var(--glasspulse-count));--glasspulse-dx:calc((cos(var(--glasspulse-next)) - cos(var(--glasspulse-angle)))*var(--glasspulse-rx));--glasspulse-dy:calc((sin(var(--glasspulse-next)) - sin(var(--glasspulse-angle)))*var(--glasspulse-ry));--glasspulse-linkangle:atan2(var(--glasspulse-dy),var(--glasspulse-dx));--glasspulse-trim:min(calc(var(--glasspulse-nw)/2/max(.001,abs(cos(var(--glasspulse-linkangle))))),calc(var(--glasspulse-nh)/2/max(.001,abs(sin(var(--glasspulse-linkangle))))));position:absolute;left:calc(50% + cos(var(--glasspulse-angle))*var(--glasspulse-rx));top:calc(50% + sin(var(--glasspulse-angle))*var(--glasspulse-ry));transform:translate(-50%,-50%);width:var(--glasspulse-nw);height:var(--glasspulse-nh);border:var(--stroke) solid var(--n-4);border-radius:var(--radius);background:linear-gradient(0deg,var(--a1-1-soft),var(--n-1) 28%);padding:var(--gap-sm);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:calc(var(--gap-sm)/2);text-align:center;}}
{s}>.node.on{{border-color:var(--a1);}}
{s}>.node::after{{content:"";position:absolute;left:50%;top:50%;width:hypot(var(--glasspulse-dx),var(--glasspulse-dy));height:var(--stroke);background:linear-gradient(90deg,color-mix(in srgb,var(--page) 0%,var(--page) 0%) var(--glasspulse-trim),var(--a1) var(--glasspulse-trim),var(--a1) calc(100% - var(--glasspulse-trim)),color-mix(in srgb,var(--page) 0%,var(--page) 0%) calc(100% - var(--glasspulse-trim)));transform-origin:0 50%;transform:rotate(var(--glasspulse-linkangle));pointer-events:none;}}
{s}>.node::before{{content:"";position:absolute;left:calc(50% + var(--glasspulse-dx) - cos(var(--glasspulse-linkangle))*var(--glasspulse-trim));top:calc(50% + var(--glasspulse-dy) - sin(var(--glasspulse-linkangle))*var(--glasspulse-trim));width:10px;height:10px;border-top:var(--stroke) solid var(--a1);border-right:var(--stroke) solid var(--a1);transform:translate(-50%,-50%) rotate(calc(var(--glasspulse-linkangle) + 45deg));}}
{s} .name{{font-size:var(--type-24);font-weight:var(--name-weight);line-height:var(--name-line);}}{s} .note{{font-size:var(--type-18);color:var(--n-7);line-height:var(--body-line);}}
'''
for n in range(3,7):css+=f'{s}:has(>.node:nth-child({n} of .node):last-child){{--glasspulse-count:{n};}}\n'
for i in range(6):css+=f'{s}>.node:nth-child({i+1} of .node){{--glasspulse-i:{i};}}\n'
css+=f'@container(max-width:700px){{{s} .name{{font-size:var(--type-20);}}{s} .note{{font-size:var(--type-14);}}}}'
write('cycle',css)
# Mood line between consecutive stage centres; --next is the endpoint mood.
s=q('journey','journey')
css=f'''{s}{{--glasspulse-count:3;display:flex;gap:var(--gap);align-items:stretch;padding:var(--gap);isolation:isolate;}}
{s}>.stage{{border:var(--stroke) solid var(--n-4);border-radius:var(--radius);background:linear-gradient(0deg,var(--a1-1-soft),var(--n-1) 28%);flex:1;min-width:0;position:relative;padding:var(--gap);display:flex;flex-direction:column;justify-content:center;gap:var(--gap-sm);--glasspulse-dx:calc((100cqw + var(--gap))/var(--glasspulse-count));--glasspulse-dy:calc((var(--mood) - var(--next,var(--mood)))*.2cqh);}}
{s}>.stage::before{{content:"";position:absolute;width:14px;height:14px;left:50%;top:calc(12% + (100 - var(--mood))*.2%);transform:translate(-50%,-50%);border-radius:50%;background:var(--a1);box-shadow:0 0 0 8px var(--a1-1-soft);z-index:2;}}
{s}>.stage:not(:last-child)::after{{content:"";position:absolute;left:50%;top:calc(12% + (100 - var(--mood))*.2%);width:hypot(var(--glasspulse-dx),var(--glasspulse-dy));height:var(--stroke);background:var(--a1);transform-origin:0 50%;transform:rotate(atan2(var(--glasspulse-dy),var(--glasspulse-dx)));z-index:1;}}
{s}>.stage.on{{border-color:var(--a1);}}
{s} .name{{font-size:var(--type-24);font-weight:var(--name-weight);line-height:var(--name-line);}}{s} .note{{font-size:var(--type-18);line-height:var(--body-line);color:var(--n-7);}}{s} .pain{{font-size:var(--type-16);line-height:var(--body-line);color:var(--bad);padding-top:var(--gap-sm);border-top:var(--stroke) solid var(--n-4);}}
'''
for n in range(3,8):css+=f'{s}:has(>.stage:nth-child({n}):last-child){{--glasspulse-count:{n};}}\n'
write('journey',css)
# Running totals and their exact endpoint-to-next-start connector.
s=q('chart-waterfall','waterfall')
css=f'''{s}{{display:flex;align-items:stretch;gap:var(--gap);padding:var(--gap-lg);border-bottom:var(--stroke) solid var(--n-4);isolation:isolate;}}
{s}>.move{{flex:1;position:relative;min-width:0;}}
{s}>.move::before{{content:"";position:absolute;left:10%;right:10%;bottom:calc(min(var(--from),var(--to))/var(--max)*75% + 35px);height:calc(abs(var(--to) - var(--from))/var(--max)*75%);background:var(--a1-3-soft);border-radius:var(--radius-sm) var(--radius-sm) 0 0;}}
{s}>.move.down::before{{background:var(--n-4);}}{s}>.move.total::before{{bottom:35px;height:calc(var(--to)/var(--max)*75%);background:var(--a1);}}
{s}>.move:not(:last-child)::after{{content:"";position:absolute;left:90%;width:calc(20% + var(--gap));bottom:calc(var(--to)/var(--max)*75% + 35px);height:var(--stroke);background:var(--n-4);}}
{s}>.move>b{{position:absolute;bottom:calc(max(var(--from),var(--to))/var(--max)*75% + 48px);left:0;right:0;text-align:center;white-space:nowrap;font-size:var(--type-22);font-weight:var(--figure-weight);line-height:var(--figure-line);}}
{s}>.move>span{{position:absolute;bottom:0;left:0;right:0;text-align:center;font-size:var(--type-16);line-height:var(--label-line);white-space:nowrap;}}
'''
write('chart-waterfall',css)
# Tree connectors share each root's actual grid row instead of disconnected stubs.
s=q('hierarchy','org')
css=f'''{s}{{--glasspulse-cols:3;display:grid;grid-template-columns:repeat(var(--glasspulse-cols),minmax(0,1fr));grid-template-rows:auto minmax(0,1fr);gap:var(--gap-lg) var(--gap);padding:var(--gap);anchor-scope:all;isolation:isolate;}}
{s}>.root{{position:relative;grid-column:1/-1;justify-self:center;padding:var(--gap) var(--gap-lg);background:var(--a1);color:var(--a1-on);border-radius:999px;font-size:var(--type-28);font-weight:var(--name-weight);line-height:var(--name-line);anchor-name:--glasspulse-org-root;}}
{s}>.root::after{{content:"";position:absolute;left:50%;top:100%;width:var(--stroke);height:calc(var(--gap-lg)/2);background:var(--n-4);}}
{s}::before{{content:"";position:absolute;top:calc(anchor(--glasspulse-org-root bottom) + var(--gap-lg)/2);left:calc(var(--gap) + (100% - var(--gap)*2 - (var(--glasspulse-cols) - 1)*var(--gap))/var(--glasspulse-cols)/2);right:calc(var(--gap) + (100% - var(--gap)*2 - (var(--glasspulse-cols) - 1)*var(--gap))/var(--glasspulse-cols)/2);height:var(--stroke);background:var(--n-4);}}
{s}>.branch{{position:relative;display:flex;flex-direction:column;justify-content:flex-start;gap:calc(var(--gap-sm)/2);min-height:0;}}
{s}>.branch::before{{content:"";position:absolute;left:50%;top:calc(-1*var(--gap-lg)/2);height:calc(var(--gap-lg)/2);width:var(--stroke);background:var(--n-4);}}
{s} .node{{border:var(--stroke) solid var(--n-4);border-radius:var(--radius);background:linear-gradient(0deg,var(--a1-1-soft),var(--n-1) 28%);padding:var(--gap-sm);text-align:center;font-size:var(--type-24);font-weight:var(--name-weight);line-height:var(--name-line);}}
{s} .leaf{{position:relative;padding:calc(var(--gap-sm)/2) var(--gap-sm);border-left:var(--stroke) solid var(--n-4);font-size:var(--type-16);line-height:var(--label-line);background:var(--n-1);}}
{s} .leaf::before{{content:"";position:absolute;left:calc(-1*var(--stroke));bottom:100%;height:calc(var(--gap-sm)/2);width:var(--stroke);background:var(--n-4);}}
{s} .name{{font-size:var(--type-24);line-height:var(--name-line);}}
'''
for n in range(2,5):css+=f'{s}:has(>.branch:nth-child({n} of .branch):last-child){{--glasspulse-cols:{n};}}\n'
write('hierarchy',css)
s=q('decision-tree','dtree')
css=f'''{s}{{display:flex;flex-direction:column;justify-content:center;padding:var(--gap);isolation:isolate;}}
{s} .q{{position:relative;border:var(--stroke) solid var(--n-4);border-radius:var(--radius);background:linear-gradient(0deg,var(--a1-1-soft),var(--n-1) 28%);padding:var(--gap);text-align:center;}}
{s} .q>.name{{font-size:var(--type-26);font-weight:var(--name-weight);line-height:var(--name-line);}}
{s} .q:has(+.opts)::after{{content:"";position:absolute;left:50%;top:100%;height:calc(var(--gap)/2);width:var(--stroke);background:var(--n-4);}}
{s} .opts{{--glasspulse-count:2;position:relative;display:flex;gap:var(--gap);justify-content:center;margin-top:var(--gap);width:100%;}}
{s} .opts:has(>.opt:nth-child(3):last-child){{--glasspulse-count:3;}}
{s} .opts::before{{content:"";position:absolute;top:calc(-1*var(--gap)/2);left:calc((100% + var(--gap))/var(--glasspulse-count)/2 - var(--gap)/2);right:calc((100% + var(--gap))/var(--glasspulse-count)/2 - var(--gap)/2);height:var(--stroke);background:var(--n-4);}}
{s} .opt{{position:relative;flex:1;min-width:0;display:flex;flex-direction:column;align-items:stretch;justify-content:flex-start;gap:var(--gap-sm);padding-top:var(--gap);}}
{s} .opt::before{{content:"";position:absolute;left:50%;top:calc(-1*var(--gap)/2);height:calc(var(--gap)*1.5);width:var(--stroke);background:var(--n-4);}}
{s} .cond{{position:relative;align-self:center;text-align:center;font-size:var(--type-18);color:var(--a1-7);line-height:var(--label-line);background:var(--page);}}
{s} .cond::after{{content:"";position:absolute;left:50%;top:100%;height:var(--gap-sm);width:var(--stroke);background:var(--n-4);}}
{s} .end{{border:var(--stroke) solid var(--n-4);border-radius:var(--radius-sm);padding:var(--gap);text-align:center;background:var(--n-1);font-size:var(--type-22);line-height:var(--name-line);}}
{s} .end.on{{background:var(--a1);color:var(--a1-on);border-color:var(--a1);}}
{s} .opt>.opts{{margin-top:calc(var(--gap) - var(--gap-sm));}}
'''
write('decision-tree',css)
s=q('concentric','orbit')
css=f'''{s}{{position:relative;display:flex;align-items:center;justify-content:center;padding:var(--gap);}}
{s}>.ring{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);border-radius:50%;border:var(--stroke) solid var(--n-4);background:var(--n-1);display:grid;grid-template-columns:auto auto;justify-content:center;align-content:start;gap:calc(var(--gap-sm)/3);padding:calc(var(--gap-sm)*2/3);text-align:center;}}
{s}>.ring:nth-child(1){{width:min(90cqw,90cqh);height:min(90cqw,90cqh);}}{s}>.ring:nth-child(2){{width:min(62cqw,62cqh);height:min(62cqw,62cqh);background:var(--a1-1-soft);}}{s}>.ring:nth-child(3){{width:min(36cqw,36cqh);height:min(36cqw,36cqh);}}{s}>.ring:nth-child(4){{width:min(18cqw,18cqh);height:min(18cqw,18cqh);}}
{s}>.ring.on{{background:var(--a1);color:var(--a1-on);border-color:var(--a1);}}
{s} .name{{font-size:var(--type-20);font-weight:var(--name-weight);line-height:var(--name-line);}}{s} .fig{{font-size:var(--type-24);font-weight:var(--figure-weight);line-height:var(--figure-line);}}{s} .note{{grid-column:1/-1;font-size:var(--type-12);line-height:var(--label-line);}}
{s}>.ring:last-child{{display:flex;flex-wrap:wrap;align-content:center;align-items:center;justify-content:center;}}{s}>.ring:last-child>.note{{flex-basis:100%;}}
@container(max-height:520px){{{s}:has(>.ring:nth-child(4))>.ring:last-child>.note{{display:none;}}{s}:has(>.ring:nth-child(4))>.ring:last-child .name{{font-size:var(--type-16);}}{s}:has(>.ring:nth-child(4))>.ring:last-child .fig{{font-size:var(--type-18);}}}}
'''
write('concentric',css)
print('wrote nine glasspulse element CSS files')
