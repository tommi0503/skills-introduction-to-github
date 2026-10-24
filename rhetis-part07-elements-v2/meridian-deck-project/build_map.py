from pathlib import Path
import json,re
P=Path(__file__).parent;raw=json.loads((P/'map-measurements.json').read_text());pages=[];gaps=[]
def union(parts):
 bs=[p['inkBBox'] or p['bbox'] for p in parts if p['bbox']['w'] and p['bbox']['h']];x=min(b['x'] for b in bs);y=min(b['y'] for b in bs);r=max(b['x']+b['w'] for b in bs);b=max(b['y']+b['h'] for b in bs);return {k:round(v,2) for k,v in dict(x=x,y=y,w=r-x,h=b-y).items()}
for rr in raw['pages']:
 n=rr['page'];parts={p['index']:p for p in rr['parts']};used=set();instances=[];furniture=[]
 def add(ids,leaf,name,variant='base',why=None,kind='element',nested=None):
  ids=list(ids) if not isinstance(ids,int) else [ids];xs=[parts[i] for i in ids];duplicate=used.intersection(ids)
  if duplicate:raise ValueError((n,duplicate))
  used.update(ids);item={'id':f'p{n:02d}-{len(instances)+len(furniture)+1:02d}','name':name,'kind':kind,'status':'unexpressible' if why else ('mapped' if kind=='element' else 'foundation'),'bbox':union(xs),'leaf':leaf,'variant':variant,'parts':[x['id'] for x in xs],'selectors':[f'main.slide > :nth-child({i})' for i in ids],'sourceMeasurements':[{k:x[k] for k in ['id','index','bbox','inkBBox','font','paint','text']} for x in xs]}
  if leaf and kind=='element' and not why:item['fixture']=f'elements/{leaf}/fixtures/replica-{n:02d}.html'
  if why:item['why']=why;gaps.append({'page':n,**item})
  if nested:item['nestedContracts']=nested
  (instances if kind=='element' or why else furniture).append(item);return item
 def a(ids,l,name,v='base',**kw):return add(ids,l,name,v,**kw)
 def f(ids,name,v='base'):return add(ids,None,name,v,kind='furniture')
 if n==1:
  f(range(1,4),'Opening lockup','cover.at-top-left');f(range(4,11),'Graphic background with three icon medallions','cover.deco');f(range(11,14),'Cover metadata rail','cover.meta')
 elif n==30:
  f(range(1,5),'Closing lockup','cover.at-center');f(range(5,12),'Map placeholder and three icon medallions','cover.deco');f(range(12,15),'Closing metadata band','cover.meta')
 else:
  idx=list(range(2,9)) if n==4 else list(range(3,10)) if n==7 else list(range(1,7)) if n==3 else list(range(1,8))
  for i in idx:
   if parts[i]['bbox']['h']==0:used.add(i);continue
   label=('Brand line' if 'BUSINESS PROJECT' in parts[i]['text'] else 'Footer' if 'PRESENTATION' in parts[i]['text'] else 'Page title' if parts[i]['bbox']['y']==98 else 'Page subtitle' if parts[i]['bbox']['y']==118 else 'Top rule' if parts[i]['bbox']['y']==49 else 'Bottom rule' if parts[i]['bbox']['y']==677 else 'Headline rail')
   f([i],label,'page-furniture')
  if n==2:a(range(8,29),'agenda','Nine agenda entries and three row rules')
  elif n==3:f(7,'World map placeholder','seat.back');a([8,9],'headline','Section number and large title','big.center');a(10,'prose','Section introduction','lead');a(11,'prose','Secondary caption','quiet')
  elif n==4:
   f(1,'Full-height supporting rail','rail');a([9,10,11],'person','Portrait and attribution');
   for i in [12,14,16,18]:a([i,i+1],'prose','Executive message paragraph')
  elif n==5:
   f(8,'World map placeholder','seat.back');a([9,10,11,13,14,15,17,18,19],'card','Three vision discs','on');a([12,16],None,'Addition operators between vision cards',why='The operators add three peer concepts. No existing contract owns a row of cards and mathematical operators; versus denotes comparison, not addition.');a(20,'headline','Vision label');a(21,'prose','Supporting vision copy')
  elif n==6:
   f(8,'Project photograph placement','seat');a(9,'prose','Photo caption','quiet')
   for i in [10,17,24]:a([i,i+1],'headline','Numbered analysis heading');a(i+2,'prose','Analysis paragraph')
   a([13,14,15,16,20,21,22,23,27,28,29,30],'pill','Six paired emphasis capsules','on')
  elif n==7:f([1,2],'Full-page photographic seat and diagonal accent plane','slide.on');a(10,'headline','Opening statement','big.on');a([11,12],'prose','Two explanatory paragraphs')
  elif n==8:f([8,9,10,11],'Two overlapping circular photo placements','seat.back.avatar');a(range(12,27),'list','Three numbered gray rows','num.divided')
  elif n==9:a(range(8,32),'card','Four icon medallion cards','on')
  elif n==10:a(range(8,28),'hub','Photographic core with three annotated spokes')
  elif n==11:
   a(range(8,20),'card','Two labelled insight panels','line.on',nested=['list']);a([20,21],'pill','Chart caption','on');a([22,23,24,25],'legend','Two series keys');a(26,'prose','Chart unit','quiet');a(range(27,48),None,'Paired bars with four shared quarter labels',why='chart.bar assigns one axis label per bar. This reference has eight values grouped under four shared category labels; representing the paired category axis needs a group part rather than blank labels or inferred sibling pairing.')
  elif n==12:a(range(8,24),'matrix','Four interlocking SWOT petals and complete notes','swot',nested=['list'])
  elif n==13:
   a(8,'headline','Two-line strategic statement','center');a(range(9,15),'card','Two icon strategy panels','on');a(15,None,'Many-to-many strategy connector',why='One broad upward arrow relates three lower execution areas to two upper goals. Flowchart directional classes cannot encode this shared many-to-many junction without a connector/junction part.');a(range(16,28),'card','Three softly headed action panels','line',nested=['list'])
  elif n==14:a(8,'headline','Introductory statement','big');a(9,'prose','Chart context');a(range(10,51),None,'Fifteen-observation filled time series',why='chart.area@1 permits only 3–12 points per series. This chart has 15 observations and 15 labels. Splitting the continuous series between roots would divide ownership of its single connected path.')
  elif n==15:a([8,9,10],'headline','Three organisation column headings');a(range(11,42),'hierarchy','Vision to two strategies and six actions',nested=['root','branch.node','branch.leaf'])
  elif n==16:a(range(8,22),'card','Three media-led analysis rows','base / line',nested=['seat'])
  elif n==17:
   a(8,'headline','Outcome statement','center');a(range(9,15),'pill','Three comparison row labels','on / quiet / base');a(range(15,54),'card','Three complete project panels','line.on',nested=['list','chart-line'])
  elif n==18:a(range(8,55),'hub','Central photographic core and four ruled descriptions')
  elif n==19:a([8,9],'headline','Two section labels');a(range(10,22),'card','Four neutral sales strategy cards');a(range(22,73),'table','Funding table with capsule row headers')
  elif n==20:
   a(8,'headline','Problem and improvement statement','center');a([9,10,11,16,17,18,23,24,25],'card','Three compact icon problem cards','on');a([12,13,14,15,19,20,21,22,26,27,28],'delta','Three issue-to-improvement comparisons')
  elif n==21:a(8,'table','Six-column budget table')
  elif n==22:a(8,'headline','Operational improvement statement','center');a(range(9,26),None,'Four-sector open fan with category badges',why='The sectors categorise four independent topics. It is neither a cyclic process nor SWOT, shares, inclusion, nor overlap. Current taxonomy has no independent fan-sector/category diagram contract.')
  elif n==23:a(range(8,48),'timeline','Five alternating circular milestones','alt')
  elif n==24:a([8,9],'pill','Long conclusion capsule','on');f(10,'Supporting photograph placement','seat');a(range(11,31),'card','Three action rows with full narrative and paired bullets','base / line',nested=['list'])
  elif n==25:
   a([8,9],'pill','Quadrant caption','on');a([10,11,12,13,14,15,18,34,35,36,37,38,39,40,41],'positioning','Four labelled ideas on two decision axes');a([16,17],'prose','Explicit axis names','quiet');a(range(19,34),'list','Four category capsules with nested action lists','divided',nested=['list'])
  elif n==26:a(8,'headline','Performance statement','center');a([9,10,15,16,21,22,27,28],'legend','Four categorical caption capsules');a([11,17,23,29],'prose','Four short business explanations','quiet');a([12,13,14,18,19,20,24,25,26,30,31,32],'chart-donut','Four shares with distinct emphasis')
  elif n==27:a([8,9,10,11,16,17,18,19,24,25,26,27],'image-frame','Three inset picture frames with plus medallions');a([12,13,14,15,20,21,22,23,28,29,30,31],'card','Three photo descriptions with title rules','line')
  elif n==28:
   a(range(8,15),None,'Phase span annotation above a four-step process',why='The two phase labels span respectively three and one process stages along one connected rail. steps has no phase-span part; roadmap requires multiple duration lanes, which this single process grouping is not.');a(range(15,56),'steps','Four connected chevrons and complete execution panels',nested=['list','delta','pill','hierarchy']);a([56,57],'callout','Investment and expected impact conclusion')
  elif n==29:a(8,'headline','Team introduction','center');a(9,'prose','Sample image note','quiet');a(range(10,26),'person','Four team profiles with names and role notes')
 missing=set(parts)-used
 if missing:raise ValueError(('unmapped',n,missing))
 # The canvas is a visible full-page surface even when no explicit DOM node paints it.
 furniture.insert(0,{'id':f'p{n:02d}-canvas','name':'Page ground','kind':'background','status':'foundation','bbox':{'x':0,'y':0,'w':1280,'h':720},'leaf':None,'variant':'page','parts':[],'selectors':['main.slide'],'sourceMeasurements':[]})
 pages.append({'page':n,'source':rr['source'],'canvas':{'w':1280,'h':720},'furniture':furniture,'instances':instances,'coverage':{'sourceParts':len(parts),'assignedParts':len(used),'unassigned':[]}})
obj={'schema':'rhetis.source-element-map/2','collection':'meridian-deck','units':'px','coordinateSystem':'1280×720 top-left; bbox is the union of actual visible text/shape bounds','measurementFile':'map-measurements.json','pages':pages}
# Flat tool-facing instances retain page ownership and an explicit named contract use.
flat=[]
for page in pages:
 for unit in page['instances']+page['furniture']:
  b=unit['bbox'];unit['bounds']=b;unit['bbox']=[b[k] for k in ['x','y','w','h']];unit['page']=page['page'];unit['use']='unexpressible' if unit['status']=='unexpressible' else ('base' if unit['variant']=='base' else 'variant:'+unit['variant']) if unit['leaf'] else 'foundation:'+unit['variant'];flat.append(unit)
# Child charts/lists remain autonomous leaves inside the mapped cards or steps.
for page_no,leaf,ids,name,variant in [(11,'list',[13,19],'Insight panel bullet lists','base'),(13,'list',[19,23,27],'Three action lists','base'),(17,'list',[21,34,47],'Project results lists','base'),(17,'chart-line',[23,24,25,26,27,36,37,38,39,40,49,50,51,52,53],'Three miniature quarter trends','base'),(28,'list',[18,26,34,40],'Process panel action lists','base'),(28,'delta',[19,20,21,22,45],'Site count change','base'),(28,'pill',[27,28,29,30,41,42,43,44],'AI and delivery capsules','base'),(28,'hierarchy',[35,36,46,47,48,49,50,51,52,53,54,55],'Carrier and three subordinate partners','base')]:
 rr=raw['pages'][page_no-1];xs=[x for x in rr['parts'] if x['index'] in ids];b=union(xs);parent=next(u['id'] for u in pages[page_no-1]['instances'] if all(x['id'] in u['parts'] for x in xs));u={'id':f'p{page_no:02d}-nested-{leaf}','page':page_no,'name':name,'kind':'element','status':'mapped','leaf':leaf,'variant':variant,'use':'base' if variant=='base' else 'variant:'+variant,'bbox':[b[k] for k in ['x','y','w','h']],'bounds':b,'parent':parent,'parts':[x['id'] for x in xs],'fixture':f'elements/{leaf}/fixtures/replica-{page_no:02d}.html','sourceMeasurements':[{k:x[k] for k in ['id','index','bbox','inkBBox','font','paint','text']} for x in xs]};flat.append(u);pages[page_no-1]['instances'].append(u)
obj['instances']=flat
(P/'map.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2))
lines=['# Gaps in the current element contracts','','Only genuinely unexpressible reference units are listed. Existing components remain mapped separately.']
proposals={5:'`<div class="sum"> <div class="term">…card…</div> ×3 </div>`; the sum root owns the plus operators.',11:'`<div class="bars grouped"><div class="group"><span class="name">category</span><div class="bar">…</div> ×2</div> ×4</div>`; the group owns one shared axis label.',13:'`<div class="strategy-flow"><div class="goals">…</div><div class="junction"></div><div class="actions">…</div></div>`; one owner connects both sets.',14:'Keep `.areas > .series > .pt` markup and extend the allowed observation count from12 to15 or24.',22:'`<div class="fan"><div class="sector"><b class="mark">…</b><b class="name">…</b><p class="note">…</p></div> ×4</div>`; sectors have no arrows or cycle semantics.',28:'Add `<div class="phase" style="--from:0;--to:3">…</div>` parts to `.steps`; the steps root owns the continuous phase rail.'}
for g in gaps:lines+=['',f'## Page {g["page"]:02d}: {g["name"]}',g['why'],'',f'Needed markup/contract: {proposals[g["page"]]}',f'Bounding box: `{g["bbox"]}`.']
(P/'GAPS.md').write_text('\n'.join(lines)+'\n')
print('Map complete:',len(pages),'pages,',sum(len(x['parts']) for x in raw['pages']),'source parts,',sum(len(p['instances']) for p in pages),'element units,',len(gaps),'honest gaps')
