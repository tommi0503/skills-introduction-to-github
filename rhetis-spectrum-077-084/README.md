# Rhetis Spectrum · 077–084

첨부 ZIP에 실제로 포함된 5개 덱, 106장을 1280×720 HTML UI로 재현하고 새로운 Rhetis 컬렉션 `rhetis-spectrum`으로 재조립한 작업입니다. 기존 프레젠테이션 프로젝트의 공통 데이터·렌더러·검수 구조를 참고해 별도 폴더에 만들었습니다.

`preview.html`을 열면 전체 페이지, 원본 비교, 라이브러리 재조립본과 PDF를 탐색할 수 있습니다. 폰트까지 정확히 로드하려면 아래처럼 이 폴더에서 로컬 서버를 실행한 뒤 `http://localhost:8000/preview.html`로 접속합니다.

```bash
python -m http.server 8000
```

범위는 077의 slide_03–24(22장), 078의 slide_01–19(19장), 079의 slide_01–19(19장), 080의 slide_01–30(30장), 084의 slide_01–16(16장)입니다. 포함되지 않은 081–083이나 077의 앞 두 장은 추가하지 않았습니다. 업로드된 README 전체는 `contract/REFERENCE-README.md`에 보관하며, 이미지 속 예시·안내 문장은 재현할 콘텐츠로만 취급합니다.

재생성에는 Node.js 18+, Python 3.10+, Pillow, PyMuPDF, Playwright와 Chromium이 필요합니다. 브라우저 경로는 `tools/render.py`의 `/usr/bin/chromium`입니다.

```bash
npm run build
python tools/render.py --round final
python tools/render.py --round final --assembly
python tools/collection-check.py
python tools/audit-slides.py
python tools/finalize.py
python tools/verify.py
python tools/check-preview.py
python tools/package.py
```

공식 컬렉션 시트 생성 명령은 다음과 같습니다. 컬렉션 CSS는 계약대로 외부 리소스를 포함하지 않습니다. 실제 폰트는 호스트가 공급하며, `tools/library-output.py`로 로컬 폰트가 연결된 `build/library/light.html`과 `dark.html`을 생성합니다.

```bash
python tools/preview.py collection/rhetis-spectrum contract/type-steps.json --out light.html
python tools/preview.py collection/rhetis-spectrum contract/type-steps.json --dark --out dark.html
python tools/library-output.py
```

소스는 `src/decks/`의 덱 데이터, `src/primitives.mjs`의 재사용 가능한 텍스트·도형·선·아이콘·placeholder, `src/renderer.mjs`의 공통 DOM/SVG 렌더러로 나뉩니다. 재조립본은 컬렉션의 실제 토큰·foundation·요소 CSS를 불러오고 card, metric, pill, image-frame의 계약 마크업과 세부 좌표 override로 구성합니다. 복잡한 표·차트·관계도는 여러 기본 단위와 SVG를 조합합니다. 31종 의미 요소 자체의 동작과 다양한 수량은 독립 fixture 시트에서 확인합니다.

`references/`는 변경하지 않은 비교 원본이며 결과 UI의 배경으로 사용하지 않습니다. 사진·3D·이미지 아이콘·기기 화면·사진 배경은 연회색 단색 자리로 바꿉니다. 사진 배경의 흰색 텍스트는 필요한 경우 남색으로 바꿔 읽을 수 있게 했습니다. 단순 도형과 벡터 장식, 표와 차트는 직접 구현했습니다. 작은 문구를 판독할 수 없는 경우 의미 있는 한국어로 대체했습니다.

Pretendard, NanumSquare, NanumSquareRound, Gmarket Sans, Montserrat의 실제 로컬 파일을 포함합니다. 일부 폰트는 시각적으로 추정했으며 PNG만으로 원본 서체·웨이트를 확정할 수 없습니다. 덱별 추정과 남은 차이, 수정 내역은 `review/deck-*.md`와 `review/final-review.md`에 기록했습니다. 휴대용 계약 검사는 Rhetis의 실제 importer 반입 검사를 대신한다고 주장하지 않습니다.

완성 산출물은 `renders/final/`의 개별 PNG, `comparisons/final/`의 원본/결과 비교 이미지, `previews/`의 시트 PNG·전체 미리보기, `pdfs/`의 개별 덱·전체·시트 PDF, `renders/library/`의 컬렉션 검수 이미지입니다. `review/`에는 자동 검사, 소스·HTML·최종 PNG 해시, 담당별 시각 검수 기록을 함께 보관합니다.

전체 ZIP은 재현/재조립이 픽셀 단위로 동일함을 확인한 뒤 원본/결과 비교 이미지를 106쌍으로 중복 제거했습니다. 재현 PNG와 재조립 PNG 212개는 모두 포함합니다.
