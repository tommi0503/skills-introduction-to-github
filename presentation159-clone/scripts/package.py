"""Package the verified final captures and the individual review evidence."""
import hashlib
import json
import math
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
manifest = json.loads((ROOT / 'public/reference/manifest.json').read_text())
verification = json.loads((ROOT / 'review/verification.json').read_text())
main_review = json.loads((ROOT / 'review/main-review.json').read_text())
assert verification['status'] == 'passed'
keys = [f"{d['id']}-{s['id']}" for d in manifest for s in d['slides']]
assert len(keys) == 159 and len(set(keys)) == 159
reviews = {f"{p['deck']}-{p['slide']}": p for p in main_review['pages']}
assert set(reviews) == set(keys)
assert all(p['finalComparisonViewed'] for p in reviews.values())

font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 16)
columns, thumb_w, thumb_h, label_h = 5, 320, 180, 28
preview = Image.new('RGB', (columns * thumb_w, math.ceil(len(keys) / columns) * (thumb_h + label_h)), '#e9ecf0')
draw = ImageDraw.Draw(preview)
files = {}
for i, key in enumerate(keys):
    deck, slide = key.split('-')
    metadata = json.loads((ROOT / f'comparisons/final/{deck}.json').read_text())
    capture = next(page for page in metadata['slides'] if page['id'] == slide)
    assert reviews[key]['definitionHash'] == metadata['definitionHash'], f'Stale definition review: {key}'
    assert reviews[key]['rendererHash'] == metadata['rendererHash'], f'Stale renderer review: {key}'
    assert not capture['findings'], f'Unresolved automatic findings: {key}'
    png = ROOT / 'renders/final' / f'{key}.png'
    raw = png.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == reviews[key]['finalPngSha256'], f'Stale visual review: {key}'
    with Image.open(png) as image:
        image.verify()
    with Image.open(png) as image:
        assert image.size == (1280, 720), f'Wrong canvas: {key}'
        x, y = i % columns * thumb_w, i // columns * (thumb_h + label_h)
        preview.paste(image.convert('RGB').resize((thumb_w, thumb_h), Image.Resampling.LANCZOS), (x, y))
        draw.text((x + 10, y + thumb_h + 5), key, fill='#20242c', font=font)
    pair = ROOT / 'comparisons/final' / f'{key}.jpg'
    assert hashlib.sha256(pair.read_bytes()).hexdigest() == reviews[key]['finalComparisonSha256'], f'Stale comparison review: {key}'
    with Image.open(pair) as image:
        image.verify()
    files[f'renders/{key}.png'] = png
    files[f'comparisons/{key}.jpg'] = pair

preview_path = REPO / 'presentation159-clone-preview.jpg'
preview.save(preview_path, quality=90, optimize=True)
files['preview.jpg'] = preview_path
files['README.md'] = ROOT / 'README.md'
files['manifest.json'] = ROOT / 'public/reference/manifest.json'
for base in ['review', 'provenance']:
    for file in sorted((ROOT / base).rglob('*')):
        if file.is_file() and file.name not in {'package-verification.json', 'github-download-verification.json'}:
            files[str(file.relative_to(ROOT))] = file
for file in sorted((ROOT / 'comparisons/final').glob('*.json')):
    files['review/final-capture-metadata/' + file.name] = file

checksums = {name: hashlib.sha256(file.read_bytes()).hexdigest() for name, file in files.items()}
zip_path = REPO / 'presentation159-clone-renders.zip'
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
    for name, file in files.items():
        archive.write(file, name)
    archive.writestr('SHA256SUMS.json', json.dumps(checksums, ensure_ascii=False, indent=2) + '\n')
with zipfile.ZipFile(zip_path) as archive:
    assert archive.testzip() is None
    assert len([name for name in archive.namelist() if name.endswith('.png')]) == 159
    assert len([name for name in archive.namelist() if name.startswith('comparisons/') and name.endswith('.jpg')]) == 159
    assert all(hashlib.sha256(archive.read(name)).hexdigest() == digest for name, digest in checksums.items())
report = {
    'status': 'passed', 'zip': zip_path.name, 'bytes': zip_path.stat().st_size,
    'sha256': hashlib.sha256(zip_path.read_bytes()).hexdigest(),
    'pngCount': 159, 'comparisonCount': 159, 'allPngSizes': [1280, 720],
    'previewSize': list(preview.size), 'crcVerified': True, 'entrySha256Verified': True,
    'latestFinalVisualReviewHashesMatch': True,
}
(ROOT / 'review/package-verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False, indent=2))
