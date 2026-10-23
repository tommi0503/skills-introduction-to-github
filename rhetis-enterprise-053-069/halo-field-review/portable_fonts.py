from pathlib import Path
import re,shutil,os
R=Path(__file__).parent;REF=Path('/workspace/work/ref/fonts');dest=R/'fonts';dest.mkdir(exist_ok=True)
s='\n'.join(line for line in (REF/'fonts.css').read_text().splitlines() if "'Freesentation'" in line or "'Nanum Gothic Coding'" in line)
(dest/'fonts.css').write_text(s)
for x in re.findall("url\\('([^']+)'\\)",s):
 d=dest/x;d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(REF/x,d)
for p in R.rglob('*.html'):
 href=os.path.relpath(dest/'fonts.css',p.parent)
 text=p.read_text().replace('http://127.0.0.1:8765/fonts/fonts.css',href);p.write_text(text)
print('relative font links ready')
