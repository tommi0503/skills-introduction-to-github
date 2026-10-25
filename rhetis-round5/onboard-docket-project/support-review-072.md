# 078 inferred element support review (072 담당)

작성 범위는 `balance`, `chart-stack`, `decision-tree`, `mindmap`, `radar`, `sankey`, `slope`, `timeline`의 8폴더뿐이다. kit·foundation·map·replica·reassembled와 다른 요소는 수정하지 않았다. 별도의 페이지 조건, 형제 요소 조건, fixture 이름 조건, 새 클래스, 외부 geometry 입력은 없다. 8개 CSS는 이전 컬렉션 CSS를 읽거나 복제하지 않고 전부 새로 작성했다.

## 추론 근거

원본 replica04·06·09·10·15·16·17·18을 실제 PNG로 읽고, source-subpart-measurements의 부모 글자와 자식 큰 숫자 굵기까지 확인했다. 지원 8종은 직접 관찰된 base가 없으므로 map에 가짜 원본을 추가하지 않았다. 반복된 둥근 paper, 중성 면, 넓은 원, 가는 연결선, 채운 알약형 제목, 얇은 구획선을 현재 공유 kit에 맞춰 확장했다. 색은 팔레트 자리만 쓰고 type 단계와 공유 간격·굵기·자간·행간·radius를 따른다.

- balance: 실제 음/양 기울기를 검증했다. pan의 바닥을 동일 beam 좌표에 두고 atan2로 폭·높이에 맞는 회전을 계산한다. 음수에서 왼쪽이 낮아진다.
- chart-stack: 일반5개 막대/100%4개/가로3개/12개월×5계열을 검증했다. 누적 막대는 같은 아래 기준선에 붙고, 100% 막대는 실제 plot 전고를 채운다. 각 계열은 순위별 역할 색이며 수치는 실제 데이터다.
- decision-tree: 2·3갈래와 세 질문 깊이를 검증했다. 부모 간격과 자식 간격이 달라지는 최소 칸에서도 질문·조건·결과와 연결선이 닿도록 분기 간격을 상속한다.
- mindmap: 2·4·6가지와6가지×4leaf를 검증했다. core와 각 가지 제목에 anchor를 두어 전체 멤버의 곡선 연결을 직접 소유한다. 선이 캡슐 글자나 leaf를 가로지르지 않게 겹침 순서를 분리했다.
- radar: 3·5·8축,1·2·3계열을 검증했다. 실제 값/최댓값으로 polygon을 계산하고 축 수는 자기 axis 멤버 수에서 읽는다. 원은 타원이 되지 않고, spoke는 중심에 모인다. 범례는 원 아래 별도 영역이다.
- sankey: 3·6분기와2차 분기를 검증했다. source 높이는 실제 band 합과 같고, 가지 간 여백은 source 바깥에서 벌어진다. 64/24/12와35/22/18/12/8/5의 실제 share 두께를 유지한다. 5% 말단은 자기 높이로 글자 단계를 낮춘다.
- slope: 상승·하강·동일값을 검증했다. before는 윤곽 숫자, after는 채운 숫자이며 dumbbell의 같은 값도 위/아래에 나뉘어 겹치지 않는다.
- timeline: 가로4시점·교대5시점·세로3시점을 검증했다. 축과 marker는 같은 좌표를 쓰고, date·name·note를 모두 유지했다.

## 실물 검수와 수정

공용 native grid 시트에서 8종의 모든 크기를 light/dark로 직접 봤다. 최종 최소 칸의 deep tree,8축 radar,6분기 Sankey,6가지×4leaf mindmap,기울어진 balance,12개월 stack은 native cell PNG로도 확대 확인했다. 첫 검수의 상단 기준선 stack, core를 가로지르던 mindmap 선, Sankey 작은 share의 수치 넘침, timeline 축의12px 차이, 떠 있던 balance pan을 고친 뒤 영향 요소만 다시 그렸다. 최신 고정 rendererVersion을 사용했으며 stage 경로 분리는 시각 규칙을 바꾸지 않은 공용 도구 변경으로 기록한다.

| 요소 | fixture | light+dark 실렌더칸 | 6범주 후보 |
|---|---:|---:|---:|
|balance|3|24|0|
|chart-stack|4|34|0|
|decision-tree|3|26|0|
|mindmap|4|24|0|
|radar|3|26|0|
|sankey|3|22|0|
|slope|2|14|0|
|timeline|3|24|0|

합계 25 fixture / 194칸. 영역 밖·실제 clip·텍스트 겹침·실색 대비·하위 요소 초과·부품 초과 후보는 모두0이며 실제 폰트 선언/로딩 실패도0이다. partial 정적 감사 전체 errors0, 원문6자 중복0이다. partial warning은 담당 밖 미완성/아직 그리지 않은 시트이므로 이8개가 전체 컬렉션 반입을 통과했다고 주장하지 않는다.

8폴더 소스 묶음 SHA256: `ff7d00dba1e75b65c8443a2a0b1126a047f4c55ece001e3f21a4a0eab60d853a`

검사 시점: 2026-10-24T12:51:45.403774+00:00

```json
{
  "leaves": [
    {
      "leaf": "balance",
      "fixtures": 3,
      "cells": 24,
      "counts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "sheetFingerprint": "bd53aeb399c69e2f039c6f6b679b8a94d221d103a828adf92fc8f767bf69065b",
      "rendererVersion": "v2-grid-paint-font-parts-1",
      "rendererSHA256": "35e0e965f27cdf7e1dd6a49837428784eed42afda17054bfe1d06e73ba6e1021"
    },
    {
      "leaf": "chart-stack",
      "fixtures": 4,
      "cells": 34,
      "counts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "sheetFingerprint": "d08ad6c70a0d5adf0cb15a4c6f7c1570c3ba78556a209f48193327c245ff7d7a",
      "rendererVersion": "v2-grid-paint-font-parts-1",
      "rendererSHA256": "c8a3ae3ca77dcd724078a3c60a1565fe1ab5db9b3577972fb8cdb28c1faaa7ad"
    },
    {
      "leaf": "decision-tree",
      "fixtures": 3,
      "cells": 26,
      "counts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "sheetFingerprint": "d4d6e5410a4783f7726ba80954ec6585efe6becaf3173775555c6784bdcb68e4",
      "rendererVersion": "v2-grid-paint-font-parts-1",
      "rendererSHA256": "c8a3ae3ca77dcd724078a3c60a1565fe1ab5db9b3577972fb8cdb28c1faaa7ad"
    },
    {
      "leaf": "mindmap",
      "fixtures": 4,
      "cells": 24,
      "counts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "sheetFingerprint": "3fc60c3c421aafe474806e9badcc5774628f45ee6f2199534eda8bf58a275bf4",
      "rendererVersion": "v2-grid-paint-font-parts-1",
      "rendererSHA256": "c8a3ae3ca77dcd724078a3c60a1565fe1ab5db9b3577972fb8cdb28c1faaa7ad"
    },
    {
      "leaf": "radar",
      "fixtures": 3,
      "cells": 26,
      "counts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "sheetFingerprint": "0f9614402e391b882ba4cfd25df88424bf4f8213e846bde088a616bb8881d6a6",
      "rendererVersion": "v2-grid-paint-font-parts-1",
      "rendererSHA256": "c8a3ae3ca77dcd724078a3c60a1565fe1ab5db9b3577972fb8cdb28c1faaa7ad"
    },
    {
      "leaf": "sankey",
      "fixtures": 3,
      "cells": 22,
      "counts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "sheetFingerprint": "9640024cc358cc07828d40b725759e66f55329a86da78183b4a72f09233cdfde",
      "rendererVersion": "v2-grid-paint-font-parts-1",
      "rendererSHA256": "35e0e965f27cdf7e1dd6a49837428784eed42afda17054bfe1d06e73ba6e1021"
    },
    {
      "leaf": "slope",
      "fixtures": 2,
      "cells": 14,
      "counts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "sheetFingerprint": "798b97cff088b98024a4dfef3d77cb73d5ba2805bedd2fec190c73e70cb16971",
      "rendererVersion": "v2-grid-paint-font-parts-1",
      "rendererSHA256": "c8a3ae3ca77dcd724078a3c60a1565fe1ab5db9b3577972fb8cdb28c1faaa7ad"
    },
    {
      "leaf": "timeline",
      "fixtures": 3,
      "cells": 24,
      "counts": {
        "outside": 0,
        "clipped": 0,
        "overlaps": 0,
        "contrast": 0,
        "outsideComponent": 0,
        "outsideParts": 0
      },
      "sheetFingerprint": "ec6ef62c8fa029b94bddd868834fd597bd8c2635010e0a58ed9e6a48edee4eeb",
      "rendererVersion": "v2-grid-paint-font-parts-1",
      "rendererSHA256": "c8a3ae3ca77dcd724078a3c60a1565fe1ab5db9b3577972fb8cdb28c1faaa7ad"
    }
  ],
  "fontFailures": [],
  "sourceFiles": {
    "onboard-docket/elements/balance/description.md": "abef1dd7f7ef44f7b281d16e9949025dd2a5689dbdb1f050f5500187f8535b39",
    "onboard-docket/elements/balance/element.css": "222e64941dbd5b5b9455caf0e894af43b11a9d23ca41d6176d172061200bc705",
    "onboard-docket/elements/balance/element.json": "e783518b44fb4fa3721d162d2fceb77d118bd0648c033b07f6842c90859c842f",
    "onboard-docket/elements/balance/fixtures/equal.html": "42a2d51252a8abeb5e0360e66fb64d94dbf89a22583970191b5b3510c0b2be58",
    "onboard-docket/elements/balance/fixtures/quality-first.html": "180eb2b64c72a2e1ce8d84b3ad97c0afb050f7130023371ccf10125ed9ee85d3",
    "onboard-docket/elements/balance/fixtures/supply-first.html": "8a4e9a2bc20d27ffd377fd7e1087d3a55aab1f7ae5a474e36828560c4e783c75",
    "onboard-docket/elements/chart-stack/description.md": "ffce99ac5463f10c8acf93e02fc25f6346f60654353abf176de71e892e03cb6f",
    "onboard-docket/elements/chart-stack/element.css": "9ea24d8046725765957246c14f98fb1bcf2c7e5835caaa33edb2083b5d7dd801",
    "onboard-docket/elements/chart-stack/element.json": "75bb2be6098e99df748017660be99f1b3775b61636781b9142f1704ebaab8c71",
    "onboard-docket/elements/chart-stack/fixtures/allocation.html": "656e9607218f01561651aa32ae6faf47e4136bbee8226e6feba323263a25d5c8",
    "onboard-docket/elements/chart-stack/fixtures/departments.html": "8aeb792b6ead856b47bb2f3ae20d032c7fcb9930afc4432b29fba584646abf87",
    "onboard-docket/elements/chart-stack/fixtures/monthly-twelve.html": "1a020f3e2bcb9766a24c5827e391579c74cb979ea5fd7ec956c5738e082e1112",
    "onboard-docket/elements/chart-stack/fixtures/orders.html": "3babe013b08a65b787b6270fca7859181d618bb8a64f52c43724e67b0967291e",
    "onboard-docket/elements/decision-tree/description.md": "9bf0a50ee861699aed99d381daf7a2ce208b5458996fe4eb0f8d0d7c84c34ee0",
    "onboard-docket/elements/decision-tree/element.css": "78eecc1e7a2ffd2b0f993866c9b2bb0f0986f231cb8dd439142da9546ea5e581",
    "onboard-docket/elements/decision-tree/element.json": "036946931b1d61ac0a77d90115d7ac3d8d7841c738d964501be547a646ebdc74",
    "onboard-docket/elements/decision-tree/fixtures/routing-deep.html": "912a3953480556cbbc0ed2a9cd463a459221f1016a58bf1cf251c04f65ccdce1",
    "onboard-docket/elements/decision-tree/fixtures/routing.html": "7b9bf2bd63af7aee708dc2089d58ba18a4a8e89b385f1f69755b5e7335a59b4b",
    "onboard-docket/elements/decision-tree/fixtures/three-routes.html": "fd2a4e66ad8c7f27f5c22c9f014b111e42592be416b50fd934e0629aae19693d",
    "onboard-docket/elements/mindmap/description.md": "48e2418a8759ace26f1828be72e173376649c8715b0c32f12440357b9df4f047",
    "onboard-docket/elements/mindmap/element.css": "66b101da55e9411f674514ab14ab714a6a4c55b9ab891dce93e3a681b5fd85aa",
    "onboard-docket/elements/mindmap/element.json": "33fe7fbc0fd5e31e8a3e43e0f428dcfc2df54e046ea63f4fcfeeaabf119f246c",
    "onboard-docket/elements/mindmap/fixtures/teams-2.html": "a304ff28aad49b40fbf1d105ca75fef4d2ad95e983ad756781d171046d94a14b",
    "onboard-docket/elements/mindmap/fixtures/teams-4.html": "58ba40268d6a8258f84a7fe33ada242f0393749b16e41560412ce83b7a3ba422",
    "onboard-docket/elements/mindmap/fixtures/teams-6.html": "074c00f2fb77629fb76dc6a523477b8da60e1ba998f877e5ebb7ffa40e6363ea",
    "onboard-docket/elements/mindmap/fixtures/teams-six-detailed.html": "07d00e3e52e2624a2510c52186a7278aad04f696a0a42b3f1779a7bbb93f8dc5",
    "onboard-docket/elements/radar/description.md": "9ec2fd3cd900822a5e6230a67a5e962ec464aa55109002acb6f5564da6eeb551",
    "onboard-docket/elements/radar/element.css": "cbc10289a50094a1232344774c186d0659034f50b1d92ff16459cbe8f3a019e0",
    "onboard-docket/elements/radar/element.json": "0c61b88600adc8cf2e417d023dc924510b36db7e83681384647831f5ad83ea38",
    "onboard-docket/elements/radar/fixtures/profile-3.html": "c7712e322557fefad138a6a373047c0b4083e2e44dd2bc540f84dc24299efbd8",
    "onboard-docket/elements/radar/fixtures/profile-5.html": "d311d9810e864fd654b33ad4ba7f5f42ffa1b1c8167e4dff139834409b01c91d",
    "onboard-docket/elements/radar/fixtures/profile-8.html": "2853726e7de14990d5d54155c956303ea6c3f2dec3a3896b3ea24a1af9932b54",
    "onboard-docket/elements/sankey/description.md": "16e923ec7197a0d6aae40527329586e9d8532b0f229e49383a8a9e4a609b9d43",
    "onboard-docket/elements/sankey/element.css": "16245514be4bd95560375ae44e7447d678c595a55db55fdd4be999a5700d7f3a",
    "onboard-docket/elements/sankey/element.json": "4facf4405e448a925c0a096e185b8b5306829dc2f23cd3d66021403159969337",
    "onboard-docket/elements/sankey/fixtures/nested.html": "1f7689e3b06aaf2feba97b48d4f80a9c97237ee79abc10009d0373616224f584",
    "onboard-docket/elements/sankey/fixtures/orders.html": "24b2cb0dde2bac34b68759dc4be2604d1f42fd31d2aa40b2a5e6be662da602eb",
    "onboard-docket/elements/sankey/fixtures/requests.html": "3ab43b4e995955a395451f643f365865f3dca1ffbac777a406ff5c5b4dab984c",
    "onboard-docket/elements/slope/description.md": "6e5160787f93d7703b8a1f35cabea5f5a3c086c039b1fc62caf2e53c0085d585",
    "onboard-docket/elements/slope/element.css": "124078475f34d699e392084a9672f162d977a499d57059b8cd17a0dac882e49c",
    "onboard-docket/elements/slope/element.json": "324924568b2092c95fc9e9db3c7fea02e41cc189ca2896ac65496d6215c47a60",
    "onboard-docket/elements/slope/fixtures/delivery.html": "0e38fddec0bea4cf850943bdd582e40849433f5f159149bca331e37ea66a88ca",
    "onboard-docket/elements/slope/fixtures/service.html": "678084317d6461f92946ccdbb7a17e643820d24b961cd097096b55b2cdb93e4e",
    "onboard-docket/elements/timeline/description.md": "7e4047bfae06aa37d97c8f58faa509abecb5cc36bc2cdd68ba4ca3b487f9f991",
    "onboard-docket/elements/timeline/element.css": "fd8babdfb5e84f0fb0442a39cab00455d252cbc1513097748e548c613395cbeb",
    "onboard-docket/elements/timeline/element.json": "0675335f717699c29cee235b3586bf2c524a718b48372500aaff15db5b5c413e",
    "onboard-docket/elements/timeline/fixtures/launch.html": "5feb7e23b353f4fc2623081c1761433be5b22663f1d5c00c4cfe89d35d548d3c",
    "onboard-docket/elements/timeline/fixtures/month.html": "60ad32c0f100c8764d725d399b4d28bcd1d4f992019f8fa7d7d6e7ab492e7924",
    "onboard-docket/elements/timeline/fixtures/review.html": "ed9c0e2e5bdf981329ab734ff9b08195394353925fcf67f552054f9270ec4934"
  }
}
```
