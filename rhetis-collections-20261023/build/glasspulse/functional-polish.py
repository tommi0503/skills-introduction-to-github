from pathlib import Path
E=Path('/workspace/output/glasspulse/elements')
p=E/'sparkline/element.css';s=p.read_text().replace('calc(100cqh - var(--gap-sm)*2)','100cqh');s+='\n@container (max-width:600px){.spark[data-el="glasspulse-sparkline"].bars{gap:var(--stroke)}.spark[data-el="glasspulse-sparkline"]{--glasspulse-spark-stroke:var(--stroke)}}\n';p.write_text(s)
p=E/'slope/element.css';p.write_text(p.read_text()+'\n@container (max-width:600px){.slope[data-el="glasspulse-slope"] :is(.name,.a,.b){font-size:var(--type-16)}}\n')
p=E/'chart-area/element.css';s=p.read_text();old='.areas[data-el="glasspulse-chart-area"]:has(.series>.name)';src='.areas[data-el="glasspulse-chart-area"]:has(>.series>.pt:nth-child(5 of .pt):last-child):not(:has(>.series:nth-child(2 of .series))):not(:has(>.series>.pt>b))';s=s.replace(old,src)
# Canonical named series: use each plot as its own size container, preserving source-deck panels.
can='.areas[data-el="glasspulse-chart-area"]:has(>.series>.name):not(:has(>.series>.pt:nth-child(5 of .pt):last-child))'
s+=f'''\n{can}>.series{{container-type:size;top:calc(var(--gap)*2);bottom:var(--gap-lg);--glasspulse-h:100cqh}}{can} .pt{{width:0;height:0;transform:none;background:none;box-shadow:0 0 0 var(--stroke) currentColor;--glasspulse-h:100cqh}}{can} .series>.name{{top:calc(var(--gap)*-1.5);font-size:var(--type-16)}}\n''';p.write_text(s)
p=E/'bullet/element.css';s=p.read_text();s+='''\n.bullet[data-el="glasspulse-bullet"]::after{background:linear-gradient(90deg,color-mix(in srgb,var(--page) 0.001%,var(--ink) 0%) calc(clamp(0,var(--target),100)*1% - var(--stroke)),var(--ink) 0 calc(clamp(0,var(--target),100)*1% + var(--stroke)),color-mix(in srgb,var(--page) 0.001%,var(--ink) 0%) 0),linear-gradient(90deg,var(--a1) calc(clamp(0,var(--v),100)*1%),color-mix(in srgb,var(--page) 0.001%,var(--ink) 0%) 0) left center/100% 6px no-repeat,linear-gradient(90deg,var(--n-4) calc(var(--low,50)*1%),var(--n-3) 0 calc(var(--high,80)*1%),var(--n-2) 0);border-radius:var(--radius-sm)}\n''';p.write_text(s)
p=E/'treemap/element.css';s=p.read_text()+'''\n.treemap[data-el="glasspulse-treemap"]>.branch{container-type:inline-size}.treemap[data-el="glasspulse-treemap"] .tile{text-align:center;padding:min(var(--gap-sm),8cqw)}.treemap[data-el="glasspulse-treemap"] .tile .name{font-size:clamp(var(--type-14),18cqw,var(--type-24));overflow-wrap:anywhere}.treemap[data-el="glasspulse-treemap"] .tile .fig{font-size:clamp(var(--type-16),24cqw,var(--type-32))}\n''';p.write_text(s)
p=E/'radar/element.css';s=p.read_text().replace('min(70cqw,70cqh)','min(64cqw,64cqh)');s+='''\n.radar[data-el="glasspulse-radar"] .series .name{top:calc(100% + var(--gap-sm));left:0;right:0;text-align:center}.radar[data-el="glasspulse-radar"] .series:nth-child(2 of .series) .name{left:0;top:calc(100% + var(--gap-sm) + var(--gap))}.radar[data-el="glasspulse-radar"] .series:nth-child(3 of .series) .name{left:0;top:calc(100% + var(--gap-sm) + var(--gap)*2)}\n''';p.write_text(s)
p=E/'balance/element.css';s=p.read_text()+'''\n.balance[data-el="glasspulse-balance"] .pan{position:relative}.balance[data-el="glasspulse-balance"] .pan:first-child{transform:translateY(calc(tan(var(--tilt)*.08deg)*-38cqw))}.balance[data-el="glasspulse-balance"] .pan:last-child{transform:translateY(calc(tan(var(--tilt)*.08deg)*38cqw))}.balance[data-el="glasspulse-balance"] .pan::before{content:'';position:absolute;left:50%;bottom:100%;height:var(--gap);border-left:var(--stroke) solid var(--n-4)}\n''';p.write_text(s)
# Distinguish series in existing noncanonical stack fixtures; keep fixture count stable.
import re
for p in (E/'chart-stack/fixtures').glob('*.html'):
 s=p.read_text();s=re.sub(r'(<div class="sbar[^"]*">)(.*?)(</div>\s*(?=<div class="sbar|\n</div>|</div>))',lambda m:m.group(0),s,flags=re.S)
 # reset tone index at every category label
 chunks=re.split(r'(<div class="sbar[^>]*>)',s)
 for i in range(2,len(chunks),2):
  n=[0]
  def tone(m):n[0]+=1;return 'class="seg tone-'+str(n[0])+'"'
  chunks[i]=re.sub(r'class="seg"',tone,chunks[i])
 s=''.join(chunks)
 if 'stack12' in p.name:
  s=s.replace('class="stacks"','class="stacks h pct"').replace('--max:150','--max:100')
  # normalize each two-part series to a total of100
  def vals(m):
   a,b=int(m.group(1)),int(m.group(2));x=round(a/(a+b)*100);return f'--v:{x}"><b>{x}%</b></div><div class="seg tone-2" style="--v:{100-x}"><b>{100-x}%'
  s=re.sub(r'--v:(\d+)"><b>\d+</b></div><div class="seg tone-2" style="--v:(\d+)"><b>\d+',vals,s)
 p.write_text(s)
