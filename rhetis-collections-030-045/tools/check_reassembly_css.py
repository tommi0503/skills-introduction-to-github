from pathlib import Path
import re,json
base=Path(__file__).resolve().parents[1]/'collections';reviews=base.parent/'reviews';results=[]
def norm(s):return re.sub(r'\s+','',re.sub(r'/\*.*?\*/','',s,flags=re.S))
for name in ['chalkline','undertow','cutplane','skylight','arrowtab','blockweave']:
 issues=[];cnt=0
 for f in (reviews/(name+'-review')/'reassembled').glob('*.html'):
  if f.name=='index.html':continue
  cnt+=1;s=f.read_text();css='\n'.join(re.findall(r'<style[^>]*>(.*?)</style>',s,re.S))
  for link in re.findall(r'<link[^>]+href="([^"]+)"',s):
   p=(f.parent/link).resolve()
   if p.exists():css+='\n'+p.read_text()
  big=norm(css)
  for folder in sorted(set(re.findall(r'data-el="'+name+r'-([\w-]+)"',s))):
   ep=base/name/'elements'/folder/'element.css'
   if not ep.exists():issues.append([f.name,'unknown element '+folder]);continue
   if norm(ep.read_text())not in big:issues.append([f.name,'loaded CSS differs from final collection: '+folder])
  for part in ['kit/css/tokens.css','foundation/foundation.css']:
   if norm((base/name/part).read_text())not in big:issues.append([f.name,'loaded CSS differs: '+part])
  # The review host supplies only fonts, palette/type values and viewport reset.
  # Reject extra page-specific design declarations, even when all source CSS is also present.
  extra=big
  for ep in sorted((base/name).rglob('*.css'),key=lambda p:-len(p.read_text())):
   extra=extra.replace(norm(ep.read_text()),'')
  for jp in (base/name).rglob('*.json'):
   for registered in json.loads(jp.read_text()).get('registrations',{}).values():extra=extra.replace(norm(registered),'')
  extra=re.sub(r'@font-face\{[^}]*\}','',extra)
  extra=re.sub(r'--[\w-]+:[^;}]*;?','',extra)
  extra=re.sub(r'\.slide(?:\.dark)?\{\}','',extra)
  extra=re.sub(r'(?:html,body|body)\{(?:margin:0;?|padding:0;?|width:1280px;?|height:720px;?|overflow:hidden;?)*\}','',extra)
  extra=re.sub(r'[^{};]+\{\}','',extra) # Empty rules have no rendering effect.
  if extra:issues.append([f.name,'extra page design CSS',extra[:400]])
 results.append({'collection':name,'pages':cnt,'issues':issues})
 print(name,cnt,'pages,',len(issues),'differences',issues[:4])
(base.parent/'checks/integration-reassembly-css-audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
