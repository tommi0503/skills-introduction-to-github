from pathlib import Path
root=Path('/workspace/output/nightchamfer/elements')
def add(name,text):
 p=root/name/'element.css'; p.write_text(p.read_text()+'\n'+text+'\n')
add('mindmap',r'''
[data-el="nightchamfer-mindmap"]{display:block;padding:0;isolation:isolate}
[data-el="nightchamfer-mindmap"]>.core{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:min(30cqw,42cqh);height:min(30cqw,42cqh);aspect-ratio:1;z-index:2}
[data-el="nightchamfer-mindmap"]>.branch{position:absolute;width:28%;height:28%;left:0;top:3%;--nightchamfer-branch-y:17;z-index:1}
[data-el="nightchamfer-mindmap"]>.branch:nth-child(odd){left:72%}
[data-el="nightchamfer-mindmap"]>.branch:nth-child(4),[data-el="nightchamfer-mindmap"]>.branch:nth-child(5){top:36%;--nightchamfer-branch-y:50}
[data-el="nightchamfer-mindmap"]>.branch:nth-child(6),[data-el="nightchamfer-mindmap"]>.branch:nth-child(7){top:69%;--nightchamfer-branch-y:83}
[data-el="nightchamfer-mindmap"]>.branch::before{left:100%;right:auto;top:50%;width:hypot(22cqw,calc((50 - var(--nightchamfer-branch-y))*1cqh));height:var(--gap-sm);border-top:1px solid var(--n-5);border-radius:50%;background:color-mix(in srgb,var(--page) 0%,var(--ink) .001%);transform-origin:0 0;transform:rotate(atan2(calc((50 - var(--nightchamfer-branch-y))*1cqh),22cqw));z-index:-1}
[data-el="nightchamfer-mindmap"]>.branch:nth-child(odd)::before{left:auto;right:100%;transform-origin:100% 0;transform:rotate(atan2(calc((var(--nightchamfer-branch-y) - 50)*1cqh),22cqw))}
[data-el="nightchamfer-mindmap"]>.branch.on::before{border-color:var(--a1)}
[data-el="nightchamfer-mindmap"]:has(>.branch:nth-child(3):last-child)>.branch{top:36%;--nightchamfer-branch-y:50}
[data-el="nightchamfer-mindmap"]:has(>.branch:nth-child(5):last-child)>.branch:nth-child(2),[data-el="nightchamfer-mindmap"]:has(>.branch:nth-child(5):last-child)>.branch:nth-child(3){top:12%;--nightchamfer-branch-y:26}
[data-el="nightchamfer-mindmap"]:has(>.branch:nth-child(5):last-child)>.branch:nth-child(4),[data-el="nightchamfer-mindmap"]:has(>.branch:nth-child(5):last-child)>.branch:nth-child(5){top:60%;--nightchamfer-branch-y:74}
''')
add('cycle',r'''
[data-el="nightchamfer-cycle"]{display:block;padding:0;isolation:isolate;--nightchamfer-node-count:3;--nightchamfer-orbit-x:35cqw;--nightchamfer-orbit-y:35cqh}
[data-el="nightchamfer-cycle"]:has(>.node:nth-child(5)){--nightchamfer-node-count:4}
[data-el="nightchamfer-cycle"]:has(>.node:nth-child(6)){--nightchamfer-node-count:5}
[data-el="nightchamfer-cycle"]:has(>.node:nth-child(7)){--nightchamfer-node-count:6}
[data-el="nightchamfer-cycle"]::before{left:15%;right:15%;top:15%;bottom:15%;border:1px dotted var(--n-5);z-index:0}
[data-el="nightchamfer-cycle"]>.core{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:min(27cqw,36cqh);height:min(27cqw,36cqh);max-width:none;font-size:var(--type-22)}
[data-el="nightchamfer-cycle"]>.node{--nightchamfer-node-index:0;--nightchamfer-angle:calc(-90deg + var(--nightchamfer-node-index)*360deg/var(--nightchamfer-node-count));--nightchamfer-mid-angle:calc(var(--nightchamfer-angle) + 180deg/var(--nightchamfer-node-count));position:absolute;left:calc(50% + var(--nightchamfer-orbit-x)*cos(var(--nightchamfer-angle)));top:calc(50% + var(--nightchamfer-orbit-y)*sin(var(--nightchamfer-angle)));transform:translate(-50%,-50%);width:26%;height:24%;max-width:240px;max-height:100px;padding:calc(var(--gap-sm)*.75);z-index:1}
[data-el="nightchamfer-cycle"]>.node:nth-child(3){--nightchamfer-node-index:1}[data-el="nightchamfer-cycle"]>.node:nth-child(4){--nightchamfer-node-index:2}[data-el="nightchamfer-cycle"]>.node:nth-child(5){--nightchamfer-node-index:3}[data-el="nightchamfer-cycle"]>.node:nth-child(6){--nightchamfer-node-index:4}[data-el="nightchamfer-cycle"]>.node:nth-child(7){--nightchamfer-node-index:5}
[data-el="nightchamfer-cycle"]>.node::before{display:none}
[data-el="nightchamfer-cycle"]>.node::after,[data-el="nightchamfer-cycle"]>.node:nth-child(odd)::after{left:calc(50% + var(--nightchamfer-orbit-x)*(cos(var(--nightchamfer-mid-angle)) - cos(var(--nightchamfer-angle))));right:auto;top:calc(50% + var(--nightchamfer-orbit-y)*(sin(var(--nightchamfer-mid-angle)) - sin(var(--nightchamfer-angle))));width:var(--gap-sm);height:var(--gap-sm);transform:translate(-50%,-50%) rotate(atan2(calc(var(--nightchamfer-orbit-y)*cos(var(--nightchamfer-mid-angle))),calc(-1*var(--nightchamfer-orbit-x)*sin(var(--nightchamfer-mid-angle))))}
[data-el="nightchamfer-cycle"]>.node.on{border-color:var(--a1);background:var(--a1-1-soft)}
@container(max-width:650px){[data-el="nightchamfer-cycle"]>.core{font-size:var(--type-16);border-width:8px}[data-el="nightchamfer-cycle"]>.node{padding:calc(var(--gap-sm)/2);gap:calc(var(--gap-sm)/3)}[data-el="nightchamfer-cycle"] .name{font-size:var(--type-14)}[data-el="nightchamfer-cycle"] .note{font-size:var(--type-12)}}
''')
add('sankey',r'''
[data-el="nightchamfer-sankey"]{display:block;padding:0;--nightchamfer-branch-count:3}
[data-el="nightchamfer-sankey"]:has(>.branch:nth-child(3):last-child){--nightchamfer-branch-count:2}
[data-el="nightchamfer-sankey"]:has(>.branch:nth-child(5):last-child){--nightchamfer-branch-count:4}
[data-el="nightchamfer-sankey"]:has(>.branch:nth-child(6):last-child){--nightchamfer-branch-count:5}
[data-el="nightchamfer-sankey"]:has(>.branch:nth-child(7):last-child){--nightchamfer-branch-count:6}
[data-el="nightchamfer-sankey"]>.source{position:absolute;left:0;top:50%;transform:translateY(-50%);width:28%;min-height:30%;justify-content:center;z-index:2}
[data-el="nightchamfer-sankey"]>.branch{--nightchamfer-branch-index:0;--nightchamfer-branch-y:calc((var(--nightchamfer-branch-index) + .5)*100/var(--nightchamfer-branch-count));position:absolute;left:48%;top:calc(var(--nightchamfer-branch-y)*1%);transform:translateY(-50%);width:52%;height:calc(100%/var(--nightchamfer-branch-count) - var(--gap-sm));z-index:1}
[data-el="nightchamfer-sankey"]>.branch:nth-child(3){--nightchamfer-branch-index:1}[data-el="nightchamfer-sankey"]>.branch:nth-child(4){--nightchamfer-branch-index:2}[data-el="nightchamfer-sankey"]>.branch:nth-child(5){--nightchamfer-branch-index:3}[data-el="nightchamfer-sankey"]>.branch:nth-child(6){--nightchamfer-branch-index:4}[data-el="nightchamfer-sankey"]>.branch:nth-child(7){--nightchamfer-branch-index:5}
[data-el="nightchamfer-sankey"]>.branch::before{right:100%;top:50%;width:hypot(20cqw,calc((var(--nightchamfer-branch-y) - 50)*1cqh));height:calc(var(--v)*.1cqh + 2px);background:var(--a1-3-soft);transform-origin:100% 50%;transform:translateY(-50%) rotate(atan2(calc((var(--nightchamfer-branch-y) - 50)*1cqh),20cqw));z-index:-1}
[data-el="nightchamfer-sankey"]>.branch.on::before{background:var(--a1-4)}
[data-el="nightchamfer-sankey"]>.branch:has(>.branch){display:grid;grid-template-columns:44% 56%;grid-auto-rows:1fr;align-items:center;gap:0;padding:0;border:0;background:color-mix(in srgb,var(--page) 0%,var(--ink) .001%)}
[data-el="nightchamfer-sankey"]>.branch:has(>.branch)>.name{position:absolute;left:0;top:35%;width:31%;font-size:var(--type-18)}
[data-el="nightchamfer-sankey"]>.branch:has(>.branch)>.fig{position:absolute;left:0;top:53%;width:31%}
[data-el="nightchamfer-sankey"]>.branch>.branch{position:relative;grid-column:2;display:flex;align-items:center;justify-content:space-between;gap:calc(var(--gap-sm)/2);border:1px solid var(--n-4);border-radius:var(--radius-sm);background:var(--n-1);padding:calc(var(--gap-sm)*.75);min-height:0;margin:calc(var(--gap-sm)/3) 0}
[data-el="nightchamfer-sankey"]>.branch>.branch>.name{font-size:var(--type-16)}[data-el="nightchamfer-sankey"]>.branch>.branch>.fig{font-size:var(--type-20)}
[data-el="nightchamfer-sankey"]>.branch:has(>.branch)::after{content:"";position:absolute;left:0;top:20%;width:32%;height:60%;border:1px solid var(--n-4);border-radius:var(--radius-sm);background:var(--n-1);z-index:-1}
[data-el="nightchamfer-sankey"]>.branch>.branch::before{content:"";position:absolute;right:100%;top:50%;width:24%;height:calc(var(--v)*.18px + 2px);background:var(--a1-3-soft)}
[data-el="nightchamfer-sankey"]>.branch:has(>.branch)::before{z-index:-2}
@container(max-width:800px){[data-el="nightchamfer-sankey"]>.source{padding:var(--gap-sm);border-width:8px}[data-el="nightchamfer-sankey"]>.source>.fig{font-size:var(--type-28)}[data-el="nightchamfer-sankey"]>.branch:has(>.branch)>.name{font-size:var(--type-14)}[data-el="nightchamfer-sankey"]>.branch:has(>.branch)>.fig{font-size:var(--type-20)}[data-el="nightchamfer-sankey"]>.branch>.branch>.name{font-size:var(--type-14)}[data-el="nightchamfer-sankey"]>.branch>.branch>.fig{font-size:var(--type-16)}}
''')
