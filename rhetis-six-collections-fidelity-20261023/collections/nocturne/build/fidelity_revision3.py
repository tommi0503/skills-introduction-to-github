from pathlib import Path
import json,shutil
B=Path('/workspace/work/deliverables/nocturne');C=B/'collection/nocturne';R=B/'review'
def patch(folder,s):
 p=C/f'elements/{folder}/element.css';p.write_text(p.read_text()+s.replace('R',f'[data-el="nocturne-{folder}"]')+'\n')
p=C/'kit/kit.json';k=json.loads(p.read_text());k['extensions'].update({'--nocturne-font-latin':'font','--nocturne-latin-track':'tracking','--nocturne-heading-track':'tracking','--nocturne-hero-track':'tracking'});p.write_text(json.dumps(k,indent=2))
p=C/'kit/css/tokens.css';p.write_text(p.read_text()+".slide{--nocturne-font-latin:'Montserrat';--nocturne-latin-track:-.015em;--nocturne-heading-track:.008929em;--nocturne-hero-track:0em;--nocturne-statement-weight:600;--nocturne-statement-scale:1.58671875;--nocturne-statement-track:.002462em;}\n")
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
.slide{background-image:radial-gradient(ellipse 790px 450px at 0 0,var(--a1-2-soft) 0,color-mix(in srgb,var(--a1-2-soft) 58%,transparent) 49%,transparent 82%),radial-gradient(ellipse 700px 560px at 100% 100%,var(--a1-3-soft) 0,color-mix(in srgb,var(--a1-3-soft) 30%,transparent) 45%,transparent 80%)}
.slide:has(.body>.prose){background-image:radial-gradient(ellipse 430px 230px at 50% 6%,var(--a1-3-soft) 0,color-mix(in srgb,var(--a1-3-soft) 65%,transparent) 52%,transparent 80%),linear-gradient(to top,var(--a1-4-soft) 0,transparent 22%)}
.slide .head{gap:calc(var(--gap-sm)*1.7)}
.slide .head .kicker{letter-spacing:var(--label-track)}
.slide .title{font-size:var(--type-56);letter-spacing:var(--nocturne-heading-track)}
.slide .page{gap:calc(var(--gap-lg)*.8535714)}
.slide .page:has(.body>.stats){gap:calc(var(--gap-lg)*.55)}
.slide .page:has(.body>.stats)>.head{gap:calc(var(--gap-sm)*1.95)}
.slide .page:has(.body>.stats)>.head>.kicker{transform:translateY(calc(var(--gap-sm)*.583333))}
.slide .page:has(.body>.seat.back){gap:calc(var(--gap-lg)*.907142857)}
.slide .page:has(.body>.seat.back)>.head{gap:calc(var(--gap-sm)*1.45)}
.slide.cover .title{font-family:var(--nocturne-font-latin);font-size:var(--type-100);font-weight:var(--nocturne-statement-weight);letter-spacing:var(--nocturne-latin-track);transform:scale(.99)}
.slide.cover .title b{font-weight:inherit}
.slide.cover .lead{color:var(--ink)}
.slide.cover .meta{margin:0}
''')
patch('headline','''R.big:has(h2>b) h2{letter-spacing:var(--nocturne-hero-track)}R.center:not(.big):not(.on):not(:has(.note)):has(h2>b)::after{border-color:var(--ink)}R.center:not(.big):not(.on):not(:has(.note)):not(:has(h2>b)) h2{letter-spacing:var(--label-track);transform:translateY(calc(var(--gap-sm)*.25))}''')
patch('callout','''R:has(p>br){transform:translateY(calc(var(--gap-sm)*-3))}''')
p=R/'assets/source-style.css';s=p.read_text().replace('--a1-2-soft:#19496d','--a1-2-soft:#16476d');s+='\n.slide.dark{--a1-4-soft:#17436b;}\n';p.write_text(s)
for p in C.rglob('*.css'):shutil.copy(p,R/'assets/collection'/p.relative_to(C))
print('Third fidelity source pass ready')
