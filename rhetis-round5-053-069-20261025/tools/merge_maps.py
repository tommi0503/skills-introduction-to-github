from pathlib import Path
import json,re
from lxml import html
from PIL import Image
def norm_markup(s):
 try:return re.sub(r"[\W_]+","","".join(html.fragment_fromstring(s,create_parent=True).itertext()),flags=re.U).casefold()
 except:return ""
Q=Path(__file__).resolve().parents[1];M=Q/'source-maps';roles=json.loads((Q/'role-contracts.json').read_text());summary={}
def page(n):
 m=re.findall(r'\d+',str(n));return m[-1].zfill(2) if m else str(n)
for col in json.loads((Q/'collections.json').read_text()):
 cid=col['id'];instances=[];covers=set();source_groups={}
 for group in ['furniture','surface','charts','relations','advanced']:
  f=M/(cid+'-'+group+'.json')
  if not f.exists():raise SystemExit('Missing '+str(f))
  d=json.loads(f.read_text());source_groups[group]=len(d.get('instances',[])) if group!='relations' else sum(len(x.get('instances',[]))for x in d.get('leaves',{}).values())
  raw_instances=d.get('instances',[])
  if group=='relations':raw_instances=[x for leaf in d.get('leaves',{}).values() for x in leaf.get('instances',[])]
  for raw in raw_instances:
   e=dict(raw);e['page']=page(e['page']);e['owner']=group;e['bbox']=[round(float(x),2)for x in e['bbox']]
   if e.get('use','').startswith('same-as:'):e['use']='same-as:'+page(e['use'].split(':',1)[1])
   if group=='furniture'and e.get('source',{}).get('cover'):covers.add(e['page'])
   design=e.get('design','')
   if isinstance(design,dict):e['source'].setdefault('numbers',design);e['design']='; '.join(str(k)+'='+str(v)for k,v in design.items())
   if e.get('leaf') and not e.get('fixture') and (Q/cid/'elements'/e['leaf']/'fixtures'/('replica-'+e['page']+'.html')).exists():e['fixture']='replica-'+e['page']
   if e.get('use')=='unexpressible':e['candidate_leaf']=e.get('leaf');e['leaf']=None
   if group=='furniture' and e.get('use')=='background' and e['bbox']==[0.0,0.0,1280.0,720.0]:
    png=next((Q/'reference/frozen'/(cid+'-review')/'replica').glob('*'+e['page']+'.png'),None)
    if png:
     pixel=list(Image.open(png).convert('RGB').getpixel((0,0)));e['source']['paintedCornerRGB']=pixel
     if max(pixel)-min(pixel)>35 and max(pixel)<175:e['source']['emphasis']=True;e['source']['paletteRole']='--a1-9'
   e['instance_id']=cid+'-'+e['page']+'-'+group+'-'+str(len(instances)+1)
   instances.append(e)
 # Integration groups are measured semantic copy blocks, not page CSS.
 integration=M/(cid+'-integration.json')
 if integration.exists():
  for index,group in enumerate(json.loads(integration.read_text()).get('groups',[]),1):
   originals=[]
   for match in group['replaces']:
    wanted=[round(float(x),2)for x in match['bbox']]
    hit=next((x for x in instances if x['page']==page(match['page']) and (x.get('leaf') or x.get('candidate_leaf'))==match['leaf'] and all(abs(a-b)<.03 for a,b in zip(x['bbox'],wanted))),None)
    if not hit:raise ValueError('Missing integration source '+cid+' '+str(match))
    originals.append(hit)
   for original in originals:instances.remove(original)
   entry=dict(group['instance']);entry['page']=page(entry['page']);entry['bbox']=[round(float(x),2)for x in entry['bbox']];entry['owner']='surface';entry['instance_id']=cid+'-'+entry['page']+'-integration-'+str(index)
   entry.setdefault('source',{})['materialParts']=[{'bbox':x['bbox'],'source':x.get('source'),'markup':x.get('markup'),'originalMeasurement':x['instance_id']}for x in originals]
   instances.append(entry)
 if integration.exists():
  for index,raw_entry in enumerate(json.loads(integration.read_text()).get('extraInstances',[]),1):
   entry=dict(raw_entry);entry['page']=page(entry['page']);entry['bbox']=[round(float(x),2)for x in entry['bbox']]
   if isinstance(entry.get('owner'),dict):entry['inline_owner']=entry['owner']
   entry['owner']='surface';entry['instance_id']=cid+'-'+entry['page']+'-inline-'+str(index)
   if entry.get('use','').startswith('same-as:'):entry['use']='same-as:'+page(entry['use'].split(':',1)[1])
   instances.append(entry)
 # Page-cover text is already a foundation part rather than an independent prose component.
 removed=[];kept=[]
 for e in instances:
  if e['owner']=='surface' and e['page']in covers and e.get('leaf')in ['headline','prose','agenda','logo-group']:
   removed.append(e);continue
  kept.append(e)
 instances=kept
 emphasis_pages={e['page']for e in instances if e.get('source',{}).get('emphasis')}
 for e in instances:
  if e.get('leaf')=='prose' and e['page']in emphasis_pages and norm_markup(e.get('markup',''))=='miricompany':
   e['leaf']=None;e['use']='furniture';e['owner']='furniture';e['design']='독립된 덱 서명 브랜드 — 본문 문단이 아닌 페이지 장치';e['source']['furniturePart']='brand-signature'
 # A compound owns the text and connectors of its members. A measured text
 # part may retain a provenance entry, but must not be painted a second time.
 for child in instances:
  if not child.get('leaf') or not child.get('markup'):continue
  cb=child['bbox'];ct=norm_markup(child['markup']);parents=[]
  if not ct:continue
  for parent in instances:
   if parent is child or parent['page']!=child['page'] or not parent.get('leaf') or not parent.get('markup'):continue
   pb=parent['bbox']
   if pb[2]*pb[3]<cb[2]*cb[3]*1.15:continue
   if cb[0]>=pb[0]-2 and cb[1]>=pb[1]-2 and cb[0]+cb[2]<=pb[0]+pb[2]+2 and cb[1]+cb[3]<=pb[1]+pb[3]+2 and ct in norm_markup(parent['markup']):parents.append(parent)
  if parents:
   parent=min(parents,key=lambda x:x['bbox'][2]*x['bbox'][3]);child['contained_by']=parent['instance_id'];child['assembly']='Already rendered by the owning compound contract part; no duplicate grid root.'
 # A primitive measurement already owned by a compound is not a second
 # unsupported element. Preserve it as source material of the smallest owner.
 absorbed=[]
 for child in list(instances):
  if child.get('owner')!='surface' or child.get('use')!='unexpressible' or not child.get('markup'):continue
  ct=norm_markup(child['markup']);cb=child['bbox'];parents=[]
  if not ct:continue
  for parent in instances:
   if parent is child or parent in absorbed or parent['page']!=child['page'] or not(parent.get('markup') or parent.get('source',{}).get('raw_markup')):continue
   if not(parent.get('leaf')or parent.get('use')=='unexpressible'):continue
   pb=parent['bbox']
   if pb[2]*pb[3]<cb[2]*cb[3]*.98:continue
   if pb[2]*pb[3]<cb[2]*cb[3]*1.15 and (parent.get('leaf') or parent.get('candidate_leaf')) in ('prose','headline','tag'):continue
   if cb[0]>=pb[0]-2 and cb[1]>=pb[1]-2 and cb[0]+cb[2]<=pb[0]+pb[2]+2 and cb[1]+cb[3]<=pb[1]+pb[3]+2 and (ct in norm_markup(parent.get('markup') or parent.get('source',{}).get('raw_markup','')) or ((parent.get('leaf') or parent.get('candidate_leaf'))=='image-frame' and re.fullmatch(r'(?:기기화면|사진)[0-9]+',ct))):parents.append(parent)
  if parents:
   parent=min(parents,key=lambda x:x['bbox'][2]*x['bbox'][3]);parent.setdefault('source',{}).setdefault('materialParts',[]).append({'bbox':cb,'text':''.join(html.fragment_fromstring(child['markup']).itertext()),'source':child.get('source'),'design':child.get('design'),'originalMeasurement':child['instance_id']});absorbed.append(child)
 for child in absorbed:instances.remove(child)
 d={'collection':cid,'replica_frozen':True,'roles':roles[cid],'instances':instances,'source_groups':source_groups,'foundation_reclassified':len(removed),'absorbed_material_parts':len(absorbed)}
 R=Q/(cid+'-review');tmp=R/'map.json.tmp';tmp.write_text(json.dumps(d,ensure_ascii=False,indent=2));tmp.replace(R/'map.json')
 counts={}
 for e in instances:
  if e.get('leaf')and e.get('use')=='base':counts[e['leaf']]=counts.get(e['leaf'],0)+1
 duplicate={k:v for k,v in counts.items()if v>1}
 if duplicate:raise SystemExit('Duplicate base '+cid+' '+str(duplicate))
 summary[cid]={'instances':len(instances),'observed_base':counts,'unexpressible':sum(e.get('use')=='unexpressible'for e in instances),'groups':source_groups,'furniture_reclassified':len(removed)}
(Q/'map-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));print(json.dumps(summary,ensure_ascii=False,indent=2))
