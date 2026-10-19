# Rhetis Strategy 048–053 · Strategy Blueprint

첨부된 참고 이미지 105장을 편집 가능한 HTML/CSS/SVG와 선언형 데이터로 재구현한 별도 프로젝트입니다. 기존 프로젝트는 수정하지 않습니다. Rhetis 컬렉션은 `strategy-blueprint/`입니다.

| 덱 | 참고 이미지 | 구현 범위 |
|---|---:|---|
| 048 파랑 모던 비즈니스 전략 | 17 | 05–21 |
| 049 회색 심플 전략 | 8 | 01–08 |
| 050 흑백 중간점검 보고서 | 20 | 01–20 |
| 051 파랑 회사소개서 | 20 | 01–20 |
| 052 하늘색 경영 기획서 | 19 | 01–19 |
| 053 파랑 정보 전달 보고서 | 21 | 01–21 |

모든 원본과 결과 슬라이드는 1280×720입니다. 사진·복잡 일러스트·복잡 이미지 로고는 연회색 단색 placeholder이며 원본 이미지를 결과 배경으로 사용하지 않습니다. 표·차트·글자·단순 도형은 실제 DOM/CSS/SVG입니다.

## 바로 보기

- `preview.html`: 직접 구현한 105장 전체. 폰트를 포함한 독립 HTML이라 내려받아 바로 열 수 있습니다.
- `assembled-preview.html`: 컬렉션 계약으로 다시 조립한 105장 전체.
- `light.html`, `dark.html`: 계약 도구로 만든 31개 요소·foundation의 85개 fixture 시트.
- `artifacts/direct-all-105.pdf`, `artifacts/assembled-all-105.pdf`: 각 105페이지의 전체 덱.
- `artifacts/direct-contact-sheets.pdf`, `artifacts/assembled-contact-sheets.pdf`: 덱별 연락처 시트, 각 6페이지.
- `artifacts/direct/`, `artifacts/assembled/`: 모든 개별 PNG와 덱별 PDF.
- `artifacts/comparisons/`: 원본 왼쪽·구현 오른쪽, 총 105개의 비교 JPG.
- `artifacts/library/`: 라이트·다크 170개의 fixture PNG와 최소 칸 검수 자료.
- `reviews/`: 덱별 차이·수정·판독·최종 통합 기록.

## 실행

Node 20 이상, Python 3.10 이상을 사용합니다. 브라우저 렌더에는 Chromium이 필요합니다.

```sh
npm install
npm run build
npm run dev
```

브라우저에서 `http://localhost:4173/?deck=048&slide=048-05`를 엽니다. `mode=assembled`를 추가하면 조립본입니다. `CHROMIUM_PATH`로 Chromium 경로를 지정할 수 있습니다. PDF·검수 후처리에는 Pillow와 PyMuPDF가 필요합니다.

```sh
node tools/render.mjs all direct
node tools/render.mjs all assembled
node tools/quality.mjs
python tools/verify-contract.py
python tools/preview.py strategy-blueprint contract/type-steps.json --out light.html
python tools/preview.py strategy-blueprint contract/type-steps.json --dark --out dark.html
node tools/library-review.mjs
node tools/minimum-review.mjs
python tools/finish-artifacts.py
python tools/verify.py
```

## 구조와 조립 방식

`src/decks/dNNN.js`는 내용·수치·배치 데이터와 덱 내부 반복 패턴을 보관합니다. `src/ui/scene.js`가 공통 도형·텍스트·그룹을 정의하고, `renderer.js`가 직접 구현본을 그립니다. `collection-adapter.js`는 같은 편집 데이터에서 실제 Rhetis `card.parts`, `metric.figure`, `pill.parts`, `frame.picture` 계약 마크업을 생성합니다. 조립본은 컬렉션의 실제 CSS 33개를 로드하고 페이지 수준 `.overrides`로 원본의 좌표·타이포를 보존합니다. 조립 경로는 `artifacts/assembly-trace.json`에서 노드별로 확인할 수 있습니다. 이 105장 조립에 모든 31종 요소를 억지로 쓰지는 않습니다.

컬렉션의 31종은 별도로 완성되어 각각 2개 이상의 fixture와 영문 설명·반응형 CSS·라이트/다크 토큰을 제공합니다. 요소 CSS에는 이미지·외부 리소스·폰트 로딩을 넣지 않았습니다. 실제 폰트 로딩과 정확한 원본 크기 지정은 프레젠테이션 계층에 있습니다. samples/atlas·miri의 디자인은 사용하지 않았습니다.

원본 정확한 폰트 파일은 첨부되지 않았습니다. Pretendard Variable, Black Han Sans, Noto Sans CJK KR의 실제 파일을 포함했으며 자폭·굵기·줄바꿈은 원본과 비교해 조정했습니다. 잔여 획·그림자·파동 위상·세부 아이콘 차이는 `reviews/`에 기록했습니다. 공식 Rhetis importer는 참고 팩에 없어 제공된 계약의 로컬 검증을 수행했습니다.
