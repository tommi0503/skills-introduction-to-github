from pathlib import Path
import json,re,hashlib
R=Path(__file__).resolve().parent;C=R/'briefing-tab';ref=R/'reference';results={'errors':[],'warnings':[]}
def err(x):results['errors'].append(x)
tax=json.loads((ref/'contract/taxonomy.json').read_text());contracts={p.parent.name:json.loads(p.read_text())['contract'] for p in (ref/'samples/annual/elements').glob('*/element.json')}
folders={p.name for p in (C/'elements').iterdir() if p.is_dir()}
if folders!=set(contracts):err('element folders mismatch '+str(folders^set(contracts)))
steps=json.loads((ref/'contract/type-steps.json').read_text())
for folder,cid in contracts.items():
 p=C/'elements'/folder
 for name in ['element.css','element.json','description.md']:
  if not (p/name).is_file():err(f'{folder}: missing {name}')
 j=json.loads((p/'element.json').read_text())
 if j.get('contract')!=cid:err(f'{folder}: contract mismatch')
 fs=list((p/'fixtures').glob('*.html'))
 if len(fs)<2:err(f'{folder}: <2 fixtures')
 for f in fs:
  t=f.read_text()
  if not re.match(r'<!-- min: [0-9]+x[0-9]+',t):err(str(f)+': missing minimum')
  if 'data-el="briefing-tab-' not in t:err(str(f)+': missing data-el')
  if re.search(r'data-el="(?!briefing-tab-)',t):err(str(f)+': foreign data-el')
  if 'grid-column:1 / span 12' not in t or 'grid-row:1 / span 6' not in t:
   if folder=='callout' and f.stem in ['callout','callout-icon']:results['warnings'].append('Preserved required golden placement: '+folder+'/'+f.stem)
   else:err(str(f)+': top-level placement mismatch')
 css=(p/'element.css').read_text()
 for pattern in [r'#[0-9a-fA-F]{3,8}\b',r'\b(?:rgb|hsl|oklch)\(',r'@(?:import|font-face|keyframes|property)\b',r'\burl\(']:
  if re.search(pattern,css):err(folder+': forbidden CSS '+pattern)
 for m in re.findall(r'var\(--type-([0-9]+)\)',css):
  if int(m)not in steps:err(folder+': invalid type '+m)
 for prop in ['font-size','font-weight','font-family','line-height','letter-spacing']:
  for val in re.findall(r'(?<![\w-])'+prop+r'\s*:\s*([^;}]+)',css):
   if not val.strip().startswith(('var(','calc(','min(','max(','inherit','0')):err(folder+': literal '+prop+' '+val)
 if '@container'not in css:err(folder+': missing container response')
for p in C.rglob('*'):
 if p.is_file() and p.suffix not in {'.css','.json','.md','.html'}:err('forbidden file type '+str(p))
tokens=json.loads((ref/'contract/kit-tokens.json').read_text())['tokens'];t=(C/'kit/css/tokens.css').read_text()
for token in tokens:
 if token+':'not in t and token+' :'not in t:err('missing kit token '+token)
masters={'card':('confetti',['card-2-quiet','card-3-icon3d','card-3-line','card-3-on','card-4','card-5-tone']),'callout':('annual',['callout','callout-icon','callout-stack']),'chart-area':('annual',['area-1','areas-2','areas-stacked-3','area-3pt']),'chart-bar':('confetti',['bars-12','bars-6','bars-3','bars-h-5','bars-h-8','bars-2']),'chart-donut':('amethyst',['donut','donuts-3','donuts-4','donut-0','donut-100']),'chart-line':('amethyst',['lines-12','lines-6','lines-3','lines-flat'])}
for folder,(sample,fixtures) in masters.items():
 for name in fixtures:
  expected=(ref/f'samples/{sample}/elements/{folder}/fixtures/{name}.html').read_text().replace(sample+'-', 'briefing-tab-')
  actual=C/f'elements/{folder}/fixtures/{name}.html'
  # Minimum declaration is metadata; markup and data must remain identical.
  strip=lambda s:re.sub(r'^<!--.*?-->\s*','',s,flags=re.S).strip()
  if not actual.exists() or strip(actual.read_text())!=strip(expected):err(f'golden mismatch {folder}/{name}')
results.update({'element_count':len(folders),'fixture_count':sum(len(list(p.glob('fixtures/*.html'))) for p in (C/'elements').iterdir() if p.is_dir()),'golden_fixture_count':sum(len(x[1])for x in masters.values()),'actual_intake_available':False})
(R/'briefing-tab-review/contract-validation.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));print(json.dumps(results,ensure_ascii=False,indent=2))
