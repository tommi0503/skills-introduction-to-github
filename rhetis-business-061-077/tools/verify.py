"""Verify counts, dimensions, freshness, schemas and static collection constraints."""
from pathlib import Path
import json,re,hashlib,collections
from PIL import Image,ImageChops,ImageStat
import fitz
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
failures=[]
def check(ok,message):
 if not ok:failures.append(message)
inventory=json.loads((ROOT/'review/reference-inventory.json').read_text());expected=sum(d['count'] for d in inventory)
lib=ROOT/'collection/business-prism';parts=sorted((lib/'elements').iterdir());check(len(parts)==31,'31 elements required')
contracts={c['id'] for c in json.loads((ROOT/'contract/taxonomy.json').read_text())['contracts']}
found=set();fixtures=0
for d in parts:
 j=json.loads((d/'element.json').read_text());found.add(j['contract']);check(j['schema']=='rhetis.design-library-element-source/1',f'{d.name} schema')
 fs=list((d/'fixtures').glob('*.html'));fixtures+=len(fs);check(len(fs)>=2,f'{d.name} fixtures')
 css=(d/'element.css').read_text();check(f'[data-el="business-prism-{d.name}"]' in css,f'{d.name} scope')
 check(not re.search(r'#[a-fA-F0-9]{3,8}\b|\b(?:rgb|hsl)a?\s*\(',css),f'{d.name} literal color')
 check(not re.search(r'font-size\s*:\s*(?!var\(--type-)\d',css),f'{d.name} literal type size')
 check(not re.search(r'@(?:import|font-face|keyframes|property)\b|url\(',css),f'{d.name} forbidden resource/at-rule')
 check('@container' in css,f'{d.name} responsive rules')
 for f in fs:
  h=f.read_text();check(bool(re.match(r'<!--\s*min:',h)),str(f.relative_to(ROOT))+' minimum declaration')
check(found==contracts,'Contract coverage')
tokens=(lib/'kit/css/tokens.css').read_text();required=json.loads((ROOT/'contract/kit-tokens.json').read_text())['tokens']
for name,kind in required.items():check(tokens.count(name+':')>=(2 if kind=='color' else 1),f'{name} missing mode')
counts={};pdfcounts={};diffs=[]
for mode in ['replica','assembly']:
 pngs=sorted((ROOT/'renders/final'/mode).glob('*/*.png'));counts[mode]=len(pngs);check(len(pngs)==expected,f'{mode} image count')
 for p in pngs:check(Image.open(p).size==(1280,720),f'{p} size')
 for d in inventory:
  report=json.loads((ROOT/'review'/f'automatic-final-{mode}-{d["id"]}.json').read_text())
  check(report['sourceHash']==sha(ROOT/'src/decks'/f'{d["id"]}.mjs'),f'{mode}/{d["id"]} stale source')
  for s in report['slides']:
   p=ROOT/'renders/final'/mode/d['id']/(s['slide']+'.png');h=ROOT/'build'/mode/d['id']/(s['slide']+'.html')
   check(s['sha256']==sha(p),f'{p} stale PNG');check(s['htmlSha256']==sha(h),f'{p} HTML changed after render');check(not s['findings'],f'{p} browser findings')
 for p in sorted((ROOT/'pdfs').glob(f'{mode}*.pdf')):
  with fitz.open(p) as doc:
   pdfcounts[p.name]=len(doc);check(all(abs(pg.rect.width-1280)<.1 and abs(pg.rect.height-720)<.1 for pg in doc),f'{p} page sizes')
for p in sorted((ROOT/'renders/final/replica').glob('*/*.png')):
 q=ROOT/'renders/final/assembly'/p.parent.name/p.name;diff=ImageChops.difference(Image.open(p).convert('RGB'),Image.open(q).convert('RGB'));ext=diff.getextrema()
 diffs.append({'deck':p.parent.name,'slide':p.stem,'meanRGBError':sum(ImageStat.Stat(diff).mean)/3,'maxChannelError':max(v[1] for v in ext),'identical':diff.getbbox() is None})
(ROOT/'review/reassembly-pixel-comparison.json').write_text(json.dumps(diffs,indent=2))
audit=json.loads((ROOT/'review/final-browser-audit.json').read_text());check(audit['issues']==0,'Final browser audit')
for name,digest in audit['sourceHashes'].items():check(sha(ROOT/name)==digest,f'{name} changed after audit')
librarypngs=list((ROOT/'renders/library').glob('*/*.png'));check(len(librarypngs)==166,'library PNG count')
check(all(Image.open(p).size==(1280,720) for p in librarypngs),'library PNG dimensions')
sheetpngs=list((ROOT/'previews').glob('*/*.png'));check(len(sheetpngs)==26,'sheet PNG count')
check(all(Image.open(p).size==(1280,720) for p in sheetpngs),'sheet PNG dimensions')
for mode in ['light','dark']:
 p=ROOT/'pdfs'/f'library-{mode}.pdf'
 with fitz.open(p) as doc:
  pdfcounts[p.name]=len(doc);check(len(doc)==83,f'{p} pages');check(all(pg.rect.width==1280 and pg.rect.height==720 for pg in doc),f'{p} sizes')
for mode in ['replica','assembly']:
 for d in inventory:
  p=ROOT/'pdfs'/mode/(d['id']+'.pdf')
  with fitz.open(p) as doc:check(len(doc)==d['count'],f'{p} deck pages')
 check(len(list((ROOT/'comparisons/final'/mode).glob('*/*.jpg')))==117,f'{mode} comparison count')
report={'referenceSlides':expected,'decks':len(inventory),'renderCounts':counts,'libraryElements':len(parts),'elementFixtures':fixtures,'foundationFixtures':len(list((lib/'foundation/fixtures').glob('*.html'))),'libraryPNGs':len(librarypngs),'pdfPages':pdfcounts,'browserAuditIssues':audit['issues'],'assemblyIdenticalPages':sum(d['identical'] for d in diffs),'assemblyMaxMeanRGBError':max(d['meanRGBError'] for d in diffs),'failures':failures}
(ROOT/'review/verification.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2));raise SystemExit(bool(failures))
