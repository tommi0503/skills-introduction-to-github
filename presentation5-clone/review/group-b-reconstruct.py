"""Prepare per-page editable geometric and text data from inspected reference crops.
The output contains only paths, rectangles, loaded-font text and designated image placeholders.
No pixels from references are included in the presentation renderer.
"""
import json,math,os,sys,subprocess,concurrent.futures
from pathlib import Path
sys.path.insert(0,'/tmp/envato-b-python')
import cv2,numpy as np,pytesseract
from PIL import Image,ImageDraw
os.environ['OMP_THREAD_LIMIT']='1'
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'public/reference/groups/b.json').read_text())
# Native positions converted from percentages of the independently cropped slide.
# These regions were identified by individually inspecting all35 input sheets.
PH={}
def masks(deck,preview,items):
 for cell,regions in items.items():PH[f'p{deck:03}/s{preview:02}-{cell:02}']=regions
masks(50,2,{1:[[54,0,46,50]],2:[[66,0,26,93]],3:[[57,0,43,100]],4:[[0,0,100,18]],5:[[0,0,100,82]],6:[[0,0,100,100]],9:[[0,0,60,100]],13:[[0,50,40,50]],16:[[0,0,16,100]]})
masks(51,1,{1:[[0,0,100,100]],2:[[47,8,47,84]],3:[[0,0,100,100]],5:[[0,0,100,41]],9:[[0,0,100,100]],11:[[0,0,100,100]]})
masks(51,5,{1:[[0,0,100,100]]})
masks(64,4,{1:[[35,42,65,44]],2:[[0,10,47,90]],4:[[8,40,25,57]],7:[[0,40,20,60]],8:[[27,10,73,47]]})
masks(69,1,{2:[[5,8,34,85]],3:[[5,12,24,80],[29,54,23,36]],4:[[63,39,23,52]],5:[[48,12,20,78],[71,12,24,78]],6:[[5,50,45,40]],7:[[0,49,100,51]],9:[[5,12,24,55],[32,33,25,55]]})
masks(69,2,{3:[[50,10,42,85]],5:[[5,19,22,28],[5,51,22,30]],6:[[0,0,39,100]]})
masks(69,3,{1:[],2:[[5,8,34,85]],3:[[5,12,24,80],[29,54,23,36]],4:[[5,50,45,40]]})
masks(69,4,{1:[[48,12,20,78],[71,12,24,78]],2:[[63,39,23,52]],4:[[0,49,100,51]],5:[[5,12,24,55],[32,33,25,55]],6:[[51,45,45,44]]})
masks(73,2,{2:[[45,0,52,100]],3:[[59,32,18,32]],5:[[8,11,32,78]],6:[[0,0,100,100]],7:[[0,0,38,100]],8:[[0,0,43,54],[59,64,41,36]],9:[[53,0,47,50]]})
masks(73,3,{1:[[50,11,41,34]],2:[[45,14,18,74]],3:[[0,0,100,100]],4:[[74,11,26,89],[0,60,26,40]],5:[[41,0,30,100]],6:[[44,0,56,64]],7:[[0,0,100,100]],8:[[57,5,43,88]],9:[[0,0,43,54],[59,64,41,36]]})
masks(80,2,{1:[[4,40,36,48]],2:[[55,49,21,39],[76,49,21,39]],3:[[25,13,17,35],[57,18,10,18],[51,57,25,31]],4:[[26,47,28,45]],5:[[26,38,16,29],[45,14,26,60],[72,13,22,26],[76,41,22,33]],6:[[7,20,29,65]]})
masks(80,3,{1:[[0,31,43,69]],2:[[47,8,26,40],[73,8,27,92]],3:[[46,34,18,39],[64,34,18,39],[82,65,18,35]],4:[[50,35,25,65],[74,35,24,30],[74,65,24,35]],5:[[8,35,28,55]],6:[[62,10,10,18],[82,30,10,18],[62,55,10,18],[82,76,10,18]],7:[[4,45,45,46]],8:[[70,8,30,41],[0,69,33,31],[70,63,20,32]],9:[[38,44,25,55]]})
masks(80,6,{1:[[5,22,29,61]],2:[[5,22,29,61]],3:[[64,16,27,59]],4:[[9,40,29,51]],5:[[24,48,23,44]],6:[[45,40,28,60]],7:[[53,41,23,49]],8:[[25,53,19,41],[57,8,36,42]],9:[[42,41,23,59]]})
masks(80,8,{1:[[5,22,29,61]],2:[[47,8,26,40],[73,8,27,92]],3:[[46,34,18,39],[64,34,18,39],[82,65,18,35]],4:[[25,13,17,35],[57,18,10,18],[51,57,25,31]]})
masks(81,2,{1:[[35,30,24,70],[60,30,18,28],[79,30,18,40],[60,60,18,40],[79,72,18,28]],4:[[29,35,38,58]],5:[[30,30,65,57]]})
masks(81,3,{1:[[41,25,55,67]],2:[[41,25,55,67]],3:[[29,14,40,50]],4:[[44,40,22,53]],5:[[38,32,20,57],[28,68,10,16]],6:[[64,15,32,85]],7:[[31,27,24,65]]})
masks(81,4,{1:[[38,32,20,57],[28,68,10,16]],3:[[29,35,38,58]],4:[[57,26,14,25],[44,54,27,45]]})
masks(81,5,{1:[[53,29,24,65],[78,28,18,42]],2:[[18,29,28,64]],3:[[16+i*22,28+j*36,10,18] for j in range(2) for i in range(4)],4:[[48,15,48,33],[38,51,22,39],[63,51,21,39]],7:[],8:[[57,26,14,25],[44,54,27,45]]})
masks(91,2,{1:[[8,12,24,77],[32,35,21,65]],2:[[8,32,21,32],[31,32,39,32],[71,32,21,32]],3:[[10,32,43,42]]})
masks(91,3,{2:[[9+i*22,32,19,44] for i in range(4)],3:[[50,20,25,65]],4:[],6:[[3,46,15,16],[76,46,18,16]],8:[[35,22,26,70]],9:[[8,68,44,30]],10:[[21,0,52,100]],12:[[3,49,23,19],[76,49,24,19]],13:[[5+i*19,30+(i%2)*25,9,15] for i in range(5)],14:[[54,50,46,41]],15:[[20,42,70,45]],16:[[74,48,22,39]]})
masks(92,1,{1:[[38,0,32,100]],3:[[45,55,55,45]],4:[[3,20,67,21],[3,43,67,21],[3,67,67,21]],5:[[33,15,31,85]],8:[[44,25,10,18]]})
# Correct combined portrait regions in advice slide.
PH['p092/s01-08']=[[44,25,10,18]]+[[5+i*32,61,10,18] for i in range(3)]
masks(92,2,{1:[[28,22,27,58]],2:[[0,41,100,59]],3:[[31,41,21,45]],4:[[38,0,32,100]],7:[[45,55,55,45]],8:[[35,40,61,33]],9:[[33,15,31,85]]})
masks(92,4,{1:[[40,0,60,100]],3:[[3,20,67,21],[3,43,67,21],[3,67,67,21]],6:[[0,47,96,39]],7:[[41,5,20,40],[76,53,22,39]]})
for pv in [2,4]:
 for c in range(1,17):
  # Bulbs containing pictorial collages, puzzle illustration or 3D art are designated imagery.
  if pv==2 and c in [1,2,7,9,14,16] or pv==4 and c in [1,5,7,10,11,12,14,16]:
   PH[f'p100/s{pv:02}-{c:02}']=[[34,17,33,78]]
masks(101,2,{1:[[0,0,100,100]],2:[[2,44,31,46]],9:[[60,9,37,83]],8:[[3,82,7,10],[36,82,7,10],[69,82,7,10]]})
masks(101,3,{1:[[3,44,31,46]],2:[[52,6,46,88]],3:[[4,55,43,45]],4:[[35,0,32,47],[0,53,33,47],[68,53,32,47]],5:[[27,3,32,41],[3,48,30,46]],6:[[0,30,15,62],[85,30,15,62]]})
masks(104,2,{1:[[9+i*29,29,23,41] for i in range(3)],2:[[6,30,42,65]],4:[[8+i*29,29,24,42] for i in range(3)],5:[[48,31,50,61]],6:[[8+i*29,58,24,42] for i in range(3)],7:[[10+i*30,34,20,39] for i in range(3)],8:[[65,28,30,66]],9:[[49,14,51,79]]})
masks(104,3,{1:[[58,3,40,94]],2:[[41,15,25,57],[70,15,25,57]],3:[[42,28,52,64]],5:[[0,28,52,64]],6:[[6,22,41,61]],7:[[6,26,56,64]],9:[[54,29,40,66]]})
masks(107,2,{1:[[13,19,20,74]],2:[[33,10,61,90]],3:[[0,10,25,90],[70,56,30,44]],4:[[0,11,67,89]]})
masks(107,5,{1:[[33,10,61,90]],2:[[0,10,25,90],[70,56,30,44]],3:[[6,10,29,77]],4:[[0,42,38,58]],5:[[29,11,42,68]],6:[[28,48,45,52]],7:[[56,11,37,66]],8:[[51,11,24,65],[76,54,24,46]]})
# Reference105 index chosen by the saved row-major crop inventory, not inferred order.
for deck in manifest:
 if deck['id']!='p105':continue
 for s in deck['slides']:
  x,y,w,h=s['crop'];pv=int(s['id'][1:3]);key=f'p105/{s["id"]}'
  if w>300:PH[key]=[[0,0,100,100]];continue
  if pv==3:
   if x==19 and y==182:PH[key]=[[40,14,60,80]]
   if x==19 and y==310:PH[key]=[[0,10,63,85]]
   if x==19 and y==438:PH[key]=[[0,10,100,62]]
   if x==19 and y==566:PH[key]=[[0,55,100,45]]
   if x==19 and y==694:PH[key]=[[0,0,100,100]]
   if x==241 and y==54:PH[key]=[[6,23,90,44]]
   if x==241 and y==182:PH[key]=[[55,0,45,100]]
   if x==241 and y==310:PH[key]=[[0,0,100,67]]
   if x==241 and y in [438,566,694]:PH[key]=[[6,17,35,23],[55,29,35,23],[6,52,35,23],[55,73,35,23]]
   if x in [465,689] and y in [54,182] or x==19 and y==823:PH[key]=[[13+i*29,24+j*39,14,23] for i in range(3) for j in range(2 if y==182 else 1)]
   if x in [689,241] and y in [-74,823]:PH[key]=[[0,10,45,90]]
  else:
   if x in [465,689] and y>=298:PH[key]=[[10,22,52,60]] # geographical map illustration
   if x in [911,1134] and y>=298:
    PH[key]=[[47,5,53,90]] if x==911 else [[0,0,50,90]]
# Per-page choices of font face come from visible family characteristics, not machine OCR.
FONT={50:'Bebas Neue',51:'DM Sans',55:'Roboto Condensed',60:'DM Sans',64:'Poppins',69:'DM Sans',73:'DM Sans',80:'Montserrat',81:'DM Sans',91:'DM Sans',92:'DM Sans',100:'Poppins',101:'DM Sans',104:'Anton',105:'Roboto Condensed',107:'DM Sans'}
TEXT='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
def css(rgb):return '#'+''.join(f'{int(v):02x}' for v in rgb)
def elem(k,x,y,w,h,**a):return dict(kind=k,x=x,y=y,w=w,h=h,**a)
def process(args):
 did,s=args;path=ROOT/'public'/s['reference'].lstrip('/');im=Image.open(path).convert('RGB');arr=np.array(im);hh,ww=arr.shape[:2];key=f'{did}/{s["id"]}';photos=PH.get(key,[])
 # Background is median of edge color frequencies; set dominant solid color deliberately.
 q=(arr//24)*24;colors,counts=np.unique(q.reshape(-1,3),axis=0,return_counts=True);rgb=colors[counts.argmax()];close=(np.max(np.abs(arr.astype(int)-rgb),axis=2)<28);bg=css(np.median(arr[close],axis=0));
 if did=='p050':bg='#090a09' if bg<'#aaaaaa' else '#e60012'
 elements=[];mask=np.zeros((hh,ww),np.uint8)
 for x,y,w,h in photos:
  ix,iy,iw,ih=round(x*ww/100),round(y*hh/100),round(w*ww/100),round(h*hh/100)
  cv2.rectangle(mask,(ix,iy),(ix+iw,iy+ih),255,-1)
 # OCR uses4x nearest-native enlargement solely for recognition, not rendering.
 clean=arr.copy();clean[mask>0]=np.array([229,229,229]);up=cv2.resize(arr,None,fx=4,fy=4,interpolation=cv2.INTER_CUBIC)
 data=pytesseract.image_to_data(up,config='--psm 11',output_type=pytesseract.Output.DICT)
 lines={};removed=mask.copy();replacements=[]
 for i,raw in enumerate(data['text']):
  word=raw.strip();conf=float(data['conf'][i]);
  if not word or conf<15:continue
  x,y,w,h=[data[k][i]/4 for k in ['left','top','width','height']]
  if photos!=[[0,0,100,100]] and mask[min(hh-1,int(y+h/2)),min(ww-1,int(x+w/2))]>0:continue
  # Mark words even when spelling is unreadable to prevent glyphs becoming geometric paths.
  cv2.rectangle(removed,(max(0,int(x)-1),max(0,int(y)-1)),(min(ww,int(x+w)+1),min(hh,int(y+h)+1)),255,-1)
  if w<1 or h<1:continue
  lk=(data['block_num'][i],data['par_num'][i],data['line_num'][i]);lines.setdefault(lk,[]).append((x,y,w,h,word,conf))
 # Connected saturated/neutral regions become a small reusable polygon primitive.
 # OCR paint is excluded. All designated photographs are excluded.
 work=arr.copy();work[removed>0]=np.array([253,251,249])
 quant=(work//40)*40
 colors,counts=np.unique(quant.reshape(-1,3),axis=0,return_counts=True)
 for rgb,ct in sorted(zip(colors,counts),key=lambda z:z[1],reverse=True)[:38]:
  if ct<ww*hh*.002:continue
  region=np.all(quant==rgb,axis=2).astype(np.uint8)*255;region[removed>0]=0
  region=cv2.morphologyEx(region,cv2.MORPH_CLOSE,np.ones((2,2),np.uint8))
  contours,_=cv2.findContours(region,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  for c in contours:
   area=cv2.contourArea(c);x,y,w,h=cv2.boundingRect(c)
   if area<ww*hh*.002 or w<4 or h<3 or area>ww*hh*.96:continue
   comp=np.zeros((hh,ww),np.uint8);cv2.drawContours(comp,[c],-1,255,-1);pixels=arr[(comp>0)&(removed==0)];
   if len(pixels)==0:continue
   fill=css(np.median(pixels,axis=0))
   if np.max(np.abs(np.array([int(fill[i:i+2],16) for i in [1,3,5]])-np.array([int(bg[i:i+2],16) for i in [1,3,5]])))<12:continue
   # Dense texture is imagery, not geometric design. Flat vector fills have tight color variance.
   if np.mean(np.std(pixels.astype(float),axis=0))>30:continue
   approximation=cv2.approxPolyDP(c,max(.7,cv2.arcLength(c,True)*.005),True).reshape(-1,2)
   if len(approximation)>40:continue
   # Individual letter shapes are usually tiny and tall; deliberately avoid reconstructing glyphs.
   if area<ww*hh*.005 and w<h*.85:continue
   if len(approximation)==4 and area/(w*h)>.9:elements.append(elem('box',x/ww*100,y/hh*100,w/ww*100,h/hh*100,fill=fill))
   else:elements.append(elem('path',0,0,100,100,points=[dict(x=float(a)/ww*100,y=float(b)/hh*100) for a,b in approximation],color=fill,fill=fill,strokeWidth=0,closed=True))
 # Explicit image placeholders are placed after extracted design shapes and before typography.
 for x,y,w,h in photos:elements.append(elem('image',x,y,w,h,text='Photograph, device screen or complex illustration placeholder'))
 for lk,words in lines.items():
  words.sort(key=lambda z:z[0]);x=min(z[0] for z in words);y=min(z[1] for z in words);right=max(z[0]+z[2] for z in words);bottom=max(z[1]+z[3] for z in words)
  txt=' '.join(z[4] for z in words);conf=sum(z[5] for z in words)/len(words);height=bottom-y
  if len(txt)<2 and not txt.isdigit():continue
  # Repair unreadable prose with genuine ordinary text of comparable length.
  bad=conf<48 or sum(not(c.isalnum() or c.isspace() or c in '.,:%$+-/&?!’\"()') for c in txt)>max(2,len(txt)*.15)
  if bad:
   original=txt
   if height<hh*.033 and len(txt)>8:txt=TEXT[:max(16,len(txt))].rsplit(' ',1)[0]+'.'
   elif len(txt)>12:txt='Your Title Here'
   elif not any(c.isalpha() for c in txt):txt='01'
   else:txt='Lorem ipsum'
   replacements.append({'box':[x,y,right-x,bottom-y],'ocr':original,'replacement':txt,'reason':'Native contact-sheet text is too small or blurred to read confidently.'})
  font=FONT[int(did[1:])];size=height/hh*720*1.25
  if int(did[1:]) in [50,104] and height<hh*.035:font='Roboto Condensed' if did=='p050' else 'DM Sans'
  if did=='p080' and height>hh*.045:font='Michroma'
  # Infer ink median by the darkest/brighest pixels inside the recognized boxes.
  sub=arr[max(0,int(y)):min(hh,int(bottom+1)),max(0,int(x)):min(ww,int(right+1))]
  gray=cv2.cvtColor(sub,cv2.COLOR_RGB2GRAY);white=np.quantile(gray,.9);black=np.quantile(gray,.1)
  ink=sub[gray<black+8] if np.mean(gray)>110 else sub[gray>white-8]
  inkcolor=css(np.median(ink,axis=0)) if len(ink) else '#222222'
  # OCR line boxes are ink bounds; compensate for loaded fonts' ascent without stretching text.
  weight=700 if height>hh*.038 and font not in ['Bebas Neue','Anton','Michroma'] else 400
  if font=='Roboto Condensed' and height<hh*.035:weight=400
  # Maintain native text start and line breaks. Boxes include enough vertical room for actual metrics.
  xx=x/ww*100;yy=max(0,y/hh*100-size/720*100*.19);width=min(100-xx,max((right-x)/ww*100+1.1,len(txt)*size*.40/1280*100))
  elements.append(elem('text',xx,yy,width,min(100-yy,size/720*100*1.55),text=txt,size=max(5,size),font=font,weight=weight,color=inkcolor,lineHeight=1.05,nowrap=True))
 return key,{'id':s['id'],'title':next((e['text'] for e in elements if e['kind']=='text' and e['size']>25),s['id']),'background':bg,'elements':elements},replacements
if __name__=='__main__':
 jobs=[(d['id'],s) for d in manifest for s in d['slides']]
 cache=ROOT/'review/group-b-page-data.json';repair=ROOT/'review/group-b-unreadable.json'
 results={};rep={}
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  for n,(key,data,replacements) in enumerate(pool.map(process,jobs),1):
   results[key]=data;rep[key]=replacements
   if n%10==0:print(n,len(jobs),key,flush=True)
 cache.write_text(json.dumps(results,ensure_ascii=False));repair.write_text(json.dumps(rep,ensure_ascii=False,indent=2))
 (ROOT/'src/decks/group-b-data.json').write_text(json.dumps(results,ensure_ascii=False))
 (ROOT/'src/decks/group-b.ts').write_text("import type { Deck, Slide } from '../model'\nimport {D} from '../primitives'\nimport pages from './group-b-data.json'\nconst data=pages as unknown as Record<string,Slide>\nexport default [\n"+',\n'.join("D("+json.dumps(d['id'])+','+json.dumps(d['title'])+",["+','.join("data["+json.dumps(d['id']+'/'+s['id'])+"]" for s in d['slides'])+"])" for d in manifest)+"\n] satisfies Deck[]\n")
