# Vectorbox · ROUND5 결과

1. **추가한 독립 디자인**: `card--selection`←03, `card--burst`·`card--caption`←04, `card--ring`←05, `card--icon`←10·11, `card--budget`←10, `card--profile`←12, `legend--vertical`←10, `chart-bar--grouped`←04, `chart-donut--pie`←10, `network--perimeter`←06. 기본 `card`는08의 선택 프레임 카드이며, 실제 원형을 가진 총18개 디자인만 남겼다.
2. **패널 사용**:04의 `.panel.plot-legend`는 범례와 묶음 차트, `.panel.badges`는 두 쌍의 burst 수치와 선택 프레임 캡션을 배치한다. 모든 연결은 요소 자신의 소유이며 panel은 배치와 틀만 맡는다.02·11의 잘린 선택 프레임은 foundation `.vector`가 그린다.
3. **차트 확장**:04는 `.bars.grouped`의 범주4개×계열2개, `--max`로 계산한 y눈금과 공통 기준선을 사용한다.10은 `.donut.pie > .slice`6개와 중심 아이콘을 가진다. `--vectorbox-slice-start`는 앞 조각의 `--v` 누적합이며 fixture와 조립본 모두 합계100을 검사했다.06은 방사 hub가 아닌 독립 core와 외곽 node4개, 사각 연결 track을 소유하는 `network--perimeter`로 복구했다.
4. **삭제한 일반 요소**: 원형 없는49개 폴더를 삭제했다. 정확한 목록은 `round5-deleted-leaves.json`에 있다. 유지한18개 디자인 사이의 별도 요소 의존성은 없다. 모범 상태의 reserved ID를 임의 재사용하지 않고 새 이름의 한국어 업무 fixture36개를 사용한다.
5. **잔여 GAP**:0건. 기존02·11 배경,04 묶음 차트,06 사각 외곽 관계도,10 다중 조각 링을 모두 복구했다. 12×6 배치의 양자화 차이와 Lucide 실루엣 차이는 GAP으로 부풀리지 않았다.10의 실제 면적25/30/15/10/10/10과 범례6×25%의 원본 불일치는 둘 다 보존했다.
6. **마지막 수정 후 직접 확인한 결과**:18개 디자인의 라이트·다크 시트36장 전체, 원형 crop|12×6|min 비교18장, 조립본02–13의 원본|불변 replica|조립 비교12장, foundation5예시×2모드10장을 열어 확인했다. 총440개 허용 크기 칸의 영역초과·잘림·겹침·대비·폰트 자동후보0, 정적·계약 검사0이다. 직접 확인한 파일의 SHA와 현재 source fingerprint는 `round5-review.json`에 기록했다.

현재 source fingerprint: `dc9b0d5ee909b2763e11e2c037cfe62f1b32bdeb2f771ada868da7cbca09cb87`.
