from pathlib import Path
import re
C=Path('/workspace/output/nightchamfer')
def append(n,s):
 p=C/'elements'/n/'element.css';p.write_text(p.read_text()+'\n'+s.replace('$',f'[data-el="nightchamfer-{n}"]')+'\n')
append('card','''$ .parts>.name{font-size:var(--type-24);background:var(--n-2);border-radius:var(--radius-sm);padding:calc(var(--gap-sm)/2) var(--gap-sm);align-items:center;line-height:var(--name-line);min-height:calc(2em * var(--name-line));max-width:100%}$ .parts>.note{font-size:var(--type-18);line-height:var(--body-line)}$ .parts>.note .seat{margin:var(--gap-sm) auto;width:100px;height:100px}$.on .parts>.name{background:var(--a1);color:var(--a1-on)}@container(max-width:400px){$ .parts>.name{font-size:var(--type-20)}$ .parts>.note{font-size:var(--type-16)}}@container(max-height:230px){$ .parts>.name{font-size:var(--type-16);min-height:0}$ .parts>.note{font-size:var(--type-12)}}''')
append('hierarchy','''$>.root{width:min(16%,34cqh);height:auto;aspect-ratio:1;max-height:none;left:50%;transform:translateX(-50%)}''')
append('delta','''$ .from,$ .to{display:flex;align-items:center;justify-content:center;text-align:center;width:28%;max-height:90%;aspect-ratio:1;border-radius:50%;border:18px solid var(--n-3);background:var(--n-2);font-size:var(--type-36);padding:var(--gap-sm)}$ .to{background:var(--a1);border-color:var(--a1-2-muted);color:var(--a1-on)}@container(max-width:650px){$ .from,$ .to{font-size:var(--type-24);border-width:10px}}@container(max-height:180px){$ .from,$ .to{border-width:6px;font-size:var(--type-20);width:auto;min-width:25%;aspect-ratio:auto;max-height:100%}}''')
# Distinct rising schedule motif from slide 12; small cells keep a level timeline.
append('timeline','''@container(min-height:380px){$:not(.col):not(.alt)>.stop{justify-content:flex-start;padding-top:var(--gap-lg);height:60%;align-self:flex-end}$:not(.col):not(.alt)>.stop:nth-child(2){height:73%}$:not(.col):not(.alt)>.stop:nth-child(3){height:86%}$:not(.col):not(.alt)>.stop:nth-child(4){height:100%}$:not(.col):not(.alt)>.stop::before{width:44px;height:44px;left:calc(var(--gap-sm)*-1);top:0;background:var(--a1);border:7px solid var(--a1-2-muted)}$:not(.col):not(.alt)>.stop::after{top:22px}$:not(.col):not(.alt)>.stop>.kick{position:relative;z-index:3;color:var(--a1-on);font-size:var(--type-14);margin-top:calc(var(--gap-lg)*-1 + var(--gap-sm));margin-bottom:var(--gap)}}''')
p=C/'foundation/foundation.css';p.write_text(p.read_text()+'''\n.page{padding-top:calc(var(--margin-y) + var(--gap) + var(--gap-sm))}.lockup.at-top-left{top:calc(var(--margin-y)*2 + var(--gap-lg))}.slide.cover .lockup .lead{font-weight:var(--title-weight);font-size:var(--type-48)}\n''')
for p in C.rglob('*.css'):
 s=p.read_text()
 for n in range(1,5):s=re.sub(r'(?<![-\w])color:\s*var\(--a'+str(n)+r'\)',f'color:var(--a{n}-7)',s)
 p.write_text(s)
# Source palette is data: use the original cool neutral ramp, never hard-code it into element styles.
p=Path('/workspace/work/nightchamfer/reassemble.py');s=p.read_text().replace("PAL=';'.join",'''pal.update({f'--n-{i}':v for i,v in enumerate(['#111111','#222222','#333333','#606060','#888888','#AAAAAA','#CCCCCC','#DDDDDD','#FFFFFF'],1)})
for i,v in enumerate(['#07111E','#0C1B37','#143263','#194786','#2057A9','#276BCD','#3982FB','#6CA5FF','#AFCEFF'],1):
 for suf in ['', '-soft','-muted']:pal[f'--a1-{i}{suf}']=v
PAL=';'.join''');p.write_text(s)
