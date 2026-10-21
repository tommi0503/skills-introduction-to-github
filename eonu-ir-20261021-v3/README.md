# EONU IR · v3

**와이어프레임 12장 + 디자인 시안 12장.** 최신 MD의 페이지 주제와 사업 논리를 유지하면서, 사용자가 마지막으로 첨부한 6개 디자인 레퍼런스를 기준으로 화면을 다시 구성했습니다. 기존 v1·v2와 다른 프레젠테이션 작업은 그대로 보존했습니다.

## 바로 확인

압축을 모두 해제한 뒤 `index.html`을 여세요. 페이지 이동, 스타일 전환, 전체 보기, 발표 대본, 기획 검토, PDF 링크가 포함된 HTML 뷰어입니다. 로컬 폰트와 상대 경로 자산을 사용하므로 열람에 패키지 설치나 외부 서비스 연결이 필요하지 않습니다.

브라우저가 로컬 파일을 제한하면 이 폴더에서 다음 명령을 실행하고 `http://localhost:8000`으로 접속하세요.

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

좌우 방향키로 이동하고, G로 전체 보기, N으로 대본, Escape로 열린 패널을 닫을 수 있습니다. Home / End는 처음 / 마지막 장으로 이동합니다.

| 결과물 | 경로 |
|---|---|
| HTML 뷰어 | `index.html` |
| 시안 12장 PDF | `previews/eonu-design.pdf` |
| 와이어프레임 12장 PDF | `previews/eonu-wireframe.pdf` |
| 통합 24장 PDF | `previews/eonu-combined-24p.pdf` |
| 시안 그리드 시트 | `previews/eonu-design-grid.jpg` |
| 와이어프레임 그리드 시트 | `previews/eonu-wireframe-grid.jpg` |
| 통합 24장 시트 | `previews/eonu-all-24-grid.jpg` |
| v2 → v3 비교 시트 | `previews/eonu-v2-v3-comparison.jpg` |
| 기획 검토·개선본·대본·근거 | `docs/planning.html`, `previews/eonu-planning.pdf` |
| 개별 HTML | `design/01.html`~`12.html`, `wireframe/01.html`~`12.html` |

## 디자인에서 바꾼 것

v2의 긴 설명과 반복 관계도, 상태표와 입력 빈칸이 화면의 무게를 분산시켰습니다. v3는 짧은 주장과 중심 시각물 하나가 먼저 보이도록 구성했습니다. 레퍼런스의 흰 패널, 옅은 회색 바닥, 원형 배지, 부드러운 그림자와 청색 강조를 사용했습니다.

- **표지:** “함께 오지 못해도, 이야기는 함께.”라는 약속과 진료 전 공유 기록.
- **문제:** 네 가지 이야기 흐름을 진료실 안/밖의 두 큰 장면으로 묶음.
- **솔루션:** 3장만 큰 관계도. 5장은 병원 설정 창, 9장은 환자 기록 중심의 확장 도식. 연결 방향을 보여주는 작은 도식은 유지.
- **데모:** 중앙의 ‘공유 전 확인’ 화면이 가장 크게 보이고, 병원 설정·기록·의료진 확인은 양옆에 배치.
- **현재와 투자:** 상세 상태표와 미확정 숫자 입력 틀은 보완 문서로 이동. 화면은 현장 접점과 다음 검증, 큰 1억 원과 세 가지 사용 목적에 집중.
- **표지·마지막:** 섹션 타이틀·페이지 번호가 없는 전용 구성. 본문 2–11장의 섹션 및 제목 시작 좌표는 통일.

공백과 HTML 태그를 제외한 슬라이드 화면 문자는 v2의 3,438자에서 2,037자로 **40.8% 감소**했습니다. 대본 12개는 그대로 유지했고, 화면에서 덜어낸 검증 조건과 상세 항목은 기획 문서와 근거 패널에서 확인할 수 있습니다. 측정 기준과 장별 결과는 `review/content-density.json`에 있습니다.

## 규격과 내용 기준

- 1280×720, Pretendard 로컬 폰트. 고정 크기·글자 크기·행간은 4px 기본 / 2px 세부 단위.
- 본문 섹션 좌표 (64,48), 제목 시작점 (64,96). 반응형 화면에서는 캔버스 전체를 비례 축소.
- 이미지 자리 11개는 모두 연한 단색 회색 `#e5e5e5`. 사진·로고·실제 서비스 캡처를 임의로 넣지 않음.
- 관계도·분기선·시장 포함 관계·데모 UI·투자 실행 구조는 실제 HTML/SVG.
- 6장 데모는 사용자가 승인한 구성. 설명용 화면이며 구현·EMR 연동 완료 증빙이 아님.
- 시장 수치, 가격, 계약·실증 실적, 자금 배분·집행 기간·목표는 임의로 확정하지 않음. 확인할 입력 틀은 문서에 보존.
- 4장의 걱정 → 관련 서비스 정보 → 자발적 상담은 검증할 사업 가설. 비급여 필요성과 전환 성과를 입증된 결과로 표시하지 않음.

## 공통 구조와 재생성

`src/components.js`는 공통 프레임·아이콘·이미지 자리·작은 관계도를 제공합니다. `src/slides.js`가 12장의 내용과 대본을, `src/slides.css`가 공통 규격과 각 장의 구도를 관리합니다. 동일한 내용과 공간 구조에 시안/와이어프레임 테마를 적용합니다. `src/viewer.*`는 페이지·전체 보기·대본·반응형 기능을 담당합니다.

재생성에는 Node.js, Python 3, Chromium이 필요합니다.

```bash
npm ci
python3 -m pip install -r requirements.txt
npm run build
CHROMIUM_PATH=/usr/bin/chromium npm run render
npm run sheets
node review/verify-viewer.cjs
python3 scripts/verify-delivery.py
npm run package
```

검수 기록은 `review/`에 있습니다. 관리형 Chromium이 `file://` 접근을 차단하는 환경이므로 실제 뷰어 기능은 localhost에서 검증합니다. 상대 경로·로컬 폰트·classic JavaScript 구조를 사용하며 fetch·CDN·외부 API 의존성은 없습니다.

Pretendard 라이선스는 `assets/fonts/Pretendard-LICENSE.txt`에 포함되어 있습니다. ZIP 내부 `review/file-manifest.json`은 파일별 SHA-256을, 저장소 루트의 `eonu-ir-20261021-v3-downloads.json`과 `eonu-ir-20261021-v3-github-verification.json`은 ZIP 및 GitHub 재다운로드 검증을 기록합니다.
