# Inferred card grid review

- note가 긴 카드에서 name/fig까지 함께 이동하던 중앙 flex 묶음을 제거했다. kick/hero(mark·fig)/name/note가 독립 grid 행을 쓴다. 자기 자식의 유무만으로 앞 행 높이를 정하고 note길이는 앞 행에 영향을 주지 않는다.
- rise는 각진 판·실제 하단 기단, anchor는 비어 있는 선과 네 귀퉁이 선택 손잡이를 적용했다. 실제 관찰된 다른5컬렉션 card는 변경하지 않았다.
- mandatory6개 및 기존 기타fixture의 DOM/data/문구/min은 그대로이다. 정식 양모드 모든 허용칸60states에서 glyph/겹침/대비/paint/font오류0이다.
- 두컬렉션 DOM 검수120states 모두 같은 행 nameTop/figTop 차이0.0px. 12x6와 최소칸 모두 포함하며 증거는 card-title-alignment-validation.json이다.

## 최종 상하 무게중심 보완

- 정보가 위에만 몰렸던 첫 grid 구성을 교정했다. note4줄의 논리 높이(kick+mark/no-fig는5줄)를 예약하고 kick/hero/name/note의 전체 grid 묶음을 세로 중앙에 놓았다. name은2줄/hero는공통높이이고 폭의 미세반올림도 행높이에 영향을 주지 않게 높이축으로 예약한다. note길이에 따른 flex 묶음 이동은 없다.
- 최종 정식120states0flags/stale0/현재SHA일치. DOM120states nameTop·figTop 최대차이 정확0px. 12x6 visible part bbox 기준 최대상단빈공간32.8%/하단38.5%, 중심오차는요소높이4.5%이내이고 실제 확대PNG에서상하균형을확인했다.
