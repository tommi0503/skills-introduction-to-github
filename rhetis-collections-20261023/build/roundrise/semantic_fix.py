from pathlib import Path
import json,math,re
B=Path('/workspace/output/roundrise/elements')
def add(e,s):p=B/e/'element.css';p.write_text(p.read_text()+'\n/* Contract functionality: final semantic review. */\n'+s+'\n')
def default(e,k,v):p=B/e/'element.json';j=json.loads(p.read_text());j['tokenDefaults'][k]=v;p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
add('journey','''
.journey[data-el="roundrise-journey"]{position:relative;isolation:isolate;--roundrise-journey-count:3;}
.journey[data-el="roundrise-journey"]>.stage::before{left:50%;bottom:calc(45% + var(--mood)*.4%);transform:translate(-50%,50%);z-index:3;}
.journey[data-el="roundrise-journey"]>.stage:not(:last-child)::after{left:50%;bottom:calc(45% + var(--mood)*.4%);width:hypot(calc((100cqw + var(--gap))/var(--roundrise-journey-count)),calc((var(--mood) - var(--next,var(--mood)))*.004*100cqh));height:2px;transform:rotate(atan2(calc((var(--mood) - var(--next,var(--mood)))*.004*100cqh),calc((100cqw + var(--gap))/var(--roundrise-journey-count))));transform-origin:left center;background:var(--a1);z-index:2;}
.journey[data-el="roundrise-journey"]>.stage>:is(.name,.note,.pain){position:relative;z-index:4;}
'''+''.join(f'.journey[data-el="roundrise-journey"]:has(>.stage:nth-child({n}):last-child){{--roundrise-journey-count:{n};}}' for n in range(4,8)))
default('journey','--roundrise-journey-count','3')
add('mindmap','''
.mindmap[data-el="roundrise-mindmap"]{isolation:isolate;}
.mindmap[data-el="roundrise-mindmap"]>.core{position:relative;z-index:2;}
.mindmap[data-el="roundrise-mindmap"]>.branch::before{right:auto;left:100%;top:50%;width:calc(60% + var(--gap));height:calc((100cqh + var(--gap))/3);background:none;border-top:var(--stroke) solid var(--a1-3-soft);border-right:var(--stroke) solid var(--a1-3-soft);border-radius:0 100% 0 0;z-index:-1;}
.mindmap[data-el="roundrise-mindmap"]>.branch:nth-child(3)::before{left:auto;right:100%;border-right:0;border-left:var(--stroke) solid var(--a1-3-soft);border-radius:100% 0 0 0;}
.mindmap[data-el="roundrise-mindmap"]>.branch:nth-child(4)::before{height:0;border-right:0;border-radius:0;}
.mindmap[data-el="roundrise-mindmap"]>.branch:nth-child(5)::before{left:auto;right:100%;height:0;border-right:0;border-radius:0;}
.mindmap[data-el="roundrise-mindmap"]>.branch:nth-child(6)::before{top:auto;bottom:50%;border-top:0;border-bottom:var(--stroke) solid var(--a1-3-soft);border-radius:0 0 100% 0;}
.mindmap[data-el="roundrise-mindmap"]>.branch:nth-child(7)::before{left:auto;right:100%;top:auto;bottom:50%;border-top:0;border-right:0;border-bottom:var(--stroke) solid var(--a1-3-soft);border-left:var(--stroke) solid var(--a1-3-soft);border-radius:0 0 0 100%;}
''')
add('sankey','''
.sankey[data-el="roundrise-sankey"]{position:relative;isolation:isolate;display:flex;flex-direction:column;gap:var(--gap-sm);padding:var(--gap-sm);padding-left:calc(28% + var(--gap));}
.sankey[data-el="roundrise-sankey"]>.source{position:absolute;left:var(--gap-sm);top:var(--gap-sm);bottom:var(--gap-sm);width:calc(28% - var(--gap-sm));align-self:auto;justify-content:center;z-index:1;}
.sankey[data-el="roundrise-sankey"]>.branch{flex:var(--v) 1 0;justify-content:space-between;min-height:0;z-index:0;}
.sankey[data-el="roundrise-sankey"]>.branch::before{right:50%;top:50%;transform:translateY(-50%);width:calc(50% + var(--gap) + 8cqw);height:60%;background:var(--a1-2-soft);z-index:-1;}
.sankey[data-el="roundrise-sankey"]>.branch.on::before{background:var(--a1);}.sankey[data-el="roundrise-sankey"]>.branch.out::before{background:var(--n-2);}
.sankey[data-el="roundrise-sankey"] .branch>.name{font-size:var(--type-22);}.sankey[data-el="roundrise-sankey"] .branch>.fig{font-size:var(--type-28);white-space:nowrap;}
.sankey[data-el="roundrise-sankey"]>.branch:has(>.branch){display:flex;flex-direction:column;align-items:stretch;padding:0;background:none;border-radius:0;gap:var(--gap-sm);}
.sankey[data-el="roundrise-sankey"]>.branch:has(>.branch)::before{right:100%;width:calc(var(--gap) + 8cqw);}
.sankey[data-el="roundrise-sankey"]>.branch:has(>.branch)::after{content:'';position:absolute;inset:0 auto 0 0;width:30%;background:var(--a1-1-soft);border-radius:var(--radius);z-index:-1;}
.sankey[data-el="roundrise-sankey"]>.branch.on:has(>.branch)::after{background:var(--a1);}
.sankey[data-el="roundrise-sankey"]>.branch:has(>.branch)>.name{position:absolute;left:0;top:calc(50% - var(--type-22)*var(--name-line));width:30%;padding:0 var(--gap-sm);text-align:center;color:var(--ink);}
.sankey[data-el="roundrise-sankey"]>.branch:has(>.branch)>.fig{position:absolute;left:0;top:50%;width:30%;padding:0 var(--gap-sm);text-align:center;color:var(--ink);}
.sankey[data-el="roundrise-sankey"]>.branch.on:has(>.branch)>:is(.name,.fig){color:var(--a1-on);}
.sankey[data-el="roundrise-sankey"]>.branch>.branch{flex:var(--v) 1 0;display:flex;align-items:center;justify-content:space-between;gap:var(--gap-sm);margin-left:calc(30% + var(--gap));padding:var(--gap-sm);position:relative;border:0;border-radius:var(--radius);background:var(--a1-1-soft);color:var(--ink);}
.sankey[data-el="roundrise-sankey"]>.branch>.branch::before{content:'';position:absolute;right:50%;top:50%;transform:translateY(-50%);width:calc(50% + var(--gap));height:60%;background:var(--a1-2-soft);z-index:-1;}
.sankey[data-el="roundrise-sankey"]>.branch>.branch.out{background:var(--n-2);}.sankey[data-el="roundrise-sankey"]>.branch>.branch.out::before{background:var(--n-2);}
@container(max-width:850px){.sankey[data-el="roundrise-sankey"] .branch>.name{font-size:var(--type-18);}.sankey[data-el="roundrise-sankey"] .branch>.fig{font-size:var(--type-24);}.sankey[data-el="roundrise-sankey"]>.branch:has(>.branch)>.name{top:calc(50% - var(--type-18)*var(--name-line));}}
''')
cy='''
.cycle[data-el="roundrise-cycle"]{display:block;padding:0;isolation:isolate;}
.cycle[data-el="roundrise-cycle"]::before{content:'';position:absolute;left:15%;top:16%;width:70%;height:68%;border:var(--stroke) solid var(--a1-3-soft);border-radius:50%;}
.cycle[data-el="roundrise-cycle"]>.core{position:absolute;left:50%;top:50%;width:min(30cqw,40cqh);height:auto;max-height:none;transform:translate(-50%,-50%);aspect-ratio:1;}
.cycle[data-el="roundrise-cycle"]>.node{position:absolute;width:24%;height:22%;transform:translate(-50%,-50%);padding:var(--gap-sm);}
.cycle[data-el="roundrise-cycle"]>.node::before{display:none;}.cycle[data-el="roundrise-cycle"]>.node::after{content:'';position:absolute;width:14px;height:12px;background:var(--a1);clip-path:polygon(0 0,100% 50%,0 100%);}
@container(max-height:350px){.cycle[data-el="roundrise-cycle"]>.node .name{font-size:var(--type-18);}.cycle[data-el="roundrise-cycle"]>.node .note{display:none;}.cycle[data-el="roundrise-cycle"]>.core{font-size:var(--type-20);padding:var(--gap-sm);}}
'''
for n in range(3,7):
 sel=f'.cycle[data-el="roundrise-cycle"]:has(>.node:nth-child({n+1}):last-child)'
 for i in range(n):
  a=-math.pi/2+2*math.pi*i/n;m=a+math.pi/n;c,s=math.cos(a),math.sin(a);mc,ms=math.cos(m),math.sin(m)
  cy+=f'{sel}>.node:nth-child({i+2}){{left:calc(50% + {c:.8f}*35%);top:calc(50% + {s:.8f}*34%);}}'
  cy+=f'{sel}>.node:nth-child({i+2})::after{{left:calc(50% + {mc-c:.8f}*35cqw);top:calc(50% + {ms-s:.8f}*34cqh);transform:translate(-50%,-50%) rotate(atan2(calc({mc:.8f}*34cqh),calc({-ms:.8f}*35cqw)));}}'
add('cycle',cy)
add('hierarchy','''
.org[data-el="roundrise-hierarchy"]{grid-auto-flow:row;grid-template-columns:repeat(2,minmax(0,1fr));grid-template-rows:auto auto;align-content:center;}
.org[data-el="roundrise-hierarchy"]:has(>.branch:nth-child(4):last-child){grid-template-columns:repeat(3,minmax(0,1fr));}.org[data-el="roundrise-hierarchy"]:has(>.branch:nth-child(5):last-child){grid-template-columns:repeat(4,minmax(0,1fr));}
.org[data-el="roundrise-hierarchy"]>.root::after{content:'';position:absolute;left:50%;top:100%;width:var(--stroke);height:calc(var(--gap-lg)/2);background:var(--a1-3-soft);}
.org[data-el="roundrise-hierarchy"]>.branch::before{top:calc(var(--gap-lg)/-2);height:calc(var(--gap-lg)/2);}
.org[data-el="roundrise-hierarchy"]>.branch::after{content:'';position:absolute;top:calc(var(--gap-lg)/-2);left:calc(var(--gap-lg)/-2);width:calc(100% + var(--gap-lg));height:var(--stroke);background:var(--a1-3-soft);}
.org[data-el="roundrise-hierarchy"]>.branch:nth-child(2)::after{left:50%;width:calc(50% + var(--gap-lg)/2);}.org[data-el="roundrise-hierarchy"]>.branch:last-child::after{width:calc(50% + var(--gap-lg)/2);}
.org[data-el="roundrise-hierarchy"]>.branch>.leaf{position:relative;}.org[data-el="roundrise-hierarchy"]>.branch>.leaf::before{content:'';position:absolute;left:50%;top:calc(var(--gap-sm)*-1);height:var(--gap-sm);width:var(--stroke);background:var(--a1-3-soft);}
''')
add('decision-tree','''
.dtree[data-el="roundrise-decision-tree"]{gap:var(--gap);}
.dtree[data-el="roundrise-decision-tree"] .q{z-index:1;}.dtree[data-el="roundrise-decision-tree"] .q::after{content:'';position:absolute;left:50%;top:100%;height:calc(var(--gap)/2);width:var(--stroke);background:var(--a1-3-soft);}
.dtree[data-el="roundrise-decision-tree"] .opts{position:relative;}.dtree[data-el="roundrise-decision-tree"] .opts::before{content:'';position:absolute;left:calc(25% - var(--gap)/4);width:calc(50% + var(--gap)/2);top:calc(var(--gap)/-2);height:var(--stroke);background:var(--a1-3-soft);}
.dtree[data-el="roundrise-decision-tree"] .opts:has(>.opt:nth-child(3))::before{left:calc(16.666667% - var(--gap)/3);width:calc(66.666667% + var(--gap)*2/3);}
.dtree[data-el="roundrise-decision-tree"] .opts>.opt::before{top:calc(var(--gap)/-2);height:calc(var(--type-16)*var(--label-line) + var(--gap)*1.5);}
.dtree[data-el="roundrise-decision-tree"] .opt>.cond{position:relative;z-index:1;align-self:center;width:max-content;max-width:100%;background:var(--page);padding:0 var(--gap-sm);line-height:var(--label-line);}
.dtree[data-el="roundrise-decision-tree"] .opt>.end{position:relative;z-index:1;}
@container(max-height:360px){.dtree[data-el="roundrise-decision-tree"] :is(.q,.end){padding:var(--gap-sm);}.dtree[data-el="roundrise-decision-tree"] .name{font-size:var(--type-18);}}
''')
add('slope','''
.slope[data-el="roundrise-slope"]:not(.dumbbell){padding:var(--pad);gap:var(--gap-sm);}
.slope[data-el="roundrise-slope"]:not(.dumbbell)>.pair{display:block;container-type:size;}
.slope[data-el="roundrise-slope"]:not(.dumbbell)>.pair>.name{position:absolute;left:50%;top:0;transform:translateX(-50%);padding:0 var(--gap-sm);font-size:var(--type-16);}
.slope[data-el="roundrise-slope"]:not(.dumbbell)>.pair>:is(.a,.b){position:absolute;left:5%;top:calc(var(--gap-sm) + (1 - var(--a)/var(--max))*(100% - var(--gap-sm)*2));transform:translate(-50%,-100%);font-size:var(--type-18);line-height:var(--figure-line);z-index:2;}
.slope[data-el="roundrise-slope"]:not(.dumbbell)>.pair>.b{left:95%;top:calc(var(--gap-sm) + (1 - var(--b)/var(--max))*(100% - var(--gap-sm)*2));}
.slope[data-el="roundrise-slope"]:not(.dumbbell)>.pair>:is(.a,.b)::after{content:'';position:absolute;left:calc(50% - 3px);top:calc(100% - 3px);width:6px;height:6px;border-radius:50%;background:var(--a1);}
.slope[data-el="roundrise-slope"]:not(.dumbbell)>.pair::before{left:5%;right:auto;top:calc(var(--gap-sm) + (1 - var(--a)/var(--max))*(100% - var(--gap-sm)*2));width:hypot(90cqw,calc((var(--a) - var(--b))/var(--max)*(100cqh - var(--gap-sm)*2)));height:var(--stroke);transform:rotate(atan2(calc((var(--a) - var(--b))/var(--max)*(100cqh - var(--gap-sm)*2)),90cqw));transform-origin:left center;}
@container(max-height:400px){.slope[data-el="roundrise-slope"]:not(.dumbbell){padding:var(--gap-sm);gap:calc(var(--gap-sm)/3);}.slope[data-el="roundrise-slope"]:not(.dumbbell)>.pair>.name{font-size:var(--type-12);}.slope[data-el="roundrise-slope"]:not(.dumbbell)>.pair>:is(.a,.b){font-size:var(--type-14);}}
''')
add('swimlane','''
.swimlane[data-el="roundrise-swimlane"]{padding-left:calc(var(--pad)*5);position:relative;}
.swimlane[data-el="roundrise-swimlane"]>.lane{position:relative;}
.swimlane[data-el="roundrise-swimlane"]>.lane>.name{position:absolute;right:calc(100% + var(--gap-sm));top:50%;width:calc(var(--pad)*4);transform:translateY(-50%);font-size:var(--type-16);text-align:right;}
@container(max-width:600px){.swimlane[data-el="roundrise-swimlane"]{padding-left:calc(var(--pad)*3);gap:var(--gap);}.swimlane[data-el="roundrise-swimlane"]>.lane>.name{width:calc(var(--pad)*2.5);font-size:var(--type-12);}.swimlane[data-el="roundrise-swimlane"]>.node::before{height:var(--gap);}.swimlane[data-el="roundrise-swimlane"]>.node::after{width:var(--gap);}}
''')
# Three sets need one real common intersection, and each set's name must remain visible.
v='''
.venn[data-el="roundrise-venn"]:has(>.set:nth-child(3)){display:block;}
.venn[data-el="roundrise-venn"]:has(>.set:nth-child(3))>.set{position:absolute;width:min(48cqw,56cqh);height:min(48cqw,56cqh);margin:0;aspect-ratio:1;transform:translate(-50%,-50%);}
.venn[data-el="roundrise-venn"]:has(>.set:nth-child(3))>.set:nth-child(1){left:42%;top:40%;align-items:flex-start;padding-top:var(--gap-lg);}
.venn[data-el="roundrise-venn"]:has(>.set:nth-child(3))>.set:nth-child(2){left:58%;top:40%;align-items:flex-start;padding-top:var(--gap-lg);}
.venn[data-el="roundrise-venn"]:has(>.set:nth-child(3))>.set:nth-child(3){left:50%;top:62%;align-items:flex-end;padding-bottom:var(--gap-lg);}
.venn[data-el="roundrise-venn"]:has(>.set:nth-child(3))>.core{left:43%;right:43%;top:46%;z-index:2;font-size:var(--type-16);}
'''
add('venn',v)
# Keep each stack series a distinct palette slot; fixture data owns its rank.
for f in (B/'chart-stack/fixtures').glob('*.html'):
 s=f.read_text();parts=re.split(r'(<div class="sbar[^"]*">)',s);new=[]
 for part in parts:
  if 'class="seg' in part:
   k=[0]
   def tone(m):
    k[0]+=1;cl=m.group(1);return 'class="seg'+(' '+cl if cl else '')+(f' tone-{k[0]}' if 'tone-' not in cl else '')+'"'
   part=re.sub(r'class="seg([^\"]*)"',tone,part)
  new.append(part)
 f.write_text(''.join(new))
add('chart-stack','.stacks[data-el="roundrise-chart-stack"].h>.sbar>span{width:calc(var(--pad)*3.5);}')
add('chart-area','.areas[data-el="roundrise-chart-area"].stacked>.series:nth-child(1 of .series){z-index:4;}.areas[data-el="roundrise-chart-area"].stacked>.series:nth-child(2 of .series){z-index:3;}.areas[data-el="roundrise-chart-area"].stacked>.series:nth-child(3 of .series){z-index:2;}.areas[data-el="roundrise-chart-area"].stacked>.series:nth-child(4 of .series){z-index:1;}')
p=B/'bullet/fixtures/bullets-4.html';p.write_text(p.read_text().replace('--v:104','--v:98').replace('104%','98%'))
p=B/'matrix-nine/fixtures/grid9-tones.html';s=p.read_text();s=s.replace('\n  <div class="cell','\n  <div class="axis-x"><span>낮음</span><span>중간</span><span>높음</span></div><div class="axis-y"><span>낮음</span><span>중간</span><span>높음</span></div>\n  <div class="cell',1);p.write_text(s)
w='''.waffle[data-el="roundrise-waffle"]{--roundrise-waffle-ratio:1;}.waffle[data-el="roundrise-waffle"]>.units{width:min(100%,calc(100cqh*var(--roundrise-waffle-ratio)));height:auto;aspect-ratio:var(--roundrise-waffle-ratio);align-self:center;justify-self:center;}'''
for rows in range(1,11):
 cond=f':has(>.units>.u:nth-child({(rows-1)*10+1}))'+(f':not(:has(>.units>.u:nth-child({rows*10+1})))' if rows<10 else '')
 w+=f'.waffle[data-el="roundrise-waffle"]{cond}{{--roundrise-waffle-ratio:{10/rows:.8f};}}'
add('waffle',w);default('waffle','--roundrise-waffle-ratio','1')
# A default sparkline is a line; only .bars produces bars.
s='''
.spark[data-el="roundrise-sparkline"]:not(.bars){display:grid;grid-auto-flow:column;grid-auto-columns:minmax(0,1fr);position:relative;gap:0;anchor-scope:all;}
.spark[data-el="roundrise-sparkline"]:not(.bars)>span{position:static;align-self:start;justify-self:center;width:0;height:0;min-height:0;border:0;background:none;border-radius:0;margin-top:calc((1 - var(--v)/var(--max))*100cqh);anchor-name:var(--roundrise-self);--roundrise-spark-vh:calc(100cqh*var(--v)/var(--max));}
.spark[data-el="roundrise-sparkline"]:not(.bars)>span::before{content:'';position:absolute;left:anchor(var(--roundrise-prev) center);right:anchor(var(--roundrise-self) center);top:calc(anchor(var(--roundrise-prev) top) - 100cqh);bottom:var(--gap-sm);clip-path:polygon(0 calc(100cqh - 1px),100% calc(100% - var(--roundrise-spark-vh) - 1px),100% calc(100% - var(--roundrise-spark-vh) + 1px),0 calc(100cqh + 1px));background:var(--a1);pointer-events:none;}
.spark[data-el="roundrise-sparkline"]:not(.bars)>span:first-child::before{display:none;}
.spark[data-el="roundrise-sparkline"]:not(.bars).up>span::before{background:var(--good);}.spark[data-el="roundrise-sparkline"]:not(.bars).down>span::before{background:var(--bad);}
.parts>.spark[data-el="roundrise-sparkline"]{height:calc(var(--gap-lg)*1.5);min-width:160px;width:100%;align-self:stretch;}
'''
for i in range(1,25):s+=f'.spark[data-el="roundrise-sparkline"]>span:nth-child({i}){{--roundrise-self:--roundrise-spark-{i};--roundrise-prev:--roundrise-spark-{i-1};}}'
add('sparkline',s)
p=B/'sparkline/fixtures/spark-in-stat.html';p.write_text(p.read_text().replace('min: 3x2','min: 3x3'))
print('Semantic fixes applied')
