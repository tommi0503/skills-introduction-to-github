# EONU IR — 12장 와이어프레임 + 12장 디자인 시안

**압축을 모두 푼 뒤 `index.html`을 열면 됩니다.** 설치 없이 로컬 HTML·CSS·JavaScript·폰트로 동작합니다. 파일을 개별적으로 옮기지 말고 폴더 구조를 유지해 주세요.

## 보기

- [슬라이드 뷰어](index.html): 시안/와이어프레임 전환, 이전·다음, 페이지 선택, 전체 12장 그리드, 발표 대본
- [기획 검토·개선본·근거 등록부](docs/planning.html)
- [디자인 PDF 12장](previews/eonu-design.pdf) / [와이어프레임 PDF 12장](previews/eonu-wireframe.pdf)
- [합본 PDF 24장](previews/eonu-combined-24p.pdf) / [기획 문서 PDF](previews/eonu-planning.pdf)
- [디자인 전체 시트](previews/eonu-design-grid.jpg) / [와이어프레임 전체 시트](previews/eonu-wireframe-grid.jpg) / [24장 비교 시트](previews/eonu-all-24-grid.jpg)

키보드: `←` `→` / `Home` `End` / `G` 전체 보기 / `N` 대본 / `Esc` 닫기. 모바일에서는 좌우 스와이프도 지원합니다. `design/01.html`~`12.html`, `wireframe/01.html`~`12.html`은 각각 독립 HTML입니다. 두 폴더의 `print.html`은 브라우저 인쇄용 전체 덱입니다.

일부 관리형 브라우저는 로컬 HTML 열기를 제한합니다. 그 경우 이 폴더에서 `python3 -m http.server 8000`을 실행하고 `http://localhost:8000`을 열면 됩니다. 사용자 기기에서의 설치나 서버 실행은 기본적으로 필요하지 않습니다.

## 기획 적용

최신 `01_PPT내용과_대본.md`(2026-10-20)의 페이지 순서·내용이 기준입니다. PPTX(2026-10-14)는 보완 참고로만 사용했습니다. 사용자가 확정한 **각각 12장, 6장 데모 진행 흐름 포함**을 반영했습니다. 첨부 문서 안의 제작 메모는 사용자 직접 지시와 구분했습니다.

문제→세 주체의 가치→병원 도입 가설→제품 흐름→사업모델→시장→확장→검증→자금→마무리의 순서입니다. 첫 고객 선정 조건, 검증 지표, 경쟁 대안 비교, 가격·원가·CAC·시장 정의를 기획 문서에 구체화했습니다. 시장 규모·가격·진척·자금 배분의 미확정 값은 임의로 채우지 않았습니다. 자료가 추가되면 `src/slides.js`와 기획 문서를 함께 갱신해 주세요.

## 공통 컴포넌트

기존 `presentation5-clone`의 데이터 모델/렌더러 분리, 로컬 폰트, 브라우저 전체 렌더, 좌표·넘침·placeholder·해시 검수 방식을 참고한 **독립 프로젝트**입니다. 기존 작업은 수정하지 않았습니다. 오프라인 배포를 위해 React/Vite 런타임 대신 정적 HTML과 공통 JavaScript를 사용합니다.

- `src/slides.js`: 단일 12장 콘텐츠와 발표 대본
- `src/components.js`: 공통 헤더/푸터, 관계도, 아이콘, 카드, placeholder 렌더러
- `src/slides.css`: 공통 좌표·크기·타이포그래피 및 두 테마
- `src/viewer.js`, `src/viewer.css`: 페이지 이동·그리드·대본·반응형 뷰어
- `assets/fonts`: 로컬 Pretendard Variable, OFL 라이선스 포함
- `docs`: 기획 검토, 개선 대본, 근거·미확정 항목
- `review`: 브라우저/시각/PDF/해시 검수 기록
- `previews`: 최종 PNG 24장, PDF 4종, 그리드 JPG 3종

슬라이드는 1280×720입니다. 모든 페이지의 섹션 라벨은 x=58, y=34 기준 헤더, 메인 타이틀은 x=58, y=92에 위치합니다. 사진·인물 장면 등 이미지 영역은 `#e5e5e5` 단색 placeholder로 처리했습니다. 차트·관계도·흐름도·UI 도식은 HTML/SVG로 구현했습니다. TAM/SAM/SOM의 도형은 포함 관계이며 금액에 비례하지 않습니다. 배분이 미정인 자금에 임의 도넛 비율을 만들지 않았습니다.

## 재생성

뷰어 이용에는 설치가 필요하지 않습니다. 아래 명령은 제작·검수용입니다.

```bash
npm install
python3 -m pip install -r requirements.txt
npm run build
# 시스템 Chromium이 다른 위치이면 CHROMIUM_PATH를 지정합니다.
npm run render
npm run sheets
node review/verify-viewer.cjs
npm run package
```

Node.js 22 이상, Chromium, Python 3, Pillow, PyMuPDF를 사용했습니다. `scripts/render.mjs`는 모든 페이지의 위치·넘침·내부 잘림·폰트·placeholder를 검사하고 PDF와 PNG를 생성합니다. `scripts/make-sheets.py`는 그리드·합본 PDF를 만들고 각 PDF 12페이지와 추출 가능한 본문을 확인합니다.

`review/render-audit.json`은 최종 소스와 PNG 해시를 기록합니다. GitHub 재다운로드 검증 기록은 저장소 루트의 `eonu-ir-20261021-github-verification.json`에 있으며, ZIP 생성 이후에 기록하므로 ZIP 내부에는 포함되지 않습니다.

## 한계와 확인 필요 사항

데모는 설명용 UI이며 실제 서비스 구현 완료를 의미하지 않습니다. 최신 자료가 빈칸으로 둔 고객군·가격·실증/계약·시장 수치·1억 배분·기간·목표·연락처는 미확정 상태로 유지했습니다. 목표 발표 시간은 5분이며 실제 리허설 시간은 측정하지 않았습니다.

관리형 실행 환경에서 `file://` 탐색은 정책으로 차단되어 실제 동작 검수는 localhost에서 수행했습니다. 런타임 외부 요청·fetch·CDN·웹폰트 서버 의존성은 없습니다.
