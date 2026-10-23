from pathlib import Path
import re,shutil
D=Path('/workspace/work/deliverables/confluence');C=D/'collection/confluence';R=D/'review'
p=C/'foundation/foundation.css';s=p.read_text();s=s.replace('.page:not(:has(>.head)){inset:0;display:block}.page:not(:has(>.head))>.body{height:100%}', '.page.overrides{inset:0;display:block}.page.overrides>.body{height:100%}');p.write_text(s)
p=R/'reassembled/slide_04.html';s=p.read_text().replace('<div class="page">','<div class="page overrides">',1);p.write_text(s)
p=C/'elements/hub/element.css';s=p.read_text().replace('.hub[data-el="confluence-hub"]:has(>.spoke:nth-child(5):last-child){display:block}','');p.write_text(s)
p=C/'elements/card/element.css';s=p.read_text();s+='\n.card[data-el="confluence-card"] .icon,.card[data-el="confluence-card"] .seat.icon{font-size:var(--type-20);line-height:var(--confluence-line-height-1)}\n';p.write_text(s)
for p in C.rglob('*.css'):
 out=R/'assets/collection'/p.relative_to(C);out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,out)
