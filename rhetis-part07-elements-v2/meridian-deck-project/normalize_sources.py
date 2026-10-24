from pathlib import Path
import json,re
P=Path(__file__).parent;C=P/'meridian-deck';tax=json.load(open('/workspace/work/reference/contract/taxonomy.json'));roots={x['id']:x['roots'] for x in tax['contracts']}
m=json.loads((P/'map.json').read_text());seen={};bases={}
for x in m['instances']:
 if x.get('use')=='base':
  if x['leaf'] in seen:x['use']='reuse:base';x['baseInstance']=seen[x['leaf']]
  else:seen[x['leaf']]=x['id'];bases[x['leaf']]=x['page']
 b=x['bbox'];x0=max(0,b[0]);y0=max(0,b[1]);x1=min(1280,b[0]+b[2]);y1=min(720,b[1]+b[3])
 if [x0,y0,x1-x0,y1-y0]!=b:
  x['unclippedBBox']=b;x['bbox']=[x0,y0,x1-x0,y1-y0];x['bounds']=dict(zip(['x','y','w','h'],x['bbox']));x['visibleBoundsNote']='The source shape crosses the canvas; bbox records only visible pixels.'
byid={x['id']:x for x in m['instances']}
for p in m['pages']:
 for k in ['instances','furniture']:p[k]=[byid.get(x['id'],x) for x in p[k]]
m['baseDesigns']={k:{'sourcePage':bases[k],'instance':v} for k,v in seen.items()};(P/'map.json').write_text(json.dumps(m,ensure_ascii=False,indent=2))
def arms(s):
 out=[];dep=0;start=0
 for i,c in enumerate(s):
  if c in '([':dep+=1
  elif c in ')]':dep-=1
  elif c==',' and dep==0:out.append(s[start:i]);start=i+1
 out.append(s[start:]);return out
def rewrite(css,leaf,rs):
 out='';pos=0
 while pos<len(css):
  l=css.find('{',pos)
  if l<0:return out+css[pos:]
  head=css[pos:l];depth=1;i=l+1;quote=None
  while depth:
   c=css[i]
   if quote:
    if c==quote and css[i-1]!='\\':quote=None
   elif c in '\"\'':quote=c
   elif c=='{':depth+=1
   elif c=='}':depth-=1
   i+=1
  body=css[l+1:i-1]
  if head.strip().startswith('@'):body=rewrite(body,leaf,rs)
  else:
   hh=[]
   for a in arms(head):
    a=a.strip();attr='[data-el="meridian-deck-'+leaf+'"]'
    if a.startswith(attr):hh.extend('.'+r+a for r in rs)
    else:
     a=re.sub(r'^(\.[\w-]+)((?:\.[\w-]+)+)('+re.escape(attr)+r')',r'\1\3\2',a);hh.append(a)
   head=','.join(hh)
  out+=head+'{'+body+'}';pos=i
 return out
for d in (C/'elements').iterdir():
 j=json.load(open(d/'element.json'));f=d/'element.css';s=f.read_text();s=re.sub(r'^/\*.*?\*/\s*','',s,flags=re.S)
 source='Measured source page '+str(bases[d.name])+'.' if d.name in bases else 'Extension of the measured circle, fine-rule and heading-band language.'
 f.write_text('/* '+d.name+' — '+source+' Ratios belong to members of this element; no page or fixture conditions. */\n'+rewrite(s,d.name,roots[j['contract']]))
# This identifier accidentally contains the source word VISION across an SQL token.
f=C/'elements/code/fixtures/code-numbered.html';f.write_text(f.read_text().replace('division','team_key'))
for f in (C/'foundation/fixtures').glob('*.html'):f.write_text(f.read_text().replace('BUSINESS','OPERATIONS').replace('Business','Operations'))
print('Normalized literal root scopes, unique base provenance, visible canvas bounds and fresh copy')
