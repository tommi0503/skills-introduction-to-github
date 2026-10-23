from pathlib import Path
import shutil
B=Path('/workspace/work/deliverables/nocturne');C=B/'collection/nocturne';R=B/'review'
p=C/'kit/css/tokens.css';p.write_text(p.read_text()+'.slide{--nocturne-statement-scale:1.59375;--nocturne-statement-track:.002451em;}\n')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
.slide .page:has(.body>.stats){gap:calc(var(--gap-lg)*.639285714)}
.slide.cover .title{transform:translate(calc(var(--gap-sm)/-3),calc(var(--gap-sm)/-4)) scale(.99)}
.slide:has(.body>.prose)::before{content:'';position:absolute;inset:0 0 auto;height:400px;z-index:0;background:linear-gradient(to bottom,transparent 0,var(--a1-5-soft) 35%,transparent 85%);clip-path:polygon(42% 0,58% 0,100% 80%,100% 100%,0 100%,0 80%);filter:blur(25px)}
''')
p=C/'elements/headline/element.css';p.write_text(p.read_text()+'''@container(min-width:900px) and (min-height:250px){[data-el="nocturne-headline"].big:not(:has(h2>b)) h2{transform:translate(calc(var(--gap-sm)/-12),calc(var(--gap-sm)*-.388889)) scale(var(--nocturne-statement-scale))}}\n''')
p=R/'assets/source-style.css';p.write_text(p.read_text()+'\n.slide.dark{--a1-5-soft:#0e263b;}\n')
p=R/'replica/replica.css';p.write_text(p.read_text()+'''
.p19::before{content:'';position:absolute;inset:0 0 auto;height:400px;z-index:0;background:linear-gradient(to bottom,transparent 0,#0e263b 35%,transparent 85%);clip-path:polygon(42% 0,58% 0,100% 80%,100% 100%,0 100%,0 80%);filter:blur(25px)}
.p23 .qa{font-size:204px;letter-spacing:.5px;top:181.6px;transform:translateX(-1px)}
.p24 .title{transform:translate(-4px,-3px) scale(.99)}
''')
for p in C.rglob('*.css'):shutil.copy(p,R/'assets/collection'/p.relative_to(C))
print('Final measured geometry and analytic spotlight beam ready')
