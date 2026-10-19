from pathlib import Path
from PIL import Image
import json,re,hashlib,fitz
root=Path(__file__).resolve().parent.parent
fail=[];result={}
def check(ok,msg):
 if not ok:fail.append(msg)
col=root/'collections/studio-spectrum';taxonomy=json.loads((root/'contract/taxonomy.json').read_text());tok=json.loads((root/'contract/kit-tokens.json').read_text())['tokens'];steps=json.loads((root/'contract/type-steps.json').read_text());kit=json.loads((col/'kit/kit.json').read_text());css=(col/'kit/css/tokens.css').read_text()
check(kit['id']=='studio-spectrum','kit id');check(kit['schema']=='rhetis.kit/2','kit schema')
light,dark=css.split('.slide.dark',1)
for name,kind in tok.items():
 check(re.search(re.escape(name)+r'\s*:',light),f'missing light {name}')
 if kind=='color':check(re.search(re.escape(name)+r'\s*:',dark),f'missing dark {name}')
folders=sorted(p for p in (col/'elements').iterdir() if p.is_dir());check(len(folders)==31,'31 elements required');fx=0;actual_contracts=[]
for p in folders:
 meta=json.loads((p/'element.json').read_text());actual_contracts.append(meta['contract']);check(meta['schema']=='rhetis.design-library-element-source/1',str(p)+' schema')
 files=sorted((p/'fixtures').glob('*.html'));check(len(files)>=2,p.name+' fixtures < 2');fx+=len(files)
 c=(p/'element.css').read_text();check('data-el="studio-spectrum-'+p.name+'"' in c,p.name+' scope')
 check(not re.search(r'@(import|font-face|keyframes|property)\b|url\(',c),p.name+' forbidden CSS resource')
 check(not re.search(r'font-size\s*:\s*[\d.]+(?:px|rem|em)',c),p.name+' literal font size')
 check(not re.search(r'#[\da-fA-F]{3,8}\b|rgba?\(',c),p.name+' literal color')
 for f in files:
  t=f.read_text();check(t.startswith('<!-- min:'),str(f)+' min declaration');check('data-el="studio-spectrum-'+p.name+'"' in t,str(f)+' fixture scope')
check(set(actual_contracts)=={x['id'] for x in taxonomy['contracts']},'contract ID coverage');result['elements']=len(folders);result['elementFixtures']=fx;result['foundationFixtures']=len(list((col/'foundation/fixtures').glob('*.html')))
result['renders']={}
for mode in ['replica','assembled']:
 files=sorted((root/'renders/final'/mode).glob('*.png'));check(len(files)==107,mode+' count');wrong=[]
 for f in files:
  if Image.open(f).size!=(1280,720):wrong.append(str(f))
 check(not wrong,mode+' dimensions');result['renders'][mode]={'count':len(files),'dimensions':[1280,720],'wrongSizes':wrong}
 records=[]
 for f in (root/'review/final').glob('*-'+mode+'.json'):
  d=json.loads(f.read_text());records.extend(d['records']);check(not d['errors'],str(f)+' browser errors');check(not d['fonts'],str(f)+' font request failures')
 findings=[dict(deck=r['deck'],slide=r['slide'],**x) for r in records for x in r['findings']];check(not findings,mode+' findings');result['renders'][mode]['findings']=findings
result['referenceImages']=len(list((root/'public/reference').glob('*/*.jpg')));check(result['referenceImages']==107,'references107')
result['comparisons']=len(list((root/'comparisons/final').glob('*/*.jpg')));check(result['comparisons']==107,'comparisons107')
lib=list((root/'exports/library').glob('*/*.png'));check(len(lib)==194,'library PNG194');check(all(Image.open(p).size==(1280,720) for p in lib),'library PNG dimensions');result['libraryPNG']=len(lib)
result['pdf']={}
for mode in ['replica','assembled']:
 p=root/f'exports/{mode}-107-slides.pdf'
 check(p.exists(),str(p)+' missing')
 if p.exists():
  d=fitz.open(p);check(len(d)==107,mode+' PDF page count');check(all(abs(p.rect.width-960)<.1 and abs(p.rect.height-540)<.1 for p in d),mode+' PDF page dimensions');result['pdf'][mode]={'pages':len(d),'mediaBoxPoints':[960,540],'cssPixels':[1280,720]}
for name in ['light','dark']:
 p=root/f'exports/library-{name}-97-fixtures.pdf'
 check(p.exists(),str(p)+' missing')
 if p.exists():
  d=fitz.open(p);check(len(d)==97,name+' library PDF97')
result['failures']=fail;result['passed']=not fail
(root/'review/verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(bool(fail))
