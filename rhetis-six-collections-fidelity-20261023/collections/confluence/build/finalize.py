from pathlib import Path
import json,shutil
R=Path('/workspace/work/deliverables/confluence/review');C=R.parent/'collection/confluence'
shutil.copy('/workspace/work/tools/icons-runtime.js',R/'assets/icons-runtime.js');shutil.copy('/workspace/work/tools/LUCIDE-LICENSE.txt',R/'assets/LUCIDE-LICENSE.txt')
for f in (R/'reassembled').glob('slide_*.html'):f.write_text(f.read_text().replace('src="../assets/icons.js"','src="../assets/icons-runtime.js"'))
p=R/'assets/icons.js'
if p.exists():p.unlink()
pal=json.loads(Path('/workspace/work/reference/contract/palette.json').read_text())['light']
pal.update({'--page':'#ffffff','--ink':'#090b0e','--a1':'#41c6db','--a1-on':'#082d36','--a2':'#3a54df','--a2-on':'#ffffff'})
for i,col in enumerate(['#f8fafb','#e1e4e6','#d0d8df','#b0bdc8','#8b99a6','#7b8792','#667078','#4b5055','#111720'],1):pal['--n-'+str(i)]=col
for a,arr in [(1,['#effbfc','#dcf5f8','#bde9ee','#8cd9e3','#41c6db','#269eb2','#197c8d','#125c69','#0c3f49']),(2,['#eef1ff','#dde4ff','#c1ccff','#8396f2','#3a54df','#354bc5','#2d40aa','#25368b','#1d296b'])]:
 for i,col in enumerate(arr,1):
  for suffix in ['', '-soft','-muted']:pal[f'--a{a}-{i}{suffix}']=col
(R/'assets/reference-style.css').write_text('.slide{'+''.join(k+':'+v+';' for k,v in pal.items())+'}\n')
p=C/'foundation/foundation.css';s=p.read_text().replace('.title b+b','.title b~b');s+='''.rail{width:calc(var(--rail-w) + var(--gap-lg));height:calc(720px - 2*var(--margin-y))}.rail::after{right:0}.rail .lead{max-width:var(--rail-w)}\n''';p.write_text(s)
p=C/'elements/card/element.css';p.write_text(p.read_text()+'.card[data-el="confluence-card"] .parts:has(.fig)>.fig:has(br){font-size:var(--type-22)}\n')
p=C/'kit/css/tokens.css';p.write_text(p.read_text().replace('--figure-line: 1.0','--figure-line: 1.1'))
def add(folder,text):
 p=C/'elements'/folder/'element.css';p.write_text(p.read_text()+text+'\n')
q='.card[data-el="confluence-card"]'
add('card',f'''{q}.on .parts>.fig,{q}.on .parts>.name,{q}.on .parts>.fig small{{color:var(--a1-on)}}''')
q='.hub[data-el="confluence-hub"]'
add('hub',f'''{q} .spoke.on{{padding:var(--gap-sm);align-items:center;justify-content:center;text-align:center}}@container (max-width:650px){{{q} .core:not(:has(.seat)){{padding:var(--gap-sm)}}{q} .core .name{{font-size:var(--type-20)}}}}''')
q='.frame[data-el="confluence-image-frame"]';add('image-frame',f'{q}'+'{width:100%;height:100%;max-width:100%;max-height:100%}')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'.stack>*{flex:1 1 0}\n')
q=':is(.stat[data-el="confluence-metric"],.stats[data-el="confluence-metric"])'
add('metric',f'''{q}.stat{{container-type:size}}{q}.stats>.stat{{align-self:stretch}}@container (max-height:110px){{{q} .parts{{gap:calc(var(--gap-sm)/2)}}{q} .fig{{font-size:var(--type-32)}}{q} .name{{font-size:var(--type-16)}}{q} .note{{display:none}}}}{q} .stat{{padding:calc(var(--gap-sm)/2)}}''')
q='.callout[data-el="confluence-callout"]'
add('callout',f'''{q}{{padding:var(--gap-sm)}}@container (max-width:650px){{{q} p{{font-size:var(--type-18)}}}}''')
q='.pill[data-el="confluence-pill"]';add('pill',f'@container (max-width:380px){{{q} .note'+'{display:none}}')
q='.prose[data-el="confluence-prose"]';add('prose',f'''@container (max-width:650px){{{q} p{{font-size:var(--type-18)}}}}@container (max-width:380px){{{q} p{{font-size:var(--type-16)}}}}''')
q='.headline[data-el="confluence-headline"]';add('headline',f'''{q}{{container-type:size}}@container (max-height:110px){{{q} .kick,{q} .note{{display:none}}{q} h2{{font-size:var(--type-28)}}}}''')
q='.waffle[data-el="confluence-waffle"]'
add('waffle',f'''{q}{{display:grid;grid-template-rows:minmax(0,1fr) auto auto;align-items:center;justify-items:center;gap:var(--gap-sm)}}{q} .units{{height:100%;width:auto;aspect-ratio:1;max-width:100%;grid-auto-rows:minmax(0,1fr)}}{q} .u{{min-height:0;aspect-ratio:auto}}{q} .units:has(>.u:nth-child(10):last-child){{aspect-ratio:10}}{q} .units:has(>.u:nth-child(20):last-child){{aspect-ratio:5}}{q} .units:has(>.u:nth-child(50):last-child){{aspect-ratio:2}}{q} .fig{{font-size:var(--type-40)}}{q} .name small{{display:block;font-size:var(--type-14);color:var(--ink)}}''')
p=C/'elements/waffle/fixtures/waffle-figures.html';p.write_text(p.read_text().replace('<!-- min: 6x1 -->','<!-- min: 6x3 -->'))
q='.heat[data-el="confluence-heatmap"]';add('heatmap',f'''{q} .cell b{{background:var(--page);color:var(--ink);padding:2px calc(var(--gap-sm)/2);border-radius:var(--radius-sm)}}''')
q='.code[data-el="confluence-code"]';add('code',f'{q} .s'+'{color:var(--a2-8)}')
q='.matrix[data-el="confluence-matrix"]';add('matrix',f'{q} .cell.on .kick'+'{color:var(--a1-on)}')
for p in [C/'foundation/foundation.css',*(C/'elements').glob('*/element.css')]:
 s=p.read_text()
 for n in range(1,5):s=s.replace('color:var(--a'+str(n)+'-7)','color:var(--a'+str(n)+'-8)')
 p.write_text(s)
p=C/'kit/kit.json';o=json.loads(p.read_text());o['extensions']['--confluence-font-code']='font';p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
p=C/'kit/css/tokens.css';p.write_text(p.read_text()+".slide{--confluence-font-code:'Nanum Gothic Coding'}\n")
p=C/'elements/code/element.css';p.write_text(p.read_text()+'.code[data-el="confluence-code"]{font-family:var(--confluence-font-code)}\n')
# Prevent preview frame's unscoped small-label colour from reaching number units.
for d in (C/'elements').iterdir():
 p=d/'element.css';p.write_text(p.read_text()+f'[data-el="confluence-{d.name}"] small'+'{color:inherit}\n')
# Portable review bundle: same library CSS, copied byte-for-byte, without page-local rules.
for f in C.rglob('*.css'):
 dst=R/'assets/collection'/f.relative_to(C);dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy(f,dst)
for f in (R/'reassembled').glob('slide_*.html'):f.write_text(f.read_text().replace('../../collection/confluence/','../assets/collection/'))
