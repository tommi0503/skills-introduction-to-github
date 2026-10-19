# Rhetis Report Suite

첨부한 **5개 덱 · 원본 121장**을 재현하고, 공통 디자인 언어를 **Rhetis 컬렉션 31개 요소**로 정리한 별도 프로젝트입니다. 기존 저장소의 프레젠테이션 작업은 수정하지 않습니다.

## 원본과 요청의 구분

사용자 요청은 1280×720 재현, 재사용 가능한 컴포넌트, 사진/복잡 삽화/기기 화면의 연회색 placeholder, 실제 브라우저의 개별 비교, PNG·PDF·ZIP, GitHub 업로드입니다. `contract/REFERENCE-README.md`는 사용자가 계약으로 명시한 첨부 문서의 사본이며, 토큰·foundation·31개 요소의 파일 형식과 CSS/fixture 규칙에 적용했습니다. atlas/miri는 구조 예시로만 확인했습니다. 레퍼런스 이미지 안의 안내 문구는 재현할 콘텐츠이며 작업 지시로 실행하지 않았습니다.

원본 범위: 005번 `slide_08`–`slide_30` 23장, 006·007·008번 `slide_01`–`slide_30` 각30장, 009번 `slide_01`–`slide_08` 8장입니다. 첨부하지 않은 장은 추가하지 않았습니다. 모든 원본은 1280×720입니다.

## 실행

```bash
npm ci
npm run dev -- --host 127.0.0.1 --port 5301
npm run build
npm run render -- --round=final --production --mode=clone
npm run render -- --round=final --production --mode=assembled
npm run verify
python scripts/contract-check.py
python scripts/package.py
```

Node 20.19+/22.12+, Python 3, Pillow, PyMuPDF와 Chromium(`/usr/bin/chromium`)이 필요합니다. `playwright-core`는 시스템 Chromium을 사용합니다. 로컬 서버·브라우저 실행이 제한되는 샌드박스에서는 해당 권한이 필요합니다.

갤러리 `/`, 단일 재현본 `?deck=005&slide=slide_08`, 재조립본 `?deck=005&slide=slide_08&mode=assembled`를 제공합니다. 설치 없는 완성본 탐색은 제출 ZIP의 `artifacts/preview.html`로 가능합니다. 패키징 결과는 `artifacts/downloads/`에 저장되며, `--output-dir`로 추가 복사 위치를 지정할 수 있습니다.

## 소스 구성

- `src/decks/deck-*.mjs`: 덱별 데이터·팩토리 및 원본 내용을 해석한 `library` 의미 데이터
- `src/primitives.mjs`, `renderer.mjs`: 공통 텍스트·chip·도형·SVG·Lucide·표·차트·placeholder 렌더러
- `src/components.mjs`, `assembly.mjs`: 실제 컬렉션 CSS/토큰/계약 마크업을 이용하는 재조립 어댑터
- `collection/rhetis-report-suite/`: 키트, foundation, 31개 요소 및 79개 fixture(요소77 + foundation2)
- `contract/`, `tools/preview.py`: 제공된 계약과 변경하지 않은 미리보기 도구
- `review/`: 원본 목록, 덱별 해석·차이·수정 기록, 개별 브라우저 캡처 검사, 통합 검사와 해시
- `renders/final/`: 121장 재현본 + 121장 재조립본의 독립 PNG
- `comparisons/final/`: 모든 원본/결과 개별 비교 JPG
- `artifacts/`: PDF, 시트, 전체 미리보기, 다운로드 ZIP

재현본은 원본의 배치와 색·선·타이포 위계를 최대한 유지합니다. 재조립본은 원본의 의미 데이터와 내용을 Rhetis의 12×6 그리드, 카드·수치·표·차트·관계 요소로 정리한 별도 구성입니다. 재조립은 라이브러리의 공통 언어를 확인하기 위한 버전이며 원본의 자유 좌표와 장식을 그대로 보존하는 재현본과 구분됩니다. 의미 데이터가 따로 없는 장은 원본 텍스트와 이미지 자리에서 목록/프레임을 구성합니다.

사진·복잡한 인물 삽화·기기 화면은 `#e5e5e5` 단색입니다. 단순 기기 외곽과 표·차트·선형 아이콘·벡터 도형은 직접 그렸습니다. 결과 슬라이드에는 원본 PNG를 삽입하지 않습니다. 원본은 비교용으로만 사용하며 경량 제출 ZIP에서는 중복 원본 PNG를 제외합니다. 비교 JPG에는 원본이 포함되어 있습니다. 비교 이미지를 재생성하려면 Git 저장소의 `public/reference/` 또는 첨부 원본 ZIP이 필요합니다.

폰트 메타데이터가 없는 래스터를 참고했기 때문에 서체는 시각적으로 추정했습니다. 실제 Noto Sans KR, Pretendard, Roboto Condensed, Cormorant Garamond, Inter, Noto Serif KR, Nanum Myeongjo 파일을 앱에서 로드합니다. 컬렉션에는 외부 자산을 넣지 않는 계약에 따라 시스템에 설치된 Noto Sans CJK KR 이름을 토큰으로 선언했습니다. 회색 placeholder, Lucide 아이콘의 형태 차이, 판독이 갈리는 문구와 판단은 덱별 기록에 명시합니다.

## 검수

덱별 2–3회 비교·수정 안에서 모든 페이지를 실제 Chromium으로 렌더하고 각 원본/결과 비교 파일을 개별 열람했습니다. 중단된 캡처는 완결된 시각 검수 회차에 포함하지 않습니다. 주 에이전트는 공통 렌더러·핵심 페이지·수정 페이지를 통합 검수합니다. 연락처 시트는 탐색용입니다.

자동 검사는 1280×720, 실제 그려진 글자의 영역 초과/잘림, 실제 문자열의 폰트 로딩, chip 글자 중심, placeholder 색, 결과 내 원본 비트맵 부재, 브라우저 오류와 실패 요청을 확인합니다. 한글 폰트의 큰 em box 때문에 생기는 오검출을 줄이기 위해 Range의 행 위치와 Canvas 실제 glyph metrics를 함께 씁니다. 최종 빌드·정의·PNG SHA-256을 검증하여 마지막 수정이 최종 렌더에 반영되었는지 확인합니다.

```bash
python tools/preview.py collection/rhetis-report-suite contract/type-steps.json --out light.html
python tools/preview.py collection/rhetis-report-suite contract/type-steps.json --dark --out dark.html
```

컬렉션은 79개 fixture의 선언된 최소 칸과 전체 칸을 라이트·다크에서 실브라우저로 점검합니다. 제공 도구는 공식 Rhetis intake가 아니며, 이 저장소는 Rhetis 서비스에 직접 반입하거나 등록하지 않습니다. 구조/CSS 계약 검사는 `review/contract-check.json`, 브라우저 결과와 결정 사항은 `review/library.md` 및 관련 기록에 있습니다.

컬렉션 전체 fixture PDF는 `artifacts/pdf/library-light.pdf`, `artifacts/pdf/library-dark.pdf`에 있습니다. 각 79페이지이며 모든 페이지는 1280×720 points입니다. 정적 전체 미리보기는 `artifacts/preview.html`입니다.
