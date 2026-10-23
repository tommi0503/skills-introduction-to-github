# 원본·카피 슬라이드 비교 검수 PDF

원본 슬라이드 하나를 PDF 한 페이지에 담았습니다. 위쪽은 **원본 | replica**, 아래쪽은 **원본 | 라이브러리 조립본**입니다. 원본과 각 카피본을 같은 줄에서 직접 비교할 수 있습니다. PDF 책갈피로 덱과 슬라이드를 찾을 수 있습니다.

기존 최종 `compare-replica/`·`compare-reassembled/`의 PNG를 리사이즈하거나 다시 그리지 않고 무손실 삽입했습니다. 확대하여 위치·글자·선·모서리를 확인하세요. 사진·복잡한3D의 회색 대체와 서체·곡률 잔차는 각 덱의 `review-notes.md` 기록을 따릅니다.

| PDF | 페이지 |
|---|---:|
| [전체 통합본](all-collections-slide-comparison.pdf) | 96 |
| [Fluxweave](fluxweave-slide-comparison.pdf) | 18 |
| [Cyanloop](cyanloop-slide-comparison.pdf) | 18 |
| [Roundrise](roundrise-slide-comparison.pdf) | 24 |
| [Nightchamfer](nightchamfer-slide-comparison.pdf) | 18 |
| [Glasspulse](glasspulse-slide-comparison.pdf) | 18 |

[검증 기록](verification.json): 원본96장에 대한 비교 PNG192개를 모두 포함합니다. 각 개별 PDF와 통합 PDF에서 모든 삽입 이미지가 원본 PNG와 픽셀 단위로 일치하고, 페이지 밖으로 잘린 이미지는 없습니다.

재생성: 상위 컬렉션 루트에서 `python slide-comparison-pdfs/build_pdfs.py`.

[업로드된 PDF 6개 실제 재다운로드 검증](download-verification.json)도 통과했습니다.
