from pathlib import Path
from lxml import html as L
P=Path(__file__).parent;p=P/'write_replica_fixtures.py';s=p.read_text();s=s.replace("else '<br>' if c.tag=='br'", "else '<u>'+val+'</u>' if c.tag=='u' else '<br>' if c.tag=='br'");p.write_text(s)
for leaf,num in [('timeline',23),('table',17)]:
 p=P/'meridian-deck/elements'/leaf/'fixtures'/f'replica-{num}.html';s=p.read_text();prefix=s.split('-->',1)[0]+'-->';t=L.fragment_fromstring(s,create_parent='div')
 nodes=t.xpath('.//div[@class="kick"]') if leaf=='timeline' else t.xpath('.//th')[1:]
 for e in nodes:
  if e.text and e.text.strip():
   b=L.Element('u');b.text=e.text;e.text=None;e.insert(0,b)
 p.write_text(prefix+'\n'+''.join(L.tostring(x,encoding='unicode') for x in t if not isinstance(x,L.HtmlComment))+'\n')
