"""Verify every portable review HTML/CSS local resource stays inside its project."""
from pathlib import Path
import re,sys,json
ROOT=Path(__file__).resolve().parent
for kid in sys.argv[1:]:
 P=ROOT/(kid+'-project');bad=[];checked=0
 for stage in ['replica','reassembled','assets']:
  for f in (P/stage).rglob('*'):
   if not f.is_file() or f.suffix not in ['.html','.css']:continue
   source=f.read_text();refs=re.findall(r'''(?:href|src)=["']([^"']+)["']''',source) if f.suffix=='.html' else re.findall(r'''url\(\s*["']?([^)'"\s]+)''',source)
   for ref in refs:
    if ref.startswith(('https:','http:','data:','#')):continue
    target=(f.parent/ref.split('?')[0].split('#')[0]).resolve();checked+=1
    if not target.is_relative_to(P.resolve()) or not target.is_file():bad.append({'source':str(f.relative_to(P)),'ref':ref,'exists':target.is_file(),'insideProject':target.is_relative_to(P.resolve())})
 report={'collection':kid,'checked':checked,'errors':bad};(P/'portable-resources.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(kid,'checked',checked,'errors',len(bad));
 for item in bad[:3]:print(item)
