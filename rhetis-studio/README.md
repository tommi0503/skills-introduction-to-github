# Rhetis Studio / Studio Spectrum

선정된 Canva 참고 10개 덱 107장을 1280×720 DOM/CSS/SVG로 재현하고, 디자인 언어를 `studio-spectrum` Rhetis 컬렉션으로 구성했습니다. 기존 프로젝트는 수정하지 않고 이 폴더에 모든 작업을 분리했습니다.

## 열기

- `exports/index.html`: 설치 없이 열 수 있는 전체 미리보기. PNG, 원본과 결과 비교, 재조립 이미지와 PDF 링크.
- `exports/replica-107-slides.pdf`: 재현 슬라이드 107장. 브라우저 인쇄 PDF로 텍스트를 보존합니다.
- `exports/assembled-107-slides.pdf`: 같은 콘텐츠를 컬렉션 구조와 타입 단계로 재조립한 107장.
- `public/sheets/light.html`, `dark.html`: 31요소와 foundation 전체 fixture 시트.
- `review/FINAL-REVIEW.md`: 통합 검수, 남는 차이, 판단과 한계.

## 개발

Node 22.12+ 사용. `npm ci`, `npm run dev`, `npm run build`.

```
npx tsc --noEmit
node scripts/render.mjs --round=final
node scripts/render.mjs --round=final --mode=assembled
python scripts/compare.py --round=final
node scripts/export.mjs
python scripts/verify.py
```

렌더 및 PDF 스크립트는 Vite 서버 `http://127.0.0.1:5173`와 `/usr/bin/chromium`을 사용합니다. 호스트에 따라 Chromium 경로를 변경할 수 있습니다.

## 구조

- `src/ui.tsx`: 절대 좌표 page authoring primitive, 실제 폰트 기반 optical centering.
- `src/decks/`: 덱별 데이터 및 반복 layout/component. 원본1600×900에서0.8배 좌표 변환.
- `src/library.tsx`, `rebuild.css`: 원본 콘텐츠와 geometry를 유지하며 card/metric/image-frame 계약 root로 조립하는 adapter. font-size 선언은 계약의 타입 단계를 사용하고, page-authoring의 균일 확대/축소로 원본의 실제 글자 크기와 자간을 보존합니다.
- `collections/studio-spectrum/`: 독립 반입용 kit + foundation + 31개 요소. 각각2개이상 fixture, 총95개 요소 fixture와2개 foundation fixture.
- `contract/`: 제공받은 계약 원본. `REFERENCE-README.md`는 첨부 계약 원문이며 일반 작업 지시와 구분해서 보관했습니다.
- `renders/final/`: replica107 PNG + assembled107 PNG.
- `comparisons/final/`: 원본/구현 좌우비교107장.
- `public/reference/`: 원본107장. 결과 UI는 이 파일을 이미지나 배경으로 사용하지 않습니다.
- `scripts/`: 재현 가능한 build/render/compare/export/package/verify 도구.

## 재조립 범위

컬렉션은10덱의 공통 언어(편집형 여백, 가는 rule, 강한 타이포, navy/red/lime/green 강조)를 하나의 일관된 kit로 해석했습니다. 각 덱의 geometry와 원본색을 유지하는 page-author overrides는 컬렉션 밖에 둡니다. 107장 재조립은 같은 source 콘텐츠를 foundation/page grid 및 card/metric/image-frame으로 다시 구성합니다. 슬라이드 특유의 단순 도형·표·차트의 세부 geometry는 page authoring 데이터로 공유합니다. 따라서 재조립은 Rhetis 서비스의 실제 importer를 통한 왕복 검증 결과가 아니라, 제공된 HTML/CSS 계약을 사용하는 로컬 브라우저 검증 결과입니다. 정식 importer는 제공되지 않았습니다.

31개 고수준 요소의 독립 동작·반응형·라이트/다크는 fixture 시트와 최소칸 검수에서 확인합니다. 원본에는 없는 funnel, pyramid, hierarchy 등은 같은 선·모서리·강조 언어로 새로 설계했습니다.

## 폰트와 이미지

Pretendard variable, Noto Sans KR(300/400/500/600/700), Noto Serif KR(400/700), Poppins(400/600/700/800), Anton, DM Serif Display regular/italic, Bodoni Moda variable을 실제로 로드합니다. Times 계열은 Nimbus Roman, Arial 계열은 Liberation Sans를 로컬 배포합니다. npm 폰트 패키지와 `public/fonts/*LICENSE*`의 라이선스를 따릅니다. 원본에는 폰트 메타데이터가 없어 일부 자형 차이가 남습니다.

사진, 복잡한 삽화와 기기 화면은 단색 연회색 placeholder입니다. 추가 규칙에 따라 SVG로 그릴 수 있는 배경·그라디언트는 직접 재현합니다. 단순 도형, 차트, 표, 텍스트, Lucide로 표현 가능한 아이콘은 구현했습니다. 판독 불가 소문구는 덱별 검수 기록에 밝히고 한국어 문장으로 대체했으며, 선으로 대신하지 않았습니다.
