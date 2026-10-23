from pathlib import Path
import re,shutil,json,hashlib
C=Path('/workspace/work/deliverables/confluence/collection/confluence');R=C.parent.parent/'review'
for name,file in [('matrix','swot'),('person','person')]:
 p=C/'elements'/name/'fixtures'/f'{file}.html';s=p.read_text().replace('<ul class="list">','<div class="list" data-el="confluence-list">').replace('</ul>','</div>');s=re.sub(r'<li>(.*?)</li>',r'<div class="item"><p class="name">\1</p></div>',s);p.write_text(s)
p=C/'elements/matrix/element.css';p.write_text(p.read_text()+'''
.matrix[data-el="confluence-matrix"] .cell.on .list{color:var(--a1-on)}
@container (max-width:650px){
.matrix[data-el="confluence-matrix"].swot .cell{padding:var(--gap-sm);gap:calc(var(--gap-sm)/2)}
.matrix[data-el="confluence-matrix"].swot .cell>.name{font-size:var(--type-18)}
.matrix[data-el="confluence-matrix"].swot .kick{font-size:var(--type-24)}
.matrix[data-el="confluence-matrix"].swot .list{padding:0;gap:calc(var(--gap-sm)/2)}
.matrix[data-el="confluence-matrix"].swot .list .item{padding-left:var(--gap)}
.matrix[data-el="confluence-matrix"].swot .list .name{font-size:var(--type-14)}
}
''')
p=C/'elements/person/element.css';p.write_text(p.read_text()+'''
.person[data-el="confluence-person"] .list{width:100%;max-width:480px;padding:0;gap:calc(var(--gap-sm)/2)}
.person[data-el="confluence-person"] .list .item{padding-left:var(--gap)}
.person[data-el="confluence-person"] .list .name{font-size:var(--type-16)}
@container (max-width:650px){.person[data-el="confluence-person"]>.seat{width:80px;height:80px}}
''')
for f in C.rglob('*.css'):
 dst=R/'assets/collection'/f.relative_to(C);dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy(f,dst)
(R/'source-manifest.json').write_text(json.dumps({str(p.relative_to(C)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(C.rglob('*')) if p.is_file()},indent=2))
