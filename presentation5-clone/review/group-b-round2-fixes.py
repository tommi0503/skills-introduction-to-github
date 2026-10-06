from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0])
d=json.loads((ROOT/'src/decks/group-b-data.json').read_text())
# Round-two observations: measured capitals, same-cell centering, real route connectors.
for e in d['p050/s02-15']['elements']:
 if e.get('text')=='DATA VISUAL COMPARISON':e['size']=100;e['w']=80
 if e.get('text','').startswith('Lorem'):e['y']=74
 if e.get('text','').endswith('%'):e['size']=140
for e in d['p050/s02-07']['elements']:
 if e.get('text') in ['40,5','59,5']:e['size']=160;e['y']=32
 if e.get('text')=='%':e['y']=39;e['size']=98
for e in d['p050/s02-09']['elements']:
 if e.get('size',0)>80:e['align']='right';e['x']=52;e['w']=43
for e in d['p050/s02-12']['elements']:
 if e.get('icon')=='CircleArrowRight':e['y']=70
 if e.get('text','').startswith('GLOBAL PERSPECTIVES'):e['y']=79
 if e.get('text','').startswith('Lorem'):e['y']=87
for e in d['p051/s01-05']['elements']:
 if e.get('text') in ['S','W','O','T']:e['x']-=7.5
 if e.get('text')=='S.W.O.T Analysis':e['x']=25;e['w']=50
for k,s in d.items():
 if k in ['p051/s01-04','p051/s05-02']:
  for e in s['elements']:
   if e.get('text')=='Target\nMarket':e['size']=52
   if e.get('text')=='Product\nMarketing\nReach':e['size']=29
 if k=='p051/s01-07':
  for e in s['elements']:
   if e.get('text')=='Sales\nDevelopment\nPlan':e['text']='Sales\nDevelopment Plan';e['size']=53;e['w']=91;e['runs']=[{'text':'Sales\n','color':'#efbd1c'},{'text':'Development Plan','color':'#fff'}]
 if k=='p051/s01-09':
  for e in s['elements']:
   if e.get('text','').startswith('Lorem'):e['y']-=7;e['size']=14
 if not k.startswith('p064'):continue
 for e in s['elements']:
  if e.get('size',0)>40:e['weight']=500;e['size']*=.88
  if e['kind']=='icon':e['w']*=.65;e['h']*=.65;e['x']+=1;e['y']+=1.5
 s['elements'] += [tx('Creative Step Business',3,4,31,15,color='#ad7cc2'),tx(k.split('-')[-1],95,94,3,14,color='#888')]
 if k=='p064/s04-02':
  s['elements'] += [chip('Starting and Expanding Your Business',62,48,32,8,16,'#fff','#a57cc0',weight=600,radius=30)]
  for i,y in enumerate([65,78]):s['elements'] += [tx(f'0{i+1}.',52,y,6,25,weight=600,color='#a57cc0'),para(57,y,37,16,lines=2),path([[52,y+9],[94,y+9]],'#eee',1)]
 if k=='p064/s04-01':
  for e in s['elements']:
   if e.get('text')=='Your Subtitle Here':e['y']=55
   if e.get('text','').startswith('Lorem') and e['x']<10:e['y']=61
   if e.get('text')=='Learn More':e['y']=73
 if k=='p064/s04-04':
  es=[e for e in s['elements'] if e['kind']=='text' and e.get('size',0)>35];g=[photo(8,40,15,51)];cs=['#7565ee','#bd5bd0','#f6bc00','#303030'];origins=[(15,16),(25,36),(35,56),(45,76)]
  g += [box(15,0,9.5,17,'#2619d5')]
  for i,(x,y) in enumerate(origins):c=cs[i];g += [path([[x,y],[x+22,y],[x+26,y+12],[x+3,y+12]],c,0,c),box(x+3,y+2,4,7,W if (W:='#fff') else W,'50%')];es += [chip(f'0{i+1}',x+3,y+2,4,7,18,W,'#ad7cc2',radius='50%'),tx('Step Here',x+9,y+3,15,23,weight=600,color=W),para(x+30,y+3,21,14,lines=3)]
  for i,(x,y) in enumerate(origins[:-1]):g += [path([[x+26,y+12],[x+21,y+20],[x+10,y+20],[x+17,y+12]],cs[i],0,cs[i])]
  s['elements']=g+es
 if k=='p064/s04-05':
  s['elements']=[e for e in s['elements'] if e['kind']=='text' and e.get('size',0)>35];s['elements'] += [ic(90,11,5,9,'Trophy','#dfb61d')]
  for i,(x,y,c) in enumerate([(30,82,'#7565ee'),(42,70,'#bd5bd0'),(54,58,'#f6bc00'),(66,46,'#303030')]):
   s['elements'] += [path([[x,y],[x+12,y-3],[x+20,y+9],[x+8,y+12]],c,0,c),path([[x+8,y+12],[x+20,y+9],[x+20,y+17],[x+8,y+20]],c,0,c),path([[x,y],[x+8,y+12],[x+8,y+20],[x,y+8]],c,0,c),box(x+9,y+1,4,7,'#fff','50%'),ic(x+10,y+2.5,2,3.5,['Target','Coins','HandCoins','ChartNoAxesCombined'][i],c),tx('Your Step '+['One','Two','Three','Four'][i],x-21,y-7,18,18,weight=600,color=c),para(x-21,y-2,18,13,lines=3)]
  s['elements'] += [path([[79,57],[80,37],[79,29],[86,25],[90,47]],'#303030',0,'#303030')]
 if k=='p064/s04-06':
  for e in s['elements']:
   if e.get('text') in ['Step One','Step Two','Step Three']:e['x']-=9
   if e.get('text','').startswith('Lorem') and e['x']>50:e['x']-=9;e['w']=21;e['size']=13
 if k=='p064/s04-08':
  for e in s['elements']:
   if e.get('text','').startswith('Building a'):e['runs']=[{'text':'Building a\nStrong ','color':'#171717'},{'text':'Brand\nIdentity','color':'#ad7cc2'}]
(ROOT/'src/decks/group-b-data.json').write_text(json.dumps(d))
