from pathlib import Path
import re
C=Path('/workspace/work/deliverables/undertow');S=Path('/workspace/work/agents/031')
MARK='/* UNDERTOW PRECISE COMPOSITIONS */'
def patch(f,func):
 p=C/'elements'/f/'element.css';s=p.read_text();a,sep,b=s.partition(MARK);p.write_text(a+sep+func(b))
patch('architecture',lambda b:b.replace('.arch[data-el="undertow-architecture"]','.arch[data-el="undertow-architecture"]:not(:has(>.layer>.chip:nth-child(3)))'))
patch('chart-bar',lambda b:b.replace('.bars[data-el="undertow-chart-bar"]:not(.h)','.bars[data-el="undertow-chart-bar"]:not(.h):has(>.bar:nth-child(4)):not(:has(>.bar:nth-child(5)))'))
patch('headline',lambda b:b.replace('.big:has(>.kick)','.big:has(>.kick):not(:has(>.note))').replace('.big:has(>.note)','.big:has(>.note):not(:has(>.kick))'))
patch('hub',lambda b:b.replace('.hub[data-el="undertow-hub"]:has(>.spoke:nth-child(5)):not(:has(>.spoke:nth-child(6)))','.hub[data-el="undertow-hub"]:has(>.spoke:nth-child(5)):not(:has(>.spoke:nth-child(6))):not(:has(>.spoke>.mark))'))
patch('list',lambda b:b.replace('.list[data-el="undertow-list"].divided:has(>.item>.note)','.list[data-el="undertow-list"].divided:has(>.item>b.name):has(>.item>.note)').replace('.list[data-el="undertow-list"].check','.list[data-el="undertow-list"].check:has(>.item>b.name)'))
patch('person',lambda b:b.replace('.people[data-el="undertow-person"]:has(>.person:nth-child(4)):not(:has(>.person:nth-child(5)))','.people[data-el="undertow-person"]:has(>.person:nth-child(4)):not(:has(>.person:nth-child(5))):has(>.person>.note>strong)'))
patch('prose',lambda b:b.replace('.prose[data-el="undertow-prose"].quiet','.prose[data-el="undertow-prose"].quiet:has(>p>span)'))
patch('steps',lambda b:b.replace('.steps[data-el="undertow-steps"]:not(.col):has(>.step:nth-child(3)):not(:has(>.step:nth-child(4)))','.steps[data-el="undertow-steps"]:not(.col):has(>.step:nth-child(3)):not(:has(>.step:nth-child(4))):has(>.step.on)'))
p=C/'elements/callout/element.css';p.write_text(p.read_text()+'\n.callout[data-el="undertow-callout"]:not(:has(.icon)) {width:100%;}\n')
p=C/'elements/agenda/element.css';p.write_text(p.read_text()+'\n.agenda[data-el="undertow-agenda"] {padding:0;}\n')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''
.slide:has(>.page>.top) .body:has(>[data-el="undertow-agenda"]) {grid-template-columns:repeat(6,100.3333px) 101px repeat(4,119.75px) 98px;grid-template-rows:213px repeat(4,66px) 243px;}
.slide.cover .lockup .title b {color:var(--a1-8);}
''')
p=C/'elements/headline/element.css';p.write_text(p.read_text()+'\n.headline[data-el="undertow-headline"].big:has(>.kick):not(:has(>.note)) h2 b {color:var(--a1-8);}\n')
p=S/'precision-pages.py';s=p.read_text();s=s.replace('(7,6,1,6))+end()', '(8,4,2,5))+end()')
s=s.replace("+';'.join('--type-'", "+';'.join('--type-'") # no-op; append host color supply below
s=s.replace("(P/'collection-preview.css').write_text(css)","(P/'collection-preview.css').write_text(css+'\\n.slide.cover,.slide:has(.agenda){--a1-8:#9bffd4;}')")
p.write_text(s)
print('contract-part regression scoping complete')
