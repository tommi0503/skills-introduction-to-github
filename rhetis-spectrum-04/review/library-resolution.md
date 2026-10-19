# 라이브러리 시각 검수 후 수정 결과

`library-visual-a.md`, `library-visual-b.md`는 1차 검수 당시의 발견 기록입니다. 아래 수정 후 라이트·다크 시트, 개별 PNG와 PDF를 다시 생성했습니다.

| 발견 | 최종 조치 |
|---|---|
| image-frame 초과 | 제공 preview 도구의 전역 `.frame`을 `article > .frame`으로 한정. 실제 요소 frame은 자신의 grid 칸을 채움 |
| legend의 막대 소실 | foundation stack의 자식 높이 배분과 legend의 고유 높이를 분리 |
| hub의 대각 연결 누락 | 중심을 통과하는 대각선 추가, 6개 노드 연결 |
| hierarchy 연결 단절 | root 행에 가로 연결선을 공유시키고 branch의 세로선과 연결 |
| funnel 작은 단계 폭 동일 | `30% + --v × 0.7%` 정규화로 마지막 세 단계도 서로 다른 폭을 유지 |
| cycle 순서 불명확 | 3–6개 멤버 수별 원주 배치, 원형 트랙과 순환 표시 |
| pill이 세로로 늘어남 | 내용 높이에 맞는 한 줄 capsule로 고정하고 다중 fixture는 세로 stack에 배치 |
| matrix 축 문구 겹침 | 각 Y축 라벨에 개별 세로 쓰기, 상하 분리 |
| venn 중앙 겹침 | 삼각형으로 배치한 진짜 3중 교집합, 이름의 z-index와 위치 분리 |
| timeline 단절 | 공통 수평 트랙에 점을 고정하고 상하 텍스트만 교대 |

최종 검사는 89개 fixture를 두 모드에서 전체 칸과 선언된 최소 칸으로 확인한 370개 상태이며 텍스트·칸 초과 경고0건입니다. 큰 정보량을 가진 fixture의 최소 칸은 실제로 읽히는 크기로 명시했습니다.

슬라이드 재조립의 내부 정렬·SVG 고유 비율 문제도 수정했습니다. 최종 82쌍은 `reassembly-pixel-comparison.json`에서 전부 픽셀이 일치합니다. 모든 최종 PNG·PDF는 마지막 DOM/CSS와 같은 버전입니다.
