from pathlib import Path
import shutil,json
B=Path('/workspace/work/deliverables/nocturne');C=B/'collection/nocturne';R=B/'review';before=R/'revision-before';before.mkdir(exist_ok=True)
for n in range(19,25):
 for kind in ['replica','reassembled','compare-reassembled']:
  p=R/kind/f'slide_{n}.png';q=before/kind/p.name;q.parent.mkdir(exist_ok=True);shutil.copy(p,q)
def patch(folder,s):
 p=C/f'elements/{folder}/element.css';p.write_text(p.read_text()+s.replace('R',f'[data-el="nocturne-{folder}"]')+'\n')
p=C/'kit/kit.json';k=json.loads(p.read_text());k['extensions'].update({'--nocturne-statement-weight':'weight','--nocturne-statement-scale':'number','--nocturne-display-gradient-start':'number'});p.write_text(json.dumps(k,indent=2))
p=C/'kit/css/tokens.css';p.write_text(p.read_text()+'.slide{--nocturne-statement-weight:700;--nocturne-statement-scale:1.59375;--nocturne-display-gradient-start:23;}\n')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
/* Fidelity revision: the two lights are drawn, never supplied as a bitmap. */
.slide{background-image:radial-gradient(ellipse 760px 520px at 0 0,var(--a1-2-soft) 0,color-mix(in srgb,var(--a1-2-soft) 35%,transparent) 49%,transparent 82%),radial-gradient(ellipse 650px 560px at 100% 100%,var(--a1-3-soft) 0,color-mix(in srgb,var(--a1-3-soft) 30%,transparent) 45%,transparent 80%)}
.slide:has(.body>.prose){background-image:radial-gradient(ellipse 700px 350px at 50% 6%,var(--a1-3-soft) 0,color-mix(in srgb,var(--a1-3-soft) 65%,transparent) 52%,transparent 80%),linear-gradient(to top,var(--a1-2-soft) 0,transparent 22%)}
.slide .top{top:calc(var(--furn-edge) - var(--gap-sm)/2);left:calc(var(--furn-edge) - 1px);right:calc(var(--furn-edge) - 1px);z-index:5;color:var(--n-8)}
.slide .top .sec{color:var(--n-6)}
.slide .head{gap:calc(var(--gap-sm)*1.5)}
.slide .head .kicker{line-height:var(--label-line);transform:translateY(calc(var(--gap-sm)/-6))}
.slide .page{gap:calc(var(--gap-lg)*.75)}
.slide .page:has(>.head.center)>.body>.group{gap:0}
.slide .body:has(>.seat.back){position:static}
.slide .body>.seat.back{inset:auto 0 0;height:330px;width:100%;max-height:none;z-index:-1}
.slide.cover .lockup{gap:calc(var(--gap-lg)*.5);transform:translateY(calc(var(--gap-sm)*-1.4))}
.slide.cover .title{background:linear-gradient(90deg,var(--a1) 17%,var(--a1-1-soft) 43%,var(--ink) 70%);background-clip:text;color:transparent}
.slide.cover .title b{color:inherit}
.slide.cover .meta{bottom:calc(var(--furn-edge) + var(--gap-sm)/2);line-height:var(--label-line);color:var(--n-8)}
''')
patch('headline','''R.big:has(h2>b) h2{background:linear-gradient(90deg,var(--a1) 0,var(--a1-1-soft) 45%,var(--ink) 83%);background-clip:text;color:transparent;transform:translateY(calc(var(--gap-sm)*-.53))}R.big:has(h2>b) h2 b{color:inherit}R.center:not(.big):not(.on):not(:has(.note)):not(:has(h2>b)) h2{font-size:var(--type-30);line-height:var(--label-line);transform:translateY(calc(var(--gap-lg)*.583333))}R.big:not(:has(h2>b)) h2{font-weight:var(--nocturne-statement-weight)}@container(min-width:900px) and (min-height:250px){R.big:not(:has(h2>b)) h2{transform:translateY(calc(var(--gap-sm)*-.222222)) scale(var(--nocturne-statement-scale))}}''')
patch('callout','''R:has(p>br){margin-inline:calc(var(--gap-lg)*.928571);align-items:flex-start;padding-top:calc(var(--gap-sm)*4.2);border-color:var(--n-3)}R:has(p>br) p{font-size:var(--type-32);line-height:1.7}R:has(p>br) b{color:var(--ink);font-weight:var(--title-weight)}R:not(:has(p>br)){border-top:0}R:not(:has(p>br))::before{content:'';position:absolute;left:50%;top:calc(var(--gap-sm)*-3.2);height:26px;border-left:3px dotted var(--ink)}''')
# Exact data is preserved; only a structural distinction separates source title roles.
p=R/'reassembled/slide_23.html';s=p.read_text().replace('<h2><b>의견과 피드백을 환영합니다!</b></h2>','<h2>의견과 피드백을 환영합니다!</h2>');p.write_text(s)
# Host palette keeps the original accent positions while remaining outside the collection.
p=R/'assets/source-style.css';s=p.read_text().replace('--a1-1-soft:#08141e','--a1-1-soft:#d5ecfc').replace('--a1-2-soft:#153e5c','--a1-2-soft:#19496d');s+='\n.slide.dark{--a1-3-soft:#153e5c;}\n';p.write_text(s)
for p in C.rglob('*.css'):
 q=R/'assets/collection'/p.relative_to(C);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy(p,q)
print('Fidelity revision sources patched; page-only render follows')
