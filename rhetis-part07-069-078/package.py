"""Verify files, build collection/review archives, and stage sources in isolated Git worktree."""
from pathlib import Path
import hashlib,json,zipfile,shutil,sys,collections
from PIL import Image,ImageOps,ImageDraw
import fitz
ROOT=Path(__file__).resolve().parent
DEST=Path('/workspace/work/rhetis-part07-publish/rhetis-part07-069-078')
META={'vectorbox':('069',12,'선택 상자와 모서리 핸들'),'seedmark':('072',21,'구절 하이라이트와 끝점'),'crossrail':('073',30,'네이비 레일과 교차선'),'meridian-deck':('074',30,'가는 프레임과 원형 배지'),'onboard-docket':('078',19,'바인더 띠와 번호 칩')}

def archive(dst,items):
 with zipfile.ZipFile(dst,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for src,arc in items:
   z.write(src,str(arc))
 with zipfile.ZipFile(dst) as z:
  assert z.testzip() is None
 return {'file':dst.name,'bytes':dst.stat().st_size,'sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'members':len(items)}

def package(kid):
 deck,count,language=META[kid];P=ROOT/(kid+'-project');K=P/kid
 resources=json.loads((P/'portable-resources.json').read_text());assert not resources['errors'],(kid,resources['errors'])
 audit=json.loads((P/'contract-audit.json').read_text());assert not audit['errors'],(kid,audit['errors'])
 elements=sorted(p.name for p in (K/'elements').iterdir() if p.is_dir());assert len(elements)==56
 images=[];pdfs={}
 library_allowed={'light.html','dark.html','library-light.pdf','library-dark.pdf'}|{name+'-'+mode+'.png' for name in ['foundation']+elements for mode in ['light','dark']}
 def include_file(f):
  rel=f.relative_to(P)
  return not(rel.parts[0]=='library' and (len(rel.parts)!=2 or rel.name not in library_allowed))
 for stage in ['replica','reassembled']:
  files=sorted((P/stage).glob('slide*.png'));assert len(files)==count,(kid,stage,len(files),count)
  assert len(list((P/stage).glob('slide*.html')))==count
  for f in files:assert Image.open(f).size==(1280,720),(kid,f)
  p=P/stage/(stage+'.pdf');doc=fitz.open(p);assert len(doc)==count;(pdfs.__setitem__(str(p.relative_to(P)),len(doc)));doc.close()
  for f in (P/('compare-'+stage)).glob('slide*.png'):assert Image.open(f).size==(2560,720)
  assert len(list((P/('compare-'+stage)).glob('slide*.png')))==count
 for mode in ['light','dark']:
  for el in ['foundation']+elements:assert (P/'library'/(el+'-'+mode+'.png')).exists(),(kid,el,mode)
  p=P/'library'/('library-'+mode+'.pdf');doc=fitz.open(p);expected_pages=audit['fixtureCount']+len(list((K/'foundation/fixtures').glob('*.html')));assert len(doc)==expected_pages,(kid,mode,'PDF fixture pages',len(doc),expected_pages);pdfs[str(p.relative_to(P))]=len(doc);doc.close()
 for f in P.rglob('*.png'):
  if include_file(f) and any(part in ['replica','reassembled','compare-replica','compare-reassembled','library','fidelity'] for part in f.relative_to(P).parts):
   with Image.open(f) as im:im.verify()
   with Image.open(f) as im:images.append({'file':str(f.relative_to(P)),'size':list(im.size)})
 review=json.loads((P/'fidelity/primary-review.json').read_text())['pages']
 assert len(review)==count,(kid,'primary review incomplete',len(review),count)
 for stem,row in review.items():
  assert row['status']=='accepted',(kid,stem,'manual review rejected')
  assert row['comparisonSha256']==hashlib.sha256((P/'fidelity'/(stem+'-triple.png')).read_bytes()).hexdigest(),(kid,stem,'manual review stale')
 # Fidelity evidence must be generated after the final render, from the same source.
 fidelity=json.loads((P/'fidelity/manifest.json').read_text())
 from render import source_fingerprint
 for stage in ['replica','reassembled']:
  assert fidelity[stage]==source_fingerprint(P,kid,stage),(kid,'stale fidelity evidence',stage)
 # Render fingerprint proves final outputs correspond to the final source HTML and every loaded CSS/runtime asset.
 from render import source_fingerprint
 fingerprints=json.loads((P/'render-fingerprints.json').read_text())
 for stage in ['replica','library','reassembled']:
  assert source_fingerprint(P,kid,stage)==fingerprints[stage]['sha256'],(kid,stage,'stale source fingerprint')
 for stage in ['replica','reassembled']:
  checks=json.loads((P/(stage+'-render-checks.json')).read_text())
  assert len(checks)==count
  for c in checks:
   assert hashlib.sha256((P/stage/c['file']).read_bytes()).hexdigest()==c['sourceSha256'],(kid,stage,'stale render',c['file'])
   assert not c['failedResources'] and not c['badResources'],(kid,stage,'failed resource',c['file'])
   assert c['doc']==[1280,720],(kid,stage,'document overflow',c['file'],c['doc'])
 manifest={'collection':kid,'deck':deck,'pageCount':count,'elementCount':56,'fixtureCount':audit['fixtureCount'],'pngCount':len(images),'pngDimensions':images,'pdfPages':pdfs,'upstreamIntake':'Not available in reference pack; independent contract audit and actual Chromium render used.'}
 (P/'build-verification.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
 DEST.mkdir(parents=True,exist_ok=True);downloads=DEST/'downloads';downloads.mkdir(exist_ok=True)
 collection_items=[]
 for f in sorted(K.rglob('*')):
  if f.is_file():
   assert f.suffix in ['.css','.json','.md','.html'],f
   collection_items.append((f,Path(kid)/f.relative_to(K)))
 col=archive(downloads/(kid+'.zip'),collection_items)
 with zipfile.ZipFile(downloads/(kid+'.zip')) as z:assert {x.split('/')[0] for x in z.namelist()}=={kid}
 include=['quality','fidelity','replica','compare-replica','library','reassembled','compare-reassembled','assets',kid]
 review_items=[]
 for n in include:
  for f in sorted((P/n).rglob('*')):
   if f.is_file() and '__pycache__' not in f.parts and include_file(f):review_items.append((f,f.relative_to(P)))
 for n in ['design-language.md','review-notes.md','build-verification.json','contract-audit.json','fixture-provenance.json','replica-render-checks.json','reassembled-render-checks.json','library-render-checks.json','library-quick-checks.json','render-fingerprints.json','preview-build.json','portable-resources.json','finalize-status.json','assembly-map.md','assembly-map.json','image-inventory.md']:
  if (P/n).exists():review_items.append((P/n,Path(n)))
 rev=archive(downloads/(kid+'-review.zip'),review_items)
 # Expanded review sources in the repository; avoid intermediate pass directories and caches.
 target=DEST/(kid+'-project');target.mkdir(exist_ok=True)
 for src,rel in review_items:
  dst=target/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 for f in P.glob('*.py'):
  dst=target/'tools'/f.name;dst.parent.mkdir(exist_ok=True);shutil.copy2(f,dst)
 return {'collection':kid,'deck':deck,'pages':count,'language':language,'archives':[col,rev],'verification':manifest}

if __name__=='__main__':
 kids=sys.argv[1:] or list(META);out=[package(k) for k in kids]
 (DEST/'archive-manifest.json').write_text(json.dumps([{k:v for k,v in x.items() if k!='verification'} for x in out],ensure_ascii=False,indent=2))
 print(json.dumps([{k:v for k,v in x.items() if k!='verification'} for x in out],ensure_ascii=False,indent=2))
