from pathlib import Path
import re
C=Path('/workspace/output/cyanloop');canonical={'card','callout','chart-area','chart-bar','chart-donut','chart-line'}
for p in C.glob('elements/*/fixtures/*.html'):
 if p.parent.parent.name in canonical:continue
 txt=p.read_text()
 def normalize(m):
  v=m.group(1);v=re.sub(r'grid-column:[^;]+','grid-column:1 / span 12',v);v=re.sub(r'grid-row:[^;]+','grid-row:1 / span 6',v);return 'style="'+v+'"'
 txt=re.sub(r'style="([^"]+)"',normalize,txt,count=1);p.write_text(txt)
p=C/'elements/person/fixtures/person.html';p.write_text(re.sub(r'<!-- min:.*?-->','<!-- min: 6x4 -->',p.read_text()))
