"""Archive only the portable project and its selected final captures."""
import hashlib
import json
import pathlib
import re
import zipfile

from PIL import Image

root = pathlib.Path(__file__).resolve().parents[1]
out = pathlib.Path('/workspace/shared/downloads')
out.mkdir(parents=True, exist_ok=True)
selected = {d['id'] for d in json.loads((root / 'public/reference/manifest.json').read_text())}
verification = json.loads((root / 'review/verification.json').read_text())
assert verification['status'] == 'passed' and verification['screens'] == len(selected)
excluded = {'node_modules', 'dist', '.git', '__pycache__', 'reference-contact'}
archive = out / 'presentation3-clone.zip'
files = []
for path in sorted(root.rglob('*')):
    relative = path.relative_to(root)
    if any(part in excluded for part in relative.parts):
        continue
    if path.is_symlink() or not path.is_file() or path.name.endswith('.tsbuildinfo'):
        continue
    if relative.parts[0] in {'renders', 'comparisons'}:
        if len(relative.parts) < 3 or relative.parts[1] != 'final':
            continue
        match = re.match(r'(p\d{2})(?:[-.]|$)', path.name)
        assert match and match[1] in selected, f'Unexpected capture: {relative}'
    files.append(path)
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zipped:
    for path in files:
        zipped.write(path, pathlib.PurePosixPath(root.name, path.relative_to(root)))
with zipfile.ZipFile(archive) as zipped:
    assert zipped.testzip() is None
    assert {name.split('/')[0] for name in zipped.namelist()} == {root.name}
    assert {name.split('/')[3] for name in zipped.namelist()
            if name.startswith(f'{root.name}/public/reference/p')} == selected
renders = list((root / 'renders/final').glob('p??-s01.png'))
assert len(renders) == len(selected)
for path in renders:
    with Image.open(path) as image:
        assert image.size == (1280, 720)
print(json.dumps({'archive': str(archive), 'screens': len(selected), 'files': len(files),
                  'bytes': archive.stat().st_size,
                  'sha256': hashlib.sha256(archive.read_bytes()).hexdigest()}, indent=2))
