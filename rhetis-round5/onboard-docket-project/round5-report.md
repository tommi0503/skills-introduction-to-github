# Onboard Docket · round5

replica의 HTML·PNG·폰트는 변경하지 않았다. 관측된 27개 디자인만 남겼다. 44개 원형 미관측 일반 요소를 제거했다. 각 요소의 출처 수치를 비율과 컨테이너 단위로 바꿨으며, 연결선은 전체 멤버를 가진 요소가 소유한다.

## 새 디자인 폴더

- `card--icon/` ← replica 11
- `card--statement/` ← replica 11
- `card--caption/` ← replica 14
- `card--photo-caption/` ← replica 19
- `headline--plain/` ← replica 05
- `headline--center/` ← replica 11
- `list--ruled/` ← replica 16
- `steps--columns/` ← replica 10
- `chart-donut--triad/` ← replica 06
- `venn--icons/` ← replica 08
- `hub--semicircle/` ← replica 13
- `steps--topics/` ← replica 14

## 패널·차트·삭제

- 11: foundation `.panel.band`가 6개 카드 위 제목 띠를 소유한다.
- 16: `.panel.tabbed` 3개가 겹치는 탭·흰 테두리·회색 판·그림자를 소유한다. 내부는 `list--ruled`다.
- 17: `.panel.kpi` 3개가 왼쪽 제목 면과 오른쪽 지표 면을 소유한다. `.stats`는 수치와 문구만 그린다.
- 19: `.panel.vertical`이 세로 제목과 사진 3열·설명을 묶는다.
- 04: foundation `.seat.tall`이 세로 사진을 배치한다. 모든 복잡한 이미지 영역은 연회색 placeholder다.
- 06: `chart-donut--triad`가 세 조각, 리더 선, 아래 설명과 포크를 함께 소유한다.
- 08: `venn--icons`가 겹친 원과 세 아이콘 위치를 소유한다.
- 13: `hub--semicircle`이 반원·4개 노드·번호·노치 라벨·설명을 소유한다.
- 14: `steps--topics`가 둥근 연결 레일·4개 원·아래 노트 타일을 소유한다.
- 삭제 목록: `round5-deleted-generic.json`의 44종. 요소 수를 채우기 위한 새 일반형은 넣지 않았다.

## 남은 GAP

없음. 09의 CEO·COO/CFO·5부서는 network 8노드/12링크로 공통 버스를 소유하고, 각 부서의 3팀은 중첩 hierarchy가 소유한다. 부서를 임의로 나누거나 지휘 관계를 바꾸지 않았다.

## 검수와 결정

모든 fixture는 실제와 같은 새 한국어 업무 내용이다. 6자 이상 원문 중복 자동검사와 정적 계약검사 결과는 0이다. 27디자인의 양모드 크기 시트, 6패널 fixture의 52칸, 22 foundation 페이지, 19개 조립·3열 비교를 최종 소스로 재렌더했다. 픽셀 크기는 조립 1280×720, 비교 3840×720이며 시트는 실제 칸 전체를 담는 가변 크기다.

- 중첩 size container가 높이 0이 되는 문제: `.panel-body`가 내부 루트에 크기를 전달하도록 foundation을 고쳤다.
- `steps--columns`의 낮은 6×4칸: 간격·패딩·부차 글자 크기를 줄여 오버플로를 제거했다.
- 반원 허브 번호를 각 멤버의 개별 카운터로 만들고 01–04 순서를 재검사했다. 2번째 노드와 제목의 교대 색도 맞췄다.
- 관측 자두색은 `--a2`다. 초안의 `--a2-7`은 파란색이므로 바꿨다. 원본 팔레트는 호스트 제공자이며 요소 CSS에는 색 리터럴이 없다.
- 원본 지표 띠의 흰 글자는 공식 팔레트에서 대비가 낮아 중간 띠 글자를 `--ink`로 정했다. 원본과 다른 부분으로 명시한다.
- 정확한 수치보다 12×6 배치가 우선하는 위치에서는 정수 그리드의 양자화 오차가 남는다. 페이지별 CSS나 절대 좌표 토큰으로 우회하지 않았다.
- 06·14의 연결된 도형과 캡션은 하나의 요소 소유다. 개별 pill/prose/card 추출 원형은 지도에 parentInstance로 관계를 명시했고 조립에서 중복 렌더하지 않는다.
- 본문 일부의 원래 낮은 회색 대비는 원본 팔레트 조립에서 유지될 수 있다. 공식 라이트·다크 요소/패널 시트의 대비 후보와 별개로 기록한다.

최종 실제 열람 PNG와 SHA는 전체 `root-visual-review.json`에 기록한다. 이 보고서는 아직 보지 않은 이미지를 보았다고 주장하지 않는다.

## 최종 대조 후 추가 복구

- `network--organization/` ← replica09: 8노드와 공통 버스.
- `hierarchy--teams/` ← replica09: 부서 1개와 3개 팀. 위 network 안에서 다섯 번 중첩 사용한다.
- `prose--compact/` ← replica12: 14px·400·진한 중성 본문, 줄간격 1.75/좁은 폭 1.7. 06의 회색 보조 문구와 분리했다.
- 02 가운데 INDEX 제목과 03 상단 브랜드 레일을 source 수치로 복구했다. 03은 표지가 아니라 일반 종이 페이지 위 chapter 장치로 분류를 바로잡았다.
- 05 제목은 중성색으로, 하단 보조 문단도 중성 회색으로 복구했다.
- 10 단계 왼쪽 면과 노치는 강조색·보조 자두색·진한 중성색 순서를 복구했다.
- 공식 팔레트의 작은 글자 대비를 유지하도록 chapter 보조문에는 --n-7을 사용했다. 원본의 아주 옅은 회색과는 차이가 있다.
- 조직도의 원본 CEO 4px/임원 8px 선 간격은 연결 소유 원칙에 따라 닫았다.
- 이전 snapshot 대조 이미지를 최종으로 인정하지 않는다. 마지막 렌더 뒤 열람한 파일/SHA만 root-visual-review.json으로 입증한다.

## 최종 낮은 본문 칸 검증

replica12의 compact 본문은 원본 크기에서14px/1.75를 유지한다. 높이150px 이하에서는12px 토큰과1.55 줄 간격으로 내려 실제 조립의134.67px 상자에서130.16px 이내로 들어오게 했다. 낮은 칸에서만 적용되는 요소 자체 container 규칙이며 페이지별 보정은 없다.
