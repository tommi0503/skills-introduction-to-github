from pathlib import Path
from PIL import Image
from html.parser import HTMLParser
import json,re,hashlib,zipfile
import fitz
P=Path(__file__).resolve().parent.parent
errors=[];report={}
def check(ok,msg):
 if not ok:errors.append(msg)
expected={'053':9,'054':20,'056':20,'057':11,'058':20,'060':30,'061':2}
refs=json.loads((P/'review/reference-manifest.json').read_text());check(len(refs)==112,'Reference manifest must have112images')
report['references']={'count':len(refs),'decks':expected,'originalSizes':sorted(set(tuple(r['size']) for r in refs))}
for mode in ['replica','assembled']:
 files=list((P/'renders'/mode).glob('*/*.png'));check(len(files)==112,f'{mode} PNG count')
 for d,c in expected.items():check(len(list((P/'renders'/mode/d).glob('*.png')))==c,f'{mode}/{d} count')
comparisons=list((P/'comparisons').glob('*/*.jpg'));check(len(comparisons)==112,'Comparison JPG count')
check(all(Image.open(p).size==(2560,752) for p in comparisons),'Comparison image dimensions');report['comparisons']={'count':len(comparisons),'size':[2560,752]}
report['renderCounts']={mode:len(list((P/'renders'/mode).glob('**/*.png'))) for mode in ['replica','assembled','library-light','library-dark']}
allpng=[p for d in ['renders','sheets','review'] for p in (P/d).rglob('*.png')]
wrong=[]
for p in allpng:
 with Image.open(p) as im:
  if im.size!=(1280,720):wrong.append({'path':str(p.relative_to(P)),'size':im.size})
check(not wrong,'Some output PNGs are not1280×720');report['pngDimensions']={'checked':len(allpng),'expected':[1280,720],'wrong':wrong}
C=P/'collection/report-forge';folders=sorted(p for p in (C/'elements').iterdir() if p.is_dir());check(len(folders)==31,'Collection must contain31elements')
tax=json.loads((P/'contract/taxonomy.json').read_text());contracts={c['id'] for c in tax['contracts']};steps=json.loads((P/'contract/type-steps.json').read_text())
sourceissues=[];fixturecount=0
for folder in folders:
 m=json.loads((folder/'element.json').read_text());check(m['schema']=='rhetis.design-library-element-source/1',f'{folder.name} schema');check(m['contract'] in contracts,f'{folder.name} contract')
 css=(folder/'element.css').read_text();fixtures=list((folder/'fixtures').glob('*.html'));fixturecount+=len(fixtures);check(len(fixtures)>=2,f'{folder.name} needs2fixtures');check(len(set(p.read_text() for p in fixtures))>=2,f'{folder.name} duplicatefixtures')
 for p in fixtures:
  text=p.read_text();check(bool(re.match(r'<!-- min: \d+x\d+',text)),f'{p} minimum comment');check(f'data-el="report-forge-{folder.name}"' in text,f'{p} data-el');check('grid-column:1 / span 12' in text and 'grid-row:1 / span 6' in text,f'{p} placement')
 check(not re.search(r'@(import|font-face|keyframes|property)\b|url\(',css),f'{folder.name} forbiddenCSS')
 check(not re.search(r'font-size\s*:\s*[^v\s]',css),f'{folder.name} font-size literals')
 for n in re.findall(r'var\(--type-(\d+)\)',css):check(int(n) in steps,f'{folder.name} invalidtype{n}')
 check(not re.search(r'#[\da-fA-F]{3,8}\b|\brgba?\(|\bhsla?\(',css),f'{folder.name} literalcolor')
 check(not re.search(r'font-weight\s*:\s*\d',css),f'{folder.name} literalweight')
check(json.loads((C/'kit/kit.json').read_text())['id']=='report-forge','kitid');tokens=json.loads((P/'contract/kit-tokens.json').read_text())['tokens'];css=(C/'kit/css/tokens.css').read_text();light,dark=css.split('.slide.dark')
for k,t in tokens.items():
 check(k+':' in light,f'missingtoken{k}')
 if t=='color':check(k+':' in dark,f'missingdarktoken{k}')
report['collection']={'id':'report-forge','elements':len(folders),'elementFixtures':fixturecount,'foundationFixtures':len(list((C/'foundation/fixtures').glob('*.html'))),'sharedTokens':len(tokens)}
for filename,count in [('audit-final-replica.json',112),('audit-assembly.json',112),('library-audit.json',260)]:
 a=json.loads((P/'review'/filename).read_text());check(len(a)==count,f'{filename} count');check(all(not x['issues'] for x in a),f'{filename} overflow');check(all(x.get('fonts',x.get('font',False)) for x in a),f'{filename} fonts')
 if filename=='library-audit.json':check(all(not x['contrastIssues'] for x in a),'librarycontrast')
 report[filename]={'cases':len(a),'overflow':sum(len(x['issues']) for x in a),'fontFailures':sum(not x.get('fonts',x.get('font',False)) for x in a),'contrastFailures':sum(len(x.get('contrastIssues',[])) for x in a)}
preview=json.loads((P/'review/preview-audit.json').read_text());check([p['slides'] for p in preview]==[112,112,89,89],'Preview slide counts');check(all(p['font'] and not p['failures'] and not p['external'] for p in preview),'Offline preview fonts/resources');check(preview[0]['filtered']==20 and preview[0]['dialog'] and preview[0]['modalSize']==[1280,720],'Preview controls');report['standalonePreviews']={'count':len(preview),'offline':True,'fontFailures':sum(not p['font'] for p in preview)}
provenance=json.loads((P/'review/final-render-inputs.json').read_text())
for name,r in provenance['sets'].items():
 for path,digest in {**r['inputs'],**r['html']}.items():check(hashlib.sha256((P/path).read_bytes()).hexdigest()==digest,f'Stale {name} input/output {path}')
 check(r['latestCSSIncluded'] and r['inputsWrittenBeforeHTMLAndPNG'],f'{name} provenance')
for row in preview:check(hashlib.sha256((P/'outputs'/f"{row['name']}.html").read_bytes()).hexdigest()==row['htmlSHA256'],f"Stale preview audit {row['name']}")
report['finalInputProvenance']={name:{'renderCount':r['renderCount'],'inputCount':len(r['inputs']),'htmlCount':len(r['html'])} for name,r in provenance['sets'].items()}
assembly=json.loads((P/'review/assembly-manifest.json').read_text());check(assembly['count']==112,'assemblycount');check(all(not c['omittedSourceRefs'] for c in assembly['compositions']),'assemblysourceomissions')
assembly_html=(P/'outputs/assembled.html').read_text()
check(not [(a,b) for a,b in re.findall(r'--type-(\d+)\s*:\s*(\d+)px',assembly_html) if a!=b],'Assembly redefines type-step values')
class TableShape(HTMLParser):
 def __init__(self):super().__init__();self.slide='';self.table=None;self.row=None;self.bad=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='section' and 'slide' in d.get('class','').split():self.slide=d.get('id')
  if t=='table':self.table=[]
  if t=='tr' and self.table is not None:self.row=0
  if t in ['th','td'] and self.row is not None:self.row+=int(d.get('colspan',1))
 def handle_endtag(self,t):
  if t=='tr' and self.row is not None:self.table.append(self.row);self.row=None
  if t=='table' and self.table is not None:
   if len(set(self.table))>1:self.bad.append({'slide':self.slide,'rowWidths':self.table})
   self.table=None
table_shapes=TableShape();table_shapes.feed(assembly_html);check(not table_shapes.bad,f'Assembly table header/body column mismatch: {table_shapes.bad}');report['assemblyTableShapes']={'mismatchCount':len(table_shapes.bad)}
report['assembly']={'independentOfReact':assembly['independentOfReact'],'count':assembly['count'],'sourceTextOmissions':sum(len(c['omittedSourceRefs']) for c in assembly['compositions']),'usedElementTypes':sorted(set(e for c in assembly['compositions'] for e in c['elements']))}
chips=json.loads((P/'review/chip-alignment.json').read_text());check(not chips['review'],'chipalignment');report['chips']={'count':chips['count'],'findings':len(chips['review'])}
checks={}
for name,count in [('replica-slides',112),('assembled-slides',112),('library-light',89),('library-dark',89),('replica-sheets',28),('assembled-sheets',28)]:
 path=P/'pdfs'/f'{name}.pdf';doc=fitz.open(path);sizes=sorted(set((round(p.rect.width,2),round(p.rect.height,2)) for p in doc));check(len(doc)==count,f'{name} PDFpages');check(sizes==[(960.0,540.0)],f'{name} PDFsize');checks[name]={'pages':len(doc),'pageSizePoints':sizes,'bytes':path.stat().st_size};doc.close()
report['pdfs']=checks
hashobj=hashlib.sha256()
for file in ['src/index.css','src/ui/index.tsx',*['src/decks/'+p.name for p in sorted((P/'src/decks').iterdir())]]:hashobj.update((P/file).read_bytes())
final=json.loads((P/'review/final-render-source.json').read_text());check(hashobj.hexdigest()==final['sourceSHA256'],'Final PNG source hash mismatch');report['sourceHash']=hashobj.hexdigest()
for p in (P/'src').rglob('*.tsx'):
 check(not re.search(r'<img\b|backgroundImage\s*:[^\n]+reference|<image\b',p.read_text()),f'Raster reference used in{p}')
production=json.loads((P/'review/production-audit.json').read_text());check(production['pass'],'Production build smoke audit');report['production']={'pass':production['pass'],'routes':len(production['rows']),'pdfs':len(production['pdfs'])}
report['errors']=errors;report['pass']=not errors
(P/'review/verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'pass':not errors,'errors':errors,'pngs':len(allpng),'elements':len(folders),'fixtures':fixturecount+2,'pdfs':len(checks)},ensure_ascii=False))
raise SystemExit(1 if errors else 0)
