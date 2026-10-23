from pathlib import Path
import math,json
C=Path('/workspace/output/nightchamfer');s='[data-el="nightchamfer-chart-area"]'
p=C/'elements/chart-area/element.css'
css=f'''\n{s}{{anchor-scope:all;--nightchamfer-plot-h:calc(100cqh - var(--gap-lg) - var(--pad))}}
{s}>.series{{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);grid-template-rows:1fr;align-items:start;anchor-scope:all;isolation:isolate;--nightchamfer-area-fill:var(--a1-2-soft);--nightchamfer-area-line:var(--a1)}}
{s}>.series.tone-2{{--nightchamfer-area-fill:var(--a2-2-soft);--nightchamfer-area-line:var(--a2)}}
{s}>.series.tone-3{{--nightchamfer-area-fill:var(--a3-2-soft);--nightchamfer-area-line:var(--a3)}}
{s}>.series.tone-4{{--nightchamfer-area-fill:var(--a4-2-soft);--nightchamfer-area-line:var(--a4)}}
{s}>.series>.pt{{position:static;justify-self:center;align-self:start;flex:none;width:0;height:0;min-width:0;display:block;background:none;border:0;margin-top:calc(var(--nightchamfer-plot-h)*(1 - var(--v)/var(--max)));--nightchamfer-vh:calc(var(--nightchamfer-plot-h)*var(--v)/var(--max));anchor-name:var(--nightchamfer-self)}}
{s}>.series>.pt:not(:first-of-type)::before{{content:"";position:absolute;left:anchor(var(--nightchamfer-prev) center);right:anchor(var(--nightchamfer-self) center);top:calc(anchor(var(--nightchamfer-prev) top) - var(--nightchamfer-plot-h));bottom:0;clip-path:polygon(0 var(--nightchamfer-plot-h),100% calc(100% - var(--nightchamfer-vh)),100% 100%,0 100%);background:var(--nightchamfer-area-fill)}}
{s}>.series>.pt:not(:first-of-type)::after{{content:"";position:absolute;left:anchor(var(--nightchamfer-prev) center);right:anchor(var(--nightchamfer-self) center);top:calc(anchor(var(--nightchamfer-prev) top) - var(--nightchamfer-plot-h));bottom:0;clip-path:polygon(0 calc(var(--nightchamfer-plot-h) - 1px),100% calc(100% - var(--nightchamfer-vh) - 1px),100% calc(100% - var(--nightchamfer-vh) + 1px),0 calc(var(--nightchamfer-plot-h) + 1px));background:var(--nightchamfer-area-line)}}
{s}>.series>.pt>b{{position:absolute;transform:translate(-50%,-150%);margin:0;z-index:10;color:var(--ink)}}
{s}.stacked>.series:nth-child(1){{z-index:4}}{s}.stacked>.series:nth-child(2){{z-index:3}}{s}.stacked>.series:nth-child(3){{z-index:2}}{s}.stacked>.series:nth-child(4){{z-index:1}}
'''
for i in range(1,25):
 # .name is the first child, so nth-of-type is not usable; .pt is always a div in canonical fixtures.
 css+=f'{s}>.series>.pt:nth-child({i+1}){{--nightchamfer-self:--nc-area-{i};--nightchamfer-prev:--nc-area-{i-1};}}\n'
# Explicit first data point follows the series name and does not connect backwards.
css+=f'{s}>.series>.pt:nth-child(2)::before,{s}>.series>.pt:nth-child(2)::after{{content:none}}\n'
p.write_text(p.read_text()+css)
# A radar supports every documented axis count rather than assuming five coordinates.
s='[data-el="nightchamfer-radar"]';p=C/'elements/radar/element.css';css=f'''\n{s}>.series{{display:contents;background:none;border:0;clip-path:none}}{s}>.series::before{{content:"";position:absolute;inset:12%;background:color-mix(in srgb,var(--a1) 24%,color-mix(in srgb,var(--page) 0%,var(--ink) .001%));z-index:-1}}{s}>.series.tone-2::before{{background:color-mix(in srgb,var(--a2) 22%,color-mix(in srgb,var(--page) 0%,var(--ink) .001%))}}{s}>.series.tone-3::before{{background:color-mix(in srgb,var(--a3) 20%,color-mix(in srgb,var(--page) 0%,var(--ink) .001%))}}{s}>.series>.name{{position:absolute;top:0;left:var(--gap);font-size:var(--type-14);color:var(--a1-7)}}{s}>.series.tone-2>.name{{left:40%;color:var(--a2-7)}}{s}>.series.tone-3>.name{{left:75%;color:var(--a3-7)}}'''
for n in range(3,9):
 sel=f'{s}:is([style*="--n:{n}"],[style*="--n: {n}"])'
 pts=[]
 for i in range(n):
  a=2*math.pi*i/n;dx=math.sin(a)*50;dy=-math.cos(a)*50
  pts.append(f'calc(50% + var(--v{i+1})/var(--max)*{dx:.6f}%) calc(50% + var(--v{i+1})/var(--max)*{dy:.6f}%)')
  css+=f'{sel}>.axis:nth-child({i+1}){{left:{50+math.sin(a)*44:.3f}%;top:{50-math.cos(a)*44:.3f}%}}\n'
 css+=f'{sel}>.series::before{{clip-path:polygon({",".join(pts)})}}\n'
p.write_text(p.read_text()+css)
# Shared kit extension for the contract's monospaced source element.
p=C/'kit/kit.json';j=json.loads(p.read_text());j['extensions']['--nightchamfer-font-code']='font';p.write_text(json.dumps(j,indent=2))
p=C/'kit/css/tokens.css';p.write_text(p.read_text()+"\n.slide { --nightchamfer-font-code: 'Nanum Gothic Coding'; }\n")
p=C/'elements/code/element.css';p.write_text(p.read_text()+'\n[data-el="nightchamfer-code"]>.lines{font-family:var(--nightchamfer-font-code)}\n')
