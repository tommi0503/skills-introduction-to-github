"""Round5 source checks: actual designs, extensible own parts, immutable source copy."""
from pathlib import Path
import argparse,json,re,hashlib,datetime,collections
from lxml import html
from sheets import ROOT,REF,minimum,fingerprint
TAX=json.loads((REF/'contract/taxonomy.json').read_text())
CONTRACTS={x['id']:x for x in TAX['contracts']}
BASES={p.name:json.loads((p/'element.json').read_text())['contract'] for p in(REF/'samples/annual/elements').iterdir()if p.is_dir()}
ALLROOTS={r for x in CONTRACTS.values()for r in x['roots']}
FOUNDATION={'slide','page','body','group','stack','split','panel','bar','seat','icon','top','rail','head','foot','lockup','meta','deco','frame','vector','label','title','lead','kicker','no','idx','deck','sec','src','logo','avatar','portrait','back'}
UTC=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
def classes(e):return set((e.get('class')or'').split())
def norm(s):return re.sub(r'\s+','',s).casefold()
def text_nodes(doc):
 for e in doc.iter():
  if not isinstance(e.tag,str)or e.tag in ['style','script','head','title']:continue
  if len(e)==0 and e.text and e.text.strip():yield e.text
  elif e.tag in ['p','h1','h2','h3','b','span','blockquote'] and e.text_content().strip():yield e.text_content()
def run(k,partial=False):
 P=ROOT/(k+'-project');K=P/k;errors=[];warnings=[];overlaps=[];files={};mapped=[];rows=[]
 def add(code,path,detail,warning=False):(warnings if warning else errors).append({'code':code,'path':str(path.relative_to(ROOT))if isinstance(path,Path)else path,'detail':detail})
 srcgrams=set()
 for p in(P/'replica').glob('slide_*.html'):
  d=html.fromstring(p.read_text())
  for s in text_nodes(d):
   t=norm(s)
   for i in range(len(t)-5):
    g=t[i:i+6]
    if re.search('[가-힣A-Za-z]',g):srcgrams.add(g)
 folders=sorted(p for p in(K/'elements').iterdir()if p.is_dir());ids={k+'-'+p.name:p for p in folders}
 for folder in folders:
  leaf=folder.name;base=leaf.split('--',1)[0];key=k+'-'+leaf
  if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*(?:--[a-z0-9]+(?:-[a-z0-9]+)*)?',leaf):add('folder-name',folder,leaf)
  if base not in BASES:add('unknown-contract-leaf',folder,base);continue
  for name in ['element.css','element.json','description.md']:
   if not(folder/name).exists():add('missing-file',folder/name,name)
  if not(folder/'element.json').exists()or not(folder/'element.css').exists():continue
  meta=json.loads((folder/'element.json').read_text());cid=meta.get('contract');roots=CONTRACTS.get(cid,{}).get('roots',[])
  if cid!=BASES[base]:add('contract-id',folder,{'expected':BASES[base],'actual':cid})
  css=(folder/'element.css').read_text();clean=re.sub(r'/\*.*?\*/','',css,flags=re.S)
  origin=re.match(r'\s*/\*(.*?)\*/',css,re.S)
  if not origin or not re.search(r'(?:replica|source|slide|page)[^\n\d]{0,40}\d{1,2}',origin.group(1),re.I):add('source-comment',folder,'first CSS comment must name a replica page and its observed design')
  if 'container-type:size'not in re.sub(r'\s+','',clean):add('size-container',folder,'root must establish size container')
  if not any(re.search(r'\.'+re.escape(r)+r'\[data-el=["\']'+re.escape(key)+r'["\']\]',clean)for r in roots):add('scope',folder,'literal contract root and full design key required')
  for at in re.findall(r'@([a-z-]+)',clean):
   if at not in ['container','media','supports']:add('at-rule',folder,at)
  if re.search(r'url\s*\(',clean):add('external-resource',folder,'url() is not admitted in collection CSS')
  for value in re.findall(r'font-size\s*:\s*([^;}]+)',clean):
   if value.strip()=='inherit':continue
   if re.search(r'\d(?:px|rem|vw|vh)',value)or not re.search(r'var\(--type-\d+\)',value):add('font-size',folder,value)
   for n in re.findall(r'--type-(\d+)',value):
    if int(n)not in list(range(8,34,2))+list(range(36,257,4)):add('type-token',folder,n)
  if re.search(r'#[0-9a-fA-F]{3,8}\b|\b(?:rgb|rgba|hsl|hsla|oklch|lab)\s*\(',clean):add('literal-color',folder,'palette slots only')
  if re.search(r'\[data-(?:page|fixture)[\s=\]]',clean):add('page-fixture-selector',folder,'page/fixture-specific selection prohibited')
  fixtures=sorted((folder/'fixtures').glob('*.html'))
  if len(fixtures)<2:add('fixture-count',folder,len(fixtures))
  deps=set()
  for f in fixtures:
   try:mini=minimum(f);assert 1<=mini[0]<=12 and 1<=mini[1]<=6
   except Exception as ex:add('minimum',f,str(ex));continue
   d=html.fragment_fromstring(f.read_text(),create_parent='audit-fragment');children=[e for e in d if isinstance(e.tag,str)]
   if len(children)!=1:add('fixture-root-count',f,len(children));continue
   root=children[0]
   if not (root.get('data-el')==key or root.xpath('.//*[@data-el="'+key+'"]')):add('fixture-own-design-missing',f,key)
   if not root.get('data-el')and not classes(root)&{'group','stack','split','panel'}:add('fixture-context-root',f,sorted(classes(root)))
   for e in root.iter():
    if not isinstance(e.tag,str):continue
    dep=e.get('data-el')
    if dep:
     if dep not in ids:add('missing-dependency',f,dep)
     else:
      actualbase=ids[dep].name.split('--',1)[0];actualroots=set(CONTRACTS[BASES[actualbase]]['roots'])
      if not classes(e)&actualroots:add('fixture-contract-root',f,{'key':dep,'classes':sorted(classes(e))})
      if dep!=key:deps.add(dep)
    owner=e
    while owner is not None and not owner.get('data-el'):owner=owner.getparent()
    if owner is not None and owner.get('data-el')in ids:
     ownbase=ids[owner.get('data-el')].name.split('--',1)[0];ownroots=set(CONTRACTS[BASES[ownbase]]['roots'])
     collisions=(classes(e)&ALLROOTS)-ownroots-FOUNDATION
     if collisions and not e.get('data-el'):add('other-contract-root-used-as-private-part',f,sorted(collisions))
   for s in text_nodes(root):
    t=norm(s);hits=sorted({t[i:i+6]for i in range(len(t)-5)if t[i:i+6]in srcgrams})
    if hits:overlaps.append({'fixture':str(f.relative_to(ROOT)),'text':s[:120],'windows':hits[:10]})
   for donut in root.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," pie ")]')+([root]if'pie'in classes(root)else[]):
    slices=[e for e in donut if'slice'in classes(e)]
    if not slices:continue
    vals=[];starts=[]
    for sl in slices:
     st=sl.get('style','');v=re.search(r'(?:^|;)\s*--v\s*:\s*([\d.]+)',st);a=re.search(r'--[\w-]*slice-start\s*:\s*([\d.]+)',st)
     if v:vals.append(float(v.group(1)))
     if a:starts.append(float(a.group(1)))
    if len(vals)!=len(slices)or not 2<=len(vals)<=6 or abs(sum(vals)-100)>.01:add('pie-shares',f,vals)
    if starts and(len(starts)!=len(vals)or any(abs(a-sum(vals[:i]))>.01 for i,a in enumerate(starts))):add('pie-derived-starts',f,{'v':vals,'starts':starts})
  rows.append({'folder':leaf,'contract':cid,'fixtures':len(fixtures),'dependencies':sorted(deps)})
 foundation_fixtures=sorted((K/'foundation/fixtures').glob('*.html'))
 for f in foundation_fixtures:
  d=html.fragment_fromstring(f.read_text(),create_parent='audit-foundation')
  for s in text_nodes(d):
   t=norm(s);hits=sorted({t[i:i+6]for i in range(len(t)-5)if t[i:i+6]in srcgrams})
   if hits:overlaps.append({'fixture':str(f.relative_to(ROOT)),'text':s[:120],'windows':hits[:10],'scope':'foundation'})
 for f in K.rglob('*'):
  if f.is_file():
   files[str(f.relative_to(K))]=hashlib.sha256(f.read_bytes()).hexdigest()
   if f.suffix not in ['.css','.json','.md','.html']:add('file-type',f,f.suffix)
 m=json.loads((P/'map.json').read_text());bases=collections.Counter()
 for i in m['instances']:
  leaf=i.get('leaf')
  if leaf and leaf not in {p.name for p in folders}:add('mapped-missing-design','map.json',leaf)
  if i.get('use')=='base'and leaf:bases[leaf]+=1
  if i.get('use')=='unexpressible'and not i.get('why'):add('gap-reason','map.json',i.get('id'))
 for leaf,n in bases.items():
  if n>1:add('duplicate-base','map.json',{leaf:n})
 if overlaps:add('replica-text','fixtures',len(overlaps))
 result={'schema':'rhetis.round5-source-audit/1','collection':k,'generatedAtUTC':UTC(),'elements':len(folders),'fixtureCount':sum(x['fixtures']for x in rows),'foundationFixtureCount':len(foundation_fixtures),'copyNormalization':'whitespace removed, Unicode casefold; element and foundation fixtures','errors':errors,'warnings':warnings,'replicaTextOverlap6':overlaps,'designs':rows,'sourceFiles':files,'globalFingerprint':fingerprint(P,k),'policy':'ROUND5-USER.md overrides historical complete56/closedparts/golden requirements; no registry state IDs claimed'}
 (P/'source-contract-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(k,len(folders),'designs',len(errors),'errors',len(overlaps),'copy overlaps');return result
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('collection');a.add_argument('--partial',action='store_true');v=a.parse_args();run(v.collection,v.partial)
