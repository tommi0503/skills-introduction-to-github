import json,pathlib,zipfile
from PIL import Image,ImageOps,ImageDraw
root=pathlib.Path(__file__).resolve().parents[1]
out=pathlib.Path('/workspace/shared/downloads');out.mkdir(parents=True,exist_ok=True)
decks=[json.loads(p.read_text()) for p in sorted((root/'comparisons/final').glob('r??.json'))]
assert len(decks)==32,f'Expected32 decks, got{len(decks)}'
assert all(d['round']=='final' for d in decks)
slides=[(d,s) for d in decks for s in d['slides']]
assert len(slides)==113,f'Expected113 visible panels, got{len(slides)}'
sheet=Image.new('RGB',(1600,2400),'#eaecf0');draw=ImageDraw.Draw(sheet)
for n,deck in enumerate(decks):
 with Image.open(deck['boardFile']) as im:
  assert im.size==(deck['referenceSize']['width']*2,deck['referenceSize']['height']*2)
  thumb=ImageOps.contain(im,(388,265));x=n%4*400;y=n//4*300
  sheet.paste(thumb,(x,y+30));draw.text((x+8,y+7),f'{deck["id"]} | {len(deck["slides"])} slides',fill='#232630')
sheet.save(out/'slide-gen-clone-preview.jpg',quality=95)
originals=json.loads((root/'public/reference/manifest.json').read_text());original_by_id={d['id']:d['original'] for d in originals}
manifest=[]
for deck,slide in slides:
 filepath=pathlib.Path(slide['file'])
 with Image.open(filepath) as im:
  assert im.size==(1280,720),(filepath,im.size)
  im.verify()
 region=deck['referenceRegions'][deck['slides'].index(slide)]
 manifest.append({'deck':deck['id'],'deck_title':deck['title'],'slide':slide['id'],'title':slide['title'],'original_file':original_by_id[deck['id']],'size':[1280,720],'full_source_rectangle_percent':region,'source_data_sha256':deck['definitionHash'],'renderer_sha256':deck['rendererHash']})
readme='''Slide Gen Clone — 재검수 수정본

32개 참고 이미지 / 113개 개별 화면

slides/ : 1280 × 720 PNG, 모두 동일한 크기.
decks/ : 원본 콜라주의 위치·간격·잘림을 유지한 모음 PNG. 원본의 2배 해상도.
review/boards/ : 원본과 수정된 모음을 나란히 비교한 이미지32개.
review/slides/ : 원본 슬라이드 영역과 수정 화면을 나란히 비교한 이미지113개.
review/ : 구체적인 재검수 기록과 자동 검증 결과.
preview.jpg : 전체 수정본 모음.
manifest.json : 원본 파일·슬라이드 이름·측정한 프레임·렌더 해시.

주요 수정: 잘린 패널을 늘리던 오류 수정, 누락된 금융 패널 추가, 원본 콜라주 배치 복원,
텍스트 크기·줄바꿈·색상·간격을 원본 좌표로 재작성, 단순 차트·표·연결선 복원.

사진·기기 화면·복잡한 그래픽은 요청대로 연한 회색 단색 플레이스홀더입니다.
비교 이미지에서 원본 파일 밖에 해당하는 회색 영역은 자료가 없는 부분입니다.
해당 영역에 새 내용을 꾸며 넣지 않고 단색 배경으로 유지합니다.
원본이3–4픽셀 글자로 압축된 본문 일부와 잘린 영역은 정확히 복구할 수 없습니다.
덱별 남은 차이는 review/re-review-*.md에 구체적으로 기록했습니다.
'''
zip_path=out/'slide-gen-clone-renders.zip'
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for deck,slide in slides:
  z.write(slide['file'],f'slides/{deck["id"]}/{slide["id"]}.png')
  z.write(root/'comparisons/final'/f'{deck["id"]}-{slide["id"]}.jpg',f'review/slides/{deck["id"]}-{slide["id"]}.jpg')
 for deck in decks:
  z.write(deck['boardFile'],f'decks/{deck["id"]}.png')
  z.write(root/'comparisons/final'/f'{deck["id"]}-board.jpg',f'review/boards/{deck["id"]}.jpg')
 for name in ['re-review-a.md','re-review-b.md','re-review-c.md','final-review.md','verification.json']:
  z.write(root/name,f'review/{name}')
 z.write(out/'slide-gen-clone-preview.jpg','preview.jpg')
 z.writestr('manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2));z.writestr('README.txt',readme)
with zipfile.ZipFile(zip_path) as z:
 assert z.testzip() is None
print(json.dumps({'archive':str(zip_path),'bytes':zip_path.stat().st_size,'decks':len(decks),'slides':len(slides),'png_files':len(slides)+len(decks),'comparison_files':len(slides)+len(decks)},indent=2))
