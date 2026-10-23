from pathlib import Path
import json
C=Path('/workspace/output/cyanloop/elements')
def add(n,s):
 p=C/n/'element.css';p.write_text(p.read_text()+'\n/* Functional geometry and readable layers, final cross-review. */\n'+s+'\n')
def defaults(n,values):
 p=C/n/'element.json';d=json.loads(p.read_text());d['tokenDefaults'].update(values);p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
add('slope','''
.slope[data-el="cyanloop-slope"]:not(.dumbbell) .pair{container-type:size;isolation:isolate;}
.slope[data-el="cyanloop-slope"]:not(.dumbbell) .pair::before{left:12%;right:auto;top:calc(15% + (1 - var(--a)/var(--max))*70%);width:hypot(76cqw,calc((var(--a) - var(--b))/var(--max)*70cqh));height:2px;transform:rotate(atan2(calc((var(--a) - var(--b))/var(--max)*70cqh),76cqw));transform-origin:left center;}
.slope[data-el="cyanloop-slope"]:not(.dumbbell) .pair .name{left:50%;top:0;transform:translateX(-50%);white-space:nowrap;font-size:var(--type-14);}
.slope[data-el="cyanloop-slope"]:not(.dumbbell) .pair .a,.slope[data-el="cyanloop-slope"]:not(.dumbbell) .pair .b{position:absolute;left:12%;top:calc(15% + (1 - var(--a)/var(--max))*70%);transform:translate(-50%,-50%);font-size:var(--type-14);padding:0 var(--gap-sm);white-space:nowrap;}
.slope[data-el="cyanloop-slope"]:not(.dumbbell) .pair .b{left:88%;top:calc(15% + (1 - var(--b)/var(--max))*70%);}
''')
add('bullet','''
:is(.bullet[data-el="cyanloop-bullet"],.bullets[data-el="cyanloop-bullet"]).bullet{grid-template-rows:auto auto var(--gap);align-content:center;}
:is(.bullet[data-el="cyanloop-bullet"],.bullets[data-el="cyanloop-bullet"]).bullet>.name{grid-column:1;grid-row:1;}
:is(.bullet[data-el="cyanloop-bullet"],.bullets[data-el="cyanloop-bullet"]).bullet>.fig{grid-column:2;grid-row:1;}
:is(.bullet[data-el="cyanloop-bullet"],.bullets[data-el="cyanloop-bullet"]).bullet>.note{grid-row:2;}
:is(.bullet[data-el="cyanloop-bullet"],.bullets[data-el="cyanloop-bullet"]).bullet::before{display:none;}
:is(.bullet[data-el="cyanloop-bullet"],.bullets[data-el="cyanloop-bullet"]).bullet::after{grid-row:3;grid-column:1/-1;height:var(--gap);border-radius:var(--radius-sm);background:linear-gradient(to right,color-mix(in srgb,var(--page) 0%,var(--ink) 0.001%) calc(min(98,var(--target)) * 1% - 1px),var(--ink) 0 calc(min(98,var(--target)) * 1% + 1px),color-mix(in srgb,var(--page) 0%,var(--ink) 0.001%) 0) center/100% 100% no-repeat,linear-gradient(to right,var(--a1-7) calc(min(100,var(--v))*1%),color-mix(in srgb,var(--page) 0%,var(--ink) 0.001%) 0) center/100% 6px no-repeat,linear-gradient(to right,var(--n-2) calc(var(--low,60)*1%),var(--n-3) 0 calc(var(--high,85)*1%),var(--n-4) 0);}
''')
add('tag','''
:is(.tag[data-el="cyanloop-tag"],.hl[data-el="cyanloop-tag"]){container-type:normal;width:max-content;max-width:100%;white-space:normal;}
''')
add('waffle','''
.waffle[data-el="cyanloop-waffle"]{display:grid;grid-template-columns:minmax(0,1fr);grid-template-rows:minmax(0,1fr) auto auto;justify-items:center;align-content:stretch;}
.waffle[data-el="cyanloop-waffle"] .units{grid-row:1;width:100%;height:100%;max-height:none;grid-auto-rows:minmax(0,1fr);align-items:center;min-height:0;}
.waffle[data-el="cyanloop-waffle"] .u{display:block;aspect-ratio:1;width:100%;height:auto;max-height:100%;min-height:0;}
.waffle[data-el="cyanloop-waffle"] .u.tone-3{background:var(--a3);}
.waffle[data-el="cyanloop-waffle"]>.fig{grid-row:2;}
.waffle[data-el="cyanloop-waffle"]>.name{grid-row:3;text-align:center;}
.waffle[data-el="cyanloop-waffle"].figures{grid-template-columns:3fr 1fr;grid-template-rows:minmax(0,1fr) minmax(0,1fr);}
.waffle[data-el="cyanloop-waffle"].figures .units{grid-row:1/3;}
.waffle[data-el="cyanloop-waffle"].figures>.fig{grid-row:1;}
.waffle[data-el="cyanloop-waffle"].figures>.name{grid-row:2;}
.waffle[data-el="cyanloop-waffle"].figures .u{aspect-ratio:.5;}
''')
add('venn','''
.venn[data-el="cyanloop-venn"]:has(>.set:nth-child(3)) .set:nth-child(2) .name{align-self:flex-start;margin-top:var(--gap-lg);}
''')
add('swimlane','''
.swimlane[data-el="cyanloop-swimlane"]:has(>.lane){padding-left:calc(var(--pad)*4);grid-template-rows:repeat(2,minmax(0,1fr));}
.swimlane[data-el="cyanloop-swimlane"]:has(>.lane:nth-child(3)){grid-template-rows:repeat(3,minmax(0,1fr));}
.swimlane[data-el="cyanloop-swimlane"] .lane{position:relative;}
.swimlane[data-el="cyanloop-swimlane"] .lane>.name{position:absolute;left:calc(0px - var(--pad)*3);top:var(--gap-sm);width:calc(var(--pad)*3 - var(--gap-sm));text-align:center;z-index:3;}
''')
add('radar','''
.radar[data-el="cyanloop-radar"] .axis{z-index:3;pointer-events:none;}
.radar[data-el="cyanloop-radar"] .axis .name{position:relative;z-index:4;}
''')
add('table','''
.tablebox[data-el="cyanloop-table"]:not(.on) .table{color:var(--ink);}
.tablebox[data-el="cyanloop-table"]:not(.on) td{color:var(--ink);}
''')
# Nine matrix cells indexed independently of axes; both fixture variations expose axes.
p=C/'matrix-nine/fixtures/grid9-tones.html';s=p.read_text();s=s.replace('  <div class="cell tone-3">','  <div class="axis-y"><span>낮음</span><span>보통</span><span>높음</span></div>\n  <div class="cell tone-3">',1);s=s.replace('\n</div>','\n  <div class="axis-x"><span>낮음</span><span>보통</span><span>높음</span></div>\n</div>');p.write_text(s)
s=''
for i in range(1,10):s+=f'.grid9[data-el="cyanloop-matrix-nine"] .cell:nth-child({i} of .cell){{grid-column:{2+(i-1)%3};grid-row:{1+(i-1)//3};}}\n'
add('matrix-nine',s)
# Area labels use the exact same 0..100 percent x positions as the fill polygon.
s='''
.areas[data-el="cyanloop-chart-area"] .series .pt{position:absolute;width:0;top:0;bottom:0;left:0;height:100%;flex:none;}
.areas[data-el="cyanloop-chart-area"] .series .pt b{left:0;transform:translateX(-50%);white-space:nowrap;}
.areas[data-el="cyanloop-chart-area"] .axis{justify-content:space-between;}
.areas[data-el="cyanloop-chart-area"] .axis span:first-child{transform:translateX(-50%);}
.areas[data-el="cyanloop-chart-area"] .axis span:last-child{transform:translateX(50%);}
.areas[data-el="cyanloop-chart-area"].stacked .series{mix-blend-mode:normal;}
.areas[data-el="cyanloop-chart-area"].stacked .series:nth-child(1){z-index:3;}
.areas[data-el="cyanloop-chart-area"].stacked .series:nth-child(2){z-index:2;}
.areas[data-el="cyanloop-chart-area"].stacked .series:nth-child(3){z-index:1;}
.areas[data-el="cyanloop-chart-area"].stacked .series::before{opacity:1;}
'''
for n in range(2,13):
 for i in range(1,n+1):s+=f'.areas[data-el="cyanloop-chart-area"] .series:has(>.pt:nth-of-type({n}):last-child) .pt:nth-of-type({i}){{left:{(i-1)/(n-1)*100:.6f}%;}}\n'
# axis children width0 so text centers directly on each vertex.
s+='''.areas[data-el="cyanloop-chart-area"] .axis>span{width:0;text-align:center;white-space:nowrap;transform:translateX(-50%);}
.areas[data-el="cyanloop-chart-area"] .axis>span:last-child{transform:translateX(-50%);}
'''
# zero-width spans cannot center their inline text; use each explicit position and translate intrinsic box.
s+='''.areas[data-el="cyanloop-chart-area"] .axis>span{position:absolute;width:max-content;transform:translateX(-50%);bottom:0;}
'''
for n in range(2,13):
 for i in range(1,n+1):s+=f'.areas[data-el="cyanloop-chart-area"] .axis:has(>span:nth-child({n}):last-child)>span:nth-child({i}){{left:{(i-1)/(n-1)*100:.6f}%;}}\n'
add('chart-area',s)
# Base hub connections point to the actual core centre; source variants retain measured geometry.
s=''
# branch -> centre dx(C/2+gap) and dy(row pitch); root box padding/gap both gap-sm.
dx='calc((100cqw + 2*var(--gap-sm))/6)';dy='calc((100cqh - var(--gap-sm))/3)'
base='.hub[data-el="cyanloop-hub"]:not(.quiet):not(.line):not(.on)'
s+=f'{base} .spoke::before{{left:100%;right:auto;top:50%;width:{dx};height:1px;background:var(--n-4);transform-origin:left center;z-index:0;}}\n'
for i,signx,signy in [(2,1,1),(3,-1,1),(4,-1,0),(5,-1,-1),(6,1,-1),(7,1,0)]:
 x=f'calc({signx} * (100cqw + 2*var(--gap-sm))/6)';y=f'calc({signy} * (100cqh - var(--gap-sm))/3)'
 s+=f'{base} .spoke:nth-child({i})::before{{left:{"100%" if signx==1 else "0"};right:auto;width:hypot({x},{y});transform:rotate(atan2({y},{x}));}}\n'
add('hub',s)
print('Applied functional corrections to 11 element folders')
