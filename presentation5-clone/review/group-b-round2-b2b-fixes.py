from pathlib import Path
import json,math
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
D=json.loads((ROOT/'src/decks/group-b-data.json').read_text());V='#7946fd';O='#ff4826';K='#070707';W='#fff'
for k,s in D.items():
 if not k.startswith('p101'):continue
 sid=k.split('/')[1]
 for e in s['elements']:
  t=e.get('text','')
  if t=='Section Infographic':
   if sid in ['s02-03','s02-06']:e['x']=7;e['w']=86
   e['runs']=[{'text':'Section ','color':K if sid=='s02-03' else V},{'text':'Infographic','color':V if sid=='s02-03' else K}]
  if t=='Performance and Progress\nAnalysis':e['runs']=[{'text':'Performance and Progress\n','color':K},{'text':'Analysis','color':V}]
  if sid=='s03-06' and t.startswith('A Glimpse'):e['runs']=[{'text':'A Glimpse into the Future of\n','color':V},{'text':'B2B Communication Through\n','color':K},{'text':'Our Pitch Mockups','color':V}]
  if sid=='s02-03' and e['kind']=='text' and e.get('x')==3:e['align']='right'
  if sid=='s02-06' and t in ['50%','60%','70%','80%']:e['y']+=8
  if sid=='s02-05' and e['kind']=='box' and e.get('fill') in [V,O,K]:e['radius']=0
  if sid=='s02-08' and e['kind']=='image':e['clipPath']='ellipse(50% 50% at 50% 50%)'
  if sid=='s02-08' and e['kind']=='path' and e.get('fill')=='#e5e5e5':
   xs=[q['x'] for q in e['points']];e['fill']='#191919' if min(xs)<35 else '#8b64fb' if min(xs)<67 else O;e['stroke']=e['fill']
  if sid=='s03-03' and e['kind']=='path' and e.get('fill')=='#e5e5e5':
   e['fill']='#191919' if min(q['x'] for q in e['points'])<80 else '#ff623f';e['stroke']=e['fill']
# The native chart has a 350 axis range; bar heights are values, not an illustration placeholder.
s=D['p101/s03-07']
for e in s['elements']:
 if e['kind']=='box' and e.get('w')==2.6 and e.get('fill') in [V,O,K]:e['h']*=1.2;e['y']=82-e['h']
s['elements'] += [tx('● Your Text 1     ● Your Text 2     ● Your Text 3',16,89,38,12,align='center')]
s=D['p101/s03-08'];s['elements'] += [tx('●  Speed       ●  Handling',17,92,35,15,align='center')]
for i in range(6):s['elements'] += [tx(str(i*20),11+i*9,83,6,12)]
for key,s in D.items():s['id']=key.split('/')[1]
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(D,ensure_ascii=False,separators=(',',':')))
