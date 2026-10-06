# Presentation 4 Clone — 차트·다이어그램 77장

첨부 `프레젠테이션_차트_다이어그램_추가77장.zip`의 실제 참고 이미지 **43개 덱, 77장 전체**를 구현합니다. 기존 작업은 보존했고 `slides-clone`은 확인하지 않았습니다. 원본은 모두 1600×900이며 결과는 같은 비율의 1280×720입니다.

```bash
cd presentation4-clone
npm ci --cache /workspace/.npm-cache
npm run dev -- --host 127.0.0.1 --port 5297 --strictPort
```

갤러리 `#/`, 덱 `#/deck/p01`, 원본 대조 `#/compare/p01`, 단일 슬라이드 `#/slide/p01/s11`을 제공합니다. 덱과 비교 화면의 제목 링크로 개별 페이지를 열 수 있습니다. 원본 JPG는 비교 화면에서만 사용합니다.

## 구성

- `src/model.ts`: 화면 데이터 계약
- `src/primitives.ts`: 1600×900 디자인 좌표에서 1280×720 출력으로 비율을 유지하는 어댑터
- `src/ui.tsx`: 텍스트, 상자, 도형, 벡터 경로, Lucide 아이콘, 차트, 표, placeholder, 글자 경계 기반 칩 중심 보정
- `src/decks/group-a.ts`: p01–p15, 25장
- `src/decks/group-b.ts`: p16–p33, 23장
- `src/decks/group-c.ts`: p34–p43, 29장
- `public/reference/manifest.json`: 원본 경로와 화면의 완전한 대응 목록
- `review/inventory.md`: 전체 작업 범위

화면 데이터와 공통 컴포넌트의 책임을 분리하며 반복 도형·차트·카드를 팩토리로 구성합니다. 사진·복잡한 일러스트·복합 이미지 아이콘·기기 화면·그래픽 배경은 연한 회색 단색 placeholder입니다. 읽을 수 있는 글자는 원문을 옮기며, 판독이 어려운 부분의 대체 문구와 폰트 차이는 검수 기록에 표시합니다. 원본 편집 파일의 폰트 메타데이터가 없으므로 동일 폰트 여부를 단정하지 않습니다. 사용한 대체 폰트와 실제 굵기는 로컬 폰트 파일로 로드합니다.

## 렌더·검수

```bash
npm run build
npm run render -- --round=final --production
node scripts/verify.mjs
python3 scripts/package.py
```

Chromium `/usr/bin/chromium`과 Python Pillow가 필요합니다. 1·2차 담당자 비교 후 주 에이전트가 3차 최종 통합 검수를 수행합니다. 연락처 시트는 탐색 용도이고 원본/결과를 나란히 둔 개별 이미지가 검수 대상입니다.

자동 검사는 77장 전체의 페이지 크기, 글자 영역 초과, 부모에 의한 잘림, 폰트 파일 로딩, chip의 실제 글자 중심, placeholder 색상, 스크린샷 삽입 여부를 확인합니다. 데이터·공통 렌더러·PNG SHA-256 해시로 마지막 수정과 최종 결과가 일치하는지 확인합니다. 최종 결과는 빌드된 production 서버에서 캡처합니다.

`../presentation4-clone-renders.zip`에는 전체 PNG 77장, 개별 원본/결과 비교 77장, 덱 모음, 전체 미리보기, 검수 기록, 이미지 목록과 해시 manifest가 포함됩니다. `../presentation4-clone-preview.jpg`는 77장 전체 미리보기입니다.
