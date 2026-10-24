from pathlib import Path
from lxml import html as L
import re,json,unicodedata
P=Path(__file__).parent
norm=lambda s:re.sub(r'\s+','',unicodedata.normalize('NFC',s or ''))
source=json.loads((P/'source-measurements.json').read_text());grams={}
for page in source['pages']:
 for part in page['parts']:
  t=norm(part['text'])
  for i in range(len(t)-5):grams.setdefault(t[i:i+6],page['page'])
rows=[]
for f in sorted((P/'crossrail/elements').glob('*/fixtures/*.html')):
 roots=L.fragments_fromstring(re.sub(r'^<!--.*?-->\s*','',f.read_text(),count=1,flags=re.S))
 for root in roots:
  if not hasattr(root,'iter'):continue
  for el in root.iter():
   if not isinstance(el.tag,str):continue
   for field,txt in [('text',el.text),('tail',el.tail)]:
    t=norm(txt);hits=sorted({t[i:i+6] for i in range(len(t)-5) if t[i:i+6] in grams})
    if hits:rows.append({'file':str(f.relative_to(P)),'tag':el.tag,'class':el.get('class',''),'field':field,'text':txt,'matches':hits,'pages':sorted({grams[x] for x in hits})})
(P/'text-copy-check.json').write_text(json.dumps({'matches':rows,'count':len(rows)},ensure_ascii=False,indent=2)+'\n');print(json.dumps(rows,ensure_ascii=False,indent=2))
