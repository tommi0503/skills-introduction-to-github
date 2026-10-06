import json,pathlib,zipfile,hashlib
from PIL import Image,ImageDraw,ImageOps
root=pathlib.Path(__file__).resolve().parents[1]
out=pathlib.Path('/workspace/shared/downloads');out.mkdir(parents=True,exist_ok=True)
decks=[json.loads(p.read_text()) for p in sorted((root/'comparisons/final').glob('p??.json'))]
assert len(decks)==36
assert sum(len(d['slides']) for d in decks)==36
verification=json.loads((root/'review/verification.json').read_text());assert verification['status']=='passed'
preview=Image.new('RGB',(1600,((len(decks)+3)//4)*270),'#e9ecf0');draw=ImageDraw.Draw(preview)
source_manifest={d['id']:d for d in json.loads((root/'public/reference/manifest.json').read_text())}
manifest=[]
for i,d in enumerate(decks):
 for s in d['slides']:
  p=pathlib.Path(s['file'])
  with Image.open(p) as im:assert im.size==(1280,720);im.verify()
  manifest.append({'template':d['id'],'templateTitle':d['title'],'slide':s['id'],'title':s['title'],'size':[1280,720],'sourceSize':source_manifest[d['id']]['sourceSize'],'sourcePlacement':source_manifest[d['id']]['sourcePlacement'],'sourceFile':source_manifest[d['id']]['sourceFile'],'pngSha256':hashlib.sha256(p.read_bytes()).hexdigest(),'definitionSha256':d['definitionHash'],'rendererSha256':d['rendererHash']})
 im=Image.open(d['slides'][0]['file']).convert('RGB').resize((390,219),Image.Resampling.LANCZOS);x=i%4*400;y=i//4*270
 preview.paste(im,(x,y+35));draw.text((x+6,y+10),f'{d["id"]} | {len(d["slides"])} slides',fill='#222')
preview.save(out/'presentation3-clone-preview.jpg',quality=95)
archive=out/'presentation3-clone-renders.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for d in decks:
  for s in d['slides']:
   z.write(s['file'],f'slides/{d["id"]}/{s["id"]}.png')
   z.write(root/'comparisons/final'/f'{d["id"]}-{s["id"]}.jpg',f'comparisons/{d["id"]}/{s["id"]}.jpg')
  z.write(root/'renders/final'/f'{d["id"]}-contact.jpg',f'templates/{d["id"]}.jpg')
 for p in sorted((root/'review').glob('*')):
  if p.is_file():z.write(p,'review/'+p.name)
 z.write(out/'presentation3-clone-preview.jpg','preview.jpg')
 z.write(root/'NEXT_SESSION_PROMPT.md','NEXT_SESSION_PROMPT.md')
 z.writestr('manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2))
 z.writestr('README.txt','''Presentation 3 Clone — 36개 화면

slides/: 동일한1280×720크기의 개별 PNG36개
templates/: 템플릿별 전체 슬라이드 모음36개
comparisons/: 원본과 구현을 나란히 대조한 이미지36개
review/: 템플릿별 비교·수정 기록 및 최종 검증
preview.jpg: 전체 템플릿 표지 모음
manifest.json: 슬라이드 이름, 크기와 렌더·소스 해시

다른 비율의 원본은 비율을 보존해 동일한 캔버스에 배치했습니다.\n기존 요청에 따라 사진·기기 화면·복잡한 일러스트와 그래픽 배경은 연한 회색 단색 플레이스홀더입니다.
일반 도형·표·차트와 텍스트는 재사용 UI로 구현했습니다. 원본 스크린샷을 배경으로 사용하지 않았습니다.
칩은 공통 컴포넌트가 실제 글자 경계로 가운데 정렬합니다.
원본 편집 파일과 폰트 정보가 제공되지 않아 가장 가까운 설치 폰트를 사용했습니다.
남은 차이와 검수 결과는 review/에서 확인할 수 있습니다.
''')
with zipfile.ZipFile(archive) as z:assert z.testzip() is None
print(json.dumps({'archive':str(archive),'bytes':archive.stat().st_size,'slides':36,'screens':36,'comparisons':36,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest()},indent=2))
