from pathlib import Path
import re
C=Path('/workspace/output/nightchamfer')
def append(n,s):
 p=C/'elements'/n/'element.css';p.write_text(p.read_text()+'\n'+s.replace('$',f'[data-el="nightchamfer-{n}"]')+'\n')
append('bullet','''$.bullets{grid-template-columns:minmax(0,1fr);align-content:stretch;justify-content:stretch}$.bullets>.bullet{width:100%;min-width:0}''')
append('slope','''$>.pair{padding:calc(var(--gap-sm)/2) 0}$>.pair>.name{font-size:var(--type-16)}$>.pair .a,$>.pair .b{font-size:var(--type-18)}''')
append('timeline','''$.col>.stop{padding-top:var(--gap-sm);padding-bottom:var(--gap-sm);gap:calc(var(--gap-sm)/2);justify-content:center}$.col>.stop .name{font-size:var(--type-18)}$.col>.stop .note{font-size:var(--type-14)}''')
append('waffle','''$ {grid-template-columns:minmax(0,3fr) minmax(0,2fr)}@container(max-width:350px){$>.fig{font-size:var(--type-24)}$>.name{font-size:var(--type-14)}$>.units{gap:2px}}''')
append('treemap','''@container(max-width:900px){$ .tile{flex-direction:column;justify-content:center;text-align:center}$ .tile .name{font-size:var(--type-14)}$ .tile .fig{font-size:var(--type-18)}}''')
append('prose','''$.cols p{break-inside:auto}@container(max-height:320px){$.cols p{font-size:var(--type-16)}}''')
# Explicitly document practical lower limits of multi-member variants.
changes={'bullet/bullets-4.html':'6x4','waffle/waffle-figures.html':'6x2','delta/delta.html':'4x2','delta/delta-big.html':'4x2','tag/tag-hl.html':'4x2','tag/tag-hl-extended.html':'4x2'}
for file,size in changes.items():
 folder,name=file.split('/');p=C/'elements'/folder/'fixtures'/name
 if p.exists():p.write_text(re.sub(r'<!-- min:.*?-->','<!-- min: '+size+' -->',p.read_text(),count=1))
