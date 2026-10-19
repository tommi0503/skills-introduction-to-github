# Rhetis Spectrum 04

첨부 ZIP의 **7개 덱, 82장**을 편집 가능한 HTML·CSS·SVG와 슬라이드 데이터로 재현한 별도 프로젝트입니다. 기존 프로젝트 파일은 수정하지 않았습니다. 컬렉션 이름은 `spectrum-04`입니다.

| 덱 | 참고 이미지 | 수량 |
|---|---|---:|
| 021 폴더링 | slide_02–11 | 10 |
| 022 노랑 회의록 | slide_01–09 | 9 |
| 028 주황 프로모션 | slide_01–18 | 18 |
| 030 블랙 커뮤니티 | slide_01–14 | 14 |
| 031 청소년 범죄 예방 | slide_01–15 | 15 |
| 033 겨울용품 | slide_01–11 | 11 |
| 034 보라 비즈니스 | slide_01–05 | 5 |

ZIP에 없는 덱이나 021의 slide_01은 추가하지 않았습니다. 첨부 README는 사용자가 명시적으로 지정한 제작 계약으로 적용했고, 샘플 디자인은 복제하지 않았습니다. 샘플의 계약 마크업과 fixture 형식을 재사용하고 CSS 디자인은 새로 작성했습니다.

## 보기

- `preview.html`: 원본 재현 82장 전체 미리보기, 개별 PNG·비교·재조립 링크. 압축을 풀고 바로 열 수 있습니다.
- `index.html`: 편집 가능한 슬라이드 UI. 모듈 로딩을 위해 로컬 서버를 사용합니다.
- `light.html`, `dark.html`: 31개 요소와 foundation, 각 89개 fixture 시트.
- `pdf/direct-slides.pdf`, `pdf/assembled-slides.pdf`: 재현·재조립 각각 82페이지. 브라우저에서 직접 인쇄한 텍스트/벡터 PDF입니다.
- `pdf/*-contact-sheets.pdf`: 4장씩 배치한 21페이지 시트, 각 페이지는 1280×720 캔버스입니다.
- `pdf/library-light.pdf`, `pdf/library-dark.pdf`: 각각 89페이지 요소 라이브러리.
- `renders/`: 재현·재조립·라이브러리 PNG. 모두 1280×720입니다.
- `comparisons/direct/final/`: 원본과 최종 재현본을 나란히 놓은 82개 JPEG.
- `review/`: 덱별 실제 시각 검수, 라이브러리 검수, 자동 검사 및 최종 해시 기록.

```bash
npm ci
python -m pip install -r requirements.txt
npm run build
npm run dev
# http://localhost:4173
# ?deck=028&slide=slide_14
# ?deck=028&slide=slide_14&mode=assembled
```

Chromium이 `/usr/bin/chromium`에 필요합니다. Python 검사/패키징은 Pillow, pypdf, reportlab을 사용합니다.

```bash
node scripts/render.mjs --round=final
node scripts/render.mjs --assembled --round=final
node scripts/library-review.mjs
node scripts/export.mjs
python scripts/package.py
npm run verify
```

## 구조와 재조립

`src/primitives.mjs`는 데이터 생성, `src/decks/`는 덱별 레이아웃/콘텐츠, `src/app.mjs`는 DOM 렌더링, `src/app.css`는 뷰어와 페이지별 override를 담당합니다. 원본 이미지 전체를 배경에 깔거나 결과 PNG를 UI로 사용하지 않습니다. Lucide 아이콘과 직접 작성한 단순 SVG를 사용합니다.

`collections/spectrum-04/`는 이미지·외부 리소스 없는 계약 컬렉션입니다. 공통 토큰, foundation, 31개 계약 요소, 89개 fixture를 포함합니다. 핵심 디자인은 028의 오렌지 프레임·둥근 흰 패널·검정 타이포·가는 규칙선이며, 다크 모드는 030의 검정과 라임을 참고해 별도로 설계했습니다. 서로 다른 원본 7덱을 하나의 팔레트로 바꾸지 않고 슬라이드 작성 계층에서 각 덱의 테마와 정밀 좌표를 override합니다.

재조립 모드는 같은 콘텐츠 데이터를 **foundation.page와 card.parts, pill.parts, frame.picture 계약 DOM**으로 조립합니다. 페이지 작성 계층의 override로 원본의 글꼴, 크기, 색, 좌표를 지정하고 SVG/차트 도형을 유지합니다. 이 화면에 쓰이지 않은 관계도·가격표 등의 나머지 계약 요소도 fixture에서 독립적으로 사용할 수 있습니다. 재현본과 재조립본의 82장 PNG를 전부 비교합니다.

## 계약 시트 명령

```bash
python tools/preview.py collections/spectrum-04 contract/type-steps.json --out light.html
python tools/preview.py collections/spectrum-04 contract/type-steps.json --dark --out dark.html
```

제공 도구의 `.frame` 미리보기 래퍼 선택자가 실제 `frame.picture`와 충돌해 도구 복사본에서 `article > .frame`으로 범위를 좁혔습니다. 커맨드와 입력 계약은 그대로입니다. `npm run build`는 시트에 프로젝트 폰트 CSS 링크를 덧붙입니다. 컬렉션 자체에는 `@font-face`, `url()`, 외부 이미지가 없습니다.

## 해석과 차이

- 사진, 복잡한 3D 캐릭터·제품·기기 화면·그래픽은 요청대로 연회색 단색 placeholder입니다. 원본 비율과 자리를 보존합니다.
- 033의 사진 표지는 연회색으로 대체한 뒤 흰 글자가 읽히도록 짙은 갈색으로 바꿨습니다.
- 021의 둥근 제목은 정확한 폰트를 확정할 수 없어 실제 로드한 Jua에 굵기·외곽 효과를 보정했습니다. 본문은 NanumSquareRound를 실제 로드했습니다. 추가 후보 폰트 URL은 404여서 사용하지 않았습니다.
- 작은 글자는 가능한 한 전사하고, 판독이 불확실한 곳은 문맥에 맞는 문장으로 작성했습니다. 덱별 상세 기록은 `review/021.md` 등에서 확인할 수 있습니다. 원본의 PEFORMANCE REPORT 표기도 보존했습니다.
- 요소 최소 칸은 각 fixture 첫 줄에 명시했습니다. 조직도·가격표처럼 정보가 많은 요소는 실제로 견디는 최소 칸을 크게 잡았습니다. funnel 폭은 작은 단계에서도 값과 이름이 읽히도록 최소 가독 폭을 포함해 정규화합니다.
- Rhetis의 실제 importer는 첨부되지 않았으므로 반입 승인까지 실행한 것은 아닙니다. 제공 계약에 대한 로컬 정적 검사와 Chromium 검수 결과를 포함합니다.

폰트는 프로젝트에 로컬 번들하며 라이선스는 `public/fonts/licenses/`에 있습니다. UI 렌더에 네트워크 폰트를 사용하지 않습니다.
