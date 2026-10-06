# Presentation 3 Clone

첨부 `presentation3.zip`의 이미지 36개를 바탕으로 만든 독립적인 UI 구현입니다. 이전 Canva 작업의 공통 데이터 모델·렌더러를 확장했습니다. 기존 프로젝트는 변경하지 않습니다.

```bash
npm ci --cache /workspace/.npm-cache
npm run dev -- --host 127.0.0.1 --port 5296 --strictPort
```

갤러리와 `#/slide/p01/s01`, `#/deck/p01`, `#/compare/p01`에서 각각 단일 화면·전체 모음·원본 대조를 확인할 수 있습니다. 모든 화면은 기울이지 않은 1280×720입니다. 4:3 원본은 비율을 유지하고 여백을 더해 같은 캔버스 안에 배치합니다. 배치는 `public/reference/manifest.json`에 기록했습니다.

`src/model.ts`는 데이터 계약, `src/primitives.ts`는 정규화한 1600×900 좌표와 1280×720 출력 사이의 변환, `src/ui.tsx`는 공통 컴포넌트입니다. 화면별 데이터는 `src/decks/group-*.ts`에 있으며 반복 카드·행·목차·표는 재사용 함수로 구성합니다. 칩은 실제 글자 경계를 기준으로 중심을 보정합니다. 글꼴, 실제 굵기, 자간, 행간은 각 요소에서 지정합니다.

이전 요청에 따라 사진·기기 화면·복잡한 일러스트·그래픽과 그라데이션 배경은 연한 회색 단색 placeholder입니다. 도형·차트·표·텍스트는 실제 UI로 구현합니다. 참고 JPG는 비교 화면에서만 사용하며, 구현 화면에 스크린샷을 포함하지 않습니다. 해상도가 작은 원본의 판독 한계와 폰트 차이는 검수 기록에 표시합니다.

```bash
npm run build
npm run render -- --round=final
node scripts/verify.mjs
python3 scripts/package.py
```

렌더와 검증은 Chromium(`/usr/bin/chromium`), 비교·패키징은 Python Pillow를 사용합니다. 각 화면은 담당 에이전트의 두 차례 비교·수정과 주 에이전트의 마지막 통합 검토까지 세 차례 범위에서 검수합니다. ZIP은 `/workspace/shared/downloads/presentation3-clone-renders.zip`에 생성하며 개별 PNG, 비교 이미지, 전체 미리보기와 검수 기록을 포함합니다.
