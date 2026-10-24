from pathlib import Path
import json
P=Path(__file__).parent;raw=json.loads((P/'source-measurements.json').read_text())
# Explicit roots inferred from measured source blocks, never from the discarded collection CSS.
# page, leaf, use, bbox, id, optional contract limitation.
D={
2:[('agenda','base',[464,343,632,312],'contents')],
3:[('headline','base',[123,239,1029,99],'statement'),('prose','base',[123,379,475,220],'left-copy'),('prose','base',[640,379,518,220],'right-copy')],
4:[('table','base',[95,381,871,274],'company-fields')],
5:[('card','variant:quiet',[291,98,856,524],'vision-columns')],
6:[('pill','base',[95,263,98,391],'levels-labels'),('pyramid','base',[196,262,543,392],'four-levels'),('prose','base',[773,288,412,340],'level-descriptions')],
7:[('card','variant:quiet',[95,260,307,395],'left-explanations'),('hub','base',[426,343,426,231],'semicircle'),('card','variant:quiet',[877,260,307,395],'right-explanations')],
8:[('list','variant:divided',[95,268,650,387],'three-notes'),('funnel','base',[729,260,455,395],'three-stages')],
9:[('card','base',[95,260,1090,395],'four-figures')],
10:[('headline','base',[95,261,1080,35],'section-statement'),('steps','base',[95,320,1096,337],'joined-four')],
11:[('card','variant:line',[95,260,1130,395],'business-panels')],
12:[('card','variant:line',[95,260,1090,245],'letter-columns'),('list','base',[95,541,1090,113],'column-bullets')],
13:[('headline','base',[95,264,1090,35],'process-caption'),('steps','variant:col',[95,313,1090,340],'icon-column')],
14:[('steps','base',[95,260,1090,170],'forward-three'),('steps','unexpressible',[95,486,1090,168],'reverse-three','The sequence contract supplies horizontal and downward flow, but no reverse-flow variant. RTL text direction is not a visual design variant.')],
15:[('image-frame','base',[174,260,931,188],'three-pictures'),('tag','base',[320,260,784,42],'letter-badges'),('table','base',[95,472,1090,183],'equipment-fields')],
16:[('table','base',[95,260,1090,395],'specification-pair')],
17:[('card','variant:line',[95,260,1090,395],'four-market-panels'),('hub','unexpressible',[491,309,298,298],'central-icon-orbit','The source contains icon-only nodes without member names or notes. Empty semantic hub members would distort the contract.')],
18:[('card','variant:quiet',[95,279,307,376],'left-strengths'),('hub','unexpressible',[442,257,394,398],'pentagon','A pentagonal outline with icon-only vertices is a different hub design. The chosen base is an open semicircle; the hub contract has no polygon variant.'),('card','variant:quiet',[882,226,307,429],'right-strengths')],
19:[('versus','base',[95,260,1090,395],'training-impact')],
20:[('table','base',[95,260,567,218],'kpi-table'),('prose','variant:quiet',[95,506,567,148],'table-commentary'),('chart-bar','base',[722,260,462,395],'quarter-bars'),('chart-bar','unexpressible',[746,296,38,310],'numeric-axis','The bar contract has no explicit numeric-axis part. Its values and category labels do not encode independent tick labels.'),('table','unexpressible',[95,394,567,84],'highlighted-row','The source emphasizes a complete row, while table.pick denotes a column focus. A row-focus extension is required.')],
21:[('card','variant:on',[95,260,235,395],'rank'),('card','base',[368,260,817,395],'four-metrics')],
22:[('prose','base',[95,260,475,198],'trend-explanation'),('metric','base',[95,458,475,197],'maximum-figure'),('chart-line','base',[675,296,465,329],'weekly-line'),('chart-line','unexpressible',[610,341,52,251],'numeric-axis','The line contract has no numeric-axis markup; adding legend keys as tick labels would change their meaning.'),('chart-bar','unexpressible',[798,322,356,303],'background-columns','The two unlabeled background columns are a mixed-chart layer whose independent labels and values are not supplied by the source.')],
23:[('chart-bar','unexpressible',[95,260,1090,395],'annotated-comparison','A standard bar root cannot move its values into external text capsules or hide values while independent pills repeat them. An annotated-bar contract needs caption, unit and note parts.'),('headline','base',[621,284,526,60],'customer-inflow'),('prose','base',[621,534,244,98],'competitor-comment'),('prose','base',[902,534,244,98],'our-comment')],
24:[('legend','base',[95,260,507,213],'regional-shares'),('headline','base',[95,499,500,35],'regional-caption'),('prose','base',[95,550,539,101],'regional-commentary'),('chart-donut','unexpressible',[673,247,597,374],'multi-share-pie','A one-share donut does not encode five jointly partitioned segments or per-segment leaders. Transparent overlaid roots would fabricate a new contract design.')],
25:[],
26:[('prose','base',[95,263,1089,22],'schedule-introduction'),('headline','base',[95,310,170,25],'planning-caption'),('roadmap','base',[95,310,1090,345],'four-lanes'),('roadmap','unexpressible',[274,343,455,79],'first-underlay','Only the first and final durations carry a broad time rail. The supplied contract has no per-bar underlay flag.'),('roadmap','unexpressible',[729,575,455,80],'final-underlay','The time rail is a distinct source decoration requiring a contract variant, not a source-index condition.')],
27:[('pill','unexpressible',[95,261,545,86],'two-line-capsules','The pill contract is a one-line capsule; date and event are stacked in the source. A stacked-pill variant is required.'),('headline','base',[116,397,510,35],'management-caption'),('list','variant:check',[116,445,510,184],'management-checks'),('table','unexpressible',[662,260,523,395],'calendar','The calendar needs day-cell layout, a contiguous date-range highlight and event captions. These are not table column-pick semantics.')],
28:[('timeline','variant:alt',[95,264,1090,397],'quarter-milestones')],
29:[('positioning','base',[95,260,515,394],'version-map'),('positioning','unexpressible',[304,350,190,164],'progress-arrow','The positioning contract has point coordinates but no links or trajectory data. A relation part is required.'),('headline','base',[681,264,510,35],'stability-caption'),('prose','base',[681,310,510,50],'cluster-explanation'),('table','base',[681,398,504,257],'version-descriptions'),('table','unexpressible',[681,610,504,44],'highlighted-row','The complete final row is highlighted; column-pick cannot represent a row emphasis without changing its semantics.')],
30:[('table','base',[686,442,484,180],'contact-fields')]
}
inst=[];pageinfo=[]
for page in raw['pages']:
 n=page['page'];comps=[]
 for k,(leaf,use,bbox,name,*why) in enumerate(D.get(n,[])):
  obj={'id':f'p{n:02}-{name}','page':n,'leaf':leaf,'use':use,'bbox':bbox,'fixture':f'elements/{leaf}/fixtures/replica-{n:02}'+('' if sum(t[0]==leaf and t[1]!='unexpressible' for t in D.get(n,[]))<=1 else '-'+name)+'.html','sourceMeasurements':[]}
  if why:obj['why']=why[0];obj['fixture']=None
  inst.append(obj);comps.append(obj)
 for part in page['parts']:
  if not part['visible']:continue
  x,y,w,h=part['bbox'];cx=x+w/2;cy=y+h/2
  fits=[o for o in comps if o['bbox'][0]-3<=cx<=o['bbox'][0]+o['bbox'][2]+3 and o['bbox'][1]-3<=cy<=o['bbox'][1]+o['bbox'][3]+3 and w*h<=o['bbox'][2]*o['bbox'][3]*1.7]
  # Text in the page header remains foundation-owned even when broad boxes cross content columns.
  header=bool(part['text'].strip()) and y<240 and n not in [1,25,30]
  global_rule=not part['text'].strip() and (w>=1180 or h>=700 or (h<=2 and w>=600 and x<95))
  if fits and not header and not global_rule:
   best=min(fits,key=lambda a:a['bbox'][2]*a['bbox'][3]);best['sourceMeasurements'].append(part);part['owner']=best['id']
  else:
   role='header' if header else ('lockup' if n in [1,25,30] and part['text'].strip() and not any(o for o in comps if part in o['sourceMeasurements']) else 'furniture')
   ident=f'p{n:02}-{role}-{part["id"]}'
   obj={'id':ident,'page':n,'leaf':'foundation','use':'page-device','bbox':[max(0,x),max(0,y),min(w,1280-max(0,x)),min(h,720-max(0,y))],'fixture':None,'role':role,'sourceMeasurements':[part]};part['owner']=ident;inst.append(obj)
 pageinfo.append({'page':n,'source':page['source'],'sourceSha256':page['sha256'],'visibleCount':sum(x['visible'] for x in page['parts']),'mappedPartCount':sum(bool(x.get('owner')) for x in page['parts']),'type':('cover' if n in [1,25] else 'contact' if n==30 else 'content')})
basechoices={'agenda':2,'headline':10,'prose':3,'card':9,'pill':6,'pyramid':6,'hub':7,'list':8,'funnel':8,'steps':10,'image-frame':15,'tag':15,'table':16,'versus':19,'chart-bar':20,'chart-line':22,'legend':24,'roadmap':26,'timeline':28,'positioning':29,'metric':22}
M={'schema':'rhetis.reference-map/2','collection':'crossrail','viewport':[1280,720],'measurementMethod':'Actual Chromium boundingClientRect and computed typography from immutable source HTML. Every visible direct source child is assigned to one component or foundation page device.','pages':pageinfo,'baseChoices':basechoices,'instances':inst,'limitations':'Unsupported visual semantics are explicit gaps. Source-specific geometry variables, sibling selectors and fixture selectors are forbidden.'}
(P/'map.json').write_text(json.dumps(M,ensure_ascii=False,indent=2)+'\n')
gaps=[o for o in inst if o['use']=='unexpressible']
need={'reverse-three':'<div class="steps reverse">…</div>','central-icon-orbit':'<div class="hub icons"><div class="core">…</div><div class="spoke"><span class="icon" data-icon="…"></span></div></div>','pentagon':'<div class="hub polygon" style="--n:5">…named or icon-only nodes…</div>','multi-share-pie':'<div class="pie"><div class="seg tone-1" style="--v:20"><b>20</b><span class="name">…</span></div>…</div>','annotated-comparison':'<div class="bars annotated"><p class="name">…</p><div class="bar" style="--v:80"><b>80</b><span>…</span><small>…</small><p class="note">…</p></div></div>','calendar':'<div class="calendar"><div class="heads">…</div><div class="day on"><b>15</b><span class="note">…</span></div>…</div>','two-line-capsules':'<div class="pill stacked"><div class="parts"><p class="name">…</p><p class="note">…</p></div></div>','progress-arrow':'<div class="posmap"><div class="link" style="--x1:…;--y1:…;--x2:…;--y2:…"></div>…</div>'}
s=['# Crossrail contract gaps','', 'These source features have no semantically faithful expression in the supplied contract. They are documented rather than emulated through hidden values, empty members, unrelated contracts or page-specific CSS.','']
for g in gaps:
 key=g['id'].split('-',1)[1];markup=need.get(key,'A named axis/row-focus/underlay part must be added to the original contract; it must carry its own data and cannot be inferred from a source page number.')
 s+=['## '+g['id'],f'- Source page: {g["page"]}; bbox: `{g["bbox"]}`.',f'- Contract: `{g["leaf"]}`.',f'- Why: {g["why"]}',f'- Required markup: `{markup}`','']
(P/'GAPS.md').write_text('\n'.join(s)+'\n')
print('map pages',len(pageinfo),'instances',len(inst),'source nodes',sum(x['mappedPartCount'] for x in pageinfo),'gaps',len(gaps))
