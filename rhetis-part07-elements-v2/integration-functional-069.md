# 통합 기능 검수 — 069 담당

읽기 전용으로 5개 컬렉션 ×13개 leaf, 각1 fixture의12×6 및 해당 최소칸 총129개 native cell을 실제로 확인했다. 원래 셀을 리사이즈하지 않고 최대·최소를 나란히 붙인 검수용 PNG를 이용했다. 아이콘은 공식 점선 slot이며 데이터 도형·선·화살표를 검사했다. 범위는 라이트 모드이며 양 모드·모든 fixture를 모두 검수했다고 주장하지 않는다. 알려진073 hub·pricing baseline·metric surface는 중복 실패로 집계하지 않는다.

원본 검사 시점 65개 leaf 모두 저장 fingerprint가 실제 의존 소스 fingerprint와 일치했다. 구체 셀 경로·fixture·크기·fingerprint는 `tools/integration-functional-069/manifest.json`, 검수용 묶음은 같은 폴더의 collection-N.png다. 소스/CSS/map/sheet 파일은 이 읽기 전용 검사에서 변경하지 않았다. 이후 주 에이전트가 별도로069 hub/hierarchy/swimlane 수정을 승인했다.

## 실제 기능 실패 후보

### crossrail / slope — 값/시점 분리

- fixture: `crossrail-project/crossrail/elements/slope/fixtures/base-b.html`
- 크기: 12×6, 6×4
- fingerprint: `0f95decebda6bc22f7da96e970aae443c75a54e549e802a492aaf92ea4c864d4`
- 근거: 2055/2056 머리글은 좌우에 있지만 a/b 숫자 둘은 왼쪽 표 열에 몰리고 실제 선은 더 오른쪽에서 시작한다. 38→46 등 수치는 상승·하강과 맞지만 각 시점 숫자와 선 끝의 결합이 없다.
- native: `crossrail-project/sheet-cells/slope--base-b--light--12x6.png`, `crossrail-project/sheet-cells/slope--base-b--light--6x4.png`

### meridian-deck / hierarchy — 부모/자식 연결 단절

- fixture: `meridian-deck-project/meridian-deck/elements/hierarchy/fixtures/replica-28.html`
- 크기: 12×6, 3×3
- fingerprint: `656b1bf4c7b668811554ad578064f7f6fc4f10cd6b13095bb759df41c1946a4d`
- 근거: root 아래 세로줄 끝과 가로 bus 사이 약12px, 자식 세로줄 끝과 A/B/C 상자 사이 약58px 공백이 최대칸에 보인다. 최소에서도 줄이 상자 전에서 끝난다. 가로줄 왼쪽은 첫 자식 중심보다 더 왼쪽 캔버스 끝까지 이어진다.
- native: `meridian-deck-project/sheet-cells/hierarchy--replica-28--light--12x6.png`, `meridian-deck-project/sheet-cells/hierarchy--replica-28--light--3x3.png`

### onboard-docket / hub — 최소칸 방사 관계 소실

- fixture: `onboard-docket-project/onboard-docket/elements/hub/fixtures/six-members.html`
- 크기: 12×6, 6×6
- fingerprint: `86b6badcddc5964a168a7c8b329223c70a1008d2cc3b9868dafd6f26788a6858`
- 근거: 최대칸은 중심과 여섯 방사형 멤버지만 최소6×6에서는 core 아래 한 세로 트랙에 멤버가 순차 배치된다. core→각 spoke를 잇는 관계 대신 순서 목록으로 읽힌다.
- native: `onboard-docket-project/sheet-cells/hub--six-members--light--12x6.png`, `onboard-docket-project/sheet-cells/hub--six-members--light--6x6.png`

### onboard-docket / cycle — 최소칸 순환 복귀선 없음

- fixture: `onboard-docket-project/onboard-docket/elements/cycle/fixtures/six-members.html`
- 크기: 12×6, 6×6
- fingerprint: `7a282bc87440cc2d696588fc8a456ac8d66794633b84531408c7408c8666ed4e`
- 근거: 최대칸은 닫힌 순환이지만 최소6×6은 위→아래 화살표뿐인 목록이며 마지막 개선 공유→첫 접수 분류 복귀 연결이 없다.
- native: `onboard-docket-project/sheet-cells/cycle--six-members--light--12x6.png`, `onboard-docket-project/sheet-cells/cycle--six-members--light--6x6.png`

### seedmark / cycle — 화살표 방향 불일치

- fixture: `seedmark-project/seedmark/elements/cycle/fixtures/cycle-4.html`
- 크기: 12×6, 6×4
- fingerprint: `d774b6476ce67792201780238e8313fad343746d73067fd3bf9b1b5dd81dd971`
- 근거: 오른쪽 생산 옆 화살표가 왼쪽, 왼쪽 개선 옆은 오른쪽, 아래 판매 옆은 위를 향한다. 원주를 따라 다음 멤버로 이어지는 방향이 아니다.
- native: `seedmark-project/sheet-cells/cycle--cycle-4--light--12x6.png`, `seedmark-project/sheet-cells/cycle--cycle-4--light--6x4.png`

### seedmark / hierarchy — bus/노드 연결 위치 불일치

- fixture: `seedmark-project/seedmark/elements/hierarchy/fixtures/org-3.html`
- 크기: 12×6, 6×4
- fingerprint: `eaa35094aca9a74550a02819ac9eb764fbc5874f6158ded1dd11e80feec49938`
- 근거: 부모 가로선의 수직줄이 branch 왼쪽 경계에 위치해 node 중심이나 면과 접속하지 않는다. 최대 x약0/375/749 대 실제 중심187/562/937. node→leaf 연결선도 보이지 않는다.
- native: `seedmark-project/sheet-cells/hierarchy--org-3--light--12x6.png`, `seedmark-project/sheet-cells/hierarchy--org-3--light--6x4.png`

### crossrail / radar — spoke 없음

- fixture: `crossrail-project/crossrail/elements/radar/fixtures/base-b.html`
- 크기: 12×6, 8×4
- fingerprint: `c5d2dd19223be3baf045408dd1d7435475026feb22e6c6658d35c0bca18c6ce0`
- 근거: 8개 축 이름과 링·polygon은 있지만 중심에서 각 축 방향으로 방사하는 spoke 선이 최대/최소 모두 없다.
- native: `crossrail-project/sheet-cells/radar--base-b--light--12x6.png`, `crossrail-project/sheet-cells/radar--base-b--light--8x4.png`

### seedmark / radar — spoke/계열 구별 없음

- fixture: `seedmark-project/seedmark/elements/radar/fixtures/radar-5.html`
- 크기: 12×6, 6×4
- fingerprint: `65404b7da4526494a24b929c0015791ea664ec19014629d7a10ea0ab248dd05c`
- 근거: 5개 축 이름과 링·polygon은 있지만 spoke 선이 없다. 두 untoned series 면이 같은 옅은 주황이며 범례도 계열색을 표시하지 않아 어느 polygon이 어느 계열인지 추적할 수 없다.
- native: `seedmark-project/sheet-cells/radar--radar-5--light--12x6.png`, `seedmark-project/sheet-cells/radar--radar-5--light--6x4.png`

### vectorbox / hub — 외곽 track은 hub spokes 아님

- fixture: `vectorbox-project/vectorbox/elements/hub/fixtures/base-long.html`
- 크기: 12×6, 9×6
- fingerprint: `af86455ba2492723acea7622ce122e1cdb57e3dfd070c2462dda8730e1bfcd76`
- 근거: 중앙 core가 외곽 네 점과 연결되지 않는 사각 track을 대표형으로 잘못 분류했다. 주 에이전트 승인으로 source06을 GAP 재분류하고 inferred radial로 교정 중이다.
- native: `vectorbox-project/sheet-cells/hub--base-long--light--12x6.png`, `vectorbox-project/sheet-cells/hub--base-long--light--9x6.png`

### vectorbox / hierarchy — branch 사이 bus 끊김

- fixture: `vectorbox-project/vectorbox/elements/hierarchy/fixtures/base-long.html`
- 크기: 12×6, 6×3
- fingerprint: `2b476bbc0f5bbbb7ad0f6148589dc0f67b0f0bc58524aa484646b9f46c0786b0`
- 근거: 각 branch의 border-top 선이 요소 사이 gap에서 끊겨 중앙 root에서 왼쪽·오른쪽 branch로 연속 연결되지 않는다. 승인된 교정 진행 중이다.
- native: `vectorbox-project/sheet-cells/hierarchy--base-long--light--12x6.png`, `vectorbox-project/sheet-cells/hierarchy--base-long--light--6x3.png`

### vectorbox / swimlane — 최소 노드 면 밖 글자

- fixture: `vectorbox-project/vectorbox/elements/swimlane/fixtures/base-long.html`
- 크기: 12×6, 6×3
- fingerprint: `6fc8748ceb72cb8e15973c55c85456011ed552234f16090355835207ec73bf7a`
- 근거: 최소6×3의 시작 원·ask·아래 노드에서 제목3줄이 면 높이보다 길어 연결선/옆 lane 영역에 걸린다. wholeComponent 자동0이 놓친 실제 내부면 잘림 사례다. 승인된 교정 진행 중이다.
- native: `vectorbox-project/sheet-cells/swimlane--base-long--light--12x6.png`, `vectorbox-project/sheet-cells/swimlane--base-long--light--6x3.png`

## 범위와 유보

나머지 선택 셀에서는 데이터에 반하는 막대 높이·누적 기준선·waterfall running total·닫힌 집합의 포함/겹침 오류를 발견하지 못했다. 이는 모든 가능한 데이터의 정확성을 증명하지 않는다. 예를 들어 sparkline 표본은 일부 컬렉션에서 bars 또는 전부0인 fixture이므로 다른 곡선의 정확성은 별도 fixture 검수가 필요하다. 면 내부 글자는 DOM 바깥 검사가 통과해도 넘칠 수 있어 실제 PNG를 우선했다. 스타일 변경 중이던 컬렉션의 결과는 최종 fingerprint와 다시 대조해 과거 결과로 분류해야 한다.

## 069 승인 교정 완료

vectorbox hub는 원본 사각 트랙을 map/GAPS에서 unexpressible로 재분류하고 inferred radial의 실제 중심→각 mark 연결로 교정했다. source06을 잘못된 radial로 조립하지 않도록 본문을 비웠다. hierarchy는 root 소유의 한 연속 bus로 branch gap을 이어 실제 node 상단에 내렸다. swimlane .name은 작은 노드 자체의 bounded font를 상속하여 최소칸 면 밖 넘침을 없앴다. 각각 양 모드·모든 허용 크기를 재렌더하고 직접 확인했다(hub16, hierarchy24, swimlane24 cell). 세 요소의 자동 후보는 양 모드 모두0이다. 최종 증거는 vectorbox-project/sheets/의 최신checks와PNG이며, 본 보고서 manifest의069 세 이전FP는 발견 시점의 과거 결과다.

069 hub는 추가 상한6멤버 fixture의 최대/최소도 양 모드에서 확인했다. 가운데 두 mark와 core 사이에 실제 방사선 간격이 남고 긴 core 이름도 면 안에 들어간다.
