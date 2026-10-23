from pathlib import Path
B=Path(__file__).resolve().parents[1];C=B/'collection/afterglow'
patches={
'foundation/foundation.css':'''\n/* The page's horizontal register and chapter navigation are shared furniture. */
.slide.on .page{background:var(--a1-7);}
.slide .page:has(.body>.headline.big):not(:has(.agenda))::before,.slide .page:has(.body>.headline.center)::before{content:"";position:absolute;left:0;right:0;top:63.3%;border-top:var(--stroke) solid var(--n-5);pointer-events:none;}
.slide.on .body:has(>.headline.big>h2:not(:has(b)))::after{content:"";position:absolute;right:var(--pad);bottom:var(--pad);width:68px;height:68px;border-radius:50%;background:var(--a1-on);}
.slide.on .body:has(>.headline.big>h2:not(:has(b)))::before{content:"";position:absolute;right:49px;bottom:46px;width:24px;height:24px;border-top:4px solid var(--a1-7);border-right:4px solid var(--a1-7);transform:rotate(45deg);z-index:1;}
''',
'elements/headline/element.css':'''\n[data-el="afterglow-headline"]:has(>.kick){gap:var(--gap-sm);padding-bottom:0;}
[data-el="afterglow-headline"].big:has(h2>b){justify-content:center;padding-top:var(--gap-lg);}
[data-el="afterglow-headline"].big>h2:not(:has(b)){font-size:var(--type-128);font-weight:300;line-height:1;transform:scale(1.46875);transform-origin:left bottom;letter-spacing:-.02em;}
[data-el="afterglow-headline"].big:has(>h2:not(:has(b))){justify-content:flex-start;padding-top:var(--gap-lg);gap:var(--gap-lg);}
[data-el="afterglow-headline"].big:has(>h2:not(:has(b)))>.note{font-size:var(--type-32);margin-top:var(--gap-lg);}
[data-el="afterglow-headline"].center{justify-content:flex-start;gap:var(--gap-lg);padding-top:0;}
[data-el="afterglow-headline"].center>.note{font-size:var(--type-16);color:var(--ink);margin-top:var(--gap-lg);}
''',
'elements/agenda/element.css':'''\n.slide.on [data-el="afterglow-agenda"]{transform:translateY(-16px);gap:var(--gap-lg);}
.slide.on [data-el="afterglow-agenda"]::before{left:calc(var(--margin-x)*-5);right:calc(var(--margin-x)*-5);background:var(--a1-on);}
.slide.on [data-el="afterglow-agenda"] .entry{background:var(--a1-7);}
.slide.on [data-el="afterglow-agenda"] .entry>.name{font-size:var(--type-22);}
''',
'elements/list/element.css':'''\n[data-el="afterglow-list"]:has(.mark){justify-content:flex-start;padding-top:var(--gap-lg);}
[data-el="afterglow-list"]:has(.mark)>.item{padding-left:38px;}
[data-el="afterglow-list"]:has(.mark)>.item>.name{font-size:var(--type-18);font-weight:var(--name-weight);}
[data-el="afterglow-list"]:has(.mark)>.item>.note{font-size:var(--type-16);color:var(--ink);}
[data-el="afterglow-list"]:has(.mark)>.item::before{content:none;}
[data-el="afterglow-list"]>.item>.mark{width:27px;height:27px;display:grid;place-items:center;border-radius:50%;background:var(--a1);color:var(--a1-on);}
[data-el="afterglow-list"]>.item>.mark>.icon{width:20px;height:20px;}
.slide.on [data-el="afterglow-list"]{padding-left:calc(var(--pad) + var(--gap-lg));transform:translateY(-24px);justify-content:flex-start;gap:0;color:var(--a1-on);}
.slide.on [data-el="afterglow-list"]>.item{padding-left:14px;}
.slide.on [data-el="afterglow-list"]>.item>.name{font-size:var(--type-16);font-weight:400;line-height:var(--body-line);}
.slide.on [data-el="afterglow-list"]>.item::before{width:4px;height:4px;background:var(--a1-on);}
''',
'elements/prose/element.css':'''\n[data-el="afterglow-prose"].quiet{color:var(--ink);}
[data-el="afterglow-prose"].quiet:has(p>b){justify-content:flex-start;padding-top:var(--gap-sm);}
[data-el="afterglow-prose"].quiet:has(p>b)>p>b{font-size:var(--type-16);}
[data-el="afterglow-prose"].quiet:has(p>b)::after{content:"";position:absolute;left:0;right:0;bottom:var(--gap-lg);border-top:var(--stroke) solid var(--a1-7);}
.slide.on [data-el="afterglow-prose"]{padding-left:calc(var(--pad) + var(--gap-lg));justify-content:flex-start;color:var(--a1-on);font-size:var(--type-16);}
''',
'elements/callout/element.css':'''\n[data-el="afterglow-callout"].quiet{border:0;align-items:flex-start;padding:var(--gap-lg) 0 0;}
[data-el="afterglow-callout"].quiet p{font-size:var(--type-14);line-height:1.65;}
''',
'elements/chart-area/element.css':'''\n[data-el="afterglow-chart-area"].quiet{background:none;border:0;z-index:0;}
[data-el="afterglow-chart-area"].quiet .series{inset:0;--afterglow-h:100cqh;--afterglow-c:var(--a1-7);display:flex;justify-content:space-between;}
[data-el="afterglow-chart-area"].quiet .pt{margin-top:calc(var(--afterglow-h) - var(--afterglow-height));justify-self:auto;}
[data-el="afterglow-chart-area"].quiet .pt::before{background:linear-gradient(var(--a1-9),var(--page));}
[data-el="afterglow-chart-area"].quiet .pt{outline:3px solid var(--a1-7);border-radius:50%;}
''',
'elements/metric/element.css':'''\n[data-el="afterglow-metric"].stat.quiet>.parts{justify-content:flex-start;padding-top:var(--gap-lg);}
[data-el="afterglow-metric"].stat.quiet>.parts>.fig{font-size:var(--type-128);font-weight:300;line-height:1;transform:scale(1.09375);transform-origin:left top;}
[data-el="afterglow-metric"].stat.quiet>.parts>.fig>small{font-size:var(--type-36);align-self:flex-start;margin-top:var(--pad);font-weight:var(--name-weight);}
''',
'elements/image-frame/element.css':'''\n[data-el="afterglow-image-frame"].quiet{padding:0;border:0;box-shadow:none;background:transparent;}
'''}
for rel,css in patches.items():
 f=C/rel;t=f.read_text();t=t.split('\n/* FIDELITY REVISION */')[0];f.write_text(t+'\n/* FIDELITY REVISION */'+css)
print('Updated',len(patches),'source files')
