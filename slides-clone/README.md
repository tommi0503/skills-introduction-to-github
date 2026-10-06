# Slides Clone

32개 프레젠테이션 레퍼런스(public/reference/NN.jpg)를 React + Tailwind CSS v4 + lucide-react로 재현.

- 모든 슬라이드는 `SLIDE` = 1280×720(16:9), 평면·정방향 `<Slide>`. 레퍼런스 1장 = 덱 1개(`src/decks/dNN`), 여러 슬라이드가 모인 보드/기울어진 목업은 슬라이드별로 분리해 평면으로 재구성
- 렌더는 덱의 슬라이드를 2열 보드로 배치 (`Board`)
- 사진·일러스트·목업·로고·그래픽 배경·lucide 미지원 아이콘 → `ImagePlaceholder` (단색)
- 덱별 `theme.ts` · `data.ts` · `components.tsx` · `index.tsx`

```bash
cd slides-clone && npm install && npm run dev      # #/ 갤러리, #/NN 덱 보드
node scripts/screenshot.mjs [NN] && python3 scripts/view.py NN   # 렌더 + 레퍼런스 비교
node scripts/audit.mjs [NN]   # 레이아웃 검수: 슬라이드 밖으로 나간 텍스트·박스 넘침·텍스트 겹침·잘림 자동 검출
```
