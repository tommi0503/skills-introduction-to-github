# cutplane 지정 5개 폴더 독립 최종 검수

검수 시각: 2026-10-23T10:59:57.253Z

판정: **통과**. 지정된 요소별 light/dark 시트 10장을 최신 갱신 후 각각 실제로 열어 확인했다. 대기 중이던 구버전 PNG와 최종 결과를 구분했다.

검수 범위는 foundation, chart-stack, funnel, journey, mindmap의 15개 fixture와 light/dark HTML 및 PNG다. 컬렉션 소스, 페이지 소스, 산출물은 수정하지 않았다. 이 보고서만 작성했다. 다른 요소, 원본 페이지 동일성, PDF 및 zip 검수는 이 보고서의 범위가 아니다.

## 자동·브라우저 확인

- 새 Chromium에서 최종 HTML을 1280×720 slide 크기로 렌더했다. Pretendard Variable 로드 정상.
- 15개 fixture의 최소·중간·12×6 중 중복 크기를 제거한 41가지/모드, 총 82가지에서 root의 slide 경계 이탈과 실제 텍스트 Range의 root 이탈·서로 겹침이 모두 0이었다.
- 저장된 native fixture PNG 30장을 새 브라우저 screenshot과 RGB 픽셀 단위로 비교했다. 30/30 동일, 최대 차이 0픽셀. 모두 1280×720.
- foundation seat root는 1104×576으로 body와 같고, 표시 면은 576×576 정사각형으로 중앙에 들어간다. 두 모드 모두 페이지 밖으로 넘지 않는다.
- 범례가 장식 위에 놓이는 구간은 실제 시트에서 확인했다. 일반 dark 삼각 면의 n-2 역할 반영 후 chart-stack의 국내/본사/제조 문구가 모두 읽힌다.

## 최종 화면 확인

| 폴더 | fixture 수 | light/dark 개별 확인 | 확인 내용 |
|---|---:|---|---|
| foundation | 2 | 통과 | 표지 제목·본문·하단 문구 대비, seat 정사각형 중앙 배치·크기 |
| chart-stack | 4 | 통과 | 12개월/5개년/가로/백분율 누적 막대, 범례, 13개 가로 segment 수치 표시 |
| funnel | 3 | 통과 | 3·5·6단계의 이름과 수치가 사다리꼴 면 안에 위치 |
| journey | 3 | 통과 | 단계별 이름·note·문제 문구, 점과 선 연결, 강조 칸 |
| mindmap | 3 | 통과 | 2·4·6 branch의 core 연결, 좌우 안쪽 경계, 이름·leaf 정렬 |

## 검수 중 발견한 문제와 최종 확인

1. 초기 dark 표지 글자가 어두운 면 위 어두운 색이었다. 최종 ink 역할 변경 후 제목·kicker·lead·meta가 읽힌다.
2. 중간 PNG는 mindmap 선과 가로 누적 막대의 일부 수치가 빠져 있었다. 이후 HTML과 PNG를 분리해 확인했고 최종본에서는 core↔branch가 연결되고 13개 수치가 모두 보인다. 가로 막대는 얇은 띠와 위·아래 수치 배치를 채택했다.
3. dark의 흰 삼각 장식이 흰 범례 글자를 가렸다. 일반 dark 면을 n-2로 조정한 최종 시트에서 해결됐다.
4. 기본 seat가 aspect-ratio 1 때문에 높이 1104px로 자라 페이지 아래로 넘쳤다. 최종본은 root를 grid 칸에 맞추고 내부 회색 정사각형 576px를 중앙에 놓아 해결했다.

시각 검수는 대비와 정렬을 실제 PNG에서 판단했다. 여기의 텍스트 경계 검사는 모든 가능한 문구·데이터의 적합성을 보증하는 검사가 아니며, 지정 fixture와 세 가지 크기에 대한 확인이다.

## 확인한 파일의 SHA256

| 파일 | 갱신 시각 UTC | 크기 | SHA256 |
|---|---|---|---|
| light.html | 2026-10-23T10:56:56.847Z | HTML | 6cd86f887d97dacca63e99ad9e42fc9e531097f9bcc3d0f93237f3662fc8be90 |
| dark.html | 2026-10-23T10:56:56.934Z | HTML | ab304a02ee3b31018ec48a9218d344e235b4eb38ea5310f47d6dc513fbd2c83e |
| foundation/light.png | 2026-10-23T10:57:37.301Z | 1280×384 | 5fa6a617bbb8320835a8c94705beaf650a1f6e3e0f8867800b6f0db7f5707814 |
| foundation/dark.png | 2026-10-23T10:57:44.745Z | 1280×384 | 6642486ff174772ff2595edae812eb35b7a95bba17ee08ff59128d92eb2d4e02 |
| chart-stack/light.png | 2026-10-23T10:57:36.685Z | 1280×768 | 962e7e8d249540bbe0b59de7d5b999c7bc818be5c90fda25160c6137ec2282c6 |
| chart-stack/dark.png | 2026-10-23T10:57:44.149Z | 1280×768 | 3fb0c966aaa458e6cb811ce6446b9d396060a5fd6f20a217d0b8d12dd723bf1a |
| funnel/light.png | 2026-10-23T10:57:37.393Z | 1280×768 | 83719289fe86772c3a068103d0770be768275771509455c57aaf47c1b0688798 |
| funnel/dark.png | 2026-10-23T10:57:44.837Z | 1280×768 | 9d09567536c1fb32064a1a93f1c02e637bbc6a1656eb0781c160f83feb4113ae |
| journey/light.png | 2026-10-23T10:57:38.181Z | 1280×768 | 5565cfc6dee658f1a2972f47f1185bc8b98aaa481fd31dbfa23007dfc8fe09ef |
| journey/dark.png | 2026-10-23T10:57:45.525Z | 1280×768 | 75d2c460529844226503c789f1d3fb020ed0df30e22eb69cd01844c673d3d421 |
| mindmap/light.png | 2026-10-23T10:57:38.725Z | 1280×768 | e7ec54161a5e784ef22ba7bc878b0e943a893c0472f078a35a8f364ea4b755bd |
| mindmap/dark.png | 2026-10-23T10:57:46.061Z | 1280×768 | f2e9ad4230b318807300331f1d134e9cc957af1e9936ee2a61dd69a4ab1436d1 |

요소별 합성 시트의 30개 타일을 native fixture PNG의 640×360 축소본과 다시 비교했다. 30/30 동일, 타일 차이 0건이다. 따라서 검수한 최신 native 렌더가 최종 폴더별 시트에도 반영되어 있다.
