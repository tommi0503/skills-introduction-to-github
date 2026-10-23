from pathlib import Path
import subprocess,json
W=Path('/workspace/work/integration');dest=W/'build-check';dest.mkdir(exist_ok=True);records=[]
for name in ['fluxweave','cyanloop','roundrise','nightchamfer','glasspulse']:
 for mode in ['light','dark']:
  out=dest/f'{name}-{mode}.html';cmd=['python','/workspace/work/reference/tools/preview.py','/workspace/output/'+name,'/workspace/work/reference/contract/type-steps.json','--out',str(out)]
  if mode=='dark':cmd.append('--dark')
  run=subprocess.run(cmd,capture_output=True,text=True);records.append({'collection':name,'mode':mode,'command':cmd,'exit_code':run.returncode,'html_bytes':out.stat().st_size if out.exists() else 0,'stderr':run.stderr})
(W/'build-check.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
assert all(r['exit_code']==0 and r['html_bytes'] for r in records),records
print('preview.py: 10 of 10 light/dark builds passed')
