from pathlib import Path
C=Path('/workspace/output/glasspulse')
for folder,root in [('flowchart','flowchart'),('swimlane','swimlane')]:
 p=C/f'elements/{folder}/element.css'
 r=f'.{root}[data-el="glasspulse-{folder}"]'
 none='color-mix(in srgb,var(--page) 0.001%,var(--page) 0%)'
 css=f'''\n/* Four independent edge layers preserve simultaneous branch directions. */
{r}>.node{{--glasspulse-clear:{none};--glasspulse-r:var(--glasspulse-clear);--glasspulse-d:var(--glasspulse-clear);--glasspulse-l:var(--glasspulse-clear);--glasspulse-u:var(--glasspulse-clear)}}
{r}>.node.to-r{{--glasspulse-r:var(--a1-7)}}{r}>.node.to-d{{--glasspulse-d:var(--a1-7)}}{r}>.node.to-l{{--glasspulse-l:var(--a1-7)}}{r}>.node.to-u{{--glasspulse-u:var(--a1-7)}}
{r}>.node:is(.to-r,.to-d,.to-l,.to-u)::after{{content:"";position:absolute;inset:calc(var(--gap)*-1);width:auto;height:auto;pointer-events:none;background:
conic-gradient(from 225deg at 100% 50%,var(--glasspulse-r) 0deg 90deg,var(--glasspulse-clear) 90deg 360deg) right center/10px 12px no-repeat,
conic-gradient(from 315deg at 50% 100%,var(--glasspulse-d) 0deg 90deg,var(--glasspulse-clear) 90deg 360deg) center bottom/12px 10px no-repeat,
conic-gradient(from 45deg at 0% 50%,var(--glasspulse-l) 0deg 90deg,var(--glasspulse-clear) 90deg 360deg) left center/10px 12px no-repeat,
conic-gradient(from 135deg at 50% 0%,var(--glasspulse-u) 0deg 90deg,var(--glasspulse-clear) 90deg 360deg) center top/12px 10px no-repeat,
linear-gradient(var(--glasspulse-r),var(--glasspulse-r)) right center/var(--gap) var(--stroke) no-repeat,
linear-gradient(var(--glasspulse-d),var(--glasspulse-d)) center bottom/var(--stroke) var(--gap) no-repeat,
linear-gradient(var(--glasspulse-l),var(--glasspulse-l)) left center/var(--gap) var(--stroke) no-repeat,
linear-gradient(var(--glasspulse-u),var(--glasspulse-u)) center top/var(--stroke) var(--gap) no-repeat}}
'''
 if folder=='swimlane':
  css+=f'''{r}{{grid-template-columns:repeat(var(--cols),minmax(0,1fr));padding-left:calc(160px + var(--gap)*2)}}{r}>.lane{{position:relative}}{r}>.lane>.name{{position:absolute;left:calc(-160px - var(--gap));width:160px;padding:var(--gap-sm)}}\n'''
 p.write_text(p.read_text()+css)
