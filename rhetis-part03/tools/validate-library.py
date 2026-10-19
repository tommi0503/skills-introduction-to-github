from pathlib import Path
import json,re
try:import tinycss2
except ImportError:tinycss2=None
R=Path(__file__).resolve().parents[1];C=R/'library/rhetis-report';tx=json.loads((R/'contract/taxonomy.json').read_text());required={x['id'] for x in tx['contracts']};found=set();fail=[];fixturecount=0
for p in sorted(C.glob('elements/*/element.json')):
 j=json.loads(p.read_text());found.add(j['contract']);d=p.parent
 if j['schema']!='rhetis.design-library-element-source/1':fail.append(str(p)+' schema')
 fixtures=list((d/'fixtures').glob('*.html'));fixturecount+=len(fixtures)
 if len(fixtures)<2:fail.append(str(d)+' needs fixtures')
 css=(d/'element.css').read_text()
 if re.search(r'@(?:import|font-face|keyframes|property)\b|url\(',css):fail.append(str(d)+' forbidden CSS resource/at-rule')
 if re.search(r'font-size\s*:\s*(?!var\(--type-)[^v\s]',css):fail.append(str(d)+' non-token font-size')
 if re.search(r'#[0-9a-fA-F]{3,8}\b|(?:rgb|hsl)a?\(',css):fail.append(str(d)+' literal color')
 if not tinycss2:
  for sel in re.findall(r'([^{}]+)\{',css):
   sel=sel.strip()
   if not sel.startswith('@') and f'data-el="rhetis-report-{d.name}"' not in sel:fail.append(str(d)+' selector '+sel)
 if tinycss2:
  def walk(rules):
   for r in rules:
    if r.type=='qualified-rule':
     sel=tinycss2.serialize(r.prelude)
     if f'data-el="rhetis-report-{d.name}"'not in sel:fail.append(str(d)+' selector '+sel)
    elif r.type=='at-rule'and r.content:walk(tinycss2.parse_rule_list(r.content))
  walk(tinycss2.parse_stylesheet(css,skip_whitespace=True,skip_comments=True))
 for f in fixtures:
  s=f.read_text()
  if not re.match(r'<!-- min: \d+x\d+',s):fail.append(str(f)+' missing minimum')
  if 'data-el="rhetis-report-'+d.name+'"'not in s:fail.append(str(f)+' data-el')
tokens=json.loads((R/'contract/kit-tokens.json').read_text())['tokens'];css=(C/'kit/css/tokens.css').read_text();dark=css.split('.slide.dark',1)[1]
for k,v in tokens.items():
 if k+':'not in css:fail.append('missing token '+k)
 if v=='color'and k+':'not in dark:fail.append('missing dark token '+k)
if found!=required:fail.append({'missingContracts':sorted(required-found),'unexpected':sorted(found-required)})
out={'elements':len(found),'elementFixtures':fixturecount,'foundationFixtures':len(list((C/'foundation/fixtures').glob('*.html'))),'staticFailures':fail,'scopeSelectorsChecked':True};(R/'review/library-contract-audit.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2));assert not fail
