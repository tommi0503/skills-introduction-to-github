from pathlib import Path
import re
P=Path(__file__).parent;C=P/'meridian-deck';E=C/'elements'
for folder in E.iterdir():
 p=folder/'element.css';s=p.read_text();e=folder.name;r=f'[data-el="meridian-deck-{e}"]'
 # Change text foreground roles only; series' currentColor still defines its own ranked fill.
 if e!='chart-area':s=re.sub(r'(?<![-\w])color:var\(--a1\)(?=[;}])','color:var(--a1-7)',s)
 s=re.sub(r'(?<![-\w])color:var\(--n-6\)(?=[;}])','color:var(--n-7)',s)
 s+=f'\n{r} small{{color:inherit;margin:0}}\n'
 if e=='chart-bar':s+=f'{r} .bar>b,{r} .bar>span{{background:var(--page);color:var(--ink)}}'
 if e=='chart-area':
  s+=f'{r} .series>.name,{r} .pt>b{{color:var(--a1-7)}}'
  for n in range(2,5):s+=f'{r} .series:nth-of-type({n})>.name,{r} .series:nth-of-type({n})>.pt>b{{color:var(--a{n}-7)}}'
 if e in ['hierarchy','timeline','concentric','positioning']:
  s=s.replace('background:var(--n-6);color:var(--page)','background:var(--n-7);color:var(--page)')
 if e=='code':s=re.sub(r'(?<![-\w])color:var\(--a([23])\)(?=[;}])',r'color:var(--a\1-7)',s)
 p.write_text(s)
f=C/'foundation/foundation.css';s=re.sub(r'(?<![-\w])color:var\(--a1\)(?=[;}])','color:var(--a1-7)',f.read_text());f.write_text(s)
f=P/'build_reassembled.py';s=f.read_text().replace("(A/'source-palette.css').write_text", "light['--a1-7']='#0063ed'\n(A/'source-palette.css').write_text");f.write_text(s)
print('Accessible text roles and units applied')
