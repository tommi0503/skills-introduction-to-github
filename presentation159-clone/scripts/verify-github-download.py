"""Download the committed GitHub ZIP and verify bytes, entries and PNG canvases."""
import hashlib
import io
import json
import re
import sys
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
commit = sys.argv[1]
assert re.fullmatch(r'[0-9a-f]{40}', commit), 'Supply the full published commit SHA'
expected = json.loads((ROOT / 'review/package-verification.json').read_text())
url = f'https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/{commit}/presentation159-clone-renders.zip'
destination = Path('/workspace/shared/downloads/presentation159-clone-renders.github.zip')
destination.parent.mkdir(parents=True, exist_ok=True)
with urllib.request.urlopen(url, timeout=60) as response, destination.open('wb') as file:
    assert response.status == 200
    while chunk := response.read(1024 * 1024):
        file.write(chunk)

digest = hashlib.sha256(destination.read_bytes()).hexdigest()
assert digest == expected['sha256'], 'GitHub download differs from packaged ZIP'
assert destination.stat().st_size == expected['bytes']
with zipfile.ZipFile(destination) as archive:
    assert archive.testzip() is None, 'ZIP CRC failed'
    names = archive.namelist()
    assert len(names) == len(set(names)), 'Duplicate archive names'
    checksums = json.loads(archive.read('SHA256SUMS.json'))
    assert set(names) == set(checksums) | {'SHA256SUMS.json'}
    for name, entry_digest in checksums.items():
        assert hashlib.sha256(archive.read(name)).hexdigest() == entry_digest, name
    pngs = [name for name in names if name.startswith('renders/') and name.endswith('.png')]
    pairs = [name for name in names if name.startswith('comparisons/') and name.endswith('.jpg')]
    assert len(pngs) == len(pairs) == 159
    for name in pngs:
        with Image.open(io.BytesIO(archive.read(name))) as image:
            assert image.size == (1280, 720), name
            image.verify()
    with Image.open(io.BytesIO(archive.read('preview.jpg'))) as image:
        assert image.size == tuple(expected['previewSize'])
        image.verify()

report = {
    'status': 'passed', 'repository': 'tommi0503/skills-introduction-to-github',
    'artifactCommit': commit, 'downloadUrl': url,
    'checkedAt': datetime.now(timezone.utc).isoformat(),
    'bytes': destination.stat().st_size, 'sha256': digest,
    'matchesLocalPackage': True, 'crcVerified': True,
    'allEntrySha256Verified': True, 'pngCount': len(pngs),
    'comparisonCount': len(pairs), 'allPngSizes': [1280, 720],
    'previewVerified': True,
}
(ROOT / 'review/github-download-verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(report, ensure_ascii=False, indent=2))
