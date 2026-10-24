# Advanced elements review

- code.block의 monospaced 계약을 충족하기 위해 요소 기본값 확장으로 `--anchor-frame-code-font`를 element.json tokenDefaults에 선언하고 제공 글꼴 Nanum Gothic Coding을 선택했다. CSS는 이 namespaced 변수만 참조한다. 공유 font-body/display를 변경하지 않는 정적 타입 기본값 예외이며, 부모의 명시적 판단에 따른다.

## Final construction review

- 관찰이 없는 advanced 요소는 다른 컬렉션 CSS에서 복사하지 않고 계약 부품에 비어 있는 얇은 outline 판, 강조 부품의 네 귀퉁이 selection handle 문법을 적용했다. 공통 의미 구조와 별개로 실제 bar/node/pan/cell 면과 선 끝을 다르게 구성했다.
- Sankey의 추가 nested split, roadmap milestone, decision-tree 3답변, network 수직·수평·대각 link fixture를 넣었다. source의 members/연결선은 각 members 컨테이너에 귀속된다.
- 좁고 낮은 칸의 실제 glyph와 paint 검수에서 slope의 마지막 endpoint capsule 하단 여백을 보완했다. matrix-nine의 axis-y 단어를 10px 한 줄로 유지해 어중간한 한국어 음절 줄바꿈을 피했다.
- code의 문자열 색은 상태용 good보다 n-1 바탕 대비가 높은 팔레트 자리 a3-7로 해석했다. 글꼴과 syntax 색의 의미를 분리했다.

## Final browser audit

- 공식 최종 엔진 `32da5568e6e5`으로 담당 14요소의 fixture × 모든 허용 칸 × light/dark, 총 250상태를 fresh 렌더했다. glyph 경계·겹침·실제 배경 대비·paint overflow·폰트 실패·chip 광학 중심 경고 0건이다.
- 검수 뒤 현재 CSS/JSON/fixtures/kit/foundation/map·엔진의 SHA를 다시 계산해 모든 audit과 일치함을 확인했다. 출력 PNG 해시와 파일 무결성, 모든 브라우저 canvas 1280×720도 확인했다. 전체 98요소/1766상태 통합 증거는 `advanced-validation.json`이다.

- 최종 통합 시각 검수에서 balance pan 안의 name+item 묶음을 수직 중앙에 맞췄다. beam/pan/tilt 기하와 item 사이 토큰 간격은 그대로 두었다. 이7요소만 PNG가 바뀌었고 다시 정식16states 검수0을 확인했다. 공통 foundation SHA 갱신 뒤 나머지91요소 PNG는 이전 검수본과 해시까지 같다.
