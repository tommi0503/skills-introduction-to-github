from pathlib import Path
B=Path(__file__).resolve().parents[1];C=B/'collection/afterglow'
f=C/'elements/headline/element.css';t=f.read_text().split('\n/* MEASURED TYPE */')[0];t+='''
/* MEASURED TYPE */
[data-el="afterglow-headline"].big:not(:has(>h2>b)){transform:translateY(-10px);}
[data-el="afterglow-headline"].big>h2:not(:has(b)){transform:translate(-12px,12px) scale(1.375);}
[data-el="afterglow-headline"].big:not(:has(>h2>b))>.note{font-size:var(--type-30);}
[data-el="afterglow-headline"].big>h2:not(:has(br))>b{font-size:var(--type-56);letter-spacing:-.8px;position:relative;left:-4px;}
[data-el="afterglow-headline"]:has(>.kick)>h2{font-weight:800;letter-spacing:-.5px;transform:translateY(-1px) scale(1.03);transform-origin:left top;}
''';f.write_text(t)
