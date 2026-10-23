from pathlib import Path
import json,hashlib,zipfile,shutil,fitz
from PIL import Image
OUT=Path('/workspace/output');O=OUT/'fluxweave';V=OUT/'fluxweave-review';A=V/'audits';A.mkdir(exist_ok=True)
for kind in ['replica','reassembled']:
 doc=fitz.open()
 for p in sorted((V/kind).glob('slide_*.png')):
  page=doc.new_page(width=960,height=540);page.insert_image(page.rect,filename=str(p))
 temp=V/kind/(kind+'-packed.pdf');doc.save(temp,garbage=4,deflate=True,deflate_images=True);doc.close();temp.replace(V/kind/(kind+'.pdf'))
manifest=[]
for p in sorted(V.rglob('*.png')):
 with Image.open(p) as im:manifest.append({'file':str(p.relative_to(V)),'width':im.width,'height':im.height,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(V/'png-manifest.json').write_text(json.dumps(manifest,indent=2))
counts={k:len(list((V/k).glob('slide_*.png'))) for k in ['replica','reassembled','compare-replica','compare-reassembled']}
assert all(n==18 for n in counts.values());assert len(list((V/'library').glob('*/light.png')))==57;assert len(list((V/'library').glob('*/dark.png')))==57
assert all((m['width'],m['height'])==(1280,720) for m in manifest if m['file'].startswith(('replica/','reassembled/')))
assert all((m['width'],m['height'])==(2560,720) for m in manifest if m['file'].startswith(('compare-replica/','compare-reassembled/')))
assert len(manifest)==186
allowed={'.css','.json','.md','.html'};assert all(p.suffix in allowed for p in O.rglob('*') if p.is_file());assert len(list(O.glob('elements/*/element.json')))==56
pdfs={}
for p in sorted(V.rglob('*.pdf')):
 with fitz.open(p) as doc:pdfs[str(p.relative_to(V))]={'pages':len(doc),'bytes':p.stat().st_size};assert len(doc)==(173 if 'library-' in p.name else 18)
for p in Path('/workspace/work/integration').glob('fluxweave-*-audit.json'):shutil.copy(p,A/p.name)
checks={'collection':'fluxweave','elements':56,'fixtures':173,'original_images':18,'page_pngs':counts,'element_light_sheets':56,'element_dark_sheets':56,'foundation_sheets':2,'total_pngs':len(manifest),'pdfs':pdfs,'allowed_collection_extensions':sorted(allowed),'zip_verification':'testzip and one-folder check performed after creation; hashes in external fluxweave-packaging-checks.json'}
(V/'packaging-checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
archives={}
for folder in [O,V]:
 archive=OUT/(folder.name+'.zip')
 with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p in sorted(folder.rglob('*')):
   if p.is_file():z.write(p,p.relative_to(OUT))
 with zipfile.ZipFile(archive) as z:
  assert z.testzip() is None
  assert {n.split('/')[0] for n in z.namelist()}=={folder.name}
  files=len(z.namelist())
 assert archive.stat().st_size<99_000_000
 archives[archive.name]={'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'files':files,'testzip':'passed','top_level':folder.name}
checks['archives']=archives
(OUT/'fluxweave-packaging-checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2));print(json.dumps(checks,ensure_ascii=False,indent=2))
