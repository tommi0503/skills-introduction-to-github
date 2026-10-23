"""Source-driven fidelity corrections; never modifies golden fixture markup or data."""
from pathlib import Path
import json
P=Path(__file__).parent;C=P/'seedmark';M='/* SOURCE_FIDELITY_CORRECTION */'
def patch(rel,s):
 p=C/rel;p.write_text(p.read_text().split(M)[0]+'\n'+M+'\n'+s+'\n')
patch('foundation/foundation.css','''
.page{gap:var(--pad)}.head{height:calc(var(--pad)*5.3125);padding-top:calc(var(--gap-sm)*.833333);gap:calc(var(--gap) + var(--gap-sm)/3)}
.head:has(.title br){height:calc(var(--pad)*7.1875)}.page:has(.head>.title br){gap:calc(var(--pad) - var(--gap-sm)/2)}.kicker{height:32px;display:flex;align-items:center;font-size:var(--type-22);padding:0 calc(var(--gap)*.75)}
.body{margin-top:0;margin-bottom:calc(var(--gap-sm)*1.5)}.top{top:var(--margin-y)}
.page:not(:has(.head))>.body{padding-top:calc(var(--pad)*1.5)}
.cover .page{inset:var(--margin-y) var(--margin-x)}.cover .at-left{top:calc(var(--pad)*3.375)}
.lockup .kicker{height:auto;font-size:var(--type-32)}.lockup .title{font-size:var(--type-100);line-height:var(--title-line)}
.cover .seat.back{top:calc(var(--pad)*1.9375);width:55.5%;height:528px;border-radius:999px 0 0 999px}
.cover .meta{bottom:calc(var(--gap-sm)*.5)}
''')
patch('elements/card/element.css','''
[data-el="seedmark-card"] .parts>.note{display:block;font-size:var(--type-16);color:var(--ink)}
[data-el="seedmark-card"] .parts>.name{font-size:var(--type-28)}
[data-el="seedmark-card"]:has(>.parts>.mark):has(>.parts>.kick){position:relative;isolation:isolate;border:0;background:none;padding:calc(var(--pad)*2.125) calc(var(--gap)*1.5) var(--gap-sm)}
[data-el="seedmark-card"]:has(>.parts>.mark):has(>.parts>.kick):before{content:'';position:absolute;inset:24px 0 0;border:var(--stroke) solid var(--n-3);border-radius:var(--radius);background:var(--page);z-index:-1;}
[data-el="seedmark-card"].line:has(>.parts>.mark):has(>.parts>.kick):before{border-color:var(--ink);}
[data-el="seedmark-card"] .parts:has(>.mark):has(>.kick){height:100%;position:relative;display:grid;grid-template-rows:calc(var(--pad)*.75) calc(var(--pad)*2.5) minmax(0,1fr);gap:calc(var(--gap-sm)/2);text-align:center}
[data-el="seedmark-card"] .parts:has(>.mark):has(>.kick)>.mark{position:absolute;top:calc(var(--pad)*-2.125);left:50%;transform:translateX(-50%);width:54px;height:54px;min-width:54px}
[data-el="seedmark-card"] .parts:has(>.mark):has(>.kick)>.mark .icon{width:30px;height:30px}
[data-el="seedmark-card"] .parts:has(>.mark):has(>.kick)>.kick{grid-row:1;display:block;font-size:var(--type-14)}
[data-el="seedmark-card"] .parts:has(>.mark):has(>.kick)>.name{grid-row:2;font-size:var(--type-30);text-align:center;padding-bottom:var(--gap-sm)}
[data-el="seedmark-card"] .parts:has(>.mark):has(>.kick)>.note{grid-row:3;text-align:left;font-size:var(--type-16)}
[data-el="seedmark-card"] .parts:has(>[data-el]){display:flex;height:100%;flex-direction:column;gap:var(--gap-sm);justify-content:center}
[data-el="seedmark-card"] .parts:has(>.group){display:flex;height:100%;padding:0;justify-content:center}
[data-el="seedmark-card"] .parts>.group{width:100%;height:100%;align-items:center;gap:var(--gap-sm)}
[data-el="seedmark-card"]:has(>.parts>.group){padding:var(--gap-sm)}
[data-el="seedmark-card"] .parts>.list{display:flex;flex-direction:column;justify-content:flex-end;padding:0;flex:1}
[data-el="seedmark-card"] .parts>.list .item{padding:0;border:0;min-height:0}
[data-el="seedmark-card"] .parts>.list .name{font-size:var(--type-14);font-weight:var(--label-weight);border:0;padding:0}
@container(max-height:220px){[data-el="seedmark-card"] .parts>.note{display:block;font-size:var(--type-16)}[data-el="seedmark-card"] .parts>.name{font-size:var(--type-24)}}
@container(max-width:260px){[data-el="seedmark-card"] .parts>.note{display:block;font-size:var(--type-16)}[data-el="seedmark-card"] .parts>.name{font-size:var(--type-24)}}
@container(max-height:180px){[data-el="seedmark-card"] .parts:has(>.mark):has(>.kick){display:flex;gap:calc(var(--gap-sm)/2);text-align:left}[data-el="seedmark-card"] .parts:has(>.mark):has(>.kick)>.mark{position:static;transform:none;width:36px;height:36px;min-width:36px}[data-el="seedmark-card"] .parts:has(>.mark):has(>.kick)>.name{font-size:var(--type-20);text-align:left}[data-el="seedmark-card"] .parts:has(>.mark):has(>.kick)>.note{font-size:var(--type-14)}}
''')
patch('elements/pill/element.css','''
[data-el="seedmark-pill"] .parts{position:relative;width:100%}
[data-el="seedmark-pill"].on:has(.mark):not(:has(.icon)){padding:var(--gap-sm) var(--gap);position:relative}
[data-el="seedmark-pill"].on:not(:has(.icon)) .parts>.mark{position:absolute;left:50%;top:calc(var(--gap-lg)*-1);transform:translateX(-50%);height:26px;min-width:94px;padding:0 calc(var(--gap-sm)/2);background:var(--page);color:var(--ink);border:var(--stroke) solid var(--n-7);border-radius:var(--radius-sm);font-size:var(--type-12);white-space:nowrap}
[data-el="seedmark-pill"].on .parts:has(>.note){flex-direction:column;gap:calc(var(--gap-sm)/2)}
[data-el="seedmark-pill"].on .name{font-size:var(--type-28)}
[data-el="seedmark-pill"].on .note{display:block;font-size:var(--type-20)}
[data-el="seedmark-pill"].line .parts:has(.icon){gap:var(--gap-lg);justify-content:flex-start}
[data-el="seedmark-pill"].line:has(.icon){padding-left:calc(var(--pad)*1.5)}
[data-el="seedmark-pill"].line .mark:has(.icon){position:absolute;left:calc(var(--pad)*-2.375);top:50%;transform:translateY(-50%);width:54px;height:54px;min-width:54px;border-radius:50%;background:var(--ink);color:var(--page)}
[data-el="seedmark-pill"].line .mark .icon{width:30px;height:30px}
[data-el="seedmark-pill"].line .parts>.name{font-size:var(--type-24);white-space:nowrap}
[data-el="seedmark-pill"].line .parts>.note{display:block;font-size:var(--type-18);color:var(--ink);max-width:70%}
[data-el="seedmark-pill"]:has(.icon[data-icon="database"]){height:100%;border-radius:50%/var(--seedmark-cylinder-curve);border-color:var(--ink);padding:0;background:var(--page);}
[data-el="seedmark-pill"]:has(.icon[data-icon="database"]) .parts{height:100%;}
[data-el="seedmark-pill"]:has(.icon[data-icon="database"]) .parts:before{content:'';position:absolute;inset:0 0 auto;height:30%;border-bottom:var(--stroke) solid var(--ink);border-radius:50%;}
[data-el="seedmark-pill"]:has(.icon[data-icon="database"]) .mark{display:none;}
[data-el="seedmark-pill"]:has(.icon[data-icon="database"]) .parts>.name{position:absolute;bottom:calc(var(--gap-sm)*-.75);left:50%;transform:translateX(-50%);font-size:var(--type-12);white-space:nowrap;background:var(--ink);color:var(--page);border-radius:var(--radius-sm);padding:calc(var(--gap-sm)/4) calc(var(--gap-sm)/2);}
@container(max-height:80px){[data-el="seedmark-pill"].on .name{font-size:var(--type-24)}[data-el="seedmark-pill"].line .parts>.note{font-size:var(--type-14)}}
''')
p=C/'elements/pill/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-pill"].quiet:has(.icon){height:100%;min-height:0;max-width:100%;padding:calc(var(--gap-sm)/2);border:0;border-radius:var(--radius);background:var(--n-1);}
[data-el="seedmark-pill"].quiet:has(.icon) .parts{display:flex;flex-direction:column;justify-content:center;gap:calc(var(--gap-sm)/2);height:100%;}
[data-el="seedmark-pill"].quiet:has(.icon) .mark{width:40px;height:40px;min-width:40px;background:none;color:var(--ink);}
[data-el="seedmark-pill"].quiet:has(.icon) .mark>.icon{width:32px;height:32px;}
[data-el="seedmark-pill"].quiet:has(.icon) .name{font-size:var(--type-12);font-weight:var(--label-weight);background:var(--ink);color:var(--page);padding:calc(var(--gap-sm)/4) calc(var(--gap-sm)/2);border-radius:var(--radius-sm);white-space:nowrap;}
[data-el="seedmark-pill"]:has(.mark):not(:has(.icon)){position:relative;isolation:isolate;background:none;border:0;padding-top:var(--gap-sm);}
[data-el="seedmark-pill"]:has(.mark):not(:has(.icon)):before{content:'';position:absolute;inset:12px 0 0;border:var(--stroke) solid var(--ink);border-radius:999px;background:var(--page);z-index:-1;}
[data-el="seedmark-pill"].on:has(.mark):not(:has(.icon)):before{background:var(--a1);border-color:var(--a1);}
[data-el="seedmark-pill"]:has(.mark):not(:has(.icon)) .parts{position:static;}
[data-el="seedmark-pill"]:has(.mark):not(:has(.icon)) .parts>.mark,[data-el="seedmark-pill"].on:has(.mark):not(:has(.icon)) .parts>.mark{position:absolute;left:50%;top:0;transform:translateX(-50%);height:26px;min-width:94px;padding:0 calc(var(--gap-sm)/2);background:var(--page);color:var(--ink);border:var(--stroke) solid var(--n-7);border-radius:var(--radius-sm);font-size:var(--type-12);}
[data-el="seedmark-pill"].on .parts:has(.note)>.name{font-size:var(--type-40);}
[data-el="seedmark-pill"].line:has(.mark):not(:has(.icon)) .name{font-size:var(--type-18);text-align:center;white-space:normal;}
[data-el="seedmark-pill"].on:not(:has(.mark,.note)) .name{font-size:var(--type-20);text-align:center;}
''')
p=C/'elements/card/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-card"] .parts{position:relative;}
[data-el="seedmark-card"] .parts>.bars{height:auto;min-height:120px;flex:1;}
[data-el="seedmark-card"] .parts>.stacks{height:80px;flex:none;padding:0;}
[data-el="seedmark-card"] .parts>.legend{height:30px;flex:none;padding:0;}
[data-el="seedmark-card"] .parts:has(>.bars)>.tag{position:absolute;right:0;top:calc(var(--pad)*2);padding:0;border:0;font-size:var(--type-22);}
[data-el="seedmark-card"] .parts:has(>.stacks)>.list{justify-content:flex-start;}
[data-el="seedmark-card"] .parts:has(>.stacks)>.list .item .name{font-size:var(--type-16);font-weight:var(--body-weight);}
@container(max-height:220px) and (min-width:300px){[data-el="seedmark-card"]:has(>.parts>.mark):not(:has(>.parts>.kick)){padding:var(--gap-sm) var(--gap);}[data-el="seedmark-card"] .parts:has(>.mark):not(:has(>.kick)){display:grid;grid-template-columns:54px minmax(0,1fr);grid-template-rows:32px minmax(0,1fr);gap:calc(var(--gap-sm)/2) var(--gap-sm);height:100%;}[data-el="seedmark-card"] .parts:has(>.mark):not(:has(>.kick))>.mark{grid-column:1;grid-row:1/span 2;align-self:center;width:54px;height:54px;min-width:54px;}[data-el="seedmark-card"] .parts:has(>.mark):not(:has(>.kick))>.name{grid-column:2;grid-row:1;border:0;font-size:var(--type-22);padding:0;}[data-el="seedmark-card"] .parts:has(>.mark):not(:has(>.kick))>.note{grid-column:2;grid-row:2;font-size:var(--type-16);}}
''')
patch('elements/prose/element.css','''
[data-el="seedmark-prose"]{justify-content:flex-start;padding:0;font-size:var(--type-16);color:var(--ink);line-height:calc(var(--body-line)*1.125)}
[data-el="seedmark-prose"].quiet{font-size:var(--type-16);color:var(--ink)}
[data-el="seedmark-prose"].lead{font-size:var(--type-20)}
@container(max-width:260px){[data-el="seedmark-prose"]{font-size:var(--type-16)}}
''')
patch('elements/flowchart/element.css','''
[data-el="seedmark-flowchart"]:has(.node>[data-el]){padding:0;gap:var(--gap-sm);grid-template-rows:repeat(6,minmax(0,1fr));flex:3.4;}
[data-el="seedmark-flowchart"] .node:has(>[data-el]){padding:0;border:0;background:none;display:flex;}
[data-el="seedmark-flowchart"] .node>[data-el]{width:100%;height:100%;}
[data-el="seedmark-flowchart"] .node:has(>.card)>.card .parts>.note{text-align:center;font-size:var(--type-18);line-height:var(--body-line);}
[data-el="seedmark-flowchart"] .node.to-r:after{width:calc(var(--gap-sm)*2);background:var(--ink);z-index:4;}
[data-el="seedmark-flowchart"] .node.to-d:before,[data-el="seedmark-flowchart"] .node.to-u:before{height:calc(var(--gap-sm)*2);background:var(--ink);z-index:4;}
[data-el="seedmark-flowchart"] .node.to-l:after{width:calc(var(--gap-sm)*2);background:var(--ink);z-index:4;}
''')
patch('elements/steps/element.css','''
[data-el="seedmark-steps"]:has(.mark>.icon){padding:0 calc(var(--pad)*3.5);gap:0;isolation:isolate}
[data-el="seedmark-steps"]:has(.mark>.icon) .step{grid-template-rows:92px 26px minmax(0,1fr);gap:0;justify-content:start}
[data-el="seedmark-steps"]:has(.mark>.icon) .mark{height:92px;width:92px;min-width:92px;align-self:center;position:relative;z-index:2;}
[data-el="seedmark-steps"] .mark>.icon{width:50px;height:50px;}
[data-el="seedmark-steps"]:has(.mark>.icon) .step>.name{position:relative;margin-top:calc(var(--gap-sm)*-.75);border:var(--stroke) solid var(--n-7);border-radius:var(--radius-sm);background:var(--page);font-size:var(--type-12);padding:calc(var(--gap-sm)/4) calc(var(--gap-sm)/2);width:auto;z-index:3}
[data-el="seedmark-steps"]:has(.mark>.icon) .step>.note{font-size:var(--type-16);text-align:center;max-width:90%;margin-top:var(--gap-sm);}
[data-el="seedmark-steps"]:has(.mark>.icon) .step:not(:last-child):after{top:46px;z-index:0;}
[data-el="seedmark-steps"]:has(.mark>.icon):before{content:'';position:absolute;top:46px;left:4.5%;right:4.5%;bottom:0;border:var(--stroke) solid var(--n-3);border-top:0;border-radius:0 0 999px 999px;z-index:-1;}
@container(max-height:150px){[data-el="seedmark-steps"]:has(.mark>.icon) .step{grid-template-rows:72px 22px minmax(0,1fr)}[data-el="seedmark-steps"]:has(.mark>.icon) .mark{width:72px;height:72px;min-width:72px}[data-el="seedmark-steps"] .mark>.icon{width:40px;height:40px}[data-el="seedmark-steps"]:has(.mark>.icon) .step>.note{font-size:var(--type-14)}[data-el="seedmark-steps"]:has(.mark>.icon) .step:not(:last-child):after,[data-el="seedmark-steps"]:has(.mark>.icon):before{top:36px}}
''')
patch('elements/headline/element.css','''[data-el="seedmark-headline"].big h2{font-size:var(--type-64);font-weight:var(--name-weight)}[data-el="seedmark-headline"] h2{font-size:var(--type-44);font-weight:var(--title-weight)}[data-el="seedmark-headline"] .note{font-size:var(--type-28)}[data-el="seedmark-headline"]{padding:0;justify-content:flex-start}''')
patch('elements/agenda/element.css','''[data-el="seedmark-agenda"]{display:flex;flex-direction:column;gap:0;padding:0;border-top:2px solid var(--ink)}[data-el="seedmark-agenda"] .entry{flex:1;border-top:0;border-bottom:var(--stroke) solid var(--n-2);padding:calc(var(--gap-sm)/2) 0;gap:var(--gap-sm);align-items:center}[data-el="seedmark-agenda"] .entry .name{font-size:var(--type-24);font-weight:var(--body-weight)}[data-el="seedmark-agenda"] .entry .mark{font-size:var(--type-14)}''')
patch('elements/metric/element.css','''[data-el="seedmark-metric"].stat .parts{height:100%;display:grid;grid-template-columns:30% minmax(0,1fr);grid-template-rows:auto auto;align-content:center;gap:0 var(--gap-sm);}[data-el="seedmark-metric"].stat .fig{font-size:var(--type-32);grid-column:1;grid-row:1}[data-el="seedmark-metric"].stat .name{font-size:var(--type-16);font-weight:var(--body-weight);grid-column:1;grid-row:2}[data-el="seedmark-metric"].stat .note{font-size:var(--type-18);grid-column:2;grid-row:1/span 2;color:var(--ink)}[data-el="seedmark-metric"].stat{border-bottom:var(--stroke) solid var(--n-3);padding:var(--gap-sm) 0;}@container(max-height:90px){[data-el="seedmark-metric"].stat .fig{font-size:var(--type-28)}[data-el="seedmark-metric"].stat .note{font-size:var(--type-16)}}''')
patch('elements/callout/element.css','''[data-el="seedmark-callout"]{padding:var(--gap-sm);font-size:var(--type-18);}[data-el="seedmark-callout"] p{font-size:var(--type-18);line-height:var(--body-line);}''')
patch('elements/timeline/element.css','''
[data-el="seedmark-timeline"]:has(.stop>.name>.frame){display:flex;align-items:stretch;gap:var(--gap-sm);padding:0;border-bottom:var(--stroke) solid var(--n-3);}
[data-el="seedmark-timeline"]:has(.stop>.name>.frame) .stop{position:relative;flex:1;min-width:0;display:grid;grid-template-rows:124px 60px minmax(0,1fr);border:0;border-left:var(--stroke) solid var(--n-2);padding:0 var(--gap-sm);gap:var(--gap);}
[data-el="seedmark-timeline"]:has(.stop>.name>.frame) .stop:before{display:none;}
[data-el="seedmark-timeline"]:has(.stop>.name>.frame) .stop>.name{grid-row:1;grid-column:1;display:block;height:100%;width:100%;}
[data-el="seedmark-timeline"]:has(.stop>.name>.frame) .name>.frame{padding:0;border:0;border-radius:999px;overflow:hidden;width:100%;height:100%;}
[data-el="seedmark-timeline"]:has(.stop>.name>.frame) .name>.frame>.seat{width:100%;height:100%;aspect-ratio:auto;border-radius:999px;max-width:none;max-height:none;}
[data-el="seedmark-timeline"]:has(.stop>.name>.frame) .stop>.kick{grid-row:2;grid-column:1;display:flex;align-items:center;justify-content:center;position:relative;width:100%;font-size:var(--type-16);font-weight:var(--name-weight);color:var(--ink);background:var(--n-1);border-radius:var(--radius);padding:calc(var(--gap-sm)/2);white-space:nowrap;}
[data-el="seedmark-timeline"]:has(.stop>.name>.frame) .stop>.kick:empty{visibility:hidden;}
[data-el="seedmark-timeline"]:has(.stop>.name>.frame) .stop:has(+.stop>.kick:empty)>.kick{width:calc(200% + var(--gap)*1.5);z-index:2;}
[data-el="seedmark-timeline"]:has(.stop>.name>.frame) .stop.on>.kick{background:var(--ink);color:var(--page);}
[data-el="seedmark-timeline"]:has(.stop>.name>.frame) .stop>.note{grid-row:3;grid-column:1;font-size:var(--type-18);color:var(--ink);display:block;}
@container(max-height:300px){[data-el="seedmark-timeline"]:has(.stop>.name>.frame) .stop{grid-template-rows:80px 44px minmax(0,1fr);gap:var(--gap-sm);}[data-el="seedmark-timeline"]:has(.stop>.name>.frame) .stop>.note{font-size:var(--type-14);}[data-el="seedmark-timeline"]:has(.stop>.name>.frame) .stop>.kick{font-size:var(--type-12);}}
''')
patch('elements/person/element.css','''
[data-el="seedmark-person"].people{gap:var(--gap);align-items:stretch;}
[data-el="seedmark-person"].people>.person{height:100%;padding:var(--gap-lg) 0 0;gap:calc(var(--gap-sm)/2);justify-content:flex-start;}
[data-el="seedmark-person"].people>.person>.seat{width:190px;height:190px;max-height:none;max-width:none;flex:none;margin-bottom:calc(var(--gap-sm)*.666667);}
[data-el="seedmark-person"].people:has(>.person:nth-child(5):last-child)>.person:nth-child(3){padding-top:0;}
[data-el="seedmark-person"].people:has(>.person:nth-child(5):last-child)>.person:nth-child(3)>.seat{width:226px;height:226px;}
[data-el="seedmark-person"].people .person>.name{font-size:var(--type-28);line-height:var(--figure-line);}
[data-el="seedmark-person"].people .person>.note{font-size:var(--type-14);line-height:var(--label-line);}
[data-el="seedmark-person"].people .person>.list{height:auto;min-height:0;margin-top:var(--gap-sm);padding:0;font-size:var(--type-18);}
[data-el="seedmark-person"].people .list .item{padding:0;border:0;}
[data-el="seedmark-person"].people .list .item .name{font-size:var(--type-18);font-weight:var(--body-weight);}
@container seedmark-people (max-width:700px){[data-el="seedmark-person"].people>.person>.seat{width:96px;height:96px;max-width:100%;}[data-el="seedmark-person"].people:has(>.person:nth-child(5):last-child)>.person:nth-child(3)>.seat{width:116px;height:116px;max-width:110%;}[data-el="seedmark-person"].people .person>.name{font-size:var(--type-20);}[data-el="seedmark-person"].people .list .item .name{font-size:var(--type-12);}}
''')
patch('elements/venn/element.css','''
[data-el="seedmark-venn"]:has(.set>.name>.icon){padding:0;}
[data-el="seedmark-venn"]:has(.set>.name>.icon) .set{height:100%;max-height:100%;width:27%;padding:var(--gap);margin-left:var(--seedmark-venn-overlap);background:var(--page);}
[data-el="seedmark-venn"]:has(.set>.name>.icon) .set:nth-child(2){height:100%;width:53%;border-radius:999px;border-color:var(--ink);}
[data-el="seedmark-venn"]:has(.set>.name>.icon) .set>.name{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:calc(var(--gap-sm)/2);font-size:var(--type-20);font-weight:var(--body-weight);max-width:100%;}
[data-el="seedmark-venn"]:has(.set>.name>.icon) .set:nth-child(2)>.name{font-weight:var(--name-weight);}
[data-el="seedmark-venn"] .set .name>.icon{width:38px;height:38px;}
[data-el="seedmark-venn"] .set .name>.tag{border:0;font-size:var(--type-12);font-weight:var(--body-weight);}
[data-el="seedmark-venn"]:has(>.core):has(>.set:nth-child(3)){isolation:isolate;--seedmark-venn-d:min(52cqw,68cqh);}
[data-el="seedmark-venn"]:has(>.core):has(>.set:nth-child(3))>.set{width:var(--seedmark-venn-d);height:var(--seedmark-venn-d);border:var(--stroke) solid var(--page);}
[data-el="seedmark-venn"]:has(>.core):has(>.set:nth-child(3))>.set:nth-child(1){top:0;left:50%;transform:translateX(-50%);}
[data-el="seedmark-venn"]:has(>.core):has(>.set:nth-child(3))>.set:nth-child(2){left:calc(50% - var(--seedmark-venn-d)*.8);top:calc(var(--seedmark-venn-d)*.55);bottom:auto;}
[data-el="seedmark-venn"]:has(>.core):has(>.set:nth-child(3))>.set:nth-child(3){left:calc(50% - var(--seedmark-venn-d)*.2);top:calc(var(--seedmark-venn-d)*.55);bottom:auto;}
[data-el="seedmark-venn"]:has(>.core):has(>.set:nth-child(3)):before{content:'';position:absolute;left:calc(50% - var(--seedmark-venn-d)*.5);top:0;width:var(--seedmark-venn-d);height:var(--seedmark-venn-d);border-radius:50%;background:var(--ink);mask-image:radial-gradient(circle calc(var(--seedmark-venn-d)*.5) at 20% 105%,var(--ink) 99%,transparent),radial-gradient(circle calc(var(--seedmark-venn-d)*.5) at 80% 105%,var(--ink) 99%,transparent);z-index:1;}
[data-el="seedmark-venn"]:has(>.core):has(>.set:nth-child(3)):after{content:'';position:absolute;left:calc(50% - var(--seedmark-venn-d)*.8);top:calc(var(--seedmark-venn-d)*.55);width:var(--seedmark-venn-d);height:var(--seedmark-venn-d);border-radius:50%;background:var(--ink);mask-image:radial-gradient(circle calc(var(--seedmark-venn-d)*.5) at 110% 50%,var(--ink) 99%,transparent);z-index:1;}
[data-el="seedmark-venn"]:has(>.core):has(>.set:nth-child(3)) .set>.name{position:relative;z-index:2;color:var(--n-7);font-size:var(--type-18);}
[data-el="seedmark-venn"]:has(>.core):has(>.set:nth-child(3)) .core{top:48%;width:25%;height:25%;padding:0;max-width:none;border:0;border-radius:50%;z-index:3;display:flex;align-items:center;justify-content:center;font-size:var(--type-18);}
''')
patch('elements/chart-donut/element.css','''
[data-el="seedmark-chart-donut"].donut{--seedmark-donut-angle:calc(var(--seedmark-donut-start) + var(--v)*1.8deg);}
[data-el="seedmark-chart-donut"].donut:after{background:conic-gradient(from var(--seedmark-donut-start),var(--a1) calc(var(--v)*1%),color-mix(in srgb,var(--n-3) calc((1 - var(--seedmark-donut-layer))*100%),transparent) 0);}
[data-el="seedmark-chart-donut"].donut:before{width:calc(min(90cqw,90cqh)*var(--seedmark-donut-hole)/100);height:calc(min(90cqw,90cqh)*var(--seedmark-donut-hole)/100);}
[data-el="seedmark-chart-donut"].donut:has(.name>.icon){background:none;pointer-events:none;}
[data-el="seedmark-chart-donut"].donut:has(.name>.icon):before{display:none;}
[data-el="seedmark-chart-donut"].donut:has(.name>.icon):after{width:min(100cqw,100cqh);height:min(100cqw,100cqh);}
[data-el="seedmark-chart-donut"].donut:has(.name>.icon)>.fig{position:absolute;left:calc(50% + sin(var(--seedmark-donut-angle))*min(30cqw,30cqh));top:calc(50% - cos(var(--seedmark-donut-angle))*min(30cqw,30cqh) + var(--gap));transform:translate(-50%,-50%);font-size:var(--type-26);}
[data-el="seedmark-chart-donut"].donut:has(.name>.icon)>.name{position:absolute;left:calc(50% + sin(var(--seedmark-donut-angle))*min(30cqw,30cqh));top:calc(50% - cos(var(--seedmark-donut-angle))*min(30cqw,30cqh) - var(--gap));transform:translate(-50%,-50%);padding:0;border:0;background:none;}
[data-el="seedmark-chart-donut"].donut .name>.icon{width:44px;height:44px;}
[data-el="seedmark-chart-donut"].donut.tone-1{color:var(--a1-on);}
[data-el="seedmark-chart-donut"].donut.tone-2{color:var(--page);}
[data-el="seedmark-chart-donut"].donut.tone-2:after{background:conic-gradient(from var(--seedmark-donut-start),var(--n-7) calc(var(--v)*1%),transparent 0);}
[data-el="seedmark-chart-donut"].donut.tone-3:after{background:conic-gradient(from var(--seedmark-donut-start),var(--n-4) calc(var(--v)*1%),transparent 0);}
[data-el="seedmark-chart-donut"].donut.tone-5:after{background:conic-gradient(from var(--seedmark-donut-start),var(--n-3) calc(var(--v)*1%),transparent 0);}
''')
meta=C/'elements/chart-donut/element.json';d=json.loads(meta.read_text());d['tokenDefaults'].update({'--seedmark-donut-start':'0deg','--seedmark-donut-hole':80,'--seedmark-donut-layer':0});meta.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
patch('elements/tag/element.css','''[data-el="seedmark-tag"].tag{justify-self:center;align-self:center;width:max-content;max-width:100%;height:auto;min-height:26px;display:inline-flex;align-items:center;justify-content:center;font-size:var(--type-12);padding:calc(var(--gap-sm)/4) calc(var(--gap-sm)/2);background:var(--page);color:var(--ink);border:var(--stroke) solid var(--n-7);border-radius:var(--radius-sm);text-align:center;}''')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'.stack{position:relative;}')
p=C/'elements/chart-donut/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-chart-donut"].donut:has(.name>.icon){position:absolute;inset:0;width:100%;height:100%;}
[data-el="seedmark-chart-donut"].donut.tone-1 .name{color:var(--a1-on);}
[data-el="seedmark-chart-donut"].donut.tone-2 .name{color:var(--page);}
''')
p=C/'elements/metric/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-metric"].stat:has(.note>[data-el="seedmark-prose"]){padding:var(--gap) 0 0;border:0;}
[data-el="seedmark-metric"].stat:has(.note>[data-el="seedmark-prose"]) .parts{grid-template-columns:100px minmax(0,1fr);grid-template-rows:64px minmax(0,1fr);gap:0;align-content:stretch;}
[data-el="seedmark-metric"].stat:has(.note>[data-el="seedmark-prose"]) .fig{font-size:var(--type-40);grid-row:1;align-self:start;}
[data-el="seedmark-metric"].stat:has(.note>[data-el="seedmark-prose"]) .name{font-size:var(--type-16);font-weight:var(--name-weight);grid-column:2;grid-row:1;align-self:start;padding-top:var(--gap-sm);}
[data-el="seedmark-metric"].stat:has(.note>[data-el="seedmark-prose"]) .note{display:block;grid-row:2;grid-column:1/span 2;}
''')
p=C/'elements/card/element.css';p.write_text(p.read_text()+'''
@container(max-height:220px) and (min-width:400px){[data-el="seedmark-card"] .parts:has(>.kick):not(:has(>.mark)){grid-template-columns:26% minmax(0,1fr);}[data-el="seedmark-card"] .parts:has(>.kick):not(:has(>.mark))>.name{font-size:var(--type-28);}[data-el="seedmark-card"] .parts:has(>.kick):not(:has(>.mark))>.note{font-size:var(--type-18);}}
[data-el="seedmark-card"].quiet:has(>.parts>.kick):not(:has(>.parts>.mark)){padding:0;border:0;border-bottom:var(--stroke) solid var(--n-3);background:none;}
[data-el="seedmark-card"].quiet .parts:has(>.kick):not(:has(>.mark)){grid-template-columns:38% minmax(0,1fr);grid-template-rows:26px minmax(0,1fr);gap:0 var(--gap-sm);}
[data-el="seedmark-card"].quiet .parts:has(>.kick):not(:has(>.mark))>.note{font-size:var(--type-18);}
''')
p=C/'elements/headline/element.css';p.write_text(p.read_text()+'''[data-el="seedmark-headline"]:not(.big):not(:has(h2>b)) h2{font-size:var(--type-28);font-weight:var(--name-weight);}''')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
.head:not(:has(.title)){height:42px;}
.cover .lockup .kicker{font-weight:var(--title-weight);}
.stack>.stack{flex:3;}
''')
p=C/'elements/prose/element.css';p.write_text(p.read_text()+'''[data-el="seedmark-prose"]:has(.tag){justify-content:space-between;padding:var(--gap-sm) 0 var(--gap);}[data-el="seedmark-prose"]:has(.tag)>p:last-child{font-size:var(--type-12);}[data-el="seedmark-prose"] .tag{min-width:94px;}''')
p=C/'elements/headline/element.css';p.write_text(p.read_text()+'''[data-el="seedmark-headline"].big{padding:var(--gap-sm) 0 0;gap:var(--gap);}[data-el="seedmark-headline"].big h2{line-height:var(--figure-line);}[data-el="seedmark-headline"]:has(h2>b){flex:2;}''')
p=C/'elements/agenda/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-agenda"]:has(>.entry:nth-child(7)){display:grid;grid-auto-flow:column;grid-template-rows:repeat(6,minmax(0,1fr));grid-template-columns:repeat(2,minmax(0,1fr));padding:calc(var(--gap-sm)*1.5) 0 0 calc(var(--pad)*1.5);column-gap:calc(var(--pad)*1.5);border:0;}
[data-el="seedmark-agenda"] .entry{display:grid;grid-template-columns:24px minmax(0,1fr);gap:var(--gap-sm);min-width:0;}
[data-el="seedmark-agenda"]:has(>.entry:nth-child(7))>.entry:first-child,[data-el="seedmark-agenda"]:has(>.entry:nth-child(7))>.entry:nth-child(7){border-top:2px solid var(--ink);}
[data-el="seedmark-agenda"]:has(>.entry:nth-child(7)) .name{font-size:var(--type-24);white-space:nowrap;}
@container(max-width:620px){[data-el="seedmark-agenda"]:has(>.entry:nth-child(7)) .name{font-size:var(--type-20);white-space:normal;}}
''')
p=C/'elements/pill/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-pill"].line:has(.parts>.note):has(.icon){height:126px;flex:none;padding:var(--gap-sm) var(--gap-sm) var(--gap-sm) calc(var(--pad)*1.5);}
[data-el="seedmark-pill"].line:has(.parts>.note):has(.icon):first-child{margin-top:var(--gap-sm);}
[data-el="seedmark-pill"].line:has(.parts>.note):has(.icon) .note{font-size:var(--type-16);max-width:74%;}
''')
p=C/'elements/venn/element.css';p.write_text(p.read_text()+'''[data-el="seedmark-venn"]:has(.set>.name>.icon){padding:var(--gap-sm) 0 0;}[data-el="seedmark-venn"]:has(.set>.name>.icon) .tag{border:0;background:none;min-height:0;}''')
p=C/'elements/concentric/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-concentric"]{padding:0;}
[data-el="seedmark-concentric"] .ring{left:0;top:calc(50% + var(--gap-sm));width:min(87.5cqw,96cqh);height:auto;padding:0 calc(var(--gap-sm)*1.333333) 0 0;}
[data-el="seedmark-concentric"] .ring:nth-child(2){width:min(61.6cqw,67.6cqh);padding:0;}
[data-el="seedmark-concentric"] .ring:nth-child(3){width:min(41.2cqw,45.4cqh);padding:0;align-items:center;}
[data-el="seedmark-concentric"] .ring .name{font-size:var(--type-30);width:108px;max-width:100%;}
[data-el="seedmark-concentric"] .ring .fig{font-size:var(--type-14);font-weight:var(--body-weight);width:108px;max-width:100%;}
@container(max-width:400px){[data-el="seedmark-concentric"] .ring .name{font-size:var(--type-20);}[data-el="seedmark-concentric"] .ring .fig{font-size:var(--type-12);}}
''')
p=C/'elements/chart-donut/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-chart-donut"].donuts>.donut{padding:0;}
[data-el="seedmark-chart-donut"].donuts>.donut:after{width:min(95cqw,95cqh);height:min(95cqw,95cqh);}
[data-el="seedmark-chart-donut"].donuts>.donut:before{width:min(76cqw,76cqh);height:min(76cqw,76cqh);}
[data-el="seedmark-chart-donut"].donuts.line{isolation:isolate;}
[data-el="seedmark-chart-donut"].donuts.line:before{content:'';position:absolute;left:10%;right:10%;top:50%;height:var(--stroke);background:var(--n-3);z-index:-1;}
''')
p=C/'elements/flowchart/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-flowchart"]:has(.node.end):has(.node .card){padding:var(--pad) 0 0 var(--pad);grid-template-rows:repeat(4,minmax(0,1fr));row-gap:var(--gap);}
[data-el="seedmark-flowchart"] .node:has(>.stack){border:0;padding:0;background:none;}
[data-el="seedmark-flowchart"] .node>.stack{width:100%;height:100%;gap:var(--gap-sm);}
[data-el="seedmark-flowchart"] .node>.stack>.pill{height:47px;flex:none;padding:0;}
[data-el="seedmark-flowchart"] .node>.stack>.pill .name{font-size:var(--type-18);}
[data-el="seedmark-flowchart"] .node:has(>br){align-self:start;margin-top:var(--gap);height:138px;}
[data-el="seedmark-flowchart"] .node.end{border-radius:var(--radius);}
[data-el="seedmark-flowchart"]:has(.node.end):has(.node .card) .node.to-r:not(:has(>[data-el])):after{width:calc(var(--pad)*2);height:calc(200% + var(--gap)*2);clip-path:none;border-top:var(--stroke) solid var(--ink);border-right:var(--stroke) solid var(--ink);background:none;top:50%;transform:none;}
[data-el="seedmark-flowchart"]:has(.node.end):has(.node .card) .node.to-r:has(>[data-el]):after{width:var(--gap);height:calc(100% + var(--gap));clip-path:none;border-top:var(--stroke) solid var(--ink);border-right:var(--stroke) solid var(--ink);background:none;top:50%;transform:none;}
''')
p=C/'elements/metric/element.css';p.write_text(p.read_text()+'''[data-el="seedmark-metric"].stat .note{font-size:var(--type-16);}[data-el="seedmark-metric"].stat .note>.prose{font-size:var(--type-16);line-height:var(--body-line);}''')
meta=C/'elements/venn/element.json';d=json.loads(meta.read_text());d['tokenDefaults']['--seedmark-venn-overlap']='-6.3%';meta.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
.group:has(>.stack:nth-child(4):last-child){gap:var(--gap-lg);position:relative;}
.group:has(>.stack:nth-child(4):last-child):before{content:'';position:absolute;left:1.5%;right:1.5%;top:53px;height:var(--stroke);background:var(--n-3);}
.group:has(>.stack:nth-child(4):last-child)>.stack{gap:calc(var(--gap) + var(--gap-sm)/4);}
.group:has(>.stack:nth-child(4):last-child)>.stack:after{content:'';position:absolute;left:50%;top:92px;height:27px;border-left:var(--stroke) dashed var(--n-3);}
''')
p=C/'elements/pill/element.css';p.write_text(p.read_text()+'''[data-el="seedmark-pill"].on:has(.mark):not(:has(.note,.icon)){height:92px;flex:none;}''')
p=C/'elements/card/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-card"]:has(>.parts>.note:only-child){padding:calc(var(--pad)*.9375);justify-content:flex-start;}
[data-el="seedmark-card"] .parts:has(>.note:only-child){justify-content:flex-start;height:100%;}
[data-el="seedmark-card"] .parts>.list .item{padding-left:var(--gap);}
[data-el="seedmark-card"] .parts>.list .item:before{left:calc(var(--gap-sm)/4);}
[data-el="seedmark-card"]:has(>.parts>.bars),[data-el="seedmark-card"]:has(>.parts>.stacks){margin-top:var(--gap-sm);height:calc(100% - var(--gap-sm));}
[data-el="seedmark-card"] .parts>.bars{padding:var(--gap-sm) 0 var(--gap);gap:calc(var(--gap-sm)/2);}
[data-el="seedmark-card"] .parts:has(>.bars)>.legend{position:absolute;top:calc(var(--pad)*3);left:0;width:100%;height:30px;justify-content:flex-start;z-index:3;}
[data-el="seedmark-card"] .parts:has(>.bars)>.tag{top:calc(var(--pad)*1.75);}
''')
p=C/'elements/chart-donut/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-chart-donut"].donut:has(.name>.icon){padding:0;--seedmark-donut-cy:calc(100% - min(50cqw,50cqh));}
[data-el="seedmark-chart-donut"].donut:has(.name>.icon):after{top:var(--seedmark-donut-cy);background-image:conic-gradient(from var(--seedmark-donut-start),transparent 0deg 1deg,var(--a1) 1deg calc(var(--v)*3.6deg - 1deg),transparent calc(var(--v)*3.6deg - 1deg));}
[data-el="seedmark-chart-donut"].donut:has(.name>.icon)>.fig{top:calc(var(--seedmark-donut-cy) - cos(var(--seedmark-donut-angle))*min(30cqw,30cqh) + var(--gap));}
[data-el="seedmark-chart-donut"].donut:has(.name>.icon)>.name{top:calc(var(--seedmark-donut-cy) - cos(var(--seedmark-donut-angle))*min(30cqw,30cqh) - var(--gap));}
[data-el="seedmark-chart-donut"].donut.tone-2:has(.name>.icon):after{background-image:conic-gradient(from var(--seedmark-donut-start),transparent 0deg 1deg,var(--n-7) 1deg calc(var(--v)*3.6deg - 1deg),transparent calc(var(--v)*3.6deg - 1deg));}
[data-el="seedmark-chart-donut"].donut.tone-3:has(.name>.icon):after{background-image:conic-gradient(from var(--seedmark-donut-start),transparent 0deg 1deg,var(--n-4) 1deg calc(var(--v)*3.6deg - 1deg),transparent calc(var(--v)*3.6deg - 1deg));}
[data-el="seedmark-chart-donut"].donut.tone-5:has(.name>.icon):after{background-image:conic-gradient(from var(--seedmark-donut-start),transparent 0deg 1deg,var(--n-3) 1deg calc(var(--v)*3.6deg - 1deg),transparent calc(var(--v)*3.6deg - 1deg));}
''')
p=C/'elements/flowchart/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-flowchart"]:has(.node>.card):not(:has(.node.end)){column-gap:var(--gap-lg);}
[data-el="seedmark-flowchart"] .node>.card:has(>.parts>.note:only-child){padding:var(--gap-sm);}
[data-el="seedmark-flowchart"] .node>.card .parts:has(>.note:only-child){justify-content:center;}
[data-el="seedmark-flowchart"]:has(.node>.card):not(:has(.node.end)) .node.to-r:after{width:var(--gap-lg);}
[data-el="seedmark-flowchart"]:has(.node>.card):not(:has(.node.end)) .node.to-r:has(>.card):after{height:calc(125% + var(--gap-sm)/4);top:50%;transform:none;clip-path:none;background:linear-gradient(var(--ink),var(--ink)) left top/100% 1.5px no-repeat,linear-gradient(to bottom right,transparent calc(50% - 1px),var(--ink) calc(50% - 1px),var(--ink) calc(50% + 1px),transparent calc(50% + 1px)) center/100% 100% no-repeat,linear-gradient(var(--ink),var(--ink)) left bottom/100% 1.5px no-repeat;}
[data-el="seedmark-flowchart"]:has(.node>.card):not(:has(.node.end)) .node.to-r:has(>.card.quiet):after{height:calc(80% + var(--gap-sm)/4);}
''')
p=C/'elements/chart-donut/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-chart-donut"].donuts{padding:0;}
[data-el="seedmark-chart-donut"].donuts:not(.line) .donut .name{border:0;background:none;padding:0;font-size:var(--type-14);}
[data-el="seedmark-chart-donut"].donuts:not(.line) .donut .name:after{content:'';position:absolute;left:50%;top:100%;height:30px;width:8px;background:var(--n-7);clip-path:polygon(40% 0,60% 0,60% 85%,100% 85%,50% 100%,0 85%,40% 85%);}
@container(max-width:700px){[data-el="seedmark-chart-donut"].donuts>.donut{height:95%;}}
''')
p=C/'elements/card/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-card"].quiet:has(>.parts>.bars){margin:0;height:100%;padding:var(--gap-sm) 0 0 var(--gap);background:none;border:0;}
[data-el="seedmark-card"].quiet .parts:has(>.bars){gap:calc(var(--gap-sm)/3);}
[data-el="seedmark-card"].quiet .parts:has(>.bars)>.tag{top:var(--gap);}
''')
p=C/'elements/prose/element.css';p.write_text(p.read_text()+'''
.group>[data-el="seedmark-prose"]{padding-top:var(--gap);text-align:center;}
.stack>[data-el="seedmark-prose"]{height:100px;flex:none;}
''')
p=C/'elements/headline/element.css';p.write_text(p.read_text()+''' .stack>[data-el="seedmark-headline"]:not(:has(h2>b)){height:52px;flex:none;padding-top:var(--gap-sm);}''')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
.stack:has(>[data-el="seedmark-chart-area"]),.stack:has(>[data-el="seedmark-chart-line"]),.stack:has(>[data-el="seedmark-chart-bar"]){gap:calc(var(--gap-sm)/2);}
''')
patch('elements/chart-area/element.css','''[data-el="seedmark-chart-area"] .series>.name:empty{display:none;}''')
p=C/'elements/tag/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-tag"].tag.line{position:relative;align-self:stretch;justify-self:center;width:46px;height:100%;background:none;border:0;padding:0;display:block;font-size:var(--type-12);text-align:center;}
[data-el="seedmark-tag"].tag.line>span{display:inline-flex;align-items:center;justify-content:center;border:var(--stroke) solid var(--n-7);border-radius:var(--radius-sm);background:var(--page);padding:calc(var(--gap-sm)/4) calc(var(--gap-sm)/2);}
[data-el="seedmark-tag"].tag.line:after{content:'';position:absolute;left:50%;top:26px;bottom:0;border-left:2px dotted var(--ink);}
''')
p=C/'elements/list/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-list"]{flex:3;}
[data-el="seedmark-list"] .item:has(>.mark){padding-left:calc(var(--pad)*2);}
[data-el="seedmark-list"] .item:has(>.mark):before{display:none;}
[data-el="seedmark-list"] .item>.mark{top:50%;left:0;transform:translateY(-50%);width:54px;height:54px;border-radius:50%;background:var(--ink);color:var(--page);display:flex;align-items:center;justify-content:center;}
[data-el="seedmark-list"] .item>.mark>.icon{width:30px;height:30px;}
[data-el="seedmark-list"] .item:has(>.mark)>.name{font-size:var(--type-20);font-weight:var(--body-weight);}
''')
p=C/'elements/positioning/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-positioning"]{width:calc(100% - var(--gap)*2);height:calc(100% - var(--gap-sm));margin-top:var(--gap-sm);}
[data-el="seedmark-positioning"] .mark:not(.on){width:48px;height:48px;}
[data-el="seedmark-positioning"] .mark:not(.on) .name{position:absolute;top:calc(100% + var(--gap-sm)/3);left:50%;transform:translateX(-50%);font-size:var(--type-12);white-space:nowrap;}
[data-el="seedmark-positioning"] .mark.on{width:159px;height:84px;}
[data-el="seedmark-positioning"] .mark.on .name{font-size:var(--type-16);}
''')
p=C/'elements/person/element.css';p.write_text(p.read_text()+'''[data-el="seedmark-person"].people{container-name:seedmark-people;}[data-el="seedmark-person"].people .person>.list{height:80px;gap:0;flex:none;}''')
p=C/'elements/pill/element.css';p.write_text(p.read_text()+'''[data-el="seedmark-pill"].quiet:has(.icon) .parts{flex-wrap:nowrap;gap:calc(var(--gap-sm)/3);}''')
p=C/'elements/flowchart/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-flowchart"]:has(.node.end):has(.node .card) .node.to-r:has(>br):after{display:none;}
[data-el="seedmark-flowchart"]:has(.node.end):has(.node .card) .node.to-r:has(>br):before{content:'';position:absolute;left:100%;top:0;width:var(--gap);height:118px;transform:none;clip-path:none;background:linear-gradient(to top right,transparent calc(50% - 1px),var(--ink) calc(50% - 1px),var(--ink) calc(50% + 1px),transparent calc(50% + 1px)) left top/100% 50% no-repeat,linear-gradient(to bottom right,transparent calc(50% - 1px),var(--ink) calc(50% - 1px),var(--ink) calc(50% + 1px),transparent calc(50% + 1px)) left bottom/100% 50% no-repeat,linear-gradient(var(--ink),var(--ink)) left center/100% 1.5px no-repeat;}
[data-el="seedmark-flowchart"]:has(.node.end) .node>.card:has(>.parts>.group){padding:0;}
[data-el="seedmark-flowchart"]:has(.node.end) .pill.quiet:has(.icon){padding:0;}
[data-el="seedmark-flowchart"]:has(.node.end) .pill.quiet:has(.icon) .mark{width:32px;height:32px;min-width:32px;}
[data-el="seedmark-flowchart"]:has(.node.end) .pill.quiet:has(.icon) .mark>.icon{width:26px;height:26px;}
[data-el="seedmark-flowchart"]:has(.node.end) .pill.quiet:has(.icon) .name{font-size:var(--type-10);}
[data-el="seedmark-flowchart"] .node>.stack>.pill.line{border-radius:var(--radius-sm);}
''')
p=C/'elements/metric/element.css';p.write_text(p.read_text()+'''[data-el="seedmark-metric"].stat .parts{grid-template-columns:28% minmax(0,1fr);}''')
p=C/'elements/chart-area/element.css';p.write_text(p.read_text()+'''[data-el="seedmark-chart-area"] .pt:after{content:'';position:absolute;left:anchor(var(--seedmark-self) center);top:anchor(var(--seedmark-self) top);transform:translate(-50%,-50%);width:6px;height:6px;border-radius:50%;background:var(--n-7);}''')
p=C/'elements/steps/element.css';p.write_text(p.read_text()+'''[data-el="seedmark-steps"]:has(.mark>.icon) .step{grid-template-columns:100%;}[data-el="seedmark-steps"]:has(.mark>.icon) .step>.note{width:100%;max-width:100%;font-size:var(--type-16);text-wrap:balance;}''')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''.foot{bottom:calc(var(--pad)*1.25);justify-content:center;}.foot .src{font-size:var(--type-10);color:var(--n-7);}''')
meta=C/'elements/pill/element.json';d=json.loads(meta.read_text());d['tokenDefaults']['--seedmark-cylinder-curve']='16%';meta.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=C/'elements/pill/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-pill"]:has(.icon[data-icon="database"]){height:132px;max-height:100%;max-width:98px;flex:none;border:0;background:none;isolation:isolate;}
[data-el="seedmark-pill"]:has(.icon[data-icon="database"]):after{content:'';position:absolute;inset:0 0 18px;border:var(--stroke) solid var(--ink);border-radius:50%/var(--seedmark-cylinder-curve);background:var(--page);z-index:-1;}
[data-el="seedmark-pill"]:has(.icon[data-icon="database"]) .parts:before{height:30%;}
[data-el="seedmark-pill"]:has(.icon[data-icon="database"]) .parts>.name{bottom:0;min-width:76px;}
''')
p=C/'elements/steps/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-steps"]:has(.mark>.icon) .step>.name{margin-top:calc(var(--gap)*-.75);}
[data-el="seedmark-steps"]:has(.mark>.icon) .step>.note{margin-top:calc(var(--gap-sm)*-.5);}
[data-el="seedmark-steps"]:has(.mark>.icon) .step:not(:last-child):after{left:calc(50% + 46px);right:calc(-50% + 46px);height:8px;top:42px;background:var(--ink);clip-path:polygon(0 40%,85% 40%,85% 0,100% 50%,85% 100%,85% 60%,0 60%);}
''')
p=C/'elements/card/element.css';p.write_text(p.read_text()+'''
@container(max-height:220px) and (min-width:300px){[data-el="seedmark-card"]:has(>.parts>.mark):not(:has(>.parts>.kick)){margin-top:calc(var(--gap-sm)*1.166667);height:calc(100% - var(--gap-sm)*1.166667);padding:var(--gap) var(--gap) var(--gap-sm);}}
[data-el="seedmark-card"].quiet:has(>.parts>.kick):not(:has(>.parts>.mark)){border-radius:0;}
[data-el="seedmark-card"].quiet .parts:has(>.kick):not(:has(>.mark))>.note{font-size:var(--type-16);}
[data-el="seedmark-card"]:has(>.parts>.list):not(:has(>.parts>.stacks)){margin-top:var(--gap-sm);height:calc(100% - var(--gap-sm));padding:var(--pad) calc(var(--pad)*.875);}
[data-el="seedmark-card"] .parts:has(>.list):not(:has(>.stacks)){display:grid;height:100%;grid-template-rows:26px 64px minmax(0,1fr) 80px;gap:calc(var(--gap-sm)/2);}
[data-el="seedmark-card"] .parts:has(>.list):not(:has(>.stacks))>.name{height:64px;}
[data-el="seedmark-card"] .parts:has(>.list):not(:has(>.stacks))>.note{margin-top:var(--gap-sm);}
[data-el="seedmark-card"] .parts:has(>.list):not(:has(>.stacks))>.list{grid-row:4;}
''')
p=C/'elements/metric/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-metric"].stat:has(.note>[data-el="seedmark-prose"]):first-child{height:196px;flex:none;padding-top:calc(var(--gap-sm)*1.5);}
[data-el="seedmark-metric"].stat:has(.note>[data-el="seedmark-prose"]):first-child:after{content:'';position:absolute;left:0;right:var(--gap-lg);bottom:0;height:var(--stroke);background:var(--n-3);}
[data-el="seedmark-metric"].stat:has(.note>[data-el="seedmark-prose"]):last-child{padding-top:calc(var(--gap-sm)*.75);}
''')
p=C/'elements/flowchart/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-flowchart"]:has(.node.end):has(.node .card) .node.to-l:after{content:'';position:absolute;left:50%;right:auto;top:100%;width:calc(100% + var(--pad)*1.25);height:calc(160% + var(--gap)*2);clip-path:none;transform:none;background:none;border-left:var(--stroke) solid var(--ink);border-bottom:var(--stroke) solid var(--ink);}
''')
p=C/'elements/prose/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-prose"].lead{font-size:var(--type-28);font-weight:var(--name-weight);line-height:var(--name-line);padding-top:var(--pad);}
.body>[data-el="seedmark-prose"].quiet{padding-top:var(--pad);}
''')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
.slide.overrides .body{margin-bottom:calc(var(--gap-sm)*.5833333333);}
.slide.overrides .body>.group,.group.overrides{display:grid;grid-template-columns:minmax(0,1fr) calc(var(--pad)*11.25) minmax(0,1fr);gap:var(--gap-lg);}
.slide.overrides .body>.group>.stack:last-child,.group.overrides>.stack:last-child{padding-left:var(--gap);}
''')
p=C/'elements/flowchart/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-flowchart"]:has(.node>.card):not(:has(.node.end)){grid-template-columns:minmax(0,min(calc(var(--pad)*9.4375),28%)) minmax(0,1fr) minmax(0,min(calc(var(--pad)*9.4375),28%));column-gap:calc(var(--gap-lg) + var(--stroke)*1.6666666667);}
[data-el="seedmark-flowchart"]:has(.node>.card):not(:has(.node.end)) .node.to-r:after{width:calc(var(--gap-lg) + var(--stroke)*1.6666666667);}
''')
p=C/'elements/pill/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-pill"]:has(.icon[data-icon="database"]){width:98px;flex:0 0 auto;}
''')
p=C/'elements/legend/element.css';base=p.read_text().split('/* SOURCE_FIDELITY_CORRECTION */')[0];p.write_text(base+'''
/* SOURCE_FIDELITY_CORRECTION */
[data-el="seedmark-legend"]{flex-direction:column;align-items:flex-start;justify-content:flex-start;gap:calc(var(--gap-sm)/3);}
[data-el="seedmark-legend"] .key{font-size:var(--type-12);}
''')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
.stack:has(>[data-el="seedmark-flowchart"]):has(>[data-el="seedmark-callout"]){gap:calc(var(--gap) + var(--gap-sm)/3);}

''')
p=C/'elements/flowchart/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-flowchart"]:has(.node>.card):not(:has(.node.end)){row-gap:calc(var(--gap-sm)*1.3333333333);flex:1;}
[data-el="seedmark-flowchart"]:has(.node>.card):not(:has(.node.end)) .node:has(>.card.quiet){height:calc(100% + var(--gap-sm)*.4166666667);align-self:start;}
[data-el="seedmark-flowchart"]:has(.node>.card):not(:has(.node.end)) .node:has(>.pill.on){height:calc(100% - var(--stroke)*1.3333333333);align-self:end;}
[data-el="seedmark-flowchart"]:has(.node>.card):not(:has(.node.end)) .node>.card:has(.pill.quiet){padding:var(--gap) calc(var(--pad)*.65625) var(--gap) calc(var(--pad)*.71875);}
[data-el="seedmark-flowchart"]:has(.node>.card):not(:has(.node.end)) .card .group:has(>.pill.quiet){gap:calc(var(--gap-sm)*1.25);}
[data-el="seedmark-flowchart"]:has(.node>.card):not(:has(.node.end)) .node>.card.quiet:has(.icon[data-icon="database"]){padding:calc(var(--pad)*.8125) calc(var(--pad)*1.265625) calc(var(--pad)*.71875);}
[data-el="seedmark-flowchart"]:has(.node>.card):not(:has(.node.end)) .card .group:has(.icon[data-icon="database"]){justify-content:space-between;gap:0;}
''')
p=C/'elements/pill/element.css';p.write_text(p.read_text()+'''
[data-el="seedmark-pill"]:has(.icon[data-icon="database"]){height:128px;}
[data-el="seedmark-pill"]:has(.icon[data-icon="database"]):after{bottom:16px;}
[data-el="seedmark-pill"]:has(.icon[data-icon="database"]) .parts>.name{width:76px;height:26px;display:flex;align-items:center;justify-content:center;}
''')
p=C/'elements/callout/element.css';p.write_text(p.read_text()+'''
.stack:has(>[data-el="seedmark-flowchart"])>[data-el="seedmark-callout"]{height:calc(var(--pad)*2.4375);flex:none;}
''')
print('Source fidelity CSS appended; golden fixtures unchanged.')
