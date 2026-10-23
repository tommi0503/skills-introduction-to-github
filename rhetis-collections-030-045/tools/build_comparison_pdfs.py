"""Export approved original | copy comparison PNGs as lossless review PDFs."""
from pathlib import Path
import json
import fitz
from PIL import Image

from build_element_sheets import sha, verify

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "comparison-pdfs"
COLLECTIONS = {
    "030": ("chalkline", 2), "031": ("undertow", 13),
    "033": ("cutplane", 15), "038": ("skylight", 21),
    "043": ("arrowtab", 20), "045": ("blockweave", 19),
}
KINDS = {"replica": "Original | Replica", "reassembled": "Original | Reassembled"}


def save(doc, target, sources, title):
    doc.set_metadata({"title": title, "author": "Rhetis collection review",
                      "subject": "Original on the left; HTML copy on the right; lossless comparison sheets"})
    doc.save(target, garbage=4, deflate=True)
    with fitz.open(target) as saved:
        verify(saved, sources)
        assert len(saved.get_toc()) >= len(saved)
    assert target.stat().st_size < 100 * 1024 ** 2
    print(target.name, len(doc), "pages; lossless image / page bounds verified", flush=True)
    return {"file": target.name, "pages": len(doc), "bytes": target.stat().st_size,
            "sha256": sha(target), "losslessPixels": True, "noImageClipping": True}


def main():
    OUTPUT.mkdir(exist_ok=True)
    all_doc, all_sources, all_toc = fitz.open(), [], []
    by_kind = {kind: {"doc": fitz.open(), "sources": [], "toc": []} for kind in KINDS}
    records = []
    for code, (name, count) in COLLECTIONS.items():
        doc, sources, toc, page_manifest = fitz.open(), [], [], []
        all_offset = len(all_doc)
        all_toc.append([1, f"{code} / {name}", all_offset + 1])
        for kind, title in KINDS.items():
            folder = ROOT / "reviews" / (name + "-review") / ("compare-" + kind)
            images = sorted(folder.glob("*.png"))
            assert len(images) == count
            start = len(doc)
            toc.append([1, title, start + 1])
            for source in images:
                with Image.open(source) as image:
                    assert image.size == (2560, 720)
                page = doc.new_page(width=1280, height=408)
                page.draw_rect(fitz.Rect(0, 0, 1280, 40), color=None, fill=(0.08, 0.08, 0.08))
                page.insert_text((14, 14), f"DECK {code} / {name} / {source.stem}", fontsize=10, color=(1, 1, 1))
                page.insert_text((14, 31), "ORIGINAL", fontsize=11, color=(1, 1, 1))
                page.insert_text((654, 31), "REPLICA" if kind == "replica" else "REASSEMBLED FROM COLLECTION",
                                 fontsize=11, color=(1, 1, 1))
                page.insert_image(fitz.Rect(0, 40, 1280, 400), filename=str(source))
                toc.append([2, source.stem, len(doc)])
                sources.append(source)
                page_manifest.append({"page": len(doc), "kind": kind, "source": str(source.relative_to(ROOT)),
                                      "sourceSHA256": sha(source), "pixels": [2560, 720]})
            group = by_kind[kind]
            offset = len(group["doc"])
            group["toc"].append([1, f"{code} / {name}", offset + 1])
            group["doc"].insert_pdf(doc, from_page=start, to_page=len(doc) - 1)
            group["sources"].extend(images)
            group["toc"].extend([2, source.stem, offset + i + 1] for i, source in enumerate(images))
        assert len(doc) == 2 * count
        doc.set_toc(toc)
        record = save(doc, OUTPUT / (name + "-slide-comparisons.pdf"), sources, code + " " + name + " - slide comparisons")
        record.update(deck=code, collection=name, pageManifest=page_manifest)
        records.append(record)
        all_doc.insert_pdf(doc)
        all_sources.extend(sources)
        all_toc.extend([level + 1, label, number + all_offset] for level, label, number in toc)
        doc.close()
    all_doc.set_toc(all_toc)
    assert len(all_doc) == 180
    records.append(save(all_doc, OUTPUT / "all-slide-comparisons.pdf", all_sources, "All 90 originals - replica and reassembled comparisons"))
    all_doc.close()
    for kind, group in by_kind.items():
        group["doc"].set_toc(group["toc"])
        assert len(group["doc"]) == 90
        records.append(save(group["doc"], OUTPUT / ("original-vs-" + kind + ".pdf"), group["sources"], KINDS[kind] + " - 90 slides"))
        group["doc"].close()
    (OUTPUT / "verification.json").write_text(json.dumps(records, ensure_ascii=False, indent=2))
    rows = "\n".join(f"| {code} · {name} | {2 * count} | [{name}]({name}-slide-comparisons.pdf) |" for code, (name, count) in COLLECTIONS.items())
    (OUTPUT / "README.md").write_text("""# 원본·카피본 슬라이드 비교 검수 PDF

모든 페이지는 왼쪽 원본, 오른쪽 카피본입니다. replica는 독립 HTML 재현본, reassembled는 컬렉션 foundation·요소로 다시 조립한 버전입니다.

- [전체 통합 180페이지](all-slide-comparisons.pdf): 원본 90장에 대한 두 종류 비교를 모두 포함합니다.
- [원본 | replica 90페이지](original-vs-replica.pdf)
- [원본 | 조립본 90페이지](original-vs-reassembled.pdf)

| 덱 · 컬렉션 | PDF 페이지 | 다운로드 |
|---|---:|---|
""" + rows + """

컬렉션별 PDF는 replica 비교 다음에 조립본 비교가 이어집니다. 북마크에서 덱·비교 종류·페이지로 이동할 수 있습니다. 한 PDF 페이지에 비교 이미지 한 장을 통째로 넣어 원본과 카피본을 나란히 확인할 수 있습니다.

최종 검수 PNG를 다시 리샘플링하지 않고 무손실로 삽입했습니다. PDF 내부 이미지를 추출해 원래 PNG의 모든 RGB 픽셀과 일치하고, 페이지 밖으로 잘리지 않는지 자동 확인했습니다. 파일 해시와 이미지 출처는 [verification.json](verification.json)에 있습니다.

재생성: 저장소 폴더에서 `python tools/build_comparison_pdfs.py` (PyMuPDF·Pillow 필요).
""")


if __name__ == "__main__":
    main()
