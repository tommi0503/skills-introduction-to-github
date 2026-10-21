# 독립 시각 검수 — EONU IR 12장 × 2종

- 검수일: 2026-10-21 (Asia/Seoul)
- 검수자: viewer 담당 서브 에이전트
- 검수 대상: `previews/design/01.png`~`12.png`, `previews/wireframe/01.png`~`12.png`
- 방법: 24개 PNG를 각각 직접 열어 원래 슬라이드 단위로 확인했다. 그리드 미리보기만으로 판정하지 않았다.
- 결과: 전달을 막는 잘림, 겹침, 누락 또는 오독 가능한 그래픽 오류를 발견하지 않았다.
- 검수 시작과 종료 시 24개 PNG의 SHA-256이 모두 일치했다.

## 페이지별 확인

| 장 | 확인한 구성 | 시안 | 와이어프레임 |
|---|---|---|---|
| 01 | EONU 소개, 의료진·환자·보호자 관계도, 핵심 문장 | 통과 | 통과 |
| 02 | 네 장면의 회색 이미지 영역, 연결 화살표, 사례 설명과 보조 보도 구분 | 통과 | 통과 |
| 03 | 세 사람의 필요, 공통 관계도와 우측 가치 카드 | 통과 | 통과 |
| 04 | 도입 가치 세 가지, 기존 채널과 걱정→정보→상담 흐름, 가설 표기 | 통과 | 통과 |
| 05 | 의료진→EONU 강조, 병원 설정 단계, QR 진입 방식 설명 | 통과 | 통과 |
| 06 | 네 단계 데모 UI, 달력·원문/요약·공유 설정·의료진 확인, 버튼 문구 | 통과 | 통과 |
| 07 | B2B→B2B2C와 별도 B2G, 유료 계약 검증 단계 | 통과 | 통과 |
| 08 | TAM/SAM/SOM 포함 관계, 기관·이용자·구매사업별 산정식 | 통과 | 통과 |
| 09 | 환자→EONU 강조, 초기 소프트웨어·연결 확장·추가 연구 구분 | 통과 | 통과 |
| 10 | 진행 상태 표, 자료 상태 배지, 다음 검증 지표 | 통과 | 통과 |
| 11 | 팀·자금 사용 항목·검증 결과의 세 카드, 미확정 입력값 | 통과 | 통과 |
| 12 | 마무리 문장, 관계도, 다음 단계와 연락처 입력 영역 | 통과 | 통과 |

## 집중 확인

- 6장: 네 화면의 마지막 동작 문구가 모두 읽힌다. 수정 후 하단 버튼의 글자가 잘리지 않고, 화면 영역과 아래 핵심 문장 영역이 분리되어 있다. 달력, 공유 토글, 작성자 구분은 단순 빈 이미지가 아니라 실제 UI 요소로 표현되어 있다.
- 11장: 대표 실행 역량, 필요한 협력, 고객 확보 경로가 왼쪽 카드 안에 들어온다. 중앙 사용계획 표와 오른쪽 기간·실증·유료 고객 입력값도 카드와 푸터 경계를 침범하지 않는다.
- 전체: 섹션 라벨, 큰 제목, 브랜드, 푸터의 기준 위치가 반복되어 페이지 간 일관성이 보인다. 사진 영역은 연한 단색 회색이며, 관계도·화살표·표·시장 포함 관계는 실제 도형이다.
- 시안은 연보라 포인트, 넓은 여백, 둥근 흰 카드로 일관된다. 와이어프레임은 중립 회색과 얇은 테두리, 흐름을 표시하는 제한적인 따뜻한 색의 연결선을 사용한다.
- 시장 규모·가격·배분·목표의 미확정 값은 빈 입력값으로 남아 있다. TAM/SAM/SOM은 금액비가 아니라 포함 관계라는 주석이 있고, 실증·계약 상태와 설명용 데모 표기도 보인다.

## 최종 도착 링크 확인

관리형 Chromium에서 뷰어의 실제 `href`를 읽고 localhost HTTP 요청을 수행했다.

| 링크 | 응답 | 확인 |
|---|---:|---|
| `docs/planning.html` | 200 | 47,357 bytes. 메뉴 클릭으로 새 탭이 열렸고 제목 `EONU · IR 기획 검토와 개선본` 확인 |
| `previews/eonu-design.pdf` | 200 | 1,851,190 bytes. `%PDF-` 파일 시그니처 확인 |
| `previews/eonu-wireframe.pdf` | 200 | 1,887,536 bytes. `%PDF-` 파일 시그니처 확인 |

PDF의 전체 페이지 렌더링·수량 검수는 부모 에이전트의 PDF 검수 범위이며, 여기서는 실제 메뉴 링크와 파일 응답을 독립 확인했다.

## 직접 열람한 최종 PNG 식별값

| 파일 | SHA-256 |
|---|---|
| `previews/design/01.png` | `703a3f4ecb8b9c853bfaaa8f0d007deff032ea0f83007c36de4255cdaba84153` |
| `previews/design/02.png` | `cfe81ddf52766f814db59e659ba0f07ece82b6a9c9358ff34f3201ad0841c159` |
| `previews/design/03.png` | `0409b1393d4d85254a7f379feacfed899f2fdad1ef04990d00454f4f080eed2f` |
| `previews/design/04.png` | `84829e1d708701b6a489884712af20493ac9306254476308c135d2d8e4406b10` |
| `previews/design/05.png` | `af1d150d92b15ea7fa8daf49828e583402c794e55d23641c87307084192c6b8b` |
| `previews/design/06.png` | `29c5148ded3a3243c74ffb0b1bf0a6d7d9e62e2de499c4beac438252db1957d6` |
| `previews/design/07.png` | `4942ca61a0a0c289ad0335b0eaa701ca72eec06d4696d373c32c118ddce2cb9a` |
| `previews/design/08.png` | `ed70464d48fa7f46c5883381ede064f508f0db89a21292500488c5822d6cd1bf` |
| `previews/design/09.png` | `ed4d9f61f63fcd2fcb73582210894fa70385314d5107efee78d19b8e9a29b266` |
| `previews/design/10.png` | `4bc26c4dba82320fd64607e61b559d4b9d3a82dd944cc90a92f6d023256423fb` |
| `previews/design/11.png` | `4a75d182b8afd30e3c79506fd067e90b50356ca87c102b82cbaa3c30e0710075` |
| `previews/design/12.png` | `555d6f993ab4576db2e737f5526a328bfea4f250be44d2ab5cdccd058810a6bc` |
| `previews/wireframe/01.png` | `d7a1c91f47ad62b7dba3657d90f21761785d5c9179d9bb57abea1ef128e742ee` |
| `previews/wireframe/02.png` | `e39e2039839697ec66d12db663581354553387f6dadb16bcd1ff560c4ae96e20` |
| `previews/wireframe/03.png` | `9891b57c2e62c0280bc5e7c154464310548aab2cdbf3fc76013b00b686c1f716` |
| `previews/wireframe/04.png` | `5c5d8230789a87fbf47fb5baaef366755bca47277fe77e715ce056204618e0a9` |
| `previews/wireframe/05.png` | `df928f645794c0fdc3a46b3cc0571b3c44ac6b9dc0a5190b7d1310a952595f60` |
| `previews/wireframe/06.png` | `e9ac47fb3ab7db5818154ad91ed681a6a17ea96a156cf1ab46cf1b1bcd96bede` |
| `previews/wireframe/07.png` | `e030cf8946fbe65a865321b1afb36fa89c5ea9c410ac6f02be891f9cd3907c89` |
| `previews/wireframe/08.png` | `e14989ac4517d4b8c737127adab5614893894f57a57b37f4b35805b814e445c6` |
| `previews/wireframe/09.png` | `44b03662cc41f376cc70d35da8b5160cd5f14ab59e545b893a1b49c87fc7dd5a` |
| `previews/wireframe/10.png` | `0c6b5d1df6d7215b3a3916c6eaa93af11c028664fda021089039aa0b33ac459d` |
| `previews/wireframe/11.png` | `478f51c23b7efe523532bb9617a7dbe92326668367602641e67c7ecb14d9e3b6` |
| `previews/wireframe/12.png` | `5e8f30c5c6d192b4917fbbef0f76c7cd3d61f989d962f311137731d88bccd933` |
