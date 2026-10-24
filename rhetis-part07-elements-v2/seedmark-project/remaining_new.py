"""Complete the new palette-independent Seedmark element set."""
import charts_new as Q
N=Q.N;D=N.CSS
D['quote']='''
${display:flex;flex-direction:column;justify-content:center;gap:var(--gap);padding:var(--pad);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);}
$ blockquote{font-size:var(--type-32);font-weight:var(--title-weight);line-height:var(--lead-line);}
$ blockquote:before{content:'“';display:block;font-size:var(--type-60);font-weight:var(--name-weight);line-height:var(--figure-line);}
$.big blockquote{font-size:var(--type-44);}
$ .by{display:grid;grid-template-columns:56px minmax(0,1fr);grid-template-rows:auto auto;gap:calc(var(--gap-sm)/3) var(--gap-sm);align-items:center;}
$ .by>.seat{grid-row:1/span 2;width:56px;height:56px;border-radius:50%;}
$ .by>.name{font-size:var(--type-20);font-weight:var(--name-weight);line-height:var(--name-line);}
$ .by>.note{font-size:var(--type-14);color:var(--n-7);line-height:var(--label-line);}
@container(max-height:350px){$ blockquote,$.big blockquote{font-size:var(--type-24)}$ blockquote:before{font-size:var(--type-36)}$ .by>.seat{width:48px;height:48px}}
'''
D['delta']='''
${display:flex;align-items:center;justify-content:center;gap:var(--gap-lg);padding:var(--gap-sm);}
$ .from,$ .to{position:relative;font-size:clamp(var(--type-24),min(10cqw,38cqh),var(--type-52));line-height:var(--name-line);font-weight:var(--figure-weight);}
$ .from{color:var(--n-7)}$ .to:before{content:'';position:absolute;right:calc(100% + var(--gap-sm));top:50%;width:var(--gap-sm);height:8px;background:var(--ink);transform:translateY(-50%);clip-path:polygon(0 40%,65% 40%,65% 0,100% 50%,65% 100%,65% 60%,0 60%);}
'''
D['table']='''
${display:flex;align-items:center;padding:var(--gap-sm);}
$ .table{width:100%;table-layout:fixed;border-collapse:collapse;font-size:var(--type-18);line-height:var(--body-line);}
$ th,$ td{padding:var(--gap-sm);border-bottom:var(--stroke) solid var(--n-3);text-align:left;overflow-wrap:anywhere;}
$ th{background:var(--ink);color:var(--page);font-weight:var(--name-weight);}
$ .num{text-align:right;font-variant-numeric:tabular-nums;}$ td.pick{background:var(--a1-2-soft);font-weight:var(--name-weight)}$ th.pick{background:var(--a1);color:var(--a1-on);}
@container(max-width:800px){$ .table{font-size:var(--type-14)}$ th,$ td{padding:calc(var(--gap-sm)/2)}}@container(max-height:400px){$ .table{font-size:var(--type-14);line-height:var(--label-line)}$ th,$ td{padding:calc(var(--gap-sm)/2)}}
'''
D['timeline']='''
${display:grid;grid-template-columns:repeat(var(--seedmark-count),minmax(0,1fr));gap:var(--gap);padding:var(--gap) var(--gap-sm);isolation:isolate;}
$:before{content:'';position:absolute;left:var(--gap-sm);right:var(--gap-sm);top:var(--gap-lg);height:var(--stroke);background:var(--n-3);z-index:-1;}
$ .stop{position:relative;min-width:0;display:flex;flex-direction:column;justify-content:center;gap:var(--gap-sm);border-left:var(--stroke) solid var(--n-2);padding-left:var(--gap-sm);}
$ .stop:before{content:'';position:absolute;left:-4px;top:calc(var(--gap-sm) - 3px);width:7px;height:7px;border-radius:50%;background:var(--n-5);}
$ .kick{font-size:var(--type-14);font-weight:var(--label-weight);line-height:var(--label-line);}
$ .name{font-size:var(--type-24);font-weight:var(--name-weight);line-height:var(--name-line);}
$ .note{font-size:var(--type-18);line-height:var(--body-line);}
$ .stop.on .kick{background:var(--ink);color:var(--page);border-radius:var(--radius-sm);padding:calc(var(--gap-sm)/2);}
$.col{grid-template-columns:1fr;grid-auto-rows:minmax(0,1fr);}
$.col:before{top:var(--gap);bottom:var(--gap);left:var(--gap-lg);width:var(--stroke);height:auto;}
$.col .stop{padding-left:var(--pad);border-left:0;}.col .stop:before{left:8px;top:50%;}
$.alt .stop:nth-child(even){flex-direction:column-reverse;}
@container(max-width:700px){$ .name{font-size:var(--type-18)}$ .note{font-size:var(--type-14)}$ .kick{font-size:var(--type-12)}}
'''
D['cycle']='''
${isolation:isolate;}
$:before{content:'';position:absolute;inset:18%;border:var(--stroke) solid var(--n-3);border-radius:50%;z-index:-1;}
$ .core{position:absolute;inset:35%;display:flex;align-items:center;justify-content:center;text-align:center;border-radius:50%;background:var(--a1);color:var(--a1-on);font-size:var(--type-20);font-weight:var(--name-weight);padding:var(--gap-sm);}
$ .node{position:absolute;left:calc(50% + sin(var(--seedmark-angle))*34cqw);top:calc(50% - cos(var(--seedmark-angle))*34cqh);width:24%;height:24%;transform:translate(-50%,-50%);padding:var(--gap-sm);display:flex;align-items:center;justify-content:center;text-align:center;border:var(--stroke) solid var(--n-3);border-radius:var(--radius);background:var(--page);font-size:var(--type-18);font-weight:var(--name-weight);line-height:var(--name-line);}
$ .node:after{content:'';position:absolute;right:-12px;top:50%;width:10px;height:8px;background:var(--n-5);clip-path:polygon(0 0,100% 50%,0 100%);transform:rotate(calc(var(--seedmark-angle) + 90deg));}
@container(max-width:650px){$ .node,$ .core{font-size:var(--type-14)}}
'''
D['hub']='''
${isolation:isolate;}
$ .core{position:absolute;inset:35%;display:flex;align-items:center;justify-content:center;padding:var(--gap-sm);border-radius:50%;background:var(--ink);color:var(--page);font-size:var(--type-20);font-weight:var(--name-weight);text-align:center;}
$ .spoke{position:absolute;left:calc(50% + sin(var(--seedmark-angle))*35cqw);top:calc(50% - cos(var(--seedmark-angle))*35cqh);transform:translate(-50%,-50%);width:26%;height:28%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:calc(var(--gap-sm)/2);text-align:center;background:var(--page);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);padding:var(--gap-sm);}
$ .spoke:before{content:'';position:absolute;left:50%;top:50%;width:100%;height:var(--stroke);background:var(--n-3);transform-origin:left center;transform:rotate(calc(var(--seedmark-angle) + 90deg));z-index:-1;}
$ .mark{width:32px;height:32px;display:flex;align-items:center;justify-content:center;border-radius:50%;background:var(--ink);color:var(--page);font-size:var(--type-14);}
$ .mark>.icon{width:56%;height:56%;}$ .name{font-size:var(--type-18);font-weight:var(--name-weight);line-height:var(--name-line)}$ .note{font-size:var(--type-14);line-height:var(--label-line);}
@container(max-width:650px){$ .name,$ .core{font-size:var(--type-14)}$ .note{font-size:var(--type-12)}}
'''
D['funnel']='''
${display:flex;flex-direction:column;align-items:center;gap:var(--gap-sm);padding:var(--gap-sm);}
$ .stage{width:100%;min-width:0;flex:1;isolation:isolate;min-height:0;position:relative;display:flex;align-items:center;justify-content:center;gap:var(--gap-sm);text-align:center;padding:calc(var(--gap-sm)/2);background:none;border:0;}
$ .stage:before{content:'';position:absolute;top:0;bottom:0;left:50%;transform:translateX(-50%);width:calc(var(--v)*1%);background:var(--n-1);border:var(--stroke) solid var(--n-3);border-radius:var(--radius-sm);z-index:-1;}
$ .stage:first-child{color:var(--a1-on)}$ .stage:first-child:before{background:var(--a1);border-color:var(--a1)}
$ .name{font-size:var(--type-18);line-height:var(--name-line);font-weight:var(--name-weight)}$ .fig{font-size:var(--type-24);line-height:var(--name-line);font-weight:var(--figure-weight);}
@container(max-width:650px){$ .name{font-size:var(--type-14)}$ .fig{font-size:var(--type-18)}}@container(max-height:300px){$ .stage{flex-direction:column;gap:0;}$ .name{font-size:var(--type-12)}$ .fig{font-size:var(--type-16)}}
'''
D['pyramid']='''
${display:flex;flex-direction:column;align-items:center;gap:var(--gap-sm);padding:var(--gap-sm);}
$ .level{position:relative;flex:1;min-height:0;width:calc((var(--seedmark-index) + 1)/(var(--seedmark-count) + 1)*100%);min-width:30%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:calc(var(--gap-sm)/2);padding:var(--gap-sm);background:var(--n-1);border:var(--stroke) solid var(--n-3);border-radius:var(--radius-sm);text-align:center;}
$ .level:first-child{background:var(--a1);color:var(--a1-on);border-color:var(--a1)}
$ .name{font-size:var(--type-20);line-height:var(--name-line);font-weight:var(--name-weight)}$ .note{font-size:var(--type-16);line-height:var(--body-line);}
@container(max-width:650px){$ .name{font-size:var(--type-16)}$ .note{font-size:var(--type-14)}}
'''
D['matrix']='''
${display:grid;grid-template-columns:repeat(2,minmax(0,1fr));grid-template-rows:repeat(2,minmax(0,1fr));gap:var(--gap-sm);padding:var(--gap-lg);}
$ .cell{min-width:0;min-height:0;border:var(--stroke) solid var(--n-3);border-radius:var(--radius);background:var(--n-1);padding:var(--gap);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:var(--gap-sm);font-size:var(--type-20);line-height:var(--name-line);}
$ .cell.on{border-color:var(--ink);background:var(--a1-2-soft);}
$ .axis-x{position:absolute;left:var(--gap-lg);right:var(--gap-lg);bottom:calc(var(--gap-sm)/2);display:flex;justify-content:space-around;font-size:var(--type-12);line-height:var(--label-line);}
$ .axis-y{position:absolute;left:calc(var(--gap-sm)/2);top:var(--gap-lg);bottom:var(--gap-lg);display:flex;flex-direction:column;justify-content:space-around;font-size:var(--type-12);line-height:var(--label-line);writing-mode:vertical-rl;}
$ .name{font-size:var(--type-24);line-height:var(--name-line);font-weight:var(--name-weight)}$ .kick{font-size:var(--type-32);line-height:var(--figure-line);font-weight:var(--figure-weight)}$ .list{width:100%;min-height:0;}
@container(max-width:650px){$ .cell{padding:var(--gap-sm);font-size:var(--type-16)}$ .name{font-size:var(--type-18)}$ .kick{font-size:var(--type-24)}}
'''
D['hierarchy']='''
${display:grid;grid-template-columns:repeat(var(--seedmark-count),minmax(0,1fr));grid-template-rows:1fr 2fr;gap:var(--gap-lg);padding:var(--gap-sm);}
$ .root{grid-column:1/-1;justify-self:center;width:50%;display:flex;align-items:center;justify-content:center;padding:var(--gap-sm);border-radius:999px;background:var(--ink);color:var(--page);font-size:var(--type-24);font-weight:var(--name-weight);text-align:center;position:relative;}
$ .root:after{content:'';position:absolute;top:100%;left:50%;height:calc(var(--gap-lg)/2);width:var(--stroke);background:var(--n-4);}
$ .branch{position:relative;min-width:0;display:flex;flex-direction:column;align-items:stretch;gap:var(--gap-sm);}
$ .branch:before{content:'';position:absolute;top:calc(var(--gap-lg)/-2);left:calc(var(--gap-lg)/-2);right:calc(var(--gap-lg)/-2);height:calc(var(--gap-lg)/2);border-top:var(--stroke) solid var(--n-4);border-left:var(--stroke) solid var(--n-4);}
$ .node,$ .leaf{flex:1;min-height:0;padding:var(--gap-sm);border:var(--stroke) solid var(--n-3);border-radius:var(--radius-sm);display:flex;align-items:center;justify-content:center;font-size:var(--type-18);line-height:var(--name-line);text-align:center;}
$ .node{font-weight:var(--name-weight);background:var(--n-1)}$ .leaf{font-size:var(--type-16);}
@container(max-width:650px){$ .root{font-size:var(--type-18)}$ .node,$ .leaf{font-size:var(--type-14)}}
'''
D['architecture']='''
${display:flex;flex-direction:column;gap:var(--gap-sm);padding:var(--gap-sm);}
$ .layer{flex:1;min-height:0;display:flex;align-items:center;gap:var(--gap);padding:var(--gap-sm) var(--gap);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);background:var(--n-1);}
$ .name{width:28%;flex:none;font-size:var(--type-22);line-height:var(--name-line);font-weight:var(--name-weight);}
$ .chip{display:flex;align-items:center;justify-content:center;min-width:0;flex:1;min-height:32px;padding:calc(var(--gap-sm)/2);border:var(--stroke) solid var(--n-3);border-radius:var(--radius-sm);background:var(--page);font-size:var(--type-16);line-height:var(--label-line);text-align:center;}
@container(max-width:650px){$ .layer{gap:var(--gap-sm);padding:var(--gap-sm)}$ .name{font-size:var(--type-16)}$ .chip{font-size:var(--type-12)}}
'''
D['versus']='''
${display:grid;grid-template-columns:minmax(0,1fr) 50px minmax(0,1fr);gap:var(--gap-sm);padding:var(--gap-sm);}
$ .side{min-width:0;min-height:0;padding:var(--gap);display:flex;flex-direction:column;justify-content:center;gap:var(--gap);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);background:var(--n-1);}
$ .side.on{border-color:var(--ink);background:var(--page);}
$ .side>.name{font-size:var(--type-28);line-height:var(--name-line);font-weight:var(--name-weight);}
$ .side>.list{min-height:0;}
$ .vs{display:flex;align-items:center;justify-content:center;font-size:var(--type-20);font-weight:var(--label-weight);line-height:var(--label-line);}
@container(max-width:650px){$ .side{padding:var(--gap-sm)}$ .side>.name{font-size:var(--type-20)}}
'''
D['pricing']='''
$.plans{display:flex;align-items:stretch;gap:var(--gap);}
$.plans>.plan{min-width:0;min-height:0;container-type:size;flex:1;}
$.plan{display:flex;flex-direction:column;justify-content:center;gap:var(--gap);padding:var(--pad);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);background:var(--page);}
$.plan.on{border-color:var(--ink);background:var(--a1-2-soft);}
$.plan>.name{font-size:var(--type-26);font-weight:var(--name-weight);line-height:var(--name-line);}
$ .price{border-bottom:var(--stroke) solid var(--n-3);padding-bottom:var(--gap-sm);}
$ .price .fig{font-size:var(--type-40);font-weight:var(--figure-weight);line-height:var(--name-line);}
$ .price small{font-size:var(--type-16);color:inherit;margin:0;}
$ .list{min-height:0;}
@container(max-width:400px){$ .name{font-size:var(--type-22)}$ .price .fig{font-size:var(--type-32)}$ .price small{font-size:var(--type-14)}}
'''
D['logo-group']='''
${display:grid;grid-template-columns:repeat(var(--seedmark-count),minmax(0,1fr));gap:var(--gap);align-items:center;padding:var(--gap-sm);}
$>.seat{width:100%;height:auto;aspect-ratio:1;border:var(--stroke) solid var(--n-3);border-radius:var(--radius);}
@container(max-width:700px){$>.seat{font-size:var(--type-12)}}
'''
D['heatmap']='''
${display:grid;grid-template-columns:minmax(0,1fr);grid-template-rows:auto repeat(var(--seedmark-count),minmax(0,1fr));gap:calc(var(--gap-sm)/2);padding:var(--gap-sm);}
$ .heads,$ .row{display:grid;grid-template-columns:minmax(0,1.5fr) repeat(var(--cols),minmax(0,1fr));gap:calc(var(--gap-sm)/2);min-height:0;align-items:stretch;}
$ .heads{font-size:var(--type-12);line-height:var(--label-line);text-align:center;}
$ .heads:before{content:'';}
$ .name{display:flex;align-items:center;font-size:var(--type-14);line-height:var(--label-line);font-weight:var(--label-weight);}
$ .cell{min-height:0;display:flex;align-items:center;justify-content:center;border:1px solid var(--n-2);border-radius:var(--radius-sm);background:color-mix(in srgb,var(--a1-2-soft) calc(var(--v)*1%),var(--page));}
$ .cell>b{font-size:var(--type-12);line-height:var(--label-line);font-weight:var(--label-weight);}
$.calendar .heads,$.calendar .row{grid-template-columns:repeat(var(--cols),minmax(0,1fr));}
$.calendar .heads:before{display:none}
@container(max-width:650px){$ .heads,$ .name,$ .cell>b{font-size:var(--type-10)}}
'''
D['waffle']='''
${display:flex;flex-direction:column;align-items:center;justify-content:center;gap:var(--gap-sm);padding:var(--gap-sm);text-align:center;}
$ .units{display:grid;grid-template-columns:repeat(10,minmax(0,1fr));gap:calc(var(--gap-sm)/3);width:min(90cqw,58cqh);}
$ .u{aspect-ratio:1;background:var(--n-2);border-radius:calc(var(--radius-sm)/3);}
$ .u.on{background:var(--a1)}$ .u.tone-2{background:var(--a2)}$ .u.tone-3{background:var(--a3)}$ .u.tone-4{background:var(--a4)}
$ .fig{font-size:var(--type-36);line-height:var(--name-line);font-weight:var(--figure-weight)}$ .name{font-size:var(--type-20);line-height:var(--name-line);font-weight:var(--name-weight);}
$ .name small{display:block;font-size:var(--type-12);line-height:var(--label-line);color:inherit;margin:0;}
$.figures .u{clip-path:polygon(35% 0,65% 0,75% 20%,65% 35%,85% 40%,95% 70%,75% 70%,70% 100%,55% 100%,50% 72%,45% 100%,30% 100%,25% 70%,5% 70%,15% 40%,35% 35%,25% 20%);}
@container(max-height:250px){$ .fig{font-size:var(--type-24)}$ .name{font-size:var(--type-16)}$ .units{width:min(85cqw,45cqh);}}
'''
D['treemap']='''
${display:flex;gap:var(--gap-sm);padding:var(--gap-sm);}
$ .branch{flex:var(--v) 0 0;min-width:0;min-height:0;display:flex;flex-direction:column;gap:calc(var(--gap-sm)/3);}
$ .branch>.name{font-size:var(--type-14);line-height:var(--label-line);font-weight:var(--name-weight);flex:none;}
$ .tile{flex:var(--v) 0 0;min-height:0;min-width:0;container-type:size;padding:calc(var(--gap-sm)/2);display:flex;align-items:center;justify-content:center;gap:calc(var(--gap-sm)/2);background:var(--n-1);border:var(--stroke) solid var(--n-3);border-radius:var(--radius-sm);}
$ .tile.on{background:var(--a1);border-color:var(--a1);color:var(--a1-on);}
$ .tile>.name{font-size:var(--type-16);line-height:var(--name-line);font-weight:var(--name-weight);}
$ .tile>.fig{font-size:var(--type-24);line-height:var(--name-line);font-weight:var(--figure-weight);}
@container(max-width:150px){$ .tile>.name{font-size:var(--type-10)}$ .tile>.fig{font-size:var(--type-14)}}@container(max-height:50px){$ .tile>.name{font-size:var(--type-10)}$ .tile>.fig{font-size:var(--type-12)}}
'''
D['sankey']='''
${display:flex;flex-direction:column;gap:var(--gap-sm);padding:var(--gap-sm);}
$ .source{position:absolute;left:var(--gap-sm);top:50%;transform:translateY(-50%);width:calc(var(--pad)*4);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:var(--gap-sm);padding:var(--gap);border-radius:var(--radius);background:var(--ink);color:var(--page);}
$ .branch{position:relative;margin-left:calc(var(--pad)*5);flex:var(--v) 0 0;min-height:64px;display:flex;flex-direction:column;justify-content:center;gap:calc(var(--gap-sm)/2);padding:var(--gap-sm);background:var(--n-1);border:var(--stroke) solid var(--n-3);border-radius:var(--radius-sm);}
$ .branch:before{content:'';position:absolute;right:100%;top:15%;bottom:15%;width:var(--pad);background:var(--a1-2-soft);clip-path:polygon(0 30%,100% 0,100% 100%,0 70%);}
$ .branch.on{background:var(--a1-2-soft);border-color:var(--ink)}$ .branch.out{background:var(--n-2);}
$ .name{font-size:var(--type-18);line-height:var(--name-line);font-weight:var(--name-weight)}$ .fig{font-size:var(--type-24);line-height:var(--name-line);font-weight:var(--figure-weight)}
@container(max-width:650px){$ .name{font-size:var(--type-14)}$ .fig{font-size:var(--type-18)}}
'''
D['radar']='''
${isolation:isolate;}
$:before{content:'';position:absolute;inset:18%;border:var(--stroke) solid var(--n-3);border-radius:50%;background:radial-gradient(circle,transparent 32%,var(--n-3) 32% 33%,transparent 33% 65%,var(--n-3) 65% 66%,transparent 66%);z-index:-1;}
$ .axis{position:absolute;left:calc(50% + sin(var(--seedmark-angle))*42cqw);top:calc(50% - cos(var(--seedmark-angle))*42cqh);transform:translate(-50%,-50%);max-width:24%;text-align:center;}
$ .axis>.name{font-size:var(--type-12);line-height:var(--label-line);font-weight:var(--label-weight);}
$ .series{position:absolute;inset:18%;}
$ .series:before{content:'';position:absolute;inset:0;background:color-mix(in srgb,var(--a1) 25%,transparent);}
$ .series>.name{position:absolute;left:0;top:calc(var(--gap-lg)*-1);font-size:var(--type-12);line-height:var(--label-line);font-weight:var(--label-weight);color:var(--ink);}
$ .series.tone-2:before{background:color-mix(in srgb,var(--a2) 25%,transparent);border-color:var(--a2)}$ .series.tone-3:before{background:color-mix(in srgb,var(--a3) 25%,transparent);border-color:var(--a3)}
'''
D['slope']='''
${isolation:isolate;padding:var(--gap-lg) var(--pad);}
$ .heads{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--gap-sm)/2);display:flex;justify-content:space-between;font-size:var(--type-14);line-height:var(--label-line);}
$ .pair{position:absolute;inset:var(--gap-lg) var(--pad);}
$ .pair:before{content:'';position:absolute;left:0;right:0;top:calc((1-max(var(--a),var(--b))/var(--max))*100%);height:calc(abs(var(--a)-var(--b))/var(--max)*100%);background:linear-gradient(to top right,transparent calc(50% - 1px),var(--n-4) calc(50% - 1px),var(--n-4) calc(50% + 1px),transparent calc(50% + 1px));}
$ .pair.on:before{background:linear-gradient(to top right,transparent calc(50% - 1px),var(--a1) calc(50% - 1px),var(--a1) calc(50% + 1px),transparent calc(50% + 1px));}
$ .pair>.a,$ .pair>.b{position:absolute;font-size:var(--type-14);line-height:var(--label-line);font-weight:var(--figure-weight);padding:0 calc(var(--gap-sm)/4);background:var(--page);}
$ .pair>.a{left:0;bottom:calc(var(--a)/var(--max)*100%);transform:translate(-50%,50%);}$ .pair>.b{right:0;bottom:calc(var(--b)/var(--max)*100%);transform:translate(50%,50%);}
$ .pair>.name{position:absolute;left:var(--gap-sm);bottom:calc(var(--a)/var(--max)*100%);font-size:var(--type-12);line-height:var(--label-line);transform:translateY(-50%);}
$.dumbbell{display:flex;flex-direction:column;gap:var(--gap-sm);}
$.dumbbell .pair{position:relative;inset:auto;flex:1;margin-left:calc(var(--pad)*3);margin-right:var(--gap);}
$.dumbbell .pair:before{left:calc(min(var(--a),var(--b))/var(--max)*100%);width:calc(abs(var(--a)-var(--b))/var(--max)*100%);right:auto;top:50%;height:2px;background:var(--n-4);}
$.dumbbell .pair>.name{left:calc(var(--pad)*-3);bottom:50%;max-width:calc(var(--pad)*2.5);}
$.dumbbell .pair>.a{left:calc(var(--a)/var(--max)*100%);bottom:50%;}.dumbbell .pair>.b{right:auto;left:calc(var(--b)/var(--max)*100%);bottom:50%;transform:translate(-50%,50%);}
'''
D['roadmap']='''
${display:flex;flex-direction:column;gap:var(--gap-sm);padding:var(--gap-sm);}
$ .heads{display:grid;grid-template-columns:repeat(var(--cols),minmax(0,1fr));margin-left:calc(var(--pad)*4);gap:var(--gap-sm);}
$ .heads>span{font-size:var(--type-12);line-height:var(--label-line);text-align:center;}
$ .lane{position:relative;flex:1;min-height:0;margin-left:calc(var(--pad)*4);display:flex;flex-direction:column;justify-content:center;gap:calc(var(--gap-sm)/2);border-bottom:var(--stroke) solid var(--n-3);}
$ .lane>.name{position:absolute;right:calc(100% + var(--gap-sm));width:calc(var(--pad)*3.5);top:50%;transform:translateY(-50%);font-size:var(--type-16);line-height:var(--name-line);font-weight:var(--name-weight);}
$ .bar{position:relative;margin-left:calc(var(--from)/var(--cols)*100%);width:calc((var(--to)-var(--from))/var(--cols)*100%);height:36px;max-height:80%;border-radius:999px;background:var(--n-2);border:var(--stroke) solid var(--n-3);display:flex;align-items:center;justify-content:center;}
$ .bar.on{background:var(--a1);color:var(--a1-on);border-color:var(--a1)}$ .bar>span{font-size:var(--type-14);line-height:var(--label-line);text-align:center;}
$ .mile{position:absolute;left:calc(var(--at)/var(--cols)*100%);top:0;bottom:0;width:1px;border-left:1px dashed var(--n-5);}$ .mile>span{position:absolute;left:var(--gap-sm);top:0;font-size:var(--type-12);line-height:var(--label-line);white-space:nowrap;}
@container(max-width:650px){$ .bar>span{font-size:var(--type-10)}$ .lane>.name{font-size:var(--type-12)}}
'''
D['swimlane']='''
${display:grid;grid-template-columns:repeat(var(--cols),minmax(0,1fr));grid-auto-rows:minmax(0,1fr);gap:var(--gap);padding:var(--gap-sm) var(--gap-sm) var(--gap-sm) calc(var(--pad)*3);}
$ .lane{grid-column:1/-1;position:relative;border-bottom:var(--stroke) solid var(--n-3);background:var(--n-1);border-radius:var(--radius-sm);}
$ .lane>.name{position:absolute;right:calc(100% + var(--gap-sm));top:50%;transform:translateY(-50%);width:calc(var(--pad)*2.5);font-size:var(--type-14);line-height:var(--name-line);font-weight:var(--name-weight);}
$ .node{position:relative;z-index:1;min-width:0;min-height:0;display:flex;align-items:center;justify-content:center;padding:var(--gap-sm);background:var(--page);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);font-size:var(--type-16);font-weight:var(--name-weight);line-height:var(--name-line);text-align:center;}
$ .node.start,$ .node.end{border-radius:999px;background:var(--ink);color:var(--page);border-color:var(--ink)}$ .node.ask{background:var(--a1-2-soft);border-color:var(--ink)}
$ .node.to-r:after{content:'';position:absolute;left:100%;top:50%;width:var(--gap);height:8px;transform:translateY(-50%);background:var(--n-5);clip-path:polygon(0 40%,80% 40%,80% 0,100% 50%,80% 100%,80% 60%,0 60%);}
$ .node.to-d:before{content:'';position:absolute;top:100%;left:50%;height:var(--gap);width:8px;transform:translateX(-50%);background:var(--n-5);clip-path:polygon(40% 0,60% 0,60% 80%,100% 80%,50% 100%,0 80%,40% 80%);}
@container(max-width:650px){$ .node{font-size:var(--type-12);padding:calc(var(--gap-sm)/2)}$ .lane>.name{font-size:var(--type-12)}}
'''
D['journey']='''
${display:grid;grid-template-columns:repeat(var(--seedmark-count),minmax(0,1fr));gap:var(--gap);padding:var(--gap-sm);}
$ .stage{position:relative;min-width:0;display:flex;flex-direction:column;justify-content:flex-end;gap:var(--gap-sm);padding-bottom:var(--gap-sm);border-bottom:var(--stroke) solid var(--n-3);}
$ .stage:before{content:'';position:absolute;left:0;right:0;top:calc(12% + (1-var(--mood)/100)*35%);height:calc(abs(var(--next,var(--mood))-var(--mood))*.35% + 2px);background:linear-gradient(to top right,transparent calc(50% - 1px),var(--n-5) calc(50% - 1px),var(--n-5) calc(50% + 1px),transparent calc(50% + 1px));}
$ .stage:after{content:'';position:absolute;left:0;top:calc(12% + (1-var(--mood)/100)*35%);width:8px;height:8px;transform:translate(-50%,-50%);border-radius:50%;background:var(--n-5);}
$ .stage.on:after{background:var(--a1)}$ .name{font-size:var(--type-20);line-height:var(--name-line);font-weight:var(--name-weight)}$ .note,$ .pain{font-size:var(--type-16);line-height:var(--body-line)}$ .pain{color:var(--bad);}
@container(max-width:650px){$ .name{font-size:var(--type-16)}$ .note,$ .pain{font-size:var(--type-12)}}
'''
D['mindmap']='''
${display:grid;grid-template-columns:1fr 1fr 1fr;grid-auto-rows:minmax(0,1fr);gap:var(--gap);padding:var(--gap-sm);}
$ .core{grid-column:2;grid-row:1/span var(--seedmark-half);align-self:center;display:flex;align-items:center;justify-content:center;text-align:center;padding:var(--gap);border-radius:999px;background:var(--ink);color:var(--page);font-size:var(--type-24);font-weight:var(--name-weight);line-height:var(--name-line);}
$ .branch{position:relative;display:flex;flex-direction:column;justify-content:center;gap:calc(var(--gap-sm)/2);padding:var(--gap-sm);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);background:var(--n-1);}
$ .branch:nth-child(even of .branch){grid-column:1;}$ .branch:nth-child(odd of .branch){grid-column:3;}
$ .branch:before{content:'';position:absolute;right:100%;top:50%;width:var(--gap);height:var(--stroke);background:var(--n-3);}
$ .branch:nth-child(even of .branch):before{right:auto;left:100%;}
$ .name{font-size:var(--type-20);font-weight:var(--name-weight);line-height:var(--name-line)}$ .leaf{font-size:var(--type-16);line-height:var(--body-line);border-top:var(--stroke) solid var(--n-3);padding-top:calc(var(--gap-sm)/2);}
@container(max-width:650px){$ .name{font-size:var(--type-16)}$ .leaf{font-size:var(--type-12)}}
'''
D['decision-tree']='''
${display:flex;flex-direction:column;justify-content:center;gap:var(--gap-lg);padding:var(--gap-sm);}
$ .q{align-self:center;max-width:70%;padding:var(--gap-sm) var(--gap);border:var(--stroke) solid var(--ink);border-radius:999px;background:var(--n-1);position:relative;text-align:center;}
$ .q:after{content:'';position:absolute;left:50%;top:100%;height:var(--gap-lg);width:var(--stroke);background:var(--n-3);}
$ .opts{display:flex;gap:var(--gap);min-width:0;}
$ .opt{position:relative;flex:1;min-width:0;display:flex;flex-direction:column;align-items:center;gap:var(--gap-sm);}
$ .opt:before{content:'';position:absolute;left:0;right:0;top:calc(var(--gap-lg)*-1);height:var(--gap-lg);border-top:var(--stroke) solid var(--n-3);border-left:var(--stroke) solid var(--n-3);}
$ .cond{font-size:var(--type-14);line-height:var(--label-line);color:var(--n-7);}
$ .end{padding:var(--gap);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);background:var(--page);text-align:center;}
$ .end.on{background:var(--a1);color:var(--a1-on);border-color:var(--a1)}$ .name{font-size:var(--type-18);font-weight:var(--name-weight);line-height:var(--name-line);}
@container(max-width:700px){$ .name{font-size:var(--type-14)}$ .cond{font-size:var(--type-12)}}
'''
D['balance']='''
${display:grid;grid-template-columns:repeat(2,minmax(0,1fr));align-items:center;gap:var(--gap-lg);padding:var(--pad) var(--gap);isolation:isolate;}
$:before{content:'';position:absolute;left:10%;right:10%;top:50%;height:var(--stroke);background:var(--n-5);rotate:calc(var(--tilt)*-.12deg);}
$ .pan{position:relative;padding:var(--gap-sm);display:flex;flex-direction:column;gap:var(--gap-sm);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);background:var(--page);transform:translateY(calc(var(--tilt)*-.18%));}
$ .pan:nth-child(2){transform:translateY(calc(var(--tilt)*.18%));}$ .pan.on{border-color:var(--ink);background:var(--a1-2-soft);}
$ .pan>.name{font-size:var(--type-22);font-weight:var(--name-weight);line-height:var(--name-line);}
$ .item{padding:calc(var(--gap-sm)/2);border-top:var(--stroke) solid var(--n-3);}
$ .item>.name{font-size:var(--type-16);line-height:var(--name-line);}
$ .fulcrum{position:absolute;left:45%;right:45%;bottom:10%;height:20%;background:none;}
$ .fulcrum:before{content:'';position:absolute;inset:0;background:var(--n-3);clip-path:polygon(50% 0,100% 100%,0 100%);}
$ .fulcrum>span{position:absolute;bottom:0;left:50%;transform:translateX(-50%);font-size:var(--type-12);white-space:nowrap;}
@container(max-width:650px){$ .pan>.name{font-size:var(--type-18)}$ .item>.name{font-size:var(--type-14)}}
'''
D['matrix-nine']='''
${display:grid;grid-template-columns:repeat(3,minmax(0,1fr));grid-template-rows:repeat(3,minmax(0,1fr));gap:var(--gap-sm);padding:var(--gap-lg);}
$ .cell{min-width:0;min-height:0;padding:var(--gap-sm);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:var(--gap-sm);border:var(--stroke) solid var(--n-3);border-radius:var(--radius-sm);background:var(--n-1);}
$ .cell.on{background:var(--a1);color:var(--a1-on);border-color:var(--a1)}
$ .cell.tone-2{background:var(--a2-2-soft)}$ .cell.tone-3{background:var(--a3-2-soft)}$ .cell.tone-4{background:var(--a4-2-soft)}$ .cell.tone-5{background:var(--n-2)}
$ .name{font-size:var(--type-20);font-weight:var(--name-weight);line-height:var(--name-line)}$ .note{font-size:var(--type-14);line-height:var(--body-line);}
$ .axis-x{position:absolute;left:var(--gap-lg);right:var(--gap-lg);bottom:calc(var(--gap-sm)/2);display:flex;justify-content:space-around;font-size:var(--type-12);line-height:var(--label-line);}
$ .axis-y{position:absolute;left:calc(var(--gap-sm)/2);top:var(--gap-lg);bottom:var(--gap-lg);display:flex;flex-direction:column;justify-content:space-around;font-size:var(--type-12);line-height:var(--label-line);writing-mode:vertical-rl;}
@container(max-width:650px){$ .name{font-size:var(--type-16)}$ .note{font-size:var(--type-12)}}
'''
D['network']='''
${isolation:isolate;}
$ .node{position:absolute;left:calc(10% + var(--x)*.8%);top:calc(10% + var(--y)*.8%);transform:translate(-50%,-50%);width:20%;min-height:14%;padding:var(--gap-sm);display:flex;align-items:center;justify-content:center;text-align:center;border:var(--stroke) solid var(--n-3);border-radius:var(--radius);background:var(--page);z-index:1;}
$ .node.on{background:var(--ink);border-color:var(--ink);color:var(--page);}
$ .node>.name{font-size:var(--type-18);line-height:var(--name-line);font-weight:var(--name-weight);}
$ .link{position:absolute;left:calc(10% + var(--x1)*.8%);top:calc(10% + var(--y1)*.8%);width:hypot(calc((var(--x2)-var(--x1))*.8cqw),calc((var(--y2)-var(--y1))*.8cqh));height:var(--stroke);transform-origin:left center;rotate:atan2(calc((var(--y2)-var(--y1))*.8cqh),calc((var(--x2)-var(--x1))*.8cqw));background:var(--n-4);}
$ .link.strong{background:var(--ink);height:2px;}
@container(max-width:650px){$ .node>.name{font-size:var(--type-12)}}
'''
D['code']='''
${display:flex;flex-direction:column;justify-content:center;gap:var(--gap-sm);padding:var(--pad);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);background:var(--n-1);}
$ .name{font-family:var(--font-body);font-size:var(--type-14);font-weight:var(--label-weight);line-height:var(--label-line);color:var(--n-7);}
$ .lines{font-family:var(--seedmark-code-font);font-size:var(--type-18);line-height:var(--body-line);counter-reset:line;min-height:0;}
$ .lines>p{white-space:pre-wrap;overflow-wrap:anywhere;position:relative;counter-increment:line;}
$.numbered .lines>p{padding-left:var(--pad);}
$.numbered .lines>p:before{content:counter(line);position:absolute;left:0;font-size:var(--type-12);line-height:var(--body-line);color:var(--n-7);}
$ .k{color:var(--a1-8);font-weight:var(--name-weight);}$ .s{color:var(--a3-8);}$ .c{color:var(--n-7);}$ .n{color:var(--a2-8);}
@container(max-width:650px){$ .lines{font-size:var(--type-14)}}@container(max-height:150px){$ .lines{font-size:var(--type-12)}$ .name{font-size:var(--type-10)}}
'''
# Structural count rules: the roots inspect only their own direct members.
for leaf,part,nmax in [('timeline','stop',12),('cycle','node',6),('hub','spoke',6),('pyramid','level',5),('hierarchy','branch',4),('logo-group','seat',12),('heatmap','row',12),('sankey','branch',6),('journey','stage',7),('mindmap','branch',6)]:
 D[leaf]+='\n'+'\n'.join('$:has(>.'+part+':nth-child('+str(n)+'):last-child){--seedmark-count:'+str(n)+';--seedmark-half:'+str((n+1)//2)+';}'for n in range(1,nmax+1))
for leaf,part,nmax in [('cycle','node',6),('hub','spoke',6)]:
 for n in range(3,nmax+1):
  for i in range(1,n+1):D[leaf]+=f'$:has(>.{part}:nth-child({n}):last-child)>.{part}:nth-child({i} of .{part}){{--seedmark-angle:{(i-1)*360/n}deg;}}\n'
for i in range(1,6):D['pyramid']+=f'$ .level:nth-child({i}){{--seedmark-index:{i};}}\n'
for n in range(3,9):
 for i in range(1,n+1):D['radar']+=f'$:has(>.axis:nth-child({n} of .axis)):not(:has(>.axis:nth-child({n+1} of .axis)))>.axis:nth-child({i} of .axis){{--seedmark-angle:{(i-1)*360/n}deg;}}\n'
 # Polygon geometry uses declared axis values; every vertex is data-driven.
 poly=','.join(f'calc(50% + sin({(i-1)*360/n}deg)*var(--v{i})/var(--max)*50%) calc(50% - cos({(i-1)*360/n}deg)*var(--v{i})/var(--max)*50%)'for i in range(1,n+1))
 D['radar']+=f'$:has(>.axis:nth-child({n} of .axis)):not(:has(>.axis:nth-child({n+1} of .axis))) .series:before{{clip-path:polygon({poly});}}\n'
# Complete files are written once from these independent definitions.
if __name__=='__main__':
 for k,v in list(D.items()):
  v=v.replace(')-',') - ').replace(')+',') + ')
  v=v.replace('1-var(', '1 - var(').replace('1-max(', '1 - max(').replace('100%-','100% - ')
  v=v.replace('}.col ', '}$.col ').replace('}.dumbbell ', '}$.dumbbell ')
  D[k]=v
 N.emit();print('Complete fresh CSS modules:',len(D));print('Missing:',set(N.FOLDERS.values())-set(D))
