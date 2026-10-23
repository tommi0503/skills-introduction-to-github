# vectorbox 검수 보고서

생성 시각: 2026-10-23T17:52:57.390065+00:00  
최종 컬렉션 SHA-256: `b84fc549970fefd09bce674f919f0dbf3dc0bf09c00fe6b1417dc0b8f5a1f6cb`

정적 계약, 실제 글꼴 로딩·코드 등폭 측정, 대비, 실제 overflow clipping, 선택한 의미·그래픽 검사에서 확인한 통과와 원본 시각 동일성은 별개다. 이 결과는 원본과 100% 동일하다는 판정이 아니다. 요소·크기·모드·예외의 구체적인 검사 범위는 각 JSON과 아래 스냅샷 상태를 따른다.

사진·복잡한 일러스트·래스터 아이콘·기기 화면 등은 요청대로 연한 회색 placeholder로 대체했다. 단순 도형·표·차트는 구현했고 가능한 선화 아이콘은 Lucide로 대체했다. 이 허용 대체와 별개로, 원본 글꼴을 식별할 수 없어 선택한 실제 로드 글꼴의 획·폭·행간, 일부 줄바꿈·미세 좌표·테두리 차이가 남는다. 페이지별 차이는 [개별 대조 메모](primary-review.md)에서 확인할 수 있다.

`현재 소스와 해시 일치`는 해당 보고서의 검사 입력과 현재 입력이 같다는 뜻이다. `과거 스냅샷`은 수정 전 보고서이며 현재 통과로 바꿔 표시하지 않았다. 소스 전용 최종 변경은 해당 구성의 별도 후속 보고서로 검증했다. 개별 해시가 없는 font/CSS 지원 등의 원시 실행 증거도 최신 소스 전체의 포괄 통과로 확대하지 않는다. gradient·polygon·sibling 배경·의도된 crop/접근성 숨김 등의 자동 후보는 원시 값을 유지하고 실화면 판단을 별도 기록했다.

[소스와 보고서 해시·스코프](source-manifest.json), [누적 감사 경과](integration-audit-history.md), [주 검수 원본 메모](primary-review.json)를 함께 보존했다. 누적 경과에는 수정 전 결과가 포함되므로 최종 상태는 해시와 후속 범위를 확인해야 한다. 정적 경고는 데이터 기하 등 검토용 후보이며 오류와 구별한다.

| 보고서 | 스냅샷 상태 | 실제 기록 요약 |
|---|---|---|
| [vectorbox-alignment-audit.json](reports/vectorbox-alignment-audit.json) | 현재 소스와 해시 일치 | 오류0, 경고0, 불완전0 |
| [vectorbox-audit.json](reports/vectorbox-audit.json) | 개별 해시 미기재·원시 실행 증거 | 오류0, 경고2, 불완전0 |
| [vectorbox-browser-css-audit.json](reports/vectorbox-browser-css-audit.json) | 개별 해시 미기재·원시 실행 증거 | 원시 결과·검사 범위 참조 |
| [vectorbox-clipping-audit.json](reports/vectorbox-clipping-audit.json) | 현재 소스와 해시 일치 | 실제 text clip 0 (검사 당시 범위) |
| [vectorbox-clipping-dark-audit.json](reports/vectorbox-clipping-dark-audit.json) | 현재 소스와 해시 일치 | 실제 text clip 0 (검사 당시 범위) |
| [vectorbox-code-font-audit.json](reports/vectorbox-code-font-audit.json) | 개별 해시 미기재·원시 실행 증거 | 실로드·등폭 통과 |
| [vectorbox-contrast-audit.json](reports/vectorbox-contrast-audit.json) | 현재 소스와 해시 일치 | 대비 후보 light 0 / dark 0 |
| [vectorbox-contrast-min-audit.json](reports/vectorbox-contrast-min-audit.json) | 현재 소스와 해시 일치 | 대비 후보 light 0 / dark 0 |
| [vectorbox-contrast-summary.md](history/vectorbox-contrast-summary.md) | 과거 스냅샷 | 과거 진단 요약; 최종 통과 판정에 단독 사용하지 않음 |
| [vectorbox-functional-audit.json](reports/vectorbox-functional-audit.json) | 현재 소스와 해시 일치 | 기능 원시 후보 stack=0, donut=0, balance=0, bullet=0, seats=0, graphics=0, polygonText=0 |
| [vectorbox-functional-dark-audit.json](reports/vectorbox-functional-dark-audit.json) | 현재 소스와 해시 일치 | 기능 원시 후보 stack=0, donut=0, balance=0, bullet=0, seats=0, graphics=0, polygonText=0 |
| [vectorbox-functional-foundation.json](history/vectorbox-functional-foundation.json) | 과거 스냅샷 | 기능 원시 후보 stack=0, donut=0, balance=0, bullet=0, seats=0, graphics=0, polygonText=0 |
| [vectorbox-math-whitespace.json](reports/vectorbox-math-whitespace.json) | 개별 해시 미기재·원시 실행 증거 | 원시 결과·검사 범위 참조 |
| [vectorbox-overflow-summary.md](history/vectorbox-overflow-summary.md) | 과거 스냅샷 | 과거 진단 요약; 최종 통과 판정에 단독 사용하지 않음 |
| [vectorbox-pill-cover-audit.json](reports/vectorbox-pill-cover-audit.json) | 개별 해시 미기재·원시 실행 증거 | 원시 결과·검사 범위 참조 |
| [vectorbox-source-font-audit.json](reports/vectorbox-source-font-audit.json) | 개별 해시 미기재·원시 실행 증거 | 오류0, 경고0, 불완전0 |

<!-- RAW CANDIDATE SCOPE -->

전체 원시 자동 후보가0이라는 뜻은 아니다. root 렌더 보고의 `overflowCandidates`는 폰트 line box·잉크 범위나 외부 연결선 pseudo의 scroll 치수도 수집한다. 제목 h1의 폰트 line box와 scroll 치수 차이가 원시 후보에 포함된다. 원시 후보는 보존했고 실제 overflow clip 검사 및112장 개별 주 검수와 구별했다. 주 검수자는 최종 페이지 PNG에서 실제 영역 잘림을 보지 못했다고 기록했으며, 원본과의 차이는 페이지별 메모에 남겼다.

<!-- END RAW CANDIDATE SCOPE -->
