from pathlib import Path
import json,re
P=Path(__file__).parent;E=P/'crossrail/elements';T=json.load(open('/workspace/work/reference/contract/taxonomy.json'));roots={c['id']:c['roots'] for c in T['contracts']}
def split(s):
 out=[];start=0;dep=0;q=None
 for i,c in enumerate(s):
  if q:
   if c==q and (i==0 or s[i-1]!='\\'):q=None
  elif c in ['"',"'"]:q=c
  elif c in '([':dep+=1
  elif c in ')]':dep-=1
  elif c==',' and dep==0:out.append(s[start:i].strip());start=i+1
 out.append(s[start:].strip());return out
def run(css,leaf,rs):
 css=re.sub(r'/\*.*?\*/','',css,flags=re.S);out='';pos=0
 while pos<len(css):
  st=css.find('{',pos)
  if st<0:break
  h=css[pos:st].strip();lv=1;i=st+1;q=None
  while lv and i<len(css):
   c=css[i]
   if q:
    if c==q and css[i-1]!='\\':q=None
   elif c in ['"',"'"]:q=c
   elif c=='{':lv+=1
   elif c=='}':lv-=1
   i+=1
  b=css[st+1:i-1]
  if h.startswith('@'):out+=h+'{'+run(b,leaf,rs)+'}'
  else:
   arms=[];a=f'[data-el="crossrail-{leaf}"]'
   for arm in split(h):
    if arm.startswith(a):
     tail=arm[len(a):];chosen=next((r for r in rs if re.match(r'\.'+re.escape(r)+r'(?![\w-])',tail)),None)
     if chosen:arms.append('.'+chosen+a+tail[len(chosen)+1:])
     else:arms += ['.'+r+a+tail for r in rs]
    else:arms.append(arm)
   out+=','.join(arms)+'{'+b+'}'
  pos=i
 return out
for d in E.iterdir():
 f=d/'element.css'
 if not f.exists():continue
 meta=json.loads((d/'element.json').read_text());css=run(f.read_text(),d.name,roots[meta['contract']]);f.write_text('/* Fresh Crossrail design. Source measurements: ../../../../source-measurements.json; map ownership: ../../../../map.json. */\n'+css+'\n')
# The comparison map selects one base instance and explicitly points other occurrences to it.
f=P/'map.json';m=json.loads(f.read_text());m['baseChoices']['list']=12;seen=set()
for x in m['instances']:
 u=x['use'];leaf=x['leaf']
 if u=='page-device':x['use']='background' if x.get('role')=='furniture' and x['bbox'][2]*x['bbox'][3]>200000 else 'furniture'
 elif u.startswith('variant:') and not u.startswith('variant:.'):x['use']='variant:.'+u[len('variant:'):]
 elif u=='base':
  bp=m['baseChoices'].get(leaf,x['page'])
  if x['page']==bp and leaf not in seen:seen.add(leaf)
  else:x['use']='same-as:'+str(bp)
f.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
