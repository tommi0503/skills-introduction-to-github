# Halo Field — Round 5 요소 검수 보고

## 범위와 출처

동결 replica를 수정하지 않고 실제 관찰된 17개 디자인을 검수했다. 아래 페이지 번호는 halo-field 원본 덱의 페이지다. 컬렉션·foundation·도구·다른 덱은 수정하지 않았다.

| 디자인 폴더 | 원본 페이지 | fixture | 검수 상태 수 |
|---|---|---:|---:|
| `agenda` | 02 | 2 | 10 |
| `callout` | 12 | 2 | 12 |
| `card` | 05 | 3 | 24 |
| `card--program` | 12 | 5 | 50 |
| `card--service` | 07 | 5 | 60 |
| `chart-bar--combo` | 04 | 2 | 24 |
| `chart-donut` | 15 | 2 | 12 |
| `cycle` | 06 | 2 | 8 |
| `image-frame` | 06 | 2 | 36 |
| `legend` | 04 | 2 | 22 |
| `person` | 14 | 5 | 32 |
| `prose` | 04 | 3 | 26 |
| `pyramid` | 08 | 2 | 8 |
| `steps` | 09 | 2 | 8 |
| `steps--rings` | 11 | 2 | 14 |
| `table` | 13 | 2 | 16 |
| `timeline` | 10 | 2 | 8 |

## 재매핑과 소유권

- 관찰되지 않은 범용 폴더 및 분리 이전 폴더 43개를 제거한 구조를 유지했다. 기존 `chart-bar`/`chart-line`은 실제 콤보 차트 `chart-bar--combo`로 통합되었고, 04페이지 차트 표제·단위·하단 설명은 foundation panel로 귀속되었다. 삭제 내역은 `halo-deleted.json`을 따른다.
- 04페이지 둥근 패널 1개는 범례와 콤보 차트를 자식으로 가진다. 표제와 하단 설명을 요소에 중복하지 않았다. 패널 구현 및 최종 조립 검수는 주 에이전트 담당이다.
- 07 서비스 카드와 12 프로그램 카드는 각각 4개의 실제 멤버에 맞춘 고유 source fixture를 갖는다. 제목 길이, 번호, 설명 유무 및 사진 슬롯을 보존하고 새 물류 업무 문구로 작성했다.
- 14페이지 인물 그룹이 3명을 함께 소유한다. 개별 인물 instance는 `contained_by`와 함께 출처 crop 추적용으로 유지하며 그룹의 `absorbed_instances`에도 기록했다.
- 지도에서 남은 `unexpressible`은 0개다. 원문은 출처 지도에만 남기고 fixture에는 새 한국어 비즈니스 데이터를 사용한다.

## 발견하여 수정한 결함

- 단독 인물 카드가 가로로 긴 칸에서 초상화까지 가로로 늘어나는 결함을 수정했다. source 377.333×401 비율의 내부 캔버스를 맞춰 넣어 모든 구성 요소가 같은 비율로 움직이도록 CSS를 새로 정리했다.
- native 인물 초상화는 158.469×244.984px, 12×6 넓은 칸에서는 167.953×259.656px로 측정되었다. 두 상태 모두 원비율 약 0.64685를 유지한다. native 이름·설명·직함은 각각 약26/18/14px이며 원본 좌표를 유지한다.
- 서비스·프로그램의 반복 fixture 참조를 고유 멤버별 참조로 교체했다. cycle·steps·timeline의 기계 설비 문구는 실제 배송·배차·회수 업무 문구로 정리했다.
- 콤보 차트 fixture의 비정량 연도는 2032~2035로 바꾸고 실제 수치와 간격은 유지했다. 지도 원문 데이터는 변경하지 않았다.

## 실제 확인과 한계

- 17개 디자인의 라이트·다크 시트 34장을 실제 이미지로 열어 확인했다. 서비스/프로그램 카드, 링 단계, 콤보, 도넛, 인물, 피라미드, 타임라인, 단계, 순환의 source 비교 crop도 확인했다. 원·링·초상화 비율, 점선·접힌 면, 연결선, 설명 줄바꿈과 칩 중앙을 검토했다.
- 최종 요소 fixture 45개, 양모드·규정 크기 상태 370개 모두 현재 소스 해시와 일치한다. quick=false, stale=false이며 overflow·textOverlap·hiddenNameFig·contrastFailures·paintOverflow·chipAlignmentFailures·fontErrors가 모두 0이다. 17개 contract ID도 `contract/leaves.json`과 일치한다.
- 최종 source6gram 검사: foundation fixture를 포함한 47개 파일, issues 0. 마지막 문구 수정 뒤 관련 시트와 감사 결과를 다시 생성했고 전체 해시를 재확인했다.
- 이 보고서는 요소 시트 및 source 크기 검증의 결과다. 최종 15페이지 조립본, foundation 패널, 격자 투영 결과, 배포 ZIP·push 성공은 이 보고서의 완료 주장에 포함하지 않는다. 사진은 사용자 규칙에 따라 회색 placeholder이며 시트 아이콘은 점선 슬롯이다.

검수 완료 후 halo-field 요소 및 지도는 동결한다.
