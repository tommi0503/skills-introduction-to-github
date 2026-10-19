"""Produce portable delivery and strict single-root collection ZIPs."""
from pathlib import Path
import hashlib, json, zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent
NAME = ROOT.name


def include(p):
    rel = p.relative_to(ROOT)
    if '__pycache__' in rel.parts or p.suffix in {'.pyc', '.log'}:
        return False
    if rel.parts[:3] == ('comparisons', 'final', 'assembly'):
        return False  # Identical pixels: one comparison pair serves both output modes.
    if rel.parts[0] in {'renders', 'comparisons'}:
        return len(rel.parts) > 1 and rel.parts[1] in {'final', 'library'}
    return True


def archive(path, base, paths, prefix):
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for p in paths:
            z.write(p, str(Path(prefix) / p.relative_to(base)))
    with zipfile.ZipFile(path) as z:
        bad = z.testzip()
        if bad:
            raise RuntimeError(f'Invalid member: {bad}')
        roots = sorted({n.split('/')[0] for n in z.namelist()})
        if roots != [prefix]:
            raise RuntimeError(f'Unexpected ZIP roots: {roots}')
        count = len(z.namelist())
    return {'name': path.name, 'bytes': path.stat().st_size,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'members': count, 'roots': roots, 'testzip': 'passed'}


def main():
    verification = json.loads((ROOT / 'review/final-verification.json').read_text())
    if not verification['success']:
        raise RuntimeError('Final browser verification has not passed')
    c = ROOT / 'collection/rhetis-spectrum'
    records = [archive(OUT / 'rhetis-spectrum-collection.zip', c,
                       sorted(p for p in c.rglob('*') if p.is_file()), c.name)]
    records.append(archive(OUT / (NAME + '-delivery.zip'), ROOT,
                           sorted(p for p in ROOT.rglob('*') if p.is_file() and include(p)), NAME))
    result = {'archives': records, 'canvas': [1280, 720],
              'references': verification['referenceCount'], 'renders': verification['renderCount']}
    (OUT / (NAME + '-archives.json')).write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
