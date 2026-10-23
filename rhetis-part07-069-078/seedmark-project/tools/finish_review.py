"""Narrow final review fixes; golden markup and source data remain intact."""
from pathlib import Path
import runpy
P=Path(__file__).parent;C=P/'seedmark';M='/* FINAL_FIDELITY_QA */'
runpy.run_path(str(P/'fidelity_pass.py'))
def add(rel,s):
 p=C/rel;p.write_text(p.read_text().split(M)[0]+'\n'+M+'\n'+s+'\n')
add('foundation/foundation.css','''
.slide.src .seat:after{content:none;}
.slide.src .title b:before,.slide.src .title b:after{width:14px;height:14px;left:-8px;top:-7px;}
.slide.src .title b:after{left:auto;right:-8px;top:auto;bottom:-7px;}
.slide.src.cover .title b:before,.slide.src.cover .title b:after{width:30px;height:30px;left:-16px;top:-15px;}
.slide.src.cover .title b:after{left:auto;right:-16px;top:auto;bottom:-15px;}
.slide.src .group:has(>.stack>[data-el="seedmark-chart-area"]){gap:calc(var(--pad)*1.875);display:grid;grid-template-columns:calc(var(--pad)*10.3125) calc(var(--pad)*10.3125) minmax(0,1fr);}
''')
add('elements/headline/element.css','''
.slide.src [data-el="seedmark-headline"] h2 b:before,.slide.src [data-el="seedmark-headline"] h2 b:after{width:14px;height:14px;}
.slide.src [data-el="seedmark-headline"].big h2 b:before,.slide.src [data-el="seedmark-headline"].big h2 b:after{width:16px;height:16px;}
''')
add('elements/card/element.css','''
[data-el="seedmark-card"].on .parts>.note{color:var(--a1-on);}
.slide.src [data-el="seedmark-card"].card .parts:has(>.kick):not(:has(>.mark))>.name{border:0;padding-bottom:0;}
.slide.src [data-el="seedmark-card"].card .parts:has(>.kick):not(:has(>.mark))>.name:after{display:none;}
.slide.src [data-el="seedmark-card"].card:has(>.parts>.bars){padding:var(--gap-sm) 0 0 calc(var(--pad)*.6875);height:100%;margin:0;border:0;}
.slide.src [data-el="seedmark-card"].card .parts:has(>.bars){display:grid;grid-template-columns:minmax(0,1fr);grid-template-rows:40px 26px minmax(0,1fr);gap:0;height:100%;}
.slide.src [data-el="seedmark-card"].card .parts:has(>.bars)>.name{grid-row:1;height:40px;border:0;padding:0;}
.slide.src [data-el="seedmark-card"].card .parts:has(>.bars)>.kick{grid-row:2;padding-top:calc(var(--gap-sm)/4);display:block;}
.slide.src [data-el="seedmark-card"].card .parts:has(>.bars)>.bars{grid-row:3;min-height:0;height:100%;padding:calc(var(--gap-sm)*1.1666666667) var(--gap-sm) var(--gap);}
.slide.src [data-el="seedmark-card"].card .parts:has(>.bars)>.legend{position:absolute;top:80px;left:var(--gap-sm);width:160px;height:36px;display:flex;flex-direction:column;align-items:flex-start;gap:0;z-index:3;}
.slide.src [data-el="seedmark-card"].card .parts:has(>.bars)>.tag{top:var(--gap);}
''')
add('elements/metric/element.css','''
.slide.src [data-el="seedmark-metric"]:not(:has(.note>[data-el])) .parts{grid-template-columns:25% minmax(0,1fr);}
.slide.src [data-el="seedmark-metric"]:not(:has(.note>[data-el])) .note{font-size:var(--type-16);line-height:calc(var(--body-line)*1.06);word-break:keep-all;}
''')
add('elements/steps/element.css','''
.slide.src [data-el="seedmark-steps"]:has(.mark>.icon):before{top:46px;border:var(--stroke) solid var(--n-3);border-radius:999px;}
.slide.src [data-el="seedmark-steps"]:has(.mark>.icon):after{content:'';position:absolute;inset:0;pointer-events:none;background:linear-gradient(135deg,transparent 50%,var(--n-4) 50%) 4.5% calc(50% + 23px)/8px 8px no-repeat,linear-gradient(315deg,transparent 50%,var(--n-4) 50%) 95.5% calc(50% + 23px)/8px 8px no-repeat;}
''')
add('elements/legend/element.css','''
.slide.src .body>[data-el="seedmark-legend"]{padding:calc(var(--gap-sm)*1.3333333333) 0 0 calc(var(--pad)*1.09375);display:flex;flex-direction:column;flex-wrap:nowrap;gap:0;}
''')
add('elements/chart-bar/element.css','''
.slide.src [data-el="seedmark-chart-bar"]{background:none;isolation:isolate;}
.slide.src [data-el="seedmark-chart-bar"]:after{content:'';position:absolute;inset:var(--gap-lg) var(--gap) var(--gap-lg);background:repeating-linear-gradient(to bottom,var(--n-3) 0 var(--stroke),transparent var(--stroke) 20%);border-bottom:var(--stroke) solid var(--n-3);z-index:-1;}
.slide.src [data-el="seedmark-card"].card [data-el="seedmark-chart-bar"]:after{inset:calc(var(--gap-sm)*1.1666666667) var(--gap-sm) var(--gap);}
.slide.src .stack>[data-el="seedmark-chart-bar"]{padding:calc(var(--pad)*.8125) var(--gap-sm) calc(var(--pad)*1.625);}
.slide.src .stack>[data-el="seedmark-chart-bar"]:after{inset:26px var(--gap-sm) 52px;}
''')
add('elements/chart-area/element.css','''
.slide.src [data-el="seedmark-chart-area"] .axis>span{visibility:visible;}
.slide.src .stack>[data-el="seedmark-chart-area"]{--gap:calc(var(--pad)*.8125);--gap-lg:calc(var(--pad)*.8125);}
''')
add('elements/chart-line/element.css','''
.slide.src .stack>[data-el="seedmark-chart-line"]{padding:calc(var(--pad)*.8125) var(--gap) calc(var(--pad)*.8125);background:none;}
.slide.src [data-el="seedmark-chart-line"] .pt>b{height:calc(100% - var(--v)/var(--max)*100%);}
.slide.src [data-el="seedmark-chart-line"]:after{content:'';position:absolute;inset:calc(var(--pad)*.8125) var(--gap) calc(var(--pad)*1.625);background:repeating-linear-gradient(to bottom,var(--n-3) 0 var(--stroke),transparent var(--stroke) 33.333333%);z-index:-1;}
.slide.src [data-el="seedmark-chart-line"] .pt>span{visibility:visible;}
''')
add('elements/prose/element.css','''
.slide.src .stack:has(>[data-el="seedmark-chart-area"])>[data-el="seedmark-prose"],.slide.src .stack:has(>[data-el="seedmark-chart-line"])>[data-el="seedmark-prose"],.slide.src .stack:has(>[data-el="seedmark-chart-bar"])>[data-el="seedmark-prose"]{height:80px;}
.slide.src .stack>[data-el="seedmark-prose"]>p{font-size:var(--type-16);line-height:calc(var(--gap)*1.1666666667);}
.slide.src .body>[data-el="seedmark-prose"].lead>p{font-size:var(--type-26);line-height:calc(var(--gap)*1.5);}
.slide.src .body>[data-el="seedmark-prose"].quiet>p{font-size:var(--type-18);line-height:calc(var(--gap)*1.25);letter-spacing:calc(var(--body-track)*2);}
''')
add('elements/list/element.css','''
.slide.src [data-el="seedmark-list"]:has(.item>.mark){justify-content:flex-start;padding:0;gap:0;}
.slide.src [data-el="seedmark-list"] .item:has(>.mark){height:96px;flex:none;display:flex;flex-direction:row;justify-content:flex-start;align-items:center;border-top:var(--stroke) solid var(--n-3);padding-bottom:0;padding-left:calc(var(--pad)*2.1875);}
.slide.src [data-el="seedmark-list"]:has(.item>.mark){margin-left:calc(var(--pad)*-.4375);width:calc(100% + var(--pad)*.4375);}
.slide.src .stack:has(>[data-el="seedmark-headline"] h2>b)>[data-el="seedmark-list"]{height:290px;flex:none;}
''')
add('elements/venn/element.css','''
.slide.src [data-el="seedmark-venn"]:has(>.core){padding:0;--seedmark-venn-d:min(calc(var(--pad)*7.75),52cqw,calc(100cqh/1.484));}
.slide.src [data-el="seedmark-venn"]:has(>.core)>.set:nth-child(1){left:calc(50% + var(--gap-sm)*.8333333333);}
.slide.src [data-el="seedmark-venn"]:has(>.core)>.set:nth-child(2){left:calc(50% + var(--gap-sm)*.8333333333 - var(--seedmark-venn-d)*.7822580645);top:calc(var(--seedmark-venn-d)*.484);}
.slide.src [data-el="seedmark-venn"]:has(>.core)>.set:nth-child(3){left:calc(50% + var(--gap-sm)*.8333333333 - var(--seedmark-venn-d)*.2177419355);top:calc(var(--seedmark-venn-d)*.484);}
.slide.src [data-el="seedmark-venn"]:has(>.core):before{left:calc(50% + var(--gap-sm)*.8333333333 - var(--seedmark-venn-d)*.5);mask-image:radial-gradient(circle calc(var(--seedmark-venn-d)*.5) at 21.774% 98.4%,var(--ink) 99%,transparent),radial-gradient(circle calc(var(--seedmark-venn-d)*.5) at 78.226% 98.4%,var(--ink) 99%,transparent);}
.slide.src [data-el="seedmark-venn"]:has(>.core):after{left:calc(50% + var(--gap-sm)*.8333333333 - var(--seedmark-venn-d)*.7822580645);top:calc(var(--seedmark-venn-d)*.484);mask-image:radial-gradient(circle calc(var(--seedmark-venn-d)*.5) at 106.45% 50%,var(--ink) 99%,transparent);}
.slide.src [data-el="seedmark-venn"]:has(>.core)>.core{left:calc(50% + var(--gap-sm)*.8333333333);top:calc(var(--seedmark-venn-d)*.82258);width:100px;height:90px;}
.slide.src [data-el="seedmark-venn"]:has(>.core)>.set:nth-child(1)>.name{margin-top:calc(var(--gap-sm)*1.5);}
.slide.src [data-el="seedmark-venn"]:has(>.core)>.set:nth-child(2)>.name,.slide.src [data-el="seedmark-venn"]:has(>.core)>.set:nth-child(3)>.name{margin-top:calc(var(--gap-sm)*-1.5);}
.slide.src [data-el="seedmark-venn"]:has(>.core) .set:after{content:'';position:absolute;inset:0;border:8px solid var(--page);border-radius:50%;z-index:2;pointer-events:none;}
.slide.src [data-el="seedmark-venn"]:has(>.core) .set>.name{z-index:3;}
''')
add('elements/timeline/element.css','''
.slide.src [data-el="seedmark-timeline"]:has(.name>.frame):after{content:'';position:absolute;left:0;right:0;bottom:0;height:13px;background:repeating-linear-gradient(90deg,var(--n-3) 0 2px,transparent 2px 5px);}
.slide.src [data-el="seedmark-timeline"]:has(.name>.frame):before{content:'';position:absolute;left:0;right:0;bottom:0;height:13px;border-left:var(--gap-sm) solid var(--n-3);border-right:var(--gap-sm) solid var(--n-3);}
.slide.src [data-el="seedmark-timeline"]:has(.name>.frame) .stop>.note{font-size:var(--type-16);line-height:calc(var(--gap)*1.125);}
''')
add('elements/tag/element.css','''
.slide.src .body:has(>[data-el="seedmark-timeline"])>[data-el="seedmark-tag"]{align-self:end;margin-bottom:calc(var(--gap-sm)*-.5);min-width:94px;}
''')
# Independent usability regressions found by final QA.
add('elements/table/element.css','''
@container(max-height:420px){[data-el="seedmark-table"] table{font-size:var(--type-14);line-height:var(--label-line);}[data-el="seedmark-table"] th,[data-el="seedmark-table"] td{padding:calc(var(--gap-sm)/2);}}
''')
add('elements/person/element.css','''
[data-el="seedmark-person"].people>.person>.seat{width:min(190px,100%);height:auto;max-width:100%;aspect-ratio:1;}
[data-el="seedmark-person"].people:has(>.person:nth-child(5):last-child){display:grid;grid-template-columns:repeat(5,minmax(0,1fr));}
[data-el="seedmark-person"].people:has(>.person:nth-child(5):last-child)>.person:nth-child(3){width:226px;max-width:120%;justify-self:center;}
[data-el="seedmark-person"].people:has(>.person:nth-child(5):last-child)>.person:nth-child(3)>.seat{width:min(226px,100%);height:auto;max-width:100%;aspect-ratio:1;}
@container seedmark-people (max-width:700px){[data-el="seedmark-person"].people>.person>.seat{width:min(96px,100%);}[data-el="seedmark-person"].people:has(>.person:nth-child(5):last-child)>.person:nth-child(3){width:116px;}[data-el="seedmark-person"].people:has(>.person:nth-child(5):last-child)>.person:nth-child(3)>.seat{width:min(116px,100%);}}
''')
add('elements/quote/element.css','''
@container(max-height:300px){[data-el="seedmark-quote"] blockquote:before{font-size:var(--type-44);}[data-el="seedmark-quote"] .by .seat{width:48px;height:48px;}[data-el="seedmark-quote"] .by{grid-template-columns:48px minmax(0,1fr);}}
''')
add('elements/waffle/element.css','''
@container(max-height:110px){[data-el="seedmark-waffle"].figures{display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);align-items:center;align-content:center;padding:calc(var(--gap-sm)/3);gap:calc(var(--gap-sm)/3);}[data-el="seedmark-waffle"].figures .units{width:100%;max-width:100%;}[data-el="seedmark-waffle"].figures .fig{font-size:var(--type-20);line-height:var(--figure-line);}}
''')
add('elements/concentric/element.css','''
[data-el="seedmark-concentric"] .ring{top:50%;}
.slide.src [data-el="seedmark-concentric"] .ring{top:calc(50% + var(--gap-sm));}
''')
add('elements/chart-stack/element.css','''
.dark [data-el="seedmark-chart-stack"] .seg:nth-child(3 of .seg):not(.tone-1,.tone-2,.tone-3,.tone-4,.tone-5){color:var(--page);}
''')
add('elements/slope/element.css','''
[data-el="seedmark-slope"].dumbbell .pair .a,[data-el="seedmark-slope"].dumbbell .pair .b{background:var(--page);padding:0 calc(var(--gap-sm)/4);isolation:isolate;}
''')
add('elements/pill/element.css','''
.slide:not(.src) [data-el="seedmark-pill"].on:has(.mark):not(:has(.icon)){background:var(--a1);isolation:isolate;}
[data-el="seedmark-pill"].on .parts>.name,[data-el="seedmark-pill"].on .parts>.note{color:var(--a1-on);}
''')
p=C/'elements/pill/element.css';p.write_text(p.read_text()+'''
.slide:not(.src) [data-el="seedmark-pill"]:has(.mark):not(:has(.icon)){padding:calc(var(--gap-sm)/2) var(--gap-sm);border:var(--stroke) solid var(--n-3);background:var(--page);isolation:isolate;}
.slide:not(.src) [data-el="seedmark-pill"]:has(.mark):not(:has(.icon)):before{content:none;}
.slide:not(.src) [data-el="seedmark-pill"].on:has(.mark):not(:has(.icon)){background:var(--a1);border-color:var(--a1);color:var(--a1-on);}
.slide:not(.src) [data-el="seedmark-pill"].quiet:has(.mark):not(:has(.icon)){background:var(--n-1);border-color:var(--n-1);}
.slide:not(.src) [data-el="seedmark-pill"]:has(.mark):not(:has(.icon)) .parts{display:flex;position:static;flex-direction:row;align-items:center;justify-content:center;flex-wrap:wrap;gap:calc(var(--gap-sm)/2);}
.slide:not(.src) [data-el="seedmark-pill"]:has(.mark):not(:has(.icon)) .parts>.mark{position:static;transform:none;min-width:26px;width:26px;height:26px;border:0;background:none;color:inherit;padding:0;}
.slide:not(.src) [data-el="seedmark-pill"]:has(.mark):not(:has(.icon)) .parts>.name{font-size:var(--type-18);white-space:normal;}
.slide:not(.src) [data-el="seedmark-pill"]:has(.mark):not(:has(.icon)) .parts>.note{font-size:var(--type-14);display:block;}
''')
print('Final review corrections applied; golden markup unchanged.')
