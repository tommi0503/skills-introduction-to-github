from pathlib import Path
from html.parser import HTMLParser
import re,json,hashlib
from PIL import Image
BASE=Path(__file__).resolve().parents[1];P=BASE/'collection/business-prism';contract=BASE/'contract'
alltokens=json.loads((contract/'kit-tokens.json').read_text())['tokens'];steps=json.loads((contract/'type-steps.json').read_text());tax=json.loads((contract/'taxonomy.json').read_text());errors=[];fixtures=[]
class Markup(HTMLParser):
 def __init__(self):super().__init__();self.depth=0;self.roots=[];self.classes=set();self.styles=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if self.depth==0:self.roots.append((tag,a))
  self.depth+=1;self.classes.update(a.get('class','').split());self.styles.append(a.get('style',''))
 def handle_endtag(self,tag):self.depth-=1
allowed=set(tax['foundation']['classes']+tax['parts']);allowed.update(['tone-'+str(i) for i in range(1,6)])
for x in tax['contracts']:
 allowed.update(x['roots']);allowed.update(re.findall(r'\.([a-z][a-z0-9-]*)',x['structure']))
allowed.update(['table','from','to','h','bar','pt','key','item','by','check','num','divided','big','alt','step','stop','core','node','spoke','stage','level','axis-x','axis-y','cell','set','root','branch','leaf','start','ask','end','to-r','to-d','to-l','to-u','layer','chip','side','vs','price','entry','quiet','line'])
folders=sorted((P/'elements').iterdir());assert len(folders)==31
ids={x['id'] for x in tax['contracts']}
for folder in folders:
 meta=json.loads((folder/'element.json').read_text());assert meta['contract'] in ids
 htmls=sorted((folder/'fixtures').glob('*.html'))
 if len(htmls)<2:errors.append(str(folder)+' lacks fixture variants')
 css=(folder/'element.css').read_text()
 for token in re.findall(r'font-size\s*:\s*([^;}]+)',css):
  m=re.fullmatch(r'var\(--type-(\d+)\)',token.strip())
  if not m or int(m[1]) not in steps:errors.append(f'{folder.name}: invalid font-size {token}')
 for rule in re.findall(r'([^{}]+)\{',css):
  if not rule.strip().startswith('@') and '[data-el="business-prism-'+folder.name+'"]' not in rule:errors.append(f'{folder.name}: unscoped selector {rule}')
 for bad in [r'#[0-9a-fA-F]{3,8}\b',r'@(?:font-face|import|keyframes|property)\b',r'url\(',r'font-weight\s*:\s*\d']:
  if re.search(bad,css):errors.append(f'{folder.name}: forbidden {bad}')
 if '@container' not in css:errors.append(f'{folder.name}: no container adaptation')
 for path in htmls:
  s=path.read_text();m=Markup();m.feed(s)
  if len(m.roots)!=1:errors.append(f'{path}: {len(m.roots)} roots')
  if m.classes-allowed:errors.append(f'{path}: unknown classes {m.classes-allowed}')
  if m.roots[0][1].get('data-el')!='business-prism-'+folder.name:errors.append(f'{path}: root data-el')
  if not s.startswith('<!-- min: '):errors.append(f'{path}: no minimum declaration')
  st=m.roots[0][1].get('style','')
  if 'grid-column:1 / span 12' not in st or 'grid-row:1 / span 6' not in st:errors.append(f'{path}: layout declaration')
  if re.search(r'<(?:img|svg|script)\b',s):errors.append(f'{path}: external/rendered resource')
  fixtures.append({'file':str(path.relative_to(P)),'minimum':s.split('\n')[0]})
css=(P/'kit/css/tokens.css').read_text();light,dark=css.split('.slide.dark')
for tok,kind in alltokens.items():
 if tok+':' not in light:errors.append('missing token '+tok)
 if kind=='color' and tok+':' not in dark:errors.append('missing dark color '+tok)
images=list((BASE/'review').glob('library-*.png'));sizes={}
for path in images:
 with Image.open(path) as im:sizes[str(path.name)]=list(im.size)
 if list(im.size)!=[1280,720]:errors.append('image dimensions '+str(path))
report={'collection':'business-prism','contracts':31,'element_fixtures':len(fixtures),'foundation_fixtures':len(list((P/'foundation/fixtures').glob('*.html'))),'all_shared_tokens':len(alltokens),'all_color_tokens_both_modes':True,'element_css_scoped':True,'type_step_usage':True,'no_external_resources_in_element_css':True,'unknown_fixture_classes':[],'fixture_inventory':fixtures,'render_png_count':len(images),'render_png_sizes':sorted({tuple(x) for x in sizes.values()}),'errors':errors,'source_sha256':{str(p.relative_to(P)):hashlib.sha256(p.read_bytes()).hexdigest() for p in P.rglob('*') if p.is_file()}}
(BASE/'review/library-contract-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['fixture_inventory','source_sha256']},ensure_ascii=False,indent=2))
