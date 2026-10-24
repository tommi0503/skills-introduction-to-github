from pathlib import Path
import math
B=Path('/workspace/work/rebuild-20261024')
for n in ['afterglow','confluence']:
 p=B/n/'collection'/n/'elements/logo-group/element.css';s=p.read_text();root=f'.logos[data-el="{n}-logo-group"]'
 s=s.replace('display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:var(--gap);padding:var(--gap);','--logo-cols:6;--logo-rows:1;display:grid;grid-template-columns:repeat(var(--logo-cols),minmax(0,1fr));grid-template-rows:repeat(var(--logo-rows),minmax(0,1fr));place-items:center;gap:var(--gap);padding:var(--gap);')
 s=s.replace('flex:1 1 15%;max-width:23%;max-height:90%;aspect-ratio:1;','width:min(100%,calc((100cqh - (var(--logo-rows) + 1)*var(--gap))/var(--logo-rows)));height:auto;max-width:100%;max-height:100%;min-width:0;min-height:0;aspect-ratio:1;')
 for k in range(1,13):s+=root+':has(>.seat:nth-child('+str(k)+'):last-child){--logo-cols:'+str(k if k<=6 else math.ceil(k/2))+';--logo-rows:'+str(1 if k<=6 else 2)+';}\n'
 s=s.replace(':not(.square)>.seat','>.seat');p.write_text(s)
for p in (B/'nocturne/collection/nocturne/elements/pricing/fixtures').glob('*.html'):p.write_text(p.read_text().replace('<small>/월</small>','<small>원/월</small>'))
