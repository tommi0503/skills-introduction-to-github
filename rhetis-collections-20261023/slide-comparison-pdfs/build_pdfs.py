"""Collate existing original/copy comparison PNGs without resampling."""
from pathlib import Path
import argparse,hashlib,json,re
import fitz
from PIL import Image
NAMES={'fluxweave':18,'cyanloop':18,'roundrise':24,'nightchamfer':18,'glasspulse':18}
SOURCE_COMMIT='d454a4c5d67bd20ba013eaa65be8a0f7ace064d7';SCALE=.75;MARGIN=24
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def ordered(root,name,kind):
 files=sorted((root/(name+'-review')/kind).glob('*.png'));assert len(files)==NAMES[name],(name,kind,len(files));return files

def generate(root,out):
 out.mkdir(parents=True,exist_ok=True);combined=fitz.open();toc=[];records=[];source_records=[]
 for name,count in NAMES.items():
  replica=ordered(root,name,'compare-replica');reassembled=ordered(root,name,'compare-reassembled');doc=fitz.open();own_toc=[];toc.append([1,name.title(),len(combined)+1])
  for i,(a,b) in enumerate(zip(replica,reassembled),1):
   assert re.search(r'(\d+)\.png$',a.name)[1]==re.search(r'(\d+)\.png$',b.name)[1]
   sizes=[Image.open(p).size for p in [a,b]];width=2*MARGIN+max(s[0] for s in sizes)*SCALE;height=136+sum(s[1]*SCALE for s in sizes)+MARGIN
   page=doc.new_page(width=width,height=height)
   page.insert_text((MARGIN,31),f'{name.title()} / Slide {i:02d}',fontname='hebo',fontsize=22,color=(.12,.14,.17))
   page.insert_text((MARGIN,52),f'{i:02d}/{count}   |   Original versus replica and library reassembly   |   Source {SOURCE_COMMIT[:8]}',fontname='helv',fontsize=10,color=(.35,.38,.42))
   y=76
   for kind,path,size,label in zip(['replica','reassembled'],[a,b],sizes,['ORIGINAL  |  REPLICA','ORIGINAL  |  LIBRARY REASSEMBLY']):
    page.insert_text((MARGIN,y),label,fontname='hebo',fontsize=12,color=(.25,.28,.32));y+=12
    rect=fitz.Rect(MARGIN,y,MARGIN+size[0]*SCALE,y+size[1]*SCALE);page.insert_image(rect,filename=str(path));y=rect.y1+36
    source_records.append({'collection':name,'slide':i,'comparison':kind,'source_png':str(path.relative_to(root)),'png_size':list(size),'png_sha256':sha(path)})
   assert y-36<=height-MARGIN,(name,i,'image exceeds page')
   own_toc.append([1,f'Slide {i:02d}',i]);toc.append([2,f'Slide {i:02d}',len(combined)+i])
  doc.set_toc(own_toc);doc.set_metadata({'title':name.title()+' - original and copy slide comparison','author':'Rhetis library','subject':'One original slide per page, with original/replica and original/library reassembly comparison rows'})
  p=out/(name+'-slide-comparison.pdf');doc.save(p,garbage=4,deflate=True,deflate_images=True);combined.insert_pdf(doc);doc.close();records.append({'file':p.name,'pages':count,'bytes':p.stat().st_size,'sha256':sha(p)})
 combined.set_toc(toc);combined.set_metadata({'title':'Rhetis - original and copy slide comparison, all five collections','author':'Rhetis library','subject':'96 source slides; original/replica and original/library reassembly comparison rows, with bookmarks'})
 p=out/'all-collections-slide-comparison.pdf';combined.save(p,garbage=4,deflate=True,deflate_images=True);combined.close();records.append({'file':p.name,'pages':96,'bytes':p.stat().st_size,'sha256':sha(p)})
 checks=[]
 for r in records:
  doc=fitz.open(out/r['file']);names=list(NAMES) if r['pages']==96 else [r['file'].split('-slide-comparison.pdf')[0]];idx=0
  assert len(doc)==r['pages']
  for name in names:
   for a,b in zip(ordered(root,name,'compare-replica'),ordered(root,name,'compare-reassembled')):
    page=doc[idx];images=page.get_images(full=True);assert len(images)==2,(r['file'],idx,len(images))
    for path,image in zip([a,b],images):
     pix=fitz.Pixmap(doc,image[0]);actual=Image.frombytes('RGB' if pix.n==3 else 'RGBA',(pix.width,pix.height),pix.samples).convert('RGB')
     with Image.open(path) as im:expected=im.convert('RGB');assert actual.size==expected.size and actual.tobytes()==expected.tobytes(),(r['file'],idx,'pixel mismatch')
     assert all(page.rect.contains(rect) for rect in page.get_image_rects(image[0])),(r['file'],idx,'clipped')
    idx+=1
  checks.append({'file':r['file'],'pages_checked':idx,'embedded_comparison_images_checked':idx*2,'pixel_mismatches':0,'clipped_images':0,'bookmarks':len(doc.get_toc())});doc.close()
 (out/'verification.json').write_text(json.dumps({'source_commit':SOURCE_COMMIT,'original_slides':96,'comparisons':192,'layout':'Each page: original | replica above; original | library reassembly below. Existing comparison PNGs embedded losslessly without resampling.','files':records,'checks':checks,'source_comparisons':source_records},ensure_ascii=False,indent=2)+'\n')
 for r in records:print(r['file'],r['pages'],'pages',r['bytes'],'bytes',flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent);p.add_argument('--out',type=Path,default=Path(__file__).resolve().parent);a=p.parse_args();generate(a.root,a.out)
