"""Make original/copy comparison PDFs from the final reviewed PNGs."""
from pathlib import Path
from PIL import Image,ImageChops
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from fontTools.ttLib import TTFont as FontToolsFont
from pypdf import PdfReader
import hashlib,json,tempfile
SOURCE=Path(__file__).resolve().parents[1];REPO=SOURCE.parent;REVIEW=SOURCE/'briefing-tab-review'
font_source=REVIEW/'fonts/artifacts/joseon-gulim/ChosunGu.woff'
font_path=Path(tempfile.gettempdir())/'briefing-tab-comparison-header.ttf'
f=FontToolsFont(font_source);f.flavor=None;f.save(font_path)
pdfmetrics.registerFont(TTFont('ReviewHeader',str(font_path)))
scale=.75;page_width=2560*scale;image_height=720*scale;header_height=52*scale
report={'source_slides':11,'layout':'Left: original / Right: copy; one slide comparison per page, unchanged 2560x720 PNG below a 52px header.','outputs':[]}
for kind,label in [('replica','원본 재현본 (replica)'),('reassembled','라이브러리 재조립본')]:
 target=REPO/f'briefing-tab-compare-{kind}.pdf'
 c=Canvas(str(target),pagesize=(page_width,image_height+header_height),pageCompression=1)
 c.setTitle(f'Briefing Tab / Original vs {kind} / slides 20-30');c.setAuthor('Rhetis library review');c.showOutline()
 pages=[]
 for index,n in enumerate(range(20,31)):
  png=REVIEW/f'compare-{kind}/slide_{n}.png'
  with Image.open(png) as im:
   assert im.size==(2560,720)
   with Image.open(REVIEW/f'originals/slide_{n}.png') as original:
    assert ImageChops.difference(im.crop((0,0,1280,720)).convert('RGB'),original.convert('RGB')).getbbox() is None
   with Image.open(REVIEW/f'{kind}/slide_{n}.png') as copy:
    assert ImageChops.difference(im.crop((1280,0,2560,720)).convert('RGB'),copy.convert('RGB')).getbbox() is None
   c.drawImage(ImageReader(im),0,0,width=page_width,height=image_height)
  c.setFillColorRGB(.97,.98,.99);c.rect(0,image_height,page_width,header_height,fill=1,stroke=0)
  c.setFillColorRGB(.15,.18,.23);c.setFont('ReviewHeader',15)
  c.drawString(18,image_height+13,'원본')
  c.drawString(page_width/2+18,image_height+13,label)
  c.setFont('ReviewHeader',12);c.drawRightString(page_width-18,image_height+13,f'슬라이드 {n} · {index+1:02d}/11')
  c.bookmarkPage(f'slide-{n}');c.addOutlineEntry(f'Slide {n} / {index+1:02d} of 11',f'slide-{n}',level=0)
  c.showPage();pages.append({'page':index+1,'slide':n,'source':str(png.relative_to(SOURCE)),'png_size':[2560,720]})
 c.save();reader=PdfReader(target)
 assert len(reader.pages)==11 and len(reader.outline)==11
 for page,item in zip(reader.pages,pages):
  assert abs(float(page.mediabox.width)-1920)<.01 and abs(float(page.mediabox.height)-579)<.01
  assert len(page.images)==1
  with Image.open(SOURCE/item['source']) as original:
   assert ImageChops.difference(page.images[0].image.convert('RGB'),original.convert('RGB')).getbbox() is None
 report['outputs'].append({'name':target.name,'pages':pages,'bookmarks':11,'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'original_and_copy_halves_match':True,'all_embedded_pixels_match':True})
 print(target.name,target.stat().st_size,'bytes; 11 pages verified',flush=True)
(Path(__file__).parent/'comparison-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
