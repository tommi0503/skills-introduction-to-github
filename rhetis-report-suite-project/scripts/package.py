#!/usr/bin/env python3
"""Validate final captures and produce the two requested reviewable archives.

Run only after the production final captures have completed:
    python scripts/package.py

The script never edits source, collection files, or reference/comparison images.
An archive over 95 MB stops publication; it is never silently recompressed.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import math
import shutil
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
COLLECTION_ID = "rhetis-report-suite"
PROJECT_ID = "rhetis-report-suite-project"
EXPECTED_PAGES = 121
CANVAS = (1280, 720)
MODES = ("clone", "assembled")
MODE_LABELS = {"clone": "RECREATED", "assembled": "REASSEMBLED"}
ARCHIVES = ("rhetis-report-suite-collection.zip", "rhetis-report-suite-deliverables.zip")
MAX_ARCHIVE_BYTES = 95_000_000
PAYLOAD_PATHS = (
    "src", "package.json", "package-lock.json", "index.html", "README.md", ".gitignore", "light.html", "dark.html", "styles",
    "scripts", "contract", "tools", "review", "collection", "artifacts",
    "renders/final", "comparisons/final",
)
EXCLUDED_DIRS = {"node_modules", "dist", "history", "intermediates", "__pycache__", ".git"}


class PackageError(RuntimeError):
    pass


def log(message: str) -> None:
    print(message, flush=True)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def source_identity() -> dict:
    # Match scripts/state.mjs byte-for-byte: sorted relative path, then contents.
    files = [p for directory in ("src", "collection") for p in (ROOT / directory).rglob("*") if p.is_file()]
    files.extend(ROOT / name for name in ("package.json", "package-lock.json", "index.html"))
    files.sort(key=relative)
    digest = hashlib.sha256()
    records = []
    for path in files:
        if path.is_symlink():
            raise PackageError(f"Source symlinks are not supported: {path}")
        content = path.read_bytes()
        digest.update(relative(path).encode("utf-8"))
        digest.update(content)
        records.append({"path": relative(path), "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest()})
    return {"hash": digest.hexdigest(), "files": len(files), "algorithm": "sha256(path + bytes), sorted paths", "entries": records}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PackageError(message)


def validate_inputs(identity: dict) -> tuple[list, dict, list]:
    inventory = json.loads((ROOT / "review/inventory.json").read_text(encoding="utf-8"))
    require(sum(len(deck["slides"]) for deck in inventory) == EXPECTED_PAGES, "Inventory must contain exactly 121 slides.")
    build_stamp = json.loads((ROOT / "dist/build-state.json").read_text(encoding="utf-8"))
    require(build_stamp["source"]["hash"] == identity["hash"], "Final source does not match the production build.")
    collection = ROOT / "collection" / COLLECTION_ID
    elements = sorted(path for path in (collection / "elements").iterdir() if path.is_dir())
    require(len(elements) == 31, "Collection must contain all 31 element folders.")
    fixture_counts = {path.name: len(list((path / "fixtures").glob("*.html"))) for path in elements}
    require(all(count >= 2 for count in fixture_counts.values()), "Every element must have at least two fixtures.")
    require(sum(fixture_counts.values()) == 77, "Expected 77 element fixtures.")
    require(len(list((collection / "foundation/fixtures").glob("*.html"))) == 2, "Expected two foundation fixtures.")
    contract_report = json.loads((ROOT / "review/contract-check.json").read_text(encoding="utf-8"))
    require(contract_report.get("status") == "passed", "Collection contract validation has not passed.")
    expected = {f"{deck['id']}-{slide}" for deck in inventory for slide in deck["slides"]}
    records, by_mode = [], {mode: [] for mode in MODES}
    for mode in MODES:
        render_dir = ROOT / "renders/final" / mode
        compare_dir = ROOT / "comparisons/final" / mode
        require({p.stem for p in render_dir.glob("*.png")} == expected, f"Incomplete or unexpected {mode} PNG set.")
        require({p.stem for p in compare_dir.glob("*.jpg")} == expected, f"Incomplete or unexpected {mode} comparison set.")
        for deck in inventory:
            capture_path = ROOT / "review/captures" / f"{deck['id']}-final-{mode}.json"
            capture = json.loads(capture_path.read_text(encoding="utf-8"))
            require(capture.get("production") is True, f"Capture is not production: {capture_path.name}")
            require(capture.get("sourceHash") == identity["hash"], f"Stale capture source: {capture_path.name}")
            require(not capture.get("errors") and not capture.get("failedRequests"), f"Capture has browser/network errors: {capture_path.name}")
            captured = {s["id"]: s for s in capture["decks"][0]["slides"]}
            require(set(captured) == set(deck["slides"]), f"Capture slide set differs from inventory: {capture_path.name}")
            for slide_id in deck["slides"]:
                audit = captured[slide_id]
                name = f"{deck['id']}-{slide_id}"
                png = render_dir / f"{name}.png"
                comparison = compare_dir / f"{name}.jpg"
                with Image.open(png) as image:
                    require(image.format == "PNG" and image.size == CANVAS, f"Invalid PNG canvas: {png}")
                    image.verify()
                digest = sha256(png)
                require(digest == audit["sha256"], f"PNG differs from captured manifest: {png}")
                require(audit.get("canvas") == list(CANVAS), f"Browser canvas mismatch: {name}")
                require(audit.get("fontStatus") == "loaded" and all(f.get("available") for f in audit.get("fonts", [])), f"Font loading failed: {name}")
                require(audit.get("embeddedRaster") == 0 and audit.get("placeholdersValid") is True, f"Raster/placeholder check failed: {name}")
                with Image.open(comparison) as image:
                    comparison_size = list(image.size)
                    image.verify()
                item = {"deck": deck["id"], "slide": slide_id, "mode": mode, "title": audit.get("title", slide_id),
                        "png": relative(png), "sha256": digest, "bytes": png.stat().st_size, "size": list(CANVAS),
                        "comparison": relative(comparison), "comparisonSha256": sha256(comparison), "comparisonSize": comparison_size,
                        "findings": audit.get("findings", [])}
                records.append(item)
                by_mode[mode].append(item)
        log(f"Validated {len(by_mode[mode])} {mode} PNGs and comparisons.")
    return inventory, by_mode, records


def font(size: int, bold: bool = False):
    candidates = [Path("/usr/share/fonts/truetype/dejavu") / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"),
                  Path("/usr/share/fonts/truetype/liberation2") / ("LiberationSans-Bold.ttf" if bold else "LiberationSans-Regular.ttf")]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default(size=size)


def slides_pdf(paths: list[Path], output: Path, title: str) -> dict:
    output.parent.mkdir(parents=True, exist_ok=True)
    document = fitz.open()
    document.set_metadata({"title": title, "author": "Rhetis Report Suite", "subject": "1280 × 720 presentation review"})
    for path in paths:
        page = document.new_page(width=CANVAS[0], height=CANVAS[1])
        page.insert_image(page.rect, filename=str(path), keep_proportion=True)
    document.save(str(output), deflate=True, garbage=4)
    document.close()
    with fitz.open(output) as check:
        require(len(check) == len(paths), f"PDF page count mismatch: {output}")
        require(all(abs(page.rect.width - 1280) < .01 and abs(page.rect.height - 720) < .01 for page in check), f"PDF page geometry mismatch: {output}")
    return {"path": relative(output), "pages": len(paths), "pageSizePoints": list(CANVAS), "sha256": sha256(output), "bytes": output.stat().st_size}


def contact_sheet(items: list[dict], output: Path, title: str, page_number: int, total_pages: int) -> None:
    sheet = Image.new("RGB", CANVAS, "#f1f3f5")
    draw = ImageDraw.Draw(sheet)
    draw.text((32, 24), title, font=font(24, True), fill="#162839")
    draw.text((32, 57), f"{page_number:02d} / {total_pages:02d}   |   six slides per review sheet", font=font(13), fill="#617180")
    for index, item in enumerate(items):
        column, row = index % 3, index // 3
        x, y = 32 + column * 412, 91 + row * 289
        with Image.open(ROOT / item["png"]) as image:
            thumbnail = image.convert("RGB").resize((384, 216), Image.Resampling.LANCZOS)
            sheet.paste(thumbnail, (x, y))
        draw.rectangle((x, y, x + 383, y + 215), outline="#c6d0d7", width=1)
        draw.text((x, y + 232), f"{item['deck']} / {item['slide'].replace('_', ' ').upper()}", font=font(16, True), fill="#1c3449")
        draw.text((x, y + 256), MODE_LABELS[item["mode"]], font=font(11), fill="#627485")
    draw.text((32, 690), "RHETIS / REPORT SUITE     1280 x 720     Original images appear only in comparison files.", font=font(11), fill="#687a89")
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, compress_level=9)


def make_contact_sheets(inventory: list, by_mode: dict) -> tuple[list, list]:
    image_records, pdf_records = [], []
    for mode, items in by_mode.items():
        groups = [("all", items)] + [(deck["id"], [item for item in items if item["deck"] == deck["id"]]) for deck in inventory]
        for group_id, members in groups:
            directory = ROOT / "artifacts/contact-sheets" / mode / group_id
            sheets = []
            count = math.ceil(len(members) / 6)
            title = f"RHETIS REPORT SUITE  /  {MODE_LABELS[mode]}  /  {'ALL DECKS' if group_id == 'all' else 'DECK ' + group_id}"
            for index in range(count):
                output = directory / f"{group_id}-{index + 1:02d}.png"
                subset = members[index * 6:(index + 1) * 6]
                contact_sheet(subset, output, title, index + 1, count)
                sheets.append(output)
                image_records.append({"path": relative(output), "mode": mode, "deck": group_id, "slides": [f"{x['deck']}/{x['slide']}" for x in subset], "size": list(CANVAS), "sha256": sha256(output)})
            pdf_records.append(slides_pdf(sheets, directory / "contact-sheets.pdf", title))
        log(f"Created {mode} deck and full contact sheets.")
    return image_records, pdf_records


def poster(items: list[dict], output: Path, label: str) -> None:
    columns, cell_w, cell_h = 5, 312, 206
    rows = math.ceil(len(items) / columns)
    canvas = Image.new("RGB", (1600, 104 + rows * cell_h), "#f1f3f5")
    draw = ImageDraw.Draw(canvas)
    draw.text((24, 22), f"RHETIS REPORT SUITE / {label}", font=font(28, True), fill="#163149")
    draw.text((24, 64), f"{len(items)} slides  |  5 decks  |  1280 x 720 native canvases", font=font(15), fill="#65798b")
    for index, item in enumerate(items):
        x, y = 24 + (index % columns) * cell_w, 104 + (index // columns) * cell_h
        with Image.open(ROOT / item["png"]) as image:
            canvas.paste(image.convert("RGB").resize((288, 162), Image.Resampling.LANCZOS), (x, y))
        draw.rectangle((x, y, x + 287, y + 161), outline="#c5d1da")
        draw.text((x, y + 174), f"{item['deck']} / {item['slide'].replace('_', ' ').upper()}", font=font(12, True), fill="#28475e")
    canvas.save(output, quality=92, optimize=True, subsampling=0)


def preview_html(inventory: list, by_mode: dict, output: Path) -> None:
    indexed = {(x["deck"], x["slide"], mode): x for mode, items in by_mode.items() for x in items}
    sections = []
    for deck in inventory:
        cards = []
        for slide_id in deck["slides"]:
            clone = indexed[(deck["id"], slide_id, "clone")]
            title = html.escape(clone["title"])
            figures = []
            for mode, korean in (("clone", "원본 재현"), ("assembled", "라이브러리 재조립")):
                item = indexed[(deck["id"], slide_id, mode)]
                png = "../" + item["png"]
                comparison = "../" + item["comparison"]
                figures.append(f'<figure class="{mode}"><a href="{png}" target="_blank"><img src="{png}" width="1280" height="720" loading="lazy" alt="{deck["id"]} {slide_id} {korean}"></a><figcaption>{korean} · <a href="{png}" target="_blank">PNG</a> · <a href="{comparison}" target="_blank">원본과 개별 비교</a></figcaption></figure>')
            cards.append(f'<article class="slide-card" data-search="{html.escape(deck["id"] + " " + slide_id + " " + clone["title"], quote=True)}"><h3>{deck["id"]} / {slide_id} · {title}</h3><div class="pair">{"".join(figures)}</div></article>')
        sections.append(f'<section id="deck-{deck["id"]}" class="deck"><h2>{html.escape(deck["label"])}</h2><p>{len(deck["slides"])}장 · <a href="contact-sheets/clone/{deck["id"]}/contact-sheets.pdf">재현 시트 PDF</a> · <a href="contact-sheets/assembled/{deck["id"]}/contact-sheets.pdf">재조립 시트 PDF</a></p>{"".join(cards)}</section>')
    document = '''<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Rhetis Report Suite — 121 슬라이드 미리보기</title>
<style>*{box-sizing:border-box}body{margin:0;background:#eef2f5;color:#172e41;font-family:system-ui,-apple-system,sans-serif}header,main{max-width:1560px;margin:auto;padding:32px}header{padding-bottom:10px}h1{font-size:32px;margin:12px 0}p{line-height:1.7}a{color:#185e9b}nav{display:flex;gap:14px;flex-wrap:wrap}button,input{font:inherit;padding:10px 14px;border:1px solid #b8c7d4;border-radius:7px;background:white;color:inherit}button{cursor:pointer}button.active{background:#183c57;color:white}.controls{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}.deck{margin:36px 0 60px}.slide-card{padding:18px;margin:18px 0;background:white;border:1px solid #d5dee6;border-radius:10px}h3{margin:0 0 16px;font-size:17px}.pair{display:grid;grid-template-columns:1fr 1fr;gap:20px}figure{margin:0;min-width:0}img{display:block;width:100%;height:auto;aspect-ratio:16/9;border:1px solid #d2dce4}figcaption{font-size:13px;margin-top:9px}body[data-view="clone"] figure.assembled,body[data-view="assembled"] figure.clone{display:none}body:not([data-view="both"]) .pair{grid-template-columns:1fr}.hidden{display:none}@media(max-width:820px){header,main{padding:18px}.pair{grid-template-columns:1fr}h1{font-size:25px}}</style>
<body data-view="both"><header><p>RHETIS / REFERENCE → COMPONENTS → REASSEMBLY</p><h1>121개 슬라이드 전체 미리보기</h1><p>설치나 서버 없이 이 HTML을 열어 모든 PNG와 개별 원본 비교 이미지를 확인할 수 있습니다. 모든 슬라이드는 1280×720입니다. 복잡한 인물·이미지 삽화는 연한 회색 placeholder로 처리했습니다.</p>
<nav><a href="pdfs/recreated-slides.pdf">원본 재현 PDF (121장)</a><a href="pdfs/reassembled-slides.pdf">재조립 PDF (121장)</a><a href="contact-sheets/clone/all/contact-sheets.pdf">전체 재현 시트 PDF</a><a href="contact-sheets/assembled/all/contact-sheets.pdf">전체 재조립 시트 PDF</a><a href="preview.jpg">재현 전체 이미지</a><a href="preview-assembled.jpg">재조립 전체 이미지</a><a href="../collection/rhetis-report-suite/preview-light.html">31개 요소 · Light</a><a href="../collection/rhetis-report-suite/preview-dark.html">Dark</a></nav>
<div class="controls"><button data-view="both" class="active">나란히 보기</button><button data-view="clone">원본 재현</button><button data-view="assembled">라이브러리 재조립</button><input id="search" type="search" placeholder="덱·슬라이드·제목 검색" aria-label="슬라이드 검색"></div></header><main>''' + "".join(sections) + '''</main><script>document.querySelectorAll('button[data-view]').forEach(b=>b.onclick=()=>{document.body.dataset.view=b.dataset.view;document.querySelectorAll('button[data-view]').forEach(x=>x.classList.toggle('active',x===b))});document.getElementById('search').oninput=e=>{const q=e.target.value.toLowerCase();document.querySelectorAll('.slide-card').forEach(c=>c.classList.toggle('hidden',!c.dataset.search.toLowerCase().includes(q)));document.querySelectorAll('.deck').forEach(d=>d.classList.toggle('hidden',![...d.querySelectorAll('.slide-card')].some(c=>!c.classList.contains('hidden'))))};</script></body></html>'''
    output.write_text(document, encoding="utf-8")


def payload_files() -> list[Path]:
    files = set()
    for name in PAYLOAD_PATHS:
        path = ROOT / name
        candidates = [path] if path.is_file() else path.rglob("*") if path.exists() else []
        for candidate in candidates:
            if not candidate.is_file():
                continue
            rel = candidate.relative_to(ROOT)
            if any(part in EXCLUDED_DIRS for part in rel.parts) or candidate.suffix in {".pyc", ".pyo"} or candidate.name == ".DS_Store":
                continue
            if rel.parts[:2] == ("artifacts", "downloads"):
                continue
            require(not candidate.is_symlink(), f"Payload symlink: {candidate}")
            files.add(candidate)
    return sorted(files, key=relative)


def write_archive(output: Path, files: list[Path], base: Path, prefix: str) -> dict:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9, allowZip64=True) as archive:
        archive.writestr(prefix + "/", b"")
        for path in files:
            archive.write(path, prefix + "/" + path.relative_to(base).as_posix())
    with zipfile.ZipFile(output) as archive:
        require(archive.testzip() is None, f"ZIP CRC failed: {output}")
        require({name.split("/")[0] for name in archive.namelist()} == {prefix}, f"ZIP top-level structure failed: {output}")
        count = len(archive.infolist())
    return {"name": output.name, "bytes": output.stat().st_size, "sha256": sha256(output), "entries": count, "crc": "passed", "topLevel": prefix + "/"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-only", action="store_true", help="Validate final source/render inputs without generating or packaging files.")
    parser.add_argument("--reuse-artifacts", action="store_true", help="Reuse existing PDF/sheet/preview artifacts after validating their recorded hashes.")
    parser.add_argument("--output-dir", type=Path, help="Also copy archives to this optional directory. The default destination is artifacts/downloads.")
    arguments = parser.parse_args()
    identity = source_identity()
    inventory, by_mode, render_records = validate_inputs(identity)
    if arguments.check_only:
        log(f"Preflight passed: {EXPECTED_PAGES} slides per mode, source {identity['hash']}")
        return 0
    started = datetime.now(timezone.utc).isoformat()
    artifacts = ROOT / "artifacts"
    artifacts.mkdir(parents=True, exist_ok=True)
    if arguments.reuse_artifacts:
        previous = json.loads((ROOT / "review/artifact-manifest.json").read_text(encoding="utf-8"))
        require(previous["sourceHash"] == identity["hash"], "Existing artifacts belong to a different source revision.")
        for record in previous["pdfs"] + previous["contactSheets"] + previous["previews"]:
            require(sha256(ROOT / record["path"]) == record["sha256"], f"Artifact hash mismatch: {record['path']}")
        pdf_records, sheet_records = previous["pdfs"], previous["contactSheets"]
        sheet_pdfs = [record for record in pdf_records if "/contact-sheets/" in record["path"]]
        log("Reusing verified PDF, contact-sheet, and poster artifacts.")
    else:
        pdf_records = []
        for mode, filename in (("clone", "recreated-slides.pdf"), ("assembled", "reassembled-slides.pdf")):
            pdf_records.append(slides_pdf([ROOT / item["png"] for item in by_mode[mode]], artifacts / "pdfs" / filename, f"Rhetis Report Suite / {MODE_LABELS[mode]} / 121 slides"))
            log(f"Created {filename}: 121 pages, 1280 x 720 points.")
        sheet_records, sheet_pdfs = make_contact_sheets(inventory, by_mode)
        pdf_records.extend(sheet_pdfs)
        poster(by_mode["clone"], artifacts / "preview.jpg", "RECREATED / ALL 121 SLIDES")
        poster(by_mode["assembled"], artifacts / "preview-assembled.jpg", "REASSEMBLED / ALL 121 SLIDES")
    preview_html(inventory, by_mode, artifacts / "preview.html")
    (artifacts / "README.md").write_text("# Rhetis Report Suite\n\nOpen `preview.html` directly in a browser; no installation is needed for the static review.\n\n- `pdfs/recreated-slides.pdf`: all 121 source recreations, 1280×720 points per page.\n- `pdfs/reassembled-slides.pdf`: all 121 genuine contract-component reassemblies.\n- `contact-sheets/`: six slides per 1280×720 sheet, per deck and full set, in PNG and PDF.\n- `preview.jpg`, `preview-assembled.jpg`: full-set posters.\n- `../renders/final/`: every native PNG.\n- `../comparisons/final/`: every individual original/result comparison.\n- `../review/`: source identity, render hashes, browser checks, contract checks, and visual review records.\n\nThe collection ZIP has exactly one top-level folder, `rhetis-report-suite/`. The source-deliverable ZIP has exactly one top-level folder, `rhetis-report-suite-project/`. Detailed original artwork is replaced by flat light gray placeholders according to the requested scope. Reference PNG originals are excluded from the source ZIP; comparisons retain the originals alongside rendered results.\n", encoding="utf-8")
    write_json(ROOT / "review/source-identity.json", {"createdAt": started, **identity})
    write_json(ROOT / "review/render-manifest.json", {"sourceHash": identity["hash"], "nativeCanvas": list(CANVAS), "modes": {mode: len(items) for mode, items in by_mode.items()}, "renders": render_records})
    write_json(ROOT / "review/artifact-manifest.json", {"sourceHash": identity["hash"], "pdfs": pdf_records, "contactSheets": sheet_records,
              "previews": [{"path": relative(artifacts / name), "sha256": sha256(artifacts / name)} for name in ("preview.jpg", "preview-assembled.jpg", "preview.html")]})
    findings = [{"deck": item["deck"], "slide": item["slide"], "mode": item["mode"], **finding} for item in render_records for finding in item["findings"]]
    write_json(ROOT / "review/package-preflight.json", {"status": "passed", "sourceHash": identity["hash"], "pagesPerMode": EXPECTED_PAGES, "allPngSize": list(CANVAS), "collectionElements": 31,
              "elementFixtures": 77, "foundationFixtures": 2, "nativePdfs": 2, "contactSheetPngs": len(sheet_records), "contactSheetPdfs": len(sheet_pdfs), "browserFindings": findings,
              "noReferencePngsInSourceZip": True, "noSourceOrCollectionEdits": True})
    require(source_identity()["hash"] == identity["hash"], "Source changed during packaging; stop and regenerate the final captures.")
    manifest_path = artifacts / "manifest.sha256"
    files = [path for path in payload_files() if path != manifest_path]
    manifest_path.write_text("".join(f"{sha256(path)}  {relative(path)}\n" for path in files), encoding="utf-8")
    files = payload_files()
    staging = ROOT / "work/package"
    collection_root = ROOT / "collection" / COLLECTION_ID
    collection_files = sorted(path for path in collection_root.rglob("*") if path.is_file())
    archive_records = [write_archive(staging / ARCHIVES[0], collection_files, collection_root, COLLECTION_ID),
                       write_archive(staging / ARCHIVES[1], files, ROOT, PROJECT_ID)]
    oversize = [record for record in archive_records if record["bytes"] > MAX_ARCHIVE_BYTES]
    if oversize:
        write_json(staging / "oversize.json", {"status": "requires-main-review", "thresholdBytes": MAX_ARCHIVE_BYTES, "archives": archive_records, "comparisonImagesReencoded": False})
        raise PackageError("ARCHIVE OVER 95 MB: notify the main agent before any quality-84 comparison re-encoding. No original/comparison images were changed. " + json.dumps(oversize, ensure_ascii=False))
    # Verify SHA-256 entries through the resulting source ZIP, in addition to CRC.
    with zipfile.ZipFile(staging / ARCHIVES[1]) as archive:
        for line in manifest_path.read_text(encoding="utf-8").splitlines():
            expected_hash, name = line.split("  ", 1)
            require(hashlib.sha256(archive.read(PROJECT_ID + "/" + name)).hexdigest() == expected_hash, f"Archived SHA-256 mismatch: {name}")
    require(source_identity()["hash"] == identity["hash"], "Source changed during archive creation.")
    destinations = {artifacts / "downloads"}
    if arguments.output_dir:
        destinations.add(arguments.output_dir.resolve())
    integrity = {"status": "passed", "sourceHash": identity["hash"], "nativePngs": 242, "comparisons": 242, "pagesPerMode": 121, "archives": archive_records, "comparisonImagesReencoded": False}
    for destination in destinations:
        destination.mkdir(parents=True, exist_ok=True)
        for record in archive_records:
            target = destination / record["name"]
            shutil.copy2(staging / record["name"], target)
            require(sha256(target) == record["sha256"], f"Copied ZIP hash mismatch: {target}")
        (destination / "SHA256SUMS.txt").write_text("".join(f"{record['sha256']}  {record['name']}\n" for record in archive_records), encoding="utf-8")
        write_json(destination / "package-integrity.json", integrity)
    log(json.dumps(integrity, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (PackageError, FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Packaging stopped: {error}", file=sys.stderr, flush=True)
        sys.exit(2)
