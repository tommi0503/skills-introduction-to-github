# ROUND5 최종 통합 검증

상태: `verified-with-recorded-candidates` · 2026-10-25T06:51:09.687950+00:00

실제 존재하는 디자인 폴더와 현재 지도·fixture·최소 칸에서 동적으로 집계했다. 이전 고정 개수/일반 요소/모범 fixture 의무를 적용하지 않는다.

|컬렉션|디자인|fixture|시트 칸|현재 FP 시트|panel 칸|잔여 GAP 인스턴스|
|---|---:|---:|---:|---:|---:|---:|
|vectorbox|18|36|440|18/18|0|0|
|seedmark|39|88|1052|39/39|44|1|
|crossrail|35|152|2178|35/35|8|0|
|meridian-deck|40|111|888|40/40|24|1|
|onboard-docket|27|57|768|27/27|52|0|

실제 페이지112장, 시트 허용 칸5326/5326개, 전용 panel 칸128개. 불변 replica 파일 해시711건 검사, 차이0건이다. 현재 원본6자 문구 겹침0건, 확정 계약 오류0건이다.

주 에이전트 검수 기록과 현재 SHA가 일치하는 canonical 이미지669/669장이다. 범위 원문: Full final sheet overviews; native crops on suspect cases. This does not claim every character in every native cell was separately read. Element authors also reviewed their own all-size cells.

집계 오류0건, 기록된 경고4건. 경고와 원본 style 대비 후보는 기능 통과나 원본과의 픽셀 동일성을 뜻하지 않는다. source 원문·자료 자체의 모순·그리드 차이는 컬렉션별 검수 기록과 GAPS를 따른다. [전체 JSON](integration-verification.json) · [실제 PNG 크기/SHA](integration-png-manifest.json) · [불변 replica 증거](integration-replica-preservation.json)

ZIP CRC·오프라인 의존성·압축 후 SHA는 package.py, 게시된 파일의 실제 재다운로드는 별도 게시 검증에서 확인한다.
