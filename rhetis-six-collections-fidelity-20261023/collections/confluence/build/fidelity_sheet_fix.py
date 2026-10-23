from pathlib import Path
import re,shutil,json
D=Path('/workspace/work/deliverables/confluence');C=D/'collection/confluence';R=D/'review'
p=C/'elements/card/fixtures/source-project-metrics.html';s=p.read_text();s=re.sub(r'(<div class="card[^>]+?) style="[^"]+"',r'\1',s);p.write_text(s)
p=C/'elements/card/element.css';s=p.read_text();s+='\n.card[data-el="confluence-card"].line:has(.kick):not(:has(.fig)) .kick{height:calc(100% - 17px)}.card[data-el="confluence-card"].line:has(.kick):not(:has(.fig)) .name{top:calc(50% - 19.5px)}\n';p.write_text(s)
p=C/'elements/hub/element.css';s=p.read_text();s+='\n.hub[data-el="confluence-hub"] .mark{font-size:var(--type-18);line-height:var(--label-line)}.hub[data-el="confluence-hub"] .mark:has(.icon){font-size:var(--type-8);line-height:var(--confluence-line-height-0)}\n';p.write_text(s)
for p in C.rglob('*.css'):
 out=R/'assets/collection'/p.relative_to(C);out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,out)

p=C/"elements/agenda/element.css";s=p.read_text();s+="\n.agenda[data-el=\"confluence-agenda\"] .entry:nth-child(odd) .mark{background:var(--a2-9)}\n";p.write_text(s)
p=R/"assets/reference-style.css";p.write_text(p.read_text()+"\n.slide{--a2-9:#3858e3;}\n")
