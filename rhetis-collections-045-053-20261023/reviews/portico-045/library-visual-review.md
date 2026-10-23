# Portico 045 라이브러리 전수 시각 검수

부모의 최종 native export 완료 통지 뒤 최신 요소별 시트를 검수한다. source/CSS는 freeze 유지. 각 fixture의 라이트/다크 1280×720 패널을 읽기 전용 scratch로 나란히 잘라 보았다. 자동 검사 0을 시각 판정 근거로 쓰지 않는다.

대상: foundation 포함 57개 leaf, 모드별176 fixture 패널, 총352 패널. 비교 scratch는 /workspace/work/visual-audit/045-library-panels 에 있다.

## 관찰 기록


## 실제 패널 판정 (수선 전 baseline)

공식 native export의57 leaf·176 fixture를 light/dark 각각 실제 열람했다. 아래 FAIL은 자동검사0과 관계없이 실제 기능/자료표현 오류로 판정했다. 수선 뒤 재판정은 별도 기록하며 이 baseline을 소급하여 pass로 바꾸지 않는다.

| leaf | 양모드 판정 | 실제 확인 |
|---|---|---|
| agenda | PASS | 3/5행의 표식·제목·보조문구 기준선과 강조행 대비 확인. |
| architecture | PASS | 2/4/5 계층 라벨 레일과 자식 chip 정렬 확인. |
| balance | FAIL | 빔과 지지대 없이 두 목록 면만 존재. --tilt 방향과 실제저울 의미 복구 필요. |
| bullet | FAIL | 목표 tick이 트랙과 분리되어 아래로 떨어짐. 4행 fixture는 이름·숫자·트랙이 중첩. |
| callout | PASS | 모범3 fixture 원형 마크업·하단배치 유지, 강조문장·아이콘 자리 대비 확인. |
| card | PASS | 8 fixture의 긴 note 및 .on/.line/.quiet/.tone 변형과 제목·숫자 기준선 확인. |
| chart-area | PASS | 4 fixture 연속영역, 교차2계열 및 누적3계열 실면적 확인. |
| chart-bar | FAIL | 8개 중 bars-h-5 긴 뉴스레터 라벨이 plot을 침범. 다른7개는 값/너비 정상. |
| chart-donut | PASS | 0·100·68 및 3/4개 그룹의 값·링 비율·중앙정렬 확인. |
| chart-line | PASS | 4 fixture의 모든 선 연속, 44→44 수평구간, 거짓 수평가지 없음 확인. |
| chart-scatter | FAIL | tone2/3 점이 지나치게 옅어 일부 실데이터 점을 사실상 식별할 수 없음. |
| chart-stack | FAIL | 여러 계열 seg 색이 동일하여 누적 구성비를 구분할 수 없음. |
| chart-waterfall | FAIL | waterfall-6의 누적연산은1241인데 마지막 total1284로 뛰어 연산과 그림 불일치. |
| code | FAIL | numbered9행이 모두1로 반복. 나머지 코드폰트/구문 구분은 정상. |
| concentric | PASS | 2/3/4 포함집합의 내부포함·명칭 가림 없음 확인. 계약은 동심원보다 포함관계 우선. |
| cycle | FAIL | 순환선은 있으나 node 면과 문구 위를 통과. 연결선을 면 뒤로 복구 필요. |
| decision-tree | FAIL | 질문/분기 결과가 목록으로만 표시되고 실제 세로 가지 연결이 없음. |
| delta | PASS | 이전→이후 방향과 숫자·단위 정렬 확인. |
| flowchart | FAIL | 일부방향의 선이 없고 화살촉도 누락. 4방향 연결의 실제기능 복구 필요. |
| foundation | PASS | 2 fixture 페이지 위계·모듈 장식·회색사진자리 및 양모드 대비 확인. |
| funnel | FAIL | min35% 너비때문에 --v34와24가 동일폭. --v의 실제데이터 너비 복구 필요. |
| gauge | PASS | 92/70/45/20/72 목표진행폭과 라벨·값 정렬 확인. |
| headline | PASS | 6 fixture 큰제목/중앙/강조/누적/기본의 줄바꿈·강조대비 확인. |
| heatmap | PASS | 12주 달력 및 2/5행의 셀 단계색·수치·축 라벨 확인. |
| hierarchy | FAIL | 수평 bus/세로 stem이 부모·자식과 이어지지 않고 텍스트 면 내부를 교차. |
| hub | PASS | 3/4/6 spoke 선이 면 뒤에 가려지고 텍스트 교차 없음 확인. |
| image-frame | PASS | 1/3 사진자리의 번호 중앙과 포티코 모듈 모서리 문법 확인. |
| journey | FAIL | 감정선이 stage마다 끊김. pain 유무에 따라 동일행 제목 시작높이 달라짐. |
| legend | FAIL | 5번째 기타 key가 4번째와 같은 보라색이라 계열을 구별하지 못함. |
| list | PASS | check/num/divided/plain4 fixture의 자동표식·숫자·텍스트 정렬 확인. |
| logo-group | PASS | 6/8 회색 로고자리 번호 중앙과 gutter 확인. |
| matrix | PASS | 일반2×2와 SWOT 모두 축/4셀 정렬 및 nested list 대비 확인. |
| matrix-nine | FAIL | axis의 자동배치 간섭으로9개 cell이 실제3×3이 아님. y축도 low가 위에 놓임. |
| metric | PASS | 1/3/4개 숫자 기준선·단위·긴 note 확인. |
| mindmap | FAIL | 방사선이 branch 면 내부와 문구를 가로지름. 면뒤·곡선관계 처리 필요. |
| network | PASS | 3/6 노드의 실제간선·강조관계와 면뒤 선 처리 확인. |
| person | PASS | 1/3/4명 사진자리·이름 기준선·목록 확인. |
| pill | PASS | 기본/강조/선/quiet 글자 시각중앙과 긴 이름 확인. |
| positioning | FAIL | y축 low/high가 양쪽상단에 가로로 놓임. low아래/high위의 세로축으로 복구 필요. |
| pricing | PASS | 2/3 plan 가격 기준선·추천자리·긴 목록의 역할 구분 확인. |
| prose | PASS | 5 fixture 문단/2단/lead/quiet의 실제줄바꿈과 본문 대비 확인. |
| pyramid | PASS | 3/4/5단계 너비 계층과 강조면 위 note 대비 확인. |
| quote | PASS | 3 fixture 인용본문·화자·이미지자리와 큰문장 위계 확인. |
| radar | FAIL | 계약K개 spoke 누락, 외곽ring clipping 및 2/3계열 식별용 명칭 누락. |
| roadmap | PASS | 2/4 lane 기간 bar와 milestone의 좌표·라벨 정렬 확인. |
| sankey | FAIL | 1단 flow는 유효하나 2단 branch를 밴드 대신 단순목록으로 표시. |
| slope | FAIL | dumbbell에 점·구간바가 없고 수평선·숫자만 존재. slope단계도 실제끝점 값과 시각좌표 정합 필요. |
| sparkline | FAIL | stat 내부 추세는 수평선 한 줄로 붕괴. standalone24점과8bar는 정상. |
| steps | PASS | 3/4/6 가로와 4 세로의 표식·제목·연결선 및 높이 정렬 확인. |
| swimlane | FAIL | 연결선이 짧은 stub에서 끝나 다음 node에 닿지 않으며 arrowhead 없음. |
| table | PASS | 3×3/5×4/7×6 실제행·열, 음수, pick 열과 숫자우측정렬 확인. |
| tag | PASS | inline highlight 및 chip의 글자 광학중앙·대비 확인. |
| timeline | FAIL | stop별 border가 gutter에서 끊겨 실제 track이 연속적이지 않음. |
| treemap | FAIL | tile min20%로46/31/15/8 실제면적이 약35/24/20/20으로 왜곡. share비례 복구 필요. |
| venn | FAIL | 3원 가로배치에는 세집합 공통영역이 없는데 core가 중간집합에만 놓임. |
| versus | PASS | 짧은/긴 양측 문장과 nested list, VS 중심정렬 확인. |
| waffle | PASS | 50/100/20칸 및 10인 pictogram의 실제계수와 46/32/22/42/9/20/60/30 표시 확인. |

기호가 점선 원으로 보이는 아이콘 자리는 공식 preview가 data-icon을 표시하는 방식이다. 회색 seat는 사진·복잡이미지의 허용 대체다. 본문에 남은 TEXT HERE 등은 비모범 fixture의 자료품질 잔여로 별도 정리한다.

## 수선 및 재판정

진행 중. 부모 담당: code/chart-stack/chart-scatter/chart-waterfall/radar/sankey. 그 밖의 위 FAIL은045담당이 수선한다. 최종 PNG 해시가 확정된 뒤 실제 재열람 근거와 JSON 판정을 기록한다.

## 검수한 원본 시트 파일의 메타데이터

| leaf | mode | native size | mtime UTC | SHA256 |
|---|---|---|---|---|
| agenda | light | 1280×1560 | 2026-10-23T10:11:20.924519+00:00 | 40b8fd3d146f6b8a064e5ed0d1a7aebc2eec95a09b34b7c9a1d170f7b3229ac6 |
| agenda | dark | 1280×1560 | 2026-10-23T10:12:21.063877+00:00 | 4fbd015bd6137c5960a1b88b90404fdbc9de6128851830efd969e561db41a753 |
| architecture | light | 1280×2320 | 2026-10-23T10:11:21.336515+00:00 | 4baf683dba10ca431d6a7978d6594a8dd6c2cce739a0080111b47ae9f5c54e09 |
| architecture | dark | 1280×2320 | 2026-10-23T10:12:21.539872+00:00 | 4f6c8756b8f40dfcf7a960a5f37b1a6ec9e42208e6db8f90f445f9ba95fab57c |
| balance | light | 1280×3840 | 2026-10-23T10:11:22.040508+00:00 | c95ee1d6326aaa56c08d59fa6e758ad37962e4cbd0d632e7fe5df686d2bd256f |
| balance | dark | 1280×3840 | 2026-10-23T10:12:22.311864+00:00 | 388942d09efda1e70895f988d821e1ea2b13e16f810ee1082e98882a7253cff8 |
| bullet | light | 1280×1560 | 2026-10-23T10:11:22.304505+00:00 | fe6af5206c119df05ee89c3217fb8362e841d4675864d76ca2b00ae4268f0b76 |
| bullet | dark | 1280×1560 | 2026-10-23T10:12:22.695860+00:00 | 37912ab0454f5fa8e99563ebcbc1316b6cc22b7f3cd3588449554fc78062ad83 |
| callout | light | 1280×2320 | 2026-10-23T10:11:22.712500+00:00 | 1cf5a7b592df4cb1e0833cfddea0bcb85e1d318843d9cdc1c4d72202603ca6af |
| callout | dark | 1280×2320 | 2026-10-23T10:12:23.215854+00:00 | 2528082ad4513bb3c53f2361724022cc8c0daa8464c1a9cfc412d84e82381734 |
| card | light | 1280×6120 | 2026-10-23T10:11:24.032486+00:00 | f7c42e9f4d2b7f55970fcffa623cf8e89b86ddd239d49348b1de33a2df96168a |
| card | dark | 1280×6120 | 2026-10-23T10:12:24.619839+00:00 | 23e8d5162ec7bdde77530c08a94bb31e1e37091f24e51ea8edd3165d2890971b |
| chart-area | light | 1280×3080 | 2026-10-23T10:11:24.616480+00:00 | 8d32e2c0bd91ed6f4aeb128d11b3e3b08d2bfb959dec60f4cf02be46e2007dd4 |
| chart-area | dark | 1280×3080 | 2026-10-23T10:12:25.803826+00:00 | 6af0a8987c4303b3a8689ffd568a754f6222b7b6eabf72fe20af250093f70562 |
| chart-bar | light | 1280×6120 | 2026-10-23T10:11:52.088188+00:00 | 95db52f1de6924b8675ef615915ea90a3ad5c505d480b5c3c0cd143040b3fb2a |
| chart-bar | dark | 1280×6120 | 2026-10-23T10:12:27.703806+00:00 | c93d64e24ec676c3861f4daf00827f62d30d835edea7bc99b8dfc902bba50be2 |
| chart-donut | light | 1280×3840 | 2026-10-23T10:11:53.904169+00:00 | 929b66971755baec1a210e8b17a720551ff3149c01fd7ab1a675df7fdcd8c866 |
| chart-donut | dark | 1280×3840 | 2026-10-23T10:12:28.695795+00:00 | 0ced37e85945a2c761d32d10168efe2db31cd69a4ac1e49c9959635a5f0ef287 |
| chart-line | light | 1280×3080 | 2026-10-23T10:11:54.956158+00:00 | f988a0fe621f5b40ede752e8fd84177e40c122d43d9c4f4f3fbcba936c392394 |
| chart-line | dark | 1280×3080 | 2026-10-23T10:12:29.323788+00:00 | 55a6348382a948550f9426685908ef8de6424493131a40ffefd913953f3c5250 |
| chart-scatter | light | 1280×2320 | 2026-10-23T10:11:55.568151+00:00 | f9887f20ecc8e285e613c8c986a7667b70efdbc9e04b339d2d2ce6660927deac |
| chart-scatter | dark | 1280×2320 | 2026-10-23T10:12:29.855783+00:00 | 954815f78c4d5f6c650695e09535754c7b6a10f682f761b33fecc394d8d5ccee |
| chart-stack | light | 1280×3080 | 2026-10-23T10:11:56.260144+00:00 | e211d6ff10a029d5c36a960924e645d5646453b517b1fbbea6ca19354273f7b1 |
| chart-stack | dark | 1280×3080 | 2026-10-23T10:12:30.823772+00:00 | 54e480ecdb0ded99f4e300f0137c293fc681ea9f0aa38d2d5f519aae1270963e |
| chart-waterfall | light | 1280×2320 | 2026-10-23T10:11:56.728139+00:00 | 07e051e71bd97854f8d4b9cd241c5d378b89905cd2b941f18e0c7e901cfc22ae |
| chart-waterfall | dark | 1280×2320 | 2026-10-23T10:12:31.291767+00:00 | 00bb9302c43b541d9f7f981a6127dbe649d7c85d5726c3e824592c2e829d3067 |
| code | light | 1280×2320 | 2026-10-23T10:11:57.309133+00:00 | 8887e03a04c48709d2a98326acf77daf1bdd371df0cdf5a6e4c880359bfe206e |
| code | dark | 1280×2320 | 2026-10-23T10:12:31.767762+00:00 | 95e3e76e9514ed6d552329f3f3265a0fe61091d4a5d5e087815b1cee8654f8c1 |
| concentric | light | 1280×2320 | 2026-10-23T10:11:57.860127+00:00 | b25c126ad2ffd5f0b8a26e64207997de6985bc58b4dd277cd2ec3216bd518bb1 |
| concentric | dark | 1280×2320 | 2026-10-23T10:12:32.359756+00:00 | 9dd4cd7e771bc1ea410a0cdb0e41d143161c31a88ad6962bc492e9a3bd18ad0d |
| cycle | light | 1280×2320 | 2026-10-23T10:11:58.476120+00:00 | 9f8ae9989f494fc4c19030f2fdada890d6a8c144931a4ccec1c75028c656ce3c |
| cycle | dark | 1280×2320 | 2026-10-23T10:12:32.863750+00:00 | bb3d63fb35890060de6c1fff96931f3ebafbb4956dea34cf1a30c0a1834bb8a2 |
| decision-tree | light | 1280×1560 | 2026-10-23T10:11:58.788117+00:00 | bb90b9c4a0c5c38184887ce187aa77e38614fa21c04b88d1da300abc8aac6a2f |
| decision-tree | dark | 1280×1560 | 2026-10-23T10:12:33.183747+00:00 | e0192fbbbc3e0fba4e3dec8ab424f7a7607de7346d9b459ea976d9e876f18e37 |
| delta | light | 1280×1560 | 2026-10-23T10:11:59.052114+00:00 | 4c57b87e2e7dbbede2c44bfc13aa9b7795bed6a52d2bd280ceb497d9332f3b04 |
| delta | dark | 1280×1560 | 2026-10-23T10:12:33.527743+00:00 | 9ff996e7dd93ec71c9824eca8fc76036b11821380a529c9a637ac1b4e8de97c0 |
| flowchart | light | 1280×1560 | 2026-10-23T10:11:59.416110+00:00 | e843e755b03819e78dbffa5b9da61487219f6f0bb5df8dc56f8247d55e0962ad |
| flowchart | dark | 1280×1560 | 2026-10-23T10:12:33.931739+00:00 | 19b462483523cc4e683f177ff8b31ff31ebb524858de3152af69fc52c8446ef5 |
| foundation | light | 1280×1560 | 2026-10-23T10:11:20.624523+00:00 | 2fcba8c76d99268ca012a7935fed8c37f049a2fb0ebb751a11bf234cc2732292 |
| foundation | dark | 1280×1560 | 2026-10-23T10:12:20.719881+00:00 | b627600684286f3a7e443f6dbaa342d37ed974e88e5b9dde012cdd8ebb756574 |
| funnel | light | 1280×2320 | 2026-10-23T10:11:59.864105+00:00 | d25c94a0abc54b91e830bfa314e02fda47c26875ef30ef194694836d8038aa10 |
| funnel | dark | 1280×2320 | 2026-10-23T10:12:34.439734+00:00 | 08a1bdb0ce6bd56da64afad66910d6f0a8cab3e2a2c12d913b1324f2f237ff0e |
| gauge | light | 1280×1560 | 2026-10-23T10:12:00.172102+00:00 | a8d1b2a2ccb09709a49122bf015d2db6b9dc2a4dc1f812a1476105f23828b7d9 |
| gauge | dark | 1280×1560 | 2026-10-23T10:12:34.891729+00:00 | 33cfabfb9292e7c38e7a94714781a640fd5ca295e31e8079709bdc5b69e3edfc |
| headline | light | 1280×4600 | 2026-10-23T10:12:01.168091+00:00 | 24e45cfb59172da11779c05af1cb890758f4170a9af5b02d3c907585432951e9 |
| headline | dark | 1280×4600 | 2026-10-23T10:12:35.935718+00:00 | 5cb157fed6490bf9fc26d7e566a5b979650cc78cd3cf7605584f346b1ab7b588 |
| heatmap | light | 1280×2320 | 2026-10-23T10:12:01.644086+00:00 | 8b32908f3eb91fa167a75161577b74568fc7d0f974697db63b3fed24338798c9 |
| heatmap | dark | 1280×2320 | 2026-10-23T10:12:36.575711+00:00 | a17c6df17bbb4cbc0019474b358a7fa5200de0c84a4ace0f4b6b6a3f808a42ab |
| hierarchy | light | 1280×2320 | 2026-10-23T10:12:02.076081+00:00 | 1415f5b1a61ced04252c29a53e6714df4a82d14ec7bf517ba5111e389f6be538 |
| hierarchy | dark | 1280×2320 | 2026-10-23T10:12:37.079705+00:00 | 7d184b1caa807476ae67e440cb67f980ec6e4959feecab19d6440626b9c8c13b |
| hub | light | 1280×2320 | 2026-10-23T10:12:02.576076+00:00 | 17d6d98c1cfacf353c28018aefe89b0ad36bbd9f8b1931a0c4ae364ee5749eef |
| hub | dark | 1280×2320 | 2026-10-23T10:12:37.911696+00:00 | 508292fb39f0e86cb1d5d76a1dfb40a61f63f6351cd7cff382289882b5fe0835 |
| image-frame | light | 1280×1560 | 2026-10-23T10:12:02.900072+00:00 | b1af4ecad653c48ba3793e76b2555d405742693219735e800397c57ee2c36b07 |
| image-frame | dark | 1280×1560 | 2026-10-23T10:12:38.731688+00:00 | c81b10958dd59e029679e0dcec838919be52336fb2c5585f10468aada3533de5 |
| journey | light | 1280×2320 | 2026-10-23T10:12:03.324068+00:00 | d3397d848cfa25ee66c98a34d84f2552e8594ba81338274b271b0c28d1871288 |
| journey | dark | 1280×2320 | 2026-10-23T10:12:39.603678+00:00 | 6df9466f274ce03c3b2af0172a882c75c67288891e921cec56a5d31f8fba297c |
| legend | light | 1280×1560 | 2026-10-23T10:12:03.660064+00:00 | 5ae22a3a10986b70bda6a1d36169b447b97129da4bdd5faabfbdc8c870125089 |
| legend | dark | 1280×1560 | 2026-10-23T10:12:40.311671+00:00 | 0fea1171461c56104cc6058d5bd1fc6f394cdf6e7cad02879046feb9abbe8b1c |
| list | light | 1280×3080 | 2026-10-23T10:12:04.288057+00:00 | 51e919941b9bef704c24f3e204aa1bfcc323e9371b0a6c03c6ea725eb72287c3 |
| list | dark | 1280×3080 | 2026-10-23T10:12:41.219661+00:00 | f7930d7d6304f64874f41b757c52f6c2ea0945a8586a596e74ea28dc8a8c2e71 |
| logo-group | light | 1280×1560 | 2026-10-23T10:12:04.660053+00:00 | 8959a99fc667495ac23490fcfef5028092d5599f5f0985c51ea1de9bb5887e8e |
| logo-group | dark | 1280×1560 | 2026-10-23T10:12:41.539657+00:00 | d4fd65d1da2f879eabc4c0a280c771a1fc236106616baa2250cc73d572c4ae80 |
| matrix | light | 1280×1560 | 2026-10-23T10:12:04.972050+00:00 | 22de245be71ec05a3f699675eca218ee0e24dac8bc3a89f18106fc7128010d81 |
| matrix | dark | 1280×1560 | 2026-10-23T10:12:42.131651+00:00 | fc0bde1af66918c515b35ae6c8d222ed97d8c8b42ce5351d13953f6140bf6305 |
| matrix-nine | light | 1280×1560 | 2026-10-23T10:12:05.300046+00:00 | 83f6cfc631e93556ee712e117e3fa6ae07ecb5cd17b2782fb25fb6df01c2ea25 |
| matrix-nine | dark | 1280×1560 | 2026-10-23T10:12:42.475647+00:00 | 2702cd6d5a02af9c623f601093e9a9ad99f897bc607e940db29cd0f0a1b12574 |
| metric | light | 1280×2320 | 2026-10-23T10:12:05.748041+00:00 | fab1f2841df7c76a9b1b9b1f72216297093a291925e9ac398921cdbea0f50566 |
| metric | dark | 1280×2320 | 2026-10-23T10:12:43.047641+00:00 | 052b85c19ebf6197ee407758183e31876c8c9e7a0925d9044026ec3ed2abeb36 |
| mindmap | light | 1280×2320 | 2026-10-23T10:12:06.192037+00:00 | 60ca301c535f2c23b22bce6d8d7af84249c880cbe96fafdbae77fd186cf9dd04 |
| mindmap | dark | 1280×2320 | 2026-10-23T10:12:43.575635+00:00 | ebfdd5b5b5bdc40072ce30cf6c288afff6972eed996a5e4afe003b07094130de |
| network | light | 1280×1560 | 2026-10-23T10:12:06.476034+00:00 | 6d36d5df3164691cae23803334dc84736e2a597289694856fa4d7530d9fd4f4b |
| network | dark | 1280×1560 | 2026-10-23T10:12:43.931632+00:00 | 68f763048904c28653aac5ed514ab70868e2cf548c3026324ba466359134706d |
| person | light | 1280×2320 | 2026-10-23T10:12:06.896029+00:00 | fa202e190c04ecc3054417b3dd1794fb0f17980757cf25b771d814fcdd0ad8ee |
| person | dark | 1280×2320 | 2026-10-23T10:12:44.387627+00:00 | f58705f9ce22a56d78307863c6ea058c8bee55cba1c799032db1c86e3dc00bb7 |
| pill | light | 1280×1560 | 2026-10-23T10:12:07.192026+00:00 | c11fd30ae2c1614a8a473ecf9ffeac5e3ad1737b4c3a960a9ad0b55724d6448d |
| pill | dark | 1280×1560 | 2026-10-23T10:12:44.747623+00:00 | 6e51e1f4488413c176f4220dadf69e247255122ef509386a73d217aaaae93099 |
| positioning | light | 1280×2320 | 2026-10-23T10:12:07.608021+00:00 | 268efebcb3c9d8d75bbdfee0fbf40cd8e3d3ecc5780bffe661c897148e18c238 |
| positioning | dark | 1280×2320 | 2026-10-23T10:12:45.211618+00:00 | 1f84115e751060737b6611cc71916acb4ba76b793db851bd36d1b3eb4c973c5e |
| pricing | light | 1280×1560 | 2026-10-23T10:12:07.896018+00:00 | 3d2467f9c37bb91103756faebc9a398223f5f319f94268c505e5e05fb59f6d54 |
| pricing | dark | 1280×1560 | 2026-10-23T10:12:45.579614+00:00 | 51567fa232c1b09620bbe1d2a7efd6b99070d5a7ddfb96dfcac42566c8526d36 |
| prose | light | 1280×3840 | 2026-10-23T10:12:08.720010+00:00 | c7847398c8f3069e9515cb7e7a4e6e130d569aebe3b5997edea3eb65fefb8c52 |
| prose | dark | 1280×3840 | 2026-10-23T10:12:46.415605+00:00 | 9863a89a4981161936bf3ca0284c2da9cfee741f50ff4d1457d48b7c8719a696 |
| pyramid | light | 1280×2320 | 2026-10-23T10:12:09.212004+00:00 | dbf19c6d294bcc0f6c54a2e5d535abfad507fd570c7269e721eee980a313e327 |
| pyramid | dark | 1280×2320 | 2026-10-23T10:12:46.923599+00:00 | ad36bb2b1d2968cd569c807b2257ea7a9e33bc59a69c90dd070e893cd0d4429a |
| quote | light | 1280×2320 | 2026-10-23T10:12:09.632000+00:00 | 83e5d5fa4a503f5cf300e965a355595fead685421daafcd61d6220a72946b529 |
| quote | dark | 1280×2320 | 2026-10-23T10:12:47.419594+00:00 | 24f523d75cb91b1b0f2030376234caee97bf89f16c41af40edf44414adc8f9a8 |
| radar | light | 1280×2320 | 2026-10-23T10:12:10.075995+00:00 | e8ef7dc757c7ddeeab85f077c1e6b826795c11363a0cd97e8fe06140aebb79f8 |
| radar | dark | 1280×2320 | 2026-10-23T10:12:47.975588+00:00 | cf707490359624fbca4b2e53e9436f72ddebbc550ff50a596530442563166538 |
| roadmap | light | 1280×1560 | 2026-10-23T10:12:10.339992+00:00 | d5c920149644c9d732218c87f095e00106d7c3f98601ac0f2683080bcbaed88c |
| roadmap | dark | 1280×1560 | 2026-10-23T10:12:48.263585+00:00 | 7742b2ff63e16a719cec302e7d1d58bd0145258078c2beac4dd623bb269031dc |
| sankey | light | 1280×2320 | 2026-10-23T10:12:10.807987+00:00 | c2011942a13b38ea606f942c211355cbb939e5419a9a399bb18faf9188184f1a |
| sankey | dark | 1280×2320 | 2026-10-23T10:12:48.763580+00:00 | 62dcb93dae6f6010402efa0325a0c0de227136f8e341fff77aea29afb2370337 |
| slope | light | 1280×2320 | 2026-10-23T10:12:11.247982+00:00 | f414afd02fd97186be4f845f009d1957033858e59435a5b320e8697cc5fe4e8e |
| slope | dark | 1280×2320 | 2026-10-23T10:12:49.267574+00:00 | 6e2b252cfe09fa964a1b1ca16be58660611422841e085d2db177408cf928614b |
| sparkline | light | 1280×2320 | 2026-10-23T10:12:11.659978+00:00 | 4d41445a2268eead1be42a7f262e38defd910cc6da812d636400927997ea1031 |
| sparkline | dark | 1280×2320 | 2026-10-23T10:12:49.775569+00:00 | 65316a0bd372dcbb42f2593aeca3572d28ccd7f8de7f24ae4294bf5423aa183d |
| steps | light | 1280×3080 | 2026-10-23T10:12:12.215972+00:00 | ba34af55a0bf88a72622626e076c60c51a54f996427c282db9aa78cdc88ecffd |
| steps | dark | 1280×3080 | 2026-10-23T10:12:50.463562+00:00 | 6fe9746c1f806c3418cb247623596add7f1004d09ba5c2e930e16a04e2a8f683 |
| swimlane | light | 1280×1560 | 2026-10-23T10:12:12.503969+00:00 | 7028ced58058000dd01352c74a217bc52cb8df02f41cac6d9003dbd98c3ee4c5 |
| swimlane | dark | 1280×1560 | 2026-10-23T10:12:50.871557+00:00 | 9e30f5c97ea970c8d229be6bf32e20b05640700a99ded11af195c94b650334d6 |
| table | light | 1280×2320 | 2026-10-23T10:12:12.927964+00:00 | b0aa96b2e07cc074cdf801a743ad66d3109836e64facf8fa51163bc3a911d4e8 |
| table | dark | 1280×2320 | 2026-10-23T10:12:54.419519+00:00 | b8b9e877a8b9b63144415022f646da4d90847d0c8d3ed3ad7d663d8895cbbec4 |
| tag | light | 1280×1560 | 2026-10-23T10:12:13.207961+00:00 | 866e0cef9080c9c8a97b1ad33da126c9aa110f4f55978aebef03600f2ae2dacd |
| tag | dark | 1280×1560 | 2026-10-23T10:12:54.735516+00:00 | 026c836c56557462d84e04221bbc5d0c378268336a0e68712a49cd2d94297ebc |
| timeline | light | 1280×2320 | 2026-10-23T10:12:13.647957+00:00 | b52507b27acbc92f96449607253767f9d4867299bb2ff577b85020d5b3c0fd1e |
| timeline | dark | 1280×2320 | 2026-10-23T10:12:55.387509+00:00 | 7f763b15e38a222e2d6e353ac83e9b274cc2ca97c2d2c7b467e25cfc0c48c9e8 |
| treemap | light | 1280×2320 | 2026-10-23T10:12:14.111952+00:00 | 54e871f72b853c9de94beae88b919e4ac7efd7841c340466164d1ffcbd0a48cc |
| treemap | dark | 1280×2320 | 2026-10-23T10:12:56.511497+00:00 | 47e69f55e1a124c07641482ebd6e1da3d3a6973a79aeab79df7e5ba9529ab3df |
| venn | light | 1280×1560 | 2026-10-23T10:12:14.411948+00:00 | 6ff315d7c31ce9db1a5893d33d55c3ec6752cd8e1fe14ecffb9daf8c8d5755c6 |
| venn | dark | 1280×1560 | 2026-10-23T10:12:57.531486+00:00 | 1a87b03173913c1cd842d9626dffdd354c7b2d937f09969e14119c6b1df12be3 |
| versus | light | 1280×1560 | 2026-10-23T10:12:14.687945+00:00 | 3bfda0b394b51b0a59c43f52ba8d2f926e4cbf97bda7c1196dad64363ab79417 |
| versus | dark | 1280×1560 | 2026-10-23T10:12:58.591474+00:00 | 12cdb20dd1c4de3b9c6e043731bc6d94b0ca6f1c5358f414332136c2a638961b |
| waffle | light | 1280×3080 | 2026-10-23T10:12:15.319939+00:00 | 9d1aafc94e5c3a7841b638bdeba3517fcb960700939f42b80985ea2c7e3b2bbd |
| waffle | dark | 1280×3080 | 2026-10-23T10:12:59.595464+00:00 | 0af8f5332f1eaa9cab33f415b8cec4c11bd6011c7d1f0c782aaa984c9d4bd4d0 |

## 최종 native 재판정

초기 FAIL25요소를 수선하고 변경된152패널을 라이트·다크 각각 다시 직접 열람했다. 정상31요소와foundation의 기존 열람 PNG는 SHA동일성을 확인했다. 재판정은 실제 관계·수치·배치 관찰 근거이며 자동0을 시각판정의 대체로 쓰지 않았다. 마지막 funnel의min-width35%와누적차트의series legend잔여까지수선했다.

| 요소 | 최종 | 실제 확인 |
|---|---|---|
| agenda | PASS | 3/5행의 표식·제목·보조문구 기준선과 강조행 대비 확인. |
| architecture | PASS | 2/4/5 계층 라벨 레일과 자식 chip 정렬 확인. |
| balance | PASS | 5fixture 양모드: beam과 삼각 fulcrum, 수평0/음수왼쪽하강/양수오른쪽하강, 1/4항목 및 verdict 실제 확인. |
| bullet | PASS | 단일/4행 양모드: 실제값86/98/62/92와 목표90/100/75/85 tick이 같은track에 위치. 3단정성band, note·이름·수치 중첩 없음. |
| callout | PASS | 모범3 fixture 원형 마크업·하단배치 유지, 강조문장·아이콘 자리 대비 확인. |
| card | PASS | 8 fixture의 긴 note 및 .on/.line/.quiet/.tone 변형과 제목·숫자 기준선 확인. |
| chart-area | PASS | 4 fixture 연속영역, 교차2계열 및 누적3계열 실면적 확인. |
| chart-bar | PASS | 8fixture 양모드: 2/3/6/12수직과5/8수평의 실제값·길이, .on/.tone 강조 확인. 긴 뉴스레터 라벨은 별도rail 안에서 plot침범 없음. |
| chart-donut | PASS | 0·100·68 및 3/4개 그룹의 값·링 비율·중앙정렬 확인. |
| chart-line | PASS | 4 fixture의 모든 선 연속, 44→44 수평구간, 거짓 수평가지 없음 확인. |
| chart-scatter | PASS | 3fixture 양모드: 점3/8 및5bubble 모두 식별, 좌표방향·bubble상대면적·강조점과 라벨 확인. 옅던tone점도 가시적인 중립색으로 복구. |
| chart-stack | PASS | 4fixture 양모드: 12/5누적·4수평·4백분율의 실제 segment값/길이와 구분색 확인. nested legend의 국내/해외 또는 제조/유통/서비스/기타 key색이각segment와정확히일치. axis와legend분리. |
| chart-waterfall | PASS | 3/6/10move 양모드: 증가·감소floatingbar와connector연속 확인. 1088+79+60+32−18=1241, 162−36=126, 240의증감후372 최종total 산술 확인. |
| code | PASS | 1/6/9행 양모드: Nanum Gothic Coding monospaced 간격, 들여쓰기, 구문별색과 실제행번호1~9연속 확인. |
| concentric | PASS | 2/3/4 포함집합의 내부포함·명칭 가림 없음 확인. 계약은 동심원보다 포함관계 우선. |
| cycle | PASS | 3/4/6node 양모드: 시계방향3/4/6화살촉 모두 실제표시, 연결선이 node/core면뒤에서가려져이름·note교차없음. |
| decision-tree | PASS | 1단3옵션/2단중첩 양모드: 질문stem→수평가지→각조건→결과의실제관계와추천강조 확인. |
| delta | PASS | 이전→이후 방향과 숫자·단위 정렬 확인. |
| flowchart | PASS | 가로6node/세로4node 양모드: right/down/left/up연결이각목적지경계까지닿으며arrowhead표시. 분기ask의오른쪽/아래동시연결 확인. |
| funnel | PASS | 3/5/6stage 양모드: --v100/80/62/46/34/24 너비가각각달라지고24가35로왜곡되지않음. 좁은stage의이름·숫자도겹침없음. |
| gauge | PASS | 92/70/45/20/72 목표진행폭과 라벨·값 정렬 확인. |
| headline | PASS | 6 fixture 큰제목/중앙/강조/누적/기본의 줄바꿈·강조대비 확인. |
| heatmap | PASS | 12주 달력 및 2/5행의 셀 단계색·수치·축 라벨 확인. |
| hierarchy | PASS | 2/3/4branch 양모드: root→상위bus→각본부→sidebus형제leaf연결. leaf끼리직속chain으로오독하지않도록sidebranch복구 확인. |
| hub | PASS | 3/4/6 spoke 선이 면 뒤에 가려지고 텍스트 교차 없음 확인. |
| image-frame | PASS | 1/3 사진자리의 번호 중앙과 포티코 모듈 모서리 문법 확인. |
| journey | PASS | 3/5/7stage 양모드: --mood/--next에따라낮아지고높아지는감정선이전체stage에연속, pain유무와관계없이제목·note시작높이동일. |
| legend | PASS | 3개긴label/5key 양모드: 다섯번째기타는중립역할로구별, 각marker와문구기준선정렬/다크가시성 확인. |
| list | PASS | check/num/divided/plain4 fixture의 자동표식·숫자·텍스트 정렬 확인. |
| logo-group | PASS | 6/8 회색 로고자리 번호 중앙과 gutter 확인. |
| matrix | PASS | 일반2×2와 SWOT 모두 축/4셀 정렬 및 nested list 대비 확인. |
| matrix-nine | PASS | 2fixture 양모드: 정확3×3셀과행순서, x low→high 및 y low아래/high위, .on과tone강조·note확인. |
| metric | PASS | 1/3/4개 숫자 기준선·단위·긴 note 확인. |
| mindmap | PASS | 2/4/6branch 양모드: 중심에서좌우branch로실제곡선연결. 선이면뒤에서가려져이름·leaf문구교차없음. |
| network | PASS | 3/6 노드의 실제간선·강조관계와 면뒤 선 처리 확인. |
| person | PASS | 1/3/4명 사진자리·이름 기준선·목록 확인. |
| pill | PASS | 기본/강조/선/quiet 글자 시각중앙과 긴 이름 확인. |
| positioning | PASS | 2/6name 및4logo 양모드: x/y점좌표와교차축, y low아래/high위세로labels, 강조mark/사진자리 가시성 확인. |
| pricing | PASS | 2/3 plan 가격 기준선·추천자리·긴 목록의 역할 구분 확인. |
| prose | PASS | 5 fixture 문단/2단/lead/quiet의 실제줄바꿈과 본문 대비 확인. |
| pyramid | PASS | 3/4/5단계 너비 계층과 강조면 위 note 대비 확인. |
| quote | PASS | 3 fixture 인용본문·화자·이미지자리와 큰문장 위계 확인. |
| radar | PASS | 3/5/8축 양모드: 정확K각외곽·격자·방사spoke 및1/2/3series실제polygon, 맨위첫축에서시계방향변수매칭, 범례색/series명확인. |
| roadmap | PASS | 2/4 lane 기간 bar와 milestone의 좌표·라벨 정렬 확인. |
| sankey | PASS | 3/6branch 및nested 양모드: 실제--v두께, source→첫split과국내/해외→두번째splitband연결 확인. 796=478+318,488=268+146+74 산술확인. |
| slope | PASS | 2/5slope와6dumbbell 양모드: 변화방향과값위치, hollow이전/filled이후점과각범위바확인. 40→35하강도반영. |
| sparkline | PASS | 24점/8bar/stat내12점 양모드: 단독추세와하강bar, stat안의상승·단기하강segment가실제로보이며평평한한줄로붕괴하지않음. |
| steps | PASS | 3/4/6 가로와 4 세로의 표식·제목·연결선 및 높이 정렬 확인. |
| swimlane | PASS | 2/3lane 양모드: 소유자rail과processnode, lane사이down/up 및동일lane right 실제화살표가목적지면경계까지연결됨. |
| table | PASS | 3×3/5×4/7×6 실제행·열, 음수, pick 열과 숫자우측정렬 확인. |
| tag | PASS | inline highlight 및 chip의 글자 광학중앙·대비 확인. |
| timeline | PASS | 5stop/6alt/4col 양모드: 가로·세로연속track, alt는동일track위·아래로교대, 날짜·이름·note·강조점읽기확인. |
| treemap | PASS | 1/4/5branch 양모드: branch폭과tile높이에--v를비례반영. 46/31/15/8실제면적이구별되며20%바닥폭없음. 모든이름·수치표시. |
| venn | PASS | 2/3집합 양모드: 실제겹침과3원공통영역, 반투명채움뒤원의경계/세이름모두보임, core가공통영역에위치. |
| versus | PASS | 짧은/긴 양측 문장과 nested list, VS 중심정렬 확인. |
| waffle | PASS | 50/100/20칸 및 10인 pictogram의 실제계수와 46/32/22/42/9/20/60/30 표시 확인. |

모든 최종 leaf PNG의 해시는 제출용 `library-visual-audit.json`에 기록했다. 처음 FAIL 표와 처음 열람 hash는 수선 전 baseline으로 보존한다.
