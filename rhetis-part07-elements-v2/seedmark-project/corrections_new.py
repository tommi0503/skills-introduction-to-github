"""First browser-review corrections to the new definitions, before whole-file emission."""
def apply(D):
 D['balance']=D['balance'].replace('top:50%;height:var(--stroke);background:var(--n-5);rotate:calc(var(--tilt)*-.12deg);','top:68%;height:var(--stroke);background:var(--n-5);rotate:calc(var(--tilt)*.12deg);').replace('translateY(calc(var(--tilt)*-.18%))','translateY(calc(var(--tilt)*-.12cqh))').replace('translateY(calc(var(--tilt)*.18%))','translateY(calc(var(--tilt)*.12cqh))').replace('bottom:10%;height:20%;','bottom:12%;height:20%;')
 # Text rows occupy a compact consistent block. All members in a row share these tracks.
 D['card']+='''
$ .parts:has(>.mark):not(:has(>.kick,>.fig)){height:min(100%,calc(var(--pad)*9));align-self:center;grid-template-rows:54px calc(var(--type-20)*2.8) minmax(0,1fr);align-content:stretch;}
$ .parts:has(>.mark):not(:has(>.kick,>.fig))>.name{grid-row:2;align-self:start;}
$ .parts:has(>.mark):not(:has(>.kick,>.fig))>.note{grid-row:3;align-self:start;}
$.quiet .parts:has(>.mark):not(:has(>.kick)){height:100%;grid-template-rows:auto auto;align-content:center;}
$.quiet .parts:has(>.mark):not(:has(>.kick))>.name{grid-row:2;align-self:center;}
$.quiet .parts:has(>.kick):not(:has(>.mark,>.fig,>.list)){height:min(100%,calc(var(--pad)*7));align-self:center;grid-template-rows:24px minmax(0,1fr);align-content:stretch;}
$ .parts:has(>.note:nth-child(2 of .note)){height:min(100%,calc(var(--pad)*9));align-self:center;grid-template-columns:minmax(0,1fr);grid-template-rows:20px 56px minmax(0,1fr) minmax(0,auto);align-content:stretch;}
$ .parts:has(>.note:nth-child(2 of .note))>.kick{grid-column:1;grid-row:1;}
$ .parts:has(>.note:nth-child(2 of .note))>.name{grid-column:1;grid-row:2;border-bottom:var(--stroke) solid var(--n-3);}
$ .parts:has(>.note:nth-child(2 of .note))>.note:nth-child(1 of .note){grid-column:1;grid-row:3;align-self:start;}
$ .parts:has(>.note:nth-child(2 of .note))>.note:nth-child(2 of .note){grid-column:1;grid-row:4;align-self:end;font-weight:var(--name-weight);font-size:var(--type-16);}
'''
 # Member names are separate legend columns, not overlaid labels.
 D['chart-area']+='\n'+''.join(f'$:has(>.series:nth-child({n} of .series)):not(:has(>.series:nth-child({n+1} of .series))){{--seedmark-series-count:{n};}}'for n in range(1,5))
 for i in range(1,5):D['chart-area']+=f'$ .series:nth-child({i} of .series)>.name{{left:calc(({i}-1)*100%/var(--seedmark-series-count));max-width:calc(100%/var(--seedmark-series-count) - var(--gap-sm));}}'
 # A compact nested bar leaves a full text track above the datum band.
 D['bullet']+='''
@container(max-height:100px){$.bullet .name{font-size:var(--type-12);line-height:var(--label-line);align-self:start;}$.bullet .fig{font-size:var(--type-14);line-height:var(--label-line);align-self:start;}$.bullet .note{font-size:var(--type-10);line-height:var(--label-line);align-self:start;}}
'''
 # Padding is part of the root box; reduce nested root overhead instead of hiding its numbers.
 D['bullet']=D['bullet'].replace('padding:var(--gap-sm) var(--gap-sm) var(--gap-lg);','padding:calc(var(--gap-sm)/3) var(--gap-sm) calc(var(--gap-sm)*2);').replace('gap:var(--gap-sm);padding:calc(var(--gap-sm)/3)','gap:calc(var(--gap-sm)/3);padding:calc(var(--gap-sm)/3)')
 D['gauge']=D['gauge'].replace('grid-template-rows:auto 12px;','grid-template-rows:auto;').replace('gap:var(--gap-sm);padding:var(--gap-sm);','gap:calc(var(--gap-sm)/2);padding:calc(var(--gap-sm)/3) var(--gap-sm) calc(var(--gap-sm)*2);')
 D['gauge']+='\n@container(max-height:100px){$ .name{font-size:var(--type-12);line-height:var(--label-line);}$ .fig{font-size:var(--type-14);line-height:var(--label-line);}}'
 D['chart-bar']=D['chart-bar'].replace('margin-left:calc(var(--pad)*2);','margin-left:calc(var(--pad)*5.5);').replace('padding:0;}\n$.h .bar>b','padding:0;max-width:calc(var(--pad)*5);white-space:normal;text-align:right;overflow-wrap:anywhere;}\n$.h .bar>b')
 D['chart-donut']+='\n@container(max-width:120px){$.donut>.fig{font-size:var(--type-16);}$.donut>.fig small{font-size:var(--type-10);}$.donut>.name{font-size:var(--type-8);}$.donut>.name>.tag{font-size:var(--type-8);}}'
 D['concentric']=D['concentric'].replace('width:23cqw;max-width:100%;','width:calc(min(100cqw,100cqh)*.23);max-width:100%;')
 D['concentric']+='\n$:has(>.ring:nth-child(2)):not(:has(>.ring:nth-child(3)))>.ring:nth-child(2){align-items:center;padding:0;}\n'
 D['flowchart']+='\n$ .node>.group,$ .node>.stack{width:100%;height:100%;}\n$ .node:has(>.group,>.stack){border:0;background:none;padding:0;}'
 # Calendar cells remain square in wide slots as well as tall ones.
 D['heatmap']+='''
$.calendar{grid-template-rows:auto repeat(var(--seedmark-count),minmax(0,1fr));align-content:center;}
$.calendar .heads,$.calendar .row{width:calc(var(--seedmark-cell)*var(--cols) + var(--gap-sm)/2*(var(--cols) - 1));justify-self:center;grid-template-columns:repeat(var(--cols),var(--seedmark-cell));}
$.calendar .row{height:var(--seedmark-cell);align-self:center;}
$.calendar .cell{aspect-ratio:1;}
$.calendar .heads,$.calendar .row{--seedmark-cell:min(calc((100cqw - var(--gap-sm)/2*(var(--cols) - 1))/var(--cols)),calc((100cqh - var(--type-12)*var(--label-line) - var(--gap-sm)/2*var(--seedmark-count))/var(--seedmark-count)));}
'''
 # Each stat's own container governs its figure and name columns.
 D['metric']+='''
@container(max-width:300px){$ .parts{grid-template-columns:1fr;grid-template-rows:auto auto auto;gap:calc(var(--gap-sm)/3);}$ .fig{grid-column:1;grid-row:1;font-size:var(--type-28);}$ .name{grid-column:1;grid-row:2;}$ .note{grid-column:1;grid-row:3;font-size:var(--type-14);}}
@container(max-height:100px){$ .parts{grid-template-columns:auto minmax(0,1fr);grid-template-rows:auto auto;gap:calc(var(--gap-sm)/6) calc(var(--gap-sm)/2);}$ .fig{grid-column:1;grid-row:1/span 2;font-size:var(--type-20);align-self:center;}$ .name{grid-column:2;grid-row:1;font-size:var(--type-12);}$ .note{grid-column:2;grid-row:2;font-size:var(--type-10);}}
'''
 D['metric']=D['metric'].replace('align-items:center;padding:var(--gap);border-right','align-items:center;padding:calc(var(--gap-sm)/2);border-right')
 D['radar']=D['radar'].replace('left:0;top:calc(var(--gap-lg)*-1);','left:0;top:calc(var(--gap-lg)*-1);width:100%;')
 D['radar']+='\n$ .series>.name{transform:none;white-space:normal;}\n'
 D['sankey']=D['sankey'].replace('min-height:64px;','min-height:0;').replace('flex-direction:column;justify-content:center;gap:calc(var(--gap-sm)/2);padding:var(--gap-sm);background:var(--n-1);','flex-direction:row;align-items:center;justify-content:space-between;gap:calc(var(--gap-sm)/2);padding:calc(var(--gap-sm)/2);background:var(--n-1);')
 D['sankey']+='\n@container(max-height:400px){$ .branch{padding:calc(var(--gap-sm)/3);}$ .name{font-size:var(--type-12);}$ .fig{font-size:var(--type-16);}}'
 # The curve owns all stages and uses the declared next mood for both directions and flat steps.
 start=D['journey'].index('$ .stage:before{');end=D['journey'].index('$ .stage.on:after')
 D['journey']=D['journey'][:start]+'''
$ .stage:before{content:'';position:absolute;left:50%;width:calc(100% + var(--gap));top:12%;height:35%;background:var(--n-5);clip-path:polygon(0 calc((1 - var(--mood)/100)*100%),100% calc((1 - var(--next,var(--mood))/100)*100%),100% calc((1 - var(--next,var(--mood))/100)*100% + 2px),0 calc((1 - var(--mood)/100)*100% + 2px));}
$ .stage:last-child:before{display:none;}
$ .stage:after{content:'';position:absolute;left:50%;top:calc(12% + (1 - var(--mood)/100)*35%);width:8px;height:8px;transform:translate(-50%,-50%);border-radius:50%;background:var(--n-5);}
'''+D['journey'][end:]
 D['hub']=D['hub'].replace('$ .core{position:absolute;','$ .core{z-index:2;position:absolute;').replace('width:100%;height:var(--stroke);background:var(--n-3);transform-origin:left center;transform:rotate(calc(var(--seedmark-angle) + 90deg));','width:hypot(calc(sin(var(--seedmark-angle))*35cqw),calc(cos(var(--seedmark-angle))*35cqh));height:var(--stroke);background:var(--n-3);transform-origin:left center;transform:rotate(atan2(calc(cos(var(--seedmark-angle))*35cqh),calc(-1*sin(var(--seedmark-angle))*35cqw)));')
 D['swimlane']+='''
$ .node.to-l:after{content:'';position:absolute;right:100%;top:50%;width:var(--gap);height:8px;transform:translateY(-50%);background:var(--n-5);clip-path:polygon(100% 40%,20% 40%,20% 0,0 50%,20% 100%,20% 60%,100% 60%);}
$ .node.to-u:before{content:'';position:absolute;bottom:100%;left:50%;height:var(--gap);width:8px;transform:translateX(-50%);background:var(--n-5);clip-path:polygon(40% 100%,60% 100%,60% 20%,100% 20%,50% 0,0 20%,40% 20%);}
'''
