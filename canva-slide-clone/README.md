# Canva Slide Clone

첨부한 Canva 참고 이미지 190장(17개 템플릿)을 기반으로 만든 독립적인 UI 구현입니다. 앞선 slide-gen-clone의 공통 UI 구조와 렌더 방식을 확장했습니다.

```bash
npm ci
npm run dev
```

갤러리에서 템플릿을 선택하거나 `#/slide/c01/s01`, `#/deck/c01`, `#/compare/c01`로 개별 화면·전체 모음·원본 대조를 확인할 수 있습니다. 화면은 모두 기울이지 않은1280×720입니다.

`src/model.ts`는 데이터 계약, `src/primitives.ts`는1600×900원본 좌표 변환, `src/ui.tsx`는 재사용 렌더러입니다. 각 템플릿의 반복 제목·카드·표는 그룹 내부의 공통 함수로 구성합니다. 칩은 CSS 정렬에 폰트의 실제 글자 경계 보정을 더해 가운데에 놓습니다. 폰트·굵기·자간·줄간격은 요소별로 지정합니다.

사진·화면 이미지·복잡한 일러스트와 그래픽 배경은 이전 요청에 따라 회색 단색 플레이스홀더입니다. 원본 JPG는 비교 화면에서만 사용합니다. `public/reference/manifest.json`에 원본 파일명과 템플릿 순서를 보존했습니다. 첨부 README와 CSV는 자료의 설명과 출처로만 사용했습니다.

```bash
npm run build
npm run render -- --round=final
node scripts/verify.mjs
python3 scripts/package.py
```

렌더와 검증은 Chromium(`/usr/bin/chromium`), 비교·패키징은 Python Pillow를 사용합니다. 원본 대조는 템플릿별 두 차례 비교·수정과 마지막 통합 검토까지 세 차례로 제한합니다. 상세 기록은 `review/`에 있습니다. 최종 ZIP에는190개 개별 PNG와17개 템플릿 모음,190개 원본 대조 이미지, 검수 기록이 포함됩니다.
