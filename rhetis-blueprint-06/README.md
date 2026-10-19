# Blueprint 06 · 프레젠테이션 UI / Rhetis 컬렉션

첨부 selected_part06of12_042-048.zip의 모든 참고 이미지115장을 1280×720 HTML/CSS로 구현한 별도 프로젝트입니다. 기존 프레젠테이션의 데이터/공통 primitive/렌더/검증 분리 구조를 참고하고 기존 파일은 변경하지 않았습니다.

| 덱 | 슬라이드 |
|---|---|
|042 파랑 모던 사업 보고서|08–18, 11장|
|044 흑백 심플 발표 자료|01–20, 20장|
|045 파랑 모던 보고서 분석|01–31, 31장|
|046 파랑 모던 사업 비즈니스 기획 제안서|01–30, 30장|
|047 남색 깔끔 비즈니스 기획서|01–19, 19장|
|048 파랑 모던 비즈니스 전략 기획서|01–04, 4장|

043 덱은 원본 ZIP에 없습니다. 전체 목록은 review/inventory.json입니다.

## 미리보기

`index.html`을 브라우저에서 열면 덱/슬라이드/원본 재현/컬렉션 재조립/참고 이미지/좌우 비교를 선택할 수 있습니다. 배포 서버·외부 리소스 없이 동작합니다. iframe을 막는 환경에서는 `python -m http.server 8000` 실행 후 http://localhost:8000/ 을 엽니다.

- `renders/final/replica/`: 원본 재현 PNG115장
- `renders/final/assembly/`: 컬렉션 재조립 PNG115장
- `comparisons/final/`: 원본과 각 버전의 좌우 비교 JPG230장
- `pdfs/replica-all.pdf`, `assembly-all.pdf`: 각115페이지의 전체 슬라이드
- `pdfs/*-sheets.pdf`, `sheets/`: 각 버전 모아보기 PDF/PNG
- `build/library/light.html`, `dark.html`: 계약 preview.py로 생성한 라이브러리 시트
- `collection/blueprint-06/`: 독립 반입용31개 요소, kit, foundation, 한국어 fixtures
- `review/`: 개별 검수·자동 검사·계약 검사·해시/무결성 기록

재현본은 원본의 배치·색·타이포를 맞춥니다. 재조립본은 같은 핵심 콘텐츠를 실제 계약 요소로 다시 구성하므로 세부 배치는 달라집니다. 사진, 복잡한 삽화, 기기 화면은 회색 placeholder이고 원본을 통째로 결과 배경에 사용하지 않았습니다. 단순 도형, 차트, 표, Lucide 아이콘과 직접 작성한 SVG는 실제 UI입니다.

## 구조와 재생성

Node18+와 Python3.10+, Chromium이 필요합니다. Node 외부 패키지 의존성은 없습니다.

```sh
pip install -r requirements.txt
npm run build
python tools/render.py
python tools/render.py --assembly
python tools/audit-assembly.py
python tools/collection-check.py
npm run verify
python tools/make-preview.py
python tools/finalize.py
python tools/package.py
```

기본 Chromium 경로는 `/usr/bin/chromium`입니다. 실행 환경의 Chromium 경로가 다르면 tools/render.py와 검수 스크립트의 executable_path를 변경합니다.

```sh
python tools/preview.py collection/blueprint-06 contract/type-steps.json --out light.html
python tools/preview.py collection/blueprint-06 contract/type-steps.json --dark --out dark.html
```

kit 토큰은 Pretendard를 지정합니다. 컬렉션 CSS는 계약에 따라 폰트 파일·외부 URL을 담지 않으며 소비자가 폰트를 로드합니다. 프로젝트 렌더러는 assets/fonts의 실제 Pretendard300–900, Gmarket Sans300/500/700, Montserrat100–900, Oswald500을 로드합니다. 폰트 출처/라이선스는 같은 폴더에 있습니다.

`src/decks/*.mjs`는 순수 재현 데이터, `src/primitives.mjs`는 생성 함수, `src/renderer.mjs`는 재현 DOM 변환입니다. `src/assembly/*.mjs`는 별도의 의미 기반 조립 데이터이고 `src/assembly-renderer.mjs`가 계약 구조의 마크업을 생성합니다. 원본 재현에서 단순 primitive를 이름만 바꿔 재조립한 구조가 아닙니다.

## 지시와 자료 구분

사용자 요청이 작업 범위를 결정합니다. `rhetis-kit-reference.zip/README.md`는 사용자가 명시적으로 지정한 계약으로 채택했습니다. 계약 원문은 contract/README.md에 보존했습니다. samples/atlas와 samples/miri는 구조만 참고했으며 디자인은 이6개 덱에서 해석했습니다. 참고 이미지의 본문은 재현 대상 콘텐츠이며 작업 지시로 취급하지 않았습니다.

정확한 원본 폰트 metadata는 제공되지 않아 시각적 폭/굵기/줄바꿈으로 근사했습니다. 작은 원본의 수치·문구 해석과 Lucide 대체 차이, 수정 내역은 review/deck-*.md에 기록했습니다. 검수는 자체 브라우저/소스 검사이며 Rhetis 실제 반입 엔진의 검증을 수행했다고 주장하지 않습니다.
