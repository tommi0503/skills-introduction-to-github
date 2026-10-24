
## Nested list ownership

- 중첩 list의 item display/flex-direction/justify/gap/padding 강제를 제거했다. 부모는 list 상자 위치·크기와 필요한 타이포만 정하고, 내측 marker/name/note layout은 list 자체가 소유한다. 필요한 이름 크기와 첫줄 line-height는 item에서 공유해 marker가 이름 첫줄과 정렬된다.
- 전체 fixture/light/dark 모든 규정 칸을 정식 재렌더해 glyph·겹침·대비·paint·폰트 오류0, stale0을 확인했다. 통합21leaf/196states 검수와 현재 소스 SHA 증거는 nested-list-validation.json이다. 관찰 scanline versus의 CSS는 수정하지 않았다.
