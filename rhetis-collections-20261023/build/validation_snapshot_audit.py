"""Ensure final checks refer to the exact sources being packaged."""
from pathlib import Path
import json,hashlib,sys
BASE=Path('/workspace/output');WORK=Path('/workspace/work/integration')
names=sys.argv[1:] or ['fluxweave','cyanloop','roundrise','nightchamfer','glasspulse']
result=[]
for name in names:
 row={'collection':name,'errors':[]}
 for suffix,key in [('browser-audit','source_sha256'),('page-audit','collection_source_sha256')]:
  path=WORK/(name+'-'+suffix+'.json')
  if not path.exists():row['errors'].append('Missing '+path.name);continue
  data=json.loads(path.read_text());snap=data.get(key,{})
  if not snap:row['errors'].append('Missing source snapshot in '+path.name)
  for rel,digest in snap.items():
   f=BASE/name/rel
   if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=digest:row['errors'].append(suffix+' stale source '+rel)
  if suffix=='browser-audit':
   row['fixture_count']=data.get('fixtures');row['grid_states']=data.get('tested_states')
   if data.get('issues'):row['errors'].append('Geometry issues remain')
   if data.get('fonts') or data.get('resources'):row['errors'].append('Font/resource failures remain')
  else:
   row['page_count']=len(data.get('pages',[]))
   row['errors']+=data.get('errors',[])
   for rel,digest in data.get('review_assets_sha256',{}).items():
    f=BASE/(name+'-review')/rel
    if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=digest:row['errors'].append('Page audit stale review asset '+rel)
 result.append(row)
 print(name,row.get('fixture_count'),row.get('grid_states'),row.get('page_count'),len(row['errors']),'errors')
 for e in row['errors'][:10]:print(' ',e)
(WORK/'validation-snapshot-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
