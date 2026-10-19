# Rhetis Business Prism · 061–077

첨부 참고 이미지 8개 덱, 117장을 재사용 가능한 HTML·CSS·데이터와 편집 가능한 SVG로 재현했습니다. 기존 프레젠테이션 프로젝트는 보존하고 이 폴더에 독립적으로 제작했습니다.

| 덱 | 이미지 수 | 범위 |
|---|---:|---|
| 061 파랑 모던 마케팅 기획서 | 17 | slide_03–19 |
| 064 주황 워크숍 결과보고서 | 18 | slide_01–18 |
| 065 파랑 사업 성과 보고서 | 18 | slide_01–18 |
| 066 흑백·회색 마케팅 전략 기획서 | 16 | slide_01–16 |
| 069 그레이·블루 상반기 성과보고서 | 8 | slide_01–08 |
| 071 하늘색 영업 전략 보고서 | 20 | slide_01–20 |
| 073 파랑 동종업계 분석 보고서 | 18 | slide_01–18 |
| 077 회색 사업 결과 보고서 | 2 | slide_01–02 |

`preview.html`을 열면 117장 전체, 덱 선택, 재현/재조립 전환, 원본과 나란히 비교, 확대 보기를 사용할 수 있습니다. 좌우 방향키로 확대 슬라이드를 이동합니다.

## 결과물

- `renders/final/replica/`: 원본 재현 PNG 117장, 각 1280×720.
- `renders/final/assembly/`: 컬렉션을 사용한 재조립 PNG 117장, 각 1280×720.
- `renders/library/`: foundation과 31개 요소의 83개 fixture를 light/dark로 렌더한 PNG 166장.
- `comparisons/final/`: 원본/재현 및 원본/재조립 개별 비교 JPG 234장. 비교 이미지의 캔버스는 2560×752이며, 두 슬라이드의 비율은 16:9로 유지합니다.
- `previews/`: 재현·재조립 각각 13개의 1280×720 시트와 전체 미리보기 JPG.
- `pdfs/replica-all.pdf`, `assembly-all.pdf`: 각각 117페이지의 전체 슬라이드 PDF. 덱별 PDF도 포함합니다.
- `pdfs/replica-sheets.pdf`, `assembly-sheets.pdf`: 각각 13페이지의 시트 PDF.
- `pdfs/library-light.pdf`, `library-dark.pdf`: 각각 83페이지의 라이브러리 PDF.
- `collection/business-prism/`: kit, foundation, 31개 요소, 83개 fixture, light/dark 시트 HTML.
- `review/`: 장별 개별 시각 검토, 최종 브라우저 검사, 최소 칸·대비 검사, SHA-256, 재조립 픽셀 비교, 무결성 기록.

라이브러리 전용 `business-prism.zip`의 최상위에는 `business-prism/` 폴더 하나만 있습니다. `rhetis-business-061-077-source.zip`은 소스·폰트·계약·참고 이미지를 포함하고, `rhetis-business-061-077-deliverables.zip`은 최종 이미지·PDF·비교·전체 미리보기·검수 기록을 포함합니다.

## 구조와 재조립

`src/decks/*.mjs`는 텍스트·배치·도형·차트·placeholder 데이터를 선언합니다. 덱 내부의 공통 헤더, 카드, 표, 차트, 기하 배경은 함수로 재사용합니다. `src/primitives.mjs`는 렌더러에 의존하지 않는 데이터 생성 API입니다.

`src/renderer.mjs`는 원본 재현 DOM을, `src/assembly.mjs`는 실제 컬렉션 CSS와 foundation의 `.page`→`.body`→`.group`, `card.parts@1`, `pill.parts@1`, `frame.picture@1`을 사용한 재조립 DOM을 만듭니다. 원본 배치와 타이포 역할은 페이지 작성 단계의 overrides로 지정합니다. 라이브러리 CSS가 표면·선·모서리·부품을 공급합니다. 표·차트의 수치 관계와 SVG 경로는 원본 데이터 그대로 유지합니다. 모든 31개 요소는 별도 fixture와 반응형 규칙을 갖추었습니다.

## 실행

Node.js 18+, Python 3.10+, Chromium이 필요합니다. Python 패키지는 `requirements.txt`를 참고하세요.

```sh
npm run build
python tools/render.py --round final
python tools/render.py --assembly --round final
python tools/audit-final.py
python tools/library-export.py
python tools/finish.py
python tools/verify.py
python tools/package.py
```

계약 도구를 그대로 실행하는 명령:

```sh
python tools/preview.py collection/business-prism contract/type-steps.json --out collection/business-prism/light.html
python tools/preview.py collection/business-prism contract/type-steps.json --dark --out collection/business-prism/dark.html
```

폰트는 실제 Pretendard 300–900, Gmarket Sans 300/500/700, Montserrat variable, Roboto Condensed variable 파일을 호스트에서 로드합니다. 컬렉션 CSS 자체는 계약에 따라 외부 리소스·`@font-face`를 포함하지 않습니다. 라이브러리 PDF와 PNG를 만들 때 호스트에 실제 폰트를 주입합니다.

## 해석과 남는 차이

사진·복잡한 3D 일러스트·기기 화면·이미지 아이콘은 사용자 지시에 따라 연한 회색 placeholder로 처리했습니다. 단순 도형, 차트, 표, 선형 배경과 종이 접힘은 HTML/CSS/SVG로 직접 그렸고 아이콘은 Lucide로 대체했습니다. 원본 이미지를 결과 화면에 깔지 않았습니다.

가장 어려운 부분은 065의 촘촘한 선형 물결, 073의 종이 접힘, 작은 차트 라벨과 복합 아이콘입니다. 벡터 곡률·아이콘 세부·서체의 비례에 차이가 남습니다. 069의 원본에는 상용 서체 `210 옴니고딕 030`이 명시되어 있지만 첨부에 폰트가 없어 Pretendard와 Roboto Condensed로 근사했습니다. 나머지 미확정 원본 서체도 실제 로드한 공개 폰트로 가장 가깝게 조정했습니다. 읽을 수 없는 작은 문구는 자연스러운 한국어 비즈니스 문장으로 작성했으며 위치별 결정은 덱 검수 기록에 남겼습니다.

`contract/REFERENCE-README.md`는 사용자가 계약으로 지정한 첨부 README 전체입니다. 문서 안의 계약과 예시는 구조·CSS·fixture 규칙으로 적용하고, 사용자 지시인 placeholder·1280×720·시각 검수·GitHub 제출 요구는 별도로 적용했습니다. 참고 이미지 안의 안내 문장은 화면 콘텐츠로 취급했습니다.
