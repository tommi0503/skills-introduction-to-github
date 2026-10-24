from pathlib import Path
from PIL import Image
import json,hashlib,time,importlib.util
R=Path('/workspace/work/rhetis-elements-v2');O=Path('/tmp/rhetis-root-replica-view');O.mkdir(exist_ok=True);entries=[];skipped=[]
sp=importlib.util.spec_from_file_location('sheet_fp',R/'tools/sheets.py');sh=importlib.util.module_from_spec(sp);sp.loader.exec_module(sh)
for P in sorted(R.glob('*-project')):
 K=next(x for x in P.iterdir() if x.is_dir() and (x/'kit/kit.json').exists());k=K.name;D=O/k;D.mkdir(exist_ok=True);mapping=json.loads((P/'map.json').read_text());active={x.get('leaf') for x in mapping.get('instances',[]) if x.get('use')=='base' or str(x.get('use','')).startswith('variant:')}
 for src in sorted((P/'sheets').glob('*-replica.png')):
  leaf=src.name[:-len('-replica.png')]
  if leaf not in active:
   skipped.append(str(src.relative_to(R)));stale=D/(leaf+'.png')
   if stale.exists():stale.unlink()
   continue
  checks=json.loads((P/'sheets'/(leaf+'-checks.json')).read_text());current=sh.fingerprint(P,k,leaf);dst=D/(leaf+'.png');im=Image.open(src).convert('RGB');originalSize=list(im.size);im.thumbnail((1700,1700),Image.Resampling.LANCZOS);tmp=dst.with_suffix('.tmp.png');im.save(tmp);tmp.replace(dst);entries.append({'canonicalRelativePath':str(src.relative_to(R)),'canonicalSHA256':hashlib.sha256(src.read_bytes()).hexdigest(),'canonicalSize':originalSize,'sheetSourceFingerprint':checks['sourceFingerprint'],'currentSourceFingerprint':current,'matchesCurrentSource':checks['sourceFingerprint']==current,'overviewAbsolutePath':str(dst),'overviewSize':list(im.size),'overviewSHA256':hashlib.sha256(dst.read_bytes()).hexdigest()})
report={'generatedAtUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'root':str(R),'maxOverviewSize':[1700,1700],'skippedInactiveCanonical':skipped,'canonicalRelativePathToSHA256':{x['canonicalRelativePath']:x['canonicalSHA256'] for x in entries},'entries':entries};(O/'provenance.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('overviews',len(entries),'collections',len(set(x['canonicalRelativePath'].split('/')[0] for x in entries)))
