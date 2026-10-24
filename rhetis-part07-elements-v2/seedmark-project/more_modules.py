"""Additional complete component definitions; no prior CSS is read."""
import new_library as N
D=N.CSS
D['chart-donut']='''
$.donuts{display:grid;grid-template-columns:repeat(var(--seedmark-count),minmax(0,1fr));gap:var(--gap);align-items:stretch;}
$.donuts>.donut{min-width:0;min-height:0;container-type:size;}
$.donut{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:calc(var(--gap-sm)/2);isolation:isolate;text-align:center;}
$.donut:after,$.donut:before{content:'';position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);border-radius:50%;pointer-events:none;}
$.donut:after{width:min(96cqw,96cqh);height:min(96cqw,96cqh);background:conic-gradient(var(--a1) calc(var(--v)*1%),var(--n-3) 0);z-index:-2;}
$.donut:before{width:min(76cqw,76cqh);height:min(76cqw,76cqh);background:var(--page);z-index:-1;}
$.donut>.fig{font-size:clamp(var(--type-20),min(12.68cqw,14cqh),var(--type-44));font-weight:var(--figure-weight);line-height:var(--name-line);max-width:75%;}
$.donut>.name{max-width:min(72cqw,64cqh);font-size:clamp(var(--type-12),min(4.2cqw,4.2cqh),var(--type-20));line-height:var(--label-line);font-weight:var(--label-weight);border:1px solid var(--ink);border-radius:var(--radius-sm);padding:calc(var(--gap-sm)/4) calc(var(--gap-sm)/2);background:var(--page);color:var(--ink);overflow-wrap:anywhere;}
$.donut>.fig small{font-size:var(--type-16);color:inherit;margin:0;}
'''
D['steps']='''
${display:grid;grid-template-columns:repeat(var(--seedmark-count),minmax(0,1fr));gap:var(--gap);isolation:isolate;}
$ .step{position:relative;min-width:0;display:grid;grid-template-rows:auto auto auto;align-content:center;justify-items:center;text-align:center;gap:var(--gap-sm);}
$ .mark{position:relative;width:min(92px,80cqw,35cqh);height:min(92px,80cqw,35cqh);display:flex;align-items:center;justify-content:center;border-radius:50%;background:var(--ink);color:var(--page);font-size:var(--type-26);font-weight:var(--figure-weight);line-height:var(--label-line);z-index:2;}
$ .mark>.icon{width:55%;height:55%;}
$ .name{font-size:var(--type-14);line-height:var(--label-line);font-weight:var(--label-weight);padding:calc(var(--gap-sm)/4) calc(var(--gap-sm)/2);border:1px solid var(--n-7);border-radius:var(--radius-sm);background:var(--page);color:var(--ink);z-index:3;}
$ .note{font-size:var(--type-16);line-height:var(--body-line);max-width:100%;word-break:keep-all;}
$ .step:not(:last-child):after{content:'';position:absolute;left:calc(50% + 46px);right:calc(-50% + 46px);top:calc(50% - 50px);height:8px;background:var(--n-5);clip-path:polygon(0 40%,85% 40%,85% 0,100% 50%,85% 100%,85% 60%,0 60%);}
$.col{grid-template-columns:1fr;grid-auto-rows:minmax(0,1fr);}
$.col .step{grid-template-columns:54px 28% minmax(0,1fr);grid-template-rows:1fr;justify-items:start;text-align:left;align-items:center;padding:var(--gap-sm);border:var(--stroke) solid var(--n-3);border-radius:999px;}
$.col .mark{width:54px;height:54px;}$.col .name{border:0;padding:0;font-size:var(--type-24);}$.col .note{font-size:var(--type-16);}
$.col .step:not(:last-child):after{left:50%;right:auto;top:100%;width:8px;height:var(--gap);clip-path:polygon(40% 0,60% 0,60% 85%,100% 85%,50% 100%,0 85%,40% 85%);}
@container(max-width:600px){$ .name{font-size:var(--type-12)}$ .note{font-size:var(--type-14)}$ .mark{width:60px;height:60px;font-size:var(--type-20)}}
@container(max-height:180px){$ .mark{width:48px;height:48px;}$ .note{font-size:var(--type-12)}$ .name{font-size:var(--type-10)}}
'''
D['flowchart']='''
${display:grid;grid-auto-columns:minmax(0,1fr);grid-auto-rows:minmax(0,1fr);gap:var(--gap-lg);padding:var(--gap-sm);}
$ .node{position:relative;min-width:0;min-height:0;display:flex;align-items:center;justify-content:center;text-align:center;border:var(--stroke) solid var(--n-3);border-radius:var(--radius);background:var(--page);padding:var(--gap-sm);}
$ .node .name{font-size:var(--type-20);font-weight:var(--name-weight);line-height:var(--name-line);}
$ .node.start,$ .node.end{border-radius:999px;background:var(--ink);color:var(--page);border-color:var(--ink);}
$ .node.ask{background:var(--a1-2-soft);border-color:var(--ink);}
$ .node.to-r:after,$ .node.to-l:after,$ .node.to-d:before,$ .node.to-u:before{content:'';position:absolute;background:var(--ink);pointer-events:none;z-index:3;}
$ .node.to-r:after{left:100%;top:50%;width:var(--gap-lg);height:8px;transform:translateY(-50%);clip-path:polygon(0 40%,85% 40%,85% 0,100% 50%,85% 100%,85% 60%,0 60%);}
$ .node.to-l:after{right:100%;top:50%;width:var(--gap-lg);height:8px;transform:translateY(-50%);clip-path:polygon(0 50%,15% 0,15% 40%,100% 40%,100% 60%,15% 60%,15% 100%);}
$ .node.to-d:before{top:100%;left:50%;width:8px;height:var(--gap-lg);transform:translateX(-50%);clip-path:polygon(40% 0,60% 0,60% 85%,100% 85%,50% 100%,0 85%,40% 85%);}
$ .node.to-u:before{bottom:100%;left:50%;width:8px;height:var(--gap-lg);transform:translateX(-50%);clip-path:polygon(50% 0,100% 15%,60% 15%,60% 100%,40% 100%,40% 15%,0 15%);}
$ .node>*{max-width:100%;max-height:100%;}
@container(max-width:700px){$ .node{padding:calc(var(--gap-sm)/2);}$ .node .name{font-size:var(--type-16)}}
@container(max-height:220px){$ .node .name{font-size:var(--type-14)}}
'''
D['agenda']='''
${display:grid;grid-template-columns:1fr;grid-auto-rows:minmax(0,1fr);padding:0;}
$ .entry{display:grid;grid-template-columns:26px minmax(0,1fr);align-content:center;gap:var(--gap-sm);border-top:var(--stroke) solid var(--n-3);padding:calc(var(--gap-sm)/2) 0;min-height:0;}
$ .mark{font-size:var(--type-14);line-height:var(--label-line);font-weight:var(--label-weight);}
$ .name{font-size:var(--type-24);line-height:var(--name-line);font-weight:var(--body-weight);}
$ .note{grid-column:2;font-size:var(--type-16);color:var(--n-7);line-height:var(--body-line);}
$ .entry.on{border-top:2px solid var(--ink);font-weight:var(--name-weight);}
$:has(>.entry:nth-child(7)){grid-template-columns:repeat(2,minmax(0,1fr));grid-template-rows:repeat(6,minmax(0,1fr));grid-auto-flow:column;column-gap:var(--gap-lg);}
@container(max-width:600px){$ .name{font-size:var(--type-18)}$ .note{font-size:var(--type-14)}}@container(max-height:220px){$ .name{font-size:var(--type-16)}$ .mark{font-size:var(--type-12)}}
'''
D['concentric']='''
${isolation:isolate;}
$ .ring{position:absolute;left:0;top:50%;transform:translateY(-50%);width:min(100cqw,100cqh);height:min(100cqw,100cqh);border-radius:50%;background:var(--ink);color:var(--page);display:flex;flex-direction:column;justify-content:center;align-items:flex-end;padding-right:var(--gap-sm);}
$ .ring:nth-child(2){width:min(70.4cqw,70.4cqh);height:min(70.4cqw,70.4cqh);background:var(--n-2);color:var(--ink);}
$ .ring:nth-child(3){width:min(47cqw,47cqh);height:min(47cqw,47cqh);background:var(--page);color:var(--ink);align-items:center;padding:0;}
$ .ring:nth-child(4){width:min(30cqw,30cqh);height:min(30cqw,30cqh);background:var(--a1-2-soft);color:var(--ink);align-items:center;padding:0;}
$ .ring .name,$ .ring .fig,$ .ring .note{width:23cqw;max-width:100%;text-align:center;}
$ .ring .name{font-size:clamp(var(--type-16),6.3cqw,var(--type-32));font-weight:var(--name-weight);line-height:var(--name-line);}
$ .ring .fig{font-size:clamp(var(--type-10),3cqw,var(--type-16));font-weight:var(--body-weight);line-height:var(--label-line);}
$ .ring .note{font-size:var(--type-12);line-height:var(--label-line);}
'''
D['positioning']='''
${background:var(--n-1);border-radius:var(--radius);padding:var(--gap);}
$:before,$:after{content:'';position:absolute;background:var(--n-4);}
$:before{left:50%;top:var(--gap-lg);bottom:var(--gap-lg);width:1px;}
$:after{top:50%;left:var(--gap-lg);right:var(--gap-lg);height:1px;}
$ .axis-x{position:absolute;left:var(--gap-sm);right:var(--gap-sm);top:50%;display:flex;justify-content:space-between;font-size:var(--type-12);color:var(--n-7);}
$ .axis-y{position:absolute;top:var(--gap-sm);bottom:var(--gap-sm);left:50%;display:flex;flex-direction:column;justify-content:space-between;text-align:center;font-size:var(--type-12);color:var(--n-7);transform:translateX(-50%);}
$ .mark{position:absolute;left:calc(var(--gap-lg)+(100cqw - var(--gap-lg)*2)*var(--x)/100);top:calc(var(--gap-lg)+(100cqh - var(--gap-lg)*2)*(1-var(--y)/100));transform:translate(-50%,-50%);width:48px;height:48px;border-radius:50%;background:var(--n-3);display:flex;align-items:center;justify-content:center;z-index:1;}
$ .mark>.name{position:absolute;top:calc(100% + var(--gap-sm)/2);left:50%;transform:translateX(-50%);font-size:var(--type-10);line-height:var(--label-line);font-weight:var(--label-weight);text-align:center;width:110px;}
$ .mark.on{width:min(159px,32cqw);height:min(84px,18cqh);border-radius:999px;background:var(--ink);color:var(--page);}
$ .mark.on>.name{position:static;transform:none;width:auto;max-width:100%;font-size:var(--type-16);padding:var(--gap-sm);}
$ .mark>.seat{width:100%;height:100%;border-radius:inherit;}
@container(max-width:400px){$ .mark{width:32px;height:32px;}$ .mark>.name{font-size:var(--type-8);width:72px;}$ .mark.on>.name{font-size:var(--type-12)}}
'''
D['venn']='''
${display:flex;align-items:center;justify-content:center;padding:var(--gap-sm);isolation:isolate;}
$ .set{position:absolute;top:50%;width:min(65cqw,90cqh);height:min(65cqw,90cqh);border:var(--stroke) solid var(--page);border-radius:50%;background:var(--n-2);display:flex;align-items:center;justify-content:center;padding:var(--gap);transform:translateY(-50%);}
$ .set:first-child{left:0;}$ .set:nth-child(2){right:0;}
$ .set>.name{font-size:var(--type-20);font-weight:var(--name-weight);line-height:var(--name-line);position:relative;z-index:3;text-align:center;}
$ .core{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:25%;height:25%;display:flex;align-items:center;justify-content:center;border-radius:50%;background:var(--page);font-size:var(--type-18);line-height:var(--name-line);font-weight:var(--name-weight);text-align:center;z-index:4;}
$:has(>.set:nth-child(3)){--seedmark-diameter:min(52cqw,64cqh);}
$:has(>.set:nth-child(3))>.set{width:var(--seedmark-diameter);height:var(--seedmark-diameter);border:8px solid var(--page);}
$:has(>.set:nth-child(3))>.set:nth-child(1){left:50%;top:0;transform:translateX(-50%);align-items:flex-start;padding-top:var(--gap-lg);}
$:has(>.set:nth-child(3))>.set:nth-child(2){left:calc(50% - var(--seedmark-diameter)*.8);right:auto;top:calc(var(--seedmark-diameter)*.55);transform:none;align-items:flex-end;justify-content:flex-start;padding-bottom:var(--gap-lg);}
$:has(>.set:nth-child(3))>.set:nth-child(3){left:calc(50% - var(--seedmark-diameter)*.2);top:calc(var(--seedmark-diameter)*.55);transform:none;align-items:flex-end;justify-content:flex-end;padding-bottom:var(--gap-lg);}
$:has(>.set:nth-child(3)):before{content:'';position:absolute;left:calc(50% - var(--seedmark-diameter)*.5);top:0;width:var(--seedmark-diameter);height:var(--seedmark-diameter);border-radius:50%;background:var(--ink);mask-image:radial-gradient(circle calc(var(--seedmark-diameter)*.5) at 20% 105%,var(--ink) 99%,transparent),radial-gradient(circle calc(var(--seedmark-diameter)*.5) at 80% 105%,var(--ink) 99%,transparent);z-index:1;}
$:has(>.set:nth-child(3)):after{content:'';position:absolute;left:calc(50% - var(--seedmark-diameter)*.8);top:calc(var(--seedmark-diameter)*.55);width:var(--seedmark-diameter);height:var(--seedmark-diameter);border-radius:50%;background:var(--ink);mask-image:radial-gradient(circle calc(var(--seedmark-diameter)*.5) at 110% 50%,var(--ink) 99%,transparent);z-index:1;}
$ .set:after{content:'';position:absolute;inset:0;border:8px solid var(--page);border-radius:50%;z-index:2;pointer-events:none;}
@container(max-width:500px){$ .set>.name{font-size:var(--type-16)}$ .core{font-size:var(--type-14)}}
'''
D['person']='''
$.people{display:flex;align-items:stretch;gap:var(--gap);}
$.people>.person{flex:1;min-width:0;min-height:0;container-type:size;}
$.person{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:calc(var(--gap-sm)/2);text-align:center;padding:var(--gap-sm);}
$.person>.seat{width:min(95cqw,52cqh);height:min(95cqw,52cqh);aspect-ratio:1;border:8px solid var(--n-2);flex:none;}
$.person>.seat.avatar{border-radius:50%;}$.person>.seat.portrait{border-radius:var(--radius);height:min(118cqw,52cqh);}
$.person>.name{font-size:clamp(var(--type-16),min(14cqw,7.4cqh),var(--type-28));font-weight:var(--name-weight);line-height:var(--name-line);}
$.person>.note{font-size:var(--type-14);line-height:var(--label-line);color:var(--n-7);}
$.person>.list{width:100%;min-height:0;}
@container(max-width:250px){$ .person>.note{font-size:var(--type-12)}}
'''
D['image-frame']='''
${display:flex;align-items:center;justify-content:center;padding:var(--gap-sm);border:var(--stroke) solid var(--n-3);border-radius:var(--radius);background:var(--page);}
$>.seat{width:min(100cqw - var(--gap-sm)*2,100cqh - var(--gap-sm)*2);height:min(100cqw - var(--gap-sm)*2,100cqh - var(--gap-sm)*2);aspect-ratio:1;border-radius:var(--radius-sm);}
'''
D['chart-bar']='''
${display:flex;align-items:stretch;gap:var(--gap-sm);padding:var(--pad) var(--gap) var(--gap-lg);isolation:isolate;}
$:before{content:'';position:absolute;inset:var(--pad) var(--gap) var(--gap-lg);background:repeating-linear-gradient(to top,var(--n-3) 0 1px,transparent 1px 20%);z-index:-1;}
$ .bar{position:relative;flex:1;min-width:0;min-height:0;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;}
$ .bar:before{content:'';position:absolute;bottom:0;width:70%;height:calc(var(--v)/var(--max)*100%);border-radius:var(--radius-sm) var(--radius-sm) 0 0;background:var(--n-4);}
$ .bar.on:before,$ .bar.tone-1:before{background:var(--a1)}$ .bar.tone-2:before{background:var(--a2)}$ .bar.tone-3:before{background:var(--a3)}$ .bar.tone-4:before{background:var(--a4)}$ .bar.tone-5:before{background:var(--n-3)}
$ .bar>b{position:absolute;left:50%;bottom:calc(var(--v)/var(--max)*100% + var(--gap-sm)/2);transform:translateX(-50%);font-size:var(--type-16);font-weight:var(--figure-weight);line-height:var(--label-line);white-space:nowrap;}
$ .bar>span{position:absolute;left:50%;top:100%;transform:translateX(-50%);font-size:var(--type-12);line-height:var(--label-line);padding-top:var(--gap-sm);white-space:nowrap;}
$.h{flex-direction:column;padding:var(--gap) var(--gap-lg);}
$.h:before{display:none}$.h .bar{display:block;margin-left:calc(var(--pad)*2);margin-right:var(--gap);}
$.h .bar:before{left:0;top:20%;bottom:20%;width:calc(var(--v)/var(--max)*100%);height:auto;border-radius:0 var(--radius-sm) var(--radius-sm) 0;}
$.h .bar>span{left:auto;right:calc(100% + var(--gap-sm));top:50%;transform:translateY(-50%);padding:0;}
$.h .bar>b{left:calc(var(--v)/var(--max)*100% + var(--gap-sm));bottom:auto;top:50%;transform:translateY(-50%);}
@container(max-width:650px){$ .bar>b{font-size:var(--type-12)}$ .bar>span{font-size:var(--type-10)}$ .bar:nth-child(even):not(:last-child)>span{visibility:hidden;}$.h .bar>span{visibility:visible;}}
'''
# Add member-count inference only from the element's own direct children.
for leaf,part,maximum in [('chart-donut','donut',8),('steps','step',10),('timeline','stop',10),('logos','seat',12)]:
 if leaf not in D:continue
 D[leaf]+='\n'+'\n'.join('$:has(>.'+part+':nth-child('+str(n)+'):last-child){--seedmark-count:'+str(n)+';}'for n in range(1,maximum+1))
if __name__=='__main__':N.emit();print('Fresh modules emitted:',len(D))
