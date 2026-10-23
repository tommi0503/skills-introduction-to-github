from pathlib import Path
import shutil,json,hashlib
C=Path('/workspace/work/deliverables/confluence/collection/confluence');R=C.parent.parent/'review'
p=C/'elements/chart-donut/element.css'
p.write_text(p.read_text()+'''
.donut[data-el="confluence-chart-donut"]{padding:0;height:100%;width:auto;max-height:500px;max-width:100%;aspect-ratio:1;justify-self:center}
.donuts[data-el="confluence-chart-donut"]{container-type:size;flex-wrap:wrap;align-content:center}
.donuts[data-el="confluence-chart-donut"]>.donut{padding:0;flex:1 1 160px;height:auto;max-height:none;width:auto;max-width:500px;aspect-ratio:1}
@container (max-width:650px){
.donuts[data-el="confluence-chart-donut"]>.donut{flex:0 0 calc((100cqh - var(--gap))/2);height:calc((100cqh - var(--gap))/2);width:calc((100cqh - var(--gap))/2);max-height:100%;padding:0}
.donuts[data-el="confluence-chart-donut"]>.donut .fig{font-size:var(--type-24)}
.donuts[data-el="confluence-chart-donut"]>.donut .name{font-size:var(--type-12);margin-top:calc(var(--gap-sm)/2)}
}
''')
p.write_text(p.read_text()+'\n@container (max-width:650px){.donuts[data-el="confluence-chart-donut"]>.donut{flex-basis:min(calc((100cqh - var(--gap))/2),calc((100cqw - var(--gap))/2));height:min(calc((100cqh - var(--gap))/2),calc((100cqw - var(--gap))/2));width:min(calc((100cqh - var(--gap))/2),calc((100cqw - var(--gap))/2))}}\n')
p=C/'elements/waffle/fixtures/waffle-figures.html';p.write_text(p.read_text().replace('<!-- min: 6x3 -->','<!-- min: 6x4 -->'))
for f in C.rglob('*.css'):
 dst=R/'assets/collection'/f.relative_to(C);dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy(f,dst)
(R/'source-manifest.json').write_text(json.dumps({str(p.relative_to(C)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(C.rglob('*')) if p.is_file()},indent=2))
