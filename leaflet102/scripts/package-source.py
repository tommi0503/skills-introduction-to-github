from pathlib import Path
import hashlib
import json
import zipfile

root = Path(__file__).resolve().parents[1]
destination = root / 'deliverables'
destination.mkdir(exist_ok=True)
excluded = {'node_modules', 'dist', 'renders', 'comparisons', 'work', 'deliverables', '.git'}
allowed = {'.ts', '.tsx', '.css', '.json', '.mjs', '.py', '.md', '.html'}
files = sorted(p for p in root.rglob('*') if p.is_file()
               and not any(part in excluded for part in p.relative_to(root).parts)
               and (p.suffix in allowed or p.name == '.gitignore'))
archive = destination / 'leaflet102-source.zip'
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
    for source in files:
        bundle.write(source, 'leaflet102/' + source.relative_to(root).as_posix())
with zipfile.ZipFile(archive) as bundle:
    assert bundle.testzip() is None
report = {'archive': archive.name, 'files': len(files), 'bytes': archive.stat().st_size,
          'sha256': hashlib.sha256(archive.read_bytes()).hexdigest(), 'crcPassed': True}
(destination / 'integrity.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
