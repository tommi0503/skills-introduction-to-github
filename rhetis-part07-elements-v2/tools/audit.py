"""Contract structure, source mapping, fresh CSS scope, text separation and final sheet provenance."""
from pathlib import Path
import re,json,hashlib,argparse,sys
from lxml import html
from sheets import ROOT,REF,fingerprint

PALETTE={'--page','--ink','--good','--warn','--bad'}|{f'--n-{i}' for i in range(1,10)}|{f'--a{i}' for i in range(1,5)}|{f'--a{i}-on' for i in range(1,5)}|{f'--a{i}-{j}{s}' for i in range(1,5) for j in range(1,10) for s in ['','-soft','-muted']}
def normal(s):return re.sub(r'\s+','',s).casefold()
def windows(s):return {s[i:i+6] for i in range(len(s)-5) if re.search('[가-힣A-Za-z]',s[i:i+6])}
def phrases(doc):
 units=list(doc.xpath('//text()[not(ancestor::script) and not(ancestor::style) and not(ancestor::title)]'))
 inline={'span','b','strong','i','em','small','br','a'}
 for e in doc.iter():
  if not isinstance(e.tag,str) or e.tag in ['script','style','title']:continue
  if len(e) and all(isinstance(c.tag,str) and c.tag in inline for c in e):units.append(e.text_content())
 return units
def text_windows(P):
 out={}
 for f in sorted((P/'replica').glob('slide*.html')):
  doc=html.fromstring(f.read_text())
  for e in doc.xpath('//script|//style|//title'):e.drop_tree()
  for s in phrases(doc):
   for word in windows(normal(s)):out.setdefault(word,[]).append(f.stem)
 return out
def blocks(css):
 css=re.sub(r'/\*.*?\*/','',css,flags=re.S);pos=0
 while pos<len(css):
  left=css.find('{',pos)
  if left<0:break
  level=1;i=left+1;quote=None
  while i<len(css) and level:
   c=css[i]
   if quote:
    if c==quote and css[i-1]!='\\':quote=None
   elif c in ['"',"'"]:quote=c
   elif c=='{':level+=1
   elif c=='}':level-=1
   i+=1
  assert not level,'unclosed CSS block'
  head=css[pos:left].strip();body=css[left+1:i-1]
  if head.startswith('@'):
   assert re.match(r'@(container|media|supports)\b',head),head
   yield from blocks(body)
  else:yield head,body
  pos=i
def audit(k,partial=False):
 P=ROOT/(k+'-project');K=P/k;issues=[];warnings=[];overlap=[];leafs=sorted(x.name for x in (REF/'samples/annual/elements').iterdir() if x.is_dir());contracts={x.name:json.loads((x/'element.json').read_text())['contract'] for x in (REF/'samples/annual/elements').iterdir() if x.is_dir()};roots={c['id']:c['roots'] for c in json.loads((REF/'contract/taxonomy.json').read_text())['contracts']};source=text_windows(P)
 allowed_steps=set(json.loads((REF/'contract/type-steps.json').read_text()))
 for file in K.rglob('*.css'):
  unknown=set(map(int,re.findall(r'var\(--type-(\d+)\)',file.read_text())))-allowed_steps
  if unknown:issues.append(['unknown type steps',str(file.relative_to(P)),sorted(unknown)])
 mapping=json.loads((P/'map.json').read_text());base={}
 if mapping.get('collection')!=k:issues.append(['map collection id',mapping.get('collection')])
 if not isinstance(mapping.get('roles'),dict) or not mapping.get('roles'):issues.append(['map roles must be nonempty dictionary'])
 for x in mapping['instances']:
  use=x.get('use','')
  for field in ['page','bbox','leaf','use','design']:
   if field not in x or field=='design' and not str(x.get(field,'')).strip():issues.append(['missing map field',x.get('id'),field])
  if use not in ['base','furniture','background','unexpressible'] and not use.startswith(('same-as:','variant:.')):issues.append(['invalid map use',x.get('id'),use])
  if x.get('use')=='base':base.setdefault(x['leaf'],[]).append(x['page'])
  if x.get('use')=='unexpressible' and not x.get('why'):issues.append(['map gap missing why',x])
  b=x['bbox']
  if len(b)!=4 or min(b)<0 or b[0]+b[2]>1281 or b[1]+b[3]>721:issues.append(['invalid bbox',x.get('id'),b])
 for leaf,pages in base.items():
  if len(pages)!=1:issues.append(['base must be unique',leaf,pages])
 for leaf in leafs:
  F=K/'elements'/leaf
  if not F.exists():
   if not partial:issues.append(['missing element',leaf])
   continue
  if not (F/'element.css').exists():
   if not partial:issues.append(['missing CSS',leaf])
   continue
  meta=json.loads((F/'element.json').read_text())
  if meta.get('contract')!=contracts[leaf]:issues.append(['wrong contract',leaf])
  css=(F/'element.css').read_text()
  if not css.lstrip().startswith('/*'):issues.append(['missing source header comment',leaf])
  if not re.search(r'container-type\s*:\s*size\b',css):issues.append(['root not size container',leaf])
  for selector,decl in blocks(css):
   # Every selector arm must start within an admitted root of this same leaf.
   for arm in re.split(r',(?=[^()]*\))(?![^()]*\))|,(?![^()]*\))',selector):
    arm=arm.strip()
    if not any(arm.startswith('.'+r+'[data-el="'+k+'-'+leaf+'"]') or arm.startswith('.'+r+"[data-el='"+k+'-'+leaf+"']") for r in roots[contracts[leaf]]):issues.append(['CSS outside literal root scope',leaf,arm])
   if re.search(r':has\(\s*[+~]|\[style|\.src\b|\.overrides\b',selector):issues.append(['page/fixture/sibling condition',leaf,selector])
   if re.search(r'#[0-9a-fA-F]{3,8}\b|\b(?:rgb|hsl|oklch|lab)\(',decl):issues.append(['colour literal',leaf,selector])
   for prop,value in re.findall(r'([\w-]+)\s*:\s*([^;]+)',decl):
    if prop=='font-size' and (re.search(r'\d\s*px\b',value) or not (value.strip().startswith('var(--type-') or value.strip().startswith('clamp(var(--type-') or value.strip()=='inherit')):issues.append(['invalid font-size',leaf,value])
    if prop in ['font-weight','font-family','line-height','letter-spacing'] and not value.strip().startswith('var(') and value.strip()!='inherit':warnings.append(['typography not shared token',leaf,prop,value])
   if re.search(r'@import|url\(|@font-face|@keyframes',decl):issues.append(['external resource',leaf])
  fixtures=list((F/'fixtures').glob('*.html'))
  if len(fixtures)<2:issues.append(['fixture count',leaf,len(fixtures)])
  for f in fixtures:
   text=f.read_text();m=re.match(r'<!--\s*min:\s*(\d+)x(\d+)',text)
   if not m:issues.append(['missing min',str(f.relative_to(P))])
   doc=html.fragment_fromstring(re.sub(r'^<!--.*?-->\s*','',text,count=1,flags=re.S),create_parent='body')
   if len(doc)!=1:issues.append(['fixture must have one child',str(f.relative_to(P))])
   for s in phrases(doc):
    for word in sorted(windows(normal(s))&set(source)):
     overlap.append({'fixture':str(f.relative_to(P)),'phrase':word,'sourcePages':sorted(set(source[word]))})
  sheet=P/'sheets'/(leaf+'-checks.json')
  if sheet.exists():
   j=json.loads(sheet.read_text())
   if j.get('sourceFingerprint')!=fingerprint(P,k,leaf):warnings.append(['stale sheet',leaf])
  elif not partial:issues.append(['missing size sheet',leaf])
 for f in (K/'foundation/fixtures').glob('*.html'):
  doc=html.fragment_fromstring(re.sub(r'^<!--.*?-->\s*','',f.read_text(),count=1,flags=re.S),create_parent='body')
  for s in phrases(doc):
   for word in sorted(windows(normal(s))&set(source)):overlap.append({'fixture':str(f.relative_to(P)),'phrase':word,'sourcePages':sorted(set(source[word]))})
 result={'collection':k,'elementFolders':sum((K/'elements'/leaf).is_dir() for leaf in leafs),'elementCssFiles':sum((K/'elements'/leaf/'element.css').exists() for leaf in leafs),'expectedElements':56,'mapInstances':len(mapping['instances']),'baseSources':base,'unexpressible':[x.get('id') for x in mapping['instances'] if x.get('use')=='unexpressible'],'errors':issues,'warnings':warnings,'replicaTextOverlap6':overlap,'replicaTextScan':'All element AND foundation fixtures. Visible text nodes plus parent phrases across inline spans/b/strong/em/small/br/a. Unicode whitespace removed and English case folded; every6-character window containing letters. Different block paragraphs are not concatenated.'}
 (P/'source-contract-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(k,'elements',result['elementFolders'],'errors',len(issues),'warnings',len(warnings),'source-phrase overlaps',len(overlap));return result

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('collection');ap.add_argument('--partial',action='store_true');a=ap.parse_args();r=audit(a.collection,a.partial);sys.exit(int(bool(r['errors'] or r['replicaTextOverlap6'])))
