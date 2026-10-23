from pathlib import Path
import re
C=Path('/workspace/output/cyanloop');R=Path('/workspace/output/cyanloop-review')
for n,name in [(11,'process-connected-discs'),(13,'leadership-semicircle')]:
 s=(R/'reassembled'/f'slide_{n:02}.html').read_text();r=re.search(r'<div class="body">(.*)</div></div></section>',s).group(1);(C/'elements/hub/fixtures'/f'{name}.html').write_text('<!-- min: 12x6 -->\n'+str(r)+'\n')
p=C/'elements/hub/element.css';s=p.read_text()
for i,a in enumerate([14.5,42.3,75,105,137.7,165.5],2):s+=f'\n.hub[data-el="cyanloop-hub"].on .spoke:nth-child({i})::before{{left:calc(50% + cos({a}deg) * 50%);top:calc(50% + sin({a}deg) * 50%);}}'
p.write_text(s)
