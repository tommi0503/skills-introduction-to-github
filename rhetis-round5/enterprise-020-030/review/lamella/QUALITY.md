# README 품질 기준 최종 점검 — round5

| 항목 | 확인과 결과 |
|---|---|
| 잘림·겹침 | 모든 fixture의 min 이상 지정9크기+min, light/dark 실제렌더. outside/clipped/hidden/member_outside/overlaps/shape_clipped/painted_outside=0. |
| 대비 | 신규 fixture의 실제 계산 전경/배경 대비 검사0건. source 조립의 inherited 대비 문제는 review-notes.md에 별도 기록. |
| 아이콘 크기 | 요소별 원·배지/내부 아이콘 실측 및 native 시트 확인. Lucide 대체 자형 차이는 기록. |
| 정렬 | chip_alignment0; 같은 멤버 제목·숫자 기준선과 최소칸 시각정렬 직접 확인. |
| 남은 장식 | 연결선/탭은 요소 소유, 장면 면·벡터는 foundation 소유. source 중복 측정2건 제거. |
| 차트 | 공유축/시리즈/조각/주석을 자체 요소로 구현, 라벨·멤버 overlap0. |
| 디자인 일관성 | replica 출처별 실제 디자인만 유지. round5가56개 완전성 요구를 폐지하므로 없는 일반 요소는 제외. |
| 다크 | 모든 fixture/크기 dark PNG도 실제렌더·직접 검수; 폰트 대체0. |
| 중복 금지 | 샘플의 폴더/계약 형식만 참조. source 없는 일반 디자인329개를7덱 전체에서 제외·보존. |

이 표의 통과는 신규 라이브러리 fixture의 검수 판정이다. 동결 replica의 기존 오류/placeholder/12×6 양자화 잔차가 없다는 뜻은 아니다. 구체적 차이는 review-notes.md를 따른다.
