# Briefing Tab 검수 자료

두 ZIP을 같은 디렉터리에 풀어 `briefing-tab/`과 `briefing-tab-review/`가 나란히 놓이게 하세요. `index.html`을 열면 11장의 원본·replica·컬렉션 조립을 비교할 수 있습니다. 조립 HTML은 이웃한 컬렉션 폴더의 CSS를 직접 읽습니다.

- `replica/`: 독립 재현 HTML/CSS,1280×720 PNG11개,11페이지PDF.
- `compare-replica/`: 원본|replica,2560×720 PNG11개.
- `library/`: 기본 팔레트 라이트·다크 HTML,56개 요소 각각의 두모드 시트PNG,foundation 시트,151페이지 PDF두개. 요소별PNG는1328px폭의세로시트로모든fixture를포함합니다.
- `reassembled/`: 컬렉션foundation·요소만으로조립한HTML,1280×720 PNG11개,11페이지PDF.
- `compare-reassembled/`: 원본|최종조립,2560×720 PNG11개.
- `originals/`: 제공된11개원본이미지.
- `fonts/`: 오프라인미리보기용실제글꼴.
- `review-notes.md`, `design-language.md`, `validation.json`: 차이·판단·실측·검사결과.

라이브러리 시트는 계약의 기준팔레트, 조립본은 원본에서 읽은 팔레트를 사용합니다. `source-theme*.css`는 색·타입토큰 값만 공급하며 새 도형 스타일을 넣지 않습니다. 원본style의낮은대비는원본보존예외로따로기록했고,기준팔레트시트는양모드6776크기조합에서잘림·겹침·대비검사를통과했습니다.

빌드 스크립트와 참조 계약은 GitHub의 `rhetis-briefing-tab/` 소스 폴더에 있습니다. Rhetis 실제 intake 프로그램은 참조팩에 포함되지 않았습니다.
