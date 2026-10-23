from pathlib import Path
import re
B=Path(__file__).resolve().parents[1];C=B/'collection/afterglow'
patches={
'elements/headline/element.css':'''[data-el="afterglow-headline"].big:has(>.kick){transform:none;justify-content:center;gap:var(--gap-sm);}
[data-el="afterglow-headline"].big:has(>.kick)>h2{font-size:var(--type-64);transform:none;font-family:var(--font-display);font-weight:700;line-height:1.2;}
[data-el="afterglow-headline"].big:has(>.kick)>.note{font-size:var(--type-20);line-height:var(--body-line);}
[data-el="afterglow-headline"].on.center>.note{color:var(--a1-on);}
''',
'elements/steps/element.css':'''[data-el="afterglow-steps"].col:not(:has(.step>.mark>.icon)){height:100%;transform:none;width:100%;gap:var(--gap);}
[data-el="afterglow-steps"].col:not(:has(.step>.mark>.icon))>.step{grid-template-columns:56px minmax(0,1fr);padding:var(--gap-sm);column-gap:var(--gap-sm);}
''',
'foundation/foundation.css':'.slide.on .page{background:var(--a1);}',
'elements/agenda/element.css':'.slide.on [data-el="afterglow-agenda"] .entry{background:var(--a1);}',
}
for rel,css in patches.items():
 f=C/rel;t=f.read_text().split('\n/* FIDELITY CONTRACT */')[0];t=re.sub(r'[^{}]*\.big:has\(>h2:not\(:has\(b\)\)\)[^{}]*\{[^{}]*\}','',t);f.write_text(t+'\n/* FIDELITY CONTRACT */\n'+css+'\n')
