from pathlib import Path
from PIL import Image,ImageChops,ImageStat
import json,hashlib,fitz,collections
P=Path(__file__).resolve().parents[1];A=P/'artifacts';errors=[];counts={'048':17,'049':8,'050':20,'051':20,'052':19,'053':21}
def check(ok,msg):
 if not ok:errors.append(msg)
for mode in ['direct','assembled']:
 for d,n in counts.items():
  files=sorted((A/mode/d).glob('*.png'));check(len(files)==n,f'{mode}/{d} PNG count')
  doc=fitz.open(A/mode/f'{d}.pdf');check(len(doc)==n,f'{mode}/{d} PDF count');check(all(tuple(p.rect)==(0,0,1280,720) for p in doc),f'{mode}/{d} native PDF dimensions')
 doc=fitz.open(A/f'{mode}-all-105.pdf');check(len(doc)==105,f'{mode} combined PDF count')
 check(len(list((A/'comparisons').glob('*/*.jpg')))==105,'comparison count')
pngs=list((P/'public/reference').glob('*/*.png'))+list(A.rglob('*.png'));dims=collections.Counter(Image.open(p).size for p in pngs);check(set(dims)=={(1280,720)},'every PNG native size')
quality=json.loads((A/'quality-audit.json').read_text());check(len(quality)==210,'quality pages');check(not any(q['issues'] for q in quality),'quality issues');check(all(q['size']==[1280,720] for q in quality),'quality DOM dimensions');check(all(q['assembledRoots']>0 for q in quality if q['mode']=='assembled'),'assembly uses contracts')
for filename,count in [('audit.json',170),('minimum-audit.json',204)]:
 data=json.loads((A/'library'/filename).read_text());check(len(data)==count,f'library {filename} count');check(not any(x['issues'] for x in data),f'library {filename} issues')
contract=json.loads((A/'contract-audit.json').read_text());check(contract['elements']==31 and not contract['errors'],'contract')
means=[]
for f in sorted((A/'direct').glob('*/*.png')):
 other=A/'assembled'/f.parent.name/f.name;diff=ImageChops.difference(Image.open(f).convert('RGB'),Image.open(other).convert('RGB'));means.append({'id':f.stem,'mean_absolute_channel_error':sum(ImageStat.Stat(diff).mean)/3,'exact':diff.getbbox() is None})
(A/'assembly-diff.json').write_text(json.dumps(means,indent=2));check(max(x['mean_absolute_channel_error'] for x in means)<2,'material assembly discrepancy')
# Record hashes of final source and actual final outputs for reviewability.
paths=list((P/'src').rglob('*'))+list((P/'strategy-blueprint').rglob('*'))+list((P/'public/fonts').glob('*'))+list(A.glob('direct/*/*.png'))+list(A.glob('assembled/*/*.png'))
manifest={str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(paths) if f.is_file()};(A/'render-manifest.json').write_text(json.dumps(manifest,indent=2))
report={'reference_slides':105,'rendered_direct':105,'rendered_assembled':105,'comparison_images':105,'png_files_total_including_reference':len(pngs),'png_dimensions':{'x'.join(map(str,k)):v for k,v in dims.items()},'browser_pages_checked':len(quality),'centered_labels_checked':sum(q['chips'] for q in quality),'collection_elements':31,'collection_element_fixtures':83,'foundation_fixtures':2,'library_full_checks':170,'library_minimum_checks':204,'maximum_assembly_channel_error':max(x['mean_absolute_channel_error'] for x in means),'errors':errors}
(A/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2));raise SystemExit(bool(errors))
