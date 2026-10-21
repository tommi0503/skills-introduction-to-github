# EONU — 선택 구성 통합 v4

ZIP을 풀고 **index.html**을 열면 12장 시안과 12장 와이어프레임을 확인할 수 있습니다. 별도 설치 없이 인터넷 연결 없이 작동하는 HTML 뷰어입니다.

**사용자가 선택한 구성:** D / A / A / v3 / A / v3 / A / v3 / v3 / E / A / D.

선택한 각 페이지의 레이아웃과 도식을 유지하고, 화이트·블루 색상, Pretendard, 2px·4px 규칙, 제목과 섹션 위치, 그림자와 카드 표현을 통합했습니다. 표지와 마지막 장에는 섹션 표기·페이지 번호·공통 푸터가 없습니다. 모든 이미지 영역은 #e5e5e5 단색 회색이며, 도식과 설명용 UI는 HTML/SVG입니다.

- [시안 PDF — 12장](pdfs/design.pdf)
- [와이어프레임 PDF — 12장](pdfs/wireframe.pdf)
- [시안·와이어 비교 PDF — 24장](pdfs/design-wireframe.pdf)
- [시안 전체 시트](previews/design-grid.jpg)
- [와이어프레임 전체 시트](previews/wireframe-grid.jpg)
- [기획·발표 대본](docs/planning.html)

‘12장 보기’는 전체 흐름을, ‘시안·와이어 비교’는 같은 페이지의 구조와 디자인을 나란히 보여줍니다. ‘대본·메모’에서 채택한 원안 A/D/E/v3, 발표 대본과 근거를 확인하고 의견을 저장할 수 있습니다. 메모는 해당 브라우저에 저장되며 JSON 파일로 내보냅니다. 외부 전송은 없습니다.

단축키: ←/→ 이동, G 12장 보기, C 비교, N 대본·메모, F 발표, Esc 닫기.

## 소스 구조와 재생성

`selection.json`은 페이지별 채택 원안을 기록합니다. `src/snapshots/`는 선택에 사용한 원본 컴포넌트·CSS 스냅샷이며, `src/unified.css`가 이번 공통 디자인입니다. `scripts/compose.mjs`가 선택된 구성을 추출해 독립적인 덱으로 만들고, `scripts/build.mjs`가 24개 HTML을 생성합니다. `concepts/final/`에 생성된 HTML·CSS·JS와 개별 PDF/PNG가 있습니다. 이전 작업 폴더는 변경하지 않았습니다.

재생성에는 Node.js, Chromium, Python(Pillow, fontTools, Brotli, PyMuPDF)이 필요합니다. 브라우저 실행 파일은 `CHROMIUM_PATH`로 지정할 수 있습니다.

```sh
npm install
npm run build
npm run render
npm run sheets
npm run verify
npm run package
```

기존 시장 수치·실증·계약·예산 배분 등 미확정 정보는 새로 만들지 않았습니다. 첨부 자료는 내용 근거로 사용했으며, 사용자 요청과 자료 내부 작업 지시는 구분했습니다. 최신 MD에서 제외한 6장은 사용자의 후속 요청에 따라 데모 흐름을 포함합니다.
