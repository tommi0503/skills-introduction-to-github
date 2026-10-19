from pathlib import Path
import zipfile,json,hashlib,fitz
from PIL import Image
from io import BytesIO
art=Path('artifacts');out=[]
for p in sorted(art.glob('*.zip')):
 with zipfile.ZipFile(p) as z:
  assert z.testzip() is None
  names=z.namelist()
  info={'file':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'entries':len(names),'crc':'passed'}
  if 'collection' in p.name:
   assert {x.split('/')[0] for x in names}=={'rhetis-spectrum'}
   assert sum(x.endswith('/element.json') for x in names)==31
   info['topLevel']='rhetis-spectrum/'
  if 'deliverables' in p.name:
   for mode in ['clone','assembly']:
    images=[x for x in names if x.startswith('renders/'+mode+'/') and x.endswith('.png')];assert len(images)==76
    for n in images:assert Image.open(BytesIO(z.read(n))).size==(1280,720)
   library=[x for x in names if x.startswith('library/') and x.endswith('.png')];assert len(library)==178
   sheets=[x for x in names if x.startswith('sheets/') and x.endswith('.png')]
   for n in library+sheets:assert Image.open(BytesIO(z.read(n))).size==(1280,720)
   for mode in ['clone','assembly']:
    with fitz.open(stream=z.read(f'pdf/all-slides-{mode}.pdf'),filetype='pdf') as doc:
     assert len(doc)==76
     assert all(abs(page.rect.width/page.rect.height-16/9)<.001 for page in doc)
     assert all(len(page.get_text().strip())>5 for page in doc)
   for n in [x for x in names if x.endswith('.zip')]:
    with zipfile.ZipFile(BytesIO(z.read(n))) as nested:assert nested.testzip() is None
   info.update({'clonePngs':76,'assemblyPngs':76,'libraryPngs':178,'contactSheetPngs':len(sheets),'pngSize':[1280,720],'comparisonJpgs':len([n for n in names if n.startswith('comparisons/')]),'allSlidesPdfs':{'clonePages':76,'assemblyPages':76},'nestedZips':'passed'})
  out.append(info)
report={'status':'passed','archives':out};Path('review/archive-verification.json').write_text(json.dumps(report,indent=2));(art/'SHA256SUMS.txt').write_text(''.join(r['sha256']+'  '+r['file']+'\n' for r in out));print(json.dumps(report,indent=2))
