"""Copy this task's sources into a new repository subdirectory; preserve all v1 work."""
from pathlib import Path
import argparse, hashlib, json, shutil

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {'__pycache__', 'sheet-runtime', 'foundation-runtime'}

def run(dest):
    dest = dest.resolve()
    assert dest.name == 'rhetis-part07-elements-v2', dest
    manifest_path = dest / 'source-copy-manifest.json'
    previous = json.loads(manifest_path.read_text()).get('files', {}) if manifest_path.exists() else {}
    current = {}
    for source in sorted(ROOT.rglob('*')):
        rel = source.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts) or source.suffix == '.pyc' or rel.as_posix() == 'STATE.md':
            continue
        if not source.is_file():
            continue
        assert not source.is_symlink(), source
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        if not target.exists() or hashlib.sha256(target.read_bytes()).hexdigest() != digest:
            shutil.copy2(source, target)
        assert hashlib.sha256(target.read_bytes()).hexdigest() == digest
        current[rel.as_posix()] = digest
    # Only remove files this script previously copied into its own new directory.
    for rel in previous.keys() - current.keys():
        target = dest / rel
        if target.is_file():
            target.unlink()
    manifest_path.write_text(json.dumps({'source': str(ROOT), 'files': current}, ensure_ascii=False, indent=2))
    print(json.dumps({'copiedFiles': len(current), 'destination': str(dest), 'allSHA256Match': True}))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('destination', type=Path)
    run(parser.parse_args().destination)
