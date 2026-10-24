# 078 inferred support second review (072 담당)

이 기록은 추가7폴더 funnel·pyramid·hierarchy·cycle·hub·flowchart·swimlane 및 색 별칭 제거를 위해 다시 인계받은 radar·slope의 최종 상태다. 기존8종의 다른6폴더와 공용 kit/foundation/map/reassembled/replica를 수정하지 않았다. root가 이번 작업에서 새로 쓴 structure_parts.py 초안을 검토·보정했고 모든 해당 CSS는 통째로 생성한다. 이전v1이나 타 컬렉션 CSS는 사용하지 않았다.

## 원본과 대조한 판단

원본09의 넓은 알약형 조직명과 작은 중성 알약 잎,10의 일관된 행 간격과 notch,15의 원형 면·삼각 화살표,16의 얇은 구획선을 기준으로 삼았다. hierarchy의 허용2–4부서는 원본의 두 중간 임원/5부서 전체 그림을 위장한 것이 아닌 별도 inferred fixture다.

- funnel은 실제 share에 비례하는 면으로 바꿨다. 초기25%최저 폭은 값0을 잘못 표현하므로 없앴다. 이름·수치는 별도 paper 지지면에서 읽히고,6단계와0%도 남긴다.
- pyramid는 좁은 맨 위의 이름이 두 글자씩 깨지지 않도록 이름을 고정하고 note가 먼저 줄을 바꾸게 했다. 낮은 칸에서는 공유 간격·type을 내린다.
- hierarchy는 원본09처럼 root/부서/leaf를 모두 capsule로 묶고 세로 연결을 잎까지 이어 그렸다. 고정64px 대신 source 크기에 가까운 공유 토큰 산술을 쓰고 전체를 중심에 놓았다.
- cycle/hub 초안은60열 모두에 gap이 붙어 좁은 칸의 실제 grid 폭이 root를 넘었다. 텍스트 후보0이어도 배경이 잘리는 실제 문제여서 column-gap을0으로 고쳤다. 좁은 core의 긴 타원도 source 어휘의 작은 capsule로 바꿨다. cycle은 compact 순서 컬럼에도 아래 방향 화살표를 남긴다.
- hub의 ellipse 반경·hypot·atan2·mask를 실브라우저로 검증했다. 4방향에서 mask가 none이 아니며 거리142.797/390.953px와90/−180/−90/0도 회전으로 계산됐다. 0축의 나눗셈도 min에서 유한58.8/135.75px cut으로 해석됐다. core를 올바른 중앙에 놓고 member 높이와 cut을 함께 줄여 위·아래에도 실제 선 구간을 남겼다.
- flowchart.ask는4삼각 gradient로 다이아몬드를 그린다. node 자체를 clip하지 않아 가로 after와 세로 before의 두 방향 연결이 동시에 보인다.
- swimlane은 자기 lane 수2–5를 읽어 row 수를 정한다.3담당자 fixture에서 분기·좌향 연결을 추가로 검증했다.
- radar/slope의 새 색 별칭은 전부 없앴다. 직접 팔레트 역할만 쓰고 ordinal 기본색보다 명시적 tone이 우선하도록 specificity도 바로잡았다.

## 검수 결과

모든 fixture와 모든 허용 크기의 light/dark 시트를 직접 확인했다. 좁은 radial,6단계0% funnel,최소 pyramid,3담당자 흐름,hub의 cardinal 마스크는 native cell에서도 확대 확인했다. 각 표의6범주 후보는 영역 밖/실제 clip/텍스트 겹침/실색 대비/하위 요소 초과/부품 초과다. 모든 폰트가 선언·로딩됐고 최신 sheet fingerprint가 현재 source와 일치한다.

|요소|fixture|양모드 실렌더칸|6범주 후보|
|---|---:|---:|---:|
|funnel|3|30|0|
|pyramid|2|22|0|
|hierarchy|2|18|0|
|cycle|2|16|0|
|hub|2|16|0|
|flowchart|2|16|0|
|swimlane|3|22|0|
|radar|3|26|0|
|slope|2|14|0|

9폴더 묶음 SHA256: `61b4438e2bd6e0ff805627b96d33974a4057d76af4dd7c22587d960173868cb7`

검사 시점: 2026-10-24T13:33:21.195260+00:00

현재 partial 정적 errors0/원문6자중복0, supplementary contracts 확정오류0이다. 전체 컬렉션의 pending/다른 요소 후보는 이 지원 범위의 완료와 구분한다.

```json
{
  "checks": [
    {
      "leaf": "funnel",
      "fixtures": 3,
      "cells": 30,
      "candidateCounts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "fingerprint": "cdeb32d4f85e0f2e6fff8de48e9cdeb1d0697468537db3d219b06bb104b4dd74"
    },
    {
      "leaf": "pyramid",
      "fixtures": 2,
      "cells": 22,
      "candidateCounts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "fingerprint": "114b398afcdb494156d131b54a217b926e25514119628a0de41b6199f4f8afd7"
    },
    {
      "leaf": "hierarchy",
      "fixtures": 2,
      "cells": 18,
      "candidateCounts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "fingerprint": "bacc6e9686b7f45fcf24c49451958cafae05d8cd95644710f5afaecb256f6c79"
    },
    {
      "leaf": "cycle",
      "fixtures": 2,
      "cells": 16,
      "candidateCounts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "fingerprint": "5613fac810851ae0664cfd9f70f89646980833cad17fc87b5cf0b8c1e2c68ba2"
    },
    {
      "leaf": "hub",
      "fixtures": 2,
      "cells": 16,
      "candidateCounts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "fingerprint": "a4cc36fdd172aa0cd90311091ee1db5607431478757e516df9470ce7756dbf6b"
    },
    {
      "leaf": "flowchart",
      "fixtures": 2,
      "cells": 16,
      "candidateCounts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "fingerprint": "ea89c27599e04b79bc6688dfc3cae613a0e732ddc63ff3a8814227ed4be0f721"
    },
    {
      "leaf": "swimlane",
      "fixtures": 3,
      "cells": 22,
      "candidateCounts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "fingerprint": "42f6d03a9778e688fe2231b7b0b8c733eab3c7aad3d422b222b8e6d94df972bb"
    },
    {
      "leaf": "radar",
      "fixtures": 3,
      "cells": 26,
      "candidateCounts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "fingerprint": "001b117e983a33ea648d8e7f067c589fd905c930b2aed8c99db41cdb2256fa1a"
    },
    {
      "leaf": "slope",
      "fixtures": 2,
      "cells": 14,
      "candidateCounts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "fingerprint": "f6c6eb475f230be95b486a2bbadccf384c174e26eb59141fcb3562a9d3fbcb98"
    }
  ],
  "fontFailures": [],
  "files": {
    "onboard-docket/elements/funnel/description.md": "4254753e2480f5175da7ffec2777f4027632e8085bb20c90bb3020a51426946e",
    "onboard-docket/elements/funnel/element.css": "b590e6fb0812bb3bb075f1d5a4dbef6ec942cb183538f5082c2606aad3c6ee05",
    "onboard-docket/elements/funnel/element.json": "449547081d223ca510f6fa33ec6c99e2fbbf2500e23cf09f6f93254dcaf9d4a2",
    "onboard-docket/elements/funnel/fixtures/five-levels.html": "f224a8b617d825d009e3fc8e1c865c7c4fb63ff75c36fc85c53381cfc3f93660",
    "onboard-docket/elements/funnel/fixtures/six-stages-zero.html": "05a2153ea10695afaac572925c4827763a536f1797e0ce2f0b5872cb88e449bd",
    "onboard-docket/elements/funnel/fixtures/three-levels.html": "92fe774173798a52c7c884999a13f1004f05ae75590324409dd285eed569e211",
    "onboard-docket/elements/pyramid/description.md": "380057363f7e055cbbc1f1c0ed191a18b39b484c36e5a55f4065b1be52515e64",
    "onboard-docket/elements/pyramid/element.css": "f6d70a687c57c0efb81a9b6803d6d4e2b55c77f629d1d1124e7b4c9694c79fb4",
    "onboard-docket/elements/pyramid/element.json": "728660d0729e8eb8834def14167b9a83d8e51eb01df0d483401e00b079eb5a11",
    "onboard-docket/elements/pyramid/fixtures/five-levels.html": "7e14ff03d1760a1f26204b0e48ac7882a37977b20a7558beca984e7c9c20984c",
    "onboard-docket/elements/pyramid/fixtures/three-levels.html": "972f2119a984eec373528df17b40a252fbd0fb27822b0cd4d1c45be27713f904",
    "onboard-docket/elements/hierarchy/description.md": "365285df3501ae3cebe4b273fe13ff03754072da1281dce8bd0a4de762279bec",
    "onboard-docket/elements/hierarchy/element.css": "32a52ec401060e618b062ca688b7dbd635d2d59781e806a8c480bbb2aa18b256",
    "onboard-docket/elements/hierarchy/element.json": "3970928aa68b0e3a69303b7d138d2c24839ab50bb2d43def75974911fb05a585",
    "onboard-docket/elements/hierarchy/fixtures/four-departments.html": "8384caa749a62c3aa38310208ce607bce783ba01021fc7a143d654140c0823cf",
    "onboard-docket/elements/hierarchy/fixtures/two-departments.html": "e1cd31fbbd17c62ade8a294f50b46887ab164d7ba562a8f2371adabc3e1b8442",
    "onboard-docket/elements/cycle/description.md": "99f2feda9c1da66409a44c2a691d5cb4053e48c4289d3b7ef5b53eb3e46e2ea4",
    "onboard-docket/elements/cycle/element.css": "2b90ec00cc038b0d0d296b45441cb0ab92edf0afd2fa1aeb397c37a1a1801da1",
    "onboard-docket/elements/cycle/element.json": "114ae26607fc800a85e53cf0dc0004c05dee1204ca58a97e6be01ef28f513cca",
    "onboard-docket/elements/cycle/fixtures/four-members.html": "ec2f69a2db07f2cca5edee53147390b1bb7b5d901e2f7c945b73ef155b943fa2",
    "onboard-docket/elements/cycle/fixtures/six-members.html": "c3b37e7a1efb48526dfe4ed1afd46f1a81f4405acd5347830f2273b12ed9c9f7",
    "onboard-docket/elements/hub/description.md": "dd8528f1409ef546394571b406dce9f7e428efd8be3bed5691afa9d5ad193ce9",
    "onboard-docket/elements/hub/element.css": "e9935ee87adb749b7016eefb01a73ea0879163a0dd70ac4114508847481640c3",
    "onboard-docket/elements/hub/element.json": "e28865251712fe36b4d4691076ed0b9c4ca4f3f0188db3abfa10b34e138ba7aa",
    "onboard-docket/elements/hub/fixtures/four-members.html": "3f93832c38b8a845da6932b00be87af77f7f7963bc106cd2be474de8b1512ddb",
    "onboard-docket/elements/hub/fixtures/six-members.html": "d6545c995eb50d93e52b33301ce7b599495c800fbd7b1c2030f54b6321392547",
    "onboard-docket/elements/flowchart/description.md": "ca2442fe82374647befda81a64a3043217826fd67b2204cacfd083fd5a928f20",
    "onboard-docket/elements/flowchart/element.css": "986f019f5becd999954d6cefc49ad6e2d139c7c8a22a2729179cf50e4bd01f21",
    "onboard-docket/elements/flowchart/element.json": "1b5a39cbcdf5a116a962064353eeb13ffb49d7247d6cce167e576fdb7fd1c625",
    "onboard-docket/elements/flowchart/fixtures/exception-review.html": "13ce3aa100ebc54f2f1eb3c687ef55b3def15fc3032d4f8bae0151e931f9a1d7",
    "onboard-docket/elements/flowchart/fixtures/request-approval.html": "54a57b917069c9704e7f394f634877d4931e808934a47ed402d277e4e20f0994",
    "onboard-docket/elements/swimlane/description.md": "414fd270a31448c536d7936d16e3570d70e769158584ddf8f27dbc975899c325",
    "onboard-docket/elements/swimlane/element.css": "0ac3d61960bcdb0fb419ce881368bcca7c9576b996d257cb756dcc2ffa5084bb",
    "onboard-docket/elements/swimlane/element.json": "0877d352bb720e6b87b28181c337111b670e97f2abc79e62b4e4d0752706055a",
    "onboard-docket/elements/swimlane/fixtures/exception-review.html": "1c8eb0b195893062bcb0a3018e6633fe43e0a2715b81a6daea2183463aaa8ad1",
    "onboard-docket/elements/swimlane/fixtures/request-approval.html": "7c5a8c43d9f72ec77575a8e9f9f2a492547ce65710d627f0ed3e4d7def36ef7c",
    "onboard-docket/elements/swimlane/fixtures/three-owners.html": "511a4bbc735488fcec63c393afc9a9ea1d5e8a64ce52c66cb32e218f740f2492",
    "onboard-docket/elements/radar/description.md": "9ec2fd3cd900822a5e6230a67a5e962ec464aa55109002acb6f5564da6eeb551",
    "onboard-docket/elements/radar/element.css": "8c7550bfc0dbf1d2c8ebb5dfb1484a941bd05550f260aea19410c5406805389d",
    "onboard-docket/elements/radar/element.json": "0c61b88600adc8cf2e417d023dc924510b36db7e83681384647831f5ad83ea38",
    "onboard-docket/elements/radar/fixtures/profile-3.html": "c7712e322557fefad138a6a373047c0b4083e2e44dd2bc540f84dc24299efbd8",
    "onboard-docket/elements/radar/fixtures/profile-5.html": "d311d9810e864fd654b33ad4ba7f5f42ffa1b1c8167e4dff139834409b01c91d",
    "onboard-docket/elements/radar/fixtures/profile-8.html": "2853726e7de14990d5d54155c956303ea6c3f2dec3a3896b3ea24a1af9932b54",
    "onboard-docket/elements/slope/description.md": "6e5160787f93d7703b8a1f35cabea5f5a3c086c039b1fc62caf2e53c0085d585",
    "onboard-docket/elements/slope/element.css": "b156a3ec53791035f2cf64ef524830d7cf1822b2fdbb8fc9e85c08d534ef23f0",
    "onboard-docket/elements/slope/element.json": "324924568b2092c95fc9e9db3c7fea02e41cc189ca2896ac65496d6215c47a60",
    "onboard-docket/elements/slope/fixtures/delivery.html": "0e38fddec0bea4cf850943bdd582e40849433f5f159149bca331e37ea66a88ca",
    "onboard-docket/elements/slope/fixtures/service.html": "678084317d6461f92946ccdbb7a17e643820d24b961cd097096b55b2cdb93e4e"
  },
  "authorSHA256": "41c25c9cc9bc753c9610f2b958047b991b2c6b536ab071bfefb03f6368c32eec"
}
```


## 최종 관계 재검사 후 hub/cycle 보정

6멤버 최소6×6과4멤버 최소6×4를 포함한 모든 허용칸에서 radial 구조를 유지한다. cycle은 마지막→첫번째 구간까지 닫힌 타원과 각 구간 접선 화살표를 유지한다. hub는 중심의 실제 반지름과 각 멤버 경계를 사용해 독립 spoke를 끝까지 그리며 compact column으로 바꾸지 않는다. 얕은 칸에서는 보조 note만 감춘다. core 지름은 너비와 높이 중 안전한 범위에서 정하고 line mask의 core-cut도 동일 반지름으로 계산한다. min 양모드 native PNG와 전체 양모드 모든칸을 직접 열어 확인했다. 두 시트32칸의 clip·겹침·대비·영역·부품·폰트 실패 후보는0이다. 공유 kit/foundation/map과 다른7지원요소는 변경하지 않았다.

- hub: `d3f6088462ddf310314fbe3e1d623cc274fad6f374e731d09d9478c5ac638341`
- cycle: `9d2e7f13e9021ab2ae09f28d2365f48988590e3b02622240f0bad23c23a4111a`
