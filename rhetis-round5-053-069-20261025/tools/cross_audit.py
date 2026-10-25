"""Read-only final map/fixture ownership and extended-chart data audit."""
from pathlib import Path
from lxml import html
import json,re,hashlib,time
ROOT=Path(__file__).resolve().parents[1]
tax={x['id']:set(x['roots'])for x in json.loads((ROOT/'contract/taxonomy.json').read_text())['contracts']};reserved={a:k for k,v in tax.items()for a in v};families=json.loads((ROOT/'contract/leaves.json').read_text());issues=[];counts={'folders':0,'fixtures':0,'maps':0,'pieGroups':0,'svg':0,'dataRoots':0};inputs={}
for c in json.loads((ROOT/'collections.json').read_text()):
 cid=c['id'];C=ROOT/cid;m=ROOT/(cid+'-review/map.json');d=json.loads(m.read_text());inputs[str(m.relative_to(ROOT))]=hashlib.sha256(m.read_bytes()).hexdigest();counts['maps']+=1
 folders=[p for p in(C/'elements').iterdir()if p.is_dir()];counts['folders']+=len(folders);keys={cid+'-'+p.name:families[p.name.split('--')[0]]for p in folders}
 docs=[(str(m.relative_to(ROOT))+'#'+x['instance_id'],x['markup'])for x in d['instances']if x.get('markup')]
 for f in sorted((C/'elements').glob('*/fixtures/*.html')):docs.append((str(f.relative_to(ROOT)),f.read_text()));counts['fixtures']+=1;inputs[str(f.relative_to(ROOT))]=hashlib.sha256(f.read_bytes()).hexdigest()
 for loc,source in docs:
  nodes=html.fragments_fromstring(re.sub(r'<!--.*?-->','',source,flags=re.S))
  for root in nodes:
   if isinstance(root,str):continue
   for n in root.iter():
    cls=set(n.get('class','').split());key=n.get('data-el')
    if n.tag=='svg':counts['svg']+=1;issues.append({'file':loc,'rule':'inline-svg'})
    if key:
     counts['dataRoots']+=1
     if key not in keys or not cls&tax.get(keys.get(key),set()):issues.append({'file':loc,'rule':'root','key':key})
    owner=n
    while owner is not None and not owner.get('data-el'):owner=owner.getparent()
    if owner is not None:
     contract=keys.get(owner.get('data-el'))
     for name in cls&reserved.keys():
      if reserved[name]!=contract:issues.append({'file':loc,'rule':'foreign-root-as-part','class':name,'owner':contract})
    if 'donut'in cls and 'pie'in cls:
     vals=[]
     for sl in n:
      if 'slice'not in sl.get('class','').split():continue
      mt=re.search(r'(?:^|;)\s*--v\s*:\s*([\d.]+)',sl.get('style',''));vals.append(float(mt[1])if mt else -999)
     counts['pieGroups']+=1
     if not 2<=len(vals)<=6 or abs(sum(vals)-100)>.01:issues.append({'file':loc,'rule':'pie-sum/count','values':vals})
report={'createdUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'scope':'Final read-only map and fixture audit. No edits to collection, map or fixture. Text/glyph behavior is checked by browser sheet audits.','counts':counts,'issues':issues,'inputs':inputs};(ROOT/'round5/cross-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps({'counts':counts,'issues':issues},ensure_ascii=False,indent=2))
