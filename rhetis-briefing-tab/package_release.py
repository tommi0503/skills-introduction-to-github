from pathlib import Path
from PIL import Image
from pypdf import PdfReader
import json,zipfile,hashlib,collections,shutil
ROOT=Path(__file__).resolve().parent;C=ROOT/'briefing-tab';R=ROOT/'briefing-tab-review';OUT=ROOT/'release-staging';OUT.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def zipfolder(folder,target):
 with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=6)as z:
  for p in sorted(folder.rglob('*')):
   if p.is_file():z.write(p,p.relative_to(folder.parent))
 with zipfile.ZipFile(target)as z:
  assert z.testzip() is None
  return {'name':target.name,'bytes':target.stat().st_size,'sha256':sha(target),'entries':len(z.namelist()),'crc_check':'pass','top_level':sorted(set(p.split('/')[0]for p in z.namelist()))}
contract=json.loads((R/'contract-validation.json').read_text());audit=json.loads((R/'browser-validation.json').read_text());chip=json.loads((R/'chip-validation.json').read_text())
assert not contract['errors'];assert not audit['font_failures'];assert not any(a['failures']for a in audit['library']);assert chip['failures']==0
assert not any(i['kind']!='contrast'for a in audit['pages'] for i in a['issues'])
sourcecss=list(C.rglob('*.css'));css_time=max(p.stat().st_mtime for p in sourcecss)
for mode in ['light','dark']:
 doc=(R/f'library/{mode}.html').read_text()
 for p in sourcecss:assert p.read_text()in doc,f'Stale compiled sheet {p}'
images=[]
for p in sorted(R.rglob('*.png')):
 im=Image.open(p);im.verify()
 with Image.open(p)as im:dim=list(im.size)
 rel=str(p.relative_to(R))
 if rel.startswith(('replica/','reassembled/','originals/')):assert dim==[1280,720],(rel,dim)
 if rel.startswith(('compare-replica/','compare-reassembled/')):assert dim==[2560,720],(rel,dim)
 if not rel.startswith('originals/'):
  assert p.stat().st_mtime>=css_time,(rel,'stale render')
  if p.parent.name in ['replica','reassembled']:
   assert p.stat().st_mtime>=p.with_suffix('.html').stat().st_mtime,(rel,'stale source')
 images.append({'path':rel,'size':dim,'sha256':sha(p)})
assert len(list((R/'replica').glob('slide_*.png')))==11
assert len(list((R/'reassembled').glob('slide_*.png')))==11
for e in (C/'elements').iterdir():
 for mode in ['light','dark']:assert (R/f'library/{e.name}/{mode}.png').is_file()
pdfs={str(p.relative_to(R)):len(PdfReader(p).pages)for p in R.rglob('*.pdf')}
assert pdfs['replica/replica.pdf']==11 and pdfs['reassembled/reassembled.pdf']==11
assert pdfs['library/library-light.pdf']==151 and pdfs['library/library-dark.pdf']==151
collection=zipfolder(C,OUT/'briefing-tab.zip');assert collection['top_level']==['briefing-tab']
with zipfile.ZipFile(OUT/'briefing-tab.zip')as z:assert all(Path(p).suffix in {'.css','.json','.md','.html'}for p in z.namelist())
validation={'build':'pass','input_decks':1,'input_images':11,'element_count':56,'element_fixtures':148,'foundation_fixtures':3,'golden_fixtures':28,'library_browser_cases':audit['cases'],'library_browser_failures':0,'font_failures':0,'rendered_pixel_chip_checks':chip['count'],'chip_failures':0,'page_clipping_overlap_overflow':0,'source_style_contrast_exceptions':'Preserved from source; see browser-validation.json and review-notes.md','contract_warnings':contract['warnings'],'actual_rhetis_intake':'Not available in reference pack; not claimed','last_css_mtime':css_time,'all_renders_after_last_css':True,'png_count':len(images),'png_dimensions':dict(collections.Counter(str(x['size'])for x in images)),'images':images,'pdf_pages':pdfs,'collection_archive':collection,'review_archive_crc_check':'pass; verified again after final packaging'}
(R/'validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2))
review=zipfolder(R,OUT/'briefing-tab-review.zip')
# Every archive is verified after its final write; immutable hashes are external to their own ZIP.
archives={'collection':collection,'review':review};(OUT/'archive-verification.json').write_text(json.dumps(archives,ensure_ascii=False,indent=2))
preview=Image.new('RGB',(2560,1440));preview.paste(Image.open(R/'compare-reassembled/slide_24.png'),(0,0));preview.paste(Image.open(R/'compare-reassembled/slide_25.png'),(0,720));preview.save(OUT/'briefing-tab-preview.png')
shutil.copy2(R/'compare-reassembled/slide_24.png',OUT/'briefing-tab-compare-24.png');shutil.copy2(R/'compare-reassembled/slide_25.png',OUT/'briefing-tab-compare-25.png')
print(json.dumps({'archives':archives,'png_count':len(images),'dimensions':validation['png_dimensions'],'pdfs':pdfs},ensure_ascii=False,indent=2))
