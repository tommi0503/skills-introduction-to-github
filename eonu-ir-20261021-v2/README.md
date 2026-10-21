# EONU IR — v2

최신 MD를 기준으로 기획을 보완한 **와이어프레임 12장 + 디자인 시안 12장**입니다. 기존 `eonu-ir-20261021`과 프레젠테이션 작업은 보존하고 새 폴더에서 다시 구성했습니다.

## 열어보기

ZIP 전체를 압축 해제한 뒤 `index.html`을 브라우저에서 여세요. 모든 폰트·CSS·JavaScript는 폴더 안에 포함되어 있습니다. CDN, 외부 이미지, 서버 API에 의존하지 않습니다.

브라우저에서 로컬 파일 실행을 제한하면 이 폴더에서 아래 명령을 실행하고 `http://localhost:8000`에 접속하세요.

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

- 좌우 방향키: 페이지 이동. Home / End: 처음 / 끝.
- 상단 버튼: 와이어프레임·시안 전환, 전체 보기, 발표 대본, PDF, 인쇄.
- G: 전체 보기. N: 대본. Escape: 열린 패널 닫기.
- `design/01.html`~`12.html`, `wireframe/01.html`~`12.html`: 개별 HTML.

## 이번 수정

- `presentation4-clone`, `presentation5-clone`, `presentation159-clone`의 실제 제작 렌더를 참고했습니다. 검토 파일과 적용 판단은 `review/design-references.md`에 기록했습니다.
- 표지와 마지막 장에는 본문용 섹션 타이틀·페이지 번호를 넣지 않았습니다. 두 페이지는 큰 이미지와 브랜드 메시지를 중심으로 별도 구성했습니다.
- 본문 2–11장의 섹션 위치와 제목 시작 좌표를 통일했습니다. 원본 캔버스는 1280×720, 좌우 여백은 64px, 제목 시작점은 (64, 96)입니다.
- 덱당 이미지 placeholder를 5개에서 12개로 늘렸습니다. 9개 페이지에 분산했고 표지·마지막 이미지 영역은 각각 화면의 46.25%·45%입니다. 모든 이미지 자리는 연회색 단색 `#e5e5e5`입니다.
- Pretendard 가변 폰트를 로컬로 포함했습니다. 고정 크기·간격·글자 크기·행간은 4px 기본, 2px 세부 단위입니다. 브라우저 크기에 따른 전체 캔버스 비례 축소는 별개입니다.
- 관계도, 시장 포함 관계, 사업 경로, 4단계 데모 UI, 자금 사용 표는 실제 HTML/SVG로 구현했습니다.

## 결과물

| 용도 | 파일 |
|---|---|
| HTML 뷰어 | `index.html` |
| 시안 PDF · 12장 | `previews/eonu-design.pdf` |
| 와이어프레임 PDF · 12장 | `previews/eonu-wireframe.pdf` |
| 통합 PDF · 24장 | `previews/eonu-combined-24p.pdf` |
| 기획 검토·개선 대본·근거 관리 | `docs/planning.html`, `previews/eonu-planning.pdf` |
| 시안 전체 시트 | `previews/eonu-design-grid.jpg` |
| 와이어프레임 전체 시트 | `previews/eonu-wireframe-grid.jpg` |
| 24장 통합 시트 | `previews/eonu-all-24-grid.jpg` |
| 개별 PNG | `previews/design/`, `previews/wireframe/` |

기획 문서에는 첫 구매자, 사업 가설, 경쟁 대안, 검증 지표, 시장 계산, 현재 진척의 증빙, 자금과 목표 연결의 빈틈을 짚고 개선안을 제시했습니다. 원문에 없는 시장 규모·매출·계약·가격·자금 배분·목표 수치는 만들지 않았습니다. 미확정 입력란과 원문 기재 상태를 유지했습니다. 6장은 사용자가 승인한 데모 흐름을 포함하며 실제 제품 화면·구현 증빙을 뜻하지 않습니다.

발표 대본은 v1의 사업 내용과 분량을 유지했습니다. 5분 배분안은 계획 시간이며 실제 낭독 측정값은 아닙니다.

## 소스 구조와 재생성

- `src/components.js`: 공통 프레임, 표지/마무리 예외, 아이콘, 이미지 자리, 관계도.
- `src/slides.js`: 12장 내용과 발표 대본.
- `src/slides.css`: 2px/4px 규격, 공통 스타일, 장별 구성, 와이어프레임 테마.
- `src/viewer.js`, `src/viewer.css`: 화면 전환·전체 보기·대본·반응형 뷰어.
- `scripts/`: 개별 HTML, 문서, PDF, PNG, 시트, ZIP 생성.
- `review/`: 기능·렌더·PDF·시각·파일 무결성 검수 기록.

열람에는 설치가 필요 없습니다. 재생성에는 Node.js, Python 3, Chromium이 필요합니다.

```bash
npm ci
python3 -m pip install -r requirements.txt
npm run build
CHROMIUM_PATH=/usr/bin/chromium npm run render
npm run sheets
node review/verify-viewer.cjs
npm run package
```

검수는 localhost에서 수행했습니다. 이 실행 환경의 관리형 Chromium은 `file://` 접근을 정책으로 차단하므로 직접 파일 열기의 실제 실행은 검증하지 못했습니다. 상대 경로와 로컬 자산 구조, 24개 HTML과 인쇄용 페이지, 폰트 로딩 및 뷰어 동작은 검증했습니다.

## 무결성

ZIP 내부의 `review/file-manifest.json`에 파일별 SHA-256이 있습니다. 저장소 루트의 `eonu-ir-20261021-v2-downloads.json`은 ZIP의 크기와 SHA-256을 기록합니다. 업로드 후 GitHub에서 실제로 내려받은 결과는 `eonu-ir-20261021-v2-github-verification.json`에 별도로 기록합니다.

Pretendard의 라이선스는 `assets/fonts/Pretendard-LICENSE.txt`에 포함되어 있습니다.
