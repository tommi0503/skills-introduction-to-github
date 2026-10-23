from pathlib import Path
O=Path('/workspace/output/fluxweave')
def ap(f,s):p=O/'elements'/f/'element.css';p.write_text(p.read_text()+s.replace('ROOT',f'[data-el="fluxweave-{f}"]'))
p=O/'foundation/foundation.css';p.write_text(p.read_text()+'''
.slide .head{grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--gap);min-height:140px;padding-top:calc(var(--gap-sm)*.8);}
.slide .head .title{line-height:calc(var(--title-line) + .05);}
.slide .rail{background:linear-gradient(155deg,var(--a2-7-soft),var(--a1-7-soft));color:var(--page);}
''')
ap('card','''
ROOT:has(>.parts>.bars),ROOT:has(>.parts>.org){padding:var(--pad);background:var(--n-1);}
ROOT:has(>.parts>.bars)>.parts,ROOT:has(>.parts>.org)>.parts{height:100%;display:grid;grid-template-columns:minmax(0,1fr);grid-template-rows:auto minmax(0,1fr);gap:var(--gap);}
ROOT:has(>.parts>.bars)>.parts>.name,ROOT:has(>.parts>.org)>.parts>.name{min-height:0;font-size:var(--type-24);line-height:var(--name-line);grid-area:1/1;}
ROOT>.parts>.bars,ROOT>.parts>.lines,ROOT>.parts>.org{grid-area:2/1;min-height:0;}
ROOT>.parts>.legend{grid-area:2/1;align-self:end;height:24px;z-index:3;}
ROOT>.parts>.legend .key{font-size:var(--type-12);gap:calc(var(--gap-sm)*.3);}
ROOT>.parts>.legend .key::before{width:10px;height:10px;}
ROOT>.parts>.bars{padding:var(--gap) calc(var(--gap-sm)*1.5) calc(var(--gap-lg)*1.8) calc(var(--gap)*2.5);gap:0;border:0;background:none;}
ROOT>.parts>.bars>.bar::before{height:calc(var(--v)/var(--max)*100%);width:66%;background:var(--a1);}
ROOT>.parts>.bars>.bar>b{font-size:var(--type-14);bottom:max(calc(var(--v)/var(--max)*100% - var(--gap-lg)),0px);color:var(--a1-on);}
ROOT>.parts>.bars>.bar>span{font-size:var(--type-12);top:calc(100% + var(--gap-sm)*.5);}
ROOT>.parts>.lines{padding:var(--gap) calc(var(--gap-sm)*1.5) calc(var(--gap-lg)*1.8) calc(var(--gap)*2.5);grid-template-rows:minmax(0,1fr);border:0;}
ROOT>.parts>.lines>.pt>b{height:calc(100% - var(--v)/var(--max)*100%);font-size:var(--type-14);color:var(--a2-7);}
ROOT>.parts>.lines>.pt>b::after{background:var(--a2);width:6px;height:6px;}
ROOT>.parts>.lines>.pt>span{display:none;}
ROOT>.parts>.lines>.pt:not(:first-child)::before{background:linear-gradient(to top right,color-mix(in srgb,var(--page) 0%,var(--page) 1%) calc(50% - 1px),var(--a2) 50%,color-mix(in srgb,var(--page) 0%,var(--page) 1%) calc(50% + 1px));}
ROOT>.parts>.lines>.pt:not(:first-child)::after{background:linear-gradient(to bottom right,color-mix(in srgb,var(--page) 0%,var(--page) 1%) calc(50% - 1px),var(--a2) 50%,color-mix(in srgb,var(--page) 0%,var(--page) 1%) calc(50% + 1px));}
ROOT>.parts>.bars::after{content:counter(flux-max) '\\A' counter(flux-three) '\\A' counter(flux-half) '\\A' counter(flux-one) '\\A 0';counter-reset:flux-max var(--max) flux-three calc(var(--max)*.75) flux-half calc(var(--max)*.5) flux-one calc(var(--max)*.25);position:absolute;left:0;top:calc(var(--gap) - var(--type-12)*.5);width:calc(var(--gap)*2.3);font-size:var(--type-12);white-space:pre;text-align:right;line-height:calc((100cqh - var(--gap) - var(--gap-lg)*1.8)/4);}
ROOT>.parts:has(>.group>.pill){position:relative;height:100%;display:block;}
ROOT:has(>.parts>.group>.pill){padding:calc(var(--gap-lg) + var(--gap-sm)*1.2);background:var(--n-1);}
ROOT>.parts:has(>.group>.pill)>.name{position:absolute;top:0;left:0;right:0;min-height:0;font-size:var(--type-24);}
ROOT>.parts:has(>.group>.pill)>.kick{position:absolute;top:calc(var(--gap)*1.5);left:0;right:0;font-size:var(--type-16);color:var(--n-5);}
ROOT>.parts:has(>.group>.pill)>.note{position:absolute;top:calc(var(--gap-lg)*2 + var(--gap-sm)*.2);left:0;width:75%;min-height:0;font-size:var(--type-18);}
ROOT>.parts:has(>.group>.pill)>.headline{position:absolute;bottom:calc(var(--gap-lg) + var(--gap)*1.2);left:0;right:0;height:28px;}
ROOT>.parts:has(>.group>.pill)>.headline>h2{font-size:var(--type-24);}
ROOT>.parts:has(>.group>.pill)>.group{position:absolute;bottom:0;left:0;right:0;height:38px;gap:calc(var(--gap-sm)*.6);}
ROOT>.parts>.group>.pill{width:auto;flex:0 1 auto;padding:calc(var(--gap-sm)*.8) var(--gap-sm);min-height:38px;height:38px;background:var(--a2);color:var(--a2-on);}
ROOT>.parts>.group>.pill .name{font-size:var(--type-18);min-height:0;white-space:nowrap;}
ROOT:has(>.parts>.group>.pill):nth-child(2){text-align:right;}
ROOT:nth-child(2)>.parts:has(>.group>.pill)>.note{left:auto;right:0;}
ROOT:nth-child(2)>.parts:has(>.group>.pill)>.group{justify-content:flex-end;}
ROOT.on:has(>.parts>.name:only-child){width:257px;height:257px;max-width:100%;max-height:100%;border:calc(var(--gap)) solid var(--page);border-radius:50%;padding:var(--gap);align-self:center;justify-self:center;display:grid;place-items:center;}
ROOT.on:has(>.parts>.name:only-child)>.parts>.name{min-height:0;text-align:center;font-size:var(--type-24);line-height:var(--title-line);}
''')
ap('hierarchy','''
ROOT{padding-top:calc(var(--gap-lg)*3 + var(--gap-sm)*.5);gap:calc(var(--gap-sm)*1.4);}
ROOT>.root{left:16.5%;width:67.5%;top:6px;height:52px;padding:var(--gap-sm);font-size:var(--type-20);line-height:var(--name-line);background:linear-gradient(90deg,var(--a2),var(--a1-3-soft));display:grid;place-items:center;}
ROOT>.root::after{height:22px;}
ROOT::before{content:"";position:absolute;top:80px;left:16.5%;right:16.5%;border-top:var(--stroke) solid var(--n-4);}
ROOT>.branch{position:relative;justify-content:flex-start;padding-top:0;border-top:0;gap:var(--gap-sm);}
ROOT>.branch::before{content:"";position:absolute;left:50%;top:-21px;height:21px;border-left:var(--stroke) solid var(--n-4);}
ROOT>.branch>.node{height:52px;flex:none;padding:var(--gap-sm);display:grid;place-items:center;font-size:var(--type-18);line-height:var(--name-line);background:var(--a2);color:var(--a2-on);}
ROOT>.branch>.leaf{height:52px;flex:none;padding:var(--gap-sm);display:grid;place-items:center;font-size:var(--type-16);line-height:var(--name-line);background:var(--page);}
''')
ap('steps','''
ROOT:has(>.step>.mark>small){display:block;isolation:isolate;}
ROOT:has(>.step>.mark>small)>.step{position:absolute;top:33.5%;left:18%;width:22%;height:66.3%;padding:calc(var(--gap)*.9);border:0;background:var(--a2);color:var(--a2-on);justify-content:flex-start;gap:var(--gap-sm);}
ROOT:has(>.step>.mark>small)>.step:nth-child(2){top:21.9%;left:46.5%;background:var(--a1);color:var(--a1-on);}
ROOT:has(>.step>.mark>small)>.step:nth-child(3){top:10.3%;left:75%;background:var(--a1-7);color:var(--page);}
ROOT:has(>.step>.mark>small) .mark{font-size:var(--type-100);line-height:var(--figure-line);font-weight:var(--body-weight);color:inherit;}
ROOT:has(>.step>.mark>small) .mark>small{position:absolute;top:calc(-1*(var(--gap-lg) + var(--gap) + var(--gap-sm)));left:calc(-1*var(--gap)*1.5);font-size:var(--type-24);font-weight:var(--name-weight);line-height:var(--name-line);color:var(--ink);white-space:nowrap;}
ROOT:has(>.step>.mark>small)>.step:nth-child(2) .mark>small{top:calc(-1*(var(--gap-lg) + var(--gap) + var(--gap-sm)*.1));left:calc(-1*var(--gap-sm)*.8);}
ROOT:has(>.step>.mark>small)>.step:nth-child(3) .mark>small{top:calc(-1*(var(--gap-lg) + var(--gap-sm)*1.5));left:calc(var(--gap-sm)*1.3);}
ROOT:has(>.step>.mark>small) .name{font-size:var(--type-22);min-height:0;}
ROOT:has(>.step>.mark>small) .note{font-size:var(--type-16);color:inherit;line-height:var(--body-line);}
ROOT:has(>.step>.mark>small)::before{content:"";position:absolute;left:18%;top:38%;width:81%;height:3px;background:var(--a1);transform:rotate(-10deg);transform-origin:left center;z-index:-1;}
ROOT:has(>.step>.mark>small)::after{content:"";position:absolute;right:2%;top:5%;width:14px;height:12px;background:var(--a1);clip-path:polygon(0 0,100% 50%,0 100%,30% 50%);transform:rotate(-10deg);}
''')
print('fidelity compositions CSS ready')
