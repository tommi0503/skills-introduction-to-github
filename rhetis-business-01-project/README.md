# Rhetis Business 01

첨부 참고 이미지 **5개 덱·105장**을 별도 프로젝트로 재현하고, 같은 디자인 언어의 Rhetis 컬렉션 **`rhetis-business-01`**을 제작했습니다. 기존 저장소의 프레젠테이션 프로젝트는 보존했습니다. 모든 슬라이드와 fixture PNG는 **1280×720**입니다.

| 덱 | 원본 | 장수 |
|---|---|---:|
| d01 | 초록 깔끔 고객 세미나 기획서 | 18 |
| d02 | 파랑 모던 제안 기획서 | 30 |
| d03 | 사업보고서용 프레젠테이션 | 20 |
| d04 | 빨강 깔끔 대행사 결과 보고서 | 30 |
| d05 | 하늘색 깔끔 비즈니스 보고서 | 7 |

## 결과물

- `deliverables/rhetis-business-01.zip`: **최상위 `rhetis-business-01/` 폴더 하나만** 포함하는 라이브러리 컬렉션.
- `deliverables/rhetis-business-01-renders.zip`: 재현 PNG 105장, 재조립 PNG 105장, 라이브러리 PNG 158장, 원본/결과 비교 JPG 105장, 전체 미리보기, PDF와 검수 기록.
- `deliverables/rhetis-business-01-source.zip`: 실행 가능한 소스, 로컬 폰트, 비교용 원본, 계약, 컬렉션, 공식 라이트·다크 시트.
- `deliverables/clone-slides.pdf`, `assembled-slides.pdf`: 각각 105페이지의 재현본·라이브러리 재조립본. 덱별 PDF와 라이트·다크 라이브러리 PDF는 `deliverables/pdf/`.
- 렌더 ZIP을 풀고 `preview.html`을 열면 서버 없이 전체 이미지와 비교 화면을 볼 수 있습니다.

## 실행

Node.js 20+, Python 3, Chromium이 필요합니다. Python 내보내기·패키징에는 Pillow와 pypdf, 계약 검사에는 표준 라이브러리만 사용합니다.

```sh
npm ci
npm run dev
# http://127.0.0.1:4173
```

다른 터미널에서:

```sh
python tools/preview.py rhetis-business-01 contract/type-steps.json --out light.html
python tools/preview.py rhetis-business-01 contract/type-steps.json --dark --out dark.html
python scripts/validate-collection.py
npm run build
npm run render -- --round=final
npm run render -- --round=final --mode=assembled
node scripts/render-collection.mjs
python scripts/compare.py final
node scripts/export.mjs
python scripts/package.py
npm run verify
```

`#/slide/d01/s01`은 개별 재현 슬라이드, `?mode=assembled#/slide/d01/s01`은 재조립 슬라이드입니다. `#/compare/d01`은 원본 나란히 비교, `#/assembled/d01`은 재조립 덱입니다. `npm run build`는 모든 데이터의 수량·좌표를 검증하고 배포용 정적 파일을 `dist/`에 만듭니다.

## 구현 구조

- `src/primitives.js`: 직렬화 가능한 텍스트·도형·placeholder·벡터·Lucide·표·차트 생성 함수.
- `src/decks/d01.js`~`d05.js`: 원본별 콘텐츠와 레이아웃 데이터. 공통 헤더·프레임·카드·차트는 덱 내부 함수로 재사용합니다.
- `src/renderer.js`: 공통 DOM 렌더링. 원본 이미지는 이 렌더러의 슬라이드 배경이나 기판으로 사용하지 않습니다.
- `src/assembly.js`: 컬렉션 CSS를 로드해 실제 정보 블록을 `card.parts`, `pill.parts`, `frame`으로 묶는 재조립 어댑터. Foundation의 `page/head/title/body`와 12×6 grid 슬롯을 사용합니다. 슬롯 내부에 원본 좌표를 보정합니다. 모든 원본 노드를 한 번씩 보존하며, 복잡한 SVG 차트·표와 작은 장식은 편집 가능한 페이지 벡터로 유지합니다.
- `rhetis-business-01/`: 공유 토큰, foundation, 계약의 31개 요소와 79개 fixture. CSS에 외부 리소스나 폰트 URL을 넣지 않았습니다. 요소마다 `data-el` 범위를 지정했습니다.
- `public/reference/`: 비교 화면에서만 읽는 원본 이미지와 SHA-256 목록.
- `review/`: 덱별 판단, 실제 브라우저 검사, 주 에이전트 통합 검수, 최종 파일 검증.

재조립 어댑터는 덱별 팔레트를 페이지 토큰으로 공급하며, 미세한 원본값은 `--reference-*` 보정값으로 표현합니다. 글자 역할 토큰과 공유 색 토큰을 바꾸면 재조립 결과도 반응합니다. 복잡한 차트·표 전체를 각각의 Rhetis 차트·표 계약으로 자동 변환하는 기능까지 포함하지는 않습니다.

## 폰트와 남는 차이

원본 PNG에는 폰트 메타데이터가 없어 정확한 서체명은 확정하지 못했습니다. 실제 로컬 파일을 로드하는 Pretendard 가변 폰트와 Oswald Bold를 사용하고 크기·굵기·자간·행간·줄바꿈을 조정했습니다. 표지의 Arial 요청은 메트릭이 호환되는 Liberation Sans Bold, 장식 인용부호의 Georgia 요청은 Noto Serif Bold를 명시적으로 번들·로드해 환경에 따른 대체를 고정했습니다. 라이선스는 `public/fonts/`에 포함합니다.

사진·인물·기기·지도·복잡한 이미지 아이콘은 요청대로 연회색 단색 placeholder입니다. 단순 도형·선·표·차트·벡터 배경과 Lucide 아이콘은 직접 구현했습니다. 일부 복합 아이콘·로고·종이/바인더의 질감과 그림자는 단순화했습니다. 판독이 어려운 작은 문구는 자연스러운 한국어로 보완했고 덱별 기록에 남겼습니다. 20/30주년, 도넛 합계 110% 등 원본 자체의 모순은 임의로 정정하지 않았습니다.

선 차트 fixture의 연결선은 CSS Anchor Positioning을 사용하므로 이를 지원하는 최신 Chromium이 필요합니다. Rhetis 공식 importer는 이 자료에 포함되어 있지 않아 실행하지 않았으며, 제공된 계약 기준의 정적 검사와 실제 Chromium 검사를 수행했습니다.

첨부 README는 사용자가 제작 계약으로 지정한 문서로 보존했고(`contract/REFERENCE-README.md`), 샘플 atlas/miri는 구조·클래스·fixture 형식만 참고했습니다.
