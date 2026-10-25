# Advanced elements review

- concentric 중간면의 역할 `--a1-5`는 유지하고 글자 역할을 `--page`에서 `--ink`로 선택했다. 원본의 흰 글자와 달라지지만 기준 팔레트의 밝은 중간면/흰 글자 대비 약2.72를 그대로 적용하면 계약 대비 기준을 통과하지 못한다. `--ink`는 라이트 약6.17, 다크 약5.19로 읽힌다. 이는 색 역할의 접근성 재해석이며 구조 표현불가 사항이 아니다.
- 원본 포함 오각형은641:609 비율을 유지한다. 넓고 낮은 칸에서는 도형을 가운데에 맞추고 글자 크기도 도형의 너비·높이 중 작은 배율로 맞춘다.
- 4개 집합 확장에서는100/75/50/25%의 별도 등비 포함 프레임과 공통 fit 높이에 맞춘 노출 밴드를 사용하여 이름·수치가 이웃 집합에 가려지지 않게 했다. 관찰된3개 집합 프레임은 원본 수치를 유지한다. 수치를 가진 집합은 각 도형의 자체 container에서 글자 크기를 정한다. 실제 수치와 이름은 숨기지 않으며 아주 작은 내부 칸에서는 note만 숨긴다.
- positioning의 두 줄 이름은84px, 기본 한 줄은98px, 강조 멤버는130px를 원본 기준 상한으로 사용한다. 원본의 중립 한 줄100px 원 하나는 같은 구조의 다른 중립 멤버와 구분할 계약 데이터가 없어98px로 정규화한다.

- code.block의 monospaced 계약을 충족하기 위해 요소 기본값 확장으로 `--corner-signal-code-font`를 element.json tokenDefaults에 선언하고 제공 글꼴 Nanum Gothic Coding을 선택했다. CSS는 이 namespaced 변수만 참조한다. 공유 font-body/display를 변경하지 않는 정적 타입 기본값 예외이며, 부모의 명시적 판단에 따른다.

## Final construction review

- 관찰이 없는 advanced 요소는 다른 컬렉션 CSS에서 복사하지 않고 계약 부품에 chamfer와 상단 강조 edge, 관찰된 포함 오각형과 축 bubble 문법을 적용했다. 공통 의미 구조와 별개로 실제 bar/node/pan/cell 면과 선 끝을 다르게 구성했다.
- Sankey의 추가 nested split, roadmap milestone, decision-tree 3답변, network 수직·수평·대각 link fixture를 넣었다. source의 members/연결선은 각 members 컨테이너에 귀속된다.
- 좁고 낮은 칸의 실제 glyph와 paint 검수에서 slope의 마지막 endpoint capsule 하단 여백을 보완했다. matrix-nine의 axis-y 단어를 10px 한 줄로 유지해 어중간한 한국어 음절 줄바꿈을 피했다.
- code의 문자열 색은 상태용 good보다 n-1 바탕 대비가 높은 팔레트 자리 a3-7로 해석했다. 글꼴과 syntax 색의 의미를 분리했다.

## Final browser audit

- 공식 최종 엔진 `32da5568e6e5`으로 담당 14요소의 fixture × 모든 허용 칸 × light/dark, 총 266상태를 fresh 렌더했다. glyph 경계·겹침·실제 배경 대비·paint overflow·폰트 실패·chip 광학 중심 경고 0건이다.
- 검수 뒤 현재 CSS/JSON/fixtures/kit/foundation/map·엔진의 SHA를 다시 계산해 모든 audit과 일치함을 확인했다. 출력 PNG 해시와 파일 무결성, 모든 브라우저 canvas 1280×720도 확인했다. 전체 98요소/1766상태 통합 증거는 `advanced-validation.json`이다.

- 최종 통합 시각 검수에서 balance pan 안의 name+item 묶음을 수직 중앙에 맞췄다. beam/pan/tilt 기하와 item 사이 토큰 간격은 그대로 두었다. 이7요소만 PNG가 바뀌었고 다시 정식16states 검수0을 확인했다. 공통 foundation SHA 갱신 뒤 나머지91요소 PNG는 이전 검수본과 해시까지 같다.
