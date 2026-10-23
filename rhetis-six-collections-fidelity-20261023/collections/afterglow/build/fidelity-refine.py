from pathlib import Path
import json
B=Path(__file__).resolve().parents[1];C=B/'collection/afterglow'
patches={
'foundation/foundation.css':'.slide .page::before{border-color:var(--n-6)!important;opacity:.6;}',
'elements/headline/element.css':'''[data-el="afterglow-headline"].big>h2:not(:has(b)){font-family:var(--afterglow-font-section);font-weight:400;transform:translateY(12px) scale(1.375);letter-spacing:.36px;}
[data-el="afterglow-headline"].big:has(>h2:not(:has(b)))>.note{margin-top:var(--gap);}
[data-el="afterglow-headline"].big:has(h2>b)>h2{font-weight:300;}
[data-el="afterglow-headline"].big>h2:not(:has(br))>b{font-size:var(--type-52);font-weight:400;}
[data-el="afterglow-headline"].big:has(>h2>b):not(:has(h2>br)){gap:var(--gap-sm);}
[data-el="afterglow-headline"]{z-index:1;}
''',
'elements/agenda/element.css':'''.slide.on [data-el="afterglow-agenda"]{padding:0 80px;gap:0;justify-content:space-between;transform:translateY(-12px);}
.slide.on [data-el="afterglow-agenda"] .entry{flex:none;width:160px;}
.slide.on [data-el="afterglow-agenda"] .entry>.name{font-size:var(--type-24);}
''',
'elements/list/element.css':'.slide.on [data-el="afterglow-list"]>.item>.name{font-size:var(--type-14);}',
'elements/prose/element.css':'''[data-el="afterglow-prose"].lead{padding-left:calc(var(--gap-lg)*2);font-weight:var(--title-weight);}
[data-el="afterglow-prose"].quiet:not(:has(p>b)){padding:var(--gap-sm) 0 0 calc(var(--pad) + var(--gap-lg));justify-content:flex-start;font-size:var(--type-16);}
.slide.on [data-el="afterglow-prose"]{font-size:var(--type-14);padding-top:4px;}
[data-el="afterglow-prose"].quiet:has(p>b){padding-top:var(--gap);}
[data-el="afterglow-prose"].quiet:has(p>b)::after{bottom:4px;}
''',
'elements/chart-area/element.css':'''[data-el="afterglow-chart-area"].quiet{margin-left:4px;width:calc(100% - 8px);height:calc(100% - var(--gap-lg));}
[data-el="afterglow-chart-area"].quiet .pt::before{background-image:linear-gradient(to top,var(--page),var(--a1-9) 70%);background-size:100% var(--afterglow-h);background-position:left bottom;background-repeat:no-repeat;}
[data-el="afterglow-chart-area"].quiet .series::after{content:"";position:absolute;inset:0;background:var(--page);z-index:1;clip-path:polygon(87% 100%,87% 53%,86% 56%,85% 54%,88% 48%,91% 54%,90% 56%,89% 53%,89% 100%,91.3% 100%,91.3% 44%,90.3% 47%,89.3% 45%,92.3% 39%,95.3% 45%,94.3% 47%,93.3% 44%,93.3% 100%,95.7% 100%,95.7% 36%,94.7% 39%,93.7% 37%,96.7% 31%,99.7% 37%,98.7% 39%,97.7% 36%,97.7% 100%);}
''',
'elements/metric/element.css':'''[data-el="afterglow-metric"].stat.quiet{padding-left:48px;}
[data-el="afterglow-metric"].stat.quiet>.parts{padding-top:80px;}
''',
'elements/card/element.css':'''[data-el="afterglow-card"]:has(>.parts>.seat){transform:translateY(var(--gap));height:calc(100% - var(--gap));}
[data-el="afterglow-card"] .parts:has(>.seat){gap:10px;}
[data-el="afterglow-card"] .parts>.seat{height:59.4%;}
[data-el="afterglow-card"] .parts:has(>.seat)>.mark{margin-top:10px;}
[data-el="afterglow-card"] .parts:has(>.seat)>.name{min-height:calc(1em*var(--name-line));}
''',
'elements/steps/element.css':'''[data-el="afterglow-steps"].col{height:calc(100% - 40px);transform:translateX(-12px);width:calc(100% + 12px);gap:var(--gap);}
[data-el="afterglow-steps"].col>.step{grid-template-columns:148px minmax(0,1fr);padding:var(--gap) var(--gap) var(--gap) var(--pad);}
[data-el="afterglow-steps"].col>.step>.mark .icon{width:80px;height:80px;}
[data-el="afterglow-steps"].col>.step>.note{font-size:var(--type-16);}
''',
'elements/callout/element.css':'[data-el="afterglow-callout"].quiet{padding-top:44px;}[data-el="afterglow-callout"].quiet p{font-size:var(--type-12);}',
}
for rel,css in patches.items():
 f=C/rel;t=f.read_text().split('\n/* FIDELITY REFINE */')[0];f.write_text(t+'\n/* FIDELITY REFINE */\n'+css+'\n')
f=C/'kit/css/tokens.css';t=f.read_text().split('\n/* SECTION FONT */')[0];f.write_text(t+'\n/* SECTION FONT */\n.slide{--afterglow-font-section:SUITE;}\n')
f=C/'kit/kit.json';kit=json.loads(f.read_text());kit['extensions']['--afterglow-font-section']='font';f.write_text(json.dumps(kit,ensure_ascii=False,indent=2))
