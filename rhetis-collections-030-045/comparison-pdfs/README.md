# 원본·카피본 슬라이드 비교 검수 PDF

모든 페이지는 왼쪽 원본, 오른쪽 카피본입니다. replica는 독립 HTML 재현본, reassembled는 컬렉션 foundation·요소로 다시 조립한 버전입니다.

- [전체 통합 180페이지](all-slide-comparisons.pdf): 원본 90장에 대한 두 종류 비교를 모두 포함합니다.
- [원본 | replica 90페이지](original-vs-replica.pdf)
- [원본 | 조립본 90페이지](original-vs-reassembled.pdf)

| 덱 · 컬렉션 | PDF 페이지 | 다운로드 |
|---|---:|---|
| 030 · chalkline | 4 | [chalkline](chalkline-slide-comparisons.pdf) |
| 031 · undertow | 26 | [undertow](undertow-slide-comparisons.pdf) |
| 033 · cutplane | 30 | [cutplane](cutplane-slide-comparisons.pdf) |
| 038 · skylight | 42 | [skylight](skylight-slide-comparisons.pdf) |
| 043 · arrowtab | 40 | [arrowtab](arrowtab-slide-comparisons.pdf) |
| 045 · blockweave | 38 | [blockweave](blockweave-slide-comparisons.pdf) |

컬렉션별 PDF는 replica 비교 다음에 조립본 비교가 이어집니다. 북마크에서 덱·비교 종류·페이지로 이동할 수 있습니다. 한 PDF 페이지에 비교 이미지 한 장을 통째로 넣어 원본과 카피본을 나란히 확인할 수 있습니다.

최종 검수 PNG를 다시 리샘플링하지 않고 무손실로 삽입했습니다. PDF 내부 이미지를 추출해 원래 PNG의 모든 RGB 픽셀과 일치하고, 페이지 밖으로 잘리지 않는지 자동 확인했습니다. 파일 해시와 이미지 출처는 [verification.json](verification.json)에 있습니다.

재생성: 저장소 폴더에서 `python tools/build_comparison_pdfs.py` (PyMuPDF·Pillow 필요).
