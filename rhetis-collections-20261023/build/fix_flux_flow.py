from pathlib import Path
base=Path('/workspace/output/fluxweave/elements')
def write(kind,body):
 p=base/kind/'element.css';head='\n'.join(p.read_text().splitlines()[:3]);p.write_text(head+'\n'+body+'\n')
write('journey','''[data-el="fluxweave-journey"]{--fw-count:3;--fw-gap:var(--gap);display:flex;gap:var(--fw-gap);isolation:isolate;}
[data-el="fluxweave-journey"]:has(>.stage:nth-child(4):last-child){--fw-count:4;}
[data-el="fluxweave-journey"]:has(>.stage:nth-child(5):last-child){--fw-count:5;}
[data-el="fluxweave-journey"]:has(>.stage:nth-child(6):last-child){--fw-count:6;}
[data-el="fluxweave-journey"]:has(>.stage:nth-child(7):last-child){--fw-count:7;}
[data-el="fluxweave-journey"]>.stage{flex:1;min-width:0;position:relative;display:flex;flex-direction:column;gap:var(--gap-sm);padding:50cqh var(--gap-sm) var(--gap-sm);border-top:2px solid var(--a1-3-soft);}
[data-el="fluxweave-journey"]>.stage.on{border-color:var(--a1);background:var(--a1-1-soft);border-radius:var(--radius);}
[data-el="fluxweave-journey"]>.stage>.name{min-height:2.5em;}
[data-el="fluxweave-journey"]>.stage::after{content:"";position:absolute;left:50%;top:calc(10cqh + (100 - var(--mood))* .35cqh);width:10px;height:10px;border-radius:50%;background:var(--a1);transform:translate(-50%,-50%);z-index:3;}
[data-el="fluxweave-journey"]>.stage:not(:last-child)::before{--fw-dx:calc((100cqw - (var(--fw-count) - 1)*var(--fw-gap))/var(--fw-count) + var(--fw-gap));--fw-dy:calc((var(--mood) - var(--next))*.35cqh);content:"";position:absolute;left:50%;top:calc(10cqh + (100 - var(--mood))*.35cqh);width:hypot(var(--fw-dx),var(--fw-dy));height:2px;background:var(--a1-4-soft);transform-origin:0 50%;transform:translateY(-50%) rotate(atan2(var(--fw-dy),var(--fw-dx)));z-index:2;}
[data-el="fluxweave-journey"] .mark{font-size:var(--type-44);font-weight:var(--figure-weight);color:var(--a1-7);}
[data-el="fluxweave-journey"] .pain{font-size:var(--type-14);color:var(--bad);}
@container(max-width:800px){[data-el="fluxweave-journey"]{--fw-gap:var(--gap-sm);}[data-el="fluxweave-journey"]>.stage>.name{font-size:var(--type-18);}[data-el="fluxweave-journey"]>.stage>.note{font-size:var(--type-14);}[data-el="fluxweave-journey"] .mark{font-size:var(--type-28);}}
''')
write('cycle','''[data-el="fluxweave-cycle"]{--fw-count:3;display:block;isolation:isolate;}
[data-el="fluxweave-cycle"]:has(>.node:nth-child(5):last-child){--fw-count:4;}
[data-el="fluxweave-cycle"]:has(>.node:nth-child(6):last-child){--fw-count:5;}
[data-el="fluxweave-cycle"]:has(>.node:nth-child(7):last-child){--fw-count:6;}
[data-el="fluxweave-cycle"]::before{content:"";position:absolute;inset:20% 16%;border:2px solid var(--a1-3-soft);border-radius:50%;z-index:0;}
[data-el="fluxweave-cycle"]>.core{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:min(17cqw,23cqh);aspect-ratio:1;border-radius:50%;background:var(--a1);color:var(--a1-on);display:grid;place-items:center;text-align:center;padding:var(--gap-sm);font-size:var(--type-20);font-weight:var(--name-weight);z-index:2;}
[data-el="fluxweave-cycle"]>.node{--fw-i:0;--fw-theta:calc(-90deg + var(--fw-i)*360deg/var(--fw-count));--fw-mid:calc(var(--fw-theta) + 180deg/var(--fw-count));position:absolute;left:calc(50% + cos(var(--fw-theta))*34cqw);top:calc(50% + sin(var(--fw-theta))*30cqh);transform:translate(-50%,-50%);width:26cqw;padding:var(--gap-sm);background:var(--n-1);border-radius:var(--radius);text-align:center;z-index:1;}
[data-el="fluxweave-cycle"]>.node:nth-child(3){--fw-i:1;}
[data-el="fluxweave-cycle"]>.node:nth-child(4){--fw-i:2;}
[data-el="fluxweave-cycle"]>.node:nth-child(5){--fw-i:3;}
[data-el="fluxweave-cycle"]>.node:nth-child(6){--fw-i:4;}
[data-el="fluxweave-cycle"]>.node:nth-child(7){--fw-i:5;}
[data-el="fluxweave-cycle"]>.node::after{--fw-tx:calc(-34cqw*sin(var(--fw-mid)));--fw-ty:calc(30cqh*cos(var(--fw-mid)));content:"";position:absolute;left:calc(50% + (cos(var(--fw-mid)) - cos(var(--fw-theta)))*34cqw);top:calc(50% + (sin(var(--fw-mid)) - sin(var(--fw-theta)))*30cqh);width:10px;height:10px;border-top:2px solid var(--a1);border-right:2px solid var(--a1);transform:translate(-50%,-50%) rotate(calc(atan2(var(--fw-ty),var(--fw-tx)) + 45deg));}
[data-el="fluxweave-cycle"]>.node .name{display:block;font-size:var(--type-20);}
[data-el="fluxweave-cycle"]>.node .note{margin-top:var(--gap-sm);font-size:var(--type-16);}
[data-el="fluxweave-cycle"] .mark{display:grid;place-items:center;width:40px;height:40px;border-radius:50%;background:var(--a1-2-soft);margin:0 auto var(--gap-sm);}
[data-el="fluxweave-cycle"] .leaf{display:block;font-size:var(--type-14);margin-top:var(--gap-sm);}
@container(max-width:850px){[data-el="fluxweave-cycle"]>.node .name{font-size:var(--type-18);}[data-el="fluxweave-cycle"]>.node .note{font-size:var(--type-14);}[data-el="fluxweave-cycle"] .mark{width:32px;height:32px;}}
''')
write('sankey','''[data-el="fluxweave-sankey"]{--fw-count:3;display:block;isolation:isolate;}
[data-el="fluxweave-sankey"]:has(>.branch:nth-child(3):last-child){--fw-count:2;}
[data-el="fluxweave-sankey"]:has(>.branch:nth-child(5):last-child){--fw-count:4;}
[data-el="fluxweave-sankey"]:has(>.branch:nth-child(6):last-child){--fw-count:5;}
[data-el="fluxweave-sankey"]:has(>.branch:nth-child(7):last-child){--fw-count:6;}
[data-el="fluxweave-sankey"]>.source{position:absolute;left:0;top:50%;width:28%;min-height:26cqh;transform:translateY(-50%);padding:var(--gap);background:var(--a1-1-soft);border-radius:var(--radius);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:var(--gap-sm);z-index:2;}
[data-el="fluxweave-sankey"]>.branch{--fw-i:0;--fw-y:calc((var(--fw-i) + .5)*100/var(--fw-count));--fw-parent-share:var(--v);--fw-parent-height:calc(100cqh/var(--fw-count) - var(--gap-sm));position:absolute;left:46%;top:calc(var(--fw-y)*1%);width:54%;height:var(--fw-parent-height);transform:translateY(-50%);display:flex;align-items:center;justify-content:space-between;gap:var(--gap-sm);padding:var(--gap-sm) var(--gap);background:var(--a1-1-soft);border-radius:var(--radius);}
[data-el="fluxweave-sankey"]>.branch:nth-child(3){--fw-i:1;}
[data-el="fluxweave-sankey"]>.branch:nth-child(4){--fw-i:2;}
[data-el="fluxweave-sankey"]>.branch:nth-child(5){--fw-i:3;}
[data-el="fluxweave-sankey"]>.branch:nth-child(6){--fw-i:4;}
[data-el="fluxweave-sankey"]>.branch:nth-child(7){--fw-i:5;}
[data-el="fluxweave-sankey"]>.branch::before{--fw-dy:calc((var(--fw-y) - 50)*1cqh);content:"";position:absolute;right:100%;top:50%;width:hypot(18cqw,var(--fw-dy));height:calc(var(--v)*.2cqh);background:var(--a1-3-soft);transform-origin:100% 50%;transform:translateY(-50%) rotate(atan2(var(--fw-dy),18cqw));z-index:-1;}
[data-el="fluxweave-sankey"]>.branch.on::before{background:var(--a1-4-soft);}
[data-el="fluxweave-sankey"]>.branch.out{background:var(--n-1);}
[data-el="fluxweave-sankey"]>.branch.out::before{background:var(--n-3);}
[data-el="fluxweave-sankey"] .fig{font-size:var(--type-24);}
[data-el="fluxweave-sankey"] .branch .name{font-size:var(--type-18);}
[data-el="fluxweave-sankey"]>.branch:has(>.branch){--fw-nested:2;display:grid;grid-template-columns:55% 45%;grid-template-rows:repeat(var(--fw-nested),minmax(0,1fr));padding:0;gap:0;background:none;border-radius:0;}
[data-el="fluxweave-sankey"]>.branch:has(>.branch:nth-child(5):last-child){--fw-nested:3;}
[data-el="fluxweave-sankey"]>.branch:has(>.branch:nth-child(6):last-child){--fw-nested:4;}
[data-el="fluxweave-sankey"]>.branch:has(>.branch)>.name,[data-el="fluxweave-sankey"]>.branch:has(>.branch)>.fig{position:absolute;left:0;width:35%;text-align:center;z-index:1;}
[data-el="fluxweave-sankey"]>.branch:has(>.branch)>.name{bottom:calc(50% + var(--gap-sm)/2);}
[data-el="fluxweave-sankey"]>.branch:has(>.branch)>.fig{top:calc(50% + var(--gap-sm)/2);}
[data-el="fluxweave-sankey"]>.branch:has(>.branch)::after{content:"";position:absolute;left:0;top:20%;width:35%;height:60%;background:var(--a1-1-soft);border-radius:var(--radius);}
[data-el="fluxweave-sankey"] .branch>.branch{--fw-j:0;position:relative;grid-column:2;align-self:center;display:flex;align-items:center;justify-content:space-between;gap:var(--gap-sm);height:calc(100% - var(--gap-sm)/2);padding:var(--gap-sm);background:var(--n-1);border-radius:var(--radius);}
[data-el="fluxweave-sankey"] .branch>.branch:nth-child(4){--fw-j:1;}
[data-el="fluxweave-sankey"] .branch>.branch:nth-child(5){--fw-j:2;}
[data-el="fluxweave-sankey"] .branch>.branch:nth-child(6){--fw-j:3;}
[data-el="fluxweave-sankey"] .branch>.branch::before{--fw-dy:calc(((var(--fw-j) + .5)/var(--fw-nested) - .5)*var(--fw-parent-height));content:"";position:absolute;right:100%;top:50%;width:hypot(10.8cqw,var(--fw-dy));height:calc(var(--v)*var(--fw-parent-share)/100*.2cqh);background:var(--a1-3-soft);transform-origin:100% 50%;transform:translateY(-50%) rotate(atan2(var(--fw-dy),10.8cqw));z-index:-1;}
[data-el="fluxweave-sankey"] .branch>.branch.out::before{background:var(--n-3);}
@container(max-width:850px){[data-el="fluxweave-sankey"] .branch .name{font-size:var(--type-16);}[data-el="fluxweave-sankey"] .branch .fig{font-size:var(--type-20);}}
''')
