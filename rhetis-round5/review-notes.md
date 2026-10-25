# ROUND5 주 에이전트 최종 검수 기록

불변 replica를 기준으로 다섯 컬렉션의 요소 CSS를 다시 작성했다. 원형이 다른 디자인은 독립 폴더로 만들고, 원형 미관측 일반 요소는 삭제했다. 요소별 출처는 ORIGINS.md에 한 줄씩 있고, 각 컬렉션 round5-report.md에 새 폴더·패널·차트 확장·삭제·남은 GAP·실제 열람 증거를 적었다.

최종 실제 폴더159개, fixture444개, 양모드 크기 칸5326개와 panel 칸128개다. 실제 열린 canonical669장(양모드 요소 시트318장, 원형 대조159장, 조립3열112장, foundation/panel80장)의 SHA가 최종 파일과 일치한다. root-visual-review.json은 전체 매트릭스의 배치·변형·최소 칸을 직접 대조한 기록이다. 모든 native 칸의 모든 글자를 개별 판독했다고 주장하지 않는다. 담당자는 native 시트를 상세 검수했고 주 에이전트가 전체 시트·112페이지 비교를 통합 검수했다.

## 실제 수정과 해석

- 연결선은 전체 연결 멤버를 가진 steps/flowchart/network/hub가 소유한다. 중첩 조직도는 network가 공통 버스를, hierarchy가 부서와 팀 관계를 소유한다.
- 카드 모양·표제 위계·노치·점선·시각 중심을 replica의 실제 수치에서 비율로 바꿨다. 작은 칸은 부차 note를 줄이고 줄 간격·글자 토큰을 조절했다.
- Seedmark 목차의 큰 제목은 DOM Range의 빈 상승부 때문에 raw24개 밖으로 계측됐다. 현재 소스로 fixture24칸과 조립02를 paired whole-canvas screenshot으로 다시 측정했다. 실제 칠해진 픽셀은25건 모두 상자 안이었다. raw JSON은 보존하고 integration의 paintBoundsResolution에 정확한 증거 경로와 해소한 후보를 기록했다. 잘림·겹침은 이 방식으로 해소하지 않는다.
- chip 광학 중심은 글자 fill을 숨긴 같은 화면과 차분해 원통/둥근 모서리를 문자로 세지 않는다. plain pill/tag 검사와 DOM 전수 검사, icon/복합 라벨의 수동 검수를 구분했다.
- CSS 첫 출처 주석을 명료하게 한 마지막 수정은 선언 본문을 바꾸지 않았다. 새 source FP로 다시 렌더하고 SHA가 달라진 곡선 안티앨리어싱 시트도 다시 열었다. 최종 확인 후 디자인 소스는 동결했다.
- 정수12×6 그리드로 조립할 때 원본 절대 위치와 일부 간격 차이가 남는다. 페이지 전용 보정 CSS를 추가하지 않았다. 사진/복잡한 이미지는 지정된 연회색 자리다. Lucide 가능한 아이콘은 구현했다.
- 원본 팔레트의 일부 작은 회색 글자에는 낮은 대비 후보가 남는다. source-style의 raw 후보246건은 공식 라이트·다크 요소의 대비 검사와 분리했다. 공식 팔레트 요소·패널의 확정 대비 오류는0이다. 계측이 실제 배경과 다른 후보는 컬렉션별 기록을 따른다.
- Seedmark18의 immutable replica 연결 관계가 원본과 다른 부분은 원본 관계를 해석해 조립했고 replica는 유지했다. 판독 불가의 작은 원문은 기존 replica의 작성 문구를 유지했으며 새 fixture는 별도 한국어 업무 문장이다. 원문6자 중복은0이다. 최종 검사에서는 foundation을 포함해 대소문자와 공백을 정규화했다. Onboard chapter의 공통 영문 CHAPTER 라벨 중복1건을 VOLUME으로 새로 쓰고, 해당 컬렉션 전체를 실제 재렌더했다.

## 남은 차이와 검증

표현 불가는 Seedmark20 단일 누적 막대와 Meridian14의15점 면 차트, 두 건뿐이다. GAPS.md에 이유와 필요한 마크업 확장을 기록했다. 일반 타이포·패널·페이지 도형을 GAP으로 버리지 않았다.

불변 replica711개 파일 해시 검사 차이0,1280×720 페이지와3840×720 비교 PNG 검사 통과, 실제 모든 PNG 크기·SHA는 integration-png-manifest.json에 있다. ZIP은 최상위 폴더·허용 확장자·CRC·로컬 의존성·manifest를 검사한다. 게시 및 실제 재다운로드 결과는 publication-verification.json에 별도로 기록하며, 게시 전에는 완료로 간주하지 않는다.

## 추가 요청: PDF와 소스 전용 ZIP

최종 크기 시트의 원래 PNG IDAT 압축 스트림을 PDF image stream에 그대로 넣었다. 개별10권은 총398페이지(요소318·foundation/panel80), 통합1권은 같은398페이지다. 모든 페이지의 원본 PNG 압축 픽셀·크기와 PDF image stream·MediaBox·배치 영역을 대조해 손실·잘림·비율 변경0을 검증했다. source-only ZIP은 css/html/js/json/md/py/txt만 허용하고 이미지·PDF·폰트·압축파일을 제외했다. 게시된 source-only ZIP의 실제 공개 재다운로드 바이트/SHA/CRC 일치도 확인했다.
