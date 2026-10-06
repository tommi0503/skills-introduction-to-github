# Presentation 159 Clone

두 분할 ZIP의 참고 이미지 **159장, 53개 덱**을 데이터와 공통 React 컴포넌트로 구현합니다. 모든 개별 슬라이드는 **1280×720**이며, 원본 1600×900 좌표를 동일 비율 0.8로 변환합니다.

## 실행

```sh
npm ci
npm run dev
npm run build
npm run render -- --round=final
node scripts/verify.mjs
node scripts/graphics-inventory.mjs
python3 scripts/package.py
```

렌더·검수에는 `/usr/bin/chromium`, Python 3 및 Pillow가 필요합니다. 화면별 주소는 `#/slide/d01/s001`, 덱은 `#/deck/d01`, 원본/구현 비교는 `#/compare/d01`입니다. 모든 폰트는 npm 패키지에서 실제 정적 또는 가변 WOFF2를 로드합니다.

## 구조와 범위

- `src/model.ts`: 화면 데이터 계약. `src/primitives.ts`: 원본 좌표를 공통 캔버스 좌표로 변환하는 어댑터.
- `src/ui.tsx`: 텍스트·도형·placeholder·Lucide·표·차트·경로·chip 공통 렌더러. chip은 실제 폰트가 로드된 뒤 glyph의 시각 중심을 보정합니다.
- `src/graphics.tsx`: SVG 패턴·질감·일러스트 및 사용자 정의 벡터 경로·그라데이션. 요소별 CSS 그라데이션, fade 마스크, 혼합 모드를 지원합니다.
- `src/decks/group-a.ts`, `group-b.ts`, `group-c.ts` 및 C 그룹 보조 파일: 서로 분리된 53장씩의 화면 데이터.
- `public/reference/manifest.json`: 전체 원본 목록, 원본 식별자, SHA-256. 원본 JPG는 비교 화면에서만 사용하며 UI 캔버스 안에 넣지 않습니다.
- `provenance/`: 입력 ZIP 목록 및 첨부 README·CSV. 이 문서들은 선별 근거와 출처 데이터로 보존했으며 사용자의 구현 지시와 구분했습니다.
- `review/agent-*.json`: 최초 구현의 원본 및 비교 검수 이력.
- `review/graphics-agent-*.json`: 그래픽 개선 작업의 원본·1차 비교 개별 관찰과 수정 사항.
- `review/graphics-revision.json`: 이전 placeholder 수와 최신 SVG·그라데이션·fade 수, 남은 사진 영역의 전체 목록.
- `review/main-review.json`: 주 에이전트의 159장 최종 개별 비교 검수와 최종 PNG 해시.
- `review/verification.json`: 모든 production 화면의 실제 글자 영역, 폰트 family/style/weight, chip, 페이지 크기, source/renderer/PNG 해시 검사.

`presentation3-clone`의 공통 모델·요소 렌더러·갤러리·검수 흐름을 참고하여 별도 프로젝트를 만들었습니다. 기존 작업을 변경하지 않았고 `slides-clone` 소스는 확인하지 않았습니다.

## 재현 기준과 남는 차이

사진과 사진에 포함된 기기 화면은 단색 **#e5e5e5** placeholder로 바꿉니다. SVG로 생성 가능한 일러스트·패턴·로고·장식과 그래픽 배경은 실제 벡터와 CSS 그라데이션으로 구현합니다. transparent fade, 다중 그라데이션, SVG 그라데이션 및 grain 질감을 지원하며 원본의 색과 대비를 복원합니다. 원본의 도형·테두리·표·차트·텍스트와 Lucide로 표현 가능한 아이콘도 구현합니다.

원본은 폰트 메타데이터가 없는 JPG입니다. 실제 로드되는 폰트 중 자형이 가까운 것을 고르고 굵기·크기·자간·줄간격·줄바꿈을 맞췄으나 일부 자형과 장식 디테일은 다릅니다. 판독 불가능한 작은 UI 문구는 자연스러운 실제 문장으로 대체하고 페이지별 기록에 남깁니다. 회색으로 치환한 사진·기기 내부 문자는 이미지 영역의 일부로 처리합니다.

초기 구현 뒤 사용자 피드백에 따라 그래픽 치환 기준을 수정했습니다. `review/pre-graphics-revision/`는 이전 결과의 이력이며 최신 개선 검수와 구분합니다. 개선 작업에서는 담당 에이전트가 모든 원본과 1차 비교를 개별 확인하고, 주 에이전트가 최종 2차 비교를 개별 확인합니다. 전체 미리보기는 탐색용이며 개별 검수의 대체물로 사용하지 않습니다. 정상적인 원본 가장자리 장식 잘림만 개별 이유와 함께 허용합니다. 폰트·chip 오류는 잘림 예외로 숨기지 않습니다.

## 결과물

저장소 루트의 `presentation159-clone-renders.zip`에는 PNG 159장, 원본/결과 개별 비교 JPG 159장, 전체 미리보기, 검수 기록, 입력 목록, SHA-256 목록을 담습니다. `presentation159-clone-preview.jpg`에는 159장 전체가 포함됩니다. ZIP 생성 후 CRC·항목 해시·PNG 개수 및 크기·최종 검수 해시 일치를 확인합니다.
