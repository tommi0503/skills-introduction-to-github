"""Bundle verified per-element sheet PNGs without cropping or rescaling pixels."""
from pathlib import Path
from PIL import Image
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader
import hashlib,json
SOURCE=Path(__file__).resolve().parents[1]
REPO=SOURCE.parent
LIBRARY=SOURCE/'briefing-tab-review/library'
folders=['foundation']+sorted(p.name for p in (SOURCE/'briefing-tab/elements').iterdir() if p.is_dir())
assert len(folders)==57
report={'sheets_per_pdf':57,'elements':56,'foundation':1,'layout':'One complete element sheet per PDF page; original PNG pixels losslessly embedded; variable page height; bookmarks in element order.','outputs':[]}
for mode in ['light','dark']:
 target=REPO/f'briefing-tab-elements-{mode}.pdf'
 c=Canvas(str(target),pageCompression=1)
 c.setTitle(f'Briefing Tab / all element sheets / {mode}')
 c.setAuthor('Rhetis library review')
 pages=[]
 for i,name in enumerate(folders):
  png=LIBRARY/name/f'{mode}.png'
  with Image.open(png) as im:
   w,h=im.size
   assert w==1328
   c.setPageSize((w*.75,h*.75))
   c.bookmarkPage(name)
   c.addOutlineEntry(f'{i+1:02d} / {name}',name,level=0,closed=False)
   c.drawImage(ImageReader(im),0,0,width=w*.75,height=h*.75)
   c.showPage()
  pages.append({'page':i+1,'element':name,'source':str(png.relative_to(SOURCE)),'png_size':[w,h]})
 c.save()
 r=PdfReader(target)
 assert len(r.pages)==57 and len(r.outline)==57
 for page,data in zip(r.pages,pages):
  assert abs(float(page.mediabox.width)-data['png_size'][0]*.75)<.01
  assert abs(float(page.mediabox.height)-data['png_size'][1]*.75)<.01
 report['outputs'].append({'name':target.name,'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'pages':pages,'bookmarks':len(r.outline)})
 print(target.name,target.stat().st_size,'bytes; 57 pages and bookmarks verified',flush=True)
(Path(__file__).parent/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
