from pathlib import Path
import json,shutil
B=Path('/workspace/work/deliverables/nocturne');C=B/'collection/nocturne';R=B/'review'
def patch(folder,s):
 p=C/f'elements/{folder}/element.css';p.write_text(p.read_text()+s.replace('R',f'[data-el="nocturne-{folder}"]')+'\n')
p=C/'kit/kit.json';k=json.loads(p.read_text());k['extensions']['--nocturne-hero-weight']='weight';p.write_text(json.dumps(k,indent=2));p=C/'kit/css/tokens.css';p.write_text(p.read_text()+'.slide{--nocturne-hero-weight:700;--nocturne-hero-track:.005682em;}\n')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'.slide .body>.group:has(>.pill){gap:calc(var(--gap-sm)*2.25)}\n')
patch('headline','''R.big:has(h2>b) h2{font-weight:var(--nocturne-hero-weight);transform:translateY(calc(var(--gap-sm)*-.7))}R.big:has(h2>b) h2 b{font-weight:inherit}R.center:not(.big):not(.on):not(:has(.note)):has(h2>b){justify-content:flex-start;padding-top:var(--gap)}R.center:not(.big):not(.on):not(:has(.note)):has(h2>b) h2{transform:none}R.center:not(.big):not(.on):not(:has(.note)):has(h2>b)::after{top:calc(var(--gap-lg)*1.6785714)}''')
patch('pill','''R.pill.line{height:65px;min-height:65px;max-height:65px;padding-inline:calc(var(--gap-sm)*2.5);transform:translateY(calc(var(--gap-sm)*.555556))}R.pill.line .name{font-size:var(--type-28)}R.pill.line.quiet{padding-inline:calc(var(--gap-sm)*2.166667)}''')
patch('list','''R.divided .item>.name{width:fit-content;max-width:94%;align-self:center}''')
patch('card','''R.quiet:has(.mark>.seat) .name{top:calc(34.9076% - var(--gap-sm)*.5)}''')
p=R/'reassembled/slide_19.html';s=p.read_text().replace('class="headline center" data-el="nocturne-headline" style="grid-column:1 / span 12; grid-row:1 / span 1"','class="headline center" data-el="nocturne-headline" style="grid-column:1 / span 12; grid-row:1 / span 2"').replace('class="pill line" data-el="nocturne-pill"><div class="parts"><b class="name">본격 확장','class="pill line quiet" data-el="nocturne-pill"><div class="parts"><b class="name">본격 확장');p.write_text(s)
# Replica remains independent from all collection rules.
p=R/'replica/replica.css';p.write_text(p.read_text()+'''
/* User-authorized fidelity revision: measured glyph silhouettes and original geometry. */
@font-face{font-family:Mont;src:url('../assets/fonts/artifacts/montserrat/Montserrat.woff2');font-weight:100 900}
.title{font-size:56.2px;line-height:1.2;letter-spacing:.5px;font-weight:780}
.p20 .title{top:121px}.p21 .title{top:118px}.p22 .title{top:115px}
.p19 .title{font-size:88.3px;font-weight:700;letter-spacing:.5px;top:248px;transform:translateX(-1px)}
.p19{background-image:radial-gradient(ellipse 430px 230px at 50% 6%,#153e5c 0,rgba(21,62,92,.65) 52%,transparent 80%),linear-gradient(to top,#17436b 0,transparent 22%)}
.slide:not(.p19){background-image:radial-gradient(ellipse 790px 450px at 0 0,#16476d 0,rgba(22,71,109,.58) 49%,transparent 82%),radial-gradient(ellipse 700px 560px at 100% 100%,#153e5c 0,rgba(21,62,92,.3) 45%,transparent 80%)}
.p23 .qa{font-size:203.1px;font-weight:600;letter-spacing:.5px;top:183.6px}
.p24 .title{font-family:Mont;font-size:100px;font-weight:700;letter-spacing:-1.5px;line-height:1.2;top:249px;transform:scale(.99)}
.value h2{font-weight:400}.value h2 b{font-weight:700}
.chips{gap:27px}.chip{font-size:28px;height:65px;padding:0 30px}.chip:last-child{padding-inline:26px}
''')
p=R/'replica/slide_21.html';s=p.read_text().replace('고객이<br>최우선입니다.','<b>고객이</b><br>최우선입니다.').replace('함께 더 멀리<br>갈 수 있습니다.','<b>함께</b> 더 멀리<br>갈 수 있습니다.').replace('실행만이<br>증명합니다.','<b>실행만이</b><br>증명합니다.');p.write_text(s)
for p in C.rglob('*.css'):shutil.copy(p,R/'assets/collection'/p.relative_to(C))
print('Fourth fidelity pass ready; independent replica updated too')
