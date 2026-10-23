from pathlib import Path
C=Path('/workspace/output/cyanloop');W=Path('/workspace/work/cyanloop')
def css(folder,s):
 p=C/'elements'/folder/'element.css';p.write_text(p.read_text()+'\n'+s)
css('card','''
.card[data-el="cyanloop-card"].on.quiet .note{width:100%;}
.card[data-el="cyanloop-card"].on.quiet .note .list{width:100%;color:inherit;}
.card[data-el="cyanloop-card"].on.quiet .note .list .item{width:100%;}
.card[data-el="cyanloop-card"].on.quiet .note .list .name{font-size:var(--type-16);font-weight:var(--body-weight);color:var(--a2-on);}
''')
css('legend','.legend[data-el="cyanloop-legend"].col{flex-wrap:nowrap;}')
css('chart-bar',r'''.bars[data-el="cyanloop-chart-bar"].line::after{top:calc(0px - var(--cyanloop-space-20));content:counter(cyanloop-y100) '\A' counter(cyanloop-y80) '\A' counter(cyanloop-y60) '\A' counter(cyanloop-y40) '\A' counter(cyanloop-y20) '\A' counter(cyanloop-y0);counter-reset:cyanloop-y100 var(--max) cyanloop-y80 calc(var(--max)*.8) cyanloop-y60 calc(var(--max)*.6) cyanloop-y40 calc(var(--max)*.4) cyanloop-y20 calc(var(--max)*.2) cyanloop-y0 0;}''')
css('person','''
.people[data-el="cyanloop-person"].on>.person>.note .kick{font-size:var(--type-20);}
.people[data-el="cyanloop-person"].on>.person:nth-child(2)>.note .kick{font-size:var(--type-18);}
''')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
.slide.cover .page.at-bottom-left .deco{left:769px;top:-117px;width:328px;height:398px;border-radius:50%;background:radial-gradient(circle at 289px 199px,var(--a3-7) 0 39px,color-mix(in srgb,var(--page) 0%,var(--ink) 0.001%) 40px),conic-gradient(from 90deg,var(--a3-7),var(--a1-7) 180deg,color-mix(in srgb,var(--page) 0%,var(--ink) 0.001%) 180deg);mask:radial-gradient(ellipse 86px 121px at center,color-mix(in srgb,var(--page) 0%,var(--ink) 0.001%) 99%,var(--ink) 100%);}
''')
p=W/'reassembly.py';s=p.read_text().replace("6,2,5,1,variant='col'", "6,2,5,2,variant='col'");p.write_text(s)
# Update source fixture expansion for independent keyword/outcome cards.
p=W/'source_fixtures.py';s=p.read_text().replace("7:['card','callout']", "7:['card','card','card','card','callout']").replace("16:['metric','prose','list','card']", "16:['metric','prose','list','card','card','card','card','card','card']");p.write_text(s)
