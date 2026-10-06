"""Package the exact final, browser-verified outputs (never intermediate captures)."""
import json,pathlib,zipfile,hashlib,html,shutil
from PIL import Image,ImageDraw
root=pathlib.Path(__file__).resolve().parents[1]
out=root.parent
verification=json.loads((root/'review/verification.json').read_text());assert verification['status']=='passed'
source=json.loads((root/'public/reference/manifest.json').read_text())
decks=[json.loads((root/'comparisons/final'/f'{d["id"]}.json').read_text()) for d in source]
assert len(decks)==43 and sum(len(d['slides']) for d in decks)==77
all_slides=[(d,s) for d in decks for s in d['slides']]
preview=Image.new('RGB',(1600,((len(all_slides)+3)//4)*260),'#edf0f4');draw=ImageDraw.Draw(preview)
manifest=[]
for i,(deck,slide) in enumerate(all_slides):
 p=root/'renders/final'/f'{deck["id"]}-{slide["id"]}.png'
 with Image.open(p) as im:
  assert im.size==(1280,720);im.verify()
 sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha==slide['pngSha256']
 im=Image.open(p).convert('RGB').resize((390,219),Image.Resampling.LANCZOS)
 x=i%4*400;y=i//4*260;preview.paste(im,(x,y+30));draw.text((x+4,y+8),f'{deck["id"]}/{slide["id"]}',fill='#212121')
 src=next(d for d in source if d['id']==deck['id']);original=next(s for s in src['slides'] if s['id']==slide['id'])
 manifest.append({'deck':deck['id'],'deckTitle':deck['title'],'originalDeck':src['originalDeck'],'slide':slide['id'],'title':slide['title'],'size':[1280,720],'sourceSize':[1600,900],'originalPath':original['originalPath'],'pngSha256':sha,'definitionSha256':deck['definitionHash'],'rendererSha256':deck['rendererHash']})
preview_path=out/'presentation4-clone-preview.jpg';preview.save(preview_path,quality=95)
# Compact independent full-deck preview pages for comfortable inspection.
preview_dir=root/'review/preview-pages';preview_dir.mkdir(exist_ok=True)
for page,start in enumerate(range(0,len(all_slides),20),1):
 end=min(start+20,len(all_slides));region=preview.crop((0,(start//4)*260,1600,((end+3)//4)*260));region.save(preview_dir/f'{page:02d}.jpg',quality=95)
cards=''.join(f'<article><h2>{html.escape(s["deck"]+"/"+s["slide"]+" · "+s["title"])}</h2><a href="slides/{s["deck"]}/{s["slide"]}.png"><img loading="lazy" width="1280" height="720" src="slides/{s["deck"]}/{s["slide"]}.png" alt="{html.escape(s["title"],quote=True)}"></a><a href="comparisons/{s["deck"]}/{s["slide"]}.jpg">원본 / 결과 비교</a></article>' for s in manifest)
preview_html='<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Presentation 4 · 77장 미리보기</title><style>body{margin:0;padding:32px;background:#edf0f4;font-family:Arial,sans-serif}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(440px,1fr));gap:24px}article{background:white;padding:16px;border:1px solid #ddd;border-radius:12px}h2{font-size:14px}img{display:block;width:100%;height:auto}a{color:#205be8}p{line-height:1.6}</style><h1>Presentation 4 · 77장</h1><p>43개 덱 · 모든 PNG 1280×720 · 이미지를 누르면 전체 크기로 열립니다.</p><main>'+cards+'</main></html>'
archive=out/'presentation4-clone-renders.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for deck,slide in all_slides:
  z.write(root/'renders/final'/f'{deck["id"]}-{slide["id"]}.png',f'slides/{deck["id"]}/{slide["id"]}.png')
  z.write(root/'comparisons/final'/f'{deck["id"]}-{slide["id"]}.jpg',f'comparisons/{deck["id"]}/{slide["id"]}.jpg')
 for d in decks:z.write(root/'renders/final'/f'{d["id"]}-contact.jpg',f'decks/{d["id"]}.jpg')
 for p in sorted((root/'review').rglob('*')):
  if p.is_file() and p.name!='archive-integrity.json':z.write(p,'review/'+str(p.relative_to(root/'review')))
 z.write(preview_path,'preview.jpg');z.writestr('preview.html',preview_html)
 z.write(root/'NEXT_SESSION_PROMPT.md','NEXT_SESSION_PROMPT.md')
 z.writestr('manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2))
 z.writestr('README.txt','Presentation 4 Clone: 43개 덱 · 77장 전체\n\nslides/: 1280×720 PNG 77개\ncomparisons/: 각 원본/구현을 나란히 놓은 비교 JPG 77개\ndecks/: 덱별 모음 43개\npreview.jpg: 77장 전체 미리보기\npreview.html: 로컬 브라우저에서 여는 전체 이미지 미리보기\nreview/: 개별 비교·수정·최종 검수 기록 및 자동 검사 결과\nmanifest.json: 원본 대응 목록과 SHA-256\n\n사진·복잡한 일러스트·복합 이미지 아이콘·기기 화면·그래픽 배경은 연한 회색 단색 placeholder입니다. 표·차트·도형·텍스트는 컴포넌트와 데이터로 재구현했습니다. 원본 편집 폰트 메타데이터가 없어서 비슷한 실제 폰트 파일을 사용한 곳과 판독 한계를 검수 기록에 남겼습니다. 원본 이미지를 UI 배경으로 쓰지 않았습니다.\n')
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None
 png=[n for n in z.namelist() if n.endswith('.png')];assert len(png)==77
 for n in png:
  import io
  with Image.open(io.BytesIO(z.read(n))) as im:assert im.size==(1280,720);im.verify()
report={'archive':archive.name,'bytes':archive.stat().st_size,'decks':43,'pngCount':77,'comparisons':77,'allPngSize':[1280,720],'zipCrcPassed':True,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest()}
(root/'review/archive-integrity.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
