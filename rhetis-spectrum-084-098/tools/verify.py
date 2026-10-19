"""Check final browser evidence, collection contract, dimensions and reproducibility."""
from pathlib import Path
from html.parser import HTMLParser
import json,re,hashlib,sys
from PIL import Image,ImageChops
import fitz
ROOT=Path(__file__).resolve().parents[1];C=ROOT/'collection/spectrum-brief'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def collection_hash():return hashlib.sha256(b''.join(p.read_bytes()for p in sorted(C.rglob('*'))if p.is_file())).hexdigest()
class Fragment(HTMLParser):
 def __init__(self):super().__init__();self.depth=0;self.roots=[];self.nodes=[]
 def handle_starttag(self,tag,attrs):
  self.nodes.append((tag,dict(attrs)))
  if self.depth==0:self.roots.append((tag,dict(attrs)))
  if tag not in ['br','hr','img','input','meta','link']:self.depth+=1
 def handle_endtag(self,tag):self.depth=max(0,self.depth-1)
def rules(css):
 css=re.sub(r'/\*.*?\*/','',css,flags=re.S);pos=0
 while pos<len(css):
  left=css.find('{',pos)
  if left<0:return
  header=css[pos:left].strip();level=1;right=left+1
  while right<len(css)and level:
   if css[right]=='{':level+=1
   elif css[right]=='}':level-=1
   right+=1
  body=css[left+1:right-1]
  if header.startswith('@'):yield from rules(body)
  else:yield header,body
  pos=right

def check_collection(fail):
 contracts={c['id'] for c in json.loads((ROOT/'contract/taxonomy.json').read_text())['contracts']};found=set();fixtures=0
 kit=json.loads((C/'kit/kit.json').read_text());tokens=(C/'kit/css/tokens.css').read_text();required=json.loads((ROOT/'contract/kit-tokens.json').read_text())['tokens'];blocks=dict(rules(tokens))
 if kit['schema']!='rhetis.kit/2'or kit['id']!='spectrum-brief':fail.append('kit schema/id')
 for token,kind in required.items():
  if token+':'not in blocks.get('.slide','').replace(' ', ''):fail.append('missing light token '+token)
  if kind=='color'and token+':'not in blocks.get('.slide.dark','').replace(' ',''):fail.append('missing dark color '+token)
 steps=json.loads((ROOT/'contract/type-steps.json').read_text())
 for element in sorted((C/'elements').iterdir()):
  j=json.loads((element/'element.json').read_text());found.add(j['contract']);css=(element/'element.css').read_text();fs=list((element/'fixtures').glob('*.html'));fixtures+=len(fs)
  if j['schema']!='rhetis.design-library-element-source/1':fail.append('element schema '+element.name)
  if len(fs)<2:fail.append('fixture count '+element.name)
  if '@container'not in css:fail.append('no container step '+element.name)
  if re.search(r'@(?:import|font-face|keyframes|property)\b|url\s*\(',css):fail.append('forbidden at-rule/resource '+element.name)
  for sel,body in rules(css):
   # Every selector branch is scoped; :is() commas are not selector branches.
   if f'[data-el="spectrum-brief-{element.name}"]'not in sel:fail.append('unscoped selector '+element.name+': '+sel)
   if re.search(r'#[0-9a-fA-F]{3,8}\b|\brgba?\s*\(|\bhsla?\s*\(',body):fail.append('literal color '+element.name)
   for v in re.findall(r'font-size\s*:\s*([^;}]+)',body):
    m=re.fullmatch(r'var\(--type-(\d+)\)',v.strip())
    if not m or int(m[1])not in steps:fail.append('font-size step '+element.name+': '+v)
   for prop in ['font-family','font-weight','line-height','letter-spacing','border-radius','padding','margin','gap','row-gap','column-gap']:
    for v in re.findall(r'(?<![-\w])'+prop+r'\s*:\s*([^;}]+)',body):
     if re.search(r'(?<![-\w])(?:[1-9]\d*|0\.\d+)(?:px|rem|em)?\b',re.sub(r'var\([^)]*\)','',v))and not(prop=='border-radius'and v.strip()=='999px'):fail.append('non-token '+element.name+' '+prop+': '+v)
  for f in fs:
   text=f.read_text();p=Fragment();p.feed(text)
   if not re.match(r'^<!-- min: \d+x\d+(?: \| \d+x\d+)* -->\n',text):fail.append('minimum comment '+str(f.relative_to(C)))
   if len(p.roots)!=1:fail.append('fixture root count '+str(f.relative_to(C)))
   elif not any(n[1].get('data-el')=='spectrum-brief-'+element.name for n in p.nodes):fail.append('fixture scope '+str(f.relative_to(C)))
   elif not re.search(r'grid-column:\s*1\s*/\s*span 12;\s*grid-row:\s*1\s*/\s*span 6',p.roots[0][1].get('style','')):fail.append('fixture grid '+str(f.relative_to(C)))
 if found!=contracts:fail.append('contract coverage mismatch')
 f=json.loads((C/'foundation/foundation.json').read_text())
 if f['schema']!='rhetis.design-library-foundation-source/1'or f['kit']!='spectrum-brief':fail.append('foundation schema')
 return {'elements':len(found),'fixtures':fixtures,'foundationFixtures':len(list((C/'foundation/fixtures').glob('*.html'))),'kit':'spectrum-brief'}

def main():
 inv=json.loads((ROOT/'provenance/input-manifest.json').read_text());decks=sorted(set(r['deck']for r in inv));fail=[];rows=[];differences=[]
 library=check_collection(fail)
 main_review=json.loads((ROOT/'review/main-review.json').read_text())
 if len(main_review['pages'])!=109 or not all(r['individualReferenceReplicaComparisonViewed']for r in main_review['pages']):fail.append('main individual review coverage')
 if main_review['libraryReview']['currentCollectionSha256']!=collection_hash():fail.append('main library review stale')
 metrics=json.loads((ROOT/'review/library-metrics.json').read_text())
 if len(metrics)!=144:fail.append('library browser coverage')
 for r in metrics:
  m=r['full']
  if not m['fonts']or m['size']!=[1280,720]or m['minText']<14 or any(m[k]for k in ['overflows','contrastIssues','textOutsideSlide']):fail.append('library browser finding '+r['mode']+'/'+r['fixture'])
  if r['minimum']and r['minimum']['overflows']:fail.append('library minimum overflow '+r['fixture'])
 if not json.loads((ROOT/'review/gallery-check.json').read_text())['success']:fail.append('gallery browser check')
 for mode in ['replica','assembly']:
  for deck in decks:
   f=ROOT/'review'/f'automatic-final-{mode}-{deck}.json'
   if not f.exists():fail.append('missing final report '+f.name);continue
   report=json.loads(f.read_text())
   for key,path in [('rendererHash','src/renderer.mjs'),('primitiveHash','src/primitives.mjs'),('assemblyCompilerHash','src/assembly.mjs'),('sourceHash',f'src/decks/{deck}.mjs')]:
    if report.get(key)!=sha(ROOT/path):fail.append(f'{mode}/{deck} stale {key}')
   if report.get('sourceBundleHash')!=hashlib.sha256(b''.join(p.read_bytes()for p in sorted((ROOT/'src').rglob('*'))if p.is_file())).hexdigest():fail.append(f'{mode}/{deck} source bundle changed after render')
   if mode=='assembly'and report.get('collectionHash')!=collection_hash():fail.append(f'{mode}/{deck} collection changed after render')
   if report['errors']:fail.append(f'{mode}/{deck} browser errors')
   expected=[r['file'][:-4]for r in inv if r['deck']==deck]
   if sorted(r['slide']for r in report['slides'])!=sorted(expected):fail.append(f'{mode}/{deck} slide coverage')
   for r in report['slides']:
    png=ROOT/'renders/final'/mode/deck/(r['slide']+'.png');html=ROOT/'build'/mode/deck/(r['slide']+'.html');size=Image.open(png).size
    if size!=(1280,720)or r['size']!=[1280,720]:fail.append('bad canvas '+str(png))
    if sha(png)!=r['sha256']or sha(html)!=r['htmlSha256']:fail.append('stale render '+str(png))
    if r['sourceImageTags']:fail.append('source bitmap inside canvas '+str(png))
    if r['findings']:fail.append(f'{mode}/{deck}/{r["slide"]} findings: {r["findings"]}')
    rows.append({'mode':mode,'deck':deck,'slide':r['slide'],'size':size,'sha256':sha(png)})
    if mode=='assembly':
     a=Image.open(png).convert('RGB');b=Image.open(ROOT/'renders/final/replica'/deck/png.name).convert('RGB');diff=ImageChops.difference(a,b);bbox=diff.getbbox();differences.append({'deck':deck,'slide':r['slide'],'pixelIdentical':bbox is None,'differenceBox':bbox})
   pdf=ROOT/'pdfs'/mode/(deck+'.pdf')
   if not pdf.exists():fail.append('missing deckPDF '+str(pdf));continue
   with fitz.open(pdf)as doc:
    if len(doc)!=len(expected):fail.append('deckPDF pagecount '+str(pdf))
    if any(tuple(pg.rect)!=(0,0,1280,720)for pg in doc):fail.append('deckPDF canvas '+str(pdf))
 for mode in ['replica','assembly']:
  with fitz.open(ROOT/'pdfs'/(mode+'-all.pdf'))as doc:
   if len(doc)!=109 or any(tuple(pg.rect)!=(0,0,1280,720)for pg in doc):fail.append('combined PDF '+mode)
 result={'success':not fail,'references':len(inv),'renderCount':len(rows),'canvas':[1280,720],'collection':library,'pages':rows,'assemblyComparison':differences,'failures':fail};(ROOT/'review/final-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps({k:v for k,v in result.items()if k not in ['pages','assemblyComparison']},ensure_ascii=False,indent=2));sys.exit(bool(fail))
if __name__=='__main__':main()
