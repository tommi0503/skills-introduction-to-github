"""Remaining selectors in the same third-round batch; no further comparison loop."""
import json,math,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
exec((ROOT/'review/group-b-refine.py').read_text().split('# Text repair:')[0]);src=ROOT/'src/decks/group-b-data.json';data=json.loads(src.read_text());rpath=ROOT/'review/group-b-final-third-round-modified.json';record=json.loads(rpath.read_text());notes={}
def els(k):return data[k]['elements']
def rem(k,p):data[k]['elements']=[e for e in els(k) if not p(e)]
def put(k,*es):els(k).extend(es)
def note(k,s):notes.setdefault(k,[]).append(s)
k='p091/s03-08';rem(k,lambda e:e['kind']=='box' and e['x']==74 and e['y']==37 and e.get('fill')=='#baacd6');note(k,'Old displaced title highlight removed after adding its correctly aligned replacement.')
k='p101/s02-03';
for e in els(k):
 if e['kind']=='text' and e.get('text')=='Your title' and e['y'] in [47,83]:e.update(x=39,w=13,align='center',size=21,h=5)
note(k,'Two orange arrow labels centered in their actual bar, separated from numbered circles.')
for k in ['p101/s02-08','p101/s03-05']:
 for e in els(k):
  if e['kind']=='path' and len(e.get('points',[]))==10 and e.get('fill')=='none':
   xx=min(p['x']for p in e['points']);c='#e4d34b' if k.endswith('s02-08') and xx>66 else '#fff';e.update(fill=c,color=c,strokeWidth=0)
 note(k,'Final rating star filled white on the two colored cards and gold on the white card, matching visible original.')
k='p101/s03-07';rem(k,lambda e:e['kind']=='text' and ('●' in e.get('text','') or e.get('text')=='60        83        65        104'))
for i,v in enumerate(['Your Text 1','Your Text 2','Your Text 3']):
 for e in els(k):
  if e['kind']=='text' and e.get('text')==['Revenue','Profit','Cost'][i] and e['y']==86.8:e.update(text=v,y=89,w=12,size=11)
 for e in els(k):
  if e['kind']=='box' and e.get('radius')=='50%' and e['x']==[11,24,34][i]:e['y']=89.3
for v,x,y in [('60',71,83),('83',78,79),('65',84,85),('104',91,80)]:put(k,tx(v,x,y,5,12,color='#fff'))
note(k,'Old combined black-dot legend and combined one-row value string removed; three colored legend labels and four distinct plotted values remain.')
k='p104/s02-01';
for e in els(k):
 if e['kind']=='text' and e.get('text')=='average order value' and e['x']==39:e['text']='20 templates'
 if e['kind']=='text' and e.get('text','').startswith('Repeatable.'):e['w']=31
note(k,'Product Bundles 20 templates and native top-right text box width.')
k='p104/s03-04';
for e in els(k):
 if e['kind']=='text' and e['x']==70 and e['y']==38:e.update(text='Represents the full revenue\npotential across all markets\nglobally.',size=13,h=9)
 if e['kind']=='text' and e['x']==71 and e['y']==83:e.update(text='Serviceable\nObtainable Market',size=16,h=6)
 if e['kind']=='text' and e['x']==71 and e['y']==92:e.update(text='Revenue we can earn through\nfocused customers and growth.',size=10.5,h=5.5)
note(k,'TAM native unique definition restored; SOM label made distinct and unreadable small bottom caption replaced by plausible ordinary two-line prose.')
k='p104/s03-05';
for e in els(k):
 if e['kind']=='text' and 'HOW WE SOLVE IT' in e.get('text',''):e['runs']=[{'text':'●  ','color':'#ed6a63'},{'text':'HOW WE SOLVE IT','color':e.get('color','#171342')}]
note(k,'How we solve it coral dot is actual DOM text run, with remaining caption color preserved.')
k='p104/s03-07';
for e in els(k):
 if e['kind']=='text' and e['x']==42 and e.get('text','').startswith('These values'):e['w']=23
note(k,'Values introduction constrained to its native gutter before the four right cards.')
# Save only this final stage once; merge all third-round notes.
(tmp:=src.with_suffix('.json.tmp')).write_text(json.dumps(data));tmp.replace(src)
for k,v in notes.items():
 if k not in record['modifiedIDs']:record['modifiedIDs'].append(k);record['pages'].append({'id':k,'fixes':[],'remainingDifferences':['Detailed images are solid gray by instruction; miniature font rendering remains approximate.']})
 next(p for p in record['pages'] if p['id']==k)['fixes']+=v
record['modifiedIDs'].sort();record['sourceSha256After']=hashlib.sha256(src.read_bytes()).hexdigest();rpath.write_text(json.dumps(record,ensure_ascii=False,indent=2));print('total modified',len(record['modifiedIDs']))
