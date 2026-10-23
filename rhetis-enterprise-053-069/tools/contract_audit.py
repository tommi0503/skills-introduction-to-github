from pathlib import Path
import json,re
B=Path(__file__).resolve().parents[1];ref=B;contracts=json.load(open(ref/'contract/taxonomy.json'))['contracts'];tokens=json.load(open(ref/'contract/kit-tokens.json'))['tokens'];results={}
for C in B.iterdir():
 if not (C/'kit/kit.json').exists():continue
 issues=[]
 if len(list((C/'elements').iterdir()))!=56:issues.append('element count')
 tk=(C/'kit/css/tokens.css').read_text()
 for t in tokens:
  if t+':' not in tk and not re.search(re.escape(t)+r'\s*:',tk):issues.append('missing token '+t)
 for co in contracts:
  name=co['category'].split('.')[-1];E=C/'elements'/name
  for file in ['element.css','element.json','description.md']:
   if not (E/file).exists():issues.append(name+' missing '+file)
  if not E.exists():continue
  if len(list((E/'fixtures').glob('*.html')))<2:issues.append(name+' fewer than 2 fixtures')
  s=(E/'element.css').read_text()
  if re.search(r'#[0-9a-fA-F]{3,8}\b|\b(?:rgb|oklch|hsl)a?\(',s):issues.append(name+' color literal')
  if re.search(r'font-size\s*:\s*(?!var\()\d',s):issues.append(name+' literal font-size')
  if re.search(r'@(?:import|font-face|keyframes)\b|url\(',s):issues.append(name+' forbidden at-rule or url')
  if json.load(open(E/'element.json'))['contract']!=co['id']:issues.append(name+' contract id')
  for f in (E/'fixtures').glob('*.html'):
   text=f.read_text()
   if not text.startswith('<!-- min:'):issues.append(str(f.relative_to(C))+' min missing')
   if 'data-el="'+C.name+'-'+name+'"' not in text:issues.append(name+' data-el missing in '+f.name)
 results[C.name]={'elements':len(list((C/'elements').iterdir())),'fixtures':len(list((C/'elements').glob('*/fixtures/*.html'))),'issues':issues}
print(json.dumps(results,ensure_ascii=False,indent=2));(B/'contract-audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
