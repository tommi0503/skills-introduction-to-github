# Seedmark 최종 native 검수 — 069

21개최종1280×720PNG를각각원래크기로직접확인. 겹침/대비후보5페이지는추가원래픽셀crop으로확인. 소스/CSS/맵/배치변경없음.

렌더: 2026-10-24T14:51:37Z. 자동9개 겹침은13/14/20에서 실제로 확인됐다. 대비7개 중06의4개·20의2개는검은면위흰문자로해소되지만16의1개는실제흰arc와흰문자충돌이다.09의면에의한가림은DOM후보가놓쳤다.

증거: `tools/integration-functional-069/seedmark-native-failures.png`, 개별crop도같은폴더. 21개PNG의SHA/판정은`seedmark-native-review-069.json`.

## 09 — painted-surface-occlusion

flowchart root row1/span5와 callout root row5/span2가5행을 공유한다. 콜아웃의 회색 면이 왼쪽 아래 설명·중앙 검은 문장·오른쪽 아래 KEYWORD를 실제로 덮는다. 자동overlap목록에 없던 실제 가림이다.

공통요소검토제안: grid를 바꾸지 않고 callout의 대표형을 실제 내용 높이와 하단 정렬로 정할 수 있는지 검토한다. 페이지별 selector/예외는 쓰지 않는다.

## 13 — text-overlap

prose.quiet 기간2050–2055년과 legend 타사/MIRI COMPANY 두 줄이 같은 row2에서 실제 겹친다. 그룹막대GAP과 무관한 잔여 보조 루트 충돌이다.

공통요소검토제안: 보조 문구와 범례의 대표 intrinsic 높이/정렬 기준으로 실제 트랙을 분리할 수 있는지 검토한다.

## 14 — axis-caption-overlap

chart-area/line root row2/span4의 하단축라벨과 prose row5/span2 첫 줄이 실제 겹친다. 자동6쌍은 모두 실제다.

공통요소검토제안: 차트의 plot/축이 요소의 끝에 붙지 않도록 공통 하단 공유여백을 예약하는 대표형 해법을 검토한다. 해당모든최소칸 재검증이 필요하다.

## 16 — white-stroke-over-white-type

검은 교집합 면은 있으나 흰 원호들이 흰 우리의핵심기술 글자를 가로질러 획과 합쳐진다. DOM대비ratio1을 단순 오탐으로 해소할 수 없다.

공통요소검토제안: core글자 뒤의 ink 면이나 실제교집합내 label 위치를 요소 자체의 공통기하로 확보한다.

## 20 — text-overlap

card의 자사예상영업이익률 제목에 legend MIRI COMPANY가 실제 겹친다.

공통요소검토제안: name+note만 갖는 card의 대표내부정렬과 legend의 intrinsic 구성을 검토한다. 페이지별분기나 기존grid변경은 하지 않는다.

## 나머지페이지

01–08,10–12,15,17–19,21에서 새 폰트페인트누락이나 의도치않은가림을 발견하지 못했다.04/17/18/21의계약GAP은잘못된빈문자로간주하지않았다. 이는원본과모든좌표/서체가동일하다는판정이아니다.13/14/20차트GAP이잔여범례/문구의겹침을정당화하지않는다.

주 에이전트와072작성자에게5개실패와원래grid/요소범위를전달했다. 이후수정및최종재렌더는그담당자가수행한다.

## 최종수정 후 재검수

072 최종동결 후 canonical09/13/14/16/20을각각1280×720으로다시확인했다.09하단문구·KEYWORD,14축/설명,16core/arc,20제목/기간/범례는실제로분리되어기존신고가해소됐다.13은승인GAP재분류로legend가빠진결과이며이를동일요소의위치수정으로주장하지않는다.이문서위의5건은발견시점의기록이다.최신FP/각PNG의SHA와후속판정은동명JSON resolution에기록했다.
