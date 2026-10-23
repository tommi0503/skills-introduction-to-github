from pathlib import Path
B=Path(__file__).resolve().parents[1];C=B/'collection/afterglow'
patches={
'elements/chart-area/element.css':'''[data-el="afterglow-chart-area"].quiet .pt{width:6px;height:6px;border-radius:999px;outline:0;background:var(--a1-7);margin-left:-3px;margin-right:-3px;margin-top:calc(var(--afterglow-h) - var(--afterglow-height) - 3px);}
[data-el="afterglow-chart-area"].quiet .pt::before,[data-el="afterglow-chart-area"].quiet .pt::after{top:calc(anchor(var(--afterglow-prev) center) - var(--afterglow-h));}
''',
'elements/metric/element.css':'[data-el="afterglow-metric"].stat.quiet>.parts>.fig>small{letter-spacing:0;word-spacing:0;}',
'elements/image-frame/element.css':''' .slide .body:has(>[data-el="afterglow-prose"]>p>b)>[data-el="afterglow-image-frame"].quiet{transform:translate(-22px,20px);width:calc(100% + 6px);height:calc(100% - 54px);}
''',
'elements/prose/element.css':'''[data-el="afterglow-prose"].quiet:has(p>b){padding-top:12px;gap:12px;}
[data-el="afterglow-prose"].quiet.line:has(p>b){padding-top:var(--pad);}
[data-el="afterglow-prose"].quiet:not(.line):has(p>b)::after{content:none;}
.slide:not(.on) [data-el="afterglow-prose"]:not(.quiet):not(.lead):has(>p>br){width:365px;justify-content:flex-start;padding-top:var(--pad);font-size:var(--type-18);font-family:var(--afterglow-font-copy);letter-spacing:var(--afterglow-copy-track);line-height:var(--afterglow-copy-line);}
.slide:not(.on) [data-el="afterglow-prose"]:not(.quiet):not(.lead):has(>p>br)>p{white-space:nowrap;transform:scale(.94);transform-origin:left top;}
''',
'elements/headline/element.css':'''[data-el="afterglow-headline"].center:not(.on)>.note{transform:translateY(7px);}
@container(max-height:170px){[data-el="afterglow-headline"].center>h2{position:absolute;top:0;left:0;right:0;font-size:var(--type-24);line-height:1.2;}[data-el="afterglow-headline"].center>.note{position:absolute;left:0;right:0;bottom:0;font-size:var(--type-14);margin-top:0;transform:none;}}
'''}
for rel,css in patches.items():
 f=C/rel;t=f.read_text().split('\n/* SOURCE POLISH */')[0];f.write_text(t+'\n/* SOURCE POLISH */\n'+css+'\n')
