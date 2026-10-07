"""Assemble the verified renders; every PNG in the delivery ZIP is 1280×720."""
import json,hashlib,zipfile,io
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
root=Path(__file__).resolve().parents[1];repo=root.parent
verification=json.loads((root/'review/verification.json').read_text());assert verification['status']=='passed'
review=json.loads((root/'review/primary-review.json').read_text());reviewed={x['key']:x for x in review['pages']};assert len(reviewed)==202
pages=[];metas=[]
for file in sorted((root/'comparisons/final').glob('l*.json')):
    m=json.loads(file.read_text());metas.append(file)
    for p in m['panels']+m['sides']:
        key=f'{m["id"]}-{p["id"]}';assert key in reviewed
        assert reviewed[key]['pngSha256']==p['pngSha256']
        assert reviewed[key]['definitionHash']==m['definitionHash'] and reviewed[key]['rendererHash']==m['rendererHash']
        assert hashlib.sha256((root/f'comparisons/final/{key}.jpg').read_bytes()).hexdigest()==reviewed[key]['comparisonSha256']
        png=root/p['file'];assert Image.open(png).size==(1280,720)
        assert hashlib.sha256(png.read_bytes()).hexdigest()==p['pngSha256'];pages.append((key,png))
assert len(pages)==202

def preview(items,out):
    cols=5;tw,th=320,208;im=Image.new('RGB',(tw*cols,th*((len(items)+cols-1)//cols)),'#e7e9ed');d=ImageDraw.Draw(im)
    for i,(key,png) in enumerate(items):
        x=(i%cols)*tw;y=(i//cols)*th;image=ImageOps.contain(Image.open(png).convert('RGB'),(320,180));im.paste(image,(x,y));d.text((x+8,y+187),key,fill='#17242d')
    im.save(out,quality=90);return out
full=preview(pages,repo/'canva-leaflets-clone-preview.jpg')
unfolded=preview([(k,p) for k,p in pages if '-p' not in k],root/'review/unfolded-preview.jpg')
files={f'renders/{k}.png':p for k,p in pages}
files.update({f'comparisons/{k}.jpg':root/f'comparisons/final/{k}.jpg' for k,p in pages})
files.update({f'capture-metadata/{p.name}':p for p in metas})
files['preview/all-202-pages.jpg']=full;files['preview/unfolded-52-sides.jpg']=unfolded
for d in ['review','provenance']:
    for p in (root/d).glob('*'):
        if p.is_file() and p.suffix in ['.json','.md','.txt','.csv']:files[f'{d}/{p.name}']=p
files['README.md']=root/'README.md'
files['reference-manifest.json']=root/'public/reference/manifest.json'
sums=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+name+'\n' for name,p in sorted(files.items()))
archive=repo/'canva-leaflets-clone-renders.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for name,p in sorted(files.items()):z.write(p,name)
    z.writestr('SHA256SUMS',sums)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    pngs=[n for n in z.namelist() if n.endswith('.png')];comparisons=[n for n in z.namelist() if n.startswith('comparisons/')]
    assert len(pngs)==202 and len(comparisons)==202
    assert all(Image.open(io.BytesIO(z.read(n))).size==(1280,720) for n in pngs)
report={'status':'passed','zipFile':archive.name,'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'entryCount':len(files)+1,'renderPNGs':202,'comparisonImages':202,'allPNGSize':[1280,720],'zipCRC':'passed','internalSHA256Manifest':'included','primaryIndividualReviews':202,'previewFile':full.name}
(root/'review/package-verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
