# Rhetis 컬렉션 독립 재조립 검수 기록

## 결과와 재현 방법

- 대상: 053(9), 054(20), 056(20), 057(11), 058(20), 060(30), 061(2), 총 112장.
- 생성기: `scripts/assemble-library.mjs`.
- 데이터: `src/assembly-data.json`. 실제 Chromium에서 각 원본 재현 페이지의 텍스트, bounding box, computed style, native table 셀, 좌석, SVG text/polyline/rect/axis 정보를 추출했다. 마지막 추출은 054-08/19의 최종 수정 이후 실행했다.
- 결과: `outputs/assembled.html`. React나 원본 PNG를 실행/삽입하지 않는 독립 HTML이다. 컬렉션 토큰, foundation 및 요소 CSS는 생성 시 `collection/report-forge/`에서 다시 읽어 합친다. 요소 CSS를 별도로 재작성하지 않는다.
- 모든 본문 슬라이드는 계약 foundation의 `.page > .head + .body`와 12열×6행 grid로 구성했다. 요소 root/data-el/parts 구조를 사용한다. 표지는 foundation cover/lockup/meta/seat를 사용한다.
- 페이지 저작 영역 `.overrides`에는 배치와 수치형 여백/타입 선택 및 덱별 테마 토큰을 사용한다. 054 빨강, 060 초록 등 원본의 색 언어를 구분한다.
- Pretendard variable WOFF2 전체를 HTML에 base64로 내장했다. 결과 HTML은 외부 폰트 서버나 React/Vite 실행 파일 없이 열 수 있다.

## 사용 및 편집

```bash
# 저장된 DOM provenance를 사용하고 최신 컬렉션 CSS로 다시 조립
node scripts/assemble-library.mjs

# 최종 원본 재현 페이지에서 내용을 다시 수집
node scripts/assemble-library.mjs --refresh

# 조립본 112장 native screenshot와 overflow/폰트 검증
node scripts/assemble-library.mjs --audit
```

개별 URL: `/outputs/assembled.html?deck=053&slide=22` 또는 `/outputs/assembled.html#053-22`. 전체 화면은 query/hash 없이 연다. 인쇄 CSS는 각 슬라이드를 1280×720 한 페이지로 출력한다.

## 내용 및 의미 검증

`review/assembly-manifest.json`은 슬라이드별 원본 deck/id, source URL/reference 경로, 사용 요소, 원문 ref 개수, 누락 ref, 좌석/SVG 개수와 도형에서 복원한 차트 값의 근거를 기록한다. 결과의 각 텍스트 span에는 `data-source-ref`가 있다.

- 추출된 원시 텍스트 및 표 셀 ref: 2,184개.
- 원문의 독립적인 bullet glyph 50개는 본문 문장과 구분했다. 실제 문장/제목/수치 누락은 0건이다.
- 060-18의 SVG rect/수치 축에서 막대 4개 값을, 060-19의 SVG polyline/수치 축에서 점 8개 값을 복원했다. 총 12개 보간 수치는 원본 SVG 좌표, 축 범위와 복원 방법을 manifest에 별도 기록했다.
- 여러 계열이 혼재한 복합 그래프는 1차 계열을 라이브러리 차트로 표현하고 추가 계열/축/범례 텍스트를 보조 카드에 보존했다. 축 눈금을 데이터 점으로 잘못 처리하지 않도록 수정했다.
- 058-15는 7개 인쇄 수치에 더해 Week 8의 명시적 `1만 달성`을 10,000으로 환산해 최종 milestone에 연결했다. 초기 조립에서 빠진 마지막 점을 원본 이미지와 대조해 복원했으며 임의 보간값은 아니다.
- 비중은 donut, 일정/월/요일은 timeline, 단계는 steps, SWOT·포지셔닝은 matrix, 순환 구조는 cycle, 연결 키워드는 hub, 팀원은 person, 정렬된 셀은 table을 사용했다. 056-12는 본부→4개 팀→8개 역할, 058-19는 TFT 팀장→2개 팀→6명 구성원의 계층 연결을 유지했다.

## 시각 검수와 수정

실제 Chromium으로 전체 112장을 렌더했다. 초기 전체 검사와 수정 후 전체 검사를 수행하고, 실패가 남은 레이아웃/차트 의미 문제 및 컬렉션 CSS 최종 수정에 대해서 추가 검증했다. 초기 결과는 `audit-assembly-pass1.json`, `audit-assembly-pass2.json`에 역사적 기록으로 남겼으며, 최종 판정은 `audit-assembly.json`이다.

대표 레이아웃은 개별 1280×720 PNG를 직접 확인했다: 053-22/24, 054-02/04/06/14, 056-04/06/16, 057-08/10, 058-15/19, 060-18/19/26, 061-02. 카드/표/타임라인/SWOT/팀 프로필/선 그래프/막대/도넛/순환/목차를 별도로 검토했다.

주요 수정: 큰 숫자나 안내문을 제목으로 오인하던 로직, 목차의 페이지 번호 누락, 긴 문장의 카드 overflow, container에 의한 note 숨김, 수치 축의 데이터 오인, 연결용 짧은 polyline의 차트 오인, source footer 위치, 좁은 조직도의 재배열, label·figure pairing을 수정했다.

## 최종 검사

- 슬라이드 112/112, PNG 112/112.
- 모든 페이지 및 PNG 1280×720.
- Pretendard 폰트 로딩 112/112 정상.
- 숨겨진 본문, 영역 초과, 요소 overflow 검사: 0건.
- 의미 있는 원문 텍스트 ref 누락: 0건.
- 최신 확정 컬렉션 CSS를 읽은 최종 HTML을 실제 렌더한 PNG로 제출한다.

재조립본은 컬렉션의 공통 레이아웃으로 다시 구성한 결과이므로 원본 재현본과 구도가 다를 수 있다. 원본을 그대로 따라 만든 결과는 별도의 `renders/replica/`이며, 재조립 결과는 `renders/assembled/`다. 표/차트/텍스트는 DOM으로 편집 가능하고, 사진·3D 자산은 원본 미사용 원칙에 따라 좌석 placeholder로 다룬다.

## 최종 통합 보완

060-02의 첫 열 번호를 header로 잘못 분류하던 조건을 제거하고 01–09 목차를 모두 복원했다. 057-06은 제목/본문의 bbox edge 관계로 묶어 3개의 제안 카드로 정리했다. 카드 제목은 22px(긴 제목 18px), 본문 16px, 여백 20px를 선택했다. 056-04와 060-08은 월/주 x축을 실제 차트 아래에 놓고 KPI와 목표 비교표를 분리했다. 주 에이전트는 이 6장과 053-24의 최종 PNG를 각각 직접 확인했다. 전체 PDF와 시트는 이 보완 후 다시 출력했다.

25개 페이지의 추가 명시적 교정 근거는 `assembly-semantic-fixes.md`, 수정 전·후 개별 검수는 `assembly-individual-A.md`와 `assembly-individual-B.md`를 참고한다.
