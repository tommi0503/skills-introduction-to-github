"""Package every independent slide plus source, excluding dependency caches."""
import hashlib, html, json, pathlib, zipfile
from PIL import Image, ImageDraw
root = pathlib.Path(__file__).resolve().parents[1]
out = root.parent
verification = json.loads((root/'review/verification.json').read_text())
visual = json.loads((root/'review/visual-review.json').read_text())
source = json.loads((root/'public/reference/manifest.json').read_text())
assert verification['status']=='passed' and verification['slides']==1057 and verification['decks']==47
assert visual['allIndividuallyViewed'] and len(visual['slides'])==1057
decks = [json.loads((root/'comparisons/final'/f'{d["id"]}.json').read_text()) for d in source]
slides = [(d,s) for d in decks for s in d['slides']]
assert len(slides)==1057
overview = Image.new('RGB',(1600,((len(slides)+7)//8)*130),'#edf0f4')
draw = ImageDraw.Draw(overview)
preview_dir = root/'review/preview-pages';preview_dir.mkdir(exist_ok=True)
pages,manifest = {},[]
for i,(deck,slide) in enumerate(slides):
    file=root/'renders/final'/f'{deck["id"]}-{slide["id"]}.png'
    sha=hashlib.sha256(file.read_bytes()).hexdigest();assert sha==slide['pngSha256']
    with Image.open(file) as im:assert im.size==(1280,720);im.verify()
    im=Image.open(file).convert('RGB')
    x,y=(i%8)*200,(i//8)*130
    overview.paste(im.resize((195,110),Image.Resampling.LANCZOS),(x,y+18))
    draw.text((x+3,y+3),f'{deck["id"]}/{slide["id"]}',fill='#222')
    page=i//20
    if page not in pages:
        count=min(20,len(slides)-page*20)
        pages[page]=Image.new('RGB',(1600,((count+3)//4)*260),'#edf0f4')
    local=i%20;px,py=(local%4)*400,(local//4)*260
    pages[page].paste(im.resize((390,219),Image.Resampling.LANCZOS),(px,py+30))
    ImageDraw.Draw(pages[page]).text((px+4,py+8),f'{deck["id"]}/{slide["id"]}',fill='#222')
    original=next(s for d in source if d['id']==deck['id'] for s in d['slides'] if s['id']==slide['id'])
    manifest.append({'deck':deck['id'],'slide':slide['id'],'title':slide['title'],
        'renderSize':[1280,720],'nativeReferenceSize':original['nativeSize'],
        'sheet':original['originalPath'],'sheetSize':original['sheetSize'],'crop':original['crop'],
        'visibleCrop':original.get('visibleCrop'),'incompleteReference':original.get('incomplete',False),
        'pngSha256':sha,'definitionSha256':deck['definitionHash'],'rendererSha256':deck['rendererHash']})
overview_path=out/'presentation5-clone-preview.jpg';overview.save(overview_path,quality=94)
for page,im in pages.items():im.save(preview_dir/f'{page+1:02d}.jpg',quality=94)
(root/'review/delivery-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
cards=''.join(f'<article><h2>{html.escape(s["deck"]+"/"+s["slide"]+" · "+s["title"])}</h2>'
    f'<a href="renders/final/{s["deck"]}-{s["slide"]}.png"><img loading="lazy" width="1280" height="720" '
    f'src="renders/final/{s["deck"]}-{s["slide"]}.png" alt="{html.escape(s["title"],quote=True)}"></a>'
    f'<a href="comparisons/final/{s["deck"]}-{s["slide"]}.jpg">원본 / 결과 비교</a></article>' for s in manifest)
preview_html=('<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width">'
    '<title>Presentation 5 · 1057페이지</title><style>body{margin:0;padding:28px;background:#edf0f4;font-family:Arial,sans-serif}'
    'main{display:grid;grid-template-columns:repeat(auto-fit,minmax(440px,1fr));gap:24px}'
    'article{background:white;padding:16px;border:1px solid #ddd;border-radius:12px}h2{font-size:14px}'
    'img{display:block;width:100%;height:auto}a{color:#205be8}p{line-height:1.6}</style>'
    '<h1>Presentation 5 · 1057페이지</h1><p>117개 참고 시트 · 47개 덱 · 각 페이지는 1280×720입니다. '
    '이미지를 누르면 전체 크기로 열립니다.</p><main>'+cards+'</main></html>')
(root/'preview.html').write_text(preview_html)
# Independent ZIPs fit GitHub's single-file limit and extract into one directory.
excluded={'node_modules','dist','__pycache__','.git'}
files=[]
for p in sorted(root.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(root)
    if excluded.intersection(rel.parts) or 'round1' in rel.parts or 'round2' in rel.parts:continue
    if p.suffix=='.log' or p.name=='archive-integrity.json' or p.name.endswith('-seed.json'):continue
    files.append((p,'presentation5-clone/'+str(rel)))
files.append((overview_path,overview_path.name))
assert len([p for p,n in files if '/renders/final/' in n and p.suffix=='.png'])==1057
limit=94*1024*1024;reserve=1024*1024
archives,current,names=[],None,[]
note=('Presentation 5 Clone — 47개 덱·1057개 독립 페이지\n\n'
    '모든 part ZIP을 같은 폴더에 압축 해제하세요. 각 ZIP은 독립적으로 열립니다.\n'
    'presentation5-clone/preview.html은 설치 없이 확인하는 전체 미리보기입니다.\n'
    '소스 실행은 README.md 참고. node_modules, dist, 중간 검수 파일은 제외했습니다.\n'
    'renders/final/: PNG1057장, 모두1280×720\ncomparisons/final/: 개별 원본/결과 비교\n'
    'review/: 분할 좌표·판독 불가 문구·복원 가정·개별 시각 검수·자동 검사 결과\n'
    'public/sheets/: 변형하지 않은117개 원본 시트\npublic/reference/: 자연 크기 개별 슬라이드 crop\n')
def finish():
    global current,names
    if current is None:return
    archive=pathlib.Path(current.filename);current.close()
    assert archive.stat().st_size<limit
    with zipfile.ZipFile(archive) as z:assert z.testzip() is None
    archives.append({'file':archive.name,'bytes':archive.stat().st_size,
        'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'payloadFiles':len(names),'zipCrcPassed':True})
    current,names=None,[]
for p,name in files:
    if current is not None and current.fp.tell()+p.stat().st_size+reserve>limit:finish()
    if current is None:
        archive=out/f'presentation5-clone-part-{len(archives)+1:02d}.zip'
        current=zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6)
        current.writestr('DELIVERY.txt',note)
    current.write(p,name);names.append(name)
finish()
assert sum(a['payloadFiles'] for a in archives)==len(files)
expected={f'presentation5-clone/renders/final/{s["deck"]}-{s["slide"]}.png':s['pngSha256'] for s in manifest}
checked=set()
for archive in archives:
    with zipfile.ZipFile(out/archive['file']) as z:
        for name in z.namelist():
            if name not in expected:continue
            data=z.read(name)
            assert hashlib.sha256(data).hexdigest()==expected[name]
            assert int.from_bytes(data[16:20],'big')==1280 and int.from_bytes(data[20:24],'big')==720
            assert name not in checked
            checked.add(name)
assert len(checked)==1057
report={'archives':archives,'decks':47,'sourceSheets':117,'pngCount':1057,'allPngSize':[1280,720],
    'zipCrcPassed':True,'allRenderHeadersAndHashesVerified':True,'extractAllPartsToSameDirectory':True}
(root/'review/archive-integrity.json').write_text(json.dumps(report,indent=2)+'\n')
(out/'presentation5-clone-downloads.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
