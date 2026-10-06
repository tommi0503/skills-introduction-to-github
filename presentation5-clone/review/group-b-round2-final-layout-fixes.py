import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'src/decks/group-b-data.json';d=json.loads(p.read_text())
for k,s in d.items():
 for e in s['elements']:
  if 'leading' in e:e['lineHeight']=e.pop('leading')
  if 'stroke' in e:
   stroke=e.pop('stroke')
   if e['kind']=='path':e['color']=stroke
   elif e['kind']=='box':e['border']=f"{e.get('strokeWidth',1)}px solid {stroke}"
  e.pop('italic',None)
  if k=='p080/s02-06' and e['kind']=='image' and e.get('alt')=='Social brand icon placeholder':e.update(x=45,y=83,w=3,h=5);e.pop('alt',None)
  if k=='p104/s02-01' and e.get('text')=='Themed packs to increase':e['text']='Themed packs to increase\naverage order value';e['y']=78
  if k in ['p104/s02-03','p104/s03-04','p104/s03-06'] and e['kind']=='text' and e.get('font')=='Anton' and '\n' in e.get('text',''):e['lineHeight']=1.24;e['y']+=1.5
  if k=='p104/s02-03' and e['kind']=='box' and e.get('fill') in ['#d49afa','#bce6ed','#ecffa6']:
   e['radius']='22px 0 0 22px' if e['x']==6 else '0 22px 22px 0' if e['x']==65 else 0
  if k=='p104/s03-05' and e['kind']=='box' and e.get('radius')=='50%':e['fill']='#ef6b62'
  if k=='p107/s05-03' and e.get('text')=='BRAND CULTURE':e['y']=78;e['size']=46
  if k=='p107/s05-08':
   if e['kind']=='box' and e.get('fill')=='#f3eee5':e['y']-=5
   if e['kind']=='image' and e['x']==51:e['h']-=5
   if e['kind']=='text' and (e.get('text')=='BRAND VALUES' or e.get('text','').startswith('Excellence Becomes')):e['y']-=5
  if k=='p107/s05-05' and e['kind']=='text' and e.get('text','').startswith('Lorem'):e['align']='center';e['text']='Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nSed do eiusmod tempor\nincididunt ut labore et dolore\nmagna aliqua. Ut enim ad\nminim veniam.'
  if k=='p107/s05-06' and e['kind']=='text' and e.get('text','').startswith('Lorem'):
   e['align']='center'
   if e['y']<30:e['text']='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
  if k=='p107/s02-01' and e['kind']=='text' and e.get('text','').startswith('Lorem'):e['text']='Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nSed do eiusmod tempor incididunt ut labore et dolore\nmagna aliqua. Ut enim ad minim veniam, quis nostrud\nexercitation ullamco laboris nisi ut aliquip.'
# Restore narrower final market circle and aligned descriptions.
s=d['p104/s03-04'];
for e in s['elements']:
 if e['kind']=='box' and e.get('fill')=='#ecffa6':e.update(x=69,y=63,w=22,h=39.11)
 if e['kind']=='text' and e['x']>=68 and e['y']>=73:e['y']-=2;e['w']=20
# Remove obsolete prose duplicated by the source marketing block.
for k,s in d.items():
 if k.startswith('p092/') and any(e.get('text')=='Marketing' for e in s['elements']):
  s['elements']=[e for e in s['elements'] if not(e['kind']=='text' and e.get('text','').startswith('Lorem') and e['x']<=3 and e['y']==56)]
p.write_text(json.dumps(d))
