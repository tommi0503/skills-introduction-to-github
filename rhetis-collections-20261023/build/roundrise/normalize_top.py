from pathlib import Path
import re,hashlib,json
B=Path('/workspace/output/roundrise');canonical={'card','callout','chart-area','chart-bar','chart-donut','chart-line'};changed=[]
for p in B.glob('elements/*/fixtures/*.html'):
 if p.parts[-3] in canonical:continue
 s=p.read_text();m=re.search(r'(<(?:div|section|span|p)\b[^>]*?\s)style="([^"]*)"',s)
 if not m:continue
 parts=[]
 for d in m[2].split(';'):
  if ':' not in d:continue
  k,v=d.split(':',1);k=k.strip();v=v.strip()
  if k in ['grid-column','grid-row'] or k.startswith('--'):parts.append(k+':'+v)
 new=m[1]+'style="'+'; '.join(parts)+'"'
 t=s[:m.start()]+new+s[m.end():]
 if t!=s:p.write_text(t);changed.append(str(p.relative_to(B)))
print('normalized',len(changed),'fixtures');print('\n'.join(changed))
m={str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in B.rglob('*') if p.is_file()};Path('/workspace/work/roundrise/frozen-source-manifest.json').write_text(json.dumps(m,indent=2))
