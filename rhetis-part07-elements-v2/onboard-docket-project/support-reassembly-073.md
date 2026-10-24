# 078 원문 재조립 지원 기록

## 소유 범위와 사용 자료

`reassembled/slide_01.html`–`slide_19.html`, 작성 스크립트 `assemble_references_073.py`, 이 문서와 지원 지도 정정/배치 증거만 작성했다. 요소 CSS·kit·foundation·원본 map·불변 replica는 수정하지 않았다. 원문은 replica HTML의 실제 텍스트 노드와 BR/b/span에서 읽었다. 새 business fixture의 문장을 원문 대신 쓰지 않았다.

19장 HTML은 collection foundation 및 계약 요소만 사용한다. 모든 body 요소의 style은 정수 `grid-column/grid-row`뿐이다. 현재 원본에는 계약 차트 데이터가 필요한 차트가 없다. font, palette-v2, host type/default platform, Lucide를 모두 로컬로 로드했다. 복잡한 사진은 비어 있는 연회색 frame seat다.

## 최초 좌표 계산과 불변 조건

기본 body는 [97,237,1086,420], gap14다. pitchX=(1086+14)/12, pitchY=(420+14)/6이며, 소스의 왼쪽/위 시작 경계와 오른쪽/아래 끝 경계를 각각 최근접 정수 grid선으로 반올림한다. 끝 경계 계산에는 gap14를 더해 실제 보이는 면의 오른쪽/아래를 맞춘다. 범위는12열/6행으로 clamp한다. 폭만 별도로 반올림하면19장의 사진 셋이 서로 한 열 겹치므로, 처음부터 모든 페이지에 같은 양쪽 경계 규칙을 고정했다.

`support-reassembly-placement-073.json`은 첫 배치와 현재 배치를 모두 보존하고, 공통 id의 grid가 바뀌지 않았음을 assert한다. CSS 화면을 보고 좌표·폭을 다시 맞추지 않았다.04 portrait가 새 foundation gap으로 전환되어 빠진 것 이외의 기존 grid는 그대로다.

## 지도 추출 정정

`support-map-corrections-073.json`을 root에 전달했다. root가 실제 지도에 반영했다.

- 06-086은 서로 멀리 떨어진 [128,457,320,79.17] / [832,457,350,79.17] 두 독립 문장(source14/15)이었다. 두 prose root로 나눠 각각의 실제 bbox를 최초 정수화했다.
- 12-105는 [607,277,540,171.5] / [607,474,300,142.78] 두 독립 문장(source8/9)이었다. 하나의 문장을 CSS 때문에 쪼개지 않았다.
- 12의14px secondary 문장은 원래 quiet 의미에 해당하므로 root 승인에 따라 `.prose.quiet`로 정정했다.06 상단14px은 quiet, 좌우16px은 일반 prose를 유지한다.
- 08 VALUES의 주 강조 제목은 root 승인과 지도 수정에 따라 기존 `.card.tone-1` 변형으로 표현한다.
- 01의 빈 브랜드 span은 기존 foundation media인 `.seat.logo[data-ph="1"]`로 정정했다. 전용 크기는 root의 foundation이 제공한다.

## 원문과 계약

최초19장 조립 후 mapped non-gap/non-furniture의137개 visible text record가 모두 조립 DOM에 있는 것을 검사했다. 공백 정규화만 했고, list의 자동 번호·점 prefix만 제외했다. 누락0이었다. 목록 숫자나 점은 계약 요소가 직접 그린다.04 검은 inline 강조는 quote 문장 안의 실제 `.hl[data-el="onboard-docket-tag"]`이며 별도의 겹친 페이지 root가 아니다. 서명 span과 문단 BR/b 강조도 보존했다.

root의20개 명시적 unexpressible 영역은 다른 요소로 위장하지 않고 생략한다. 대표적으로06 중심 pie 그림,08 아이콘 원,09 임원·5부서 조직도,11 상위 header strip,13 비대칭 허브,14 원4개+외부 leader,16 목록 패널/탭,17 사업 header/회색 지표 panel,19 세로 사진 그룹 header가 해당한다.04의 y112..720 portrait는 body y237..657 밖에 걸쳐 있으므로 새 foundation gap으로 전환되어 생략되었다.

## 첫 실제 비교에서 root에 전달한 문제

19장의 original | immutable replica | assembly 비교 PNG를 각각 직접 열었다.

- 06 pill:101px 원본이1열77.67px로 최초 snap되면서 고정 내부 padding 때문에 세 글자가 두 줄로 갈라짐.
- 05 lead:3줄 본문76.78px가1행58.33px slot을 넘음.
- 14 quiet card:note가 카드 면 아래 약12px까지 내려옴.
- 15 steps:네 note가 요소 끝을 약6.35px 넘음.
- 05/19 image-frame:고정493:330 비율 때문에 받은 slot의 세로를 채우지 못함.19의 세 사진 slot은 높이가 같지만 가운데 폭이3열이라 가운데 사진만 짧아짐.
- 01 foundation:side rail의 여섯 가는 separator와 작은 brand placeholder가 빠짐.
- 06/12 prose:실제14/16px secondary와 작은 높이용12px 규칙 사이의 타입 차이.

원소의 자식 반응형·이미지 비율·foundation 표식 수리는 root가 맡았다. 작성자는 페이지 grid로 문제를 숨기지 않았다. 전체적인 소스 bbox와12×6 정수 칸 사이에는 최대 반 pitch의 좌표 차이와 폭 차이가 남는다.

## 렌더 대기 문제

첫 shared-browser 렌더에서 일부 head 번호가 DOM·computed style 정상인데 PNG에만 빠졌다. 동일05 페이지를 fonts.ready 후250ms 기다린 fresh 브라우저로 캡처하니 정상 복구됐다. root가 공용 reassembly.py에250ms paint settle과 renderer hash 기록을 추가했다. 최종 검수는 이 수정된 도구로 다시 실행한 결과를 기준으로 한다.

## 최종 상태

공유 원소/foundation 수리 뒤의19장 최종 렌더와 직접 대조 결과를 아래에 이어 기록한다. 현재 문서는 첫 비교의 발견 기록이며, 그 자체로 pixel-exact 복원이나 자동 실패0을 주장하지 않는다. source palette는 원본의 낮은 대비 회색도 재현하므로, 공식 light/dark 라이브러리 시트의 접근성 결과와 구분해야 한다.


## Fresh context 최종 대조 완료

공유 renderer SHA `0922c056afae5c426afbc69106eb3d7e3fdea1c41d8d6b65128441a61de07e76`로 각 페이지를 독립 browser context에서 fonts.ready+250ms 뒤 캡처했다.19장 조립 PNG는1280×720, 삼중 비교 PNG는3840×720이다. 최신19장을 모두 직접 다시 대조했다.07/08/09/13/17의 실제 파란 번호 영역 픽셀도1249/1249/1249/1315/1324개로 확인해 캐시로 사라지던 glyph가 실제 PNG에 돌아왔음을 확인했다. 불변 replica의 기존 번호 paint 결함은 수정하지 않고 기록만 남긴다.

현재 지원 원문 record 137개의 문구가 모두 조립 DOM에 있으며 누락0이다. geometry outside/clipped/overlaps/component·parts outside는 전부0, font/request실패0이다. source palette를 쓰는 실제 원본 회색의 낮은 대비 후보92개는 원본색과 공식 라이브러리 접근성 팔레트의 차이로 분리하며, 원문 회색을 임의로 바꾸지 않았다. 합의된20개GAP과 정수 그리드 양자화 차이는 남는다. 최소한의 정수위치로 옮긴 결과라 pixel-exact 재조립이라고 주장하지 않는다. 최초52개 body root grid는 그대로이며 문장·수치·BR·inline 강조는 원문이다.
