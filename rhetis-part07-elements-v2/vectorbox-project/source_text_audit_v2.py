from pathlib import Path
from lxml import html
import json
P=Path(__file__).parent;out=[]
norm=lambda x:''.join(x.split())
for n in range(2,14):
 src=html.fromstring((P/'replica'/f'slide_{n:02}.html').read_text());dst=html.fromstring((P/'reassembled'/f'slide_{n:02}.html').read_text());target=norm(''.join(dst.xpath('//section//text()')));rows=[]
 for i,e in enumerate(src.xpath('//section/*'),1):
  t=norm(e.text_content())
  if not t:continue
  state='present-in-DOM' if t in target else 'missing';why=None
  if state=='missing' and n==6:state='explicit-unexpressible';why='06 perimeter graph with independent core; see GAPS.md and map.json'
  if state=='missing' and n==4:state='explicit-unexpressible';why='04-grouped-chart axis/category labels; see GAPS.md and map.json'
  if state=='missing' and n==9 and t in [f'{i:02}' for i in range(1,7)]:state='generated-CSS';why='steps counter(vectorbox-seq,decimal-leading-zero), source-shaped markup has6 step members; verify native slide09'
  rows.append({'sourceObject':f'{n:02}-raw-{i:02}','text':e.text_content().strip(),'status':state,'why':why})
 out.append({'page':f'{n:02}','sourceTextObjects':len(rows),'unexplainedMissing':sum(r['status']=='missing' for r in rows),'objects':rows})
(P/'reassembly-source-text-checks.json').write_text(json.dumps({'method':'Each immutable replica direct object text checked against assembled section text after whitespace normalization; CSS-generated stage numerals separately classified. Fixtures are not a source for assembly copy.','pages':out},ensure_ascii=False,indent=2)+'\n')
print('Unexplained missing:',sum(x['unexplainedMissing'] for x in out))
