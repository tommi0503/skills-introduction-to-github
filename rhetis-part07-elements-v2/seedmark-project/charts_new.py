"""New data-driven chart definitions built from their contract data."""
import more_modules as M
N=M.N;D=N.CSS
D['chart-line']='''
${display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);grid-template-rows:minmax(0,1fr) auto;gap:var(--gap-sm);padding:var(--pad) var(--gap) var(--gap-lg);isolation:isolate;anchor-scope:all;}
$:before{content:'';position:absolute;inset:var(--pad) var(--gap) var(--gap-lg);background:repeating-linear-gradient(to bottom,var(--n-3) 0 1px,transparent 1px 25%);z-index:-1;}
$ .pt{display:contents;}
$ .pt>b{grid-row:1;align-self:start;justify-self:center;height:calc(var(--type-14)*var(--label-line));margin-top:calc((100cqh - var(--pad) - var(--gap-lg) - var(--gap-sm) - var(--type-12)*var(--label-line))*(1 - var(--v)/var(--max)) - var(--type-14)*var(--label-line));font-size:var(--type-14);font-weight:var(--figure-weight);line-height:var(--label-line);position:relative;anchor-name:var(--seedmark-self);white-space:nowrap;}
$ .pt>b:after{content:'';position:absolute;width:6px;height:6px;left:50%;bottom:-3px;transform:translateX(-50%);background:var(--ink);border-radius:50%;}
$ .pt>span{grid-row:2;text-align:center;font-size:var(--type-12);line-height:var(--label-line);border-top:var(--stroke) solid var(--n-3);padding-top:var(--gap-sm);white-space:nowrap;}
$ .pt:before,$ .pt:after{content:'';position:absolute;left:anchor(var(--seedmark-prev) center);right:anchor(var(--seedmark-self) center);pointer-events:none;}
$ .pt:before{top:anchor(var(--seedmark-self) bottom);bottom:anchor(var(--seedmark-prev) bottom);background:linear-gradient(to top right,transparent calc(50% - 1px),var(--ink) calc(50% - 1px),var(--ink) calc(50% + 1px),transparent calc(50% + 1px));}
$ .pt:after{top:anchor(var(--seedmark-prev) bottom);bottom:anchor(var(--seedmark-self) bottom);background:linear-gradient(to bottom right,transparent calc(50% - 1px),var(--ink) calc(50% - 1px),var(--ink) calc(50% + 1px),transparent calc(50% + 1px));}
$ .pt:first-child:before,$ .pt:first-child:after{display:none;}
@container(max-width:650px){$ .pt>span{font-size:var(--type-10)}$ .pt:nth-child(even):not(:last-child)>span{visibility:hidden;}$ .pt>b{font-size:var(--type-12)}}
'''
for i in range(1,25):D['chart-line']+=f'$ .pt:nth-child({i}){{--seedmark-self:--seedmark-line-{i};--seedmark-prev:--seedmark-line-{i-1};}}\n'
D['chart-area']='''
${isolation:isolate;}
$:before{content:'';position:absolute;inset:var(--pad) var(--gap) var(--gap-lg);background:repeating-linear-gradient(to bottom,var(--n-3) 0 1px,transparent 1px 25%);z-index:-1;}
$ .series{position:absolute;inset:var(--pad) var(--gap) calc(var(--gap-lg) + var(--gap-sm));display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);anchor-scope:all;}
$ .pt{width:0;height:0;justify-self:center;margin-top:calc((100cqh - var(--pad) - var(--gap-lg) - var(--gap-sm))*(1 - var(--v)/var(--max)));anchor-name:var(--seedmark-self);}
$ .pt:before{content:'';position:absolute;left:anchor(var(--seedmark-prev) center);right:anchor(var(--seedmark-self) center);top:calc(anchor(var(--seedmark-prev) top) - (100cqh - var(--pad) - var(--gap-lg) - var(--gap-sm)));bottom:0;background:color-mix(in srgb,var(--a1) 30%,transparent);clip-path:polygon(0 calc(100cqh - var(--pad) - var(--gap-lg) - var(--gap-sm)),100% calc(100% - (100cqh - var(--pad) - var(--gap-lg) - var(--gap-sm))*var(--v)/var(--max)),100% 100%,0 100%);}
$ .pt:first-of-type:before{display:none;}
$ .series>.name{position:absolute;left:0;top:calc(var(--pad)*-1);font-size:var(--type-12);line-height:var(--label-line);font-weight:var(--label-weight);}
$ .pt>b{display:block;position:relative;transform:translate(-50%,-100%);font-size:var(--type-12);font-weight:var(--figure-weight);line-height:var(--label-line);white-space:nowrap;}
$ .axis{position:absolute;bottom:0;left:var(--gap);right:var(--gap);height:var(--gap-lg);display:flex;justify-content:space-between;align-items:center;border-top:var(--stroke) solid var(--n-3);}
$ .axis>span{font-size:var(--type-12);line-height:var(--label-line);}
$ .series:nth-child(2 of .series) .pt:before{background:color-mix(in srgb,var(--a2) 30%,transparent);}
$ .series:nth-child(3 of .series) .pt:before{background:color-mix(in srgb,var(--a3) 30%,transparent);}
$ .series:nth-child(4 of .series) .pt:before{background:color-mix(in srgb,var(--a4) 30%,transparent);}
@container(max-width:650px){$ .axis>span{font-size:var(--type-10)}$ .axis>span:nth-child(even):not(:last-child){visibility:hidden;}}
'''
for i in range(1,25):D['chart-area']+=f'$ .pt:nth-child({i} of .pt){{--seedmark-self:--seedmark-area-{i};--seedmark-prev:--seedmark-area-{i-1};}}\n'
D['chart-stack']='''
${display:flex;align-items:stretch;gap:var(--gap);padding:var(--pad) var(--gap);}
$ .sbar{flex:1;position:relative;min-width:0;min-height:0;display:flex;flex-direction:column-reverse;justify-content:flex-start;}
$ .sbar>span{position:absolute;top:calc(100% + var(--gap-sm)/2);left:50%;transform:translateX(-50%);font-size:var(--type-12);line-height:var(--label-line);white-space:nowrap;}
$ .seg{height:calc(var(--v)/var(--max)*100%);width:100%;min-height:0;display:flex;align-items:center;justify-content:center;background:var(--a1);color:var(--a1-on);}
$ .seg b{font-size:var(--type-14);font-weight:var(--figure-weight);line-height:var(--label-line);}
$ .seg:nth-child(2 of .seg),$ .seg.tone-2{background:var(--a2-2-soft);color:var(--ink)}$ .seg:nth-child(3 of .seg),$ .seg.tone-3{background:var(--a3-2-soft);color:var(--ink)}$ .seg:nth-child(4 of .seg),$ .seg.tone-4{background:var(--a4-2-soft);color:var(--ink)}$ .seg.tone-1{background:var(--a1);color:var(--a1-on)}$ .seg.tone-5{background:var(--n-2);color:var(--ink)}
$.pct .seg{height:calc(var(--v)*1%);}
$.h{flex-direction:column;}
$.h .sbar{flex-direction:row;justify-content:flex-start;margin-left:calc(var(--pad)*2);}
$.h .sbar>span{left:auto;right:calc(100% + var(--gap-sm));top:50%;transform:translateY(-50%);}
$.h .seg{height:100%;width:calc(var(--v)/var(--max)*100%);}
$.h.pct .seg{width:calc(var(--v)*1%);}
@container(max-height:200px){$ .seg b{font-size:var(--type-10)}}
'''
D['chart-waterfall']='''
${display:flex;gap:var(--gap);padding:var(--pad) var(--gap) var(--gap-lg);isolation:isolate;}
$:before{content:'';position:absolute;inset:var(--pad) var(--gap) var(--gap-lg);background:repeating-linear-gradient(to top,var(--n-3) 0 1px,transparent 1px 25%);z-index:-1;}
$ .move{position:relative;flex:1;min-width:0;}
$ .move:before{content:'';position:absolute;left:10%;right:10%;bottom:calc(min(var(--from),var(--to))/var(--max)*100%);height:calc(abs(var(--to)-var(--from))/var(--max)*100%);background:var(--a1-2-soft);border:var(--stroke) solid var(--n-4);border-radius:var(--radius-sm);}
$ .move.down:before{background:var(--n-2)}$ .move.total:before{bottom:0;height:calc(var(--to)/var(--max)*100%);background:var(--a1);border-color:var(--a1)}
$ .move:not(:last-child):after{content:'';position:absolute;left:90%;width:calc(var(--gap) + 20%);bottom:calc(var(--to)/var(--max)*100%);height:1px;background:var(--n-5);}
$ .move>b{position:absolute;left:50%;bottom:calc(max(var(--from),var(--to))/var(--max)*100% + var(--gap-sm)/2);transform:translateX(-50%);font-size:var(--type-14);line-height:var(--label-line);white-space:nowrap;}
$ .move>span{position:absolute;left:50%;top:calc(100% + var(--gap-sm)/2);transform:translateX(-50%);font-size:var(--type-12);line-height:var(--label-line);white-space:nowrap;}
@container(max-width:650px){$ .move>b{font-size:var(--type-12)}$ .move>span{font-size:var(--type-10)}}
'''
D['chart-scatter']='''
${padding:var(--pad);isolation:isolate;}
$:before{content:'';position:absolute;inset:var(--pad);border-left:var(--stroke) solid var(--n-5);border-bottom:var(--stroke) solid var(--n-5);background:repeating-linear-gradient(to top,var(--n-2) 0 1px,transparent 1px 25%);z-index:-1;}
$ .axis-x{position:absolute;left:var(--pad);right:var(--pad);bottom:calc(var(--gap-sm)/4);text-align:center;font-size:var(--type-14);line-height:var(--label-line);}
$ .axis-y{position:absolute;left:calc(var(--gap-sm)/4);top:var(--pad);font-size:var(--type-14);line-height:var(--label-line);writing-mode:vertical-rl;}
$ .dot{position:absolute;left:calc(var(--pad) + (100cqw - var(--pad)*2)*var(--x)/var(--xmax));top:calc(var(--pad) + (100cqh - var(--pad)*2)*(1 - var(--y)/var(--ymax)));width:12px;height:12px;border-radius:50%;transform:translate(-50%,-50%);background:var(--n-5);border:2px solid var(--page);}
$ .dot.on{background:var(--a1);}$ .dot.tone-2{background:var(--a2)}$ .dot.tone-3{background:var(--a3)}$ .dot.tone-4{background:var(--a4)}
$ .dot>span{position:absolute;left:50%;bottom:calc(100% + var(--gap-sm)/3);transform:translateX(-50%);font-size:var(--type-12);line-height:var(--label-line);white-space:nowrap;}
$.bubble .dot{width:calc(12px + var(--r)*.55px);height:calc(12px + var(--r)*.55px);background:var(--a1-2-soft);border:var(--stroke) solid var(--a1);}
@container(max-width:650px){$ .dot>span{font-size:var(--type-10)}}
'''
D['gauge']='''
${display:grid;grid-template-columns:minmax(0,1fr) auto;grid-template-rows:auto 12px;align-content:center;gap:var(--gap-sm);padding:var(--gap-sm);}
$ .name{font-size:var(--type-20);font-weight:var(--name-weight);line-height:var(--name-line);}
$ .fig{font-size:var(--type-24);line-height:var(--figure-line);font-weight:var(--figure-weight);}
$:before,$:after{content:'';position:absolute;left:var(--gap-sm);right:var(--gap-sm);top:calc(50% + var(--gap-sm));height:12px;border-radius:999px;background:var(--n-2);}
$:after{right:auto;width:calc((100cqw - var(--gap-sm)*2)*var(--v)/100);background:var(--a1);}
@container(max-width:500px){$ .name{font-size:var(--type-16)}$ .fig{font-size:var(--type-20)}}
'''
D['bullet']='''
$.bullets{display:flex;flex-direction:column;gap:var(--gap);}
$.bullets>.bullet{flex:1;min-height:0;container-type:size;}
$.bullet{display:grid;grid-template-columns:minmax(0,1fr) auto;grid-template-rows:auto auto;align-content:center;gap:var(--gap-sm);padding:var(--gap-sm) var(--gap-sm) var(--gap-lg);}
$.bullet .name{font-size:var(--type-18);font-weight:var(--name-weight);line-height:var(--name-line)}$.bullet .fig{font-size:var(--type-24);font-weight:var(--figure-weight);line-height:var(--name-line)}
$.bullet .note{grid-column:1/span 2;font-size:var(--type-14);color:var(--n-7);line-height:var(--label-line);}
$.bullet:before{content:'';position:absolute;left:var(--gap-sm);right:var(--gap-sm);bottom:var(--gap-sm);height:14px;background:linear-gradient(to right,var(--n-3) calc(var(--low,40)*1%),var(--n-2) 0 calc(var(--high,75)*1%),var(--n-1) 0);border-radius:var(--radius-sm);}
$.bullet:after{content:'';position:absolute;left:var(--gap-sm);bottom:calc(var(--gap-sm) + 3px);width:calc((100cqw - var(--gap-sm)*2)*var(--v)/100);height:8px;background:var(--a1);border-radius:999px;}
$.bullet .fig:after{content:'';position:absolute;bottom:calc(var(--gap-sm) - 3px);left:calc(var(--gap-sm) + (100cqw - var(--gap-sm)*2)*var(--target)/100);height:20px;width:2px;background:var(--ink);z-index:2;}
@container(max-height:100px){$.bullet .name{font-size:var(--type-14)}$.bullet .fig{font-size:var(--type-18)}$.bullet .note{font-size:var(--type-12)}}
'''
D['sparkline']='''
${display:flex;align-items:flex-end;gap:calc(var(--gap-sm)/4);padding:var(--gap-sm);}
$>span{position:relative;flex:1;min-width:0;height:calc(var(--v)/var(--max)*100%);border-radius:var(--radius-sm) var(--radius-sm) 0 0;background:var(--a1);}
$.up>span{background:var(--good)}$.down>span{background:var(--bad)}
'''
# Sparse, data-scaled chart primitives; no fixture value or page condition is used.
if __name__=='__main__':N.emit();print('Fresh modules emitted:',len(D))
