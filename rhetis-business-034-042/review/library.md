# Business Spectrum 라이브러리 검수 기록

## 계약과 범위

`rhetis-kit-reference.zip`의 README.md를 끝까지 읽고 taxonomy 2026-10-18.1, kit-tokens.json, measure.json, type-steps.json을 기준으로 제작했다. 문서의 예시는 구조·클래스·범위 지정·fixture 형식에만 사용했다. atlas/miri의 CSS나 디자인을 복사하지 않았다.

- 컬렉션: `collection/business-spectrum/`
- 요소: 31종 전부. 요소 fixture 83개, foundation fixture 2개, 총 85개.
- 공유 토큰: 필수 토큰 전체 + placeholder 전용 `--business-spectrum-seat` 색 토큰. 모든 색은 light/dark에 별도로 정의했다.
- 기본 글꼴: Pretendard. 컬렉션 CSS에는 계약대로 `@font-face`, `url()`, 외부 자원을 넣지 않았다. 실제 검수 호스트에서 로컬 Pretendard 300/400/500/600/700/800/900을 로드했다.
- 본문 grid: 12열 × 6행. 페이지는 모두 1280×720.
- 각 요소에 `data-el="business-spectrum-…"` 범위, 계약 root/부품 클래스, 2개 이상의 한국어 실제 문장 fixture, 요소별 container 대응을 구현했다.
- card의 일반/on/quiet/line/tone 1–5, pill의 일반/on/quiet/line, list의 dot/check/num/divided, timeline의 일반/alt/col을 별도 fixture로 검토했다. cycle/hub/funnel은 3–6개, pyramid는 3–5개, hierarchy는 2–4개 분기 수를 다뤘다.

## 원본 해석

039/040/041/042/034 덱의 전체 보드를 먼저 확인하고, 다음 원본을 개별로 열어 형태·색·타이포를 확인했다.

| 원본 | 라이브러리에 반영한 언어 |
|---|---|
| 039 slide 08 | 하늘색·네이비의 수치 강조, 원형 마크, 얇은 세로 구분선 |
| 040 slide 26 | 명확한 수치와 기간, 절제된 연결선, 넉넉한 그래프 여백 |
| 041 slide 13 | 네이비 KPI 계층, 밝은 패널, 선명한 목표 수치 |
| 042 slide 06 | 사각 업무 패널, 좁은 상단 강조선, 명확한 계층과 연결 |
| 034 slide 07 | 소프트 퍼플 보조 톤, 둥근 강조부, 넓은 비교 영역 |

기본은 흰 배경, 남색 제목, 얇은 청회색 선, 밝은 하늘색 패널이다. 퍼플은 보조 톤으로 제한했다. 표지의 대각 리본은 원본의 파란 모서리 도형을 평면 CSS로 재해석했다. 사진·기기 화면·복잡한 3D 형상·고유 로고는 연회색 단색의 번호 seat로 처리했다.

원본의 장식용 3D 형상을 새 라이브러리의 기본 재료로 쓰지 않았다. funnel/architecture/table 등에는 사각 패널을, 단계 및 강조에는 캡슐을 사용해 이미지에 없는 요소도 같은 언어로 설계했다. `gauge`는 계약이 정한 가로 progress bar이며, KPI의 원형 비율은 `chart-donut`에 배정했다.

## 시각 검토와 수정

31종의 개별 full PNG를 열어 확인했다. 최소 칸의 카드, 캡슐, 가격표, steps, timeline, line/bar 차트, cycle/hub, matrix/venn 등 복잡도가 높은 요소와 dark 상태도 개별 PNG로 추가 확인했다. 연락처 시트만으로 검수를 끝내지 않았다.

1차와 2차를 비교하며 다음을 수정했다.

- 가로 막대의 수치가 한 자리씩 줄바꿈되던 문제를 `white-space:nowrap`으로 수정했다.
- 가격표 안의 nested list가 size containment 때문에 높이 0으로 계산되어 가격과 겹치던 문제를 flex allocation으로 수정했다.
- 작은 세로 steps/timeline에서 마지막 항목이 넘치던 문제를 높이 단계별 글자·간격·패딩 조정으로 수정했다.
- 3집합 venn의 두 번째 이름이 중앙 캡슐에 가리던 문제를 삼각 배치와 집합별 이름 위치로 수정했다. 이름은 숨기지 않았다.
- matrix의 세로축 글자가 뒤집혀 보이던 문제를 가로 조판 후 회전하는 방식으로 수정했다.
- decision 노드의 clip-path가 방향 화살표까지 자르던 문제를 둥근 판정 패널로 바꿔 수정했다.
- 공식 preview 도구의 전역 `small` 색이 수치 단위를 회색으로 바꾸던 문제를 요소 범위의 `color:inherit`로 차단했다.
- `pill.on`의 흰 체크가 옅은 원 위에서 저대비였던 문제를 accent/accent-ink 쌍으로 수정했다.
- 긴 highlight가 두 줄이 될 때 표면 높이가 줄 높이를 따라가지 못하던 문제를 inline-size containment로 수정했다.
- 공식 preview의 외부 `.frame` 클래스가 이미지 frame 요소의 크기에 간섭하던 문제를 요소 범위의 auto width/height로 차단했다.
- cycle/hub 연결선은 현재 칸의 가로·세로 비율을 CSS `hypot`/`atan2`로 계산하고 패널 뒤로 배치하여 실제 중심과 노드를 연결했다.
- line chart는 CSS anchor 좌표로 점 사이의 실제 선을 그린다. 상승과 하락 구간을 각각 개별 PNG에서 확인했다.

## 자동 검사와 재현

공식 도구로 두 시트를 생성했다.

```sh
python tools/preview.py collection/business-spectrum contract/type-steps.json --out light.html
python tools/preview.py collection/business-spectrum contract/type-steps.json --dark --out dark.html
```

작업 당시 공식 HTML은 `collection/business-spectrum/preview-light.html`, `preview-dark.html`에 생성했다. root 통합 시 `build/library/`로 분리할 수 있다. 실제 브라우저 검수는 localhost HTTP 서버와 Chromium을 사용했다. `file://` 로드는 사용하지 않았다.

검수 스크립트 원본:

- `tools/render-library.py`: 85 fixture × full/min × light/dark = 340 PNG, 글자 영역·겹침·폰트 검사.
- `tools/audit-library.py`: 최종 대비·크기·폰트·겹침·chip 중심 감사, 마지막 수정 요소 재촬영, 양 모드 fixture PDF와 소스 SHA-256 생성.

최초 전체 렌더의 14개 보고 항목은 실제 최소 칸 overflow 10건과 첫 cover의 폰트 대기 타이밍 4건이었다. 모두 수정했고 2차 340 상태 렌더에서 해당 검사는 0건이었다. 대비 추가 감사에서는 막대/점 바깥에 놓인 라벨에 부모 도형 배경을 적용하던 오탐과 `color(srgb …)` 파싱을 수정했다. 마지막 수정 내용은 재촬영 PNG와 최종 소스 해시로 확인한다.

`review/library-automatic-final.json`은 개별 PNG SHA-256, 페이지·root 크기, 대비 수치, 글꼴 준비 상태, 글자 겹침·영역 초과 및 chip 중심 편차를 기록한다. `review/library-source-hashes.json`은 최종 CSS/JSON/fixture 소스의 SHA-256이다. Rhetis 저장소의 실제 intake 도구는 참고팩에 없으므로 이 기록은 참고팩 계약과 브라우저 검수 결과이며 intake 실행을 뜻하지 않는다.

## 해석이 갈린 부분과 판단

여러 덱의 하늘색·네이비·파랑·퍼플은 동일한 브랜드의 완전히 같은 색 체계가 아니다. 새 컬렉션은 네이비/블루를 주축으로 통합하고 퍼플은 보조 색으로 선택했다. 사진과 3D 형상이 차지하는 시각적 무게는 회색 seat의 크기와 위치로 유지한다. 원본의 작은 설명 문구를 모든 fixture에 억지로 옮기는 대신, 요소의 역할에 맞는 한국어 비즈니스 문장을 작성했다. 이 문장은 원본에서 판독한 텍스트로 주장하지 않는다.

## 최종 수치

- 전체 상태: 340개(85 fixture × 2크기 × 2모드).
- PNG: 340개, 모두 1280×720.
- 글자 root 영역 초과, 글자 간 겹침, 글꼴 로딩 실패, 대비 미달, chip 중심 편차 초과: 0건.
- 검사된 텍스트의 최소 대비: 5.02:1. 일반 텍스트 4.5:1, 큰 텍스트 3:1 기준을 충족했다.
- pill/tag의 기하학적 중심 편차 최대: 0px. 글리프의 시각 중심과 두 줄 highlight의 배경 높이는 개별 PNG로 확인했다.
- 폰트 준비: 340개 상태 모두 true.
- fixture PDF: light/dark 각각 85쪽, 페이지 크기 960×540pt(1280×720 CSS px).
- 최종 CSS/JSON/fixture 해시 목록: 151개 항목. 340개 PNG는 개별 결과 SHA-256을 기록했다.
- 마지막 hub/cycle stacking 수정은 두 요소의 3–6개 멤버 수, full/min 및 light/dark PNG 전부를 다시 렌더해 최종 감사 기록에 병합했다.
