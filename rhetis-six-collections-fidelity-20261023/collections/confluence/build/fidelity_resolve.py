from pathlib import Path
import shutil,json,re,hashlib,collections
from PIL import Image
import fitz
D=Path('/workspace/work/deliverables/confluence');C=D/'collection/confluence';R=D/'review'
p=C/'elements/hub/element.css';s=p.read_text();rule='\n@container(min-width:1200px){.hub[data-el="confluence-hub"]:has(>.spoke:nth-child(5):last-child) .core,.hub[data-el="confluence-hub"]:has(>.spoke:nth-child(5):last-child) .spoke{grid-column:1 / -1!important;grid-row:1 / -1!important}}\n'
if rule.strip() not in s:s+=rule;p.write_text(s)
for p in C.rglob('*.css'):
 out=R/'assets/collection'/p.relative_to(C);out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,out)
manifest={str(p.relative_to(C)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(C.rglob('*')) if p.is_file()};(R/'source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
# Preserve concrete evidence of a radial-gradient false positive using actual exported pixels.
def lum(rgb):
 a=[v/255 for v in rgb];a=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in a];return sum(v*k for v,k in zip(a,[.2126,.7152,.0722]))
html=(R/'library/dark.html').read_text();titles=re.findall(r'<h2[^>]*>(.*?)</h2>',html);idx=next(i for i,t in enumerate(titles) if t.startswith('prose / prose-cols '));pdf=fitz.open(R/'library/library-dark.pdf');pix=pdf[idx].get_pixmap();bg=pix.pixel(90,275)[:3];fg=(246,247,250);ratio=(max(lum(bg),lum(fg))+.05)/(min(lum(bg),lum(fg))+.05);pdf.close()
(R/'audit-gradient-evidence.json').write_text(json.dumps({'case':'dark prose / prose-cols, first text region','pdfPageIndex':idx,'samplePixel':[90,275],'actualBackgroundRgb':bg,'computedForegroundRgb':fg,'actualContrast':round(ratio,2),'rawGradientStopRatio':1.09,'interpretation':'The transparent radial stop is composited over a dark linear background. Treating it as opaque white gives a false contrast failure. Shape retained to preserve the source.'},ensure_ascii=False,indent=2)+'\n')
print('Source manifest and radial evidence written')
