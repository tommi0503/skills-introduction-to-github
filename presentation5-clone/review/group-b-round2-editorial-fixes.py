from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
D=json.loads((ROOT/'src/decks/group-b-data.json').read_text());W='#fff';B='#645740';K='#383838'
def page(s):return D['p080/'+s]
def add(s,els):page(s)['elements']+=els
for key,s in D.items():
 if not key.startswith('p080'):continue
 es=s['elements'];s['elements']=[e for e in es if e['kind'] in ['box','path','circle']]+[e for e in es if e['kind']=='image']+[e for e in es if e['kind'] not in ['box','path','circle','image']]
 for e in s['elements']:
  t=e.get('text','')
  if t.startswith('SELECTEDWORK') or t.startswith('GOOD IDEA'):e['weight']=600
s=page('s02-01')
for e in s['elements']:
 if e['kind']=='image':e['y']=47
 if e['kind']=='text' and e.get('x',0)>=49 and e.get('y',0)>25:e['x']-=6;e['w']=min(e['w'],100-e['x']-2)
add('s02-01',[para(49,86,18,13,W,3),para(78,86,18,13,W,3)])
# The original package numbers are outlined capsules/circles.
for x,y,t in [(5,45,'01'),(33,45,'02'),(5,80,'03')]:add('s02-02',[{**box(x,y,7,7,'transparent','50%'),'border':'1px solid #666'}])
# Every original photograph is its own placeholder; keep their collage boundary.
s=page('s03-04');s['elements']=[e for e in s['elements'] if e['kind']!='image'];s['elements'][1:1]=[photo(51,33,23,63),photo(74,33,24,32),photo(74,65,13,31),photo(87,65,11,17)]
for sid in ['s03-02','s08-02']:
 s=page(sid);s['elements']=[e for e in s['elements'] if not(e.get('text','').startswith('Lorem') and e.get('x',0)<30)]
s=page('s03-05')
for e in s['elements']:
 if e.get('text')=='Valerie\nWarrington':e.update(x=45,y=42,w=15,size=25,align='right')
 if e.get('text')=='Subtitle_':e.update(x=63,y=42)
 if e.get('text','').startswith('SELECTEDWORK'):e.update(x=63,y=49,w=30)
s=page('s03-06')
for e in s['elements']:
 if e['kind']=='text' and e.get('x',0)>=78 and e.get('y',0)>12:e['x']-=4;e['w']=min(e.get('w',20),96-e['x'])
s=page('s03-07')
for e in s['elements']:
 if e.get('text','').startswith('Sales Associate'):e['y']=54
 if e.get('text','').startswith('Bachelor'):e['y']=82
 if e.get('text','').startswith('Lorem') and e.get('y',0)>40:e['y']+=4
s=page('s03-08')
for e in s['elements']:
 if e['kind']=='text' and e.get('text','').startswith('SELECTEDWORK'):e['y']=40
 if e['kind']=='text' and e.get('text','').startswith('THERE ARE'):e['y']=53;e['w']=31
 if e['kind']=='text' and e.get('text')=='Virginia Kelly':e['y']=64
for sid in ['s06-01','s06-02','s08-01']:
 for e in page(sid)['elements']:
  if e.get('text')=='Template':e['color']='#cf873b';e['x']=72;e['y']=47
  if e.get('text')=='Design\nPortfolio':e['size']=86;e['w']=57
  if e.get('text','').startswith('“we are'):e['x']=24;e['w']=12
s=page('s06-03')
for e in s['elements']:
 if e['kind']=='image':e.update(x=64,y=21,w=28,h=49,clipPath='ellipse(50% 50% at 50% 50%)')
 if e['kind']=='text' and e.get('x')==4 and e.get('y',0)>40:e['x']=13
s=page('s06-04');s['elements']=[e for e in s['elements'] if not(e.get('text','').startswith('Lorem'))]
s['elements'] += [para(45,49,46,13,W,4),para(45,62,46,13,W,3),para(45,77,46,13,W,3)]
s=page('s06-06');s['elements']=[e for e in s['elements'] if not(e.get('text')=='Virginia Kelly' and e.get('font')=='Kaushan Script') and not(e.get('text','').startswith('Lorem') and e.get('x',0)<35)]
for e in s['elements']:
 if e.get('text','').startswith('SELECTEDWORK'):e['y']=47
 if e.get('text','').startswith('THERE ARE'):e['y']=61
s=page('s06-07')
for e in s['elements']:
 if e['kind']=='text' and e.get('x')==4 and e.get('y',0)>40:e['x']=13
s=page('s06-08');found=False;els=[]
for e in s['elements']:
 if e.get('text','').startswith('Lorem'):
  if found:continue
  found=True;e.update(x=56,y=65,w=37)
 els.append(e)
s['elements']=els
# Match the original modest outlined buttons and actual simple star symbols.
for sid in ['s02-03','s02-05','s03-02','s03-03','s03-06','s03-09','s06-03','s06-05','s06-06','s06-07','s06-09','s08-02','s08-03','s08-04']:
 s=page(sid);txt=next((e for e in s['elements'] if e.get('text','').startswith('SELECTEDWORK')),None)
 if txt:s['elements'] += [ic(txt['x'],txt['y']-7,2.2,4,'Star',B,1),ic(txt['x']+3.2,txt['y']-7,2.2,4,'Star',B,1)]
for sid in ['s03-03','s08-03']:
 s=page(sid)
 for e in s['elements']:
  if e.get('text') in ['01','02']:e['y']=72
 s['elements'] += [{**box(x,70,10,9,'transparent','50%'),'border':'1px solid #666'} for x in [50,68]]+[{**box(86,53,10,9,'transparent','50%'),'border':'1px solid #666'}]
for key,s in D.items():s['id']=key.split('/')[1]
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(D,ensure_ascii=False,separators=(',',':')))
