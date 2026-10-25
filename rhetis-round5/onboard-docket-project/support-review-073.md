# 073 담당자의 078 공간 도해 지원 검수

## 소유 범위

`space_parts.py`와 matrix, matrix-nine, concentric, venn, network, positioning 여섯 폴더만 작성했다. 공유 kit/foundation/map/reassembled와 다른 leaf는 바꾸지 않았다. 공용 시트 도구의 해당 leaf 출력만 생성했다. Crossrail 요소 CSS를 읽거나 옮기지 않고, root가 이 작업에서 새로 만든 초안을 소스 관찰에 따라 다시 작성했다.

원본형 replica06/08/14/15/16/17/18을 각각 1280×720으로 열고 실제 HTML 및 `source-subpart-measurements.json`의 하위 글자 크기까지 읽었다. source06의101×30 capsule·248px 원, source08/14의 원형 면·겹침, source15의 옅은 원, source16의 가는 목록선, source17의 bare figure, source18의 둥근 중성 bay를 근거로 삼았다. 미지원 source08 아이콘 도해를 Venn으로 위장하지 않았다. Venn은 이 계약의 plain-name 2–3집합이다.

## 실제 구성과 수정

- matrix:4칸 비교 min4×3 및 SWOT min8×6. SWOT의 네 list는 진짜 `onboard-docket-list`이고 각2개 업무 항목이 있다.
- matrix-nine:짧은 항목 min6×4, 긴 이름 포함 min6×6. 긴 제목이 작은 bay 밖으로 흐르는 것을 native 셀에서 확인해 두 번째 fixture의 정직한 min을 높였다. 각 축은3개 라벨이다.
- concentric:3링+optional note min5×4,4링 min6×4. 실제 링 개수로 지름/annulus를 계산한다. 이름+fig는 같은 줄이며, 작은 높이에서 note가 다음 링과 닿던 것을 확인해 note가 있는 fixture의 min을 정했다. note를 숨기지 않는다.
- venn:2집합 min5×3,3집합 min6×4. 원의 fill과 이름의 stacking을 분리했고, 세 번째 이름의 selector 우선순위로 core에 겹치던 문제를 수정했다. 글자 크기는 각 원 자신의 지름을 query하여 넓고 낮은 상자에서도 낱말을 불필요하게 쪼개지 않는다.
- network:4node min5×3,5node min6×4. node와 link가 같은 여유 폭을 쓴다. hypot/atan2로 공개 좌표 쌍의 선을 계산하고 실제 연결을 눈으로 확인했다. 긴 node 이름·강한 선·tone 변형도 검사했다.
- positioning:텍스트 mark min5×3, logo seat min6×4. 얇은 두 축과 가운데 capsule 문법을 썼고, seat는 같은 가로·세로 길이로 남는다.

12개 light/dark 전체 크기 시트를 모두 열었고, 최소/넓고 낮음/12×6의 원·이름·중첩 list·연결선 위험 사례는 native crop을 추가로 열었다. 재현→수정은 해당 요소별 최대3회 이내였다. 128개 crop을 모두 개별 장으로 사람이 읽었다고 주장하지 않는다.

## 고정 시트 검사

renderer `v2-grid-paint-font-parts-1`. 현재128 native 셀에서 outside/clipped/text overlap/outsideComponent/outsideParts/painted contrast/font failure 모두0이다. 여섯 leaf의 시트 fingerprint가 현재 자기 소스·의존 list·공유 tokens/foundation/fonts와 일치한다. readonly taxonomy 감사의 해당6폴더 오류0, 실제 신규 fixture의 원본6자 중복0, literal data-el scope 검사0이다. 오래된 min/이전 글자 크기의 사용하지 않는 해당 leaf crop10개를 제거했다.

| leaf | light+dark native cells | source fingerprint |
|---|---:|---|
| matrix | 20 | `c486728022b7f46c6b44b768088313630c41adc0911cdd916cc2a1fd6b984e90` |
| matrix-nine | 16 | `b1414b27356f21b737c080570bf80e95144e7c2ac9cd88b1c79c8a031eb85edb` |
| concentric | 20 | `52dc77852808e66f160329eb394c5297f6e44e21e3a21972e7ffcf78dfd592eb` |
| venn | 24 | `12999f33cf674951753d17a09e2e8aaab880fa9061a90ee7d1001518e092ba1e` |
| network | 24 | `6f9a45ab9b2af9cf0f7f32f7d256a3dcc42083747ce7be50d24d2d1e320ed551` |
| positioning | 24 | `8c1fd1e4765e8b7915b6151490187f9fa12e64e21e0a4aa656b9a70367cfff63` |

공유 list나 foundation/token이 이후 바뀌면 matrix를 포함한 의존 시트는 root의 최종 통합 렌더에서 다시 갱신해야 한다. `space_parts.py`를 다시 실행하면 해당 여섯 폴더의 지원 fixture를 덮어쓰므로, 후속 수동 수정이 있는 경우 실행하지 않는다.
