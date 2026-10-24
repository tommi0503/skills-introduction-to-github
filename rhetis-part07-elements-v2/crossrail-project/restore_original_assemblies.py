"""Restore original presentation text/data in assemblies only. Never alter fixtures or grid.
Keep a stable root->source identity file, so later reruns do not rely on rewritten text.
"""
from pathlib import Path
from lxml import html,etree
import json,re,copy,hashlib
P=Path(__file__).parent;K=P/'crossrail';M=json.loads((P/'map.json').read_text());INDEX={i['id']:i for i in M['instances']};DOC={n:html.fromstring((P/'replica'/f'slide_{n:02}.html').read_text()) for n in range(1,31)};SLIDE={n:d.xpath('//section')[0] for n,d in DOC.items()}
def src(n,number):return list(SLIDE[n])[number-1]
def ri(r):return int(r['id'].split('-')[-1])
def rows(i):return sorted([r for r in i.get('sourceMeasurements',[]) if r.get('text')],key=ri)
def source_for(n,r):return src(n,ri(r))
def clear(e):
 for c in list(e):e.remove(c)
 e.text=None
 return e
def rich(e,s,keep_icon=False,strip_bullet=False):
 icon=next(iter(e.xpath('./span[contains(concat(" ",normalize-space(@class)," ")," icon ")]')),None) if keep_icon else None
 if icon is not None:icon=copy.deepcopy(icon)
 clear(e);text=s.text or ''
 if strip_bullet:text=re.sub(r'^\s*•\s*','',text)
 if icon is not None:e.append(icon);icon.tail=text
 else:e.text=text
 def copy_child(ch):
  if ch.tag=='svg':return None
  z=html.Element('br' if ch.tag=='br' else 'b' if ch.tag in ['b','strong'] else 'span');z.text=ch.text
  for c in ch:
   if isinstance(c.tag,str):
    a=copy_child(c)
    if a is not None:z.append(a)
  z.tail=ch.tail;return z
 for ch in s:
  if isinstance(ch.tag,str):
   a=copy_child(ch)
   if a is not None:e.append(a)
 return e
def settext(e,t):clear(e);e.text=t;return e
def cls(e,c):return c in e.get('class','').split()
def direct(e,c):return [x for x in e if isinstance(x.tag,str) and cls(x,c)]
def node_for(rows,term):return next(r for r in rows if r['id']==term)
identity_file=P/'original-assembly-identities.json'
if identity_file.exists():IDENT=json.loads(identity_file.read_text())
else:
 old=json.loads((P/'assembly-placement.json').read_text());IDENT={}
 for page in old:
  n=page['page'];d=html.fromstring((P/'reassembled'/f'slide_{n:02}.html').read_text());body=d.xpath('//div[@class="body"]');roots=list(body[0]) if body else[];items=page.get('placements',[]);assert len(roots)==len(items),(n,len(roots),len(items));ids=[]
  for e,x in zip(roots,items):
   candidates=x['mapIds'];assert candidates,(n,x);col=int(re.search(r'grid-column:\s*(\d+)',e.get('style'))[1]);px=95+(col-1)*(1102/12);chosen=min(candidates,key=lambda a:abs(INDEX[a]['bbox'][0]-px));ids.append(chosen)
  IDENT[str(n)]=ids
 identity_file.write_text(json.dumps(IDENT,ensure_ascii=False,indent=2)+'\n')
# Correct real data mistakenly owned by decorative gaps. One direct source node keeps one owner.
def move(n,ids,target):
 dest=INDEX[target]
 for i in M['instances']:
  if i['page']!=n or i is dest:continue
  moved=[r for r in i.get('sourceMeasurements',[]) if r['id'] in ids];i['sourceMeasurements']=[r for r in i.get('sourceMeasurements',[]) if r['id'] not in ids]
  for r in moved:r['owner']=target;dest.setdefault('sourceMeasurements',[]).append(r)
move(3,{'source-7'},'p03-statement')
# Source22 points26..39 are line data, not the two decorative background columns.
move(22,{'source-'+str(i) for i in range(25,40)},'p22-weekly-line')
move(26,{'source-14','source-16','source-22','source-26'},'p26-four-lanes')
# Empty furniture duplicate after correct statement ownership no longer represents a visible separate part.
M['instances']=[i for i in M['instances'] if not(i['id']=='p03-header-source-7' and not i.get('sourceMeasurements'))]
# Pale time rails are genuine image-reference gaps; coloured bars have all been restored to roadmap ownership.
for i in M['instances']:
 if i['id']=='p26-first-underlay':i['bbox']=[274,343,455,79];i['why']='The image reference has a pale time-rail field behind the first coloured bar. The coloured bar and its label are ordinary roadmap data and are not omitted. Only this additional underlay field lacks a contract part.'
 if i['id']=='p26-final-underlay':i['bbox']=[729,575,455,80];i['why']='Only the pale time-rail field behind the final coloured bar is unsupported. The final bar and its label are restored as normal roadmap data.'
INDEX={i['id']:i for i in M['instances']}
# Avoid body identity changing when a source is later classified unexpressible: the HTML keeps its other grid slots.
changed=[];frozen=[]
for n in range(1,31):
 f=P/'reassembled'/f'slide_{n:02}.html';d=html.fromstring(f.read_text());before=[e.get('style') for e in d.xpath('//div[@class="body"]/*')];body=d.xpath('//div[@class="body"]');roots=list(body[0]) if body else[];ids=IDENT[str(n)];assert len(roots)==len(ids),(n,len(roots),len(ids))
 # Restore original foundation text; remove invented title/footer where no original exists.
 head=d.xpath('//header[contains(concat(" ",normalize-space(@class)," ")," head ")]')
 if n not in [1,25] and head:
  h=head[0]
  if n==30:
   kick=next(iter(direct(h,'kicker')),None)
   for e in list(h):
    if e is not kick:h.remove(e)
   rich(kick,src(n,8))
  else:
   allparts=[]
   for j,e in enumerate(SLIDE[n]):
    st=e.get('style','');fs=re.search(r'font-size:([\d.]+)px',st);top=re.search(r'top:([\d.]+)px',st);left=re.search(r'left:([\d.]+)px',st)
    if fs and top and left and e.text_content().strip():allparts.append((float(fs[1]),float(top[1]),float(left[1]),e))
   title=next((e for fs,y,x,e in allparts if fs>=56 and y<220 and x<200),None)
   kicker=next((e for fs,y,x,e in allparts if fs<=24 and y<140 and x<200),None)
   number=next((e for fs,y,x,e in allparts if y<140 and x>1100 and re.fullmatch(r'\d{2}',e.text_content().strip())),None)
   for c,s in [('title',title),('kicker',kicker),('no',number)]:
    a=next(iter(direct(h,c)),None)
    if a is not None:
     if s is not None:rich(a,s)
     else:h.remove(a)
 if n in [1,25]:
  lock=d.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," lockup ")]')[0]
  if n==1:
   rich(direct(lock,'kicker')[0],src(n,7));title=direct(lock,'title')[0];rich(title,src(n,8));br=html.Element('br');title.append(br);b=html.Element('b');rich(b,src(n,9));title.append(b)
   for e in direct(lock,'lead'):lock.remove(e)
   for e in d.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," meta ")]'):settext(e,src(n,10).text_content())
  else:
   rich(direct(lock,'kicker')[0],src(n,8));rich(direct(lock,'title')[0],src(n,9));rich(direct(lock,'lead')[0],src(n,10))
   for e in d.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," meta ")]'):e.getparent().remove(e)
 for e,id_ in zip(roots,ids):
  i=INDEX[id_];leaf=i['leaf'];r=rows(i);ns=[source_for(n,x) for x in r]
  if leaf=='headline':rich(e.xpath('./h2')[0],ns[0])
  elif leaf=='prose':
   pp=e.xpath('./p');assert len(pp)==len(ns),(n,id_,len(pp),len(ns))
   for p,s in zip(pp,ns):rich(p,s,strip_bullet=n==18)
  elif leaf in ['pill','tag']:
   dest=e.xpath('./div[@class="parts"]/*[contains(concat(" ",normalize-space(@class)," ")," name ")]') if leaf=='pill' else[e]
   rich(dest[0],ns[0])
  elif leaf=='agenda':
   entries=direct(e,'entry');pairs=[]
   for j in range(0,len(ns),2):pairs.append((ns[j],ns[j+1]))
   for a,(name,mark) in zip(entries,pairs):rich(direct(a,'name')[0],name);rich(direct(a,'mark')[0],mark)
  elif leaf=='card':
   p=direct(e,'parts')[0]
   if n==5:fields=['kick','name','note']
   elif n in [9,12]:fields=['fig','name','note']
   elif n==11:fields=['kick','name','note']
   elif n==21:fields=['mark','name','note']
   else:fields=['name','note']
   assert len(fields)==len(ns),(n,id_,fields,len(ns))
   for field,s in zip(fields,ns):rich(direct(p,field)[0],s)
  elif leaf=='pyramid':
   for a,s in zip(direct(e,'level'),ns):rich(direct(a,'name')[0],s)
  elif leaf=='hub':
   for a,s in zip(direct(e,'spoke'),ns[:4]):rich(direct(a,'name')[0],s)
   core=direct(e,'core')[0];rich(direct(core,'name')[0],ns[4]);rich((direct(core,'note') or core.xpath('./small'))[0],ns[5])
  elif leaf=='list':
   items=direct(e,'item')
   if n==8:
    for j,a in enumerate(items):rich(direct(a,'name')[0],ns[2*j]);rich(direct(a,'note')[0],ns[2*j+1])
   else:
    assert len(items)==len(ns),(n,id_)
    for a,s in zip(items,ns):name=direct(a,'name')[0];rich(name,s);name.text=re.sub(r'^\s*•\s*','',name.text or '')
  elif leaf=='funnel':
   for a,s in zip(direct(e,'stage'),ns):
    t=s.text_content().strip().split();settext(direct(a,'name')[0],' '.join(t[:-1]));settext(direct(a,'fig')[0],t[-1])
  elif leaf=='steps':
   for j,a in enumerate(direct(e,'step')):
    rich(direct(a,'mark')[0],ns[j*3],keep_icon=n==13);rich(direct(a,'name')[0],ns[j*3+1],keep_icon=n==10);rich(direct(a,'note')[0],ns[j*3+2])
   names={10:['target','lightbulb','search','chart-no-axes-combined'],13:['lightbulb','search','credit-card','message-circle']}.get(n)
   if names:
    for a,name in zip(direct(e,'step'),names):
     icon=a.xpath('.//*[@data-icon]')
     if icon:icon[0].set('data-icon',name)
  elif leaf=='image-frame':
   for seat in direct(e,'seat'):seat.set('data-ph','')
  elif leaf=='table':
   ordered=sorted(r,key=lambda v:(round(v['bbox'][1]/4),v['bbox'][0]));cells=e.xpath('.//th|.//td');assert len(cells)==len(ordered),(n,id_,len(cells),len(ordered))
   for a,z in zip(cells,ordered):rich(a,source_for(n,z))
  elif leaf=='versus':
   sides=direct(e,'side');names=[z for z in r if not z['text'].lstrip().startswith('•')];bullets=[z for z in r if z['text'].lstrip().startswith('•')]
   for j,a in enumerate(sides):
    rich(direct(a,'name')[0],source_for(n,names[j]));lis=a.xpath('./*[@data-el="crossrail-list"]')[0]
    for item,z in zip(direct(lis,'item'),bullets[j*3:j*3+3]):v=direct(item,'name')[0];rich(v,source_for(n,z));v.text=re.sub(r'^\s*•\s*','',v.text or '')
   settext(direct(e,'vs')[0],'')
  elif leaf=='chart-bar':
   labels=[s for s in ns if re.fullmatch(r'[1-4]분기',s.text_content().strip())]
   for bar,s in zip(direct(e,'bar'),labels):rich(bar.xpath('./span')[0],s)
  elif leaf=='metric':
   p=direct(e,'parts')[0];rich(direct(p,'name')[0],ns[0]);rich(direct(p,'fig')[0],ns[1]);rich(direct(p,'note')[0],ns[2])
  elif leaf=='chart-line':
   labels=[e_ for e_ in SLIDE[n] if re.fullmatch(r'[월화수목금토일]요일',e_.text_content().strip())]
   for pt,s in zip(direct(e,'pt'),labels):rich(pt.xpath('./span')[0],s)
  elif leaf=='legend':
   for j,a in enumerate(direct(e,'key')):
    clear(a);a.text=ns[2*j].text_content()+' ';b=html.Element('b');rich(b,ns[2*j+1]);a.append(b)
  elif leaf=='roadmap':
   heads=direct(e,'heads')[0]
   for a,s in zip(heads, [src(n,x) for x in [10,11,12,13]]):rich(a,s)
   lane_source=[[22],[23,24],[25],[26]]
   for j,a in enumerate(direct(e,'lane')):
    rich(direct(a,'name')[0],src(n,[15,17,19,21][j]));bars=direct(a,'bar')
    for b in bars:a.remove(b)
    for idx in lane_source[j]:
     s=src(n,idx);st=s.get('style');x=float(re.search(r'left:([\d.]+)px',st)[1]);w=float(re.search(r'width:([\d.]+)px',st)[1]);kind='tone-3' if idx==22 else 'on' if idx in [23,26] else 'tone-2';b=html.Element('div',{'class':'bar '+kind,'style':f'--from:{(x-275)/227:.12g};--to:{(x+w-275)/227:.12g}'});span=html.SubElement(b,'span') if hasattr(html,'SubElement') else etree.SubElement(b,'span');rich(span,s);a.append(b)
  elif leaf=='timeline':
   for j,a in enumerate(direct(e,'stop')):
    rich(direct(a,'kick')[0],ns[j*3]);rich(direct(a,'name')[0],ns[j*3+1]);rich(direct(a,'note')[0],ns[j*3+2])
  elif leaf=='positioning':
   for a,t in zip(direct(e,'axis-x')[0],['불안정','안정']):settext(a,t)
   for a,t in zip(direct(e,'axis-y')[0],['느림','빠름']):settext(a,t)
   labels=sorted([s for s in ns if re.fullmatch(r'버전 \d',s.text_content().strip())],key=lambda s:int(s.text_content().strip()[-1]))
   for a,s in zip(direct(e,'mark'),labels):rich(direct(a,'name')[0],s)
  else:raise ValueError((n,id_,leaf))
  changed.append([n,id_,leaf])
 after=[e.get('style') for e in d.xpath('//div[@class="body"]/*')];assert before==after,('grid modified',n);frozen.append({'page':n,'styles':before})
 f.write_text('<!doctype html>'+html.tostring(d,encoding='unicode')+'\n')
(P/'map.json').write_text(json.dumps(M,ensure_ascii=False,indent=2)+'\n')
(P/'original-restoration-log.json').write_text(json.dumps({'restored':changed,'gridStylesUnchanged':frozen,'policy':'Original replica text/data in assemblies; new business copy remains only in fixtures. No element CSS changed by this script.'},ensure_ascii=False,indent=2)+'\n')
print('restored pages30 roots',len(changed),'all grid styles unchanged')
