"""Exercise newly reconstructed structures without changing golden fixtures."""
from pathlib import Path
from lxml import html,etree
import re
P=Path(__file__).parent;E=P/'seedmark/elements'
def source(i,selector):
 d=html.parse(str(P/'reassembled'/f'slide_{i:02}.html'));xpath='//'+ '/'.join('*'+''.join('[contains(concat(" ",normalize-space(@class)," ")," '+c+' ")]'for c in part.split('.')[1:])for part in selector.split('>'));n=d.xpath(xpath)[0];s=etree.tostring(n,encoding='unicode',method='html')
 s=re.sub(r'grid-column:[^;\"]+;?grid-row:[^;\"]+;?', 'grid-column:1 / span 12;grid-row:1 / span 6;',s,count=1)
 return s
def put(folder,name,markup,minimum):
 if not re.search(r'^<[^>]*style=',markup):markup=markup.replace('>', ' style="grid-column:1 / span 12;grid-row:1 / span 6">',1)
 (E/folder/'fixtures'/f'{name}.html').write_text(f'<!-- min: {minimum} -->\n'+markup+'\n')
put('flowchart','system-cylinders',source(9,'.body>.stack'),'12x6')
put('flowchart','controller-gateway-devices',source(18,'.body>.flowchart'),'7x6')
put('timeline','photo-phases-5',source(17,'.body>.track'),'12x6')
put('steps','icon-cycle-5',source(11,'.body>.steps'),'12x3')
put('card','hanging-icon-3',source(5,'.body>.group'),'12x4')
put('pill','database-cylinders-3',source(9,'.flowchart>.node>.card.quiet'),'6x3')
put('chart-donut','pie-allocation',source(21,'.body>.group'),'12x6')
put('tag','milestone-label',source(14,'.body>.tag.line'),'1x3')
put('person','people-5-leader',source(19,'.body>.people'),'12x6')
put('card','revenue-plans-4',source(10,'.body>.group'),'12x5')
put('agenda','agenda-11',source(2,'.body>.agenda'),'8x5')
put('metric','allocation-details-2',source(21,'.body>.group>.stack'),'4x6')
put('prose','technology-heading',source(18,'.body>.prose.lead'),'5x2')
print('Added thirteen fidelity structure fixtures; golden fixtures unchanged.')
