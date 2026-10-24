from pathlib import Path
import json
P=Path(__file__).parent;A=json.loads((P/'map.json').read_text());raw={p['page']:p['nodes']for p in A['rawMeasurements']}
expanded=[]
for inst in A['instances']:
 if inst['leaf']=='foundation':
  for j,n in enumerate(inst['sourceMeasurements']):expanded.append({'id':inst['id']+'-f'+str(j),'page':inst['page'],'leaf':None,'use':'background'if'photo'in n.get('classes','')else'furniture','bbox':n['bbox'],'fixture':None,'selectors':[n.get('selector',inst['selectors'][min(j,len(inst['selectors'])-1)])],'sourceMeasurements':[n]})
  continue
 if inst['leaf']=='card'and inst['page']in[8,11,12]:inst['use']='base'
 if inst['leaf']=='pill'and inst['page']==20 and inst['use']=='variant:on':inst['use']='base'
 if inst['use'].startswith('variant:'):inst['contractVariant']=inst['use'].split(':',1)[1]
 elif inst['use']!='unexpressible':inst['contractVariant']=''
 expanded.append(inst)
A['instances']=expanded
for inst in A['instances']:
 if inst['leaf']=='timeline'and inst['page']==17:
  want=[n for n in inst['sourceMeasurements']if n['index']not in[24,25,26]]if inst['use']!='unexpressible'else inst['sourceMeasurements']+[raw[17][j]for j in[24,25,26]]
  inst['sourceMeasurements']=want;inst['selectors']=[n['selector']for n in want];x=min(n['bbox'][0]for n in want);y=min(n['bbox'][1]for n in want);right=max(n['bbox'][0]+n['bbox'][2]for n in want);bottom=max(n['bbox'][1]+n['bbox'][3]for n in want);inst['bbox']=[x,y,right-x,bottom-y]
  if inst['use']=='unexpressible':inst['why']+=' The three PHASE labels belong to these duration groups, not to five individual stop dates.'
first={};variants={}
for inst in A['instances']:
 if inst['use']in['furniture','background','unexpressible']:continue
 leaf=inst['leaf'];variant=inst.get('contractVariant','')
 if variant:
  key=(leaf,variant)
  if key in variants:inst['use']='same-as:'+str(variants[key]['page']);inst['baseRef']=variants[key]['id']
  else:variants[key]=inst;inst['use']='variant:'+variant
 elif leaf in first:inst['use']='same-as:'+str(first[leaf]['page']);inst['baseRef']=first[leaf]['id']
 else:first[leaf]=inst;inst['use']='base'
(P/'map.json').write_text(json.dumps(A,ensure_ascii=False,indent=2));print(len(A['instances']),'canonical instances; bases',len(first))
