# Rhetis Spectrum · 098–106

첨부한 6개 덱의 **76장 전체**를 재사용 가능한 컴포넌트와 데이터로 구현한 별도 프로젝트입니다. 기존 프로젝트는 수정하지 않았습니다. 모든 슬라이드는 **1280×720**입니다.

| 덱 | 디자인 | 장 수 | 제공 원본 범위 |
|---|---|---:|---|
| 098 | 파랑과 하늘색 기업 보고서 | 7 | 17–23 |
| 101 | 파랑과 회색 비즈니스 보고서 | 10 | 01–10 |
| 103 | 빨강 연말 성과 보고서 | 10 | 01–10 |
| 104 | 하늘색 수요 분석·사업 제안서 | 19 | 01–19 |
| 105 | 하늘색 SNS 마케팅 제안서 | 10 | 01–10 |
| 106 | 민트 브랜드 마케팅 제안서 | 20 | 01–20 |

099·100·102 및 098의 01–16은 첨부 ZIP에 없으며 새로 만들지 않았습니다. 원본 전체 목록·해시는 [input-inventory.json](review/input-inventory.json)에 있습니다.

## 실행

```sh
npm ci
npm run dev -- --port 4173
# 전체 미리보기: http://127.0.0.1:4173/
# 원본 재현: /?deck=104&slide=01
# 라이브러리 재조립: /?deck=104&slide=01&mode=assembly
npm run build
```

- `src/decks/d*.mjs`: 텍스트·좌표·표·차트 값으로 구성한 덱 데이터. 원본 이미지를 출력 페이지에 사용하지 않습니다.
- `src/primitives.mjs`, `src/renderer.mjs`: 텍스트, 표, 차트, Lucide 아이콘, SVG 등 공통 표현 계층.
- `src/assembly.mjs`: 컬렉션의 card, pill, metric, image-frame, table, chart-bar, chart-donut 구조를 사용하는 별도 DOM 조립기. 도형·SVG는 foundation 장식으로 재사용합니다. 12×6 body의 한 group 안에서 페이지 작성자의 위치·타입 override로 원본 배치를 보존합니다. 이 픽셀 배치는 라이브러리 element.css에 들어가지 않습니다.
- `collection/rhetis-spectrum/`: 키트, foundation, 31개 요소, 요소 fixture 87개와 foundation fixture 2개.
- `contract/README.md`: 사용자 요청에 따라 읽고 적용한 첨부 README 계약 원문.
- `public/references/`: 비교 검수용 원본. 출력 DOM에는 이미지로 삽입하지 않습니다.

## 컬렉션 시트

```sh
python tools/preview.py collection/rhetis-spectrum contract/type-steps.json --out light.html
python tools/preview.py collection/rhetis-spectrum contract/type-steps.json --dark --out dark.html
python scripts/contract-check.py
```

두 시트는 첨부 도구로 생성합니다. 컬렉션에는 외부 폰트·이미지·URL을 넣지 않았습니다. 앱과 최종 렌더는 로컬 패키지의 Pretendard Variable, Noto Sans KR 300–900, Inter Variable을 실제 로드합니다. 컬렉션 시트의 브라우저 캡처에도 동일한 Pretendard를 로드합니다. 폰트 라이선스는 해당 npm 패키지의 OFL을 따릅니다.

각 요소 CSS는 data-el 범위로 제한됩니다. 크기는 type step, 색·타입·여백은 공유 토큰을 사용합니다. 다크 모드는 별도 색상 토큰입니다. fixture의 최소칸은 새 구현으로 검사한 지원 크기입니다. 복잡한 표·다중 요금제는 내용 가독성을 위해 더 큰 최소칸을 요구합니다.

## 브라우저 검수와 산출물

담당별 원본 전체 개별 열람 → 실제 Chromium 렌더 → 원본/결과 개별 비교 → 2–3회 수정/비교 → 주 에이전트 최종 통합 검수 순서로 진행했습니다. 최종 캡처에는 최종 소스 해시와 production 여부를 기록합니다. 자동 검사는 실제 글리프 경계에 대한 잘림·캔버스 초과·chip 광학 중심, 폰트 가용성, 1280×720 크기와 래스터 삽입 여부를 확인합니다.

```sh
node scripts/render.mjs --round=final --mode=clone --production=1 --pdf=1 --url=http://127.0.0.1:4176
node scripts/render.mjs --round=final --mode=assembly --production=1 --pdf=1 --url=http://127.0.0.1:4176
python scripts/compare.py final
npm run verify
```

- `renders/final/clone/`: 원본 재현 PNG 76장.
- `renders/final/assembly/`: 컬렉션 조립 PNG 76장.
- `comparisons/final/`: 원본/재현 좌우 비교 76장.
- `renders/library/`: 라이트·다크 fixture PNG 각각 89장.
- `artifacts/pdf/`: 덱별 및 전체 PDF, 전체 연락처 시트 PDF.
- `artifacts/`: 제출용 컬렉션 ZIP, 전체 결과 ZIP, 소스 ZIP, 정적 미리보기.
- `review/d*.md`: 장별 수정·차이·판독·판단 기록.
- `review/captures/*final*.json`: 최종 자동검사 원본.

## 원본과의 차이와 판단

사진, 인물, 제품 사진, 복잡한 이미지 및 기기 화면은 요청대로 **#e5e5e5 단색 placeholder**입니다. 단순 도형, 표, 차트, 지도와 선형 배경은 HTML/SVG로 그렸습니다. 기기의 단순 외곽은 벡터로 재현했습니다. 원본 자체를 배경으로 깔지 않습니다.

원본에 폰트명이 없어 글자 형태와 폭을 보고 실제 로드 가능한 한국어·영문 폰트를 선정했습니다. 제목의 폭·자간·위치·줄바꿈을 원본과 비교해 조정했습니다. Lucide 치환 아이콘, 브랜드 심볼·서명 벡터, 배경 광택과 일부 부분색 강조에는 세부 차이가 있습니다. 판독할 수 없는 작은 보조문구는 자연스러운 한국어 비즈니스 문장으로 작성했고 장별 기록에 남겼습니다.

신규 요소는 여섯 덱에 공통인 명료한 정보 위계·가는 선·연한 정보 면·강조색과 넓은 여백을 확장했습니다. 파랑을 공통 기본색으로, 민트·코랄을 보조색으로 삼았습니다. samples의 fixture 마크업은 계약 형식 참고용으로 재사용했으며 CSS와 cover 그래픽은 새로 작성했습니다. 축소된 원본의 안티앨리어싱·폰트 자형 차이 때문에 픽셀 동일성을 주장하지 않습니다.
