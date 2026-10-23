# Current Fold review

`replica/slide_01.html`부터 `slide_18.html`까지 원본 재현 소스입니다. `reassembled/`는 collection CSS와 계약 마크업으로 조립한 페이지입니다. 각 폴더에 PNG와 PDF가 있습니다.

`library/light.html`, `dark.html`은 전체 시트입니다. `library/<요소>/light.png`, `dark.png`에는 그 요소의 전체 fixture와 최소 칸 뷰가 있습니다. `fonts/`를 함께 보존하면 미리보기에서 실제 Pretendard Variable이 로드됩니다.

이 폴더에서 `python -m http.server 8000`으로 서빙한 뒤 브라우저로 HTML을 여세요. 컬렉션의 원본 CSS·fixture가 바뀌면 상위 저장소의 `contract/`, `tools/`와 인접 `current-fold/` 소스를 두고 `python build_review.py`로 HTML을 다시 만듭니다. 렌더 스크립트는 작업 환경의 Chromium 경로와 HTTP 주소를 사용하므로 다른 환경에서는 주소를 조정해야 합니다.

실제 확인한 항목, 판독과 해석, 미해결 차이는 `review-notes.md`, 자동 검사 결과는 `verification.json` 및 `*-audit.json`에 있습니다. Rhetis 공식 intake를 실행했다고 주장하지 않습니다.
