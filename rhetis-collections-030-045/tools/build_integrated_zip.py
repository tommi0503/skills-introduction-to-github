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
    parser.add_argument("--source-only", action="store_true", help="Include every code/font file and native slide previews; omit review media.")
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
        if args.source_only:
            if rel.parts[0] == "originals" or source.suffix == ".pdf":
                continue
            if source.suffix == ".png" and rel.as_posix() != "preview.png":
                if not (len(rel.parts) == 4 and rel.parts[0] == "reviews" and rel.parts[2] in {"replica", "reassembled"}):
                    continue
        files.append(source)
    overrides = {}
    if args.source_only:
        # Keep the standalone index useful without duplicating large comparison images.
        html = (ROOT / "index.html").read_text()
        import re
        html = re.sub(r'(?<![\w/])reviews/[\w-]+-review/compare-(?:replica|reassembled)/[\w.-]+\.png',
                      lambda match: "https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/" + NAME + "/" + match[0], html)
        overrides["index.html"] = html.encode()
    contents = []
    for source in files:
        rel = source.relative_to(ROOT).as_posix()
        payload = overrides.get(rel)
        entry = {"path": rel, "bytes": len(payload) if payload is not None else source.stat().st_size,
                 "sha256": hashlib.sha256(payload).hexdigest() if payload is not None else sha(source)}
        if payload is not None:
            entry["sourceSHA256"] = sha(source)
            entry["exportChange"] = "Comparison media links point to the published original files."
        contents.append(entry)
    excluded = ["downloads/ (the twelve redundant individual ZIPs)",
                "integrated-bundle/ (publication receipts)", "Python caches"]
    if args.source_only:
        excluded.extend(["PDFs", "original reference PNGs", "library/comparison PNGs (published separately)"])
    manifest = {"topFolder": NAME, "collections": COLLECTIONS,
                "elements": 336, "replicaPages": 90, "reassembledPages": 90,
                "sourceOnly": args.source_only, "excluded": excluded,
                "files": contents}
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for source in files:
            rel = source.relative_to(ROOT).as_posix()
            if rel in overrides:
                archive.writestr(NAME + "/" + rel, overrides[rel])
            else:
                archive.write(source, NAME + "/" + rel)
        archive.writestr(NAME + "/bundle-manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))
        if args.source_only:
            archive.writestr(NAME + "/BUNDLE-README.md", """# 전체 컬렉션·복제본 통합 소스

컬렉션6개(요소336종), replica90장과 조립본90장의 HTML/CSS, 모든 fixture·metadata·문서·빌드도구와 실행용폰트를 포함합니다. 슬라이드별 PNG180장과 첫 화면 미리보기도 포함했습니다.

1. 이 폴더에서 `python3 -m http.server 8000 --bind 127.0.0.1` 실행
2. `http://127.0.0.1:8000/` 열기
3. 컬렉션은 `collections/`, 복제본 코드는 `reviews/<name>-review/replica/`, 조립본은 `reviews/<name>-review/reassembled/`에서 확인

검수PDF·원본PNG·비교PNG·요소시트PNG는 별도제공한 검수자료에 있습니다. 비교미리보기는 게시된 이미지로 연결됩니다. 네이티브 HTML 슬라이드와 라이브러리 HTML은 포함된 로컬폰트로 실행할 수 있습니다.

[전체소스·검수자료](https://github.com/tommi0503/skills-introduction-to-github/tree/main/rhetis-collections-030-045)

ZIP 내부 `bundle-manifest.json`에서 모든 포함파일의 SHA-256을 확인할 수 있습니다. 전체미디어 통합 ZIP은 `python tools/build_integrated_zip.py --out ../all-with-review-media.zip`으로 만들 수 있습니다(별도검수자료를 source tree에 받은 뒤 실행).
""")
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
    if args.source_only:
        assert target.stat().st_size < 100 * 1024 ** 2
    report = {"file": target.name, "bytes": target.stat().st_size, "sha256": sha(target),
              "entries": len(contents) + (2 if args.source_only else 1), "topFolder": NAME, "zipCRC": "passed",
              "everyFileSHA256": "passed", "collections": 6, "elements": 336,
              "replicaPages": 90, "reassembledPages": 90,
              "sourceOnly": args.source_only,
              "includes": (["every collection/fixture source", "every replica and reassembled source",
                            "all code files and metadata", "fonts", "180 native slide PNGs", "contract",
                            "build and review tools", "interactive preview"] if args.source_only else
                           ["collection sources", "replica and reassembled sources", "all review images and PDFs",
                            "original reference images", "fonts", "contract", "build and review tools", "interactive preview"]),
              "excluded": manifest["excluded"]}
    publication = ROOT / "integrated-bundle"
    publication.mkdir(exist_ok=True)
    (publication / "verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
