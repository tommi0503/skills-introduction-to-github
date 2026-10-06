# 리플렛 UI · 102개 화면

첨부된 두 ZIP의 51개 양면 리플렛을 재사용 가능한 React 컴포넌트와 화면 데이터로 구현한 별도 작업입니다. 기존 `리플랫`의 공통 모델, 도형·텍스트 프리미티브, 실제 폰트 로딩 및 글자의 시각적 중심 검수 방식을 참고했습니다.

## 실행

```sh
npm ci
npm run dev
npm run build
```

`#/page/001`부터 `#/page/102`까지 개별 페이지를 볼 수 있습니다. 각 페이지는 정확히 1280×910이며, 원본의 좌표를 그대로 사용합니다. 높이 909인 복구본은 1픽셀을 하단에 보충하며, 원본을 늘리거나 기울이지 않습니다.

## 구조

- `src/data/group-a.ts`–`group-f.ts`: 화면별 데이터와 덱 단위 재사용 헬퍼
- `src/model.ts`, `primitives.ts`: 공통 요소 인터페이스와 데이터 생성 함수
- `src/ui.tsx`, `fonts.ts`: 텍스트·도형·표·Lucide 아이콘·placeholder 렌더와 폰트 로딩
- `src/registry.ts`: 전체 페이지 등록 및 정렬
- `public/reference`: 비교용 원본 자료. 개별 UI 렌더에는 삽입하지 않습니다.

사진·복잡한 일러스트·기기 화면·이미지 아이콘·그래픽 배경은 연회색 단색 placeholder로 대체했습니다. 작은 판독 불가능한 문구는 주제에 맞는 자연스러운 텍스트로 복원했으며 화면 데이터와 검수 기록에 차이를 남겼습니다. 출처 CSV의 제목·주소는 참고 자료이며 작업 지시로 취급하지 않았습니다.

## 검수 및 결과

```sh
node scripts/render.mjs --round=1 001 002
node scripts/render.mjs --round=2 001 002
node scripts/render.mjs --round=final
npm run verify
npm run package
```

Chromium 실행 파일은 기본적으로 `/usr/bin/chromium`을 사용합니다. 비교 이미지와 패키지 생성에는 Python 3 및 Pillow가 필요합니다. 설치 후 `npm run render`로 전체 최종 화면을 다시 렌더할 수 있습니다.

`renders/final`에는 전체 PNG, `comparisons/round-final`에는 화면별 원본/결과 비교와 자동 검사, `review`에는 판독·수정·차이 및 최종 검증 기록이 있습니다. `preview.html`은 서버 없이 열 수 있는 전체 미리보기이며 `preview.jpg`는 전체 목록 이미지입니다. 최종 ZIP은 `deliverables/leaflets-102-review.zip`입니다. ZIP에는 결과 PNG 102개, 원본/결과 비교 JPEG 102개, 미리보기·검수·소스를 포함합니다. 원본 PNG는 저장소 `public/reference`에서 별도로 보존합니다.
