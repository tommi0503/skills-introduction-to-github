# Confluence 검수 기록

020 산학협력 제안서 4장, kit·foundation·56요소가 범위다. README 전체와 taxonomy 계약을 읽고 replica → 디자인 언어 → 컬렉션 → 라이브러리 검수 → 재조립 순으로 만들었다. 예시의 CSS 디자인은 복사하지 않았고, 필수 모범 fixture는 마크업·데이터를 보존했다.

## 재검수에서 철회한 판단

이전 결과의 진한 강조 글자, 균등 그리드에 따른 카드 높이 변경, 본문 크기 변경을 원본과의 허용 차이로 보았던 판단을 철회했다. 사용자의 충실도 재작업 요청 뒤 패키징을 멈추고 원본 네 장을 각각 다시 열었다. 페이지 디자인 CSS를 새로 넣지 않고 foundation·kit·요소 CSS와 계약 마크업을 수정했다. 원본 색은 review/assets/reference-style.css가 공급하며 collection CSS에는 색 값이 없다. 라이브러리 light/dark는 계약 기준 팔레트를 사용한다.

## 장별 수정과 남은 차이

|장|복원한 사항|남은 차이·대체|
|---|---|---|
|01|x701/y166 제목 lockup, 128단계 굵은 제목, 작은 연한 영문, 회색 보조제목, 원본 청록/파랑, 검은 제목과 설명의 세로 위치|좌측 3D와 QR은 회색 번호 seat. 맨 아래 판독 불가 3줄은 한국어 산학협력 설명으로 작성했다. 원본 폰트 미확정이며 제안서 자형의 폭·높이는 약 6px 차이가 남는다.|
|02|3열×2행 6개 목차, 카드346×152, 열간27/행간47, 53px 배지, 파랑·청록 교대 순서, 원본 회색 설명, 1px 구획선|상단 3D 책은 seat. 허용 폰트의 자형 때문에 제목 폭에 수 px 차이가 남는다.|
|03|원본 x420/y75 상단 카드766×115, 아래 카드242×433 및 y213, 열간20/행간23, 넓은 제목 띠, 흰 글자, 점선, 본문·수치 중앙정렬, 원본 데이터 전부|좌측 3D는 seat. 12×6은 유지하되 rail 페이지 행을 115px+나머지 5행으로 정했다. 원본 금액·이름과 글꼴의 획 모양이 완전히 같지는 않다.|
|04|367px 중심 원, 넓은 바탕 링, 원본 주제 좌표, 중앙의 흰 프로젝트/파랑 목표, 원본 색 번호, 두색 Lucide 조합|중앙 3D는 seat. 단순 아이콘은 실제 Lucide 2개씩을 조합했으며 원본 그림의 세부 윤곽과 차이가 있다. 원본 글자의 하단획을 밑줄로 잘못 해석했던 수정은 취소하고 추가 u/밑줄을 전부 제거했다.|

원본의 넓고 각진 한글 display의 정확한 family는 확인할 수 없다. 확대 crop의 후보 분석에서 제공된 Pretendard Variable이 외부 Gmarket 추정보다 가까웠으며 외부 family 추정은 철회했다. README 허용 목록의 Pretendard Variable을 실제 로드했고, 크기·굵기·자간으로 가까이 맞췄다. 외부 폰트를 허용 family 이름으로 위장하지 않았다. ③ 프로젝트 제목은 원본과 x95/y240, ④ 중앙 제목은 y301을 맞췄으며 자간을 별도 공유 토큰으로 조정했다.

## 팔레트와 계약 결정

원본의 채도가 높은 면에서 실제 픽셀을 읽어 host의 대표 강조를 #44cde5, #3858e3으로 정정했다. PNG에 리샘플링·압축에 따른 인접 색 변동이 있어 모든 픽셀을 동일한 단색이라고 단정하지 않았다. 원본의 낮은 대비를 진한 색으로 바꾸지 않았다. 기준 library palette와 원본 host palette 검사는 구분한다.

kit의 새로운 간격·radius·tracking·line·weight는 typed extension으로 선언했다. 조립본의 페이지별 inline style은 정수 grid-column/grid-row 배치뿐이다. ④ 넓은 캔버스는 foundation의 계약 클래스 .page.overrides를 쓰며, 56개 요소의 일반 페이지 그리드에는 영향을 주지 않는다. 큰 원과 주변 항목은 hub 요소가 그린다.

모범 구성은 동일 마크업·데이터 지시가 우선이므로 기존 wrapper .group/.stack, 기존 grid placement, ✹ 문자까지 보존했다. 그 밖의 fixture와 조립본은 빈 Lucide span을 쓰고 runtime에서 실제 SVG로 채운다. runtime과 Lucide 라이선스를 review assets에 포함했다.

## 검증과 산출

재검수는 큰 구조·팔레트, 타이포·아이콘, 통합 계약/최소칸의 세 묶음으로 진행했고, 각 묶음 안에서 자동 렌더 결과를 확인했다. 이전 결과를 그대로 통과로 취급하지 않았다. 도구의 폰트 CORS·selector 문제는 공용 도구를 수정한 뒤 재실행했다.

176개 요소 fixture와 foundation fixture 2개가 있다. 추가한 프로젝트 제목/프로젝트 수치 fixture도 원본 카드 구조를 실제 기준 팔레트 시트에서 검수한다. 모든 CSS의 포터블 사본을 assets/collection에 동일 바이트로 넣고 source-manifest.json에 SHA-256을 기록한다. 최종 수량·1280×720 크기·폰트 실패·잘림은 audit/verification 파일의 실제 마지막 결과를 따른다. 원본 비교 PNG는 2560×720이다.

자동 대비 검사의 donut/scatter/slope 경고는 면의 기하를 보지 않고 조상 conic-gradient/점 채움을 배경으로 잡는 경우를 포함한다. raw 경고를 삭제하지 않았고 light/dark 실제 PNG에서 텍스트가 놓인 구멍·점 바깥 바탕을 확인했다. 원본을 재현한 host의 낮은 대비도 raw audit에 남긴다.

Radial background는 원본의 중앙 밝기를 근사한 형태이므로 유지했다. 실제 exported pixel과 글자색의 대비 근거는 audit-gradient-evidence.json에 있다. 투명 radial stop을 흰 면으로 취급한 1.09 대비 경고를 없애기 위해 배경을 바꾸지 않았다. 원본 card label과 agenda note의 원본 host 색은 유지하고, 기준 library에는 대비가 나는 깊이 자리(a1-8/n7)를 배정했다.

최종 재작업 검증값: collection 352파일, 56요소, 요소 fixture176개+foundation2개. light/dark PDF는 각각178페이지이며 card/hub/agenda 최종15개 fixture 페이지를 다시 렌더해 전체 PDF의 동일 위치에 교체했다. 716개 full/minimum probe에서 clip0/fontFailure0/zeroElementRoot0, 마지막 card/hub/agenda 60probe는 clip0/overflow0/fontFailure0이다. replica·재조립은 각각4장 모두 clip0/overflow0/fontFailure0이다. PNG130장(페이지8/비교8/시트114)의 실제 크기와 PDF 페이지 크기는 verification.json에 전부 적었다. 포터블 CSS58개는 원본과 동일 바이트다.

마지막 raw 대비 경고는885건이다. light에서는 donut 구멍 배경의 오탐34건이 남고, 나머지는 dark의 투명 radial stop 및 도형 바깥 라벨 배경을 잘못 잡은 경고다. 기준 palette의 card 작은 label·agenda note와 홀수 배지는 실제 대비가 나는 역할 자리로 고쳤고 원본 host에서는 원래 값을 공급했다. dark agenda의 실제 배지 대비3은 a2-9/a1-1 짝으로 수정한 후 raw 경고도0이 됐다. 기준 배경에서 실제 픽셀을 확인한 기록은 audit-gradient-evidence.json을 참조한다. 원본과 100% 픽셀 동일하다고 주장하지 않으며 원본 폰트 자형과 Lucide 윤곽의 남은 차이는 위 표에 기록했다.
