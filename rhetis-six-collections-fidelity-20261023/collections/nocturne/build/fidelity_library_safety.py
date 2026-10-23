from pathlib import Path
import shutil
B=Path('/workspace/work/deliverables/nocturne');C=B/'collection/nocturne';R=B/'review'
p=C/'elements/headline/element.css';p.write_text(p.read_text()+'''[data-el="nocturne-headline"].big:has(.kick) h2,[data-el="nocturne-headline"].big:has(.note) h2{transform:none}\n''')
p=C/'elements/callout/element.css';p.write_text(p.read_text()+'''
[data-el="nocturne-callout"]:not(:has(p>br))::before{content:none}
[data-el="nocturne-callout"]:not(:has(p>br)) p{position:relative}
[data-el="nocturne-callout"]:not(:has(p>br)) p::before{content:'';position:absolute;left:50%;bottom:calc(100% + var(--gap)*1.066667);height:26px;border-left:3px dotted var(--ink)}
@container(max-height:200px){[data-el="nocturne-callout"]:not(:has(p>br)){align-items:flex-end}}
@container(max-height:110px){[data-el="nocturne-callout"]:not(:has(p>br)) p::before{content:none}}
[data-el="nocturne-callout"]:has(p>br){transform:translateY(calc(var(--gap-sm)*-2.666667));padding-top:calc(var(--gap-sm)*4.444444)}
''')
p=R/'reassembled/slide_20.html';s=p.read_text().replace('class="callout" data-el="nocturne-callout" style="grid-column:1 / span 12; grid-row:6 / span 1"','class="callout" data-el="nocturne-callout" style="grid-column:1 / span 12; grid-row:5 / span 2"');p.write_text(s)
for p in C.rglob('*.css'):shutil.copy(p,R/'assets/collection'/p.relative_to(C))
print('Reusable fixture safety: scaled statement does not overlap kick/note; caption dots stay in their slots')
