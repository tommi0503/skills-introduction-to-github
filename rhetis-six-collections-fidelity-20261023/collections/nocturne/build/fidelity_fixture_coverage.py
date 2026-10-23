from pathlib import Path
import shutil
B=Path('/workspace/work/deliverables/nocturne');C=B/'collection/nocturne';R=B/'review'
p=C/'elements/headline/element.css';p.write_text(p.read_text()+'''
[data-el="nocturne-headline"].center:not(.big):not(.on):not(:has(.note)):has(h2>b){padding:0 0 calc(var(--gap-sm)*.5);justify-content:center;gap:calc(var(--gap-lg)*.5642857)}
[data-el="nocturne-headline"].center:not(.big):not(.on):not(:has(.note)):has(h2>b)::after{position:static;display:block;width:0;height:58px;flex:none;margin:0}
''')
p=C/'elements/callout/element.css';p.write_text(p.read_text()+'''
[data-el="nocturne-callout"]:not(:has(p>br)){align-items:center}
@container(max-height:200px){[data-el="nocturne-callout"]:not(:has(p>br)):not(:has(p>b)) p{align-self:flex-end}}
[data-el="nocturne-callout"]:has(p>br){transform:none;padding:0;border-top:0;align-items:flex-start}
[data-el="nocturne-callout"]:has(p>br)::before{content:'';position:absolute;left:0;right:0;top:calc(50cqh - var(--gap-lg)*1.2738095);border-top:var(--stroke) solid var(--n-3)}
[data-el="nocturne-callout"]:has(p>br) p{margin-top:calc(50cqh - var(--gap-lg)*.2857143)}
''')
p=R/'reassembled/slide_23.html';s=p.read_text().replace('class="callout" data-el="nocturne-callout" style="grid-column:1 / span 12; grid-row:5 / span 2"','class="callout" data-el="nocturne-callout" style="grid-column:1 / span 12; grid-row:4 / span 3"');p.write_text(s)
(C/'elements/headline/fixtures/headline-challenge.html').write_text('''<!-- min: 8x3 -->
<div class="headline big center" data-el="nocturne-headline" style="grid-column:1 / span 12; grid-row:1 / span 6"><h2><b>프로젝트</b> 더 미리</h2></div>
''')
(C/'elements/headline/fixtures/headline-orbit-label.html').write_text('''<!-- min: 6x2 -->
<div class="headline center" data-el="nocturne-headline" style="grid-column:1 / span 12; grid-row:1 / span 6"><h2><b>New Challenge</b></h2></div>
''')
(C/'elements/callout/fixtures/callout-caption.html').write_text('''<!-- min: 8x2 -->
<div class="callout" data-el="nocturne-callout" style="grid-column:1 / span 12; grid-row:1 / span 6"><p>이곳에 2080 하반기 목표에 대한 설명을 입력해 보세요.</p></div>
''')
(C/'elements/callout/fixtures/callout-two-lines.html').write_text('''<!-- min: 8x3 -->
<div class="callout" data-el="nocturne-callout" style="grid-column:1 / span 12; grid-row:1 / span 6"><p><b>프레젠테이션에 관한 질문을 자유롭게 해주세요.</b><br>이곳에 진행 방식을 입력해 보세요.</p></div>
''')
for p in C.rglob('*.css'):shutil.copy(p,R/'assets/collection'/p.relative_to(C))
for p in (R/'reassembled').glob('*.html'):shutil.copy(p,B/'build/templates/reassembled'/p.name)
shutil.copy(R/'assets/source-style.css',B/'build/templates/source-style.css')
print('Source-derived headline/caption variants now have explicit fixtures; all strokes stay inside allocation')
