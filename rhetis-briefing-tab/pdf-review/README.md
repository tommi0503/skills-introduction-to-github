# 요소별 검수 PDF

저장소 루트의 `briefing-tab-elements-light.pdf`, `briefing-tab-elements-dark.pdf`는 각각 57페이지입니다. foundation 다음 56개 요소를 이름순으로 수록하고, 요소마다 한 페이지와 북마크를 배정했습니다. 한 요소의 모든 fixture는 해당 페이지에 함께 들어갑니다.

이미 검수한 요소별 PNG를 무손실로 포함했습니다. 페이지 높이는 시트 높이에 맞추며 자르거나 비율을 바꾸지 않습니다. PDF 뷰어에서 ‘너비에 맞춤’으로 보면 작은 글자도 확인할 수 있습니다. 이미지 기반 PDF이므로 본문 텍스트 검색은 지원하지 않습니다. 텍스트 검색이 필요한 fixture별 벡터 PDF는 `briefing-tab-review/library/library-light.pdf`, `library-dark.pdf`에 있습니다.

`python pdf-review/build_element_pdfs.py`로 다시 만듭니다. Pillow, pypdf, reportlab이 필요합니다. `validation.json`에 페이지별 원본 경로·크기, 북마크 수와 파일 해시를 기록했습니다. 최종 PDF의 114개 삽입 이미지가 원본 PNG 픽셀과 모두 일치하는지 확인했습니다.

## 원본·카피 비교 PDF

저장소 루트의 `briefing-tab-compare-replica.pdf`, `briefing-tab-compare-reassembled.pdf`는 각각 11페이지입니다. 왼쪽은 원본, 오른쪽은 원본 재현본 또는 컬렉션 재조립본이며, 상단에 구분과 원본 슬라이드 번호를 표시합니다. 슬라이드20–30 순서로 북마크가 있습니다. 최종 비교 PNG를 무손실로 삽입하고 양쪽 이미지가 각 최종 원본/카피 PNG와 일치하는지도 검사했습니다.

`python pdf-review/build_comparison_pdfs.py`로 다시 만듭니다. Pillow, pypdf, reportlab, fonttools가 필요합니다. 머리글은 동봉된 조선굴림 글꼴을 PDF에 포함합니다. `comparison-validation.json`에 페이지 목록·크기·해시와 원본 픽셀 일치 결과를 기록했습니다.
