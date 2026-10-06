# 리플랫

첨부 `miricanvas_leaflet_large_144.zip`의 72종 브로셔 앞·뒷면을 각 접지면으로 나누어 구현합니다. 72종 × 앞면 3페이지·뒷면 3페이지 = 독립 페이지 432개입니다. 앞·뒷면 144장을 펼쳐 보는 화면도 제공합니다.

```bash
npm ci --cache /workspace/.npm-cache
npm run dev -- --host 127.0.0.1 --port 5297 --strictPort
```

`#/brochure/l01`은 접지면 6페이지, `#/page/l01/s01-p1`은 독립 페이지, `#/unfold/l01`은 펼침, `#/compare/l01`은 원본 비교입니다. 모든 PNG 캔버스는 1280×720입니다. 세로형 접지면은 중앙에 비율을 유지하여 배치합니다. 펼침 이미지의 좌측·중앙·우측 순서대로 p1/p2/p3을 정의하며 접지나 읽기 순서를 임의 변경하지 않습니다.

`src/model.ts`는 요소·페이지·패치 계약, `src/primitives.ts`는 원본 좌표 기반 재사용 UI, `src/ui.tsx`는 폰트·칩 중심·단색 이미지 영역·차트 렌더러, `src/registry.ts`는 앞·뒤 원본과 여섯 접지면 사이의 변환을 담당합니다. 공유 요소를 접지 경계에서 정확히 잘라 각각의 페이지를 구성하고, 가로·세로에 동일한 배율을 적용합니다. `src/data/patch-*.ts`는 여섯 담당자의 화면 데이터입니다.

사진·기기·복잡한 이미지 아이콘·일러스트·그래픽 배경은 단색 #e5e5e5로 표시합니다. 기본 도형·표·차트·텍스트와 Lucide 아이콘은 실제 UI입니다. 참고 이미지는 원본 비교 화면에서만 사용합니다. 판독할 수 없는 작은 문구는 이번 지시에 따라 자연스러운 내용으로 작성하고 검수 기록에 표시합니다. 일반 텍스트를 회색 선으로 대체하지 않습니다.

```bash
npm run build
npm run render -- --round=final
node scripts/verify.mjs
python3 scripts/package.py
```

렌더에는 `/usr/bin/chromium`, 비교·패키징에는 Python Pillow가 필요합니다. `extract-layout.py`는 참고 자료 분석을 위한 선택적 도구로 SciPy, NumPy, 한국어 Tesseract 데이터가 필요하며 일반 실행·빌드에는 필요하지 않습니다. 추출 결과는 참고 초안이며 담당자가 원본을 읽어 제목·본문·카드·표를 복원하고 검수합니다.

PNG 576장과 검수 기록은 `/workspace/shared/downloads/leaflet-renders.zip`, 원본·구현 접지면 비교 모음 72장은 `leaflet-review.zip`에 별도로 패키징합니다. 제출본은 저장소 루트의 같은 파일명으로 제공합니다. 의존성·빌드 산출물·중간 렌더는 Git에서 제외합니다.
