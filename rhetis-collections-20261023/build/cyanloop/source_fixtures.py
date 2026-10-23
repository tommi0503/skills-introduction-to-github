from pathlib import Path
import runpy,re
W=Path('/workspace/work/cyanloop');C=Path('/workspace/output/cyanloop');R=Path('/workspace/output/cyanloop-review')
p=W/'reassembly.py';s=p.read_text();s=s.replace("+b+'</div></div>' for i,(a,b)", "+listel([(v,'') for v in b.split('<br>')])+'</div></div>' for i,(a,b)");p.write_text(s)
for stale in C.glob('elements/*/fixtures/source-*.html'):stale.unlink()
ns=runpy.run_path(str(p));P=ns['P']
def chunks(s):
 out=[];dep=0;start=0
 for m in re.finditer(r'<(/?)div\b[^>]*>',s):
  if not m.group(1):
   if dep==0:start=m.start()
   dep+=1
  else:
   dep-=1
   if dep==0:out.append(s[start:m.end()])
 return out
mapping={2:['agenda'],3:['prose','agenda'],4:['prose','image-frame','chart-bar','chart-line','legend'],5:['callout','card'],7:['card','card','card','card','callout'],8:['pyramid','prose','callout'],9:['hub'],10:['timeline','image-frame'],12:['image-frame','hub'],14:['table'],15:['person'],16:['metric','prose','list','card','card','card','card','card','card'],17:['roadmap']}
for n,folders in mapping.items():
 for i,(part,folder) in enumerate(zip(chunks(P[n]),folders)):
  part=re.sub(r'style="grid-column:[^"]*?grid-row:[^";]*(;[^\"]*)?"',lambda m: 'style="grid-column:1 / span 12; grid-row:1 / span 6'+(m.group(1) or '')+'"',part,count=1)
  (C/'elements'/folder/'fixtures'/f'source-{n:02}-{i+1}.html').write_text('<!-- min: 12x6 -->\n'+part+'\n')
for n in [1,2,3,18]:
 s=(R/'reassembled'/f'slide_{n:02}.html').read_text();body=re.search(r'<section.*?</section>',s).group()
 (C/'foundation/fixtures'/f'source-{n:02}.html').write_text('<!-- min: 12x6 -->\n'+body+'\n')
p=C/'elements/prose/element.css';p.write_text(p.read_text()+'''\n.prose[data-el="cyanloop-prose"].on{background:var(--a1-7);color:var(--page);}@container(min-height:200px){.prose[data-el="cyanloop-prose"].on{justify-content:center;}}\n''')
