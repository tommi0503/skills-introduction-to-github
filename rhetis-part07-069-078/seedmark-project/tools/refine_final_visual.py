"""One final functional CSS patch after inspecting all 56 light/dark element sheets.
Does not regenerate fixture data, metadata, runtime, or any other source files.
"""
from pathlib import Path
P=Path(__file__).parent;C=P/'seedmark';E=C/'elements';MARK='/* FINAL_FUNCTIONAL_REVIEW */'
backup=P/'local-review/final-css-before';backup.mkdir(parents=True,exist_ok=True)
def patch(rel,css):
 p=C/rel;old=p.read_text();safe=old.split(MARK)[0]
 dest=backup/rel;dest.parent.mkdir(parents=True,exist_ok=True)
 if not dest.exists():dest.write_text(old)
 p.write_text(safe+'\n'+MARK+'\n'+css+'\n')
patch('elements/chart-donut/element.css','''
[data-el="seedmark-chart-donut"].donut{position:relative;width:100%;height:100%;max-height:100%;max-width:100%;aspect-ratio:auto;align-self:stretch;justify-self:stretch;background:none;border-radius:0;isolation:isolate;}
[data-el="seedmark-chart-donut"].donut:after{content:'';position:absolute;left:50%;top:50%;width:min(90cqw,90cqh);height:min(90cqw,90cqh);transform:translate(-50%,-50%);border-radius:50%;background:conic-gradient(var(--a1) calc(var(--v)*1%),var(--n-3) 0);z-index:-2;}
[data-el="seedmark-chart-donut"].donut:before{content:'';position:absolute;inset:auto;left:50%;top:50%;width:min(68.4cqw,68.4cqh);height:min(68.4cqw,68.4cqh);transform:translate(-50%,-50%);border-radius:50%;background:var(--page);z-index:-1;}
[data-el="seedmark-chart-donut"].donuts>.donut{width:calc((100cqw - var(--gap)*(var(--seedmark-count) - 1))/var(--seedmark-count));height:90%;aspect-ratio:auto;flex:none;align-self:center;}
[data-el="seedmark-chart-donut"] .name{max-width:min(70cqw,55cqh);}
[data-el="seedmark-chart-donut"] small{color:inherit;margin:0;}
''')
# Untoned data series need ranked default colors; explicit tone classes retain precedence.
stack=''
for i in range(1,6):
 color=('var(--a3-7)' if i==3 else 'var(--a'+str(i)+')')if i<5 else'var(--n-3)';ink='var(--a'+str(i)+'-on)'if i<5 else'var(--ink)'
 stack+=f'[data-el="seedmark-chart-stack"] .seg:nth-child({i} of .seg):not(.tone-1,.tone-2,.tone-3,.tone-4,.tone-5)'+'{background:'+color+';color:'+ink+';}\n'
stack+='[data-el="seedmark-chart-stack"] .seg.tone-3{background:var(--a3-7);color:var(--a3-on);}'
patch('elements/chart-stack/element.css',stack)
area=''
for i in range(1,5):
 area+=f'[data-el="seedmark-chart-area"] .series:nth-child({i} of .series):not(.tone-1,.tone-2,.tone-3,.tone-4) .pt:before'+'{background:color-mix(in srgb,var(--a'+str(i)+') 35%,transparent);}\n'
 area+=f'[data-el="seedmark-chart-area"] .series:nth-child({i} of .series)>.name:before'+'{content:\'\';display:inline-block;width:8px;height:8px;background:var(--a'+str(i)+');margin-right:calc(var(--gap-sm)/2);}\n'
patch('elements/chart-area/element.css',area)
grid=''
for i in range(9):grid+=f'[data-el="seedmark-matrix-nine"] .cell:nth-child({i+1} of .cell)'+'{grid-column:'+str(2+i%3)+';grid-row:'+str(1+i//3)+';}\n'
patch('elements/matrix-nine/element.css',grid)
patch('elements/radar/element.css','''
[data-el="seedmark-radar"] .series,[data-el="seedmark-radar"] .series.tone-1,[data-el="seedmark-radar"] .series.tone-2,[data-el="seedmark-radar"] .series.tone-3{background:none;border:0;inset:auto;left:50%;top:50%;width:min(64cqw,64cqh);height:min(64cqw,64cqh);transform:translate(-50%,-50%);}
[data-el="seedmark-radar"]:before{inset:auto;left:50%;top:50%;width:min(64cqw,64cqh);height:min(64cqw,64cqh);transform:translate(-50%,-50%);}
[data-el="seedmark-radar"] .axis{left:calc(50% + sin(var(--seedmark-angle))*min(43cqw,43cqh));top:calc(50% - cos(var(--seedmark-angle))*min(40cqw,40cqh));}
[data-el="seedmark-radar"] .series>.name{top:calc(var(--gap-lg)*-2);font-size:var(--type-12);}
''')
journey='''[data-el="seedmark-journey"]{--seedmark-journey-count:3;}
[data-el="seedmark-journey"] .stage:not(:last-child):after{left:50%;top:calc(35% - var(--mood)*.25%);bottom:auto;right:auto;z-index:3;width:calc(hypot(calc((100cqw + var(--gap-sm))/var(--seedmark-journey-count)),calc((var(--mood) - var(--next))*.25cqh)));height:var(--stroke);background:var(--n-4);transform-origin:left center;transform:rotate(atan2(calc((var(--mood) - var(--next))*.25cqh),calc((100cqw + var(--gap-sm))/var(--seedmark-journey-count))));}
'''
for i in range(3,8):journey+=f'[data-el="seedmark-journey"]:has(>.stage:nth-child({i}):last-child)'+'{--seedmark-journey-count:'+str(i)+';}\n'
patch('elements/journey/element.css',journey)
patch('elements/slope/element.css','''
[data-el="seedmark-slope"]:not(.dumbbell) .pair:before{background:linear-gradient(to top right,transparent calc(50% - 1px),var(--n-5) calc(50% - 1px),var(--n-5) calc(50% + 1px),transparent calc(50% + 1px));}
[data-el="seedmark-slope"]:not(.dumbbell) .pair:after{background:linear-gradient(to bottom right,transparent calc(50% - 1px),var(--n-5) calc(50% - 1px),var(--n-5) calc(50% + 1px),transparent calc(50% + 1px));}
''')
patch('elements/steps/element.css','''
[data-el="seedmark-steps"]{padding:var(--gap-sm);}
[data-el="seedmark-steps"]:not(.col) .step{display:grid;grid-template-rows:minmax(0,1fr) calc(var(--pad)*2) minmax(0,1fr);gap:var(--gap-sm);align-content:stretch;justify-items:center;}
[data-el="seedmark-steps"]:not(.col) .step>.mark{grid-row:1;align-self:end;}
[data-el="seedmark-steps"]:not(.col) .step>.name{grid-row:2;align-self:start;}
[data-el="seedmark-steps"]:not(.col) .step>.note{grid-row:3;align-self:start;}
[data-el="seedmark-steps"]:not(.col) .step:not(:last-child):after{top:calc((100% - var(--pad)*2 - var(--gap-sm)*2)/2 - 38px);}
[data-el="seedmark-steps"].col .mark{justify-self:center;}
@container(max-height:250px){[data-el="seedmark-steps"]:not(.col) .step{grid-template-rows:minmax(0,1fr) calc(var(--pad)*1.5) minmax(0,1fr);gap:calc(var(--gap-sm)/2);}[data-el="seedmark-steps"]:not(.col) .step:not(:last-child):after{top:calc((100% - var(--pad)*1.5 - var(--gap-sm))/2 - 27px);}}
''')
patch('elements/image-frame/element.css','''
[data-el="seedmark-image-frame"].frame{width:100%;height:100%;background:var(--page);}
[data-el="seedmark-image-frame"] .seat{width:min(100cqw,100cqh);height:min(100cqw,100cqh);max-width:100%;max-height:100%;aspect-ratio:1;flex:none;}
''')
patch('foundation/foundation.css','''
.stack>.seat{flex:none;width:min(160px,35cqh);height:min(160px,35cqh);max-width:100%;max-height:100%;aspect-ratio:1;align-self:center;}
.cover .lockup>.lead{margin-top:var(--gap-sm);}
''')
# Retain a single root-to-branch path in both halves of a mind map.
mind='''[data-el="seedmark-mindmap"]{transform:translate(0);anchor-scope:all;}
[data-el="seedmark-mindmap"] .core{anchor-name:--seedmark-mind-core;}
[data-el="seedmark-mindmap"] .branch:before,[data-el="seedmark-mindmap"] .branch:after{content:'';position:fixed;pointer-events:none;z-index:-1;width:auto;height:auto;margin:0;border:0;background:none;left:anchor(var(--seedmark-mind-self) right);right:anchor(--seedmark-mind-core left);}
[data-el="seedmark-mindmap"] .branch:before{top:anchor(var(--seedmark-mind-self) center);bottom:anchor(--seedmark-mind-core center);border-top:var(--stroke) solid var(--n-3);border-right:var(--stroke) solid var(--n-3);border-radius:0 50% 0 0;}
[data-el="seedmark-mindmap"] .branch:after{top:anchor(--seedmark-mind-core center);bottom:anchor(var(--seedmark-mind-self) center);border-bottom:var(--stroke) solid var(--n-3);border-right:var(--stroke) solid var(--n-3);border-radius:0 0 50% 0;}
[data-el="seedmark-mindmap"] .branch:nth-child(even):before,[data-el="seedmark-mindmap"] .branch:nth-child(even):after{left:anchor(--seedmark-mind-core right);right:anchor(var(--seedmark-mind-self) left);}
[data-el="seedmark-mindmap"] .branch:nth-child(even):before{border-right:0;border-left:var(--stroke) solid var(--n-3);border-radius:50% 0 0 0;}
[data-el="seedmark-mindmap"] .branch:nth-child(even):after{border-right:0;border-left:var(--stroke) solid var(--n-3);border-radius:0 0 0 50%;}
'''
for i in range(1,7):mind+=f'[data-el="seedmark-mindmap"] .branch:nth-child({i} of .branch)'+'{--seedmark-mind-self:--seedmark-mind-'+str(i)+';anchor-name:--seedmark-mind-'+str(i)+';}\n'
mind+='''@container(max-height:420px){[data-el="seedmark-mindmap"] .branch{padding:calc(var(--gap-sm)/2);gap:calc(var(--gap-sm)/4);}[data-el="seedmark-mindmap"] .branch>.name{font-size:var(--type-16);line-height:var(--name-line);}[data-el="seedmark-mindmap"] .branch>.note{font-size:var(--type-12);line-height:var(--body-line);}}'''
patch('elements/mindmap/element.css',mind)
patch('elements/hierarchy/element.css','[data-el="seedmark-hierarchy"] .branch{justify-content:flex-start;}')
patch('elements/positioning/element.css','''[data-el="seedmark-positioning"] .axis-x{writing-mode:horizontal-tb;}[data-el="seedmark-positioning"] .axis-x>span{writing-mode:vertical-rl;}''')
# Actual line sparklines use data-derived anchor connectors; .bars keeps the compact bars.
spark='''[data-el="seedmark-sparkline"]{transform:translate(0);anchor-scope:all;}
[data-el="seedmark-sparkline"]:not(.bars)>span{position:static;background:none;border:0;}
[data-el="seedmark-sparkline"].up{color:var(--good);}[data-el="seedmark-sparkline"].down{color:var(--bad);}
[data-el="seedmark-sparkline"]:not(.bars)>span:before,[data-el="seedmark-sparkline"]:not(.bars)>span:after{content:'';position:fixed;pointer-events:none;left:anchor(var(--seedmark-spark-prev) center);right:anchor(var(--seedmark-spark-self) center);}
[data-el="seedmark-sparkline"]:not(.bars)>span:before{top:calc(anchor(var(--seedmark-spark-prev) top) - 1px);bottom:calc(anchor(var(--seedmark-spark-self) top) - 1px);background:linear-gradient(to top right,transparent calc(50% - 1px),currentColor calc(50% - 1px),currentColor calc(50% + 1px),transparent calc(50% + 1px));}
[data-el="seedmark-sparkline"]:not(.bars)>span:after{top:calc(anchor(var(--seedmark-spark-self) top) - 1px);bottom:calc(anchor(var(--seedmark-spark-prev) top) - 1px);background:linear-gradient(to bottom right,transparent calc(50% - 1px),currentColor calc(50% - 1px),currentColor calc(50% + 1px),transparent calc(50% + 1px));}
[data-el="seedmark-sparkline"]:not(.bars)>span:first-child:before,[data-el="seedmark-sparkline"]:not(.bars)>span:first-child:after{content:none;}
'''
for i in range(1,25):spark+=f'[data-el="seedmark-sparkline"]>span:nth-child({i})'+'{--seedmark-spark-self:--seedmark-spark-'+str(i)+';--seedmark-spark-prev:--seedmark-spark-'+str(i-1)+';anchor-name:--seedmark-spark-'+str(i)+';}\n'
patch('elements/sparkline/element.css',spark)
patch('elements/treemap/element.css','''
[data-el="seedmark-treemap"] .tile{container-type:size;padding:calc(var(--gap-sm)/6);gap:0;position:relative;}
@container(max-height:80px){[data-el="seedmark-treemap"] .tile>.name{font-size:var(--type-12);line-height:var(--label-line)}[data-el="seedmark-treemap"] .tile>.fig{font-size:var(--type-16);line-height:var(--figure-line)}}
@container(max-width:90px){[data-el="seedmark-treemap"] .tile>.name{font-size:var(--type-12);line-height:var(--label-line)}[data-el="seedmark-treemap"] .tile>.fig{font-size:var(--type-16);line-height:var(--figure-line)}}
@container(max-height:45px){[data-el="seedmark-treemap"] .tile>.name{position:absolute;left:var(--gap-sm);top:50%;transform:translateY(-50%);font-size:var(--type-12);white-space:nowrap;}[data-el="seedmark-treemap"] .tile>.fig{position:absolute;right:var(--gap-sm);top:50%;transform:translateY(-50%);font-size:var(--type-14);white-space:nowrap;}}
''')
patch('elements/venn/element.css','''
[data-el="seedmark-venn"]:not(:has(>.set:nth-child(3))) .set{width:min(45cqw,84cqh);height:auto;max-height:none;aspect-ratio:1;flex:none;}
[data-el="seedmark-venn"]:has(>.core):has(>.set:nth-child(3)) .set{width:min(52cqw,72cqh);height:min(52cqw,72cqh);aspect-ratio:1;max-height:none;padding:var(--gap);}
[data-el="seedmark-venn"]:has(>.core):has(>.set:nth-child(3)) .set:nth-child(1){left:50%;right:auto;top:2%;bottom:auto;transform:translateX(-50%);justify-content:flex-start;padding-top:var(--gap-lg);}
[data-el="seedmark-venn"]:has(>.core):has(>.set:nth-child(3)) .set:nth-child(2){left:calc(50% - min(46.8cqw,64.8cqh));right:auto;top:auto;bottom:2%;transform:none;justify-content:center;align-items:flex-start;}
[data-el="seedmark-venn"]:has(>.core):has(>.set:nth-child(3)) .set:nth-child(3){left:calc(50% - min(5.2cqw,7.2cqh));right:auto;top:auto;bottom:2%;transform:none;justify-content:center;align-items:flex-end;}
''')
patch('elements/swimlane/element.css','''[data-el="seedmark-swimlane"]{padding-left:calc(var(--pad)*3);}[data-el="seedmark-swimlane"] .lane{position:relative;}[data-el="seedmark-swimlane"] .lane>.name{position:absolute;right:calc(100% + var(--gap-sm));top:50%;transform:translateY(-50%);width:calc(var(--pad)*2);max-width:none;font-size:var(--type-14);text-align:center;writing-mode:horizontal-tb;}''')
patch('elements/cycle/element.css','''[data-el="seedmark-cycle"]:after{content:'';position:absolute;left:78%;right:auto;top:71%;width:8px;height:8px;border-bottom:var(--stroke) solid var(--ink);border-right:var(--stroke) solid var(--ink);transform:translate(-50%,-50%) rotate(90deg);}''')
patch('elements/card/element.css','''@container(max-height:300px){[data-el="seedmark-card"] .parts>.mark>.icon{width:20px;height:20px;}}''')
patch('elements/heatmap/element.css','''[data-el="seedmark-heatmap"].calendar .cell{aspect-ratio:auto;min-height:0;}[data-el="seedmark-heatmap"].calendar .row{grid-template-columns:repeat(var(--cols),minmax(0,1fr));}[data-el="seedmark-heatmap"].calendar .heads{margin-left:0;}''')
patch('elements/waffle/element.css','''
[data-el="seedmark-waffle"]{padding:var(--gap-sm);gap:var(--gap-sm);}
[data-el="seedmark-waffle"] .units{width:min(440px,60cqh,100%);}
[data-el="seedmark-waffle"].figures{padding:calc(var(--gap-sm)/2);gap:calc(var(--gap-sm)/4);}
[data-el="seedmark-waffle"].figures .units{width:min(440px,100%);gap:calc(var(--gap-sm)/4);}
[data-el="seedmark-waffle"].figures .name small{display:block;font-size:var(--type-12);line-height:var(--label-line);}
@container(max-height:110px){[data-el="seedmark-waffle"].figures .units{max-width:210px;}[data-el="seedmark-waffle"].figures .name{font-size:var(--type-12);line-height:var(--label-line);}[data-el="seedmark-waffle"].figures .name small{font-size:var(--type-10);}[data-el="seedmark-waffle"].figures .fig{font-size:var(--type-20);}}
''')
# A one-row golden fixture contains two figure-waffles. Foundation makes that compact stack a row.
p=C/'foundation/foundation.css';s=p.read_text();p.write_text(s+'\n.stack:has(>[data-el="seedmark-waffle"].figures){flex-direction:row;gap:var(--gap-sm);align-items:stretch;}\n')
patch('elements/person/element.css','''
[data-el="seedmark-person"].person>.seat{width:min(144px,28cqh);height:min(144px,28cqh);max-height:none;flex:none;}
[data-el="seedmark-person"].person>.seat.portrait{height:min(180px,35cqh);}
[data-el="seedmark-person"].person>.list{height:auto;min-height:0;flex:none;line-height:var(--body-line);padding-left:var(--gap);margin:0;}
@container(max-height:300px){[data-el="seedmark-person"] .note{font-size:var(--type-12);}[data-el="seedmark-person"] .name{font-size:var(--type-20);}[data-el="seedmark-person"] .list{font-size:var(--type-12);}}
''')
patch('elements/funnel/element.css','''
[data-el="seedmark-funnel"] .stage{container-type:size;flex-direction:column;padding:calc(var(--gap-sm)/3);gap:0;justify-content:center;}
[data-el="seedmark-funnel"] .stage>.name{font-size:var(--type-18);line-height:var(--label-line);max-width:85%;white-space:nowrap;}
[data-el="seedmark-funnel"] .stage>.fig{font-size:var(--type-24);line-height:var(--figure-line);white-space:nowrap;}
@container(max-width:150px){[data-el="seedmark-funnel"] .stage>.name{font-size:var(--type-12);}[data-el="seedmark-funnel"] .stage>.fig{font-size:var(--type-16);}}
@container(max-height:65px){[data-el="seedmark-funnel"] .stage>.name{font-size:var(--type-12);}[data-el="seedmark-funnel"] .stage>.fig{font-size:var(--type-16);}}
''')
patch('elements/pyramid/element.css','''
[data-el="seedmark-pyramid"] .level{container-type:size;}
[data-el="seedmark-pyramid"] .level>.note{display:block;font-size:var(--type-12);line-height:var(--label-line);}
[data-el="seedmark-pyramid"] .level:first-child{justify-content:flex-end;padding:var(--gap-sm) calc(var(--gap-sm)/3) calc(var(--gap-sm)/3);}
[data-el="seedmark-pyramid"] .level:first-child>.name{font-size:var(--type-14);line-height:var(--label-line);white-space:nowrap;}
[data-el="seedmark-pyramid"] .level:first-child>.note{font-size:var(--type-12);line-height:var(--label-line);white-space:nowrap;}
@container(max-height:65px){[data-el="seedmark-pyramid"] .level:first-child>.name{font-size:var(--type-12);}[data-el="seedmark-pyramid"] .level:first-child>.note{font-size:var(--type-10);}}
''')
print('Patched final functional CSS only; fixtures, metadata, source palette and runtime preserved.')
