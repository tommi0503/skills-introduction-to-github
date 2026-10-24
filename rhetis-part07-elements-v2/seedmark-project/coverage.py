from pathlib import Path
from lxml import html
import json,re
P=Path(__file__).parent;M=json.loads((P/'map.json').read_text());out=[]
norm=lambda t:re.sub(r'\s+','',t).casefold()
for q in M['rawMeasurements']:
 page=q['page'];doc=html.fromstring((P/f'reassembled/slide_{page:02}.html').read_text());text=norm(doc.text_content())
 for n in q['nodes']:
  txt=norm(n['text']);
  if not txt or txt in text:continue
  gaps=[i['id']for i in M['instances']if i['page']==page and i['use']=='unexpressible'and any(s==f'main > :nth-child({n["index"]+1})'for s in i['selectors'])]
  out.append({'page':page,'index':n['index'],'text':n['text'],'gapIds':gaps})
(P/'text-coverage.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
for x in out:print(x)
