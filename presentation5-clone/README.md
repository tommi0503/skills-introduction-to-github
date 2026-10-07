# Presentation 5 Clone — Envato 참고 시트 분할

두 첨부 ZIP의 **47개 덱·117개 참고 이미지**를 **1,057개 독립 슬라이드 페이지**로 구현하는 프로젝트입니다. 모든 결과 캔버스는 **1280×720**입니다. `presentation3-clone`의 공통 모델/렌더러 구조와 `presentation4-clone`의 실제 브라우저 검수 도구를 바탕으로 새 폴더에서 작업합니다. 기존 프로젝트를 보존했고 `slides-clone`은 확인하지 않았습니다.

```bash
cd presentation5-clone
npm ci --cache /tmp/presentation5-npm-cache --no-audit --no-fund
npm run dev -- --host 127.0.0.1 --port 5298 --strictPort
```

갤러리 `#/`, 덱 `#/deck/p004`, 개별 원본 비교 `#/compare/p004`, 단일 페이지 `#/slide/p004/s02-01`을 제공합니다. ID의 `p004`는 참고 덱 번호이고 `s02-01`은 두 번째 참고 이미지 안의 첫 번째 슬라이드입니다. 결과 UI는 시트가 아니라 각각 독립된 페이지이며, 갤러리의 축소 미리보기는 탐색용입니다.

## 구성과 표현

- `src/model.ts`: 요소·슬라이드·덱의 데이터 계약
- `src/primitives.ts`: 1600×900 디자인 좌표를 동일 비율의 1280×720로 변환
- `src/ui.tsx`: 공통 텍스트·chip·도형·벡터 경로·표·차트·Lucide 아이콘·SVG 장면·placeholder 렌더러
- `src/graphics`: 담당별 SVG 장면과 재사용 가능한 지도 경계 데이터
- `src/decks/group-*.ts`: 담당 파일을 분리한 6개 구성 모듈과 덱별 데이터/팩토리
- `public/sheets`: 변형하지 않은 원본 참고 이미지 117개
- `public/reference`: 각 슬라이드의 자연 크기 참고 crop
- `public/reference/manifest.json`: 전체 시트→개별 페이지 좌표·자연 크기·잘린 영역 대응
- `review`: 전체 범위, 판독 불가 문구, 복원 가정, 개별 비교·수정 및 자동 검사 기록

사진·복잡한 사진 기반 일러스트·기기 화면은 #e5e5e5 단색 placeholder입니다. 품질 개선 요청에 따라 SVG로 재현 가능한 리본·입체 도형·지도·기기 외곽·그래픽 장식은 실제 벡터 컴포넌트로 구현합니다. 단순 도형·표·차트·텍스트와 Lucide로 표현 가능한 아이콘도 컴포넌트로 구현합니다. 원본 시트를 결과 화면의 배경에 삽입하지 않습니다. 원본이 작아 판독하지 못하는 문구는 정상적인 대체 문구로 작성하고 기록합니다. 텍스트를 선이나 글자 실루엣 벡터로 흉내 내지 않습니다.

실제 폰트 파일과 굵기를 로컬 의존성으로 로드합니다. 원본 편집 파일의 폰트 메타데이터가 없는 곳은 비슷한 글꼴로 근사하고 차이를 기록합니다. chip은 글자의 실제 경계를 측정해 상하·좌우의 시각적 중앙을 보정합니다. 스티커처럼 원본의 개별 요소가 회전한 경우만 요소의 회전을 적용하고, 화면 전체는 기울이거나 비율을 왜곡하지 않습니다.

`p127`의 Clash Display는 올바른 글꼴 파일과 배포 조건을 확보하지 못해 실제 로드한 Inter로 근사했습니다. 해당 차이는 검수 기록에 남깁니다.

71개 타일은 원본 시트의 가장자리에서 일부 잘려 있습니다. 같은 시트의 완전한 슬라이드로 전체 타일 크기를 추정해 참고 crop을 흰색 padding으로 보존합니다. 보이는 원본 픽셀을 늘려 누락 영역을 채우지 않습니다. 결과의 복원 가정은 해당 페이지의 검수 기록에 남깁니다.

`p105/s03-25`는 시트에 포함된 218×377 세로형 Timeline 한 장입니다. 이를 여러 장으로 잘라내지 않고 1280×720 캔버스 안에 비율을 유지하여 배치합니다. 이 시트의 불규칙한 타일 경계 수정과 ID 대응은 `review/group-b-p105-crop-correction.json`에 기록했습니다.

## 검수와 재생성

```bash
node scripts/collect.mjs
npm run build
npm run render -- --round=final --production
npm run verify
python3 scripts/finalize-quality-review.py
npm run package
```

Chromium `/usr/bin/chromium`과 Python Pillow가 필요합니다. 공통 구성·데이터 변경 후 최종 렌더를 다시 생성해야 합니다. 검수 도구는 1,057장 전체의 크기, 글자 영역 초과/잘림, 실제 폰트 로딩, chip의 글자 중심, placeholder 색상, 원본 스크린샷 삽입 여부를 검사합니다. 데이터·공통 렌더러·PNG SHA-256이 최종 소스와 일치하는지도 확인합니다. 비교 원본은 비율을 유지하여 확대하고, 결과는 production 빌드에서 실제 브라우저로 캡처합니다.

담당자별 1·2차 비교와 주 에이전트의 3차 통합 검수를 수행합니다. 담당자는 모든 페이지를 원본/결과의 개별 이미지로 확인하고, 주 에이전트는 47개 덱의 대표 페이지와 요청한 보정 페이지를 개별 최종 확인합니다. 연락처 시트는 탐색용입니다. 이전에 개별 검토한 브라우저 PNG와 원본이 최종 파일과 byte 단위로 같은 경우에는 그 증빙을 보존합니다. 비교 이미지의 상단 round 표기만 바뀐 경우도 실제 페이지 픽셀을 독립 검증하고, 당시 열람한 비교 파일을 ZIP에 포함합니다.

## 제출 파일

개선본 `../presentation5-clone-quality-v2-part-XX.zip`은 소스·참고 이미지·전체 PNG·개별 비교·검수 기록을 포함하며, 모든 part를 같은 폴더에 압축 해제합니다. 각 ZIP은 독립적으로 열리고 GitHub 단일 파일 제한보다 작게 패키징합니다. `node_modules`, `dist`, 중간 검수 결과는 제외합니다. 이전 제출 ZIP은 별도로 보존합니다.

`../presentation5-clone-quality-v2-preview.jpg`는 개선본 전체 미리보기이며, 읽기 쉬운 20장 단위 미리보기는 `review/preview-pages`에 있습니다. ZIP의 `presentation5-clone/preview.html`은 설치 없이 로컬 브라우저에서 전체 PNG와 개별 비교를 여는 미리보기입니다. ZIP의 해시와 수량은 `../presentation5-clone-quality-v2-downloads.json` 및 `review/archive-integrity.json`에 기록합니다. 새 개별 재검수 증거는 `review/quality`에 있고, 이전 검수는 `review/history`에서 확인할 수 있습니다.

Git에는 소스·참고 자료·검수 기록·미리보기·ZIP을 저장합니다. 큰 PNG 및 비교 JPG는 ZIP에 모두 포함하며 별도 중복 커밋하지 않습니다. `preview.html`은 모든 part ZIP을 같은 폴더에 압축 해제한 뒤 열거나, 소스에서 위 명령으로 렌더를 생성한 뒤 사용합니다.
