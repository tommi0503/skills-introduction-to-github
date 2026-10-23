from pathlib import Path
O=Path('/workspace/output/fluxweave')
def add(p,s):
 f=O/p;f.write_text(f.read_text()+'\n'+s+'\n')
add('foundation/foundation.css','''
.slide:has(.body>.track.col) .page{padding-top:0;padding-bottom:0;}
.slide:has(.body>.track.col) .head{position:absolute;left:var(--margin-x);top:calc(var(--margin-y) + var(--gap-sm)*.8);width:444px;padding:0;display:block;min-height:0;}
.slide:has(.body>.track.col) .head .title>.icon{display:block;margin-left:0;margin-top:var(--gap);width:43px;height:43px;}
.slide:has(.body>.track.col) .head .lead{margin-top:calc(var(--gap) + var(--gap-sm)*.6);padding:0;}
.slide .group.col:has(>.card>.parts>.fig){gap:calc(var(--gap) - var(--gap-sm)*.1);padding-top:var(--gap-lg);align-items:stretch;}
.slide .group.col:has(>.card>.parts>.fig)>*{flex:none;height:109px;}
.slide:has(.body>.hub>.spoke:nth-child(4)):not(:has(.body>.hub>.spoke:nth-child(5))) .head{min-height:130px;}
.slide .group:has(>.frame)>.frame{padding:0;background:none;align-items:flex-start;justify-content:center;}
.slide .group:has(>.frame)>.frame>.seat{width:218px;height:242px;aspect-ratio:auto;border-radius:0;}
''')
add('elements/card/element.css','''
.card[data-el="fluxweave-card"]:has(>.parts>.fig):has(>.parts>.mark>.icon)>.parts{display:grid;grid-template-columns:24px 1fr auto;grid-template-rows:1fr;gap:var(--gap-sm);align-items:center;}
.card[data-el="fluxweave-card"]:has(>.parts>.fig):has(>.parts>.mark>.icon)>.parts>.mark{grid-area:1/1;width:24px;height:24px;color:var(--n-6);margin:0;}
.card[data-el="fluxweave-card"]:has(>.parts>.fig):has(>.parts>.mark>.icon)>.parts>.name{grid-area:1/2;text-align:left;font-size:var(--type-18);color:var(--n-6);height:auto;min-height:0;}
.card[data-el="fluxweave-card"]:has(>.parts>.fig):has(>.parts>.mark>.icon)>.parts>.fig{grid-area:1/3;font-size:var(--type-40);color:var(--ink);height:auto;margin:0;}
.card[data-el="fluxweave-card"]:has(>.parts>.fig):has(>.parts>.mark>.icon)>.parts>.note{display:none;}
.card[data-el="fluxweave-card"]:has(>.parts>.logos){height:106px;align-self:start;padding:var(--gap);}
.card[data-el="fluxweave-card"]:has(>.parts>.logos)>.parts{display:flex;flex-direction:row;align-items:center;gap:var(--gap);}
.card[data-el="fluxweave-card"]:has(>.parts>.logos)>.parts>.name{width:180px;flex:none;text-align:center;font-size:var(--type-24);height:auto;min-height:0;}
.card[data-el="fluxweave-card"]:has(>.parts>.logos)>.parts>.logos{flex:1;height:70px;container-type:normal;padding:0;background:none;}
.card[data-el="fluxweave-card"]:has(>.parts>.logos) .seat.logo{width:100px;height:70px;aspect-ratio:auto;border-radius:0;}
.card[data-el="fluxweave-card"]:has(>.parts>.kick:last-child):not(:has(>.parts>.fig)){height:176px;align-self:start;margin-top:calc(var(--gap-sm)*.7);padding:var(--gap-lg) calc(var(--gap-lg) + var(--gap-sm)*.4);}
.card[data-el="fluxweave-card"]:has(>.parts>.kick:last-child):not(:has(>.parts>.fig))>.parts{position:relative;display:block;height:100%;}
.card[data-el="fluxweave-card"]:has(>.parts>.kick:last-child):not(:has(>.parts>.fig))>.parts>.name{font-size:var(--type-24);min-height:0;height:auto;white-space:nowrap;}
.card[data-el="fluxweave-card"]:has(>.parts>.kick:last-child):not(:has(>.parts>.fig))>.parts>.note{font-size:var(--type-18);line-height:calc(var(--body-line) - .15);margin-top:calc(var(--gap-sm)*.8);min-height:0;height:auto;}
.card[data-el="fluxweave-card"]:has(>.parts>.kick:last-child):not(:has(>.parts>.fig))>.parts>.kick{position:absolute;bottom:calc(-1*var(--gap-sm)*.4);right:0;font-size:var(--type-16);color:var(--n-6);font-weight:var(--body-weight);}
.card[data-el="fluxweave-card"]:has(>.parts>.mark>.icon)>.parts>.mark{color:var(--a1-7);}
.group.two>.card[data-el="fluxweave-card"]:has(>.parts>.mark>.icon)>.parts>.mark{color:var(--a2-7);}
.group.two>.card.on[data-el="fluxweave-card"]:has(>.parts>.mark>.icon)>.parts>.mark{color:var(--a2-on);}
''')
add('elements/timeline/element.css','''
@container(min-width:400px) and (min-height:650px){
.track.col[data-el="fluxweave-timeline"]{display:block;position:relative;padding:0;}
.track.col[data-el="fluxweave-timeline"]::before{content:"";position:absolute;left:138px;top:0;bottom:0;width:3px;background:var(--a1);}
.track.col[data-el="fluxweave-timeline"]>.stop{display:block;position:relative;height:25%;padding:calc(var(--gap-lg)*1.5) 0 0 calc(var(--margin-x)*2.025);border:0;background:none;}
.track.col[data-el="fluxweave-timeline"]>.stop::before{display:none;}
.track.col[data-el="fluxweave-timeline"]>.stop::after{content:"";position:absolute;left:132px;top:83px;width:15px;height:15px;border-radius:50%;background:var(--a1-7);}
.track.col[data-el="fluxweave-timeline"]>.stop>.kick{position:absolute;left:calc(var(--gap-sm)*1.8);top:calc(var(--margin-y)*.925);font-size:var(--type-28);line-height:var(--figure-line);color:var(--a1-7);font-weight:var(--figure-weight);}
.track.col[data-el="fluxweave-timeline"]>.stop>.name{font-size:var(--type-24);min-height:0;line-height:var(--name-line);}
.track.col[data-el="fluxweave-timeline"]>.stop>.note{font-size:var(--type-18);line-height:calc(var(--body-line) - .1);margin-top:var(--gap-sm);}
}
''')
# Compose distinct 3- and 6-spoke diagram forms from the source's directional layout.
add('elements/hub/element.css','''
@container(min-width:800px) and (min-height:350px){
.hub[data-el="fluxweave-hub"]{display:block;}
.hub[data-el="fluxweave-hub"]>.core{position:absolute;display:grid;aspect-ratio:auto;padding:var(--gap);font-size:var(--type-24);line-height:var(--figure-line);max-height:none;}
.hub[data-el="fluxweave-hub"]>.spoke{position:absolute;}
.hub[data-el="fluxweave-hub"]>.spoke::before{display:none;}
.hub[data-el="fluxweave-hub"]:not(:has(>.spoke:nth-child(5)))>.core{left:0;top:97px;width:205px;height:205px;}
.hub[data-el="fluxweave-hub"]:not(:has(>.spoke:nth-child(5)))>.spoke{left:226px;width:calc(100% - 226px);height:116px;display:flex;align-items:center;padding:calc(var(--gap) + var(--gap-sm)*.2);gap:var(--gap);text-align:left;}
.hub[data-el="fluxweave-hub"]:not(:has(>.spoke:nth-child(5)))>.spoke:nth-child(2){top:0;}
.hub[data-el="fluxweave-hub"]:not(:has(>.spoke:nth-child(5)))>.spoke:nth-child(3){top:141px;left:254px;width:calc(100% - 282px);}
.hub[data-el="fluxweave-hub"]:not(:has(>.spoke:nth-child(5)))>.spoke:nth-child(4){top:282px;}
.hub[data-el="fluxweave-hub"]:not(:has(>.spoke:nth-child(5)))>.spoke>.name{width:235px;flex:none;height:65px;border-radius:var(--radius);background:var(--page);display:grid;place-items:center;font-size:var(--type-24);}
.hub[data-el="fluxweave-hub"]:not(:has(>.spoke:nth-child(5)))>.spoke>.note{margin:0;font-size:var(--type-18);line-height:calc(var(--body-line) - .1);}
.hub[data-el="fluxweave-hub"]:not(:has(>.spoke:nth-child(5)))>.spoke::before{display:block;inset:auto;width:98px;height:2px;background:var(--a1);left:-98px;top:54px;transform:rotate(-64deg);transform-origin:right center;}
.hub[data-el="fluxweave-hub"]:not(:has(>.spoke:nth-child(5)))>.spoke:nth-child(3)::before{width:50px;left:-50px;top:58px;transform:none;}
.hub[data-el="fluxweave-hub"]:not(:has(>.spoke:nth-child(5)))>.spoke:nth-child(4)::before{top:58px;transform:rotate(64deg);}
.hub[data-el="fluxweave-hub"]:not(:has(>.spoke:nth-child(5)))>.spoke::after{content:"";position:absolute;left:-3px;top:51px;width:7px;height:7px;border-radius:50%;background:var(--a1);}
.hub[data-el="fluxweave-hub"]:has(>.spoke:nth-child(7))>.core{left:calc(50% - 85px);top:118px;width:170px;height:170px;}
.hub[data-el="fluxweave-hub"]:has(>.spoke:nth-child(7))>.spoke{width:242px;height:96px;left:0;padding:0;background:none;border-radius:0;border-bottom:2px solid var(--n-4);text-align:left;}
.hub[data-el="fluxweave-hub"]:has(>.spoke:nth-child(7))>.spoke:nth-child(2),.hub[data-el="fluxweave-hub"]:has(>.spoke:nth-child(7))>.spoke:nth-child(5){top:47px;}
.hub[data-el="fluxweave-hub"]:has(>.spoke:nth-child(7))>.spoke:nth-child(3),.hub[data-el="fluxweave-hub"]:has(>.spoke:nth-child(7))>.spoke:nth-child(6){top:167px;}
.hub[data-el="fluxweave-hub"]:has(>.spoke:nth-child(7))>.spoke:nth-child(4),.hub[data-el="fluxweave-hub"]:has(>.spoke:nth-child(7))>.spoke:nth-child(7){top:287px;border-bottom:0;}
.hub[data-el="fluxweave-hub"]:has(>.spoke:nth-child(7))>.spoke:nth-child(n+5){left:auto;right:0;width:227px;}
.hub[data-el="fluxweave-hub"]:has(>.spoke:nth-child(7))>.spoke>.name{font-size:var(--type-24);white-space:nowrap;}
.hub[data-el="fluxweave-hub"]:has(>.spoke:nth-child(7))>.spoke>.note{font-size:var(--type-18);line-height:calc(var(--body-line) - .15);margin-top:var(--gap-sm);}
.hub[data-el="fluxweave-hub"]:has(>.spoke:nth-child(7))>.spoke>.mark{position:absolute;left:245px;top:-10px;width:96px;height:96px;background:var(--n-1);margin:0;}
.hub[data-el="fluxweave-hub"]:has(>.spoke:nth-child(7))>.spoke:nth-child(n+5)>.mark{left:-115px;}
.hub[data-el="fluxweave-hub"]:has(>.spoke:nth-child(7))>.spoke>.mark>.icon{width:40%;height:40%;color:var(--a1-7);}
}
''')
add('elements/table/element.css','''
@container(min-width:800px){
.tablebox[data-el="fluxweave-table"]:not(:has(th:empty)){align-items:stretch;}
.tablebox[data-el="fluxweave-table"]:not(:has(th:empty))>.table{height:100%;font-size:var(--type-18);border-collapse:separate;border-spacing:0;}
.tablebox[data-el="fluxweave-table"]:not(:has(th:empty)) th{background:linear-gradient(90deg,var(--a2-7-soft),var(--a1-7-soft));color:var(--page);border-radius:var(--radius) var(--radius) 0 0;text-align:center;padding:var(--gap-sm);font-size:var(--type-18);}
.tablebox[data-el="fluxweave-table"]:not(:has(th:empty)) td{text-align:center;padding:var(--gap-sm);font-size:var(--type-18);font-weight:var(--body-weight);line-height:var(--body-line);}
.tablebox[data-el="fluxweave-table"]:not(:has(th:empty)) td:first-child{font-weight:var(--name-weight);}
.tablebox[data-el="fluxweave-table"]:has(th:nth-child(2):last-child){height:160px;align-self:end;}
.tablebox[data-el="fluxweave-table"]:has(th:nth-child(2):last-child) th:first-child{width:35%;}
.tablebox[data-el="fluxweave-table"]:has(th:nth-child(4)) th:nth-child(1){width:25%;}
.tablebox[data-el="fluxweave-table"]:has(th:nth-child(4)) th:nth-child(2){width:25%;}
.tablebox[data-el="fluxweave-table"]:has(th:nth-child(4)) th:nth-child(3){width:31%;}
.tablebox[data-el="fluxweave-table"]:has(th:nth-child(4)) th:nth-child(4){width:19%;background:var(--a1);color:var(--a1-on);}
.tablebox[data-el="fluxweave-table"]:has(th:nth-child(4)) td:last-child{color:var(--a1-7);font-weight:var(--name-weight);}
.tablebox[data-el="fluxweave-table"] td .icon{display:inline-block;width:16px;height:16px;vertical-align:middle;color:var(--a1-7);margin-right:calc(var(--gap-sm)*.4);}
.tablebox[data-el="fluxweave-table"]:has(th:nth-child(3):last-child){align-self:end;height:254px;}
.tablebox[data-el="fluxweave-table"]:has(th:nth-child(3):last-child) th:first-child{width:21.2%;background:var(--n-3);color:var(--ink);}
.tablebox[data-el="fluxweave-table"]:has(th:nth-child(3):last-child) th:nth-child(2){background:var(--a1);color:var(--a1-on);}
.tablebox[data-el="fluxweave-table"]:has(th:nth-child(3):last-child) th:nth-child(3){background:var(--a1-7);color:var(--page);}
.tablebox[data-el="fluxweave-table"]:has(th:nth-child(3):last-child) td:not(:first-child){text-align:left;padding-left:var(--gap);}
.tablebox[data-el="fluxweave-table"] .pick{background:none;}
}
''')
print('other pages CSS')
