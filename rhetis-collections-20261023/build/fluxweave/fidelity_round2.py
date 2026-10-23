from pathlib import Path
import json
O=Path('/workspace/output/fluxweave');W=Path('/workspace/work/fluxweave')
def add(file,t):
 p=O/file;p.write_text(p.read_text()+'\n'+t+'\n')
p=O/'kit/css/tokens.css';s=p.read_text().replace('--weight-display:850','--weight-display:900').replace('--tracking-display:-.04em','--tracking-display:-.045em').replace('.slide{','.slide{--fluxweave-axis-steps:4;',1);p.write_text(s)
p=O/'kit/kit.json';d=json.loads(p.read_text());d['extensions']['--fluxweave-axis-steps']={'type':'number','description':'Number of equal divisions in the paired-chart value axis.'};p.write_text(json.dumps(d,indent=2))
p=O/'elements/card/element.css';p.write_text(p.read_text().replace('line-height:calc(100cqh/4)','line-height:calc(100cqh/var(--fluxweave-axis-steps))'))
add(Path('foundation/foundation.css'),'''
.slide .seat::after{display:none;}
.slide.cover .at-top-left{top:calc(var(--margin-y) + var(--gap-sm)*1.5);}
.slide.cover .kicker{font-size:var(--type-48);font-weight:var(--body-weight);line-height:calc(var(--title-line) + .02);margin-bottom:var(--gap-sm);}
.slide.cover .title{line-height:calc(var(--figure-line) - .15);}
.slide.cover .meta{left:0;right:0;text-align:center;bottom:calc(var(--margin-y)*.65);}
.slide.cover .top{left:auto;right:var(--margin-x);top:calc(var(--margin-y) + var(--gap-sm)*.5);font-size:var(--type-16);font-weight:var(--figure-weight);display:flex;gap:var(--furn-gap);align-items:center;}
.slide.cover .top>.logo{display:inline-block;position:relative;width:16px;height:20px;background:var(--a1);clip-path:polygon(0 0,75% 30%,75% 100%,0 70%);}
.slide.cover .at-bottom-left{bottom:calc(var(--margin-y) + var(--gap-sm)*.5);}
.slide.cover .at-bottom-left .kicker{position:absolute;bottom:calc(var(--margin-y)*.8);left:0;font-size:var(--type-128);font-weight:var(--weight-display);line-height:var(--figure-line);color:var(--n-2);transform:scale(1.875);transform-origin:bottom left;z-index:-1;}
.slide.cover .at-bottom-left .lead{font-weight:var(--name-weight);margin-top:var(--gap);}
.slide.cover .at-left:not(:has(.kicker)){left:58.36%;top:14%;max-width:39%;}
.slide.cover:has(.at-left:not(:has(.kicker)))>.page>.top{left:var(--margin-x);right:auto;}
.slide.cover .at-left:not(:has(.kicker)) .lead{font-size:var(--type-36);line-height:calc(var(--name-line) - .03);margin-top:calc(var(--gap-sm)*1.6);}
.slide .title>.icon{width:60px;height:60px;vertical-align:baseline;margin-left:var(--gap-sm);}
.slide .deco:has(svg){inset:auto 0 0;height:370px;opacity:1;overflow:hidden;}
.slide .deco:has(svg)::before,.slide .deco:has(svg)::after{display:none;}
.slide .deco>svg{display:block;width:100%;height:100%;}
.slide.cover:has(.at-bottom-left) .deco{height:340px;top:0;bottom:auto;}
.slide.cover:has(.at-left:not(:has(.kicker))) .deco{transform:scaleX(-1);}
.slide:has(.body>.agenda) .deco{height:440px;width:520px;left:0;top:0;bottom:auto;}
.slide.cover .page::before,.slide.cover .page::after{content:"";position:absolute;right:calc(var(--margin-x)*.91);top:calc(var(--margin-y)*1.76);width:90px;height:126px;background:radial-gradient(var(--n-3) 2px,color-mix(in srgb,var(--page) 0%,var(--page) 1%) 2.5px);background-size:19px 19px;z-index:-1;}
.slide.cover .page::after{left:calc(var(--margin-x)*.91);right:auto;top:calc(var(--margin-y)*5.36);}
.slide.cover:has(.at-bottom-left) .page::before{top:auto;bottom:var(--margin-y);}
.slide.cover:has(.at-bottom-left) .page::after{display:none;}
.slide.cover:has(.at-left:not(:has(.kicker))) .page::before{left:calc(var(--margin-x)*.91);right:auto;}
.slide.cover:has(.at-left:not(:has(.kicker))) .page::after{left:auto;right:calc(var(--margin-x)*.91);}
.slide:has(.body>.frame>.seat.portrait) .page{padding-right:calc(var(--margin-x)*.475);padding-bottom:0;}
.slide:has(.body>.frame>.seat.portrait) .head{position:absolute;left:var(--margin-x);top:calc(var(--margin-y)*1.875);width:906px;padding:0;min-height:0;}
.slide:has(.body>.frame+.frame) .page{padding-right:0;padding-bottom:calc(var(--margin-y)*.9);}
.slide:has(.body>.frame+.frame) .head{position:absolute;left:var(--margin-x);top:calc(var(--margin-y) + var(--gap-sm)*.8);width:444px;padding:0;display:block;min-height:0;}
.slide:has(.body>.frame+.frame) .head .title>.icon{display:block;margin-left:0;margin-top:var(--gap);width:43px;height:43px;}
.slide:has(.body>.frame+.frame) .head .lead{margin-top:calc(var(--gap) + var(--gap-sm)*.6);padding-right:0;}
.slide:has(.body>.venn) .head{min-height:114px;}
''')
add(Path('elements/headline/element.css'),'''
.headline.big[data-el="fluxweave-headline"]{justify-content:flex-end;padding-bottom:calc(var(--gap-sm)*1.6);}
.headline.big[data-el="fluxweave-headline"]>.kick{order:0;color:var(--ink);font-size:var(--type-16);margin-bottom:var(--gap);}
.headline.big[data-el="fluxweave-headline"]>h2{font-size:var(--type-88);font-weight:var(--weight-display);letter-spacing:var(--tracking-display);line-height:var(--figure-line);}
@container(max-width:480px){.headline.big[data-el="fluxweave-headline"]>h2{font-size:var(--type-60);}}
''')
add(Path('elements/agenda/element.css'),'''
.agenda[data-el="fluxweave-agenda"]:has(>.entry .name>small){display:block;padding:calc(var(--margin-y)*1.7) 0 0 calc(var(--margin-x)*.975);}
.agenda[data-el="fluxweave-agenda"]:has(>.entry .name>small)>.entry{position:relative;display:grid;grid-template-columns:46px 1fr;grid-template-rows:35px auto;gap:0;height:115px;padding:0 0 var(--gap);border-bottom:2px solid var(--n-2);background:none;}
.agenda[data-el="fluxweave-agenda"]:has(>.entry .name>small)>.entry:last-child{height:79px;border:0;}
.agenda[data-el="fluxweave-agenda"]:has(>.entry .name>small) .mark{grid-column:1;grid-row:1;align-self:start;justify-self:start;width:auto;height:auto;background:none;color:var(--ink);font-size:var(--type-18);padding-top:calc(var(--gap-sm)*.4);}
.agenda[data-el="fluxweave-agenda"]:has(>.entry .name>small) .name{grid-column:2;grid-row:1;align-self:start;font-size:var(--type-28);line-height:var(--name-line);}
.agenda[data-el="fluxweave-agenda"]:has(>.entry .name>small) .name>small{position:absolute;right:0;top:calc(var(--gap-sm)*.6);font-size:var(--type-18);font-weight:var(--weight-display);}
.agenda[data-el="fluxweave-agenda"]:has(>.entry .name>small) .note{grid-column:2;grid-row:2;align-self:start;font-size:var(--type-16);line-height:var(--body-line);margin-top:var(--gap-sm);}
''')
add(Path('elements/image-frame/element.css'),'''
.frame[data-el="fluxweave-image-frame"]:has(>.seat.portrait){padding:0;background:none;justify-content:flex-end;align-items:flex-end;}
.frame[data-el="fluxweave-image-frame"]>.seat.portrait{width:338px;height:634px;aspect-ratio:auto;border-radius:0;}
.frame[data-el="fluxweave-image-frame"]:has(+.frame[data-el="fluxweave-image-frame"]),.frame[data-el="fluxweave-image-frame"]:nth-child(3):has(>.seat[data-ph="2"]){padding:0;background:none;justify-content:flex-end;align-items:flex-start;}
.frame[data-el="fluxweave-image-frame"]:has(+.frame[data-el="fluxweave-image-frame"])>.seat{width:502px;height:274px;aspect-ratio:auto;border-radius:0;}
.frame[data-el="fluxweave-image-frame"]:nth-child(3):has(>.seat[data-ph="2"]){align-items:flex-end;}
.frame[data-el="fluxweave-image-frame"]:nth-child(3)>.seat[data-ph="2"]{width:502px;height:272px;aspect-ratio:auto;border-radius:0;transform:translateY(calc(-1*var(--gap-sm)*.8));}
''')
add(Path('elements/card/element.css'),'''
.card[data-el="fluxweave-card"]:has(>.parts>.prose){width:calc(100% - var(--gap-lg) - var(--furn-gap));height:314px;align-self:start;margin-top:calc(var(--gap) + var(--gap-sm)*.4);padding:calc(var(--pad) + var(--gap-sm)*.8);}
.card[data-el="fluxweave-card"]:has(>.parts>.prose)>.parts{display:block;position:relative;height:100%;}
.card[data-el="fluxweave-card"]:has(>.parts>.prose)>.parts>.name{font-size:var(--type-28);color:var(--a1-7);height:auto;}
.card[data-el="fluxweave-card"]:has(>.parts>.prose)>.parts>.prose{position:absolute;left:0;top:calc(var(--gap-lg)*1.5);width:72%;container-type:normal;display:block;font-size:var(--type-16);line-height:calc(var(--body-line) + .05);}
.card[data-el="fluxweave-card"]:has(>.parts>.prose)>.parts>.prose p{font-size:var(--type-16);line-height:calc(var(--body-line) + .05);}
.card[data-el="fluxweave-card"]:has(>.parts>.prose)>.parts>.note{position:absolute;top:calc(var(--margin-y)*2.7);right:34.3%;font-size:var(--type-20);line-height:var(--body-line);height:auto;}
.card[data-el="fluxweave-card"]:has(>.parts>.prose)>.parts>.note small{font-size:var(--type-14);color:var(--n-6);font-weight:var(--body-weight);}
''')
add(Path('elements/table/element.css'),'''
.tablebox[data-el="fluxweave-table"]:has(th:empty){width:445px;height:270px;align-self:end;margin-bottom:calc(var(--gap-sm)*.8);padding:0;background:none;}
.tablebox[data-el="fluxweave-table"]:has(th:empty) thead{display:none;}
.tablebox[data-el="fluxweave-table"]:has(th:empty) .table{font-size:var(--type-18);height:100%;}
.tablebox[data-el="fluxweave-table"]:has(th:empty) td{padding:var(--gap-sm) 0;border-top:var(--stroke) solid var(--n-4);border-bottom:0;text-align:left;font-size:var(--type-18);line-height:calc(var(--name-line) + .05);font-weight:var(--body-weight);color:var(--ink);}
.tablebox[data-el="fluxweave-table"]:has(th:empty) tr:last-child td{border-bottom:var(--stroke) solid var(--n-4);}
.tablebox[data-el="fluxweave-table"]:has(th:empty) td:first-child{width:35%;font-weight:var(--name-weight);}
''')
add(Path('elements/list/element.css'),'''
.list[data-el="fluxweave-list"]:has(>.item>.mark>.icon){display:block;padding-top:calc(var(--gap) + var(--gap-sm)*.6);}
.list[data-el="fluxweave-list"]:has(>.item>.mark>.icon)>.item{height:138px;display:grid;grid-template-columns:60px 1fr;grid-template-rows:30px 1fr;gap:0 var(--gap);padding:0;border-bottom:2px solid var(--n-4);}
.list[data-el="fluxweave-list"]:has(>.item>.mark>.icon)>.item::before{display:none;}
.list[data-el="fluxweave-list"]:has(>.item>.mark>.icon)>.item>.mark{grid-column:1;grid-row:1/3;align-self:start;margin-top:var(--gap);width:48px;height:48px;}
.list[data-el="fluxweave-list"]:has(>.item>.mark>.icon)>.item>.mark>.icon{width:100%;height:100%;}
.list[data-el="fluxweave-list"]:has(>.item>.mark>.icon)>.item>.name{grid-column:2;grid-row:1;font-size:var(--type-24);color:var(--ink);}
.list[data-el="fluxweave-list"]:has(>.item>.mark>.icon)>.item>.note{grid-column:2;grid-row:2;font-size:var(--type-18);line-height:calc(var(--body-line) - .1);margin-top:calc(var(--gap-sm)*.6);max-width:520px;}
.list[data-el="fluxweave-list"]:has(>.item>.mark>.icon)>.item:nth-child(1){color:var(--a1-7);}
.list[data-el="fluxweave-list"]:has(>.item>.mark>.icon)>.item:nth-child(1)>.name{color:var(--a1-7);}
.list[data-el="fluxweave-list"]:has(>.item>.mark>.icon)>.item:nth-child(3){color:var(--a2-7);}
.list[data-el="fluxweave-list"]:has(>.item>.mark>.icon)>.item:nth-child(3)>.name{color:var(--a2-7);}
''')
add(Path('elements/venn/element.css'),'''
.venn[data-el="fluxweave-venn"]:has(>.set .icon){padding:0;}
.venn[data-el="fluxweave-venn"]:has(>.set .icon)>.set{background:none;border:0;padding:0;isolation:auto;}
.venn[data-el="fluxweave-venn"]:has(>.set .icon)>.set::before{content:"";position:absolute;inset:0;border-radius:50%;background:var(--a1);opacity:.92;}
.venn[data-el="fluxweave-venn"]:has(>.set .icon)>.set:nth-child(1){left:calc(50% - min(65%,65cqh)*.485);transform:none;}
.venn[data-el="fluxweave-venn"]:has(>.set .icon)>.set:nth-child(2){left:calc(50% - min(65%,65cqh)*.8);}
.venn[data-el="fluxweave-venn"]:has(>.set .icon)>.set:nth-child(3){left:calc(50% - min(65%,65cqh)*.18);}
.venn[data-el="fluxweave-venn"]:has(>.set .icon)>.set:nth-child(2)::before{background:var(--n-8);}
.venn[data-el="fluxweave-venn"]:has(>.set .icon)>.set:nth-child(3)::before{background:var(--a2);}
.venn[data-el="fluxweave-venn"]:has(>.set .icon)>.set>.name{position:absolute;top:100px;left:0;right:0;font-size:var(--type-24);line-height:var(--name-line);z-index:5;color:var(--page);}
.venn[data-el="fluxweave-venn"]:has(>.set .icon)>.set:first-child>.name{top:calc(var(--margin-y)*.875);}
.venn[data-el="fluxweave-venn"]:has(>.set .icon)>.set .icon{display:block;margin:0 auto var(--gap-sm);width:32px;height:32px;}
.venn[data-el="fluxweave-venn"]:has(>.set .icon)>.set:first-child .icon{margin:calc(var(--gap-sm)*1.4) auto 0;}
''')
print('CSS first six fidelity')
