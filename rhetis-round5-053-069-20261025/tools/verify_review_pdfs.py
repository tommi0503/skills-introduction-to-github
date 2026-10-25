"""Verify coverage, lossless images, PDF layout and every page render."""
from pathlib import Path
from collections import defaultdict
import hashlib,json,re
import fitz
from PIL import Image
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'pdfs'
CHOICES={'rise-block':'timeline','cinder-pulse':'steps','current-fold':'chart-area','scanline-rise':'hub--clover','halo-field':'pyramid','corner-signal':'concentric--market','anchor-frame':'image-frame'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 m=json.loads((OUT/'manifest.json').read_text());rows=[];preview=OUT/'previews';preview.mkdir(exist_ok=True);totals={'fullSheets':0,'samples':0,'pagesRendered':0}
 for c in m['collections']:
  cid=c['collection'];path=ROOT/c['pdf'];assert sha(path)==c['sha256'];doc=fitz.open(path);assert not doc.is_repaired;assert len(doc)==c['pages'];assert len(doc.get_toc())>=len(c['sheets']);assert '전체요소검수시트'in re.sub(r'\s+','',doc[0].get_text())
  expected=set();leaves={r['leaf']for r in c['sheets']}
  for leaf in leaves:
   a=json.loads((ROOT/(cid+'-review/audits')/(leaf+'.json')).read_text());expected.update((leaf,s['fixture'],s['mode'],s['size'])for s in a['states'])
  actual={(s['leaf'],s['fixture'],s['mode'],s['size'])for s in c['samples']};assert actual==expected;assert len(actual)==len(c['samples'])
  images=0
  for s in c['sheets']:
   source=ROOT/s['png'];assert sha(source)==s['pngSHA256'];pg=doc[s['overviewPage']-1];candidates=[r for r in pg.get_images(full=True)if r[2:4]==(s['width'],s['height'])];assert len(candidates)==1,(cid,s['leaf'],s['mode'],candidates)
   pix=fitz.Pixmap(doc,candidates[0][0])
   if pix.colorspace.n!=3:pix=fitz.Pixmap(fitz.csRGB,pix)
   if pix.alpha:pix=fitz.Pixmap(pix,0)
   assert pix.stride==pix.width*3;assert hashlib.sha256(pix.samples).hexdigest()==s['pixelSHA256'],(cid,s['png'],'image pixels differ');images+=1;del pix
  grouped=defaultdict(list)
  for s in c['samples']:
   p=doc[s['page']-1];r=fitz.Rect(s['targetRect']);clip=fitz.Rect(s['sourceClip']);assert p.rect.contains(r)and r.y0>=95.9;assert abs(r.width/r.height-clip.width/clip.height)<.00001
   for other in grouped[s['page']]:assert (r&other).is_empty,(cid,s['page'],'sample overlap')
   grouped[s['page']].append(r)
  for page in doc:
   scale=min(.3,1000/page.rect.width,800/page.rect.height);pix=page.get_pixmap(matrix=fitz.Matrix(scale,scale),alpha=False);assert pix.width>0 and pix.height>0
   for link in page.get_links():
    if link.get('kind')==fitz.LINK_GOTO:assert 0<=link['page']<len(doc)
  choice=CHOICES[cid];samples=[r for r in c['samples']if r['leaf']==choice and r['mode']=='light'];first=samples[0]['page'];small=next(r['page']for r in samples if r['minimum'])
  for label,n in [('detail',first),('minimum',small),('cover',1)]:doc[n-1].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False).save(preview/(cid+'-'+label+'.png'))
  rows.append({'collection':cid,'pdf':c['pdf'],'sha256':c['sha256'],'pagesRendered':len(doc),'losslessSheets':images,'gridSizeSamples':len(actual),'coverage':'pass','imagePixelEquality':'pass','sampleBoundsAndOverlap':'pass','pdfLinks':'pass'});totals['fullSheets']+=images;totals['samples']+=len(actual);totals['pagesRendered']+=len(doc);doc.close();print('VERIFIED',cid,rows[-1]['pagesRendered'],'pages;',images,'lossless sheets;',len(actual),'samples',flush=True)
 assert totals['fullSheets']==435 and totals['samples']==3448
 (OUT/'verification.json').write_text(json.dumps({'status':'pass','method':'Every PDF page rendered; all original embedded sheet pixels compared; all fixture/mode/size states checked against audits; detail bounds, non-overlap and internal links checked.','totals':totals,'collections':rows},ensure_ascii=False,indent=2));print('ALL PDF CHECKS PASS',totals,flush=True)
if __name__=='__main__':main()
