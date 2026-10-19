# Rhetis Part 03 — 90 editable presentation slides

첨부 ZIP의 8개 덱, 90개 1280×720 이미지를 HTML/CSS/SVG와 데이터로 재구현했습니다. 기존 프레젠테이션 프로젝트의 model/primitives/ui 분리를 참고한 독립 폴더입니다. 기존 작업 파일은 수정하지 않았습니다.

## 결과

- `src/decks/`: 8개 덱 90장. 공통 `model.ts`, `primitives.ts`, `ui.tsx`로 재사용합니다.
- `library/rhetis-report/`: 공유 토큰, foundation, 31개 계약 요소, 요소 fixture 87개와 foundation fixture 2개.
- `renders/final/`: 원본 재현 PNG 90개, 모두 1280×720.
- `renders/assembly/`: 라이브러리 재조립 PNG 90개, 모두 1280×720.
- `renders/library/`: fixture 89개 × 라이트/다크 = PNG 178개, 모두 1280×720.
- `comparisons/final/`: 원본 좌측·재현 우측 비교 PNG 90개(2560×720), 보기용 JPG 90개(1280×360).
- `deliverables/pdf/`: 전체 90장 재현 PDF, 덱별 PDF, 비교 PDF, 연락처 시트 PDF, 라이브러리 재조립 PDF.
- `deliverables/preview.html`: 서버 없이 여는 전체 PNG 미리보기. 원본 비교와 조립본 토글.
- `assembly.html`: 실제 라이브러리 HTML/CSS로 재조립한 90페이지. `tools/assemble.py`로 생성합니다.
- `review/`: 원본 목록, 덱별 개별 시각 검수, 자동 검사와 구성요소 매핑 기록.

## 실행

Node 24 이상, Python 3, Chromium이 필요합니다.

```sh
npm install
npm run dev -- --host 127.0.0.1 --port 5173
npm run verify
npm run build
```

브라우저에서 `?deck=009&slide=slide_09`는 1280×720 단일 화면, `?deck=009&mode=compare`는 원본 비교입니다. 원본은 `public/reference/`에서 비교에만 사용하며 슬라이드 캔버스에는 원본 이미지를 넣지 않습니다. 사진·복잡한 삽화·기기 화면은 연회색 placeholder입니다.

## 라이브러리 계약 및 조립

`contract/REFERENCE-README.md`는 사용자가 계약으로 지정한 첨부 README의 보존 사본입니다. 샘플 atlas/miri에서는 폴더·fixture 구조만 참고했고 CSS 디자인은 새로 작성했습니다. 컬렉션 ZIP의 최상위는 `rhetis-report/` 하나입니다.

```sh
python tools/preview.py library/rhetis-report contract/type-steps.json --out library/rhetis-report/preview-light.html
python tools/preview.py library/rhetis-report contract/type-steps.json --dark --out library/rhetis-report/preview-dark.html
```

재조립본은 원본 재현 데이터의 위치를 페이지 `.overrides`로 유지하면서 카드·pill·metric·frame·tag·차트·표를 컬렉션 계약 마크업으로 변환합니다. 글자 크기는 가장 가까운 허용 `--type-N` 단계로 정규화합니다. `review/assembly-map.json`은 3,529개 원본 요소와 사용한 계약의 대응표입니다. 장표 밖에서 도형/아이콘 SVG를 따로 생성하여 결합하며 원본 스크린샷으로 대체하지 않습니다. Foundation fixture와 31개 요소 시트에서는 페이지 전용 override 없이 컬렉션의 기본 디자인·반응형 동작을 확인할 수 있습니다.

## 검수 및 차이

담당자 6명 이내로 분담했고 모든 원본을 개별 확인했습니다. 각 덱은 실제 Chromium 렌더와 원본/결과 개별 비교를 2–3회 내에서 수행하고 주 담당자가 통합 렌더·표본 확대·자동 검수를 수행했습니다. 마지막 글자 프레임 보정을 포함한 최종 렌더는 `review/final-audit.json`의 PNG SHA-256에 연결됩니다.

원본 폰트 파일과 폰트명 메타데이터가 없어 실제 로드한 Pretendard Variable/Inter 및 시스템 글꼴로 근사했습니다. 014의 네온 곡률·빛 번짐, 021의 장식 타이틀 글꼴, 일부 로고·아이콘은 원본과 다릅니다. 8개 다른 덱을 통합한 컬렉션은 라임 강조·가는 선·정돈된 회색 패널을 중심 문법으로 삼았습니다. 원본에 없는 요소와 fixture 문장은 새로 설계했습니다. 상세 해석과 판독상의 판단은 덱별 검수 문서에 기록했습니다.

## 재생성

`npm run render`는 5174의 production preview를 사용합니다. `tools/outputs.py`는 비교·PDF·정적 미리보기를 만들며 Pillow가 필요합니다. `tools/assemble.py`는 렌더 메타데이터와 SVG를 컬렉션으로 조립합니다. `tools/render-assembly.mjs`와 `tools/contrast.mjs`는 5175의 정적 서버를 사용합니다. Playwright Core와 Chromium 실행 경로는 환경에 맞게 설정하십시오.
