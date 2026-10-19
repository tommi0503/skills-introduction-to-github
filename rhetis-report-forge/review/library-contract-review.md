# Rhetis Report Forge 라이브러리 독립 계약 검수

2026-10-19. 라이브러리 소스는 수정하지 않고, 제공 README·taxonomy·kit-tokens·type-steps와 `collection/report-forge`를 대조했다. 주 에이전트가 동시에 소스를 보완하고 있으므로 아래는 정적 점검 시점의 결과다. 변경이 필요한 항목은 즉시 주 에이전트에게 전달했다.

## 점검 결과

| 항목 | 결과 |
|---|---|
| 컬렉션 구조 | `report-forge/` 영문 소문자·하이픈 이름. kit, foundation, 31개 요소 폴더, 각 CSS/JSON/영문 description 존재 |
| kit 메타데이터 | `rhetis.kit/2`, id `report-forge`, tokens/description 상대 경로 유효 |
| foundation 메타데이터 | schema/kit/registrations/tokenDefaults 정상 |
| element 메타데이터 | 31개 모두 `rhetis.design-library-element-source/1`, taxonomy의 계약 id 및 폴더 매칭 정상, registrations/tokenDefaults 객체 존재 |
| 공유 토큰 | `.slide`의 모든 공유 토큰 누락 없음. `.slide.dark`의 모든 color 토큰 누락 없음. 불필요한 비색상 토큰 dark 재정의 없음 |
| CSS 범위 | 중첩 at-rule까지 전개해 모든 요소 CSS selector 확인. 각 selector에 자기 `data-el="report-forge-<폴더>"` 범위 지정 존재. 범위 이탈 selector 미발견 |
| 타입 단계 | 모든 font-size는 `var(--type-N)`이며 허용 목록에 포함. px font-size 미발견 |
| 외부 리소스/금지 문법 | 요소 CSS에서 url, 이미지 참조, @import/@font-face/@keyframes/@property, 색 리터럴 미발견. 허용 at-rule 범위 준수 |
| 토큰 참조 | 공유 토큰, `--type-N`, 계약 값 `--v/--max` 외 미선언 변수 미발견. 요소별 추가 변수 default 누락 미발견 |
| fixture 수 | 31개 요소 각각 2개 이상, 요소 87개 + foundation 2개 = 전체 89개 |
| fixture 외곽 구조 | HTMLParser로 모든 요소 fixture 확인: body 자식 1개, min 첫 줄, 최상위 12×6 grid 배치 정상 |
| element data-el | 모든 요소 root와 중첩 card/list/tag/chart-bar 등 참조 root의 data-el 확인, 누락 미발견 |
| 내부 계약 구조 | card/pill parts, list item, table thead/tbody, matrix 4cell+2axis, versus 2side+vs, cycle/hub core, flowchart node grid 좌표 확인. 멤버 수 범위 위반 미발견 |
| 차트 값 | bars/lines의 --max와 각 bar/pt/stage/donut/meter의 --v 확인. 값 속성 누락 미발견 |
| 축소 규칙 | 각 요소에 @container 존재. kick를 먼저 숨기고 더 좁을 때 note를 숨기는 규칙 존재. name/fig 숨김 규칙 미발견 |
| 공식 미리보기 | 아래 명령으로 light/dark 생성 성공. preview 도구 자체는 시각·계약 검증을 수행하지 않는다는 점을 구분함 |

```sh
python tools/preview.py collection/report-forge contract/type-steps.json --out review/library-contract-light.html
python tools/preview.py collection/report-forge contract/type-steps.json --dark --out review/library-contract-dark.html
```

## 수정 필요 항목 — 담당자 전달 완료

### 서로 동일한 두 fixture: 7개 요소

SHA-256 원문 비교 결과 다음 `extended.html`이 기존 fixture와 완전히 동일했다. README의 2개 이상 개수는 충족하지만, 서로 다른 변형·멤버 수·긴 이름/긴 note를 검증하는 자료로서 부족하므로 서로 다른 한국어 콘텐츠 및 의미 있는 변형을 넣어야 한다.

| 요소 | extended.html과 동일한 파일 |
|---|---|
| flowchart | flowchart.html |
| image-frame | frame.html |
| legend | legend-bars.html |
| matrix | matrix.html |
| pricing | plans-3.html |
| tag | tag-hl.html |
| versus | versus.html |

특히 pricing은 3개 plan만 두 번 있으므로 2개 plan 또는 1개 plan fixture가 유용하다. legend는 키 개수 차이, flowchart는 다른 경로/결정 분기, matrix는 강조 quadrant 차이, image-frame은 긴 설명/다른 seat 비율, tag는 긴 라벨, versus는 양쪽 내용 길이 차이 등을 통해 의미 있게 바꿀 수 있다.

### 간격 리터럴의 엄격한 토큰 규칙: 3곳

- `elements/chart-bar/element.css`: `padding-left:20%`
- `elements/hierarchy/element.css`: `padding-top:24%`
- `elements/venn/element.css`: `margin-left:-6%`

이 값들은 일반 여백보다 차트 라벨/계층 배선/집합 겹침의 기하학적 위치에 가깝다. 다만 README의 “간격은 공유 토큰으로만”을 엄격하게 적용하면 예외로 명시되어 있지 않다. 따라서 안전한 처리로는 해당 값을 kit의 정식 확장 토큰에 선언하거나, 같은 시각적 geometry를 grid/position/transform으로 표현하는 방법을 권고했다. 0/auto, 원형 50%, 허용된 999px, 선/도형의 고유 크기는 이 이슈에 포함하지 않았다.

## 검수 범위의 한계

이 문서는 소스 계약·메타데이터·fixture 구조 독립 검수다. 모든 최소 칸과 모든 fixture를 light/dark 브라우저에서 시각 검토했다고 주장하지 않는다. line 차트 연결선과 cycle/hub geometry는 주 에이전트가 이미 보완 중이라고 알려 준 항목이므로 중복 blocking으로 보고하지 않았다. 최종 source 수정 뒤에는 중복 fixture와 3개 간격 선언을 재확인해야 한다.


## 최종 수정 뒤 재확인 — 해결 상태

위 최초 발견 목록은 수정 전 기록으로 보존한다. 최종 source에 대해 다시 정적 확인하고, light/dark 178개 개별 PNG의 시각 검수를 별도 `library-visual-review.md`에 기록했다.

| 최초 항목 | 최종 상태 |
|---|---|
| 7개 요소의 완전히 같은 extended fixture | 해결. 전체 요소 fixture를 SHA-256으로 다시 비교한 결과 동일 원문 중복 0개. pricing은 2plan/3plan, legend는 2key/4key 등 변형이 구별됨 |
| chart-bar padding-left:20% | 해결. 해당 선언 없음. 현재 토큰 기반 간격/기하 위치로 변경된 것을 재확인 |
| hierarchy padding-top:24% | 해결. 해당 선언 없음. 최종 root/branch 연결선이 보임 |
| venn margin-left:-6% | 해결. 해당 선언 없음. 겹침 도형이 보이고 라벨을 읽을 수 있음 |
| chart-line 점만 보임 | 해결. 표준 markup을 유지한 CSS anchor/실제 b anchor로 연결. 양 모드 6점/12점 PNG에서 모든 구간 및 수평 구간 확인 |
| steps/table 대비 보완 | 해결. 최종 075–080 PNG 양 모드에서 글자와 강조 구분 확인. 자동 감사 contrast 위반 0 |
| donut 정원/숫자 위계 | 해결. 최종 갱신한 022–024 PNG 양 모드 재열람. 정원과 수치 위계 확인 |
| funnel 45% 최소폭으로 작은 값의 폭이 같음 | 최종 시각검수에서 추가 발견 후 해결. --v를 도형 너비에 실제 반영하고 좌우 caption rail로 텍스트 분리. 최종 035–037 양 모드 개별 확인 |

전체 89 fixture(요소87+foundation2), 각 mode PNG89개, 크기 전부1280×720. 당시260case 검사 overflow0/contrast0 및 당시 donut/funnel24case 검사 overflow0/contrast0 결과를 확인했다. 그 시점의 폰트 false 상태는 아래 후속 최종검사에서 해결됐다. 이 재확인 작업에서는 library source를 수정하지 않았다.


### 후속 최종 폰트 검사

미리보기/capture에 Pretendard data URL을 내장한 뒤 전체 full/min260case를 다시 검사했다. 현재 `library-audit.json`은 font true260/260, overflow0, contrast0이다. 갱신된 양 모드178PNG를 모두 개별 재열람한 결과 폰트 변경으로 새 글자 잘림·겹침이 생기지 않았다. 이전 targeted24case JSON은 폰트 수정 전 기록이며 최종 근거는 전체260case JSON이다. 외부 리소스가 금지된 collection source CSS는 그대로 두고 배포용 미리보기/렌더 환경에서 폰트를 내장했다. 자세한 최종 시각검수는 `library-visual-review.md`를 따른다.
