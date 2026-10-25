# 원문 조립 통합 수정

- source15는 mark 기반 source10과 다른 자기 자식 구성(kick/name/note/seat portrait)이다. 원본 DOM에서 261.25×422, kick y2/h43, title y59/18px, note y92/16px, 날짜16px, portrait y182/158×210을 측정해 child 소유 분기로 구현했다. 긴 인증 제목을 줄이거나 원문을 바꾸지 않았다.
- source16의 fig/name/note는 358×203에서64/18/16px 위계를 보존하고 두 축 최소값으로 낮은 칸에 비례 축소한다. note가 없는 figure 카드는 별도44px 비율을 유지해 폭/높이 제약을 서로 섞지 않는다. source10 mark 기본 도형과 위치는 변경하지 않았다.
- 신규 replica-15-portrait fixture는 원문 대신 새로운 한국어 사업 문구를 쓰고 같은 자기 자식 구성을 검수한다. map은 변경하지 않았다.
- 실제 원문 current10/15/16과 corner04를 독립 Chromium으로1280×720에서 렌더해 밖 글자/겹침/페인트 초과/폰트 오류0을 확인했다. 검수 증거는 work/element-rebuild/fix-two-assembly-qa.json이다.
