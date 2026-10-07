# C 덱 품질 검수 기록

담당 p110(20), p112(31), p119(18), p127(36), p143(20), p145(36), 총 161페이지. 1280×720 독립 페이지를 baseline→개선→통합 순으로 원본과 개별 비교했다. 최신 통합 PNG가 이전에 실제 열람한 PNG와 동일한 페이지는 byte SHA로 연결하고, 달라진 페이지는 최신 비교 이미지를 직접 다시 열었다. production final은 별도 SHA 연결/실제뷰 후 최종 확인한다.

- 타이포그래피: Manrope, Poppins, Roboto 실제 variable weight와 Roboto italic, Playfair Display italic을 로드했다. 제목/본문/카드 행수, 줄간격, 굵기, 폭, chip 시각적 중심을 조정했다. p112 카드를 좁히고 제목 및 본문 기준선을 개별 원본과 맞췄다.
- p119: 18개 variant별 카드 제목·본문을 독립 좌표로 조정했다. 배경 곡선/종이비행기는 SVG이며 비행기 높이/방향/잘림을 바로잡았다. 3색 band 위치를 올렸고, 정면 아치·puzzle3piece·6개 분리층은 원본 구조에 맞춘 별도 SVG이다. 원본처럼 gloss가 있는 복잡한 3D 투영·curve는 근사치가 남아 있다.
- p127: 밝은 palette색상을 원본 표본 median blue #327ef5 / gold #fddd70 / purple #7c64f0 / green #acee8d로 맞췄다. documented primary HEX는 유지했다. Clash Display 공식 폰트 URL은 403으로 확보하지 못해 Inter 대체를 기록한다. Maxx 로고 글자 형태/가로비는 이 대체로 원본과 차이가 있다.
- p145: 실제 개별뷰로 자동검사에서 찾지 못한 pie범례/본문 중첩, axis 100%와 white stat의 중복 재배치, 카드 본문8줄 초과, leaf도형과 본문의 겹침을 발견·수정했다. s03-09의 pie조각이 filter에 삭제되고 area레이어가 white로 전부 덮인 문제를 바로잡아 6컬러 누적 SVG를 복원했다. 단일 페이지 새 캡처와 비교로 마지막 수정 반영을 확인했다.
- 단순 leaf/방사능/구/독일16주/worldland globe/map/법률 contour/brand mockup틀·diagram·chart를 재사용 SVG·DOM으로 구현했다. 공통 world dateline수정 후 globe/map에서 seam줄무늬가 없는 실제 결과를 확인했다.

원본 저해상도에서 읽지 못하는 본문과 작은 chart수치는 자연스러운 문구·typed 합리적 숫자로 대체했다. 일부 원본 cell은 아래쪽 자체가 흰 영역으로 잘려 있어 보이지 않는 하단 layout을 일관된 페이지 구조로 완성했다. 사진·복잡한 삽화·device화면 내용만 연한 회색 placeholder로 남겼다.

자동검사: build/typecheck 성공, C 최신 렌더 실제크기1280×720, fontready 후 캡처. p127 AaBb specimen의 의도된 stage잘림2개는 original에 대응하는 expected clip으로 기록한다. production final 자동검사와 PNG/ref SHA 연결은 주 에이전트가 전체 통합 렌더 후 수행한다.
