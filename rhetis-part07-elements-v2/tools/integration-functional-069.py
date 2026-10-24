from pathlib import Path
import json,importlib.util,re
from PIL import Image,ImageDraw,ImageFont
R=Path('/workspace/work/rhetis-elements-v2'); O=R/'tools/integration-functional-069';O.mkdir(exist_ok=True)
spec=importlib.util.spec_from_file_location('sheets',R/'tools/sheets.py');s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
leaves='hub cycle hierarchy flowchart swimlane roadmap chart-stack chart-waterfall slope radar concentric venn sparkline'.split()
manifest=[]
for P in sorted(R.glob('*-project')):
 K=next(x for x in P.iterdir() if x.is_dir() and (x/'kit').exists()); k=K.name; rows=[]
 for leaf in leaves:
  d=json.loads((P/'sheets'/f'{leaf}-checks.json').read_text()); cells=d['modes']['light']; fs=list(dict.fromkeys(c['fixture'] for c in cells)); fn=next((x for x in fs if 'long' in x),fs[-1]); selected=[c for c in cells if c['fixture']==fn and(c['size']==[12,6] or c['isMin'])]
  selected=sorted(selected,key=lambda c:0 if c['size']==[12,6] else 1); imgs=[];paths=[]
  for c in selected:
   n=f"{leaf}--{Path(fn).stem}--light--{c['size'][0]}x{c['size'][1]}.png"; f=P/'sheet-cells'/n; imgs.append(Image.open(f).convert('RGB'));paths.append(str(f.relative_to(R)))
  H=max(i.height for i in imgs);W=sum(i.width for i in imgs)+24; row=Image.new('RGB',(W,H+56),'#eeeeee'); dr=ImageDraw.Draw(row);dr.text((8,8),f'{k} | {leaf} | {fn} | 12x6 LEFT / MIN RIGHT | fingerprint current={d["sourceFingerprint"]==s.fingerprint(P,k,leaf)}',fill='#111111'); x=0
  for im in imgs:row.paste(im,(x,56));x+=im.width+24
  rows.append(row)
  manifest.append({'collection':k,'leaf':leaf,'fixture':fn,'paths':paths,'fingerprint':d['sourceFingerprint'],'currentFingerprint':s.fingerprint(P,k,leaf),'generated':d['generatedAtUTC'],'sizes':[c['size'] for c in selected],'source':str((K/'elements'/leaf/'fixtures'/fn).relative_to(R))})
 for start in range(0,len(rows),3):
  group=rows[start:start+3]; out=Image.new('RGB',(max(i.width for i in group),sum(i.height for i in group)+24*(len(group)-1)),'#dddddd');y=0
  for im in group:out.paste(im,(0,y));y+=im.height+24
  out.save(O/f'{k}-{start//3+1}.png')
(O/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('selected',len(manifest),'native cells',sum(len(x['paths']) for x in manifest),'stale',[(x['collection'],x['leaf']) for x in manifest if x['fingerprint']!=x['currentFingerprint']])
