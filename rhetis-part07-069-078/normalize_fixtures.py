from pathlib import Path
import re,sys
from scaffold import GOLD
R=Path(__file__).resolve().parent
for kid in sys.argv[1:]:
 count=0
 for p in (R/(kid+'-project')/kid/'elements').glob('*/fixtures/*.html'):
  if p.parent.parent.name in GOLD and p.stem in GOLD[p.parent.parent.name][1]:continue
  txt=p.read_text();m=re.search(r'<(?!\!)[a-zA-Z][^>]*>',txt)
  if not m:continue
  tag=m.group();st=re.search(r'style="([^"]*)"',tag)
  if st:
   value=st.group(1);value=re.sub(r'grid-column\s*:[^;"\n]+','grid-column:1 / span 12',value);value=re.sub(r'grid-row\s*:[^;"\n]+','grid-row:1 / span 6',value)
   if 'grid-column:' not in value:value+='; grid-column:1 / span 12'
   if 'grid-row:' not in value:value+='; grid-row:1 / span 6'
   newtag=tag[:st.start(1)]+value+tag[st.end(1):]
  else:newtag=tag[:-1]+' style="grid-column:1 / span 12; grid-row:1 / span 6">'
  out=txt[:m.start()]+newtag+txt[m.end():]
  if txt!=out:p.write_text(out);count+=1
 print(kid,'non-golden fixture placements normalized',count)
