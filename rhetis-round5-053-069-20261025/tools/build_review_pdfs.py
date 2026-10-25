"""Lossless PDF review books from the final audited element PNGs.

Each element has the complete light/dark sheets, readable A3 fixture detail
pages for every advertised size, and the replica comparison. Cropped detail
views reuse the original image object; no image is resized or JPEG encoded.
"""
from pathlib import Path
from collections import OrderedDict
from zoneinfo import ZoneInfo
from datetime import datetime
import hashlib,json,math,re
import fitz
from PIL import Image
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'pdfs';OUT.mkdir(exist_ok=True)
SIZES=['12x6','12x3','9x4','8x6','6x6','6x3','4x4','4x3','3x3']
A3=(1190.5512,841.8898);M=32;SCALE=.75

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pixel_sha(p):
 with Image.open(p)as im:return hashlib.sha256(im.convert('RGB').tobytes()).hexdigest()
def layout(audit,mode):
 states=[s for s in audit['states']if s['mode']==mode];groups=OrderedDict()
 for s in states:groups.setdefault(s['fixture'],[]).append(s)
 cols=SIZES+sorted({s['size']for s in states if s['size']not in SIZES})
 def dims(s):
  r=s['slot'];return(math.ceil(r['x']+r['w']+6)-math.floor(r['x']-6),math.ceil(r['y']+r['h']+6)-math.floor(r['y']-6))
 widths={k:max([dims(s)[0]for s in states if s['size']==k]or[80])for k in cols};xs={};x=210
 for k in cols:xs[k]=x;x+=widths[k]+12
 rows=[];y=40
 for name,ss in groups.items():
  rh=max(dims(s)[1]for s in ss)+38;minimum=next(s['size']for s in ss if s['minimum']);cells=[]
  for k in cols:
   s=next((s for s in ss if s['size']==k),None)
   if s:
    w,h=dims(s);cells.append({'size':k,'minimum':k==minimum,'clip':[xs[k],y+28,xs[k]+w,y+28+h]})
  rows.append({'fixture':name,'minimum':minimum,'cells':cells});y+=rh
 return (x,y),rows

def text(page,point,value,size=12,bold=False):page.insert_text(point,value,fontname='hebo'if bold else'helv',fontsize=size,color=(.12,.15,.2))
def korean(page,point,value,size=14):page.insert_text(point,value,fontname='korea',fontsize=size,color=(.12,.15,.2))
def header(page,cid,leaf,section,fixture=None,minimum=None):
 text(page,(M,29),cid+' / '+leaf,16,True);text(page,(M,49),section+(('  |  '+fixture+'  |  min '+minimum)if fixture else''),11)
 text(page,(M,page.rect.height-15),'Rhetis Round 5  |  '+str(page.number+1),9)

def build(c):
 cid=c['id'];R=ROOT/(cid+'-review');folders=sorted(p.name for p in(ROOT/cid/'elements').iterdir()if p.is_dir());leaves=folders+(['foundation-panels']if json.loads((R/'map.json').read_text()).get('panels')else[])
 doc=fitz.open();doc.new_page(width=A3[0],height=A3[1]);doc.new_page(width=A3[0],height=A3[1]);toc=[[1,cid,1],[2,'Element index',2]];records=[];details=[];index=[]
 for leaf in leaves:
  audit=json.loads((R/'audits'/(leaf+'.json')).read_text());leafpage=len(doc)+1;index.append((leaf,leafpage));toc.append([2,leaf,leafpage])
  for mode in ['light','dark','replica']:
   path=R/'sheets'/(leaf+'-'+mode+'.png');rel=str(path.relative_to(ROOT));assert sha(path)==audit['outputs']['sheets/'+path.name],rel+' is stale'
   with Image.open(path)as im:W,H=im.size
   source=fitz.open();imagepage=source.new_page(width=W,height=H);imagepage.insert_image(imagepage.rect,stream=path.read_bytes())
   scale=min(1,13800/max(W,H));pg=doc.new_page(width=W*scale+M*2,height=H*scale+M*2+48);rect=fitz.Rect(M,62,M+W*scale,62+H*scale);pg.show_pdf_page(rect,source,0)
   header(pg,cid,leaf,mode.title()+' full sheet  |  original PNG '+str(W)+' x '+str(H));overview=pg.number;toc.append([3,mode.title()+' full sheet',overview+1]);records.append({'collection':cid,'leaf':leaf,'mode':mode,'png':rel,'pngSHA256':sha(path),'pixelSHA256':pixel_sha(path),'width':W,'height':H,'overviewPage':overview+1,'imageRect':list(rect)})
   if mode!='replica':
    expected,rows=layout(audit,mode);assert expected==(W,H),(rel,expected,(W,H))
    for row in rows:
     pg=None;x=y=rowh=0;first=None
     for cell in row['cells']:
      clip=fitz.Rect(cell['clip']);assert source[0].rect.contains(clip)
      factor=min(SCALE,(A3[0]-2*M)/clip.width);w=clip.width*factor;h=clip.height*factor;tileh=h+23
      if pg is None or (x+w>A3[0]-M+.01 and y+rowh+12+tileh>A3[1]-M-12):
       pg=doc.new_page(width=A3[0],height=A3[1]);header(pg,cid,leaf,mode.title()+' fixture detail',row['fixture'],row['minimum']);x=M;y=76;rowh=0
       if first is None:first=pg.number+1;toc.append([3,mode.title()+' / '+row['fixture']+' / min '+row['minimum'],first])
      elif x+w>A3[0]-M+.01:x=M;y+=rowh+12;rowh=0
      if y+tileh>A3[1]-M-12:
       pg=doc.new_page(width=A3[0],height=A3[1]);header(pg,cid,leaf,mode.title()+' fixture detail',row['fixture'],row['minimum']);x=M;y=76;rowh=0
      label=cell['size']+('  MIN'if cell['minimum']else'');text(pg,(x,y+12),label,11,True);dest=fitz.Rect(x,y+20,x+w,y+20+h);assert pg.rect.contains(dest);pg.show_pdf_page(dest,source,0,clip=clip,keep_proportion=False)
      details.append({'collection':cid,'leaf':leaf,'mode':mode,'fixture':row['fixture'],'size':cell['size'],'minimum':cell['minimum'],'page':pg.number+1,'png':rel,'sourceClip':list(clip),'targetRect':list(dest)});x+=w+12;rowh=max(rowh,tileh)
   source.close()
  print(cid,leaf,'PDF pages',len(doc),flush=True)
 # Cover and a clickable index are added after page numbers are known.
 pg=doc[0];text(pg,(48,66),'RHETIS / ROUND 5',28,True);korean(pg,(48,108),'전체 요소 검수 시트',24);text(pg,(48,151),cid,24,True)
 body=[f"{len(folders)} element designs + {len(leaves)-len(folders)} foundation panel sheet",f"{len(records)} full sheets / {len(details)} grid-size samples / {len(doc)} PDF pages",'Light / Dark / Replica comparison', 'A3 landscape detail pages; original-resolution overview pages']
 for i,line in enumerate(body):text(pg,(48,199+i*30),line,15)
 notes=['각 요소의 전체 시트와 모든 fixture 크기를 수록했습니다.','책갈피나 다음 페이지의 목록에서 요소를 선택하세요.','확대 페이지는 A3 가로형입니다. MIN은 fixture의 최소 칸입니다.','전체 시트는 원본 해상도로 보존해 확대해 볼 수 있습니다.','replica 대조는 원본 조각, 12×6, 최소 칸 순서입니다.','PDF는 마지막 검수가 끝난 PNG를 사용하며 이미지 손실 압축을 하지 않습니다.']
 for i,line in enumerate(notes):korean(pg,(48,374+i*30),line,14)
 korean(pg,(48,645),'원본 색은 팔레트 역할로 치환되며, 사진 자리는 중성 placeholder입니다.',12);text(pg,(48,691),'Source: tommi0503/skills-introduction-to-github / '+ROOT.name,12)
 header(doc[1],cid,'INDEX','Click an element; PDF bookmarks include fixture sections')
 for i,(leaf,page)in enumerate(index):
  yy=82+i*18;text(doc[1],(M,yy),leaf,12);text(doc[1],(A3[0]-95,yy),str(page),12);doc[1].insert_link({'kind':fitz.LINK_GOTO,'from':fitz.Rect(M,yy-13,A3[0]-M,yy+3),'page':page-1})
 doc.set_toc(toc);doc.set_metadata({'title':cid+' — all element review sheets','author':'Rhetis','subject':'Light, dark, replica comparisons and every fixture size','keywords':'Rhetis, round5, element library, review, responsive, min'});doc.subset_fonts()
 out=OUT/(cid+'-elements-review.pdf');doc.save(out,garbage=4,deflate=True);doc.close()
 return{'collection':cid,'elements':len(folders),'panelSheets':len(leaves)-len(folders),'pdf':str(out.relative_to(ROOT)),'pages':len(fitz.open(out)),'bytes':out.stat().st_size,'sha256':sha(out),'sheets':records,'samples':details}

def main():
 collections=json.loads((ROOT/'collections.json').read_text());result=[build(c)for c in collections];report={'createdKST':datetime.now(ZoneInfo('Asia/Seoul')).isoformat(),'source':'Final audited PNG sheets; element CSS and fixtures unchanged','collections':result,'elements':sum(c['elements']for c in result),'fullSheets':sum(len(c['sheets'])for c in result),'samples':sum(len(c['samples'])for c in result),'pdfPages':sum(c['pages']for c in result)};(OUT/'manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('BUILT',report['elements'],'elements;',report['fullSheets'],'sheets;',report['samples'],'samples;',report['pdfPages'],'PDF pages',flush=True)
if __name__=='__main__':main()
