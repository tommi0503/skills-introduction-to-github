from pathlib import Path
from lxml import html as LH
import json,re,html,math
P=Path(__file__).parent;C=P/'meridian-deck';M=json.loads((P/'map.json').read_text());RAW=json.loads((P/'map-measurements.json').read_text());S={pg['page']:{x['index']:x for x in pg['parts']} for pg in RAW['pages']}
# Reuse only the contractual component builders. No replica CSS is imported.
ns={'__file__':str(P/'write_replica_fixtures.py')};exec((P/'write_replica_fixtures.py').read_text().split('# Cards:')[0],ns)
ns['fresh']=lambda s:html.escape(s.strip());spec={}
def capture(leaf,n,body,mini='6x3',suffix=''):spec[(leaf,n,suffix)]=body
ns['save']=capture
ss=(P/'write_replica_fixtures.py').read_text();exec(ss[ss.index('# Cards:'):ss.index('# Source-specific named suffixes')],ns)
for fname,marker in [('fixtures_structures.py',"save('agenda'"),('fixtures_connected.py',"save('headline',12"),('fixtures_comparison.py',"# The reference")]:
 ss=(P/fname).read_text();exec(ss[ss.index(marker):],ns)
# Keep the source trend's unlabelled point markup and measured SVG scale.
for key in [('card',17,''),('chart-line',17,''),('table',17,'')]:
 tree=LH.fragment_fromstring(spec[key],create_parent='div')
 for e in tree.xpath('.//*[@data-el="meridian-deck-chart-line"]'):
  vals=[float(re.search(r'--v:([\d.]+)',x.get('style')).group(1)) for x in e.xpath('./div')];e.set('style','--max:'+str(max(vals)*1.25))
  for b in e.xpath('./div/b'):b.text=''
 spec[key]=''.join(LH.tostring(x,encoding='unicode') for x in tree)
# Explicit relationship between each map unit and one contract root in its specimen.
def choose(unit,pg,counters):
 leaf=unit['leaf'];fx=unit.get('fixture','');suf='-line' if '-13-line' in fx else '-quiet' if '-03-quiet' in fx else '-caption' if '-25-caption' in fx else ''
 body=spec.get((leaf,pg,suf))
 if body is None:
  # Nested units already belong to the whole card or process specimen.
  return None
 tree=LH.fragment_fromstring(body,create_parent='div');top=tree[0]
 key=(leaf,fx);nth=counters.get(key,0);counters[key]=nth+1
 same=[i for i in M['pages'][pg-1]['instances'] if i.get('leaf')==leaf and i.get('fixture')==fx]
 if len(same)>1 and top.get('data-el') is None:
  children=list(top)
  if nth<len(children):return LH.tostring(children[nth],encoding='unicode')
 return body
# Slot assignment is a direct, reproducible quantisation of measured source boxes.
# It does not alter any page or element CSS to chase reference coordinates.
def grid(box):
 x,y,w,h=box;cw=1164/12;rh=486/6
 c=max(1,min(12,round((x-58)/cw)+1));r=max(1,min(6,round((y-174)/rh)+1));ww=max(1,min(13-c,round(w/cw)));hh=max(1,min(7-r,round(h/rh)));return c,r,ww,hh


def placed(body,box):
 c,r,w,h=grid(box);t=LH.fragment_fromstring(body,create_parent='div');e=t[0];e.set('style',f'grid-column:{c} / span {w};grid-row:{r} / span {h}');return LH.tostring(e,encoding='unicode')
def original(pg,i):return html.escape(S[pg][i]['text'])
css=['../assets/fonts/fonts.css','../assets/type-steps.css','../meridian-deck/kit/css/tokens.css','../meridian-deck/foundation/foundation.css']+['../meridian-deck/elements/'+d.name+'/element.css' for d in sorted((C/'elements').iterdir())]+['../assets/source-palette.css']
head='<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>Measured component assembly</title>'+''.join('<link rel="stylesheet" href="'+x+'">' for x in css)+'<script defer src="../assets/lucide.min.js"></script><script defer src="../assets/render-icons.js"></script></head><body>'
out=P/'reassembled';out.mkdir(exist_ok=True);decisions=[]
for pg in range(1,31):
 page=M['pages'][pg-1];items=[];count={}
 if pg in [1,30]:
  cls='at-top-left' if pg==1 else 'at-center'
  title=original(pg,1)+'<br><b>'+original(pg,2)+'</b>' if pg==1 else original(pg,2)+'<br><b>'+original(pg,3)+'</b>'
  kick='' if pg==1 else '<p class="kicker">'+original(pg,1)+'</p>'
  lead=original(pg,3 if pg==1 else 4);meta='<span class="deck">'+original(pg,12 if pg==1 else 13)+'</span><span class="src">'+original(pg,13 if pg==1 else 14)+'</span>'
  body='<section class="slide cover"><div class="page"><div class="lockup '+cls+'">'+kick+'<h1 class="title">'+title+'</h1><p class="lead">'+lead+'</p></div><div class="deco'+(' on' if pg==30 else '')+'"><span class="label"><span class="icon" data-icon="folder-open"></span></span><span class="label"><span class="icon" data-icon="pencil"></span></span><span class="label"><span class="icon" data-icon="graduation-cap"></span></span></div><p class="meta'+(' on' if pg==30 else '')+'">'+meta+'</p></div></section>'
 else:
  for u in page['instances']:
   if pg==6 and u.get('leaf') in ['headline','prose','pill']:continue
   if pg==26 and u.get('leaf') in ['legend','prose']:continue
   if u.get('status')!='mapped' or u.get('kind')!='element' or 'nested' in u['id']:continue
   # These owned child elements are already included in their parent's contract root.
   if pg in [11,13,17,28] and u['leaf'] in ['list','chart-line'] :continue
   if pg==28 and u['leaf'] in ['delta','pill','hierarchy']:continue
   b=choose(u,pg,count)
   if not b:continue
   measures=u.get('sourceMeasurements',[]);boxes=[x['bbox'] for x in measures if x.get('bbox') and x.get('tag')!='svg']
   if boxes:
    x=min(z['x'] for z in boxes);y=min(z['y'] for z in boxes);xx=max(z['x']+z['w'] for z in boxes);yy=max(z['y']+z['h'] for z in boxes);box=[x,y,xx-x,yy-y]
   else:box=u['bbox']
   items.append(placed(b,box))
  if pg==26:
   selected=[u for u in page['instances'] if u.get('leaf') in ['legend','prose']]
   bs=[u['bbox'] for u in selected];x=min(b[0] for b in bs);y=min(b[1] for b in bs);right=max(b[0]+b[2] for b in bs);bottom=max(b[1]+b[3] for b in bs)
   items.append(placed('<div class="stack">'+spec[('legend',26,'')]+spec[('prose',26,'')]+'</div>',[x,y,right-x,bottom-y]))
  if pg==6:
   H=LH.fragment_fromstring(spec[('headline',6,'')],create_parent='div')[0]
   Q=LH.fragment_fromstring(spec[('prose',6,'')],create_parent='div')[0]
   T=LH.fragment_fromstring(spec[('pill',6,'')],create_parent='div')[0]
   rows=[]
   for j in range(3):
    hs=LH.tostring(H[j],encoding='unicode');qs=LH.tostring(Q[j+1],encoding='unicode');ps='<div class="group">'+''.join(LH.tostring(T[k],encoding='unicode') for k in [j*2,j*2+1])+'</div>'
    rows.append('<div class="stack">'+hs+qs+ps+'</div>')
   items.append(placed('<div class="stack">'+''.join(rows)+'</div>',[581,181,619,458]))
   items.append(placed(LH.tostring(Q[0],encoding='unicode'),[101,586,450,50]))
  # Foundation seats remain page devices; only scalar media positions occupy grid slots.
  for u in page['furniture']:
   if u.get('name','').lower().find('photo')>=0 or u.get('name','').lower().find('image')>=0 or u.get('name','').lower().find('map')>=0:
    # Skip the portrait, hub centre and frames, which are already owned by mapped roots.
    if pg in [4,7,8,10,18,27,29]:continue
    if u['bbox'][1]>=174:items.insert(0,placed('<div class="seat'+(' back' if 'map' in u.get('name','').lower() else '')+'" data-ph="1"></div>',u['bbox']))
  # Standard furniture uses the source wording, without ad-hoc geometric attributes.
  texts=[x for x in S[pg].values() if x['text'] and x['index']<10];title=next((x['text'] for x in texts if x['bbox']['y'] in [98]),'');lead=next((x['text'] for x in texts if x['bbox']['y']==118),'');kicker=next((x['text'] for x in texts if x['bbox']['y']==41),'');foot=next((x['text'] for x in texts if x['bbox']['y']==666),'')
  header='' if pg==3 else '<header class="head"><p class="kicker">'+html.escape(kicker)+'</p><h1 class="title">'+html.escape(title)+'</h1><p class="lead">'+html.escape(lead)+'</p></header>'
  if pg==3:header='<p class="top">'+html.escape(kicker)+'</p>'
  extra=''.join('<div class="rail"></div>' for u in page['furniture'] if 'Full-height supporting rail' in u.get('name',''))
  extra+=''.join('<div class="seat back" data-ph="1"></div>' for u in page['furniture'] if 'map' in u.get('name','').lower() and u['bbox'][1]<174)
  back='<div class="seat back'+(' avatar' if pg==8 else '')+'" data-ph="1"></div>' if pg in [7,8] else ''
  body='<section class="slide'+(' on' if pg==7 else '')+'"><div class="page">'+extra+back+header+'<div class="body">'+''.join(items)+'</div><footer class="foot">'+html.escape(foot)+'</footer></div></section>'
  gaps=[x['id'] for x in page['instances'] if x.get('use')=='unexpressible']
  if gaps:decisions.append({'page':pg,'contractGaps':gaps,'behavior':'Unsupported owner is omitted and documented in GAPS.md; mapped neighbouring elements retain their source content.'})
 (out/f'slide_{pg:02}.html').write_text(head+body+'</body></html>')
(P/'assembly-decisions.json').write_text(json.dumps(decisions,ensure_ascii=False,indent=2));print('30 contract-only assemblies written; explicit gaps',len(decisions))
