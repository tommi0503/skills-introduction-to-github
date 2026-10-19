# Report Forge — 프레젠테이션 재현과 Rhetis 컬렉션

첨부한 7개 덱의 112개 참고 이미지를 별도 프로젝트에 구현했습니다. 원본 재현본과 Rhetis 컬렉션을 사용한 독립 조립본은 서로 다른 결과물입니다. 기존 저장소의 작업은 변경하지 않았습니다.

| 덱 | 범위 | 장수 |
|---|---|---:|
| 053 | 22–30 | 9 |
| 054 | 01–20 | 20 |
| 056 | 01–20 | 20 |
| 057 | 01–11 | 11 |
| 058 | 01–20 | 20 |
| 060 | 01–30 | 30 |
| 061 | 01–02 | 2 |

## 먼저 볼 파일

- `outputs/preview.html`: 원본 재현본 전체 미리보기. 덱 필터, 클릭 확대, 방향키 이동을 지원합니다. 폰트를 내장하여 서버 없이 열 수 있습니다.
- `outputs/assembled.html`: 컬렉션으로 다시 조립한 112장. 원본 페이지의 텍스트·데이터를 계약 요소에 재배치했습니다. 원본의 픽셀 배치를 그대로 유지하는 두 번째 복제품은 아닙니다.
- `outputs/light.html`, `outputs/dark.html`: foundation 2개와 요소 fixture 87개, 모드별 89장.
- `pdfs/replica-slides.pdf`, `assembled-slides.pdf`: 한 페이지에 한 슬라이드, 각각 112페이지.
- `pdfs/replica-sheets.pdf`, `assembled-sheets.pdf`: 4장씩 모은 28페이지 시트.
- `pdfs/library-light.pdf`, `library-dark.pdf`: 각 89페이지 요소 시트.
- `renders/`: 재현본 112 PNG, 조립본 112 PNG, 라이브러리 178 PNG. 모두 1280×720입니다.
- `sheets/`: 재현본/조립본의 4장씩 모은 시트 PNG, 각 28개, 모두 1280×720입니다.
- `comparisons/`: 원본과 최종 재현본을 좌우로 배치한 112개 JPG.
- `review/verification.json`: 자동 최종 검사. 개별 비교 기록은 `review/deckNNN-review.md`, 통합 기록은 `review/FINAL-REVIEW.md`입니다.
- `collection/report-forge/`: kit, foundation, 요소 31개. 별도 `report-forge.zip`의 최상위 폴더도 `report-forge/` 하나입니다.

## 구현과 실행

React/TypeScript + Vite, Lucide 아이콘을 사용합니다. `src/ui/`의 공통 컴포넌트와 `src/decks/`의 덱별 데이터/구성으로 나누었습니다. 사진·3D·복잡한 그래픽은 연한 회색 placeholder이며 단순 도형과 차트는 DOM/SVG로 구현했습니다. 원본 전체 이미지는 재현 화면에 사용하지 않았습니다. `public/reference/`의 이미지는 비교 자료로만 포함합니다.

```sh
npm ci
npm run dev
npm run typecheck
npm run build
```

빌드 시 standalone 미리보기와 PDF도 `dist/outputs/`·`dist/pdfs/`에 복사하므로 프로덕션 앱의 링크가 연결됩니다. 개별 슬라이드 PDF는 텍스트를 유지하며, 4-up 시트 PDF는 PNG를 모은 이미지 시트입니다.

Node 22 이상과 Python 3을 권장합니다. 검수 스크립트는 Chromium(`/usr/bin/chromium`), Python Pillow·PyMuPDF·reportlab이 필요합니다. 브라우저 검수에는 개발 서버가 실행되어 있어야 합니다.

```sh
# 참고팩 원본 도구로 시트 생성
python tools/preview.py collection/report-forge contract/type-steps.json --out light.html
python tools/preview.py collection/report-forge contract/type-steps.json --dark --out dark.html
# 컬렉션 최신 CSS로 독립 조립 및 감사
npm run assemble
# 원본 최종 PNG, 폰트 내장 미리보기, 전체 PDF
npm run export
python scripts/compare.py
python scripts/sheets.py
npm run verify
```

참고팩의 preview 도구는 변경하지 않았습니다. 납품용 `outputs/light.html`·`dark.html`에는 preview 생성 후 문서 레벨에 Pretendard를 내장했습니다. 컬렉션 CSS에는 외부 폰트나 이미지 URL이 없습니다. 시트를 다시 생성하면 이 문서 레벨 내장 폰트는 없어지며 설치 폰트로 대체될 수 있습니다.

## 계약과 판단

사용자가 계약으로 지정한 첨부 README를 먼저 끝까지 읽고 그 계약을 적용했습니다. 원문은 `contract/REFERENCE-README.md`입니다. samples의 구조·클래스·fixture 형식만 참고했으며 디자인은 원본 이미지의 보고서 언어에서 구성했습니다. 컬렉션은 64개 공유 토큰, light/dark 색, 12×6 foundation, 요소 31개와 서로 다른 fixture를 갖습니다. Rhetis 서비스로 실제 반입한 것은 아니며 로컬 계약/렌더 검증 결과를 제공합니다.

원본 폰트 파일이 없어 Pretendard, Noto Sans CJK KR 및 Arial 호환 Liberation Sans를 로드했습니다. 영문 자폭과 일부 한국어 줄바꿈은 원본과 차이가 있습니다. 판독이 어려운 작은 문구는 자연스러운 한국어로 보완하고 덱별 검수 기록에 적었습니다. 060-08의 옅은 보조 계열은 이미지에서 읽은 값으로 재구성했습니다. 조립본의 일부 복합 차트는 주요 계열을 그래프로, 나머지 축/수치/설명을 보조 영역으로 보존합니다.

폰트 라이선스는 `public/fonts/`에 포함했습니다. 참고 이미지의 권리는 원저작자에게 있습니다.

## 배포 파일

- [전체 납품 ZIP](../rhetis-report-forge-delivery.zip): 소스, 재현/조립 PNG, 원본 비교, 시트, PDF, 미리보기, 검수 기록.
- [컬렉션 ZIP](../report-forge.zip): 최상위 `report-forge/` 하나만 포함한 Rhetis 컬렉션.
- ZIP 해시는 저장소 루트 `rhetis-report-forge-archives.json`, GitHub 재다운로드 검증은 `rhetis-report-forge-github-verification.json`에서 확인합니다.
