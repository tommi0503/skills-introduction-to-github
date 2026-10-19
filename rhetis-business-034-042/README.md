# Business Spectrum · Rhetis presentation collection

첨부한 part05 ZIP의 실제 5개 덱, 91장을 새 폴더에서 구현했습니다. 기존 프로젝트는 수정하지 않습니다. 범위: 034의 slide_06–09(4장), 039(30장), 040(30장), 041(20장), 042의 slide_01–07(7장). 없는 035–038 덱이나 다른 파트 이미지는 추정해 추가하지 않았습니다.

`preview.html`에서 모든 페이지와 원본/결과 비교, 재조립본을 탐색합니다. 각 결과는 1280×720입니다. 이미지에 담긴 문구는 디자인 참고 자료로만 다루고, 제작 계약은 사용자가 지정한 첨부 README 전체(`contract/REFERENCE-README.md`)와 사용자의 직접 지시를 따릅니다.

## 재생성

Node.js 18+, Python 3.10+, Pillow, PyMuPDF, Playwright 및 Chromium이 필요합니다. 아이콘은 Lucide SVG를 로컬 데이터로 묶어 별도 npm 의존성이 없습니다. 실제 로컬 폰트도 포함합니다.

```bash
npm run build
python tools/render.py --round final
python tools/render.py --round final --assembly
python tools/collection-check.py
python tools/verify.py
python tools/finalize.py
```

`tools/render.py`는 localhost 임시 서버 한 개와 Chromium 한 개를 사용합니다. 기본 Chromium 경로는 `/usr/bin/chromium`입니다. 다른 운영체제에서는 해당 경로를 설치 위치로 수정하세요. PDF는 실제 DOM을 브라우저에서 출력한 것이며, 재현본·재조립본 각각 전체 PDF 및 12장 단위 시트 PDF를 제공합니다.

공식 컬렉션 미리보기:

```bash
python tools/preview.py collection/business-spectrum contract/type-steps.json --out light.html
python tools/preview.py collection/business-spectrum contract/type-steps.json --dark --out dark.html
```

폰트는 컬렉션 CSS의 외부 리소스 금지 계약에 따라 호스트에서 로드합니다. 제출 미리보기 `build/library/`는 실제 로컬 Pretendard 파일을 호스트 CSS로 주입합니다. 컬렉션 자체는 `@font-face`, `url()`, 이미지·외부 리소스를 포함하지 않습니다.

## 소스 구조

- `src/primitives.mjs`: 텍스트·도형·선·아이콘·placeholder·chip의 독립 데이터 계약
- `src/decks/`: 담당별 5개 덱 데이터 및 덱 내부의 재사용 함수
- `src/renderer.mjs`: 공통 DOM/SVG 렌더러와 컬렉션을 로드하는 재조립 어댑터
- `collection/business-spectrum/`: kit, foundation, 계약 요소 31개와 한국어 fixture 85개(요소 83개·foundation 2개)
- `contract/`: 업로드된 계약 원본과 공식 preview 도구의 입력
- `review/`: 전수 이미지 목록, 담당별 개별 시각 비교, 자동 검사 및 최종 소스/렌더 해시
- `references/`: 변형하지 않은 참고 PNG(결과 UI의 배경으로 사용하지 않음)
- `build/replica/`, `build/assembly/`: 생성된 개별 HTML과 덱별 인쇄 HTML
- `renders/final/`, `comparisons/final/`: 전체 PNG와 원본/결과 pair(완성 ZIP에 포함)
- `pdfs/`, `previews/`: 전체 PDF, 시트 PDF 및 전체 미리보기

재조립본은 collection의 실제 CSS와 contract markup을 불러와 card, pill, metric, image-frame을 기본 단위로 조립하며, 원본 좌표와 세부 색을 유지하는 페이지 override를 사용합니다. 복잡한 표·차트·관계도는 원본 재현용 데이터에 정의한 여러 기본 단위와 SVG를 조합합니다. 컬렉션 31종의 독립 의미 단위와 다양한 수량·최소 칸 동작은 별도 fixture 시트로 확인할 수 있습니다.

사진·복잡한 3D·기기 화면·이미지 로고는 사용자의 지시대로 연회색 단색입니다. 편집 파일의 폰트 정보가 없어 시각적으로 판정한 실제 Pretendard/Gmarket Sans/Montserrat를 로드했으며 원본 글꼴과 완전히 동일하다고 단정하지 않습니다. 작은 판독 불가 문구는 정상적인 한국어 문장으로 대체하고 담당별 검수 기록에 적었습니다. 지도는 단순화된 벡터와 placeholder로 해석한 부분이 있습니다.
