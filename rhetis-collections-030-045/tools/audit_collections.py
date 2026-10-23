"""Independent, non-mutating Rhetis source/artifact audit; run by the lead author."""
from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
import json, re, hashlib, sys
from PIL import Image

BASE=Path(__file__).resolve().parents[1]
REF=BASE
ROOT=BASE/'collections'
NAMES={'030':'chalkline','031':'undertow','033':'cutplane','038':'skylight','043':'arrowtab','045':'blockweave'}
EXPECTED_PAGES={'chalkline':2,'undertow':13,'cutplane':15,'skylight':21,'arrowtab':20,'blockweave':19}
README=(REF/'contract/REFERENCE-README.md').read_text()
CONTRACTS=dict((folder,cid) for cid,folder in re.findall(r'\| `([^`]+@1)` \| `elements/([^/]+)/`',README))
EXEMPLARS={
 'card':('confetti',['card-2-quiet','card-3-icon3d','card-3-line','card-3-on','card-4','card-5-tone']),
 'callout':('annual',['callout','callout-icon','callout-stack']),
 'chart-area':('annual',['area-1','areas-2','areas-stacked-3','area-3pt']),
 'chart-bar':('confetti',['bars-12','bars-6','bars-3','bars-h-5','bars-h-8','bars-2']),
 'chart-donut':('amethyst',['donut','donuts-3','donuts-4','donut-0','donut-100']),
 'chart-line':('amethyst',['lines-12','lines-6','lines-3','lines-flat']),
}

class DOM(HTMLParser):
 def __init__(self,text):
  super().__init__();self.tags=[];self.feed(text)
 def handle_starttag(self,tag,attrs):self.tags.append((tag,dict(attrs)))

def canonical(text):
 # The namespace changes; the min annotation is authoring metadata, not fixture markup/data.
 text=re.sub(r'^<!--\s*min:[^>]*-->\s*','',text)
 text=re.sub(r'data-el="(?:annual|confetti|amethyst|'+ '|'.join(NAMES.values())+r')-', 'data-el="KIT-',text)
 return re.sub(r'\s+',' ',text).strip()

def audit(name):
 p=ROOT/name;rv=BASE/'reviews'/(name+'-review');errors=[];warnings=[];stats={}
 def check(ok,msg):
  if not ok: errors.append(msg)
 check(p.exists(),'missing collection')
 if not p.exists():return dict(collection=name,errors=errors,warnings=warnings)
 files=list(p.rglob('*'));bad=[str(f.relative_to(p)) for f in files if f.is_file() and f.suffix not in {'.css','.json','.md','.html'}]
 check(not bad,'forbidden collection files: '+str(bad))
 actual={x.name for x in (p/'elements').iterdir() if x.is_dir()} if (p/'elements').exists() else set()
 check(actual==set(CONTRACTS),'element folder set: missing '+str(set(CONTRACTS)-actual)+' unexpected '+str(actual-set(CONTRACTS)))
 stats['elements']=len(actual)
 for folder,cid in CONTRACTS.items():
  ep=p/'elements'/folder
  for f in ['element.css','element.json','description.md']:check((ep/f).is_file(),f'{folder}: missing {f}')
  if not (ep/'element.json').exists():continue
  try:
   metadata=json.loads((ep/'element.json').read_text());check(metadata.get('schema')=='rhetis.design-library-element-source/1',folder+': schema');check(metadata.get('contract')==cid,folder+': contract');check(isinstance(metadata.get('registrations'),dict),folder+': registrations');check(isinstance(metadata.get('tokenDefaults'),dict),folder+': tokenDefaults')
  except Exception as e:errors.append(folder+': invalid metadata '+str(e))
  fixtures=list((ep/'fixtures').glob('*.html'))
  check(len(fixtures)>=2,folder+': needs two fixtures')
  for fixture in fixtures:
   txt=fixture.read_text();check(bool(re.match(r'<!--\s*min:\s*\d+x\d+',txt)),str(fixture.relative_to(p))+': missing minimum')
   check('data-el="'+name+'-'+folder+'"' in txt,str(fixture.relative_to(p))+': missing own namespace')
   parsed=DOM(txt)
   mandatory=folder in EXEMPLARS and fixture.stem in EXEMPLARS[folder][1]
   if parsed.tags and not mandatory:
    style=parsed.tags[0][1].get('style','')
    check(bool(re.search(r'grid-column\s*:\s*1\s*/\s*span\s+12',style)),str(fixture.relative_to(p))+': root must span columns 1/12')
    check(bool(re.search(r'grid-row\s*:\s*1\s*/\s*span\s+6',style)),str(fixture.relative_to(p))+': root must span rows 1/6')
   for tag,attrs in parsed.tags:
    if 'data-el' in attrs:check(attrs['data-el'].startswith(name+'-'),str(fixture.relative_to(p))+': foreign data-el '+attrs['data-el'])
    if 'data-icon' in attrs:check(tag in {'span','i','div'},str(fixture.relative_to(p))+': icon tag')
  if folder in EXEMPLARS:
   src,names=EXEMPLARS[folder]
   for stem in names:
    f=ep/'fixtures'/(stem+'.html');check(f.exists(),folder+': missing mandatory '+stem)
    if f.exists():
     orig=REF/'contract/exemplars'/src/'elements'/folder/'fixtures'/(stem+'.html')
     check(canonical(f.read_text())==canonical(orig.read_text()),folder+': modified mandatory markup/data '+stem)
 try:
  kit=json.loads((p/'kit/kit.json').read_text());check(kit.get('id')==name,name+': kit id');check(kit.get('schema')=='rhetis.kit/2',name+': kit schema')
  tokens=(p/'kit'/kit['tokens']).read_text()
  req=json.loads((REF/'contract/kit-tokens.json').read_text())['tokens']
  for token in req:check(bool(re.search(re.escape(token)+r'\s*:',tokens)),'missing token '+token)
  check('.slide.dark' in tokens,'missing dark token preview')
 except Exception as e:errors.append('kit invalid: '+str(e))
 for f in p.rglob('*.css'):
  css=f.read_text();rel=str(f.relative_to(p))
  check(not re.search(r'@(import|font-face|keyframes|property)\b|url\s*\(',css,re.I),rel+': forbidden CSS at-rule/resource')
  if rel!='kit/css/tokens.css':
   check(not re.search(r'#[0-9a-fA-F]{3,8}\b|\b(?:rgb|rgba|hsl|hsla|oklch|oklab)\s*\(',css),rel+': literal color')
  for value in re.findall(r'font-size\s*:\s*([^;}]+)',css):
   check(bool(re.fullmatch(r'var\(--type-(?:\d+)\)',value.strip())),rel+': invalid font-size '+value)
  for prop,value in re.findall(r'(?<![-\w])(font-family|font-weight|line-height|letter-spacing)\s*:\s*([^;}]+)',css):
   check(value.strip().startswith('var('),rel+': untokenized '+prop+' '+value)
  if rel.startswith('elements/'):
   check('@container' in css,rel+': missing container responses')
 try:
  fd=json.loads((p/'foundation/foundation.json').read_text());check(fd.get('kit')==name,'foundation kit');check(fd.get('schema')=='rhetis.design-library-foundation-source/1','foundation schema')
 except Exception as e:errors.append('foundation invalid: '+str(e))
 stats['fixtures']=len(list(p.glob('elements/*/fixtures/*.html')))
 stats['file_count']=sum(f.is_file() for f in files)
 pngs=list(rv.rglob('*.png'));stats['review_png_count']=len(pngs);sizes=Counter()
 for f in pngs:
  try:
   with Image.open(f) as im:
    im.verify()
   with Image.open(f) as im:sizes[str(im.size)]+=1
  except Exception as e:errors.append('bad PNG '+str(f)+': '+str(e))
 stats['png_sizes']=dict(sizes)
 for kind in ['replica','reassembled']:
  pp=list((rv/kind).glob('*.png'));check(len(pp)==EXPECTED_PAGES[name],kind+': wrong page PNG count '+str(len(pp)))
  for f in pp:
   with Image.open(f) as im:check(im.size==(1280,720),kind+': wrong page size '+f.name)
  check((rv/kind/(kind+'.pdf')).is_file(),kind+': missing PDF')
 for kind in ['compare-replica','compare-reassembled']:
  pp=list((rv/kind).glob('*.png'));check(len(pp)==EXPECTED_PAGES[name],kind+': wrong comparison count '+str(len(pp)))
 for mode in ['light','dark']:
  check((rv/'library'/(mode+'.html')).exists(),'missing library/'+mode+'.html')
  check((rv/'library'/('library-'+mode+'.pdf')).exists(),'missing library PDF '+mode)
  for folder in list(CONTRACTS)+['foundation']:
   sheet=rv/'library'/folder/(mode+'.png')
   check(sheet.is_file(),'missing element sheet '+folder+'/'+mode+'.png')
   if sheet.is_file():
    with Image.open(sheet) as im:check(im.width==1280 and im.height>0,'invalid element sheet size '+str(sheet))
 for doc in ['design-language.md','review-notes.md','inventory.md','automatic-checks.json']:check((rv/doc).exists(),'missing '+doc)
 return dict(collection=name,errors=errors,warnings=warnings,stats=stats)

if __name__=='__main__':
 names=sys.argv[1:] or list(NAMES.values());report=[audit(n) for n in names]
 out=BASE/'checks/integration-audit.json';out.write_text(json.dumps(report,ensure_ascii=False,indent=2))
 for row in report:
  print(row['collection'],row.get('stats',{}),'ERRORS',len(row['errors']))
  for err in row['errors']:print(' ',err)
 print('REPORT',out)
