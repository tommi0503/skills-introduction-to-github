from pathlib import Path
import re
C=Path('/workspace/output/cyanloop');W=Path('/workspace/work/cyanloop')
def css(folder,s):
 p=C/'elements'/folder/'element.css';p.write_text(p.read_text()+'\n'+s)
css('agenda','''
.agenda[data-el="cyanloop-agenda"].quiet .entry>.note .list{height:calc(4 * var(--type-20) * var(--name-line) + var(--gap-sm));}
.agenda[data-el="cyanloop-agenda"].quiet.line{background:var(--a1-7);}
''')
css('card','''
.card[data-el="cyanloop-card"].on.quiet .note .list{height:calc(6 * var(--gap));}
.card[data-el="cyanloop-card"].quiet.line .kick,.card[data-el="cyanloop-card"].on.line .kick{color:var(--n-7);}
''')
css('hub','''
.hub[data-el="cyanloop-hub"].on .core{color:var(--n-9);}
.hub[data-el="cyanloop-hub"].on .core::before{background:var(--n-1);}
.hub[data-el="cyanloop-hub"].on .spoke:nth-child(4),.hub[data-el="cyanloop-hub"].on .spoke:nth-child(7){color:var(--page);}
''')
css('person','''
.people[data-el="cyanloop-person"].on>.person>:is(.name,.note),.people[data-el="cyanloop-person"].on>.person>.note .kick,.people[data-el="cyanloop-person"].on>.person>.list .name{background:var(--a1);}
.people[data-el="cyanloop-person"].on>.person:nth-child(2)>:is(.name,.note),.people[data-el="cyanloop-person"].on>.person:nth-child(2)>.note .kick,.people[data-el="cyanloop-person"].on>.person:nth-child(2)>.list .name{background:var(--a2);}
.people[data-el="cyanloop-person"].on>.person:nth-child(3)>:is(.name,.note),.people[data-el="cyanloop-person"].on>.person:nth-child(3)>.note .kick,.people[data-el="cyanloop-person"].on>.person:nth-child(3)>.list .name{background:var(--a1-7);}
''')
# Horizontal and vertical arrows occupy separate pseudo-elements, so branches preserve both directions.
for folder,root in [('flowchart','flowchart'),('swimlane','swimlane')]:
 p=C/'elements'/folder/'element.css';s=p.read_text();s=re.sub(r'[^{}]*\.to-[rdlu]::(?:before|after)\s*\{[^{}]*\}','',s)
 base=f'.{root}[data-el="cyanloop-{folder}"] '
 s+='\n'+base+'''.to-r::after{content:'';position:absolute;left:100%;right:auto;top:calc(50% - 4px);bottom:auto;width:var(--gap);height:8px;background:var(--a1);clip-path:polygon(0 40%,70% 40%,70% 0,100% 50%,70% 100%,70% 60%,0 60%);transform:none;}\n'''
 s+=base+'''.to-l::after{content:'';position:absolute;right:100%;left:auto;top:calc(50% - 4px);bottom:auto;width:var(--gap);height:8px;background:var(--a1);clip-path:polygon(0 40%,70% 40%,70% 0,100% 50%,70% 100%,70% 60%,0 60%);transform:rotate(180deg);}\n'''
 s+=base+'''.to-d::before{content:'';position:absolute;left:calc(50% - 4px);right:auto;top:100%;bottom:auto;width:8px;height:var(--gap);background:var(--a1);clip-path:polygon(40% 0,60% 0,60% 70%,100% 70%,50% 100%,0 70%,40% 70%);transform:none;}\n'''
 s+=base+'''.to-u::before{content:'';position:absolute;left:calc(50% - 4px);right:auto;bottom:100%;top:auto;width:8px;height:var(--gap);background:var(--a1);clip-path:polygon(40% 0,60% 0,60% 70%,100% 70%,50% 100%,0 70%,40% 70%);transform:rotate(180deg);}\n'''
 p.write_text(s)
 fixture='<!-- min: 10x5 -->\n<div class="'+root+'" data-el="cyanloop-'+folder+'" style="grid-column:1 / span 12; grid-row:1 / span 6; --cols:4">'+''.join('<div class="node '+cl+'" style="grid-column:'+str(co)+';grid-row:'+str(ro)+'">'+name+'</div>' for cl,co,ro,name in [('start to-r',1,1,'접수'),('ask to-r to-d',2,1,'검토'),('to-r',3,1,'승인'),('end',4,1,'종료'),('to-d',2,2,'보완'),('to-r',2,3,'재검토'),('to-u',3,3,'확인'),('to-l',3,2,'회신')])+'</div>\n'
 (C/'elements'/folder/'fixtures/branch-four-directions.html').write_text(fixture)
p=W/'reassembly.py';s=p.read_text().replace("('Practical','presentation')", "('Practical','cpu')");s=s.replace("(R/'library/runtime-original.css').write_text(style+orig)", "orig+='\\n.slide.dark .hub.on{--page:#f5f5f5;}\\n'\n(R/'library/runtime-original.css').write_text(style+orig)");p.write_text(s)
p=C/'elements/card/fixtures/features-3-circles.html';p.write_text(p.read_text().replace('data-icon="presentation"','data-icon="cpu"'))
