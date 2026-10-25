# ROUND5 검수 기록

이 문서는 이전 라운드의56개 완성·일반화 수용 기록을 대체한다. immutable replica는 수정하지 않았다. 원형이 없는 일반 폴더32개와 대체된 chart-bar/legend/chart-stack3개를 현재 컬렉션에서 제거했고, 실제 관측 디자인39종만 유지한다.

원본·replica 단계의 차이와 replica→조립 단계를 분리했다. 사진·복잡한 이미지 아이콘은 허용된 연회색 면/Lucide 대체다. 원본18의 실제 연결 경로를 다시 읽어, 불변 replica에서 gateway 안으로 끝나거나 빠진 device 연결을 조립 network에서 바로잡았다. 원본의 읽히는 제목·본문·수치와 순서는 조립에 유지했고, 크기 fixture 문구는 새 한국어 사업 문장이다.

처음에는 정수 칸에 독립 부품을 흩어 놓아 범례·기간·캡션이 겹쳤다. ROUND5에서는 source top-down panel이 제목/기간/plot/범례를 소유하도록 재구성했다. 09callout은 실제78px 면, 07metric은 figure/name 왼쪽과 note 오른쪽, 17사진은200×121 capsule, 21pie는4share와 경계선을 보존했다. 모든 사진 data-ph 값은 빈 문자열이다.

실제 차이가 남는 부분: 원본21의 중간 회색30% 영역 흰 글자는 AA 확보를 위해 컬렉션에서 ink로 바꾼다. 패널의 전체12×6 배치에서 생기는 소수점 양자화와 글꼴 rasterization 차이를 완전 동일하다고 주장하지 않는다. 원본에 보이는3D/사진의 자세한 내용은 연회색 대체다. 진짜 계약 한계는 GAPS.md의 source20 한 관측치 예산4분할 bar1건뿐이다.

검수 중 contents의 DOM Range 상단 여분을 처음에는 글꼴 계측으로만 판단했으나, 전체 캔버스 paint 검사에서 실제 긴 note와 과대 글자도 발견했다.64/60/28px 원본 상한과 내부 선택점 여유를 적용해 수정했다. 최종 자동 후보와 실제 paint 결과는 round5-final-verification.json 및 round5-contents-paint-proof.json에 원자료를 보존한다. 후보를 지우거나 raw0이라고 바꾸지 않는다.

fixture의 긴 본문, 한 줄 career/결제 조건은 원래 의미를 유지한다. 단일 조건을 억지2항목 list로 늘리지 않고 owner.note로 표현했다. chart14 --max100과 실제 두 계열 범주를 유지했으며, 숨긴 빈 label이나 fake 두 번째 관측치는 쓰지 않는다. 모범 상태ID를 선언하지 않고 business-* 이름을 썼다.
