"""Restore directly measured bases without source/size-driven design swaps.
Only the four explicitly reviewed element CSS files are rewritten.
"""
from pathlib import Path
P=Path(__file__).parent; E=P/'meridian-deck/elements'

def root(leaf,cls):
 s=f'.{cls}[data-el="meridian-deck-{leaf}"]'
 return s, f'''/* {leaf}: one measured base at every admitted size. */
{s}{{box-sizing:border-box;position:relative;min-width:0;min-height:0;container-type:size;font-family:var(--font-body);font-weight:var(--body-weight);line-height:var(--body-line);letter-spacing:var(--body-track);color:var(--n-7)}}
{s} *{{box-sizing:border-box}}
'''

s,css=root('legend','legend')
css+=f'''{s}{{display:flex;flex-direction:column;align-items:flex-start;justify-content:center;gap:calc(var(--gap-sm)*.35);padding:0}}
{s}>.key{{display:flex;align-items:center;gap:calc(var(--gap-sm)/2);min-width:0;max-width:100%;font-size:var(--type-10);font-weight:var(--body-weight);line-height:var(--body-line);color:var(--n-7);overflow-wrap:anywhere}}
{s}>.key::before{{content:"";display:block;flex:none;width:min(42px,53cqw);height:8px;background:var(--a1)}}
{s}>.key.tone-2::before{{background:var(--n-7)}}
{s}>.key.tone-3::before{{background:var(--n-6)}}
{s}>.key.tone-4::before{{background:var(--a2)}}
{s}>.key.tone-5::before{{background:var(--a3)}}
{s}>.key b{{font-weight:var(--name-weight)}}
'''
(E/'legend/element.css').write_text(css)

s,css=root('table','tablebox')
css+=f'''{s}{{display:block;padding:0}}
{s}>.table{{width:100%;height:100%;table-layout:fixed;border-collapse:separate;border-spacing:calc(var(--gap-sm)*1.1) calc(var(--gap-sm)*1.4);font-family:var(--font-body)}}
{s}>.table th,{s}>.table td{{padding:calc(var(--gap-sm)*.4);border:0;text-align:center;font-size:clamp(var(--type-10),2.4cqw,var(--type-14));font-weight:var(--body-weight);line-height:var(--label-line);overflow-wrap:anywhere;vertical-align:middle}}
{s}>.table th{{background:none;color:var(--a1-7);font-weight:var(--label-weight)}}
{s}>.table th:first-child{{width:13.55%}}
{s}>.table td{{border-radius:999px;background:var(--n-1);color:var(--n-7)}}
{s}>.table td{{position:relative;z-index:1}}
{s}>.table td:first-child{{position:relative;isolation:isolate;z-index:0;background:none;color:var(--n-7)}}
{s}>.table td:first-child::before{{content:"";position:absolute;inset:0 auto 0 0;width:calc(100%*160/74);border-radius:999px;background:var(--a1-1-muted);z-index:-1}}
{s}>.table tbody>tr:nth-child(n+4)>td:first-child{{color:var(--a1-on)}}
{s}>.table tbody>tr:nth-child(n+4)>td:first-child::before{{background:var(--a1)}}
{s}>.table .pick{{background:var(--a1-2-muted);color:var(--a1-7)}}
{s}>.table .num{{font-variant-numeric:tabular-nums;text-align:right}}
'''
css+=f'{s}>.table td>[data-el]{{width:100%;height:18cqh;min-height:0}}\n'
(E/'table/element.css').write_text(css)

# Point anchors preserve each real equal-step observation. The chart owns
# its connected series, markers, labels and single source baseline.
s,css=root('chart-line','lines')
css+=f'''{s}{{anchor-scope:all;display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);grid-template-rows:minmax(0,1fr) auto;padding:var(--gap-lg) var(--gap-sm) var(--gap);font-size:var(--type-16);color:var(--a1-7)}}
{s} .pt{{display:contents}}
{s} .pt>b{{position:relative;grid-row:1;align-self:start;height:calc(100%*(1 - var(--v)/var(--max,100)));display:flex;flex-direction:column;align-items:center;justify-content:flex-end;font-size:clamp(var(--type-10),3cqw,var(--type-16));font-weight:var(--figure-weight);line-height:var(--figure-line)}}
{s} .pt>b::after{{content:"";width:8px;height:8px;flex:none;border:var(--stroke) solid var(--a1);border-radius:50%;background:var(--page);margin-top:var(--gap-sm);margin-bottom:calc(var(--stroke)*-4);z-index:2}}
{s} .pt>span{{grid-row:2;text-align:center;padding-top:var(--gap-sm);font-size:var(--type-12);line-height:var(--label-line);color:var(--n-7)}}
{s}>.pt:first-child>span{{anchor-name:--meridian-v2-line-caption}}
{s}::after{{content:"";position:absolute;left:anchor(--meridian-v2-line-1 center);top:anchor(--meridian-v2-line-caption top);height:var(--stroke);background:var(--n-7);pointer-events:none}}
{s}:has(>.pt>b:empty):not(:has(>.pt>b:not(:empty))){{padding:0 var(--gap-sm)}}
'''
for n in range(1,25):
 css+=f'{s} .pt:nth-child({n})>b{{anchor-name:--meridian-v2-line-{n}}}\n'
 if n==1:continue
 css+=f'{s}:has(>.pt:nth-child({n}):last-child)::after{{right:anchor(--meridian-v2-line-{n} center)}}\n'
 for pseudo,direction,top,bottom in [('before','to top right',n-1,n),('after','to bottom right',n,n-1)]:
  css+=f'{s} .pt:nth-child({n})::{pseudo}{{content:"";position:absolute;pointer-events:none;left:anchor(--meridian-v2-line-{n-1} center);right:anchor(--meridian-v2-line-{n} center);top:calc(anchor(--meridian-v2-line-{top} bottom) - 1px);bottom:calc(anchor(--meridian-v2-line-{bottom} bottom) - 1px);background:linear-gradient({direction},transparent calc(50% - 1px),var(--a1) calc(50% - 1px),var(--a1) calc(50% + 1px),transparent calc(50% + 1px))}}\n'
(E/'chart-line/element.css').write_text(css)

s,css=root('delta','delta')
css+=f'''{s}{{display:grid;grid-template-columns:minmax(0,42fr) minmax(0,14fr) minmax(0,44fr);align-items:center;padding:0;isolation:isolate}}
{s}>.from,{s}>.to{{min-width:0;margin:0;padding:0 var(--gap-sm);text-align:center;font-size:clamp(var(--type-12),2.25cqw,var(--type-18));font-weight:var(--body-weight);line-height:var(--body-line);color:var(--n-7);overflow-wrap:anywhere}}
{s}>.from{{grid-column:1;grid-row:1}}
{s}>.to{{grid-column:3;grid-row:1;font-weight:var(--name-weight)}}
{s}::before{{content:"";grid-column:2;grid-row:1;width:100%;height:min(69.44cqh,9.375cqw);background:linear-gradient(to right,transparent,var(--a1-4-muted));clip-path:polygon(0 27%,66% 27%,66% 0,100% 50%,66% 100%,66% 73%,0 73%)}}
'''
(E/'delta/element.css').write_text(css)
