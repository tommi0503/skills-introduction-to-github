"""Record a primary-agent decision after individually viewing named final comparison images."""
from pathlib import Path
import sys,json,hashlib,time
from render import ROOT
kid,status,notes,*pages=sys.argv[1:]
assert status in ['accepted','needs-fix'] and pages
P=ROOT/(kid+'-project');f=P/'fidelity/primary-review.json';report=json.loads(f.read_text()) if f.exists() else {'collection':kid,'scope':'Primary-agent individual three-way visual review. This does not assert pixel identity; permitted media/icon/font substitutions are recorded separately.','pages':{}}
for page in pages:
 name='slide_'+page.zfill(2);pic=P/'fidelity'/(name+'-triple.png');assert pic.exists()
 report['pages'][name]={'status':status,'notes':notes,'comparisonSha256':hashlib.sha256(pic.read_bytes()).hexdigest(),'reviewedAtUTC':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
f.write_text(json.dumps(report,ensure_ascii=False,indent=2));print(kid,len(report['pages']),'individual pages recorded')
