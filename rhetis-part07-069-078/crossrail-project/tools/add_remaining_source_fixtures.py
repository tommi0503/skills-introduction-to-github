from pathlib import Path
from bs4 import BeautifulSoup as B
P=Path(__file__).parent;E=P/'crossrail/elements'
for el,n,name,w,h in [('pyramid',6,'pyramid-source-four',6,5),('funnel',8,'funnel-three-capsules',6,5),('table',4,'table-keyvalues-four',10,4),('table',15,'table-equipment-pairs',4,3),('table',16,'table-spec-pair',6,4),('table',20,'table-kpi-two',6,3),('table',30,'table-contact-five',6,3),('versus',19,'versus-annotated',12,6),('headline',23,'headline-icon-source',8,3),('list',8,'list-three-ruled-source',8,5),('card',5,'card-vision-source',12,6)]:
 s=B((P/f'reassembled/slide_{n:02}.html').read_text(),'html.parser');r=s.select_one(f'[data-el="crossrail-{el}"]')
 if name=='card-vision-source':r=s.select_one('.body>.group')
 st=';'.join(x for x in r.get('style','').split(';') if x and not x.startswith(('grid-column:','grid-row:')))
 if st:r['style']=st
 else:r.attrs.pop('style',None)
 (E/el/f'fixtures/{name}.html').write_text(f'<!-- min:{w}x{h} max:12x6 -->\n'+str(r)+'\n')
