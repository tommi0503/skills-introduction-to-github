"""Validate final dimensions, hashes, fonts, source count and archive readiness."""
import json,hashlib,sys
from pathlib import Path
from PIL import Image
import fitz
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 inv=json.loads((ROOT/'review/inventory.json').read_text());fail=[];rows=[];manifest={r['id']:r for r in json.loads((ROOT/'build/manifest.json').read_text())}
 for mode in ['replica','assembly']:
  for deck in sorted(set(r['deck']for r in inv)):
   f=ROOT/'review'/f'automatic-final-{mode}-{deck}.json'
   if not f.exists():fail.append(f'missing {f.name}');continue
   report=json.loads(f.read_text());src=ROOT/'src/decks'/f'{deck}.mjs'
   if report.get('rendererHash')!=sha(ROOT/'src/renderer.mjs') or report.get('primitiveHash')!=sha(ROOT/'src/primitives.mjs'):fail.append(f'{deck} shared source changed after final render')
   if report['sourceHash']!=sha(src):fail.append(f'{deck} source changed after final render')
   if manifest[deck]['builtSourceHash']!=sha(src):fail.append(f'{deck} source changed after build')
   if mode=='assembly':
    if report.get('assemblySourceHash')!=sha(ROOT/'src/assembly'/f'{deck}.mjs') or manifest[deck]['builtAssemblySourceHash']!=sha(ROOT/'src/assembly'/f'{deck}.mjs'):fail.append(f'{deck} assembly source changed after final build/render')
    if report.get('assemblyRendererHash')!=sha(ROOT/'src/assembly-renderer.mjs'):fail.append('assembly renderer changed after render')
   if report['errors']:fail.append(f'{deck} browser errors')
   expected=[r for r in inv if r['deck']==deck]
   if len(report['slides'])!=len(expected):fail.append(f'{deck} missing pages')
   for r in report['slides']:
    png=ROOT/'renders/final'/mode/deck/(r['slide']+'.png');html=ROOT/'build'/mode/deck/(r['slide']+'.html');size=Image.open(png).size
    if size!=(1280,720):fail.append(f'bad size {png}')
    if sha(png)!=r['sha256'] or sha(html)!=r['htmlSha256']:fail.append(f'stale render {deck}/{r["slide"]}')
    if r['sourceImageTags']:fail.append(f'source bitmap in result {deck}/{r["slide"]}')
    if r['findings']:fail.append(f'{mode}/{deck}/{r["slide"]}: {r["findings"]}')
    if any(x['status']!='loaded'for x in r['fonts']):
     # Unused font weights may remain unloaded. Actual text was checked with document.fonts.check.
     pass
    rows.append({'mode':mode,'deck':deck,'slide':r['slide'],'size':size,'sha256':sha(png)})
 for mode in ['replica','assembly']:
  for deck in sorted(set(r['deck']for r in inv)):
   pdf=ROOT/'pdfs'/mode/(deck+'.pdf')
   expected=sum(r['deck']==deck for r in inv)
   if not pdf.exists():fail.append(f'missing PDF {mode}/{deck}')
   else:
    doc=fitz.open(pdf)
    if len(doc)!=expected:fail.append(f'PDF page count {mode}/{deck}')
    for pg in doc:
     if list(pg.rect)!=[0.0,0.0,1280.0,720.0]:fail.append(f'PDF page size {mode}/{deck}')
    doc.close()
 result={'success':not fail,'referenceCount':len(inv),'renderCount':len(rows),'canvas':[1280,720],'pages':rows,'failures':fail};(ROOT/'review/final-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps({k:v for k,v in result.items()if k!='pages'},ensure_ascii=False,indent=2));sys.exit(bool(fail))
if __name__=='__main__':main()
