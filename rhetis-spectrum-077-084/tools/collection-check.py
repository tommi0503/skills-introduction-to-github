"""Portable source-contract checks; does not claim Rhetis importer admission."""
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];C=ROOT/'collection/rhetis-spectrum';issues=[];rows=[]
if not C.exists():raise SystemExit('collection missing')
required=json.loads((ROOT/'contract/kit-tokens.json').read_text())['tokens'];tokens=(C/'kit/css/tokens.css').read_text();steps=json.loads((ROOT/'contract/type-steps.json').read_text());kit=json.loads((C/'kit/kit.json').read_text())
for k in required:
 if k not in tokens:issues.append('missing token '+k)
 if required[k]=='color' and len(re.findall(re.escape(k)+r'\s*:',tokens))<2:issues.append('missing dark token '+k)
for folder in sorted((C/'elements').iterdir()):
 if not folder.is_dir():continue
 name=folder.name;css=(folder/'element.css').read_text();meta=json.loads((folder/'element.json').read_text());fixtures=list((folder/'fixtures').glob('*.html'))
 if len(fixtures)<2:issues.append(name+' fewer than 2 fixtures')
 if '@container' not in css:issues.append(name+' missing container query')
 for bad in ['@import','url(', '@font-face','@keyframes']:
  if bad in css:issues.append(name+' forbidden '+bad)
 if re.search(r'#[0-9a-fA-F]{3,8}\b|\brgba?\s*\(|\bhsla?\s*\(',css):issues.append(name+' literal color')
 if re.search(r'font-size\s*:\s*(?!var\(--type-)',css):issues.append(name+' non-type font size')
 if re.search(r'font-weight\s*:\s*\d',css):issues.append(name+' literal font weight')
 # Every ordinary selector should include this element's exact scope.
 stripped=re.sub(r'/\*.*?\*/','',css,flags=re.S)
 for selector in re.findall(r'([^{}]+)\{',stripped):
  if selector.strip().startswith('@'):continue
  if 'data-el="rhetis-spectrum-'+name+'"' not in selector and "data-el='rhetis-spectrum-"+name+"'" not in selector:issues.append(name+' unscoped selector '+selector[:100])
 for f in fixtures:
  text=f.read_text()
  if not re.match(r'<!--\s*min:',text):issues.append(str(f.relative_to(C))+' missing minimum')
  if 'data-el="rhetis-spectrum-'+name+'"' not in text:issues.append(str(f.relative_to(C))+' missing root scope')
  if not re.search(r'grid-column\s*:\s*1\s*/\s*span\s*12',text):issues.append(str(f.relative_to(C))+' missing layout')
 rows.append({'element':name,'fixtures':len(fixtures),'contract':meta['contract']})
if len(rows)!=31:issues.append('element count !=31')
result={'success':not issues,'kit':kit['id'],'elements':rows,'elementCount':len(rows),'fixtureCount':sum(x['fixtures']for x in rows),'issues':issues};(ROOT/'review/collection-contract-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(bool(issues))
