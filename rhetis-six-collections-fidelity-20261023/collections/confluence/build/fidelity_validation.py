from pathlib import Path
import shutil,re
D=Path('/workspace/work/deliverables/confluence');C=D/'collection/confluence';R=D/'review'
p=C/'elements/hub/element.css';s=p.read_text().replace('@container(min-width:1000px)','@container(min-width:1200px)').replace('@container (min-width:1000px)','@container (min-width:1200px)');s+='\n@container(min-width:1200px){.hub[data-el="confluence-hub"]:has(>.spoke:nth-child(5):last-child) .core .name{left:3px;right:3px;transform:none}}\n';p.write_text(s)
p=C/'foundation/foundation.css';s=p.read_text();s+='\n.page:has(>.head.center)>.body{top:272px;height:374px}\n';p.write_text(s)
p=C/'elements/agenda/element.css';s=p.read_text();s+='\n.agenda[data-el="confluence-agenda"]{padding-top:var(--confluence-row-gap)}\n';p.write_text(s)
# Source structure fixtures exercise the library-level metric/header treatments.
s=(R/'reassembled/slide_03.html').read_text();cards=re.findall(r'<div class="card [^"]+".*?</div></div>',s)
(C/'elements/card/fixtures/source-project-name.html').write_text('<!-- min: 12x2 -->\n'+cards[0]+'\n')
cards=[re.sub(r'style="[^"]+"','style="grid-column:1 / span 12;grid-row:1 / span 6"',c,count=1) for c in cards[1:]]
(C/'elements/card/fixtures/source-project-metrics.html').write_text('<!-- min: 12x5 -->\n<div class="group three" style="grid-column:1 / span 12;grid-row:1 / span 6">'+''.join(cards)+'</div>\n')
p=R/'replica/slide_01.html';s=p.read_text().replace('line-height:.92;margin-top:8px','line-height:.92;margin-top:8px;height:253px').replace('letter-spacing:-.65px;margin-top:16px','letter-spacing:-.65px;margin-top:-1.5px');p.write_text(s)
p=R/'replica/slide_03.html';s=p.read_text().replace('letter-spacing:2.1px;font-weight:800','letter-spacing:2.1px;font-weight:800;height:125px').replace('letter-spacing:2px;margin-top:13px','letter-spacing:2px;margin-top:8px');p.write_text(s)
p=R/'replica/slide_04.html';s=p.read_text().replace('letter-spacing:2.1px;font-weight:800;color:white','letter-spacing:2.1px;font-weight:800;color:white;height:125px').replace('letter-spacing:2px;margin-top:13px','letter-spacing:2px;margin-top:8px');p.write_text(s)
p=R/'replica/replica.css';s=p.read_text()+'\n.icon svg{display:block}\n';p.write_text(s)
for p in C.rglob('*.css'):
 out=R/'assets/collection'/p.relative_to(C);out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,out)
