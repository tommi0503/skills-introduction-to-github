"""Contract-only078 assemblies. Original measured edges are snapped once; no visual retuning.
Writes only reassembled HTML and support-map-corrections/placement evidence.
"""
from pathlib import Path
from lxml import html,etree
import json,math,re,copy,hashlib
P=Path(__file__).parent;K=P/'onboard-docket';M=json.loads((P/'map.json').read_text());S=json.loads((P/'source-measurements.json').read_text());D=P/'reassembled';D.mkdir(exist_ok=True)
DOC={n:html.fromstring((P/'replica'/f'slide_{n}.html').read_text()) for n in S}
CHILD={n:doc.xpath('//section[contains(concat(" ",normalize-space(@class)," ")," slide ")]')[0] for n,doc in DOC.items()}
def source(n,index):return list(CHILD[n])[index-1]
def tag(name='div',cls=None,text=None,el=None):
 e=html.Element(name)
 if cls:e.set('class',cls)
 if el:e.set('data-el','onboard-docket-'+el)
 if text is not None:e.text=text
 return e
def rich_into(dest,src):
 dest.text=src.text
 for child in src:
  if not isinstance(child.tag,str):continue
  if child.tag=='svg':continue
  if child.tag=='br':new=html.Element('br')
  elif child.tag in ['b','strong']:new=html.Element('b');rich_into(new,child)
  else:
   new=html.Element('span')
   if 'background:#000' in child.get('style','').replace(' ',''):new.set('class','hl');new.set('data-el','onboard-docket-tag')
   rich_into(new,child)
  new.tail=child.tail;dest.append(new)
 return dest
def part(parent,cls,src=None,text=None,name='p'):
 e=tag(name,cls,text)
 if src is not None:rich_into(e,src)
 parent.append(e);return e
def root(leaf,cls=None):return tag('div',cls or {'image-frame':'frame','metric':'stats'}.get(leaf,leaf),el=leaf)
def text_nodes(i):return [r for r in i['sourceMeasurements'] if r['text']]
def grid(bbox):
 x,y,w,h=bbox;gx=(1086+14)/12;gy=(420+14)/6;nearest=lambda v:math.floor(v+.5)
 c=max(0,min(11,nearest((x-97)/gx)));r=max(0,min(5,nearest((y-237)/gy)))
 ce=max(c+1,min(12,nearest((x+w+14-97)/gx)));re_=max(r+1,min(6,nearest((y+h+14-237)/gy)))
 return [c+1,r+1,ce-c,re_-r]
def place(e,bbox):
 c,r,w,h=grid(bbox);e.set('style',f'grid-column:{c} / span {w};grid-row:{r} / span {h}');return e
# Two map extraction groups contain independent source paragraphs; split only those measured regions.
CORRECTIONS=[]
for oldid in ['06-086','12-105']:
 old=next((i for i in M['instances'] if i['id']==oldid),None)
 if old:
  parts=[]
  for j,r in enumerate(text_nodes(old)):
   i=copy.deepcopy(old);i['id']=oldid+'-'+str(j+1);i['bbox']=r['bbox'];i['sourceNodes']=[r['index']];i['selectors']=[r['selector']];i['sourceMeasurements']=[r];i.pop('fixture',None);parts.append(i)
  CORRECTIONS.append({'id':oldid,'reason':'Distinct independently positioned source paragraphs were aggregated by the extractor. These are not one sentence split to change CSS.','replacements':[{'id':i['id'],'bbox':i['bbox'],'sourceNodeIds':i['sourceNodes'],'leaf':'prose','use':i['use']} for i in parts]})
  M['instances']=[i for i in M['instances'] if i['id']!=oldid]+parts
if CORRECTIONS:(P/'support-map-corrections-073.json').write_text(json.dumps(CORRECTIONS,ensure_ascii=False,indent=2)+'\n')

def component(n,i):
 leaf=i['leaf'];rows=text_nodes(i);nodes=[source(n,r['index']) for r in rows];e=None
 if leaf=='agenda':
  e=root(leaf)
  for j in range(0,len(nodes),2):
   a=tag('div','entry');part(a,'mark',nodes[j],name='span');part(a,'name',nodes[j+1]);e.append(a)
 elif leaf=='quote':
  e=root(leaf);q=tag('blockquote');part(q,None,nodes[0]);part(q,None,nodes[1]);e.append(q);by=tag('div','by');part(by,'name',nodes[2]);e.append(by)
 elif leaf=='tag':return None # Original04 highlight is a real inline tag inside its quote paragraph.
 elif leaf=='image-frame':
  e=root(leaf);seat=tag('div','seat'+(' portrait' if n=='04' else ''));seat.set('data-ph','');e.append(seat)
 elif leaf=='headline':
  e=root(leaf,'headline'+(' center' if '.center' in i['use'] else ''))
  if len(nodes)>1:part(e,'kick',nodes[0]);part(e,None,nodes[1],name='h2')
  else:part(e,None,nodes[0],name='h2')
 elif leaf=='prose':
  cls='prose'+(' lead' if '.lead' in i['use'] else ' quiet' if '.quiet' in i['use'] or n=='12' else '')
  e=root(leaf,cls)
  for s in nodes:part(e,None,s)
 elif leaf=='pill':
  e=root(leaf,'pill'+(' on' if '.on' in i['use'] else ' quiet' if '.quiet' in i['use'] else ''));p=tag('div','parts');part(p,'name',nodes[0]);e.append(p)
 elif leaf=='callout':
  e=root(leaf);part(e,None,nodes[0])
 elif leaf=='card':
  variants=re.findall(r'\.(quiet|on|line|tone-[1-5])',i['use']);variants += ['tone-1'] if i['id']=='08-092' and 'tone-1' not in variants else [];e=root(leaf,'card'+(' '+ ' '.join(variants) if variants else ''));p=tag('div','parts')
  if '.on' in i['use'] or (n=='19'):
   part(p,'note',nodes[-1])
  else:
   part(p,'name',nodes[0]);part(p,'note',nodes[1])
   if n=='11':
    mark=tag('span','mark');icon=tag('span','icon');icon.set('data-icon',['chart-no-axes-combined','chart-column','lightbulb'][(int(i['sourceNodes'][0])-7)//5]);mark.append(icon);p.insert(0,mark)
  e.append(p)
 elif leaf=='list':
  e=root(leaf,'list divided' if '.divided' in i['use'] else 'list num')
  if '.divided' in i['use']:
   for s in nodes:
    item=tag('div','item');name=tag('p','name');name.text=re.sub(r'^\s*•\s*','',s.text_content());item.append(name);e.append(item)
  else:
   for j in range(0,len(nodes),2):
    item=tag('div','item');name=tag('p','name');name.text=re.sub(r'^\s*\d+\.\s*','',nodes[j].text_content());item.append(name);part(item,'note',nodes[j+1]);e.append(item)
 elif leaf=='steps':
  col='.col' in i['use'];e=root(leaf,'steps col' if col else 'steps')
  if col:
   for j in range(0,len(nodes),3):
    a=tag('div','step');part(a,'mark',nodes[j],name='div');part(a,'name',nodes[j+1]);part(a,'note',nodes[j+2]);e.append(a)
  else:
   for j in range(0,len(nodes),2):
    a=tag('div','step');m=tag('div','mark');icon=tag('span','icon');icon.set('data-icon',['handshake','lightbulb','chart-column','rocket'][j//2]);m.append(icon);a.append(m);part(a,'name',nodes[j]);part(a,'note',nodes[j+1]);e.append(a)
 elif leaf=='metric':
  e=root(leaf)
  for j in range(0,len(nodes),3):
   a=root(leaf,'stat');p=tag('div','parts');part(p,'name',nodes[j]);fig=tag('p','fig');t=nodes[j+1].text_content();match=re.fullmatch(r'\s*(\S+)\s+(.+?)\s*',t)
   if match:fig.text=match[1]+' ';fig.append(tag('small',text=match[2]))
   else:fig.text=t
   p.append(fig);part(p,'note',nodes[j+2]);a.append(p);e.append(a)
 else:raise ValueError((n,i['id'],leaf))
 return e

CSS=['../assets/fonts/fonts.css','../onboard-docket/kit/css/tokens.css','../onboard-docket/foundation/foundation.css']+[f'../onboard-docket/elements/{f.name}/element.css' for f in sorted((K/'elements').iterdir()) if (f/'element.css').exists()]+['../assets/v2-platform.css','../assets/source-palette-v2.css']
HEAD=''.join('<link rel="stylesheet" href="'+s+'">' for s in CSS);placements=[]
for n in sorted(S):
 s=tag('section','slide'+(' cover' if n in ['01','03'] else ''));page=tag('div','page');s.append(page)
 if n=='01':
  rail=tag('div','rail')
  for name in ['file-pen-line','briefcase-business','folders','network','messages-square','pencil','search']:
   icon=tag('span','icon');icon.set('data-icon',name);rail.append(icon)
  s.insert(0,rail);lock=tag('div','lockup at-left');kicker=part(lock,'kicker',source(n,16))
  for logo in kicker.xpath('./span'):
   if not logo.text_content():logo.set('class','seat logo');logo.set('data-ph','1')
  h=part(lock,'title',name='h1');h.text=source(n,17).text_content();h.append(tag('br'));b=tag('b',text=source(n,18).text_content());h.append(b);part(lock,'lead',source(n,19));page.append(lock)
  meta=tag('div','meta');part(meta,'label',source(n,21),name='span');tail=tag('span',text=source(n,22).text_content());meta.append(tail);page.append(meta)
 else:
  oldrail=next(iter(CHILD[n].xpath('.//div[@class="rail"]')),None);top=tag('div','top');brand=oldrail.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," brand ")]')[0] if oldrail is not None else None
  part(top,'label',text=brand.text_content() if brand is not None else 'MIRICOMPANY',name='span');chapter=oldrail.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," chapter ")]') if oldrail is not None else []
  if chapter:top.append(tag('span',text=chapter[0].text_content()))
  s.insert(0,top)
  if n=='03':
   lock=tag('div','lockup at-center');h=part(lock,'title',name='h1');h.text=source(n,3).text_content();h.append(tag('br'));h.append(tag('b',text=source(n,4).text_content()));part(lock,'lead',source(n,6));page.append(lock)
  else:
   oldhead=next(iter(CHILD[n].xpath('.//header')),None);head=tag('header','head'+(' center' if n=='02' else ''))
   if n=='02':part(head,'title',source(n,3),name='h1')
   else:
    part(head,'no',oldhead.xpath('./span[@class="num"]')[0],name='span');part(head,'title',oldhead.xpath('./span[@class="title"]')[0],name='h1');part(head,'lead',oldhead.xpath('./span[@class="suffix"]')[0])
   page.append(head);body=tag('div','body');page.append(body)
   for i in M['instances']:
    if i['page']!=n or i['use'] in ['background','furniture','unexpressible']:continue
    e=component(n,i)
    if e is None:
     placements.append({'page':n,'id':i['id'],'placement':'semantic inline tag in quote, not a second overlapping page root','bbox':i['bbox']});continue
    place(e,i['bbox']);body.append(e);placements.append({'page':n,'id':i['id'],'sourceBBox':i['bbox'],'grid':grid(i['bbox']),'leaf':i['leaf']})
 out='<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=1280"><title>078 original contract assembly '+n+'</title>'+HEAD+'</head><body>'+html.tostring(s,encoding='unicode')+'<script src="../assets/lucide.min.js"></script><script src="../assets/render-icons.js"></script></body></html>\n'
 (D/f'slide_{n}.html').write_text(out)
evidence=P/'support-reassembly-placement-073.json'
previous=json.loads(evidence.read_text()) if evidence.exists() else {}
initial=previous.get('initialPlacements',previous.get('placements',placements))
oldgrid={x['id']:x['grid'] for x in initial if 'grid' in x};newgrid={x['id']:x['grid'] for x in placements if 'grid' in x}
assert all(newgrid[k]==oldgrid[k] for k in newgrid.keys() & oldgrid.keys()),'A previously fixed grid placement changed'
evidence.write_text(json.dumps({'algorithm':'Nearest source start/end grid boundaries, with14px gap and fixed body97,237,1086,420. No visual retuning.','sourceMapSHA256':hashlib.sha256((P/'map.json').read_bytes()).hexdigest(),'foundationSHA256':hashlib.sha256((K/'foundation/foundation.css').read_bytes()).hexdigest(),'initialGridPreserved':True,'initialPlacements':initial,'removedAsNewContractGap':sorted(oldgrid.keys()-newgrid.keys()),'placements':placements},ensure_ascii=False,indent=2)+'\n')
print('assembled',len(S),'placements',len(placements),'map extraction corrections',len(CORRECTIONS))
