from pathlib import Path
from lxml import html
import json,re,hashlib
P=Path(__file__).parent;M=json.loads((P/'map.json').read_text());I=json.loads((P/'original-assembly-identities.json').read_text());N=lambda t:re.sub(r'\s+','',t)
rows=[];miss=[];covered=0
for n in range(1,31):
 d=html.fromstring((P/'reassembled'/f'slide_{n:02}.html').read_text()); roots=d.xpath('//div[@class="body"]/*[@data-el]');ids=I[str(n)];assert len(roots)==len(ids),(n,len(roots),len(ids))
 for e,id in zip(roots,ids):
  i=next(q for q in M['instances'] if q['id']==id);tx=N(e.text_content())
  for s in i.get('sourceMeasurements',[]):
   st=N(s.get('text',''))
   if not st:continue
   expected=st
   if i['leaf'] in ['prose','list','versus']:expected=expected.lstrip('•·●')
   # Original source funnel keeps its label/value in separate semantic fields and list bullets are CSS markers.
   if i['leaf'] in ['funnel']:expected=expected.replace('STEP','')
   present=expected in tx
   generated_axis=(n==20 and s['id'] in ['source-27','source-29','source-31','source-33']) or (n==22 and s['id'] in ['source-41','source-42','source-43','source-44'])
   if generated_axis:
    maximum=float(re.search(r'--max:([\d.]+)',e.get('style',''))[1]);ticks=[maximum*k/3 for k in range(4)];present=any(abs(float(st.replace(',',''))-v)<.005 for v in ticks)
   rows.append({'page':n,'mapId':id,'sourceNodeId':s['id'],'original':st,'present':present,**({'renderedBy':'CSS counter rail','derivedFrom':'--max','ticks':ticks} if generated_axis else {})})
   if present:covered+=1
   else:miss.append(rows[-1])
# Header source furniture and cover lockup text is checked independently.
head=[]
for n in range(1,31):
 tx=N(html.fromstring((P/'reassembled'/f'slide_{n:02}.html').read_text()).text_content())
 for i in M['instances']:
  if i['page']!=n or i['use']!='furniture':continue
  for s in i.get('sourceMeasurements',[]):
   st=N(s.get('text',''))
   if st and i.get('leaf')=='foundation':head.append({'page':n,'id':s['id'],'text':st,'present':st in tx})
report={'bodyRecords':len(rows),'bodyPresent':covered,'bodyMissing':miss,'headerRecords':head,'bodyDetails':rows,'note':'Only supported mapped roots are checked. GAPS.md contains omitted unsupported original regions. Whitespace and CSS bullet glyphs are normalized, original copy is never replaced with fixture text.'}
(P/'original-text-coverage.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('body',len(rows),'present',covered,'missing',len(miss));print(miss);print('headers missing',[x for x in head if not x['present']])
