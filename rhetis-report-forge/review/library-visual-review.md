# 라이브러리 최종 개별 시각 검수

2026-10-19. `renders/library-light/001.png`–`089.png`와 `renders/library-dark/001.png`–`089.png`, 합계 178개의 개별 1280×720 PNG를 하나씩 열어 확인했다. 이후 Pretendard 내장 폰트 수정으로 전체 PNG가 갱신되어, 최종 178개도 모두 다시 개별 열람하고 글자 잘림·겹침의 유무를 재확인했다. 한 화면에 여러 이미지를 도구로 요청하되 각각 원래 PNG로 열람했으며, 연락처 시트로 검수를 대체하지 않았다. 라이브러리 source는 이 검수에서 변경하지 않았다.

## 결과와 수정 확인

- 전체 31개 요소와 foundation에서 잘린 글자·칩 글자의 중심 이탈·페이지 외부 넘침을 새로 발견하지 않았다. 제목·본문·수치의 역할, 카드의 강조선, indigo accent 및 선 굵기가 같은 디자인 계열로 읽힌다.
- 다크 모드는 어두운 navy page/surface와 밝은 lavender accent를 사용한다. 강조 카드·tag·core는 밝은 면 위의 어두운 글자로 전환되고, 일반 본문은 밝은 글자로 남아 역할을 구별한다. 선/축/placeholder도 배경과 구분된다.
- 도넛 022–024는 수정 뒤 양 모드에서 다시 개별 확인했다. 도형이 타원으로 찌그러지지 않는 정원이며, 숫자가 이름보다 크게 읽힌다. 3·4개 묶음에서 각 값과 도형을 식별할 수 있다.
- line 025–026은 양 모드에서 모든 점 사이의 연결선을 확인했다. 12점 fixture의 하강·상승·44→44 수평 구간도 끊기지 않는다.
- cycle 027–030과 hub 043–046은 멤버가 서로 겹치지 않고 core·연결선·방향 화살표가 보인다. hierarchy 040–042도 root/branch 관계를 읽을 수 있다.
- funnel 035–037의 최초 검사에서는 45% 최소 폭 때문에 작은 --v 값들이 동일한 너비로 보이는 의미상 문제를 발견해 즉시 전달했다. 최종 수정 PNG를 양 모드에서 재열람했고, 단계 폭이 --v에 따라 실제로 달라지며 이름과 숫자는 도형 좌우의 고정 caption 레일로 분리된 것을 확인했다. 해당 문제는 해결됐다.
- steps 075–077의 본문과 table 078–080의 행/열 헤더·강조 열은 밝은/어두운 면의 역할이 구별되며 글자가 읽힌다. pricing 추천 tag, architecture chip, inline tag 081–082의 중앙 정렬도 육안으로 확인했다.

최종 자동 검사 증거는 Pretendard 내장 뒤 다시 생성한 `library-audit.json`의 260개 full/min case(font true 260/260, overflow 0, contrast 0)다. `library-audit-targeted.json`의 24개 donut/funnel case는 폰트 수정 전의 과거 검사 기록이며 최종 판정 근거와 구분한다. PNG 수/크기는 별도 확인해 양 모드 각각 89개, 전체 1280×720임을 확인했다. 이 독립 시각 검수는 full PNG 전체이며 모든 min PNG를 개별 열람했다고 주장하지 않는다.

### 폰트 수정과 최종 재검수

과거 1차 라이브러리 감사에서는 260개 case의 `font`가 false였다. 이 문제를 발견해 전달했고, 주 에이전트가 미리보기 HTML에 Pretendard data URL을 내장하고 캡처에서도 같은 폰트 데이터를 사용하도록 수정했다. 라이브러리 source CSS의 외부 리소스 금지 계약은 유지했다.

최종 `library-audit.json`을 직접 읽어 총 260개 case 모두 `font:true`, overflow 0, contrast 0임을 확인했다. 갱신된 라이트89장과 다크89장 전부를 다시 각각 열어 폰트 변경 뒤의 글자 잘림·겹침을 확인했고 새 문제는 발견하지 않았다. 제목 폭과 일부 한글 줄바꿈이 바뀌었으나 수치·칩·표·차트 레이블이 영역 안에 남고 line/funnel/donut 도형도 유지된다. 아래 개별 확인 표는 이 최종 폰트 적용 PNG까지 포함한 결과다.

### 납품을 막지 않는 표현상 관찰

- pill 066–067은 12×6 전체 슬롯에서 높이가 크게 늘어나 긴 세로 캡슐로 보인다. 문구는 한 줄이고 가운데 정렬이지만, 실제 조립에서는 낮고 넓은 슬롯을 권장한다.
- card 010–016, metric 060–062처럼 짧은 콘텐츠를 전체 슬롯에 배치한 fixture는 여백이 크다. 이는 fixture의 full-slot 대응 결과이며 잘림과 구분한다.
- quote 073–074, timeline 083–085 등 일부 긴 한국어 어절은 줄 중간에서 나뉜다. 내용 손실은 없지만 편집 단계에서 자연스러운 어절 경계를 고를 수 있다.
- people 063–064는 설명 길이가 다를 때 사진/이름 baseline이 약간 달라진다. 읽기나 영역 안전성 문제는 없으며 더 엄격한 baseline 정렬은 선택적 개선이다.
- image-frame 두 fixture는 서로 다른 번호의 seat를 검증한다. 다른 종횡비의 실제 사진은 이 fixture에 포함되지 않는다.

## 개별 PNG 확인 목록

아래 번호는 양 모드 PNG 파일명에 대응한다. “확인”은 해당 PNG를 실제로 열어 이 문서의 기준으로 검토했다는 뜻이며 원본 이미지와 픽셀 동일성을 뜻하지 않는다.

| 번호 | fixture | light | dark |
|---|---|---|---|
| 001 | foundation / cover min 12x6 | 확인 | 확인 |
| 002 | foundation / seat min 12x6 | 확인 | 확인 |
| 003 | agenda / agenda-4 min 12x6 | 확인 | 확인 |
| 004 | agenda / agenda-5 min 12x6 | 확인 | 확인 |
| 005 | architecture / arch-2 min 12x6 | 확인 | 확인 |
| 006 | architecture / arch-4 min 12x6 | 확인 | 확인 |
| 007 | architecture / arch-5 min 12x6 | 확인 | 확인 |
| 008 | callout / callout-plain min 6x3 | 확인 | 확인 |
| 009 | callout / callout min 6x3 | 확인 | 확인 |
| 010 | card / card-2-quiet min 6x3 | 확인 | 확인 |
| 011 | card / card-3-icon3d min 6x3 | 확인 | 확인 |
| 012 | card / card-3-line min 6x3 | 확인 | 확인 |
| 013 | card / card-3-on min 6x3 | 확인 | 확인 |
| 014 | card / card-4 min 6x3 | 확인 | 확인 |
| 015 | card / card-5-tone min 6x3 | 확인 | 확인 |
| 016 | card / card min 6x3 | 확인 | 확인 |
| 017 | chart-bar / bars-12 min 12x6 | 확인 | 확인 |
| 018 | chart-bar / bars-3 min 12x6 | 확인 | 확인 |
| 019 | chart-bar / bars-6 min 12x6 | 확인 | 확인 |
| 020 | chart-bar / bars-h-5 min 12x6 | 확인 | 확인 |
| 021 | chart-bar / bars-h-8 min 12x6 | 확인 | 확인 |
| 022 | chart-donut / donut min 6x3 | 확인 | 확인 |
| 023 | chart-donut / donuts-3 min 6x3 | 확인 | 확인 |
| 024 | chart-donut / donuts-4 min 6x3 | 확인 | 확인 |
| 025 | chart-line / lines-12 min 12x6 | 확인 | 확인 |
| 026 | chart-line / lines-6 min 12x6 | 확인 | 확인 |
| 027 | cycle / cycle-3 min 12x6 | 확인 | 확인 |
| 028 | cycle / cycle-4 min 12x6 | 확인 | 확인 |
| 029 | cycle / cycle-5 min 12x6 | 확인 | 확인 |
| 030 | cycle / cycle-6 min 12x6 | 확인 | 확인 |
| 031 | delta / delta min 6x3 | 확인 | 확인 |
| 032 | delta / extended min 6x3 | 확인 | 확인 |
| 033 | flowchart / extended min 12x6 | 확인 | 확인 |
| 034 | flowchart / flowchart min 12x6 | 확인 | 확인 |
| 035 | funnel / funnel-3 min 6x3 | 확인 | 확인 |
| 036 | funnel / funnel-5 min 8x4 | 확인 | 확인 |
| 037 | funnel / funnel-6 min 8x4 | 확인 | 확인 |
| 038 | gauge / meter-4 min 6x3 | 확인 | 확인 |
| 039 | gauge / meter min 6x3 | 확인 | 확인 |
| 040 | hierarchy / org-2 min 12x6 | 확인 | 확인 |
| 041 | hierarchy / org-3 min 12x6 | 확인 | 확인 |
| 042 | hierarchy / org-4 min 12x6 | 확인 | 확인 |
| 043 | hub / hub-3 min 12x6 | 확인 | 확인 |
| 044 | hub / hub-4 min 12x6 | 확인 | 확인 |
| 045 | hub / hub-5 min 12x6 | 확인 | 확인 |
| 046 | hub / hub-6 min 12x6 | 확인 | 확인 |
| 047 | image-frame / extended min 6x3 | 확인 | 확인 |
| 048 | image-frame / frame min 6x3 | 확인 | 확인 |
| 049 | legend / extended min 6x3 | 확인 | 확인 |
| 050 | legend / legend-bars min 6x3 | 확인 | 확인 |
| 051 | list / list-3 min 6x3 | 확인 | 확인 |
| 052 | list / list-check min 6x3 | 확인 | 확인 |
| 053 | list / list-divided min 6x4 | 확인 | 확인 |
| 054 | list / list-num min 6x4 | 확인 | 확인 |
| 055 | list / list min 6x3 | 확인 | 확인 |
| 056 | logo-group / logos-6 min 6x3 | 확인 | 확인 |
| 057 | logo-group / logos-8 min 6x3 | 확인 | 확인 |
| 058 | matrix / extended min 12x6 | 확인 | 확인 |
| 059 | matrix / matrix min 12x6 | 확인 | 확인 |
| 060 | metric / stat min 6x3 | 확인 | 확인 |
| 061 | metric / stats-3 min 6x3 | 확인 | 확인 |
| 062 | metric / stats-4 min 6x3 | 확인 | 확인 |
| 063 | person / people-3-portrait min 12x6 | 확인 | 확인 |
| 064 | person / people-4 min 12x6 | 확인 | 확인 |
| 065 | person / person min 12x6 | 확인 | 확인 |
| 066 | pill / pill-3 min 6x3 | 확인 | 확인 |
| 067 | pill / pill min 6x3 | 확인 | 확인 |
| 068 | pricing / extended min 12x6 | 확인 | 확인 |
| 069 | pricing / plans-3 min 12x6 | 확인 | 확인 |
| 070 | pyramid / pyramid-3 min 12x6 | 확인 | 확인 |
| 071 | pyramid / pyramid-4 min 12x6 | 확인 | 확인 |
| 072 | pyramid / pyramid-5 min 12x6 | 확인 | 확인 |
| 073 | quote / quote-big min 6x3 | 확인 | 확인 |
| 074 | quote / quote min 6x3 | 확인 | 확인 |
| 075 | steps / steps-3 min 12x6 | 확인 | 확인 |
| 076 | steps / steps-5 min 12x6 | 확인 | 확인 |
| 077 | steps / steps-col-4 min 12x6 | 확인 | 확인 |
| 078 | table / table-3x3 min 12x6 | 확인 | 확인 |
| 079 | table / table-5x4 min 12x6 | 확인 | 확인 |
| 080 | table / table-7x6 min 12x6 | 확인 | 확인 |
| 081 | tag / extended min 6x3 | 확인 | 확인 |
| 082 | tag / tag-hl min 6x3 | 확인 | 확인 |
| 083 | timeline / track-4 min 12x6 | 확인 | 확인 |
| 084 | timeline / track-6 min 12x6 | 확인 | 확인 |
| 085 | timeline / track-alt-5 min 12x6 | 확인 | 확인 |
| 086 | venn / venn-2 min 6x3 | 확인 | 확인 |
| 087 | venn / venn-3 min 6x3 | 확인 | 확인 |
| 088 | versus / extended min 12x6 | 확인 | 확인 |
| 089 | versus / versus min 12x6 | 확인 | 확인 |
