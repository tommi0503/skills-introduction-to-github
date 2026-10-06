# 독립 통합 구조 검사

실제 registry에 import된 6개 모듈을 Vite/Chromium에서 불러와 47개 덱·1,057페이지·23,065개 element 항목을 검사했다. ignored *-seed.json은 제외했고 소스를 수정하지 않았다. 데이터·구조 검사이며 전체 1,057장의 새로운 시각 검수라고 주장하지 않는다.

## 확인된 문제

1. p026의 15개 페이지에 element object 대신 객체 키 문자열 234개가 들어 있었다. 실제 text object가 사라지고 무효 element가 렌더될 수 있다. 페이지별 index와 값을 JSON에 기록했고 주 에이전트에게 즉시 전달했다.
2. 설치된 Lucide의 1,506개 사용 이름을 전부 대조하여 p043/s04-09 Instagram 및 p080/s02-06 Facebook을 찾을 수 없었다. 현재 renderer는 Circle로 조용히 대체한다.
3. p069/s02-06의 원본 인용문은 실제 italic이다. live object의 italic:true는 renderer가 무시하는 필드다. 지원되는 fontStyle:'italic'와 실제 DM Sans italic face 로딩이 필요하다.

모두 주 에이전트에게 수정 요청을 전달했다. 본 JSON은 발견 당시 snapshot이며 수정 완료 상태를 추정하지 않는다.

## 데이터·경로 확인

x/y/w/h 및 숫자 필드와 path point에 비유효 숫자/누락은 없었다. 덱/페이지 ID 중복은 없고 모든 1,057 reference 경로가 실제 파일로 존재하며 deck/page ID와 일치한다. 브라우저 갤러리에 47개 링크가 있고 대표 p151의 deck/compare/slide route가 정상이다. 단일 결과 article은 1280×720이며 원본 img는 비교 페이지의 article 바깥에만 있다.

공통 ElementView에서 image kind는 항상 #e5e5e5 placeholder를 렌더한다. 실제 element fill/background/src/href 필드에 원본 screenshot embedding 후보가 없었다. 텍스트 runs는 renderer가 실제 표시하는 runs를 우선 검사했고, 보조 text와 합쳐 중복 문자열이라고 오판하지 않았다. 확정한 OCR gibberish, glyph contour path, 문구 대신 가짜 막대를 배치한 항목은 없다. 이는 자동·표본 검사에서 확인한 범위이며 모든 문장을 원본과 대조하여 완전성을 증명한 것은 아니다.

빈 text 56개와 chip 44개를 목록화했다. 원본 확인 표본은 빈 제목/의도적 양식/장식/axis slot 등을 포함하므로 일괄 결함으로 보지 않는다. 많은 가는 선을 가진 p112의 격자/차트, p127의 logo clearance, p055의 circular arc를 원본과 확인했다. Increament., Porpose, TOXICAL은 원본에도 존재하므로 OCR 오류로 지적하지 않았다.

## 재사용 구조

Deck/Slide/Element 타입, T/B/C/I/L/IC/P 좌표 adapter, SlideCanvas/ElementView, path/chart/table/Lucide/optical ChipLabel을 공유한다. 페이지 데이터·좌표 변환·렌더링·탐색의 책임은 분리되어 있다. SOLID 전 항목을 형식적으로 증명한 것은 아니다. 새로운 primitive 추가 시 ElementView의 kind 분기를 수정해야 하고 큰 deck 모듈은 유지보수 한계가 남는다. JSON type assertion은 구조 오류를 컴파일 단계에서 놓칠 수 있어 verify/render의 runtime schema 검사로 보완해야 한다.

App의 활성 route는 개별 ScaledSlide/SlideCanvas를 쓴다. ui.tsx의 ReferenceBoard sheet helper는 존재하지만 App에서 사용하지 않는다. 비교 route의 원본은 결과 canvas와 별도 영역에 표시된다. 자세한 검사 범위·확인 원본·snapshot hash·모든 의심 항목은 integration-structure-audit.json에 있다.


## Final resolution (2026-10-06T17:56:20.662941+00:00)

모든 owner 동결 이후 실제 Vite/Chromium registry 47덱·1057쪽·24524개 객체를 독립 재검사했다. 비객체·미지원 kind/field·필수 좌표 오류·비유한 수·중복 ID·누락 reference·미지원 Lucide 모두 0이다. 1692개 실제 icon 이름을 설치된 lucide-react와 대조했다. p026 문자열 spread, 브랜드 아이콘 누락, p069 italic 설정과 미지원 필드는 해결됐다. p069의 DM Sans italic 실제 로딩 import를 재확인한다.

빈 텍스트 후보 101개는 앞서 확인한 입력 서식·축/차트·부분 crop 공란을 포함하며 일괄 결함으로 분류하지 않았다. OCR 비언어·무모음 긴 단어 후보는 0개다. 갤러리 47개 링크, p151 deck/compare/slide 경로를 실제 브라우저에서 확인했고 결과 article 내 원본 img는 0개, 단일 페이지는 1280×720이다. 현재 snapshot과 실제 active source SHA를 JSON에 기록했다. 이 데이터·구조 재검사는 전체 1057 PNG 개별 시각 검수와 구분된다.

마지막 group-c.ts p127 보정 반영 후 실제 registry를 다시 읽었다 (2026-10-06T18:00:31.889041+00:00). 24524개 객체·1692개 icons, kind별 필수값과 전체 1057 원본 경로까지 재검사해 모두 오류 0. 최신 source SHA 6개는 JSON finalResolution과 일치한다.
