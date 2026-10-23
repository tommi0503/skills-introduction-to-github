"""Build one standalone ZIP containing all six collections and review/source files."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "rhetis-collections-030-045"
COLLECTIONS = {"chalkline": 2, "undertow": 13, "cutplane": 15,
               "skylight": 21, "arrowtab": 20, "blockweave": 19}


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    target = Path(args.out).resolve()
    assert ROOT not in target.parents, "Write the ZIP outside its source folder."
    target.parent.mkdir(parents=True, exist_ok=True)
    files = []
    for source in sorted(ROOT.rglob("*")):
        if not source.is_file():
            continue
        rel = source.relative_to(ROOT)
        if rel.parts[0] in {"downloads", "integrated-bundle", ".git"}:
            continue
        if "__pycache__" in rel.parts or source.suffix == ".pyc":
            continue
        files.append(source)
    contents = [{"path": str(f.relative_to(ROOT)), "bytes": f.stat().st_size,
                 "sha256": sha(f)} for f in files]
    manifest = {"topFolder": NAME, "collections": COLLECTIONS,
                "elements": 336, "replicaPages": 90, "reassembledPages": 90,
                "excluded": ["downloads/ (the twelve redundant individual ZIPs)",
                             "integrated-bundle/ (publication receipts)", "Python caches"],
                "files": contents}
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for source in files:
            archive.write(source, NAME + "/" + source.relative_to(ROOT).as_posix())
        archive.writestr(NAME + "/bundle-manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))
    with zipfile.ZipFile(target) as archive:
        assert archive.testzip() is None
        names = set(archive.namelist())
        assert {name.split("/")[0] for name in names} == {NAME}
        for name, count in COLLECTIONS.items():
            base = NAME + "/collections/" + name + "/"
            elements = {p.split("/")[4] for p in names if p.startswith(base + "elements/")}
            assert len(elements) == 56, (name, len(elements))
            for kind in ("replica", "reassembled"):
                base = NAME + "/reviews/" + name + "-review/" + kind + "/"
                pages = [p for p in names if p.startswith(base) and "/" not in p[len(base):]
                         and p.endswith(".html") and not p.endswith("/index.html")]
                assert len(pages) == count, (name, kind, len(pages))
        for entry in contents:
            with archive.open(NAME + "/" + entry["path"]) as stream:
                digest = hashlib.sha256()
                while chunk := stream.read(1024 * 1024):
                    digest.update(chunk)
                assert digest.hexdigest() == entry["sha256"], entry["path"]
    report = {"file": target.name, "bytes": target.stat().st_size, "sha256": sha(target),
              "entries": len(contents) + 1, "topFolder": NAME, "zipCRC": "passed",
              "everyFileSHA256": "passed", "collections": 6, "elements": 336,
              "replicaPages": 90, "reassembledPages": 90,
              "includes": ["collection sources", "replica and reassembled sources",
                           "all review images and PDFs", "original reference images",
                           "fonts", "contract", "build and review tools", "interactive preview"],
              "excluded": manifest["excluded"]}
    publication = ROOT / "integrated-bundle"
    publication.mkdir(exist_ok=True)
    (publication / "verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
