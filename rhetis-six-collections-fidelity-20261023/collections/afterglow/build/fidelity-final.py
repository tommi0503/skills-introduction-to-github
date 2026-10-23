from pathlib import Path
B=Path(__file__).resolve().parents[1];C=B/'collection/afterglow'
# :has() cannot be nested. Navigation targets use two independent relational tests.
f=C/'foundation/foundation.css';t=f.read_text().replace('.body:has(>.headline.big>h2:not(:has(b)))','.body:has(>.headline.big):not(:has(>.headline.big>h2>b))');f.write_text(t)
patches={
'elements/headline/element.css':'''[data-el="afterglow-headline"].big:not(:has(>h2>b)){transform:translateY(-14px);}
[data-el="afterglow-headline"].big:not(:has(>h2>b))>.note{font-family:var(--afterglow-font-section);font-size:var(--type-32);}
[data-el="afterglow-headline"].big:has(>h2>b):not(:has(h2>br)){transform:translateY(-4px);}
[data-el="afterglow-headline"].big:has(>h2>b):not(:has(h2>br))>.note{font-size:var(--type-32);margin-top:-16px;}
''',
'elements/agenda/element.css':''' .slide.on [data-el="afterglow-agenda"] .entry{gap:0;}
.slide.on [data-el="afterglow-agenda"] .entry>.name{padding-bottom:4px;}
.slide.on [data-el="afterglow-agenda"] .entry>.note{font-size:var(--type-16);font-weight:var(--name-weight);}
''',
'elements/list/element.css':'.slide.on [data-el="afterglow-list"]>.item>.name{font-size:var(--type-16);line-height:1.5;}',
'elements/image-frame/element.css':'[data-el="afterglow-image-frame"].quiet{transform:translate(-12px,6px);width:calc(100% + 12px);height:calc(100% - 4px);}',
'elements/steps/element.css':'[data-el="afterglow-steps"].col{transform:translateY(5px);width:100%;height:calc(100% - 50px);gap:13px;}[data-el="afterglow-steps"].col>.step{grid-template-columns:132px minmax(0,1fr);}',
}
for rel,css in patches.items():
 f=C/rel;t=f.read_text().split('\n/* FIDELITY FINAL */')[0];f.write_text(t+'\n/* FIDELITY FINAL */\n'+css+'\n')
