"""Portable source checks. This is a review aid, not the unavailable Rhetis intake."""
from pathlib import Path
import argparse,re,json,collections,hashlib
from html.parser import HTMLParser
REF=Path(__file__).resolve().parents[1]/'reference'
REQUIRED={'card':('confetti',['card-2-quiet','card-3-icon3d','card-3-line','card-3-on','card-4','card-5-tone']),'callout':('annual',['callout','callout-icon','callout-stack']),'chart-area':('annual',['area-1','areas-2','areas-stacked-3','area-3pt']),'chart-bar':('confetti',['bars-12','bars-6','bars-3','bars-h-5','bars-h-8','bars-2']),'chart-donut':('amethyst',['donut','donuts-3','donuts-4','donut-0','donut-100']),'chart-line':('amethyst',['lines-12','lines-6','lines-3','lines-flat'])}
class Markup(HTMLParser):
 def __init__(self):super().__init__();self.tags=[];self.depth=0;self.top=[]
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs);self.tags.append((tag,attrs));
  if self.depth==0:self.top.append((tag,attrs))
  if tag not in ['area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr']:self.depth+=1
 def handle_startendtag(self,tag,attrs):self.tags.append((tag,dict(attrs)))
 def handle_endtag(self,tag):self.depth=max(0,self.depth-1)
def check(c):
 name=c.name;issues=[];warn=[];counts=collections.Counter();steps=json.loads((REF/'contract/type-steps.json').read_text());expected_dirs={p.name for p in (REF/'samples/annual/elements').iterdir() if p.is_dir()}
 def error(path,msg):issues.append({'file':str(path.relative_to(c)),'message':msg})
 for p in c.rglob('*'):
  if p.is_file() and p.suffix not in {'.css','.json','.md','.html'}:error(p,'Forbidden file type')
 for f in ['kit/kit.json','kit/css/tokens.css','kit/description.md','foundation/foundation.css','foundation/foundation.json','foundation/description.md']:
  if not (c/f).exists():error(c/f,'Missing required file')
 actual={p.name for p in (c/'elements').iterdir() if p.is_dir()} if (c/'elements').exists() else set()
 for n in sorted(expected_dirs-actual):error(c/'elements'/n,'Missing element')
 for n in sorted(actual-expected_dirs):error(c/'elements'/n,'Unexpected element folder')
 for p in c.rglob('*.json'):
  try:json.loads(p.read_text())
  except Exception as ex:error(p,'Invalid JSON: '+str(ex))
 # Exact metadata contracts are compared against reference folder mappings, not inferred from names.
 for n in sorted(actual & expected_dirs):
  d=c/'elements'/n;counts['elements']+=1
  for fn in ['element.css','element.json','description.md']:
   if not (d/fn).exists():error(d/fn,'Missing required file')
  meta=d/'element.json'
  if meta.exists():
   x=json.loads(meta.read_text());ref=json.loads((REF/'samples/annual/elements'/n/'element.json').read_text())
   if x.get('schema')!='rhetis.design-library-element-source/1' or x.get('contract')!=ref['contract']:error(meta,'Schema or contract mismatch')
   if any(not k.startswith('--'+name+'-') for k in x.get('tokenDefaults',{})):error(meta,'Unprefixed page default variable')
  fixtures=sorted((d/'fixtures').glob('*.html'));counts['fixtures']+=len(fixtures)
  if len(fixtures)<2:error(d/'fixtures','At least 2 fixtures required')
  for f in fixtures:
   text=f.read_text();m=re.match(r'<!--\s*min:\s*([^>]+)-->\s*',text)
   if not m:error(f,'Missing first-line minimum slot declaration')
   parser=Markup();parser.feed(text)
   if len(parser.top)!=1:error(f,f'Expected exactly one root; found {len(parser.top)}')
   for _,a in parser.top:
    if a.get('data-el')!=f'{name}-{n}' and not any(a2.get('data-el')==f'{name}-{n}' for _,a2 in parser.tags):error(f,'Missing scoped element in fixture')
    style=a.get('style','')
    if n not in REQUIRED and (not re.search(r'grid-column\s*:\s*1\s*/\s*span\s*12',style) or not re.search(r'grid-row\s*:\s*1\s*/\s*span\s*6',style)):error(f,'Root fixture placement must be 12x6')
   for tag,a in parser.tags:
    if 'data-el'in a and not a['data-el'].startswith(name+'-'):error(f,'Nested data-el still names another collection')
    classes=set(a.get('class','').split())
    if classes & {'list','tag','hl'}:
     expected='list' if 'list'in classes else 'tag'
     if a.get('data-el')!=f'{name}-{expected}':error(f,'Nested '+expected+' requires its own scoped data-el')
    if tag=='li' and 'item'not in classes:error(f,'Legacy list member lacks .item contract class')
    if 'data-icon'in a and not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',a['data-icon']):error(f,'Invalid Lucide icon name')
    if tag in ['img','svg','script','iframe']:error(f,'Fixture includes image/script/SVG outside contract markup')
  if n in REQUIRED:
   refname,names=REQUIRED[n]
   for fn in names:
    f=d/'fixtures'/(fn+'.html');src=REF/'samples'/refname/'elements'/n/'fixtures'/(fn+'.html')
    if not f.exists():error(f,'Required model fixture missing');continue
    def norm(t):
     t=re.sub(r'^<!--.*?-->\s*','',t,flags=re.S);t=t.replace(refname+'-',name+'-');return re.sub(r'\s+',' ',t).strip()
    if norm(f.read_text())!=norm(src.read_text()):error(f,'Required model markup/data differ (prefix and minimum comment excepted)')
 for p in c.rglob('*.css'):
  s=re.sub(r'/\*.*?\*/','',p.read_text(),flags=re.S)
  if re.search(r'@(import|font-face|keyframes|property)\b|url\s*\(',s,re.I):error(p,'Forbidden at-rule/resource')
  for val in re.findall(r'font-size\s*:\s*([^;}]+)',s):
   if not re.fullmatch(r'var\(--type-(\d+)\)',val.strip()):error(p,'Font size is not a direct type-step token: '+val)
   elif int(re.search(r'\d+',val)[0]) not in steps:error(p,'Invalid type-step: '+val)
  if 'kit/css/tokens.css' not in str(p):
   for prop in ['font-family','font-weight','line-height','letter-spacing']:
    for val in re.findall(r'(?<![-\w])'+prop+r'\s*:\s*([^;}]+)',s):
     if 'var(' not in val and val.strip() not in ['inherit','normal','initial','unset']:error(p,'Literal '+prop+': '+val)
   if re.search(r'#[0-9a-fA-F]{3,8}\b|\b(?:rgb|rgba|hsl|hsla|oklch|oklab)\s*\(',s):error(p,'Literal color outside kit')
   if re.search(r'(?<![-\w])(?:color|background(?:-color)?|border(?:-(?:top|bottom|left|right))?(?:-color)?|fill|stroke)\s*:\s*(?:white|black|gray|grey|red|blue|yellow|green)\b',s):error(p,'Named color outside kit')
  if '/elements/' in str(p):
   n=p.parent.name
   if f'data-el="{name}-{n}"' not in s and f"data-el='{name}-{n}'" not in s:error(p,'Missing element scope')
   # Parse opening-brace preambles. @container conditions are intentionally skipped.
   for selector in re.findall(r'(?:^|[{}])\s*([^{}]+)\{',s):
    if selector.strip().startswith('@'):continue
    if 'data-el='not in selector:warn.append({'file':str(p.relative_to(c)),'message':'Inspect unscoped selector: '+selector.strip()[:160]})
 kit=c/'kit/css/tokens.css'
 if kit.exists():
  tokens=json.loads((REF/'contract/kit-tokens.json').read_text())['tokens'];text=kit.read_text()
  for token in tokens:
   if not re.search(re.escape(token)+r'\s*:',text):error(kit,'Missing shared token '+token)
 result={'collection':name,'counts':dict(counts),'errors':issues,'warnings':warn,'note':'Static review aid; Rhetis intake itself is not included in reference ZIP.'}
 return result
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('collection');a.add_argument('--out');args=a.parse_args();r=check(Path(args.collection).resolve());text=json.dumps(r,ensure_ascii=False,indent=2)
 if args.out:Path(args.out).write_text(text)
 print(json.dumps({'collection':r['collection'],'counts':r['counts'],'errors':len(r['errors']),'warnings':len(r['warnings'])}))
 if not args.out and r['errors']:print(text)
 sys_exit=1 if r['errors'] else 0
 raise SystemExit(sys_exit)
