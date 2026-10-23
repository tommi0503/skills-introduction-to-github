from pathlib import Path
import re,json
C=Path('/workspace/output/cyanloop');canonical={'card','callout','chart-area','chart-bar','chart-donut','chart-line'};changed=set(['logo-group','hub','list'])
for p in C.glob('elements/*/fixtures/*.html'):
 name=p.parent.parent.name
 if name in canonical:continue
 old=p.read_text();new=re.sub(r';?\s*justify-content:[^;\"]+','',old);new=re.sub(r';?\s*gap:var\(--gap(?:-lg)?\)','',new)
 new=re.sub(r'<span class="icon">[^<]+</span>','<span class="icon" data-icon="book-open"></span>',new)
 if new!=old:p.write_text(new);changed.add(name)
p=C/'elements/logo-group/element.css';s=p.read_text();r='.logos[data-el="cyanloop-logo-group"]';s+='\n'+r+'{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));align-content:center;justify-items:center;}'+r+' .seat.logo{width:100%;max-width:160px;min-width:0;aspect-ratio:1;}'+r+':has(>.seat:nth-child(6):last-child){grid-template-columns:repeat(6,minmax(0,1fr));}\n';p.write_text(s)
p=Path('/workspace/work/cyanloop/render_final.py');s=p.read_text();s=re.sub(r'selected=\{[^\n]+\}',f'selected={changed!r}',s);p.write_text(s)
print('affected:',','.join(sorted(changed)))
