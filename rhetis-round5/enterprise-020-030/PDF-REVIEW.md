# 모든 요소 크기별 검수 PDF

107개 요소와7개 foundation의 라이트·다크 시트를14개 PDF, 총1,272페이지로 제공합니다. 4,744개 fixture/모드/크기 칸을 모두 포함합니다.

| 컬렉션 | 요소+foundation | 전체 칸 | PDF 페이지 | 다운로드 |
|---|---:|---:|---:|---|
| tide-tab | 8+1 | 324 | 82 | [라이트](review/tide-tab/library-light.pdf) · [다크](review/tide-tab/library-dark.pdf) |
| cutfield | 15+1 | 790 | 220 | [라이트](review/cutfield/library-light.pdf) · [다크](review/cutfield/library-dark.pdf) |
| filament | 9+1 | 572 | 144 | [라이트](review/filament/library-light.pdf) · [다크](review/filament/library-dark.pdf) |
| portico | 19+1 | 830 | 212 | [라이트](review/portico/library-light.pdf) · [다크](review/portico/library-dark.pdf) |
| toggle-grid | 13+1 | 522 | 152 | [라이트](review/toggle-grid/library-light.pdf) · [다크](review/toggle-grid/library-dark.pdf) |
| lamella | 30+1 | 1256 | 328 | [라이트](review/lamella/library-light.pdf) · [다크](review/lamella/library-dark.pdf) |
| rulemark | 13+1 | 450 | 134 | [라이트](review/rulemark/library-light.pdf) · [다크](review/rulemark/library-dark.pdf) |

각 fixture는 독립 행이며 모든 크기 칸과 min 표시가 들어갑니다. 긴 행은 칸 경계에서만 나눴고 한 칸을 자르지 않았습니다. 원본 픽셀을 줄이지 않고 RGB/Flate 무손실 이미지로 넣었습니다. 각 PDF의 페이지 머리글과 JSON 색인에 요소/fixture/모드/칸크기가 있습니다.

주 담당자가 각 컬렉션의 라이트·다크 대표 페이지14개를 직접 열었습니다. 전1,272페이지의 PDF 이미지 RGB 해시를 원본 시트에서 자른 strip 해시와 대조했고, PDF에 들어간4,744개 칸의 집합이 최종 QA proof의 칸 집합과 정확히 같음을 확인했습니다. source PNG228개의 SHA256도 최종 시트와 일치합니다.

PDF는 ZIP과 별도의 파일로 제공합니다. 컬렉션별 `review/<collection>/pdf-index.json`에는 페이지별 요소·fixture·크기·min 여부, source PNG SHA256, PDF SHA256/바이트가 있습니다. 이미지와 CSS는 PDF 제작 중 변경하지 않았습니다.
