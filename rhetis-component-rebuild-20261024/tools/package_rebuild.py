"""Stage six independent collection archives and their review evidence, preserving prior delivery."""
from pathlib import Path
import argparse,json,re,shutil,hashlib,zipfile
from PIL import Image
B=Path('/workspace/work/rebuild-20261024');P=Path('/workspace/work/publish/rhetis-component-rebuild-20261024');R=Path('/workspace/work/reference');NAMES=['nocturne','inflexion','diecut','afterglow','dockside','confluence'];COUNTS=dict(nocturne=6,inflexion=20,diecut=19,afterglow=9,dockside=30,confluence=4)
def copy(p,q):
 q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
def fonts(name,target):
 c=B/name/'collection'/name;text='\n'.join(p.read_text()for p in c.rglob('*')if p.is_file()and p.suffix in ['.css','.json']);blocks=re.findall(r'@font-face\s*\{[^}]+\}',(R/'fonts/fonts.css').read_text());kept=[];families=[]
 for block in blocks:
  family=re.search(r'font-family:\s*[\'\"]([^\'\"]+)',block)[1]
  if family not in text:continue
  kept.append(block);families.append(family)
  for path in re.findall(r'url\([\'\"]([^\'\"]+)',block):copy(R/'fonts'/path,target/path)
 (target/'fonts.css').write_text('\n'.join(kept)+'\n');return sorted(set(families))
def zipdir(source,out,top):
 with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
  for p in sorted(source.rglob('*')):
   if p.is_file():z.write(p,str(Path(top)/p.relative_to(source)))
 with zipfile.ZipFile(out)as z:
  assert z.testzip()is None
  if out.name.endswith('-review.zip'):pass
  else:
   assert {x.split('/')[0]for x in z.namelist()}=={top}
   assert all(Path(x).suffix in ['.css','.json','.md','.html']for x in z.namelist())
 return {'file':out.name,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'zipIntegrity':'pass','gitStorage':'lfs'if out.stat().st_size>=90*1024*1024 else'git'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def gate(n,c,r):
 from size_review import source_hash
 current=source_hash(c);d=json.loads((r/'size-summary-all.json').read_text())
 assert d['sourceSHA256']==current and d['sourceUnchanged'],(n,'stale size summary')
 for k in ['outsideCases','clipCases','fontFailureCases','hiddenCases','zeroCases','pixelFailureCases']:assert d[k]==0,(n,k,d[k])
 for f in ['copy-audit.json','copy-block-audit.json']:assert not json.loads((r/f).read_text())['collisions'],(n,f)
 cases=0
 for p in (r/'sheets').glob('*-audit.json'):
  a=json.loads(p.read_text())
  for v in a['cases']:
   fixture=c/'elements'/a['leaf']/'fixtures'/(v['fixture']+'.html')
   assert sha(fixture)==v['fixtureSHA256'],(n,p.name,'stale fixture')
   assert v.get('pixelContrast') is not None and not v['pixelContrast']['failures'],(n,p.name,'contrast')
   for key in ['outsideText','clipped','fontFailures','hiddenEssential','zeroRoots','scriptErrors']:assert not v.get(key),(n,p.name,key)
   cases+=1
 assert cases==d['cases'],(n,cases,d['cases'])
 audit=json.loads((r/'reassembled-audit.json').read_text())
 if audit['sourceSHA256']!=current:
  proof=json.loads((r/'reassembled-fixture-update-proof.json').read_text())
  assert proof['currentCollectionSourceSHA256']==current and proof['lastActualAssemblySourceSHA256']==audit['sourceSHA256']
  for key in ['CSSUnchanged','kitJSONUnchanged','sourcePaletteUnchanged','assemblyArtifactsUnchanged']:assert proof[key]
  for path,h in proof['afterCSSSHA256'].items():assert sha(c/path)==h
  for path,h in proof['assemblyArtifactsSHA256'].items():assert sha((r/path) if (r/path).exists() else (r/'reassembled'/path))==h
 for page in audit['pages']:
  fn=Path(page['file']).name
  assert sha(r/'reassembled'/fn)==page['htmlSHA256'],(n,fn,'stale html')
  assert not page.get('failedFonts') and not page.get('clipped') and not page.get('zeroElementRoots'),(n,fn,'page audit')
 return {'sourceSHA256':current,'cases':cases,'latestFixtureAndRenderedCSSVerified':True}
def stage():
 P.mkdir(exist_ok=True);manifest=[];zips=[]
 for n in NAMES:
  c=B/n/'collection'/n;r=B/n/'review';gate_result=gate(n,c,r);tc=P/'collections'/n;tr=P/'reviews'/n
  assert len(list((c/'elements').glob('*/element.css')))==56,n
  for dst in [tc,tr]:
   if dst.exists():shutil.rmtree(dst)
  shutil.copytree(c,tc);tr.mkdir(parents=True)
  for fn in ['map.json','GAPS.md','review-notes.md','design-language.md','source-palette.json']:
   p=r/fn
   if p.exists():copy(p,tr/fn)
  for p in r.glob('*.json'):copy(p,tr/p.name)
  for p in (r/'sheets').iterdir():
   if p.suffix in ['.png','.json']:copy(p,tr/'sheets'/p.name)
  for folder in ['reassembled','compare-reassembled','render-reuse','probes']:
   if not (r/folder).exists():continue
   for p in (r/folder).iterdir():
    if p.suffix in ['.html','.css','.png','.json']:copy(p,tr/folder/p.name)
  for p in (r/'assets').glob('*.js'):copy(p,tr/'assets'/p.name)
  copy(Path('/workspace/work/tools/LUCIDE-LICENSE.txt'),tr/'assets/LUCIDE-LICENSE.txt')
  family=fonts(n,tr/'assets/fonts');shutil.copy(B/'replica-freeze-validation.json',tr/'replica-freeze-validation.json')
  leaves=sorted(p.parent.name for p in (c/'elements').glob('*/element.css'));pages=sorted((tr/'reassembled').glob('*.png'));comps=sorted((tr/'compare-reassembled').glob('*.png'))
  assert len(pages)==COUNTS[n]and len(comps)==COUNTS[n],(n,len(pages),len(comps))
  sizes=[]
  for folder,expected in [('reassembled',(1280,720)),('compare-reassembled',(3840,720))]:
   for p in (tr/folder).glob('*.png'):
    with Image.open(p)as im:assert im.size==expected,(p,im.size);im.verify()
    sizes.append({'file':str(p.relative_to(tr)),'width':expected[0],'height':expected[1]})
  for leaf in leaves:
   for mode in ['light','dark']:
    p=tr/'sheets'/(leaf+'-'+mode+'.png');assert p.exists(),p
    with Image.open(p)as im:sizes.append({'file':str(p.relative_to(tr)),'width':im.width,'height':im.height});im.verify()
  d=json.loads((tr/'map.json').read_text());mapped=sorted({x['leaf']for x in d['instances']if x.get('leaf')and x['use']not in ['unexpressible','furniture','background']})
  for leaf in mapped:assert(tr/'sheets'/(leaf+'-replica.png')).exists(),(n,leaf)
  seen={x['file']for x in sizes}
  for p in tr.rglob('*.png'):
   if str(p.relative_to(tr))in seen:continue
   with Image.open(p)as im:sizes.append({'file':str(p.relative_to(tr)),'width':im.width,'height':im.height});im.verify()
  x={'collection':n,'renderGate':gate_result,'elements':56,'fixtures':len(list((c/'elements').glob('*/fixtures/*.html'))),'pages':len(pages),'sizeSheets':112,'sourceComparisonSheets':len(mapped),'fonts':family,'pngs':sizes,'gaps':sum(x['use']=='unexpressible'for x in d['instances'])};manifest.append(x)
  (tr/'image-validation.json').write_text(json.dumps(x,ensure_ascii=False,indent=2));zips.extend([zipdir(tc,P/(n+'.zip'),n),zipdir(tr,P/(n+'-review.zip'),n+'-review')])
 (P/'.gitattributes').write_text(''.join(z['file']+' filter=lfs diff=lfs merge=lfs -text\n'for z in zips if z['gitStorage']=='lfs'))
 for fn in ['element-origins.md','map-summary.json','replica-freeze.json','replica-freeze-validation.json','gap-index.md']:
  copy(B/fn,P/fn)
 shutil.copytree(B/'tools',P/'tools',dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__'))
 report={'collections':manifest,'zips':zips,'allZipIntegrity':'pass','totalElements':sum(x['elements']for x in manifest),'totalPages':sum(x['pages']for x in manifest),'note':'All page PNGs are1280x720; triples3840x720; requested size sheets retain their native composite sizes.'};(P/'delivery-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 print(json.dumps({'folder':str(P),'zips':len(zips),'MB':round(sum(x['bytes']for x in zips)/1024**2,1),'pages':report['totalPages'],'elements':report['totalElements']}))
if __name__=='__main__':stage()
