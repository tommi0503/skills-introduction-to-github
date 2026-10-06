"""Reference analysis only: editable flat regions and positioned OCR text.
Photos and graphic art are removed by the manually reviewed SidePatch regions.
The source raster is never used by the implementation renderer.
"""
import csv,io,json,os,pathlib,subprocess,tempfile,concurrent.futures
import numpy as np
from scipy import ndimage
from PIL import Image

root=pathlib.Path(__file__).resolve().parents[1]
analysis=pathlib.Path('/workspace/leaflet-ocr');analysis.mkdir(exist_ok=True)
manifest=json.loads((root/'public/reference/manifest.json').read_text())
tessdata='/workspace/canva-ocr/tessdata'

def rgb(values):return '#'+''.join(f'{int(v):02x}' for v in values)
def fallback(title):
    if any(w in title for w in ['금융','은행','자산']):return '고객의 목표에 맞춘 전문 상담을 제공합니다.'
    if any(w in title for w in ['콘서트','공연','뮤지컬','연주']):return '공연 일정과 프로그램을 확인해 주세요.'
    if any(w in title for w in ['축제','행사']):return '함께 즐기는 다채로운 프로그램을 준비했습니다.'
    if any(w in title for w in ['병원','의료','치과','건강']):return '상담과 예약은 안내된 연락처로 문의해 주세요.'
    if any(w in title for w in ['카페','와인','한우','다과']):return '정성껏 준비한 상품으로 특별한 마음을 전합니다.'
    return '자세한 프로그램과 이용 안내를 확인해 주세요.'

def process(item):
    deck,side=item;key=deck['id']+'-'+side['id'];output=root/'src/data/baseline'/f'{key}.json'
    if output.exists() and os.environ.get('LEAFLET_REOCR')!='1':return key+' cached'
    path=root/'public'/side['reference'].lstrip('/');image=Image.open(path).convert('RGB');a=np.asarray(image);height,width=a.shape[:2]
    with tempfile.TemporaryDirectory(prefix='leaflet-ocr-',dir='/tmp') as temp:
        lines={}
        for panel in range(3):
            left=round(width*panel/3);right=round(width*(panel+1)/3)
            part=image.crop((left,0,right,height));input_path=pathlib.Path(temp)/f'panel-{panel}.png'
            part.resize((part.width*2,height*2),Image.Resampling.LANCZOS).save(input_path)
            result=subprocess.run(['tesseract',str(input_path),'stdout','--tessdata-dir',tessdata,'-l','kor+eng','--psm','3','tsv'],env=dict(os.environ,OMP_THREAD_LIMIT='1'),capture_output=True,text=True,check=True)
            (analysis/f'{key}-p{panel+1}.tsv').write_text(result.stdout)
            for word in csv.DictReader(io.StringIO(result.stdout),delimiter='\t',quoting=csv.QUOTE_NONE):
                if word['level']!='5' or not word['text'].strip():continue
                word['left']=str(int(word['left'])+left*2)
                k=(panel,word['block_num'],word['par_num'],word['line_num']);lines.setdefault(k,[]).append(word)
    texts=[];flat=a.copy()
    for index,words in enumerate(lines.values()):
        x=min(int(w['left']) for w in words)//2;y=min(int(w['top']) for w in words)//2
        right=max(int(w['left'])+int(w['width']) for w in words)/2;bottom=max(int(w['top'])+int(w['height']) for w in words)/2
        w=right-x;h=bottom-y;content=' '.join(v['text'] for v in words).strip();conf=sum(float(v['conf']) for v in words)/len(words)
        if h<4 or w<4 or h>105 or w>width*.65 or len(content)>250:continue
        crop=a[max(0,y):min(height,int(bottom)+1),max(0,x):min(width,int(right)+1)]
        edge=np.concatenate([crop[0],crop[-1],crop[:,0],crop[:,-1]],axis=0);bg=np.median(edge,axis=0)
        distances=np.linalg.norm(crop.astype(float)-bg,axis=2);ink=crop[distances>max(32,np.percentile(distances,62))]
        if len(ink)<3:continue
        color=np.median(ink,axis=0)
        invalid=conf<27 or sum(c.isalnum() or '\uac00'<=c<='\ud7a3' for c in content)<max(1,len(content)*.35)
        if invalid:
            capacity=int(w/max(1,h)/.85)
            content=fallback(deck['title']) if capacity>24 else '자세한 안내를 확인해 주세요.' if capacity>14 else '담당자에게 문의해 주세요.' if capacity>10 else '자세히 보기' if capacity>5 else '안내'
        # Confident Korean recognition uses spatial word gaps, not inserted syllable spaces.
        if not invalid:
            joined=words[0]['text']
            for previous,current in zip(words,words[1:]):
                gap=(int(current['left'])-int(previous['left'])-int(previous['width']))/2
                join=any('\uac00'<=c<='\ud7a3' for c in previous['text']+current['text']) and gap<max(2.8,h*.16)
                joined+=('' if join else ' ')+current['text']
            content=joined
        texts.append({'id':f't{index:04}','kind':'text','x':x,'y':y,'w':round(w,1),'h':round(h,1),'text':content,'font':'Pretendard','weight':700 if h>=22 else 400,'color':rgb(color),'inkFit':True,'confidence':round(conf,1),'replacement':invalid})
        flat[max(0,y-2):min(height,int(bottom)+3),max(0,x-2):min(width,int(right)+3)]=bg.astype(np.uint8)
    # Large uniform regions become editable boxes. No raster tracing of artwork.
    q=(flat.astype(np.int32)//12);codes=q[:,:,0]*484+q[:,:,1]*22+q[:,:,2];values,counts=np.unique(codes,return_counts=True)
    order=np.argsort(counts)[::-1][:20];shapes=[]
    for idx in order:
        if counts[idx]<800:continue
        mask=codes==values[idx]
        mask=ndimage.binary_closing(mask,iterations=2)
        labels,count=ndimage.label(mask);objects=ndimage.find_objects(labels)
        for label,region in enumerate(objects,1):
            if region is None:continue
            yy,xx=region;x=xx.start;y=yy.start;w=xx.stop-x;h=yy.stop-y
            if w<18 or h<5 or w*h<650:continue
            local=labels[region]==label;area=local.sum();purity=area/(w*h)
            # Fill holes made by text while preserving the rectangle's outer contour.
            filled=ndimage.binary_fill_holes(local);coverage=filled.sum()/(w*h)
            if coverage<.78:continue
            pixels=flat[region][local];color=np.median(pixels,axis=0)
            if np.std(pixels,axis=0).max()>10:continue
            if w>width*.9 and h>height*.9:continue
            radius=0
            if not filled[1:min(5,h),1:min(5,w)].any():radius=min(w,h)*(.5 if .77<coverage<.83 and abs(w-h)<w*.1 else .08)
            shapes.append({'kind':'box','x':x,'y':y,'w':w,'h':h,'fill':rgb(color),'radius':round(radius,1)})
    shapes.sort(key=lambda e:-e['w']*e['h'])
    output.write_text(json.dumps({'id':key,'elements':shapes+texts,'replacementCount':sum(t['replacement'] for t in texts)},ensure_ascii=False,indent=2))
    return f'{key}: {len(shapes)} flat regions, {len(texts)} text lines'

if __name__=='__main__':
    tasks=[(d,s) for d in manifest for s in d['sides']]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for message in pool.map(process,tasks):print(message,flush=True)
