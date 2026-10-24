"""New v2 source preparation: replica measurements and contract markup only.
Does not read or import any previous element CSS. Replica files are read-only.
"""
from pathlib import Path
from lxml import html,etree
import re,json,copy
P=Path(__file__).parent;REF=Path('/workspace/work/reference');K=P/'vectorbox';K.mkdir(exist_ok=True)
def props(e):return dict(x.split(':',1) for x in e.get('style','').split(';') if ':' in x)
def num(v):
 m=re.match(r'(-?[\d.]+)',v or '0');return float(m[1]) if m else 0
raw={};roots={};texts=[]
for p in sorted((P/'replica').glob('slide_*.html')):
 n=int(p.stem[-2:]);root=html.fromstring(p.read_text());roots[n]=root;raw[n]=[]
 for i,e in enumerate(root.xpath('//section/*'),1):
  s=props(e);t=' '.join(e.text_content().split());texts.append(t)
  raw[n].append({'id':f'{n:02}-raw-{i:02}','selector':f'.slide > :nth-child({i})','bbox':[num(s.get(k)) for k in ['left','top','width','height']],'class':e.get('class',''),'text':t,'sourceMeasurements':{'fontSize':s.get('font-size'),'weight':s.get('font-weight'),'lineHeight':s.get('line-height'),'tracking':s.get('letter-spacing'),'svgCount':len(e.xpath('.//*[local-name()="svg"]'))}})
instances=[];assigned={n:set() for n in raw}
def add(n,label,indices,leaf,use='base',variant=None,suffix='',why=None):
 o=[raw[n][i-1] for i in indices];x=min(t['bbox'][0] for t in o);y=min(t['bbox'][1] for t in o);r=max(t['bbox'][0]+t['bbox'][2] for t in o);b=max(t['bbox'][1]+t['bbox'][3] for t in o)
 fixture=(f'elements/{leaf}/fixtures/replica-{n:02}{suffix}.html' if leaf else None)
 item={'id':f'{n:02}-{label}','page':f'{n:02}','leaf':leaf,'use':use,'variant':variant,'bbox':[x,y,r-x,b-y],'fixture':fixture,'selectors':[t['selector'] for t in o],'sourceObjectIds':[t['id'] for t in o],'sourceMeasurements':o}
 if why:item['why']=why
 instances.append(item);assigned[n].update(indices)
for n in raw:
 instances.append({'id':f'{n:02}-background','page':f'{n:02}','leaf':None,'use':'background','bbox':[0,0,1280,720],'fixture':None,'selectors':['.slide'],'sourceMeasurements':{'surface':'uniform page'}})
 add(n,'head',[1,2] if n==13 else [1,2,3],None,'furniture')
 for i,o in enumerate(raw[n],1):
  if 'dots' in o['class']:add(n,'index',[i],None,'furniture')
add(2,'contents',list(range(4,20)),'agenda')
for i in [20,21]:add(2,f'decor-{i}',[i],None,'furniture')
add(3,'lead',[5],None,'furniture')
for j in range(4):add(3,f'outline-{j+1}',list(range(6+3*j,9+3*j)),'card','variant:.line' if j==0 else 'same-as:03','.line')
add(4,'legend',list(range(5,9)),'legend')
add(4,'grouped-chart',list(range(9,33)),'chart-bar','unexpressible',why='Flat bar contract has one value and one label per member. The replica groups two series under each year and supplies a separate numeric y-axis; no grouped category or explicit axis markup is defined.')
for j,ids in enumerate([[33],[36]]):add(4,f'burst-{j+1}',ids,'card','variant:.on' if j==0 else 'same-as:04','.on','-on')
for j,ids in enumerate([[34,35],[37,38]]):add(4,f'caption-{j+1}',ids,'card','variant:.line' if j==0 else 'same-as:03','.line','-line')
for j in range(4):add(5,f'ring-{j+1}',list(range(5+3*j,8+3*j)),'card','variant:.quiet' if j==0 else 'same-as:05','.quiet')
add(6,'hub',list(range(5,19)),'hub')
add(7,'comparison',[5],'table')
for j in range(4):add(8,f'result-{j+1}',list(range(5+4*j,9+4*j)),'card','base' if j==0 else 'same-as:08')
add(9,'sequence',list(range(5,34)),'steps')
add(10,'budget-ring',[5],'chart-donut','unexpressible',why='The source is a six-sector ring with six independent category shares. chart.donut defines one share and donuts defines a row, not a multi-sector ring. Overlapping independent roots would change the semantic model.')
add(10,'coins',[6],'card','base',suffix='-mark')
add(10,'budget-legend',list(range(7,19)),'legend','same-as:04')
add(10,'budget-card',list(range(19,23)),'card','base',suffix='-text')
add(11,'conversation',[6,7,8],'callout')
add(11,'microphone',[9],'card','same-as:10',suffix='-mark')
for i in [4,5]:add(11,f'decor-{i}',[i],None,'furniture')
add(12,'representative',list(range(4,9)),'card','variant:.line','.line')
add(12,'contacts',list(range(9,27)),'list','variant:.divided','.divided')
add(13,'statement',[3,4,5],'headline','variant:.big','.big')
for i in [6,7,8]:add(13,f'decor-{i}',[i],None,'furniture')
for i in [9,10]:add(13,f'photo-{i}',[i],'image-frame','base' if i==9 else 'same-as:13')
add(13,'footer',[11],'prose','variant:.quiet','.quiet')
assert all(assigned[n]==set(range(1,len(v)+1)) for n,v in raw.items())
mapping={'schema':'rhetis.replica-map/2','collection':'vectorbox','canvas':[1280,720],'source':'replica (immutable)','pages':[{'page':f'{n:02}','source':f'replica/slide_{n:02}.html','sourceObjectCount':len(v),'visibleObjects':v} for n,v in raw.items()],'instances':instances,'coverage':{'replicaVisibleObjects':sum(map(len,raw.values())),'backgrounds':len(raw),'unassigned':0}}
(P/'map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
gaps=[i for i in instances if i['use']=='unexpressible'];(P/'GAPS.md').write_text('# Unexpressible source structures\n\n'+''.join(f"- Page {i['page']} / {i['id']}: {i['why']} Needed markup: "+('a category group containing two series bars, explicit axis ticks and per-bar annotation control.\n' if i['leaf']=='chart-bar' else 'a donut root with a list of labeled segments and numeric segment values.\n') for i in gaps))
# Shared values derived from replica: 12/24/36 spacing, square selection frames,
# 60/26/22 typography, Montserrat kicker and Pretendard body.
kitvals={'--page':'#ffffff','--ink':'#000000','--font-display':"'Pretendard Variable'",'--font-body':"'Pretendard Variable'",'--weight-display':'850','--weight-body':'450','--tracking-display':'-.025em','--radius':'0px','--radius-sm':'6px','--stroke':'1px','--text-min':'14px','--margin-x':'76px','--margin-y':'60px','--gap':'24px','--gap-sm':'12px','--gap-lg':'36px','--pad':'24px','--furn-edge':'62px','--top-h':'44px','--foot-h':'32px','--furn-gap':'12px','--rail-w':'8px','--rail-gap':'28px','--title-weight':'850','--title-line':'1.15','--title-track':'-.025em','--lead-weight':'450','--lead-line':'1.4','--lead-track':'-.015em','--figure-weight':'700','--figure-line':'1','--figure-track':'0em','--name-weight':'650','--name-line':'1.2','--name-track':'-.02em','--body-weight':'450','--body-line':'1.35','--body-track':'-.015em','--label-weight':'600','--label-line':'1.2','--label-track':'0em','--label-track-latin':'0em','--vectorbox-font-latin':"'Montserrat'",'--vectorbox-font-code':"'Nanum Gothic Coding'"}
(K/'kit/css').mkdir(parents=True,exist_ok=True);(K/'kit/css/tokens.css').write_text('.slide{'+''.join(f'{k}:{v};' for k,v in kitvals.items())+'}\n.slide.dark{--page:#111111;--ink:#f7f7f7}\n')
(K/'kit/kit.json').write_text(json.dumps({'schema':'rhetis.kit/2','id':'vectorbox','label':'Vectorbox','tokens':'css/tokens.css','description':'Selection outlines, circular line icons and heavy editorial type.','extensions':{'--vectorbox-font-latin':'font','--vectorbox-font-code':'font'}},indent=2))
(K/'kit/description.md').write_text('A precise editing-selection language: hairline rectangular borders, four compact corner handles, large circular marks and heavy sans-serif headings. Open page areas and repeated modular spacing keep attention on one clear accent.\n')
# Contract markup only, never sample CSS.
golden={'card':('confetti',['card-2-quiet','card-3-icon3d','card-3-line','card-3-on','card-4','card-5-tone']),'callout':('annual',['callout','callout-icon','callout-stack']),'chart-area':('annual',['area-1','areas-2','areas-stacked-3','area-3pt']),'chart-bar':('confetti',['bars-12','bars-6','bars-3','bars-h-5','bars-h-8','bars-2']),'chart-donut':('amethyst',['donut','donuts-3','donuts-4','donut-0','donut-100']),'chart-line':('amethyst',['lines-12','lines-3','lines-6','lines-flat'])}
allsource=''.join(re.sub(r'\W','',x).lower() for x in texts)
gram={allsource[i:i+6] for i in range(len(allsource)-5) if re.search('[가-힣]',allsource[i:i+6])}
names=['물류망 재편','권한별 승인','납품 오차 축소','신규 매장 실험','재고 경보 체계','교육 이력 연동','수출 계약 갱신','채권 회수 점검','주문 배정 규칙','납기 위험 탐지','지점별 손익 진단','원가 배분 개선']
notes=['발주 기록과 납품 이력을 묶어 누락된 거래를 찾습니다.','점검 담당자에게 변경 이력을 전달하고 승인 시간을 줄입니다.','지점마다 다른 기준을 맞춘 뒤 다음 분기 예산을 정합니다.','계약 갱신 기한이 다가오면 담당 부서에 먼저 알립니다.']
changes=[]
def rename(text,fresh=False):
 text=re.sub(r'data-el="[^"-]+-', 'data-el="vectorbox-', text)
 # Prefixes can contain hyphens; replace using the original known source ids.
 for col in ['annual','confetti','amethyst']:text=text.replace('data-el="'+col+'-','data-el="vectorbox-')
 root=html.fragment_fromstring(re.sub(r'^<!--.*?-->','',text,count=1,flags=re.S),create_parent='div')
 if fresh:
  for j,e in enumerate(root.iter()):
   if e.tag=='div' and e is root:continue
   cl=set(e.get('class','').split())
   if ('name' in cl or 'kick' in cl or 'note' in cl) and len(e)==0:
    e.text=(notes[j%len(notes)] if 'note' in cl else names[j%len(names)])
 # Preserve golden DOM and values; replace only source-overlapping prose.
 for e in root.iter():
  if e.text and any(g in re.sub(r'\W','',e.text).lower() for g in gram):
   before=e.text;e.text=notes[len(changes)%len(notes)] if len(before)>14 else names[len(changes)%len(names)];changes.append({'old':before,'new':e.text})
 out=''.join(etree.tostring(e,encoding='unicode',method='html') for e in root)
 # Default fixtures have one normalized top-level body child.
 return out
for folder in sorted((REF/'samples/annual/elements').iterdir()):
 leaf=folder.name;dest=K/'elements'/leaf;(dest/'fixtures').mkdir(parents=True,exist_ok=True)
 meta=json.loads((folder/'element.json').read_text());meta['registrations']={};meta['tokenDefaults']={};(dest/'element.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
 sample=sorted((folder/'fixtures').glob('*.html'))
 for j in range(2):
  src=sample[j%len(sample)].read_text();mini=re.match(r'<!--.*?-->',src,re.S)[0];new=rename(src,True)
  # Honest broad minimum initially; size review can lower it after direct renders.
  (dest/'fixtures'/('base-short.html' if j==0 else 'base-long.html')).write_text('<!-- min: 6x3 -->\n'+new+'\n')
 if leaf in golden:
  col,files=golden[leaf]
  for name in files:
   src=(REF/'samples'/col/'elements'/leaf/'fixtures'/(name+'.html')).read_text();mini=re.match(r'<!--.*?-->',src,re.S)[0];(dest/'fixtures'/(name+'.html')).write_text(mini+'\n'+rename(src)+'\n')
 (dest/'description.md').write_text(f'The {leaf} uses a single scalable Vectorbox construction: hairline geometry, circular emphasis and aligned sans-serif type. Contract variants change their stated emphasis or direction, while the same rules govern all fixture content.\n')
(P/'fixture-text-replacements.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
print('Map complete:',mapping['coverage'],'unexpressible:',len(gaps),'gold text replacements:',len(changes))
