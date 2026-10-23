"""Produce final source-matched renders only after a collection's fidelity source is frozen."""
from pathlib import Path
import subprocess,sys,json,time
ROOT=Path(__file__).resolve().parent
for kid in sys.argv[1:]:
 P=ROOT/(kid+'-project');events=[]
 def command(script,*args):
  cmd=[sys.executable,str(ROOT/script),*args];start=time.time();subprocess.run(cmd,cwd=ROOT,check=True);events.append({'script':script,'args':args,'seconds':round(time.time()-start,1)})
 command('integrate_runtime.py',kid)
 command('validate.py',kid)
 assert not json.loads((P/'contract-audit.json').read_text())['errors']
 command('check_resources.py',kid)
 assert not json.loads((P/'portable-resources.json').read_text())['errors']
 command('qa/audit_css.py',kid)
 assert json.loads((ROOT/'qa'/(kid+'-audit.json')).read_text())['summary']['error']==0
 command('render.py',kid,'all')
 command('official_preview.py',kid)
 command('fidelity.py',kid)
 (P/'finalize-status.json').write_text(json.dumps({'collection':kid,'status':'rendered; manual fidelity acceptance is separate','completedAtUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'commands':events},ensure_ascii=False,indent=2))
 print(kid,'FINAL SOURCE-MATCHED OUTPUT COMPLETE',flush=True)
