from pathlib import Path
import shutil
D=Path('/workspace/work/deliverables/confluence');C=D/'collection/confluence';R=D/'review'
p=C/'foundation/foundation.css';s=p.read_text();s+='''\n/* Palette roles: source host preserves the exact original color values. */
.title b,.cover .title b{color:var(--a1-8)}.title b~b,.cover .title b~b{color:var(--a2-8)}
.cover .title small{color:var(--n-5)}.cover .kicker{color:var(--a1-7)}.rail .kicker{color:var(--a2-7)}.head.center .kicker{color:var(--a2-7)}
''';p.write_text(s)
p=C/'elements/card/element.css';s=p.read_text();s+='\n.card[data-el="confluence-card"].tone-1:has(.fig) .name,.card[data-el="confluence-card"].tone-1:has(.fig) .note>b{color:var(--a1-8)}\n';p.write_text(s)
p=C/'elements/agenda/element.css';s=p.read_text();s+='\n.agenda[data-el="confluence-agenda"] .entry .mark{color:var(--a1-1)}.agenda[data-el="confluence-agenda"] .entry:nth-child(even) .mark{color:var(--a1-on)}.agenda[data-el="confluence-agenda"] .entry .note{color:var(--n-7)}\n';p.write_text(s)
p=C/'elements/hub/element.css';s=p.read_text();s+='\n.hub[data-el="confluence-hub"] .spoke:nth-child(3) .name b,.hub[data-el="confluence-hub"] .spoke:nth-child(4) .name b{color:var(--a1-8)}\n';p.write_text(s)
p=R/'assets/reference-style.css';s=p.read_text();s+='\n.slide{--a1-1:#44cde5;--a1-7:#a8d8e8;--a1-8:#44cde5;--a2-7:#9cabb0;--a2-8:#3858e3;--n-5:#7b8183;--n-7:#979fa4;}\n';p.write_text(s)
for p in C.rglob('*.css'):
 out=R/'assets/collection'/p.relative_to(C);out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,out)
