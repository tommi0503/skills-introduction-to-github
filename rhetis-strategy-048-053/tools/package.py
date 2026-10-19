from pathlib import Path
import zipfile,hashlib,json,shutil
P=Path(__file__).resolve().parents[1];repo=P.parent;out=Path('/codex/browser/projectless/0016-files-mentioned-by-the-user-uploaded-file-pointe/output');can_mirror=out.exists()
files=[]
for name,root in [('strategy-blueprint.zip',P/'strategy-blueprint'),('rhetis-strategy-048-053-deliverables.zip',P)]:
 target=repo/name
 with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for f in sorted(root.rglob('*')):
   if not f.is_file() or any(x in f.parts for x in ['node_modules','__pycache__']):continue
   z.write(f,str(Path(root.name)/f.relative_to(root)))
 with zipfile.ZipFile(target) as z:
  assert z.testzip() is None
  assert {n.split('/')[0] for n in z.namelist()}=={root.name}
  count=len(z.namelist())
 digest=hashlib.sha256(target.read_bytes()).hexdigest();record={'name':name,'bytes':target.stat().st_size,'sha256':digest,'entries':count,'top_level':root.name,'crc_test':'passed'};files.append(record);
 if can_mirror:shutil.copy2(target,out/name)
for f in ([] if not can_mirror else ['preview.html','assembled-preview.html','light.html','dark.html']):shutil.copy2(P/f,out/f)
for f in ([] if not can_mirror else ['direct-all-105.pdf','assembled-all-105.pdf','all-slides-preview.jpg','verification.json']):shutil.copy2(P/'artifacts'/f,out/f)
(repo/'rhetis-strategy-048-053-downloads.json').write_text(json.dumps({'archives':files},indent=2));print(json.dumps(files,indent=2))
