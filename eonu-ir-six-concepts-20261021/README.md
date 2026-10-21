# EONU — six design concepts

ZIP을 풀고 **index.html**을 여세요. 인터넷 연결 없이 6개 안의 디자인·와이어프레임을 살펴볼 수 있습니다.

각 안은 **12장**이며 총 디자인 72장 + 와이어프레임 72장입니다. `concepts/a`부터 `concepts/f`까지 각각의 소스, 24개 HTML, PDF 2개, 그리드 시트 2개가 있습니다. `previews/all-designs-grid.jpg`는 72장을 같은 페이지별로 비교하는 전체 시트입니다. `pdfs/all-design.pdf`는 6개 디자인을 합친 72쪽 PDF입니다.

상단 시안 탭은 현재 페이지를 유지합니다. **6안 비교 / 12장 / 대본·메모 / 발표**를 사용할 수 있습니다. 메모는 브라우저에만 저장되며 JSON으로 내보낼 수 있습니다. 서버로 전송되지 않습니다.

전체 기획과 대본: [docs/planning.html](docs/planning.html). 방향별 차이와 검수 방법: [docs/design-review.md](docs/design-review.md).

## 재생성

Node.js, Chromium, Python(Pillow, fontTools, Brotli, PyMuPDF)이 필요합니다. 뷰어를 열기만 할 때는 설치가 필요 없습니다.

```sh
npm install
npm run build
npm run render
python3 scripts/sheets.py
npm run verify
python3 scripts/package.py
```

`CHROMIUM_PATH`로 Chromium 위치를 지정할 수 있습니다. 기본값은 `/usr/bin/chromium`입니다. 렌더는 로컬 HTTP 서버를 사용합니다. CSS와 소스 해시, PDF 페이지 수, 텍스트 경계, 폰트, 섹션 좌표, 탐색·메모 동작을 `review/`에 기록합니다.

기존 제작물은 수정하지 않았습니다. 이번 6개 안만 별도 폴더에 생성했습니다. Pretendard 라이선스는 `shared/fonts/`에 포함되어 있습니다.
