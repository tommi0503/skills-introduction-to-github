# Rhetis Spectrum Brief — 084–098

첨부 `selected_part11of12_084-098.zip`의 **7개 덱·109개 이미지**를 독립적인 HTML/CSS/벡터 컴포넌트와 슬라이드 데이터로 재현한 프로젝트입니다. 기존 작업을 보존하고 새 폴더에 구현했습니다. 모든 개별 슬라이드의 캔버스와 PNG는 **1280×720**입니다.

`preview.html`을 브라우저에서 열면 덱 필터, 제목 검색, 원본/결과 나란히 보기, 재현/재조립 전환, 개별 HTML, PDF 및 라이브러리 시트에 접근할 수 있습니다. 폰트와 벡터가 로컬에 있어 인터넷 없이 볼 수 있습니다.

## 실행과 검수

Node.js 20 이상, Python 3, Pillow, PyMuPDF, Playwright, `/usr/bin/chromium`이 필요합니다. 실행 환경에 맞게 Chromium 경로를 바꿀 수 있습니다.

```sh
python -m pip install pillow pymupdf playwright
npm run build
python tools/render.py --round final
python tools/render.py --assembly --round final
python tools/exports.py
python tools/verify.py
python tools/package.py
```

계약에서 제공한 시트 생성 명령도 그대로 지원합니다.

```sh
python tools/preview.py collection/spectrum-brief contract/type-steps.json --out previews/light.html
python tools/preview.py collection/spectrum-brief contract/type-steps.json --dark --out previews/dark.html
```

위 두 명령의 기본 출력은 운영체제 폰트를 사용합니다. 제출한 미리보기에는 별도 검수 도구가 로컬 Pretendard 폰트를 로드합니다. 컬렉션 자체에는 계약상 금지된 `@font-face`, 외부 리소스, 이미지가 없습니다. 라이브러리 검수는 `python tools/library-review.py`로 재현합니다.

## 구조

- `src/primitives.mjs`: 텍스트·도형·선·Lucide·벡터·placeholder·chip 공통 데이터 모델.
- `src/decks/`: 덱별 문구·색·좌표·차트 값과 반복 구조를 정의하는 독립 파일.
- `src/renderer.mjs`: 실제 폰트를 사용하는 공통 HTML 렌더러. chip은 실제 글리프의 시각적 중심을 보정합니다.
- `src/assembly.mjs`: 컬렉션의 `card.parts`, `metric.figure`, `pill.parts`, `frame.picture` 계약으로 다시 조립하는 컴파일러. 패널 안의 문구를 해당 card의 parts로 묶고 페이지별 위치·색·크기 override를 유지합니다. 원본에 없는 나머지 라이브러리 요소도 같은 토큰과 언어로 별도로 설계했습니다.
- `build/assembly-data/`: 재조립에 쓰인 컴포넌트 계약·소유 관계·원본 노드 인덱스·데이터. 입력 이미지를 추적하거나 결과 bitmap을 가져오는 과정은 없습니다.
- `collection/spectrum-brief/`: 공유 토큰·페이지 foundation·31개 요소 및 변형 fixture. Atlas/Miri는 파일 형식과 계약 클래스의 구조만 참고했습니다.
- `references/`: 비교 화면 전용 원본. 슬라이드 UI에는 원본 bitmap을 삽입하지 않습니다.
- `provenance/`: 입력 목록·SHA-256·읽은 README 원문. 첨부 문서는 사용자가 지정한 계약 및 출처로 취급하고, 사용자의 직접 지시와 구분했습니다.
- `renders/final/{replica,assembly}/`: 두 결과의 모든 개별 PNG.
- `comparisons/final/`: 원본과 최종 결과를 나란히 놓은 개별 비교 이미지.
- `pdfs/`: 덱별 PDF, 전체 109페이지 PDF, 9-up 시트 PDF.
- `previews/`: 전체 미리보기와 라이브러리 light/dark 시트.
- `review/`: 덱별 에이전트 검수, 주 에이전트 통합 검수, 실제 브라우저 측정값·폰트 상태·최종 소스/HTML/PNG 해시.

기존 `rhetis-business-034-042`의 공통 primitive·렌더·검수 구조를 참고해 별도 프로젝트를 만들었습니다. 이번 이미지의 디자인과 데이터는 새로 구성했습니다.

## 재현 범위와 판단

사진, 복잡한 3D 일러스트, 이미지 아이콘, 사진 속 기기 화면은 연회색 단색 placeholder로 바꿉니다. 원본의 크롭과 프레임 모양은 유지합니다. 단순 도형·표·차트·텍스트·Lucide 아이콘 및 직접 그릴 수 있는 기하학 배경은 구현합니다. 원본을 통째로 결과에 배치하지 않습니다.

원본은 폰트 정보가 없는 래스터 이미지입니다. Pretendard, NanumSquareRound, Gmarket Sans, Montserrat의 실제 파일과 굵기를 로드하고 가까운 자형·줄바꿈을 맞췄습니다. 원본과 완전히 동일한 서체임을 단정하지 않으며, 세부 차이와 판독이 어려운 문구의 해석은 검수 기록에 남겼습니다.

컬렉션은 서로 다른 일곱 덱의 공통 디자인을 한 가지 언어로 통합합니다. mint rail, navy figure, 흰 사각 패널, blue/cyan·green 보조색, 제한적인 lavender를 사용합니다. 원본에 없는 요소는 이 언어에서 확장했습니다. 다크 모드는 별도 배색이며, 작은 칸에서는 글자 단계를 낮추고 부가 문구의 우선순위를 조정합니다.

## 산출물

- `spectrum-brief.zip`: 최상위에 `spectrum-brief/` 하나만 있는 Rhetis 컬렉션.
- `rhetis-spectrum-084-098-deliverables.zip`: 소스, 전체 PNG, 원본/결과 비교, PDF, 전체 미리보기, 라이브러리, 검수 기록.

아카이브 CRC와 SHA-256, 이미지 수·크기, PDF 페이지 수·크기, 빌드 및 마지막 수정의 최종 렌더 반영을 검사합니다. GitHub에 올린 ZIP은 다시 다운로드하여 로컬 결과와 SHA-256을 비교합니다.
