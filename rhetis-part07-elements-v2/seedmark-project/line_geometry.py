"""Positive anchor rectangles: flat, rising and falling lines share one formula."""
def line_css():
 s='''
${display:grid;grid-template-columns:repeat(var(--seedmark-count),minmax(0,1fr));grid-template-rows:minmax(0,1fr);padding:var(--pad) var(--gap) var(--gap-lg);isolation:isolate;anchor-scope:all;}
$:before{content:'';position:absolute;inset:var(--pad) var(--gap) var(--gap-lg);background:repeating-linear-gradient(to bottom,var(--n-3) 0 1px,transparent 1px 25%);z-index:-1;}
$ .pt{position:static;grid-column:var(--seedmark-index);grid-row:1;align-self:start;justify-self:center;width:0;height:0;margin-top:calc(100cqh*(1 - var(--v)/var(--max)));anchor-name:var(--seedmark-self);}
$ .pt>b{position:absolute;left:anchor(var(--seedmark-self) center);top:anchor(var(--seedmark-self) center);transform:translate(-50%,-100%);font-size:var(--type-14);font-weight:var(--figure-weight);line-height:var(--label-line);white-space:nowrap;}
$ .pt>span{position:absolute;left:anchor(var(--seedmark-self) center);bottom:calc((var(--gap-lg) - var(--type-12)*var(--label-line))/2);transform:translateX(-50%);font-size:var(--type-12);line-height:var(--label-line);white-space:nowrap;}
$ .pt:before{content:'';position:absolute;left:anchor(var(--seedmark-prev) center);right:anchor(var(--seedmark-self) center);top:calc(anchor(var(--seedmark-prev) center) - 100cqh);bottom:var(--gap-lg);background:var(--ink);clip-path:polygon(0 100cqh,100% calc(100% - 100cqh*var(--v)/var(--max)),100% calc(100% - 100cqh*var(--v)/var(--max) + 2px),0 calc(100cqh + 2px));}
$ .pt:first-child:before{display:none;}
$ .pt:after{content:'';position:absolute;left:anchor(var(--seedmark-self) center);top:anchor(var(--seedmark-self) center);width:6px;height:6px;transform:translate(-50%,-50%);border-radius:50%;background:var(--ink);}
@container(max-width:650px){$ .pt>span{font-size:var(--type-10)}$ .pt:nth-child(even):not(:last-child)>span{visibility:hidden;}$ .pt>b{font-size:var(--type-12)}}
'''
 for n in range(1,25):s+=f'$:has(>.pt:nth-child({n}):last-child){{--seedmark-count:{n};}}\n$ .pt:nth-child({n}){{--seedmark-index:{n};--seedmark-self:--seedmark-line-{n};--seedmark-prev:--seedmark-line-{n-1};}}\n'
 return s

def spark_css():
 s='''
${display:grid;grid-template-columns:repeat(var(--seedmark-count),minmax(0,1fr));grid-template-rows:minmax(0,1fr);padding:var(--gap-sm);anchor-scope:all;}
$>span{position:static;grid-column:var(--seedmark-index);grid-row:1;align-self:start;justify-self:center;width:0;height:0;margin-top:calc(100cqh*(1 - var(--v)/var(--max)));anchor-name:var(--seedmark-self);}
$>span:before{content:'';position:absolute;left:anchor(var(--seedmark-prev) center);right:anchor(var(--seedmark-self) center);top:calc(anchor(var(--seedmark-prev) center) - 100cqh);bottom:var(--gap-sm);background:var(--ink);clip-path:polygon(0 100cqh,100% calc(100% - 100cqh*var(--v)/var(--max)),100% calc(100% - 100cqh*var(--v)/var(--max) + 2px),0 calc(100cqh + 2px));}
$>span:first-child:before{display:none;}
$.up>span:before{background:var(--good)}$.down>span:before{background:var(--bad)}
$.bars>span{align-self:end;justify-self:stretch;width:auto;height:calc(100cqh*var(--v)/var(--max));margin-top:0;margin-inline:calc(var(--gap-sm)/6);border-radius:var(--radius-sm) var(--radius-sm) 0 0;background:var(--a1);}
$.bars>span:before{display:none;}$.up.bars>span{background:var(--good)}$.down.bars>span{background:var(--bad)}
'''
 for n in range(1,25):s+=f'$:has(>span:nth-child({n}):last-child){{--seedmark-count:{n};}}\n$>span:nth-child({n}){{--seedmark-index:{n};--seedmark-self:--seedmark-spark-{n};--seedmark-prev:--seedmark-spark-{n-1};}}\n'
 return s
