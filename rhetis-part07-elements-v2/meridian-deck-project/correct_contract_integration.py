from pathlib import Path
from lxml import html as LH,etree
import json,re,copy
P=Path(__file__).parent;K=P/'meridian-deck'
# Non-golden nested list contracts are explicit elements with real members.
for leaf in ['matrix','pricing','versus','person']:
 for f in (K/'elements'/leaf/'fixtures').glob('*.html'):
  if f.name=='replica-12.html':continue
  text=f.read_text();doc=LH.fragment_fromstring(text,create_parent='audit');changed=False
  for e in doc.xpath('.//*[@class]'):
   cs=set(e.get('class','').split())
   if 'list' in cs and not e.get('data-el'):
    e.set('data-el','meridian-deck-list');changed=True
    if e.tag=='ul':
     e.tag='div'
     for li in e:
      if li.tag!='li':continue
      li.tag='div';li.set('class','item');content=(li.text or '')+''.join(etree.tostring(x,encoding='unicode',method='html') for x in li);li.clear();li.set('class','item')
      name=LH.fragment_fromstring('<b class="name">'+content+'</b>');li.append(name);li.append(LH.fromstring('<p class="note"></p>'))
    if leaf=='pricing':e.set('class','list check')
   if 'tag' in cs and not e.get('data-el'):e.set('data-el','meridian-deck-tag');changed=True
  if changed:f.write_text(text.split('\n',1)[0]+'\n'+''.join(etree.tostring(x,encoding='unicode',method='html') for x in doc if isinstance(x.tag,str))+'\n')
# Source12 is prose, not a list: retain all four headers and paragraphs separately.
f=P/'fixtures_connected.py';s=f.read_text();old=next((x for x in s.splitlines() if x.startswith("save('matrix',12")),None);new="save('headline',12,group([root('headline','headline','<h2>'+txt(12,i)+'</h2>') for i in [16,18,20,22]]),'12x1')\nsave('prose',12,group([root('prose','prose quiet','<p>'+txt(12,i)+'</p>') for i in [17,19,21,23]]),'12x2')";s=s.replace(old,new) if old else s;f.write_text(s)
f=P/'assemble.py';s=f.read_text().replace("('fixtures_connected.py',\"save('matrix'\")","('fixtures_connected.py',\"save('headline',12\")");f.write_text(s)
ns={'__file__':str(P/'fixtures_connected.py')};prefix=(P/'write_replica_fixtures.py').read_text().split('# Cards:')[0];exec(prefix,ns);exec(new,ns)
# Keep the original separator and a complete new business qualifier in the fixture.
f=K/'elements/headline/fixtures/replica-12.html';text=f.read_text();doc=LH.fragment_fromstring(text,create_parent='x')
for heading,word in zip(doc.xpath('.//h2'),['정비','개선','확장','대응']):
 b=heading.find('b')
 if b is not None:b.tail=' │ '+word
f.write_text(text.split('\n',1)[0]+'\n'+''.join(etree.tostring(x,encoding='unicode',method='html') for x in doc if isinstance(x.tag,str))+'\n')
(K/'elements/matrix/fixtures/replica-12.html').unlink(missing_ok=True)
M=json.loads((P/'map.json').read_text());u=next(x for x in M['instances'] if x['id']=='p12-08');original=copy.deepcopy(u);parts=sorted({m['index']:m for unit in M['instances'] if unit['page']==12 for m in unit.get('sourceMeasurements',[]) if 8<=m['index']<=23}.values(),key=lambda m:m['index']);shape=[x for x in parts if x['index']<=15]
def box(items):
 bs=[x['bbox'] for x in items];x=min(z['x'] for z in bs);y=min(z['y'] for z in bs);return [x,y,max(z['x']+z['w'] for z in bs)-x,max(z['y']+z['h'] for z in bs)-y]
u.update(name='Four-lobe SWOT owner with paragraph slots unsupported by current swot contract',status='unexpressible',use='unexpressible',why='SWOT requires nested list.items but the source has four continuous paragraphs. Splitting physical lines into fake list members would change semantics. Proposed extension: .matrix.swot > .cell > .prose[data-el]. The real paragraphs and headings are retained separately.',bbox=box(shape),parts=[x['id'] for x in shape],sourceMeasurements=shape)
u.pop('fixture',None);u['selectors']=original['selectors'][:8];u['bounds']=dict(zip(['x','y','w','h'],u['bbox']))
base={x['leaf']:x['id'] for x in M['instances'] if x.get('use')=='base' and x['id']!='p12-08'}
add=[]
for idx in [16,17,18,19,20,21,22,23]:
 m=next(x for x in parts if x['index']==idx);leaf='headline' if idx%2==0 else 'prose';b=box([m]);ident=f'p12-{leaf}-{idx}'
 add.append({'id':ident,'name':f'SWOT {leaf} {idx}','kind':'element','status':'mapped','bbox':b,'bounds':dict(zip(['x','y','w','h'],b)),'leaf':leaf,'variant':'quiet' if leaf=='prose' else '', 'parts':[m['id']],'selectors':[f'main.slide > :nth-child({idx})'],'sourceMeasurements':[m],'page':12,'use':'same-as:04' if leaf=='prose' else 'same-as:05','baseRef':base[leaf],'fixture':f'elements/{leaf}/fixtures/replica-12.html'})
M['instances']=[x for x in M['instances'] if not x['id'].startswith(('p12-headline-','p12-prose-'))]+add
pg=M['pages'][11];pg['instances']=[x for x in pg['instances'] if x['id']!='p12-08' and not x['id'].startswith(('p12-headline-','p12-prose-'))]+[u]+add
(P/'map.json').write_text(json.dumps(M,ensure_ascii=False,indent=2)+'\n')
# Nested roots receive space, while their own CSS supplies their drawing.
for leaf,selector in [('pricing','.plan[data-el="meridian-deck-pricing"]>.list'),('versus','.versus[data-el="meridian-deck-versus"]>.side>.list')]:
 f=K/'elements'/leaf/'element.css';s=f.read_text();s=re.sub(re.escape(selector)+r'\{[^}]*\}',selector+'{flex:1;min-height:0;}',s);s=re.sub(re.escape(selector)+r'>li\{[^}]*\}','',s);f.write_text(s)
print('nested contracts repaired; source12 unsupported owner isolated; eight real text units preserved')
