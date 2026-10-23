"""Execute the exact provided preview CLI and prove its HTML equals the rendered sheet input."""
from pathlib import Path
import subprocess,sys,json,hashlib
ROOT=Path(__file__).resolve().parent;REF=Path('/workspace/work/reference') if Path('/workspace/work/reference').exists() else ROOT/'reference'
for kid in sys.argv[1:]:
 P=ROOT/(kid+'-project');report=[]
 for mode in ['light','dark']:
  out=P/'library'/(mode+'.html');old=out.read_bytes()
  args=[sys.executable,str(REF/'tools/preview.py'),str(P/kid),str(REF/'contract/type-steps.json'),'--out',str(out),'--fonts',str(P/'assets/fonts/fonts.css')]
  if mode=='dark':args.append('--dark')
  subprocess.run(args,check=True,capture_output=True)
  text=out.read_text().replace((P/'assets/fonts/fonts.css').as_uri(),'../assets/fonts/fonts.css');out.write_text(text)
  assert old==out.read_bytes(),(kid,mode,'CLI output differs from rendered source; rerender required')
  report.append({'mode':mode,'command':args,'identicalToRenderedInput':True,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()})
 (P/'preview-build.json').write_text(json.dumps(report,indent=2))
 print(kid,'official CLI light/dark identical',flush=True)
