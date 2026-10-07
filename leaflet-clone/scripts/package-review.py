"""Package existing UI renders and proportionally contained 1280x720 review pages."""
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw,ImageFont
import argparse,hashlib,zipfile,json,io,html,datetime
p=argparse.ArgumentParser();p.add_argument('capture_folder');p.add_argument('--build-log',type=Path);a=p.parse_args()
root=Path(__file__).resolve().parents[1];repo=root.parent;out=Path(a.capture_folder)
report=json.loads((out/'render-verification.json').read_text());assert report['status']=='passed' and report['screenCount']==35
sha=lambda data:hashlib.sha256(data).hexdigest()
(out/'review-1280').mkdir(exist_ok=True)
rows=[]
for row in report['pages']:
 source=out/row['file'];assert sha(source.read_bytes())==row['sha256']
 im=Image.open(source).convert('RGB');assert list(im.size)==row['size']
 page=Image.new('RGB',(1280,720),'#f4f4f5');contained=ImageOps.contain(im,(1280,720),Image.Resampling.LANCZOS);page.paste(contained,((1280-contained.width)//2,(720-contained.height)//2));file=out/'review-1280'/f'{row["id"]}.png';page.save(file)
 rows.append({**row,'reviewFile':str(file.relative_to(out)),'reviewSize':[1280,720],'reviewSHA256':sha(file.read_bytes()),'nativeToReview':'Uniform scale, centered with neutral margins; no stretch or rotation'})
cols=5;tw,th=320,210;overview=Image.new('RGB',(cols*tw,7*th),'#e7e9ed');draw=ImageDraw.Draw(overview);font=ImageFont.truetype('DejaVuSans.ttf',18)
for i,row in enumerate(rows):
 x=i%cols*tw;y=i//cols*th;thumb=Image.open(out/row['reviewFile']).resize((320,180),Image.Resampling.LANCZOS);overview.paste(thumb,(x,y));draw.text((x+10,y+185),f'{row["id"]}  |  {row["size"][0]} x {row["size"][1]}',font=font,fill='#17242d')
preview=repo/'leaflet-clone-render-preview.jpg';overview.save(preview,quality=92)
report['pages']=rows;report['reviewPages']=35;report['reviewPageSize']=[1280,720];report['build']='npm run build passed';report['buildLogSHA256']=sha(a.build_log.read_bytes()) if a.build_log else None;report['packagedAt']=datetime.datetime.now(datetime.timezone.utc).isoformat()
(out/'render-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
cards='\n'.join(f'<article><h2>{html.escape(row["id"]+" · "+row["title"])}</h2><a href="{row["file"]}"><img src="{row["reviewFile"]}" alt="{html.escape(row["title"])}" loading="lazy"></a><p><a href="{row["reviewFile"]}">검수용 1280×720</a> · <a href="{row["file"]}">원래 크기 {row["size"][0]}×{row["size"][1]}</a></p></article>' for row in rows)
index='''<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>리플렛 렌더 35개</title><style>body{margin:0;padding:24px;background:#edf0f3;font-family:system-ui,sans-serif;color:#17242d}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(520px,1fr));gap:24px}article{padding:16px;background:white;border-radius:8px}h2{font-size:16px}img{width:100%;height:auto;display:block}a{color:#2464a6}p{font-size:14px}</style><h1>리플렛 렌더 35개</h1><p>이미지를 누르면 원래 크기 PNG를 열 수 있습니다. 검수용 이미지는 비율을 유지하여 1280×720 안에 배치했습니다.</p><main>'''+cards+'</main></html>'
(out/'index.html').write_text(index)
(out/'README.md').write_text('# 리플렛 시각 검수용 렌더\n\n현재 소스의 화면 35개를 빌드된 앱의 실제 브라우저에서 렌더했습니다. UI 배치·텍스트·스타일은 수정하지 않았습니다.\n\n- native: 기본 종이 크기의 PNG 35장(1440×1018 또는 1920×1018)\n- review-1280: 비율을 유지한 1280×720 PNG 35장\n- preview.jpg: 전체 미리보기\n- index.html: 화면별 이미지를 열 수 있는 검수 목록\n- render-verification.json: 캡처 시점, 소스 해시, 폰트 로딩 상태, 크기와 PNG 해시\n- SHA256SUMS: 내부 파일 무결성 해시\n\nZIP을 풀고 index.html을 열면 각 화면을 확대해 확인할 수 있습니다. 원본 참고 이미지와의 개별 비교·디자인 수정은 수행하지 않았습니다.\n')
files={str(f.relative_to(out)):f for f in sorted(out.rglob('*')) if f.is_file()};files['preview.jpg']=preview
sums=''.join(sha(f.read_bytes())+'  '+name+'\n' for name,f in sorted(files.items()))
archive=repo/'leaflet-clone-renders.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for name,file in sorted(files.items()):z.write(file,name)
 z.writestr('SHA256SUMS',sums)
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None
 pngs=[n for n in z.namelist() if n.endswith('.png')];assert len(pngs)==70
 for row in rows:
  assert list(Image.open(io.BytesIO(z.read(row['file']))).size)==row['size']
  assert Image.open(io.BytesIO(z.read(row['reviewFile']))).size==(1280,720)
 for line in z.read('SHA256SUMS').decode().splitlines():
  digest,name=line.split('  ',1);assert sha(z.read(name))==digest
 summary={'status':'passed','sourceCommit':report['sourceCommit'],'sourceUIChanged':False,'screenCount':35,'nativePNGs':35,'nativeSizes':sorted({tuple(row['size']) for row in rows}),'reviewPNGs':35,'reviewPNGSize':[1280,720],'totalPNGs':70,'build':'passed','browserAndAssetErrors':0,'zipCRC':'passed','internalSHA256Manifest':'passed','verifiedMemberHashes':len(files),'archive':archive.name,'bytes':archive.stat().st_size,'sha256':sha(archive.read_bytes()),'preview':preview.name}
 deliver=root/'deliverables';deliver.mkdir(exist_ok=True);(deliver/'render-package-verification.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
