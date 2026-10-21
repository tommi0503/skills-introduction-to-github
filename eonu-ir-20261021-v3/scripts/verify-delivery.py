"""Verify rendered sources, all PNGs, HTML references, fixed pixels and PDFs."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import hashlib
import json
import re
import fitz

ROOT = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
render = json.loads((ROOT / 'review/render-audit.json').read_text())
viewer = json.loads((ROOT / 'review/viewer-check.json').read_text())
assert render['status'] == 'passed'
assert viewer['status'] == 'passed'
source_match = all(sha(ROOT / p) == h for p, h in render['sourceHashes'].items())
viewer_match = all(sha(ROOT / p) == h for p, h in viewer['sourceHashes'].items())
png_match = all(sha(ROOT / 'previews' / p['theme'] / (p['id'] + '.png')) == p['pngSha256'] for p in render['pages'])
assert source_match and viewer_match and png_match, 'Source or preview changed after inspection'

missing = []
htmls = list(ROOT.rglob('*.html'))
for file in htmls:
    if 'node_modules' in file.parts:
        continue
    for ref in re.findall(r'''(?:href|src)=["']([^"']+)''', file.read_text()):
        parsed = urlsplit(ref)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        if not (file.parent / unquote(parsed.path)).exists():
            missing.append([str(file.relative_to(ROOT)), ref])
assert not missing, missing

pixel_audit = {}
for name in ['src/slides.css', 'src/viewer.css', 'scripts/build-pages.mjs', 'scripts/build-docs.mjs']:
    values = [float(v) for v in re.findall(r'(-?\d*\.?\d+)px', (ROOT / name).read_text())]
    off_grid = [v for v in values if v % 2]
    pixel_audit[name] = {'tokens': len(values), 'offGrid': off_grid}
    assert not off_grid, (name, off_grid)

pdfs = []
for file in sorted((ROOT / 'previews').glob('*.pdf')):
    doc = fitz.open(file)
    expected = {'eonu-design.pdf': 12, 'eonu-wireframe.pdf': 12, 'eonu-combined-24p.pdf': 24}.get(file.name)
    if expected:
        assert len(doc) == expected
        assert all(page.rect.width == 960 and page.rect.height == 540 for page in doc)
    assert all(page.get_text().strip() for page in doc)
    pdfs.append({'file': str(file.relative_to(ROOT)), 'pages': len(doc), 'bytes': file.stat().st_size, 'sha256': sha(file), 'textOnEveryPage': True})

report = {
    'status': 'passed',
    'finalSourceHashesMatch': source_match,
    'viewerSourceHashesMatch': viewer_match,
    'all24PngHashesMatch': png_match,
    'htmlFilesChecked': len([f for f in htmls if 'node_modules' not in f.parts]),
    'localHtmlLinksResolve': True,
    'missing': missing,
    'pixelGrid': pixel_audit,
    'placeholdersPerVariant': {theme: sum(len(p['placeholders']) for p in render['pages'] if p['theme'] == theme) for theme in ['design', 'wireframe']},
    'bookendsHaveNoRunningHeader': all(not p['bookendHasRunningHeader'] for p in render['pages'] if p['bookend']),
    'pdfs': pdfs,
}
(ROOT / 'review/final-consistency.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'status': 'passed', 'htmls': report['htmlFilesChecked'], 'pngs': len(render['pages']), 'pdfPages': {p['file']: p['pages'] for p in pdfs}}, ensure_ascii=False, indent=2))
