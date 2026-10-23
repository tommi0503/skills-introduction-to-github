from pathlib import Path
import json
base=Path('/workspace/output/cyanloop/elements')
patches={
'journey':r'''
/* Emotion segments use the actual distance between the following stage centres. */
.journey[data-el="cyanloop-journey"]{isolation:isolate;--cyanloop-journey-count:3;}
.journey[data-el="cyanloop-journey"]:has(>.stage:nth-child(4):last-child){--cyanloop-journey-count:4;}
.journey[data-el="cyanloop-journey"]:has(>.stage:nth-child(5):last-child){--cyanloop-journey-count:5;}
.journey[data-el="cyanloop-journey"]:has(>.stage:nth-child(6):last-child){--cyanloop-journey-count:6;}
.journey[data-el="cyanloop-journey"]:has(>.stage:nth-child(7):last-child){--cyanloop-journey-count:7;}
.journey[data-el="cyanloop-journey"]>.stage::before{left:50%;top:calc(45% - var(--mood) * .3%);transform:translate(-50%,-50%);z-index:3;}
.journey[data-el="cyanloop-journey"]>.stage:not(:last-child)::after{left:50%;top:calc(45% - var(--mood) * .3%);height:2px;width:hypot(calc((100cqw - var(--gap-sm)) / var(--cyanloop-journey-count)),calc((var(--mood) - var(--next,var(--mood))) * .003 * (100cqh - 2 * var(--gap-sm))));transform:rotate(atan2(calc((var(--mood) - var(--next,var(--mood))) * .003 * (100cqh - 2 * var(--gap-sm))),calc((100cqw - var(--gap-sm)) / var(--cyanloop-journey-count))));transform-origin:left center;z-index:2;}
.journey[data-el="cyanloop-journey"]>.stage>:is(.name,.note,.pain){position:relative;z-index:4;}
''',
'mindmap':r'''
/* Each curved branch reaches the centre, underneath the central capsule. */
.mindmap[data-el="cyanloop-mindmap"]{isolation:isolate;}
.mindmap[data-el="cyanloop-mindmap"]>.core{position:relative;z-index:2;}
.mindmap[data-el="cyanloop-mindmap"]>.branch::before{content:'';position:absolute;left:100%;top:50%;width:calc(50% + var(--gap-sm));height:calc((100cqh - var(--gap-sm)) / 3);border-top:var(--stroke) solid var(--a1);border-right:var(--stroke) solid var(--a1);border-top-right-radius:100%;z-index:-1;}
.mindmap[data-el="cyanloop-mindmap"]>.branch:nth-child(3)::before{left:auto;right:100%;border-right:0;border-left:var(--stroke) solid var(--a1);border-radius:100% 0 0 0;}
.mindmap[data-el="cyanloop-mindmap"]>.branch:nth-child(4)::before{height:0;border-right:0;border-radius:0;}
.mindmap[data-el="cyanloop-mindmap"]>.branch:nth-child(5)::before{left:auto;right:100%;height:0;border-right:0;border-radius:0;}
.mindmap[data-el="cyanloop-mindmap"]>.branch:nth-child(6)::before{top:auto;bottom:50%;border-top:0;border-bottom:var(--stroke) solid var(--a1);border-radius:0 0 100% 0;}
.mindmap[data-el="cyanloop-mindmap"]>.branch:nth-child(7)::before{left:auto;right:100%;top:auto;bottom:50%;border-top:0;border-right:0;border-bottom:var(--stroke) solid var(--a1);border-left:var(--stroke) solid var(--a1);border-radius:0 0 0 100%;}
''',
'hierarchy':r'''
/* The root stem joins one rail, whose drops meet every branch node. */
.org[data-el="cyanloop-hierarchy"]>.root::after{height:calc(var(--gap) / 2);}
.org[data-el="cyanloop-hierarchy"]>.branch::before{top:calc(0px - var(--gap) / 2);height:calc(var(--gap) / 2);}
.org[data-el="cyanloop-hierarchy"]>.branch::after{content:'';position:absolute;top:calc(0px - var(--gap) / 2);left:calc(0px - var(--gap-sm) / 2);width:calc(100% + var(--gap-sm));height:var(--stroke);background:var(--n-4);}
.org[data-el="cyanloop-hierarchy"]>.branch:nth-child(2)::after{left:50%;width:calc(50% + var(--gap-sm) / 2);}
.org[data-el="cyanloop-hierarchy"]>.branch:last-child::after{width:calc(50% + var(--gap-sm) / 2);}
.org[data-el="cyanloop-hierarchy"]>.branch>.leaf{position:relative;}
.org[data-el="cyanloop-hierarchy"]>.branch>.leaf::before{content:'';position:absolute;left:50%;top:calc(0px - var(--gap-sm));width:var(--stroke);height:var(--gap-sm);background:var(--n-4);}
@container(max-height:350px){.org[data-el="cyanloop-hierarchy"]>.branch>.leaf::before{top:calc(0px - var(--gap-sm) / 2);height:calc(var(--gap-sm) / 2);}}
''',
'decision-tree':r'''
/* Recursive question groups share a continuous branching rail at every depth. */
.dtree[data-el="cyanloop-decision-tree"]{gap:var(--gap);}
.dtree[data-el="cyanloop-decision-tree"] .q{z-index:1;}
.dtree[data-el="cyanloop-decision-tree"] .q::after{height:calc(var(--gap) / 2);}
.dtree[data-el="cyanloop-decision-tree"] .opts{position:relative;}
.dtree[data-el="cyanloop-decision-tree"] .opts::before{content:'';position:absolute;left:calc(25% - var(--gap) / 4);width:calc(50% + var(--gap) / 2);top:calc(0px - var(--gap) / 2);height:var(--stroke);background:var(--n-4);}
.dtree[data-el="cyanloop-decision-tree"] .opts:has(>.opt:nth-child(3))::before{left:calc(16.666667% - var(--gap) / 3);width:calc(66.666667% + var(--gap) * 2 / 3);}
.dtree[data-el="cyanloop-decision-tree"] .opts>.opt::before{content:'';position:absolute;left:50%;top:calc(0px - var(--gap) / 2);width:var(--stroke);height:calc(var(--type-16) * var(--label-line) + var(--gap) * 1.5);background:var(--n-4);}
.dtree[data-el="cyanloop-decision-tree"] .opt>.cond{position:relative;z-index:1;width:max-content;max-width:100%;align-self:center;background:var(--page);padding:0 var(--gap-sm);line-height:var(--label-line);}
.dtree[data-el="cyanloop-decision-tree"] .opt>.end{position:relative;z-index:1;}
@container(max-width:650px){.dtree[data-el="cyanloop-decision-tree"] .opts>.opt::before{height:calc(var(--type-12) * var(--label-line) + var(--gap) * 1.5);}}
''',
'sankey':r'''
/* Parallel source bands keep a common proportional thickness, including nested splits. */
.sankey[data-el="cyanloop-sankey"]{display:flex;flex-direction:column;position:relative;isolation:isolate;padding:var(--gap-sm);padding-left:calc(26% + var(--gap));gap:calc(var(--gap-sm) / 2);}
.sankey[data-el="cyanloop-sankey"]>.source{position:absolute;left:var(--gap-sm);top:var(--gap-sm);bottom:var(--gap-sm);width:calc(26% - var(--gap-sm));padding:var(--gap-sm);z-index:1;}
.sankey[data-el="cyanloop-sankey"]>.branch{flex:var(--v) 1 0;min-height:0;border-radius:999px;position:relative;padding:calc(var(--gap-sm) / 2) var(--gap-sm);z-index:0;}
.sankey[data-el="cyanloop-sankey"]>.branch::before{right:100%;top:50%;transform:translateY(-50%);width:calc(var(--gap) + 12cqw);height:calc(var(--v) * .006 * (100cqh - 2 * var(--gap-sm)));background:var(--a1-2-soft);z-index:-1;}
.sankey[data-el="cyanloop-sankey"]>.branch.on::before{background:var(--a1);}
.sankey[data-el="cyanloop-sankey"]>.branch.out::before{background:var(--n-2);}
.sankey[data-el="cyanloop-sankey"] .branch>.name{font-size:var(--type-16);flex:1;}
.sankey[data-el="cyanloop-sankey"] .branch>.fig{font-size:var(--type-24);flex:none;white-space:nowrap;}
.sankey[data-el="cyanloop-sankey"]:has(>.branch>.branch){padding-left:calc(21% + var(--gap));gap:var(--gap-sm);}
.sankey[data-el="cyanloop-sankey"]:has(>.branch>.branch)>.source{width:calc(21% - var(--gap-sm));}
.sankey[data-el="cyanloop-sankey"]>.branch:has(>.branch){display:grid;grid-template-columns:30% 1fr;gap:calc(var(--gap-sm) / 2) var(--gap);padding:0;background:none;color:var(--ink);border-radius:0;}
.sankey[data-el="cyanloop-sankey"]>.branch:has(>.branch)::after{content:'';position:absolute;left:0;top:0;bottom:0;width:30%;background:var(--a1-2-soft);border-radius:var(--radius);z-index:-1;}
.sankey[data-el="cyanloop-sankey"]>.branch.on:has(>.branch)::after{background:var(--a1);}
.sankey[data-el="cyanloop-sankey"]>.branch:has(>.branch)>.name{position:absolute;left:0;top:calc(50% - var(--type-16) * var(--name-line));width:30%;padding:0 var(--gap-sm);text-align:center;}
.sankey[data-el="cyanloop-sankey"]>.branch:has(>.branch)>.fig{position:absolute;left:0;top:50%;width:30%;padding:0 var(--gap-sm);text-align:center;}
.sankey[data-el="cyanloop-sankey"]>.branch.on:has(>.branch)>:is(.name,.fig){color:var(--a1-on);}
.sankey[data-el="cyanloop-sankey"]>.branch>.branch{grid-column:2;display:flex;position:relative;min-height:0;padding:calc(var(--gap-sm) / 2) var(--gap-sm);gap:calc(var(--gap-sm) / 2);background:var(--a1-2-soft);color:var(--ink);}
.sankey[data-el="cyanloop-sankey"]>.branch>.branch::before{width:var(--gap);right:100%;top:50%;transform:translateY(-50%);height:calc(var(--v) * .008 * (100cqh - 2 * var(--gap-sm)) * .38);background:var(--a1-2-soft);z-index:-1;}
.sankey[data-el="cyanloop-sankey"]>.branch>.branch.out{background:var(--n-2);}
.sankey[data-el="cyanloop-sankey"]>.branch>.branch.out::before{background:var(--n-2);}
@container(max-width:650px){.sankey[data-el="cyanloop-sankey"] .branch>.name{font-size:var(--type-14);}.sankey[data-el="cyanloop-sankey"] .branch>.fig{font-size:var(--type-20);}.sankey[data-el="cyanloop-sankey"]>.branch:has(>.branch)>.name{top:calc(50% - var(--type-14) * var(--name-line));}}
@container(max-height:350px){.sankey[data-el="cyanloop-sankey"] .branch>.name{font-size:var(--type-14);}.sankey[data-el="cyanloop-sankey"] .branch>.fig{font-size:var(--type-20);}.sankey[data-el="cyanloop-sankey"]>.branch:has(>.branch)>.name{top:calc(50% - var(--type-14) * var(--name-line));}}
'''
}
for e,css in patches.items():
 p=base/e/'element.css';p.write_text(p.read_text()+'\n'+css)
p=base/'journey/element.json';j=json.loads(p.read_text());j['tokenDefaults']['--cyanloop-journey-count']='3';p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print('Patched',list(patches))
