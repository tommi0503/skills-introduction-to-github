from pathlib import Path
import shutil
B=Path(__file__).resolve().parent.parent
C=B/'collection/nocturne';R=B/'review';D=R/'reassembled';D.mkdir(parents=True,exist_ok=True)
for p in C.rglob('*.css'):
 q=R/'assets/collection'/p.relative_to(C);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy(p,q)
for p in (B/'build/templates/reassembled').glob('*.html'):shutil.copy(p,D/p.name)
shutil.copy(B/'build/templates/source-style.css',R/'assets/source-style.css')
print('Reassembled sources restored from the measured contract-markup templates; collection CSS copied')
