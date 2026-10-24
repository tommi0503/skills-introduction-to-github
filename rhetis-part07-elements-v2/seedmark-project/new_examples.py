from pathlib import Path
from lxml import html,etree
import json,re
P=Path(__file__).parent;C=P/'seedmark'
for leaf in ['pricing','versus']:
 files=sorted((C/'elements'/leaf/'fixtures').glob('*.html'))
 if len(files)>=2:continue
 s=files[0].read_text();doc=html.fragment_fromstring(re.sub(r'^<!--.*?-->\s*','',s,count=1,flags=re.S))
 if leaf=='pricing':
  plans=doc.xpath('./*[contains(concat(" ",normalize-space(@class)," ")," plan ")]')
  if len(plans)>2:doc.remove(plans[-1])
  for j,n in enumerate(doc.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," name ")]')):
   if j<2:n.text=['직무별 승인 절차 설계','여러 법인을 잇는 통합 업무 관리'][j]
  minimum='8x5'
 else:
  for j,n in enumerate(doc.xpath('./*[contains(concat(" ",normalize-space(@class)," ")," side ")]')):
   n.set('class','side on'if j==0 else'side')
   name=n.xpath('./*[contains(concat(" ",normalize-space(@class)," ")," name ")]')
   if name:name[0].text=['한 번에 모아서 검토하는 방식','변경 건을 실시간으로 조율하는 방식'][j]
  minimum='10x5'
 (C/'elements'/leaf/'fixtures'/'extended-options.html').write_text(f'<!-- min: {minimum} -->\n'+etree.tostring(doc,encoding='unicode',method='html'))
a=json.loads((P/'map.json').read_text())
for i in a['instances']:
 if i['use'].startswith('variant:')and not i['use'].startswith('variant:.'):i['use']=i['use'].replace('variant:','variant:.',1)
(P/'map.json').write_text(json.dumps(a,ensure_ascii=False,indent=2))
