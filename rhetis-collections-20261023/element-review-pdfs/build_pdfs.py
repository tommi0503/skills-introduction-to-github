"""Create one page per element, with original light/dark sheet PNGs side by side."""
from pathlib import Path
import argparse,hashlib,json
import fitz
from PIL import Image
NAMES=['fluxweave','cyanloop','roundrise','nightchamfer','glasspulse']
LABELS={n:n.title() for n in NAMES}
SCALE=.75;MARGIN=24;GUTTER=24;TOP=96
SOURCE_COMMIT='79e3ceb26493b9aedc7ce62bae14aa176af0a766'
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def sheets(root,name):
 lib=root/(name+'-review')/'library';elements=sorted(p.name for p in (root/name/'elements').iterdir() if p.is_dir());assert len(elements)==56
 result=[]
 for el in ['foundation']+elements:
  candidates=[lib/el,lib/'elements'/el];folder=next((f for f in candidates if (f/'light.png').is_file() and (f/'dark.png').is_file()),None)
  assert folder is not None,(name,el)
  fixtures=(root/name/('foundation' if el=='foundation' else 'elements/'+el)/'fixtures');result.append((el,folder,len(list(fixtures.glob('*.html')))))
 return result

def generate(root,out):
 out.mkdir(parents=True,exist_ok=True);records=[];combined=fitz.open();toc=[];source_records=[]
 for name in NAMES:
  doc=fitz.open();own_toc=[];start=len(combined)+1;toc.append([1,LABELS[name],start])
  for index,(element,folder,fixture_count) in enumerate(sheets(root,name),1):
   paths=[folder/(mode+'.png') for mode in ['light','dark']];sizes=[Image.open(p).size for p in paths]
   panel_w=max(s[0] for s in sizes)*SCALE;width=2*MARGIN+2*panel_w+GUTTER;height=TOP+max(s[1] for s in sizes)*SCALE+MARGIN
   page=doc.new_page(width=width,height=height)
   page.insert_text((MARGIN,31),f'{LABELS[name]} / {element}',fontname='hebo',fontsize=22,color=(.12,.14,.17))
   page.insert_text((MARGIN,52),f'{index:02d}/57   |   {fixture_count} fixtures   |   Source {SOURCE_COMMIT[:8]}',fontname='helv',fontsize=10,color=(.35,.38,.42))
   for i,(mode,path,size) in enumerate(zip(['LIGHT','DARK'],paths,sizes)):
    x=MARGIN+i*(panel_w+GUTTER);page.insert_text((x,79),mode,fontname='hebo',fontsize=12,color=(.25,.28,.32))
    rect=fitz.Rect(x,TOP,x+size[0]*SCALE,TOP+size[1]*SCALE);page.insert_image(rect,filename=str(path))
    source_records.append({'collection':name,'element':element,'mode':mode.lower(),'source_png':str(path.relative_to(root)),'png_size':list(size),'png_sha256':digest(path)})
   own_toc.append([1,element,index]);toc.append([2,element,len(combined)+index])
  doc.set_toc(own_toc);doc.set_metadata({'title':LABELS[name]+' - element review sheets (light and dark)','author':'Rhetis library','subject':'56 elements and foundation; one element per page, original PNG resolution preserved'})
  path=out/(name+'-element-sheets.pdf');doc.save(path,garbage=4,deflate=True,deflate_images=True);combined.insert_pdf(doc);doc.close();records.append({'file':path.name,'pages':57,'bytes':path.stat().st_size,'sha256':digest(path)})
 combined.set_toc(toc);combined.set_metadata({'title':'Rhetis - all five element libraries (light and dark)','author':'Rhetis library','subject':'280 elements and five foundations; paired light/dark sheets with collection and element bookmarks'})
 path=out/'all-collections-element-sheets.pdf';combined.save(path,garbage=4,deflate=True,deflate_images=True);combined.close();records.append({'file':path.name,'pages':285,'bytes':path.stat().st_size,'sha256':digest(path)})
 # Check every embedded image against the original pixels, for every individual PDF and the combined PDF.
 checks=[]
 for record in records:
  doc=fitz.open(out/record['file']);names=NAMES if record['pages']==285 else [record['file'].split('-element-sheets.pdf')[0]];idx=0
  assert len(doc)==record['pages']
  for name in names:
   for element,folder,fixture_count in sheets(root,name):
    page=doc[idx];images=page.get_images(full=True);assert len(images)==2,(record['file'],idx,len(images))
    for mode,image in zip(['light','dark'],images):
     source=folder/(mode+'.png');pix=fitz.Pixmap(doc,image[0]);actual=Image.frombytes('RGB' if pix.n==3 else 'RGBA',(pix.width,pix.height),pix.samples).convert('RGB')
     with Image.open(source) as original:expected=original.convert('RGB');assert actual.size==expected.size and actual.tobytes()==expected.tobytes(),(record['file'],idx,mode,'pixels differ')
     for rect in page.get_image_rects(image[0]):assert page.rect.contains(rect),(record['file'],idx,'clipped sheet')
    idx+=1
  checks.append({'file':record['file'],'pages_checked':idx,'embedded_sheet_images_checked':idx*2,'pixel_mismatches':0,'clipped_sheet_images':0,'bookmark_entries':len(doc.get_toc())});doc.close()
 (out/'verification.json').write_text(json.dumps({'source_commit':SOURCE_COMMIT,'collections':5,'elements':280,'foundations':5,'layout':'One element per page; light and dark sheet PNGs side by side, no resampling','files':records,'checks':checks,'source_sheets':source_records},ensure_ascii=False,indent=2)+'\n')
 for r in records:print(r['file'],r['pages'],'pages',r['bytes'],'bytes',flush=True)
 return records
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent);parser.add_argument('--out',type=Path,default=Path(__file__).resolve().parent);a=parser.parse_args();generate(a.root,a.out)
