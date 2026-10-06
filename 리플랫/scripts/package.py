import hashlib,json,pathlib,zipfile
from PIL import Image,ImageDraw
root=pathlib.Path(__file__).resolve().parents[1]
out=pathlib.Path('/workspace/shared/downloads');out.mkdir(parents=True,exist_ok=True)
metas=[json.loads(p.read_text()) for p in sorted((root/'comparisons/final').glob('l??.json'))]
assert len(metas)==72 and sum(len(d['panels']) for d in metas)==432
verification=json.loads((root/'review/verification.json').read_text());assert verification['status']=='passed'
source={d['id']:d for d in json.loads((root/'public/reference/manifest.json').read_text())}
manifest=[]
preview=Image.new('RGB',(1600,18*300),'#eef0f3');draw=ImageDraw.Draw(preview)
for i,d in enumerate(metas):
    front=Image.open(d['sides'][0]['file']).convert('RGB');thumb=front.resize((390,219),Image.Resampling.LANCZOS);x=i%4*400;y=i//4*300;preview.paste(thumb,(x,y+34));draw.text((x+8,y+10),d['id']+' | 6 panels',fill='#222')
    for p in d['panels']:
        with Image.open(p['file']) as image:assert image.size==(1280,720);image.verify()
        manifest.append({'brochure':d['id'],'title':d['title'],'page':p['id'],'side':p['id'].split('-')[0],'size':[1280,720],'nativePanelSize':p['size'],'sourceCrop':p['crop'],'sha256':hashlib.sha256(pathlib.Path(p['file']).read_bytes()).hexdigest(),'definitionHash':d['definitionHash'],'rendererHash':d['rendererHash']})
preview.save(out/'leaflet-preview.jpg',quality=94)
# Four smaller preview sheets are easier to inspect than one long contact sheet.
for batch,(top,bottom) in enumerate([(0,1500),(1500,3000),(3000,4200),(4200,5400)]):preview.crop((0,top,1600,bottom)).save(out/f'leaflet-preview-{batch+1}.jpg',quality=94)
archive=out/'leaflet-renders.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for d in metas:
        for p in d['panels']:
            z.write(p['file'],f'pages/{d["id"]}/{p["id"]}.png')
        for s in d['sides']:
            with Image.open(s['file']) as image:assert image.size==(1280,720)
            z.write(s['file'],f'unfolded/{d["id"]}/{s["id"]}.png')
    for p in (root/'review').iterdir():
        if p.is_file():z.write(p,'review/'+p.name)
    for p in out.glob('leaflet-preview*.jpg'):z.write(p,p.name)
    for p in out.glob('leaflet-before-after-*.jpg'):z.write(p,p.name)
    z.writestr('manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2))
    z.writestr('README.txt','''리플랫 — 3단 브로셔 72종, 접지면 432페이지

pages/: 앞면 s01-p1/p2/p3, 뒷면 s02-p1/p2/p3. 원본의 왼쪽→가운데→오른쪽 순서입니다.
unfolded/: 앞·뒷면을 각각 펼쳐 확인할 수 있는 144장입니다.
모든 PNG는 동일한 1280×720입니다. 세로형 접지면은 비율을 유지해 중앙에 배치했습니다.
원본·구현 대조 모음은 별도 leaflet-review.zip에 담았습니다. 소스의 원본 비교 화면에서도 확인할 수 있습니다.
review/: 수정 사항, 폰트·문구 대체 내역, 최종 검증입니다.
사진·복잡한 일러스트·그래픽 배경은 요청한 단색 회색 placeholder입니다.
판독할 수 없는 작은 문구는 자연스러운 안내문으로 작성했습니다. 줄 모양으로 대체하지 않았습니다.
원본 스크린샷을 구현 화면에 삽입하지 않았습니다. 원본 폰트 정보가 없어 실제 로드한 가장 가까운 폰트를 사용했습니다.
''')
with zipfile.ZipFile(archive) as z:assert z.testzip() is None
with zipfile.ZipFile(out/'leaflet-review.zip','w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for d in metas:z.write(root/'comparisons/final'/f'{d["id"]}-contact.jpg',f'brochures/{d["id"]}.jpg')
    for p in out.glob('leaflet-before-after-*.jpg'):z.write(p,p.name)
    for p in (root/'review').iterdir():
        if p.is_file():z.write(p,'review/'+p.name)
with zipfile.ZipFile(out/'leaflet-review.zip') as z:assert z.testzip() is None
print(json.dumps({'archive':str(archive),'bytes':archive.stat().st_size,'pages':432,'unfoldedSheets':144,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest()},indent=2))
