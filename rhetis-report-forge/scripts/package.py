from pathlib import Path
import hashlib,json,zipfile,shutil
P=Path(__file__).resolve().parent.parent
R=P.parent
excluded={'node_modules','dist','work','.git'}
def files():
 return sorted(p for p in P.rglob('*') if p.is_file() and not any(part in excluded for part in p.relative_to(P).parts) and not p.name.endswith('.tsbuildinfo'))
manifest={str(p.relative_to(P)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files() if p.name!='sha256-files.json'}
(P/'review/sha256-files.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
archives=[(R/'report-forge.zip',P/'collection/report-forge','report-forge'),(R/'rhetis-report-forge-delivery.zip',P,'rhetis-report-forge')]
summary=[]
for target,root,prefix in archives:
 items=sorted(p for p in root.rglob('*') if p.is_file()) if root!=P else files()
 with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p in items:z.write(p,prefix+'/'+str(p.relative_to(root)))
 with zipfile.ZipFile(target) as z:
  assert z.testzip() is None
  assert {n.split('/')[0] for n in z.namelist()}=={prefix}
  assert target.stat().st_size<100*1024*1024,'GitHub file limit'
  summary.append({'file':target.name,'entries':len(z.namelist()),'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'testzip':True,'topFolder':prefix})
(R/'rhetis-report-forge-archives.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
