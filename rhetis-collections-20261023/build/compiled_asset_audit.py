"""Check that review HTML actually embeds/links every final library CSS source."""
from pathlib import Path
import re,json,sys,hashlib
BASE=Path('/workspace/output');WORK=Path('/workspace/work/integration')
names=sys.argv[1:] or ['fluxweave','cyanloop','roundrise','nightchamfer','glasspulse']
norm=lambda x:re.sub(r'\s+','',re.sub(r'/\*.*?\*/','',x,flags=re.S))
records=[]
for name in names:
 root=BASE/name;review=BASE/(name+'-review');errors=[];checks=[]
 inputs=[root/'kit/css/tokens.css',root/'foundation/foundation.css']+sorted(root.glob('elements/*/element.css'))
 htmls=sorted((review/'reassembled').glob('slide*.html'))+[review/'library/light.html',review/'library/dark.html']
 for html in htmls:
  text=html.read_text();combined='\n'.join(re.findall(r'<style[^>]*>(.*?)</style>',text,flags=re.S))
  for ref in re.findall(r'<link[^>]+href=["\']([^"\']+)',text):
   if 'fonts.css' not in ref and not ref.startswith(('http:','https:')):combined+='\n'+(html.parent/ref).resolve().read_text()
  compiled=norm(combined);missing=[str(f.relative_to(root)) for f in inputs if norm(f.read_text()) not in compiled]
  if missing:errors.append({'html':str(html.relative_to(review)),'missing_latest_css':missing})
  checks.append({'html':str(html.relative_to(review)),'css_inputs_verified':len(inputs)-len(missing)})
 record={'collection':name,'errors':errors,'checks':checks,'source_sha256':{str(f.relative_to(root)):hashlib.sha256(f.read_bytes()).hexdigest() for f in inputs}};records.append(record)
 print(name,len(htmls),'HTML',len(errors),'stale compiled asset errors')
(WORK/'compiled-asset-audit.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
