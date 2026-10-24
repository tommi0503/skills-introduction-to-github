from pathlib import Path
from bs4 import BeautifulSoup
import json,re,hashlib,sys,collections
R=Path('/workspace/work/rebuild');REF=Path('/workspace/work/reference');TAX=json.loads((REF/'contract/taxonomy.json').read_text());TOK=json.loads((REF/'contract/kit-tokens.json').read_text())['tokens'];TYPES=json.loads((REF/'contract/type-steps.json').read_text());ALLOWED=set(TOK)|{'--v','--max','--x','--y','--xmax','--ymax','--n','--r','--from','--to','--cols','--at','--mood','--next','--target','--low','--high','--a','--b','--tilt','--x1','--x2','--y1','--y2'}
for c in ['--page','--ink','--good','--warn','--bad']:ALLOWED.add(c)
for k in range(1,5):
 ALLOWED|={f'--a{k}',f'--a{k}-on'}
 for n in range(1,10):ALLOWED|={f'--a{k}-{n}',f'--a{k}-{n}-soft',f'--a{k}-{n}-muted'}
ALLOWED|={f'--n-{n}'for n in range(1,10)}|{f'--type-{n}'for n in TYPES}|{f'--v{n}'for n in range(1,9)}

def selectors(s):
 out=[];start=0;depth=0
 for j,c in enumerate(s):
  if c in '([':depth+=1
  elif c in ')]':depth-=1
  elif c==','and depth==0:out.append(s[start:j].strip());start=j+1
 out.append(s[start:].strip());return out

def ownscope(s,name,leaf):
 direct=r'\.[\w-]+\[data-el=[\'\"]'+re.escape(name+'-'+leaf)+r'[\'\"]\]'
 if re.match(direct,s):return True
 for fn in [':is(',':where(']:
  if s.startswith(fn):
   depth=1;k=len(fn)
   while k<len(s)and depth:
    if s[k]=='(':depth+=1
    elif s[k]==')':depth-=1
    k+=1
   return depth==0 and all(ownscope(a,name,leaf)for a in selectors(s[len(fn):k-1]))
 return False

def rules(css):
 css=re.sub(r'/\*.*?\*/','',css,flags=re.S);i=0
 while i<len(css):
  start=css.find('{',i)
  if start<0:break
  pre=css[i:start].strip();depth=1;k=start+1;quote=None
  while k<len(css)and depth:
   c=css[k]
   if quote:
    if c==quote and css[k-1]!='\\':quote=None
   elif c in ['"',"'"]:quote=c
   elif c=='{':depth+=1
   elif c=='}':depth-=1
   k+=1
  content=css[start+1:k-1];i=k
  if pre.startswith('@'):
   name=pre.split()[0].split('(')[0].lower()
   if name not in ['@container','@supports','@media']:yield('error','forbidden '+name)
   else:yield from rules(content)
  else:yield('rule',pre)

def classes_for(contract):
 cs=set(re.findall(r'\.([A-Za-z][\w-]*)',contract['structure']))|set(contract['roots'])|set(TAX['parts'])
 for a in re.findall(r'''class\s*=\s*["']([^"']+)''',contract['structure'].replace('\\','')):cs.update(a.split())
 if set(contract['roots'])&{'flowchart','swimlane'}:cs|={'to-r','to-d','to-l','to-u'}
 if 'tone-N'in cs:
  cs.remove('tone-N');cs|={f'tone-{k}'for k in range(1,13)}
 if 'tone-1'in cs:cs|={f'tone-{k}'for k in range(1,6)}
 # Required lines-12/lines-6/lines-3 explicitly contain .pt.on; the README
 # chart quality rule also names .on. Preserve the mandatory contract examples.
 if contract['id']=='chart.line@1':cs.add('on')
 return cs|{'icon','seat','avatar','portrait','logo','back','group','col','two','three','stack','split','wide-left'}

def audit(n):
 C=R/n/n;errors=[];pending=[];detail=[];kit=json.loads((C/'kit/kit.json').read_text());tc=(C/'kit/css/tokens.css').read_text();declared=set(re.findall(r'(--[\w-]+)\s*:',tc));errors+=['missing kit token '+t for t in TOK if t not in declared]
 if kit['schema']!='rhetis.kit/2'or kit['id']!=n:errors.append('kit identity/schema')
 for f in C.rglob('*'):
  if f.is_file()and f.suffix not in ['.css','.json','.md','.html']:errors.append('forbidden file '+str(f.relative_to(C)))
 leaves=sorted([p.name for p in (C/'elements').iterdir()if p.is_dir()]);
 if len(leaves)!=56:errors.append('element folders '+str(len(leaves)))
 for leaf in leaves:
  d=C/'elements'/leaf;f=d/'element.css'
  if not f.exists():pending.append(leaf);continue
  css=f.read_text();le=[];meta=json.loads((d/'element.json').read_text());contract=next((x for x in TAX['contracts']if x['id']==meta['contract']),None)
  if not contract:le.append('unknown contract')
  if not re.match(r'\s*/\*',css):le.append('missing source design comment')
  elif css.split('*/',1)[0].count('\n')>2:le.append('source comment exceeds3 lines')
  if not re.search(r'container-type\s*:\s*size',css):le.append('missing size container')
  stripped=re.sub(r'/\*.*?\*/','',css,flags=re.S)
  if re.search(r'#[0-9a-fA-F]{3,8}\b|\b(?:rgb|rgba|hsl|hsla|oklch|lab)\s*\(',stripped):le.append('literal colour')
  if re.search(r'(?<![\w-])(?:black|white|red|blue|green|gray|grey|orange|navy)(?![\w-])',re.sub(r'''"[^"]*"|'[^']*' ''','',stripped)):le.append('colour keyword')
  if re.search(r'font-size\s*:[^;{}]*\d(?:\.\d+)?px',stripped):le.append('px font size')
  if re.search(r'\b(?:font-weight|line-height|letter-spacing)\s*:\s*-?[\d.]',stripped):le.append('unshared typography literal')
  if re.search(r'url\s*\(|@import|@font-face|@keyframes',stripped):le.append('external resource/animation')
  for token in set(re.findall(r'var\(\s*(--[\w-]+)',stripped)):
   if token not in ALLOWED and not token.startswith('--'+n+'-'):le.append('unprefixed/unknown variable '+token)
  for r,sel in rules(css):
   if r=='error':le.append(sel);continue
   for s in selectors(sel):
    if not ownscope(s,n,leaf):le.append('unscoped selector '+s[:120])
   if re.search(r'fixture|slide_\d|replica-|\[style',sel):le.append('fixture/position style selector '+sel[:120])
  fs=list((d/'fixtures').glob('*.html'))
  if len(fs)<2:le.append('fewer than2 fixtures')
  for f in fs:
   s=f.read_text();soup=BeautifulSoup(s,'html.parser');roots=[x for x in soup.contents if getattr(x,'name',None)]
   if len(roots)!=1:le.append(f.name+': root count')
   elif (roots[0].get('data-el')!=n+'-'+leaf and not(set(roots[0].get('class',[]))&({'group','stack','split','prose'}if leaf=='tag'else{'group','stack','split'}) and roots[0].select('[data-el="'+n+'-'+leaf+'"]'))) or not re.search(r'grid-column\s*:\s*1\s*/\s*span\s+12',roots[0].get('style',''))or not re.search(r'grid-row\s*:\s*1\s*/\s*span\s+6',roots[0].get('style','')):le.append(f.name+': root identity/grid')
   if not re.match(r'<!-- min: \d+x\d+(?: \| \d+x\d+)* -->',s):le.append(f.name+': minimum comment')
   for elem in soup.find_all():
    owner=elem if elem.has_attr('data-el')else elem.find_parent(attrs={'data-el':True})
    if owner:
     oid=owner.get('data-el','');odir=C/'elements'/oid.removeprefix(n+'-')/'element.json'
     if not oid.startswith(n+'-')or not odir.exists():le.append(f.name+': unknown nested data-el '+oid);continue
     oc=next((x for x in TAX['contracts']if x['id']==json.loads(odir.read_text())['contract']),None)
     if not oc:continue
     if elem is owner and not set(elem.get('class',[]))&set(oc['roots']):le.append(f.name+': invalid contract root '+str(elem.get('class')))
     extra=set(elem.get('class',[]))-classes_for(oc)
     if extra:le.append(f.name+': undeclared classes '+','.join(sorted(extra)))
   for icon in soup.select('[data-icon]'):

    if icon.get_text().strip()or icon.find():le.append(f.name+': nonempty icon')
   for nested in soup.select('.list,.stat,.person,.card,.donut,.plan'):
    if nested.get('data-el')is None and nested.get('class',[None])[0]in ['list','person','card','donut','plan'] and not ((leaf=='person'and 'person'in nested.get('class',[]))or(leaf=='pricing'and 'plan'in nested.get('class',[]))or(leaf=='chart-donut'and 'donut'in nested.get('class',[]))):le.append(f.name+': nested missing data-el '+str(nested.get('class')))
  detail.append({'leaf':leaf,'errors':sorted(set(le)),'fixtures':len(fs),'css_sha256':hashlib.sha256(css.encode()).hexdigest()});errors.extend(leaf+': '+e for e in sorted(set(le)))
 report={'collection':n,'expected_leaves':56,'authored':56-len(pending),'pending':pending,'errors':errors,'elements':detail}
 (R/n/'review/validation/contract-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(n,'authored',report['authored'],'pending',len(pending),'errors',len(errors));print('\n'.join(errors[:20]))
 return report
if __name__=='__main__':
 for n in sys.argv[1:]or['tide-tab','cutfield','filament','portico','toggle-grid','lamella','rulemark']:audit(n)
