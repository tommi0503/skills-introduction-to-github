"""Package the approved element PNG sheets as lossless, bookmarked review PDFs."""
from pathlib import Path
import hashlib
import json

import fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "element-sheet-pdfs"
COLLECTIONS = {
    "030": "chalkline", "031": "undertow", "033": "cutplane",
    "038": "skylight", "043": "arrowtab", "045": "blockweave",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(doc, sources):
    assert len(doc) == len(sources)
    for page, source in zip(doc, sources):
        images = page.get_images(full=True)
        assert len(images) == 1
        pix = fitz.Pixmap(doc, images[0][0])
        if pix.n != 3:
            pix = fitz.Pixmap(fitz.csRGB, pix)
        with Image.open(source) as image:
            rgb = image.convert("RGB")
            assert (pix.width, pix.height) == rgb.size
            assert pix.samples == rgb.tobytes(), source
        rectangle = page.get_image_rects(images[0][0])[0]
        assert page.rect.contains(rectangle), source


def main():
    OUTPUT.mkdir(exist_ok=True)
    combined = fitz.open()
    combined_toc, combined_sources, records = [], [], []
    for code, name in COLLECTIONS.items():
        doc, toc, sources, pages = fitz.open(), [], [], []
        folder = ROOT / "reviews" / (name + "-review") / "library"
        elements = sorted(p.name for p in (ROOT / "collections" / name / "elements").iterdir() if p.is_dir())
        assert len(elements) == 56
        offset = len(combined)
        combined_toc.append([1, f"{code} / {name}", offset + 1])
        for mode in ("light", "dark"):
            toc.append([1, mode.title(), len(doc) + 1])
            for element in ["foundation", *elements]:
                source = folder / element / (mode + ".png")
                with Image.open(source) as image:
                    width, height = image.size
                assert width == 1280
                scale = 0.75
                page = doc.new_page(width=width * scale, height=height * scale + 40)
                page.draw_rect(fitz.Rect(0, 0, page.rect.width, 32), color=None, fill=(0.08, 0.08, 0.08))
                page.insert_text((14, 21), f"{code}  {name}  /  {mode.upper()}  /  {element}", fontsize=12, color=(1, 1, 1))
                page.insert_image(fitz.Rect(0, 32, width * scale, 32 + height * scale), filename=str(source))
                toc.append([2, element, len(doc)])
                sources.append(source)
                pages.append({"page": len(doc), "mode": mode, "element": element,
                              "source": str(source.relative_to(ROOT)), "sourceSHA256": sha(source),
                              "pixels": [width, height]})
        doc.set_toc(toc)
        doc.set_metadata({"title": f"{code} {name} - element review sheets", "author": "Rhetis collection review",
                          "subject": "56 elements and foundation; light and dark; lossless approved PNG sheets"})
        target = OUTPUT / (name + "-element-sheets.pdf")
        doc.save(target, garbage=4, deflate=True)
        with fitz.open(target) as saved:
            verify(saved, sources)
            combined.insert_pdf(saved)
        combined_toc.extend([[level + 1, title, number + offset] for level, title, number in toc])
        combined_sources.extend(sources)
        records.append({"collection": name, "deck": code, "file": target.name, "pages": len(doc),
                        "bytes": target.stat().st_size, "sha256": sha(target), "losslessPixels": True,
                        "pageManifest": pages})
        doc.close()
        print(name, "114 pages, embedded image pixels identical", flush=True)
    combined.set_toc(combined_toc)
    combined.set_metadata({"title": "Rhetis - six collections - element review sheets", "author": "Rhetis collection review"})
    target = OUTPUT / "all-collections-element-sheets.pdf"
    combined.save(target, garbage=4, deflate=True)
    combined.close()
    with fitz.open(target) as saved:
        verify(saved, combined_sources)
        assert len(saved) == 684
    records.append({"file": target.name, "pages": 684, "bytes": target.stat().st_size,
                    "sha256": sha(target), "losslessPixels": True})
    (OUTPUT / "verification.json").write_text(json.dumps(records, ensure_ascii=False, indent=2))
    (OUTPUT / "README.md").write_text("""# 요소 시트 검수 PDF

컬렉션마다 foundation 1종과 요소 56종을 각 한 시트씩 담았습니다. 라이트 57장 다음에 다크 57장이 이어져 컬렉션별 114페이지이며, 통합본은 684페이지입니다.

각 시트는 최종 검수 PNG를 자르거나 다시 축소하지 않고 무손실로 넣었습니다. 원래 시트의 모든 fixture가 포함되도록 페이지 높이가 달라집니다. PDF 북마크에서 컬렉션·모드·요소로 이동할 수 있습니다. 조밀한 시트는 확대해서 확인해 주세요.

| 덱 | 컬렉션별 PDF |
|---|---|
""" + "\n".join(f"| {code} | [{name}]({name}-element-sheets.pdf) |" for code, name in COLLECTIONS.items()) +
        "\n\n[전체 통합 PDF](all-collections-element-sheets.pdf) · [이미지 무손실·페이지 수·SHA-256 검증](verification.json)\n")
    print("Combined: 684 pages; all 684 embedded images verified pixel-identical", flush=True)


if __name__ == "__main__":
    main()
