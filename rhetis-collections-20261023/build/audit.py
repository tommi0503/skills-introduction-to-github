import json,re,sys,zipfile,hashlib
from pathlib import Path
from html.parser import HTMLParser
from PIL import Image
REF=Path('/workspace/work/reference')
NAMES=['fluxweave','cyanloop','roundrise','nightchamfer','glasspulse']
CONTRACTS=json.loads((REF/'contract/taxonomy.json').read_text())['contracts']
REQTOK=json.loads((REF/'contract/kit-tokens.json').read_text())['tokens']
STEPS=json.loads((REF/'contract/type-steps.json').read_text())
GOLD={
 'card':('confetti',['card-2-quiet','card-3-icon3d','card-3-line','card-3-on','card-4','card-5-tone']),
 'callout':('annual',['callout','callout-icon','callout-stack']),
 'chart-area':('annual',['area-1','areas-2','areas-stacked-3','area-3pt']),
 'chart-bar':('confetti',['bars-12','bars-6','bars-3','bars-h-5','bars-h-8','bars-2']),
 'chart-donut':('amethyst',['donut','donuts-3','donuts-4','donut-0','donut-100']),
 'chart-line':('amethyst',['lines-12','lines-6','lines-3','lines-flat'])}
def normalize(s):
 return re.sub(r'data-el="[^"\s]+"','data-el="COLLECTION"',s).strip()
def split_selectors(selector):
 parts=[];start=0;depth=0;quote=None
 for i,c in enumerate(selector):
  if quote:
   if c==quote and (i==0 or selector[i-1]!='\\'):quote=None
  elif c in ['"',"'"]:quote=c
  elif c in '([':depth+=1
  elif c in ')]':depth-=1
  elif c==',' and depth==0:parts.append(selector[start:i]);start=i+1
 parts.append(selector[start:]);return parts

def audit(root):
 result={'collection':root.name,'errors':[],'warnings':[],'counts':{}}
 def err(msg): result['errors'].append(msg)
 def warn(msg): result['warnings'].append(msg)
 def read(p):
  if not p.is_file(): err('Missing '+str(p.relative_to(root)));return ''
  return p.read_text()
 if not root.exists(): err('Missing collection');return result
 for p in root.rglob('*'):
  if p.is_file() and p.suffix not in {'.css','.json','.md','.html'}:err('Disallowed file '+str(p.relative_to(root)))
 kit=json.loads(read(root/'kit/kit.json') or '{}')
 if kit.get('id')!=root.name or kit.get('schema')!='rhetis.kit/2':err('kit id/schema')
 read(root/'kit/description.md')
 tok=read(root/'kit/css/tokens.css')
 for t in REQTOK:
  if t+':' not in tok and not re.search(re.escape(t)+r'\s*:',tok):err('Missing shared token '+t)
 for kind,folder in [('foundation',root/'foundation')]+[('element',p) for p in sorted((root/'elements').glob('*')) if p.is_dir()]:
  desc=read(folder/'description.md')
  if re.search(r'[가-힣]',desc):warn(str(folder.relative_to(root))+' description should be English')
  meta=json.loads(read(folder/(kind+'.json')) or '{}')
  expected='rhetis.design-library-'+('foundation' if kind=='foundation' else 'element')+'-source/1'
  if meta.get('schema')!=expected:err(str(folder.relative_to(root))+' schema')
  css=read(folder/(kind+'.css'))
  clean=re.sub(r'/\*.*?\*/','',css,flags=re.S)
  if re.search(r'#[0-9a-fA-F]{3,8}\b|\b(?:rgb|rgba|hsl|hsla|oklch|lab|lch)\s*\(',clean):err(str(folder.relative_to(root))+' color literal')
  if re.search(r'@(?:import|font-face|keyframes|property)\b|url\s*\(',clean):err(str(folder.relative_to(root))+' forbidden at-rule/resource')
  for prop,value in re.findall(r'([a-z-]+)\s*:\s*([^;{}]+)',clean):
   if re.search(r'(?<![-\w])(?:white|black|red|blue|gray|grey|transparent)(?![-\w])',value,re.I):err(str(folder.relative_to(root))+' named color literal '+value)
   if prop=='font-size' and not re.fullmatch(r'var\(--type-(\d+)\)(?:\s*!important)?',value.strip()):err(str(folder.relative_to(root))+' font-size '+value)
   if prop in ['font-family','line-height','letter-spacing'] and 'var(' not in value:err(str(folder.relative_to(root))+' literal typography '+prop+':'+value)
   if prop in ['padding','padding-top','padding-bottom','padding-left','padding-right','margin','margin-top','margin-bottom','margin-left','margin-right','gap','row-gap','column-gap'] and re.search(r'[1-9]\d*(?:px|em|rem)',value):warn(str(folder.relative_to(root))+' literal spacing '+prop+':'+value)
   if prop=='font-weight' and re.search(r'\d',value) and 'var(' not in value:err(str(folder.relative_to(root))+' literal font-weight')
  fixtures=sorted((folder/'fixtures').glob('*.html'))
  if len(fixtures)<(1 if kind=='foundation' else 2):err(str(folder.relative_to(root))+' insufficient fixtures')
  if kind=='element':
   if '@container' not in clean:warn(folder.name+' missing responsive @container')
   token='data-el="'+root.name+'-'+folder.name+'"'
   if token not in css and token.replace('"',"'") not in css:err(folder.name+' missing data-el CSS scope')
   for selector in re.findall(r'([^{}]+)\{',clean):
    selector=selector.strip()
    if selector.startswith('@'):continue
    for sel in split_selectors(selector):
     if 'data-el=' not in sel:warn(folder.name+' possible unscoped selector '+sel[:100])
   for f in fixtures:
    s=f.read_text()
    if not re.match(r'<!--\s*min:\s*\d+x\d+',s):err(str(f.relative_to(root))+' missing min')
    if token not in s:err(str(f.relative_to(root))+' missing data-el')
  if folder.name in GOLD:
   sample,ids=GOLD[folder.name]
   for id in ids:
    f=folder/'fixtures'/(id+'.html')
    if not f.exists():err(folder.name+' missing gold '+id);continue
    src=(REF/'samples'/sample/'elements'/folder.name/'fixtures'/(id+'.html')).read_text()
    # min declaration may be tailored to the new design; DOM/data cannot.
    stripmin=lambda s: re.sub(r'\A<!--.*?-->\s*','',s,flags=re.S)
    if normalize(stripmin(src))!=normalize(stripmin(f.read_text())):err(folder.name+' gold markup/data mismatch '+id)
 result['counts']['elements']=len(list((root/'elements').glob('*/element.json')))
 result['counts']['fixtures']=len(list(root.glob('**/fixtures/*.html')))
 if result['counts']['elements']!=56:err('Expected 56 elements')
 ids={json.loads(p.read_text()).get('contract') for p in root.glob('elements/*/element.json')}
 if ids!={c['id'] for c in CONTRACTS}:err('Contract IDs mismatch')
 return result
if __name__=='__main__':
 reports=[audit(Path('/workspace/output')/n) for n in (sys.argv[1:] or NAMES)]
 Path('/workspace/work/integration/static-audit.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2))
 for r in reports:
  print(r['collection'],r['counts'],len(r['errors']),'errors',len(r['warnings']),'warnings')
  for e in r['errors'][:50]:print('ERROR',e)
  for e in r['warnings'][:10]:print('WARN',e)
