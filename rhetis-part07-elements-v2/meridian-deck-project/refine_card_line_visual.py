from pathlib import Path
P=Path(__file__).parent;C=P/'meridian-deck'
f=C/'elements/card/element.css';s=f.read_text();s+='''
.card[data-el="meridian-deck-card"].on:not(:has(>.parts>.mark))>.parts>.note{font-size:clamp(var(--type-12),min(5cqw,5cqh),var(--type-16))}.card[data-el="meridian-deck-card"].on>.parts:has(>.fig)>.note{font-size:clamp(var(--type-12),4cqw,var(--type-14))}.card[data-el="meridian-deck-card"]>.parts>[data-el]{height:31%}
''';f.write_text(s)
f=C/'elements/chart-line/element.css';s=f.read_text().replace('padding:var(--gap) var(--gap-sm)','padding:var(--gap-lg) var(--gap-sm) var(--gap)').replace('height:calc(100% - var(--v)/var(--max,100)*(100% - var(--gap-lg)))','height:calc(100%*(1 - var(--v)/var(--max,100)))').replace('margin-top:var(--gap-sm);z-index:2','margin-top:var(--gap-sm);margin-bottom:calc(var(--stroke)*-4);z-index:2');s+='\n.lines[data-el="meridian-deck-chart-line"]:has(>.pt>b:empty):not(:has(>.pt>b:not(:empty))){padding:0 var(--gap-sm)}\n';f.write_text(s)
# Optional source value labels were absent; keep b as the chart anchor, not as invented copy.
for f in [C/'elements/chart-line/fixtures/replica-17.html',C/'elements/card/fixtures/replica-17.html']:
 s=f.read_text()
 import re
 values=[[20,35,61],[25,65,80],[30,36,69]];idx=[0]
 def plot(m):
  v=values[idx[0]%3];idx[0]+=1;return m[0].replace('--max:100','--max:'+str(max(v)*1.25),1)
 s=re.sub(r'<div class="lines"[^>]*>',plot,s);s=re.sub(r'(<div class="pt"[^>]*>)<b>\d+</b>',r'\1<b></b>',s);f.write_text(s)
print('Visual correction: circular notes contained and source trends use the measured full plot range')
