# 최종 통합 검증

상태: `verified-with-recorded-candidates`. 생성시각: 2026-10-24T16:35:20.671583+00:00. 이 보고서는 이전 author 요약의 오래된 SHA·칸 수를 대체한다. 원본과의 시각적 동일성 및 계약 GAPS는 자동 기능 검사와 구별한다.

|컬렉션|요소|fixture|시트 칸|현재 FP 시트|6자 겹침|확정 계약 오류|GAPS|
|---|---:|---:|---:|---:|---:|---:|---:|
|vectorbox|56|166|1966|56/56|0|0|5|
|seedmark|56|206|2632|56/56|0|0|11|
|crossrail|56|243|3244|56/56|0|0|34|
|meridian-deck|56|195|2224|56/56|0|0|15|
|onboard-docket|56|172|2016|56/56|0|0|20|

원본112페이지. golden140개는 visible field text135개동일·실제문구차이5개이며,그5개에는각각원문6자충돌근거가있다. raw DOM비교의추가29건은끝빈줄등formatting-only차이로문구변경이아니다. 새fixture나CSS변경없이감사판정만정정했다. [140개개별근거](integration-golden-text-evidence.json)를참조한다. golden fixture는 컬렉션별28개, 총140개의 구조·수치 계약을 검사했다. 원문6자 금지가 우선하는 텍스트 예외와 모범 구조에 원래 들어 있는 예외는 상세 JSON에 남겼다.

기존/새 replica 474파일 해시 확인, 변경 0건. 새 컬렉션 CSS와 보존된 v1 CSS의 완전 동일 파일 0건이다. 이 byte 검사는 디자인 독립성 자체의 증명은 아니다.

PNG 13679개의 실제 크기·SHA를 [PNG 명세](integration-png-manifest.json)에 기록했다. 조립·foundation·원본 replica 페이지는1280×720, 세 열 비교는3840×720이다. native cell과 요소 전체 시트는 행·크기 수에 따라 다르며, 현재 결과와 과거 진단 이미지를 역할로 구분한다.

일반 DOM chip 측정 3514건과 별도로, 단일 채움 pill/tag의 실제 글리프 중심 504건을 측정했고 후보 0건이다. 여러 부품이나 inline 강조는 실제 캡슐 중심과 같지 않아 별도로 제외했다. Seedmark의 eligible0을 측정 통과로 주장하지 않는다.

주 에이전트 최종 원본·조립 비교 및 현재 시트 검수 775/775장(요소 mode560·mapped 비교79·triples112·foundation24)의 SHA가 모두 현재 결과와 일치한다. 주 에이전트 직접 검수의 현재 SHA와 일치하는 요소 mode 시트는 560/560장이다. 검수 범위 원문: Full final sheet overviews; native crops on suspect cases. This does not claim every character in every native cell was separately read. Element authors also reviewed their own all-size cells.

확정 집계 오류 0건, 기록된 경고 0건. 세부 후보·현재 fingerprint·도구 SHA·참조 계약 SHA·superseded 목록은 [전체 JSON](integration-verification.json)을 따른다. ZIP CRC·업로드 다운로드 일치·Git push는 root의 패키징/배포 검증에서 추가한다.
