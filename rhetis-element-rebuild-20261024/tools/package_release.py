#!/usr/bin/env python3
"""Package the seven audited collections. Never run before primary release review.

Default: python tools/package_release.py
Existing ZIPs are preserved unless --replace is explicitly supplied; replaced files
are moved to a timestamped backup directory. No immutable replica is packaged.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import sys
import tempfile
import zipfile
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
NAMES = ("tide-tab", "cutfield", "filament", "portico", "toggle-grid", "lamella", "rulemark")
SOURCE_EXTENSIONS = {".css", ".json", ".md", ".html"}
FORBIDDEN_REVIEW_PARTS = {"replica", "build", "cells", "__pycache__", ".git"}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def safe_file(path: Path, base: Path) -> None:
    require(not path.is_symlink(), f"Symlink refused: {path}")
    require(path.is_file(), f"Not a regular file: {path}")
    require(path.resolve().is_relative_to(base.resolve()), f"Path escapes tree: {path}")
    relative = path.relative_to(base)
    require(all(part not in (".", "..", "") for part in relative.parts), f"Unsafe path: {path}")


def collect(name: str) -> dict[str, list[tuple[Path, str]]]:
    source = ROOT / name / name
    review = ROOT / name / "review"
    require(source.is_dir() and review.is_dir(), f"Missing source or review: {name}")
    for tree in (source, review):
        require(not tree.is_symlink(), f"Symlink root refused: {tree}")
        require(not any(p.is_symlink() for p in tree.rglob("*")), f"Symlink in {tree}")
    collection = []
    for path in sorted(source.rglob("*")):
        if path.is_dir():
            continue
        safe_file(path, source)
        require(path.suffix in SOURCE_EXTENSIONS, f"Unsupported collection file: {path}")
        collection.append((path, name + "/" + path.relative_to(source).as_posix()))
    require(collection, f"Empty collection: {name}")
    expected_html = {
        "html/" + folder.name + "/" + fixture.stem + "-" + mode + ".html"
        for folder in source.joinpath("elements").iterdir() if folder.is_dir()
        for fixture in folder.joinpath("fixtures").glob("*.html")
        for mode in ("light", "dark")
    }
    review_files = []
    for path in sorted(review.rglob("*")):
        if path.is_dir():
            continue
        relative = path.relative_to(review)
        if FORBIDDEN_REVIEW_PARTS.intersection(relative.parts):
            continue
        safe_file(path, review)
        member = relative.as_posix()
        if relative.parts[0] == "html" and member not in expected_html:
            continue
        review_files.append((path, member))
    available = {member for _, member in review_files}
    require(expected_html <= available, f"Missing current fixture HTML in {name}: {sorted(expected_html - available)[:8]}")
    for item in ("map.json", "GAPS.md", "review-notes.md", "light.html", "dark.html", "validation/release-audit.json"):
        require(item in available, f"Required review file absent: {name}/{item}")
    for directory in ("sheets", "reassembled", "compare-reassembled"):
        require(any(member.startswith(directory + "/") for member in available), f"Empty review directory {name}/{directory}")
    return {name + ".zip": collection, name + "-review.zip": review_files}


def audit_all() -> dict:
    # An existing final READY gate is mandatory. Re-run its checks as well so a
    # subsequent source change cannot pass using an old successful JSON file.
    previous = {}
    for name in NAMES:
        path = ROOT / name / "review/validation/release-audit.json"
        require(path.is_file(), f"Missing release-audit: {name}")
        report = json.loads(path.read_text())
        require(report.get("collection") == name and report.get("ready") is True and not report.get("issues"), f"Release gate is not READY: {name}")
        previous[name] = report
    from release_audit import check
    fresh = {name: check(name) for name in NAMES}
    require(all(report.get("ready") is True and not report.get("issues") for report in fresh.values()), "Fresh release audit failed; no archives were created")
    return fresh


def write_zip(target: Path, files: list[tuple[Path, str]], expected: dict[Path, str]) -> dict:
    dimensions = {}
    entries = []
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path, member in files:
            pure = PurePosixPath(member)
            require(not pure.is_absolute() and ".." not in pure.parts and "\\" not in member, f"Unsafe ZIP member: {member}")
            data = path.read_bytes()
            require(sha(data) == expected[path], f"Source changed during packaging: {path}")
            if path.suffix.lower() == ".png":
                with Image.open(io.BytesIO(data)) as im:
                    require(im.format == "PNG", f"Wrong PNG format: {path}")
                    im.verify()
                with Image.open(io.BytesIO(data)) as im:
                    dimensions[member] = list(im.size)
                    if member.startswith(("reassembled/",)):
                        require(im.size == (1280, 720), f"Wrong page size: {path}: {im.size}")
            # Stable metadata makes reruns reproducible while retaining UTF-8 names.
            info = zipfile.ZipInfo(member, (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
            entries.append({"path": member, "bytes": len(data), "sha256": sha(data)})
    with zipfile.ZipFile(target) as archive:
        require(archive.testzip() is None, f"ZIP CRC failure: {target}")
        require(archive.namelist() == [item["path"] for item in entries], f"ZIP member mismatch: {target}")
        require(len(archive.namelist()) == len(set(archive.namelist())), f"Duplicate ZIP paths: {target}")
        if not target.name.endswith("-review.zip"):
            name = target.stem
            require({PurePosixPath(item).parts[0] for item in archive.namelist()} == {name}, f"Wrong collection top-level: {target}")
            require(all(PurePosixPath(item).suffix in SOURCE_EXTENSIONS for item in archive.namelist()), f"Wrong collection extension: {target}")
        else:
            require(not any(FORBIDDEN_REVIEW_PARTS.intersection(PurePosixPath(item).parts) for item in archive.namelist()), f"Private or replica path in review: {target}")
    return {"file": target.name, "bytes": target.stat().st_size, "sha256": sha(target.read_bytes()), "file_count": len(entries), "png_count": len(dimensions), "png_dimensions": dimensions, "entries": entries, "zip_test": "pass"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replace", action="store_true", help="Preserve existing release files in a timestamped backup and replace them")
    args = parser.parse_args()
    gates = audit_all()
    # Preflight every collection before making dist or opening any ZIP.
    plans = {}
    for name in NAMES:
        plans.update(collect(name))
    require(len(plans) == 14, "Expected exactly fourteen archives")
    snapshots = {path: sha(path.read_bytes()) for files in plans.values() for path, _ in files}
    dist = ROOT / "dist"
    outputs = list(plans) + ["release-manifest.json", "SHA256SUMS", "png-dimensions.json"]
    existing = [dist / name for name in outputs if (dist / name).exists()]
    require(args.replace or not existing, "Existing release outputs preserved. Pass --replace to back them up explicitly: " + ", ".join(path.name for path in existing))
    dist.mkdir(exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".release-staging-", dir=dist))
    try:
        reports = [write_zip(staging / name, files, snapshots) for name, files in plans.items()]
        require(all(sha(path.read_bytes()) == digest for path, digest in snapshots.items()), "Source changed after packaging; staged archives rejected")
        manifest = {"schema": "rhetis.release-manifest/1", "created_utc": datetime.now(timezone.utc).isoformat(), "release_gates": {name: {"ready": report["ready"], "native_cases": report["native_cases"], "elements": len(report["elements"]), "audit_sha256": sha((ROOT / name / "review/validation/release-audit.json").read_bytes())} for name, report in gates.items()}, "archive_count": len(reports), "archives": reports}
        (staging / "release-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        (staging / "png-dimensions.json").write_text(json.dumps({item["file"]: item["png_dimensions"] for item in reports}, ensure_ascii=False, indent=2) + "\n")
        (staging / "SHA256SUMS").write_text("".join(item["sha256"] + "  " + item["file"] + "\n" for item in reports))
        if existing:
            backup = dist / ("previous-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ"))
            backup.mkdir()
            for path in existing:
                shutil.move(str(path), backup / path.name)
        for name in outputs:
            os.replace(staging / name, dist / name)
        for item in reports:
            print(f"{item['file']} {item['bytes']} bytes {item['sha256']} PNG={item['png_count']} CRC=pass", flush=True)
        print(f"PACKAGED: {len(reports)} archives; manifest: {dist / 'release-manifest.json'}", flush=True)
    finally:
        shutil.rmtree(staging, ignore_errors=True)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (RuntimeError, OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        print("PACKAGING BLOCKED: " + str(error), file=sys.stderr)
        sys.exit(1)
