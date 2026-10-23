# 요소별 검수 PDF

각 페이지는 요소 하나의 라이트·다크 시트를 나란히 담습니다. 컬렉션별 56개 요소와 foundation을 포함하며, PDF 책갈피로 컬렉션·요소를 바로 찾을 수 있습니다. 모든 fixture가 담긴 기존 최종 시트 PNG를 다시 그리거나 리사이즈하지 않고 무손실 삽입했습니다. 작은 문구는 PDF를 확대해 확인하세요.

| 파일 | 페이지 | 구성 |
|---|---:|---|
| [전체 통합 PDF](all-collections-element-sheets.pdf) | 285 | 5개 컬렉션 전체 |
| [Fluxweave](fluxweave-element-sheets.pdf) | 57 | 56요소 + foundation |
| [Cyanloop](cyanloop-element-sheets.pdf) | 57 | 56요소 + foundation |
| [Roundrise](roundrise-element-sheets.pdf) | 57 | 56요소 + foundation |
| [Nightchamfer](nightchamfer-element-sheets.pdf) | 57 | 56요소 + foundation |
| [Glasspulse](glasspulse-element-sheets.pdf) | 57 | 56요소 + foundation |

각 개별 PDF와 통합 PDF의 모든 삽입 이미지가 원본 PNG와 픽셀 단위로 같은지 검사했고, 페이지 밖으로 잘린 시트는 없습니다. [검증 기록](verification.json)에 파일별 SHA-256, 페이지 수, 원본 시트 목록을 담았습니다.

재생성: `python element-review-pdfs/build_pdfs.py` (상위 컬렉션 루트 기준). 기존 컬렉션·ZIP·replica·재조립 페이지는 변경하지 않았습니다.
