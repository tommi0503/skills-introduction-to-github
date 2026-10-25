#!/usr/bin/env python3
"""Lossless PDF review books from every final reviewed size matrix.
Install: python -m pip install img2pdf pymupdf Pillow
One complete element matrix per page; foundation and panel pages follow.
PNG IDAT streams are embedded directly, retaining every source pixel.
"""
from pathlib import Path
import collections,datetime,hashlib,json,struct,shutil,sys
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
import img2pdf,fitz
ROOT=Path(__file__).resolve().parents[1]
PROJECTS=['vectorbox','seedmark','crossrail','meridian-deck','onboard-docket']
H=lambda b:hashlib.sha256(b).hexdigest()

def png_stream(p):
 b=p.read_bytes();assert b[:8]==b'\x89PNG\r\n\x1a\n';pos=8;chunks=[];head=None
 while pos<len(b):
  n=struct.unpack('>I',b[pos:pos+4])[0];kind=b[pos+4:pos+8];data=b[pos+8:pos+8+n]
  if kind==b'IHDR':head=struct.unpack('>IIBBBBB',data)
  if kind==b'IDAT':chunks.append(data)
  pos+=12+n
 assert head[2:]==(8,2,0,0,0),('Expected reviewed RGB8, non-interlaced PNG',p,head)
 return head[:2],b''.join(chunks)
def source(k,mode):
 P=ROOT/(k+'-project');rows=[]
 for d in sorted((P/k/'elements').iterdir()):
  if d.is_dir():rows.append({'collection':k,'leaf':d.name,'kind':'element','mode':mode,'path':P/'sheets'/f'{d.name}-{mode}.png'})
 for f in sorted((P/'foundation-sheets').glob('*-'+mode+'.png')):rows.append({'collection':k,'leaf':f.stem[:-(len(mode)+1)],'kind':'foundation','mode':mode,'path':f})
 for f in sorted((P/'panel-sheets').glob('*-'+mode+'.png')):rows.append({'collection':k,'leaf':f.stem[:-(len(mode)+1)],'kind':'panel','mode':mode,'path':f})
 return rows

def book(path,rows,reviewed):
 for r in rows:
  rel=r['path'].relative_to(ROOT).as_posix();assert reviewed[rel]['sha256']==H(r['path'].read_bytes()),('Not the last directly reviewed image',rel)
 raw=img2pdf.convert([str(r['path'])for r in rows],title=path.stem,author='Rhetis Library Review',nodate=True)
 tmp=path.with_suffix('.tmp.pdf');tmp.write_bytes(raw)
 doc=fitz.open(tmp);toc=[];last=None
 for index,r in enumerate(rows,1):
  group=r['collection']
  if group!=last:toc.append([1,group,index]);last=group
  toc.append([2,r['kind']+' / '+r['leaf']+' / '+r['mode'],index])
 doc.set_toc(toc);doc.save(path,garbage=0,deflate=False);doc.close();tmp.unlink()
 result={'path':path.relative_to(ROOT).as_posix(),'downloadPath':'deliverables/'+path.name,'bytes':path.stat().st_size,'sha256':H(path.read_bytes()),'pages':len(rows),'elementPages':sum(r['kind']=='element'for r in rows),'foundationAndPanelPages':sum(r['kind']!='element'for r in rows),'checks':[]}
 assert path.stat().st_size<100_000_000,('GitHub file limit conservative100MB',path)
 doc=fitz.open(path);assert doc.page_count==len(rows)
 for index,r in enumerate(rows):
  page=doc[index];ims=page.get_images(full=True);assert len(ims)==1,(path,index,ims);xref=ims[0][0];size,pngraw=png_stream(r['path']);pdfraw=doc.xref_stream_raw(xref)
  assert pdfraw==pngraw,('PNG compressed pixels were recompressed or changed',path,index)
  assert(ims[0][2],ims[0][3])==size;rects=page.get_image_rects(xref);assert len(rects)==1
  rect=rects[0];assert max(abs(rect.x0),abs(rect.y0),abs(rect.x1-page.rect.width),abs(rect.y1-page.rect.height))<.1,('PDF image is cropped',path,index,rect,page.rect)
  assert abs(rect.width/rect.height-size[0]/size[1])<.0001
  result['checks'].append({'page':index+1,'collection':r['collection'],'leaf':r['leaf'],'kind':r['kind'],'mode':r['mode'],'sourcePNG':r['path'].relative_to(ROOT).as_posix(),'sourcePNG_SHA256':H(r['path'].read_bytes()),'PNGdimensions':size,'PDFpagePoints':[page.rect.width,page.rect.height],'losslessPNGStreamSHA256':H(pdfraw),'fullPageUncropped':True})
 doc.close();print(path.name,len(rows),'pages',path.stat().st_size,'bytes / lossless stream and full-page bounds passed',flush=True);return result

def run():
 reviewed=json.loads((ROOT/'root-visual-review.json').read_text())['images'];reports=[];allrows=[]
 for k in PROJECTS:
  P=ROOT/(k+'-project');paired={}
  for mode in['light','dark']:
   rows=source(k,mode);path=P/('library-'+mode+'.pdf');report=book(path,rows,reviewed);flat=ROOT/'deliverables'/(k+'-library-'+mode+'.pdf');shutil.copyfile(path,flat);report['downloadPath']=flat.relative_to(ROOT).as_posix();reports.append(report)
   for r in rows:paired[(r['kind'],r['leaf'],mode)]=r
  for kind,leaf in sorted({(a,b)for a,b,_ in paired},key=lambda x:({'element':0,'foundation':1,'panel':2}[x[0]],x[1])):
   allrows.extend(paired[(kind,leaf,m)]for m in['light','dark'])
 report=book(ROOT/'deliverables/all-elements-review.pdf',allrows,reviewed);reports.append(report)
 counts=collections.Counter((r['kind'],r['mode'])for r in allrows);assert counts[('element','light')]==159 and counts[('element','dark')]==159
 result={'schema':'rhetis.lossless-review-pdf/1','generatedAtUTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'verified','policy':'One full final matrix per PDF page. Original PNG IDAT streams remain byte-identical; no JPEG conversion, resizing, crop, ratio change or colour quantization. Foundation/panel evidence follows elements.','elementDesigns':159,'globalPages':len(allrows),'globalElementPages':318,'globalFoundationAndPanelPages':len(allrows)-318,'pdfCount':len(reports),'pdfs':reports,'errors':[]}
 (ROOT/'pdf-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 (ROOT/'deliverables/PDF-SHA256SUMS').write_text(''.join(x['sha256']+'  '+Path(x['downloadPath']).name+'\n'for x in reports))
if __name__=='__main__':run()
