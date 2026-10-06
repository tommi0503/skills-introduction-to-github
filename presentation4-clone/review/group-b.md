# Group B 개별 검수 기록 — p16–p33, 23장

담당 소스: `src/decks/group-b.ts`. 원본 `public/reference/manifest.json`의 18개 덱과 23개 슬라이드 ID/순서를 유지했다. 1600×900 원본 좌표를 공통 `primitives.ts`로 1280×720에 균등 변환했다. 원본 이미지 전체를 구현 화면에 삽입하지 않았으며 `sourceAspect`, 텍스트 `scaleX`, 화면 회전을 사용하지 않았다. p32의 원래 세로 방향 캡션만 90도 회전했다.

## 방법과 자동 검사

- 원본 23장을 각각 `view_image`로 확인한 후 데이터를 작성했다. 연락처 시트로 검수를 대신하지 않았다.
- round1: 실제 Chromium 브라우저에서 23장을 캡처하고 원본/결과 비교 JPG 23장을 모두 각각 열어 확인했다. 공유 그룹 소스 작성 중이어서 이 첫 캡처에 한해 메모리 Vite load 플러그인으로 group-b만 로드했고 공유 파일을 수정하지 않았다.
- round1 자동 발견 13건: 본문 추가 줄바꿈 또는 텍스트 박스 높이 초과. 캔버스 크기, 폰트 로딩 실패, chip 중심, 이미지 전체 삽입 오류는 없었다.
- round2: 정식 `node scripts/render.mjs p16 … p33 --round=round2`로 캡처. 원본/결과 비교 JPG 23장을 각각 다시 열었다. 23장 모두 **자동 발견 0건**, 1280×720, 모든 사용 폰트 로딩 성공, placeholder 배경 RGB(229,229,229), embedded image 0.
- round2 후 마지막 국소 조정: 가로 누적 막대의 마지막 행이 원본 기준선에 닿도록 공통 행 간격을 조정했다(p19, p24/s11, p29/s11). p25의 대학 이름 영역은 chip이 아닌 좌측 배너 텍스트로 바꾸었다. p28 본문 Tinos를 31→33으로 높이고 줄간격을 1.24→1.165로 보정해 원본 너비와 줄 높이를 맞추었다. 이 마지막 조정은 주 에이전트의 최종 통합 third capture 및 검사에서 확인해야 한다. 추가 agent visual round는 하지 않았다.

## 텍스트 및 폰트 해석

이미지는 폰트 메타데이터를 포함하지 않아 정확한 상업용 원본 폰트 이름은 확인할 수 없다. 실제 로드한 폰트를 아래 표에 기록했다. 가변 폰트의 각 지정 굵기를 실제 지원하며 `font-synthesis:none`을 유지했다. 정적 Poppins/Jua/Noto Sans KR/Tinos는 공통 CSS의 실제 굵기 파일을 사용한다. 읽을 수 있는 모든 제목, 본문, 표, 축, 범례를 영문 그대로 전사했다. 담당 23장의 구현 대상 영역에는 판독 불가능해 임의로 만든 문구가 없다. 사진 속 작은 문서 문구와 로고 내부 문구는 사진/로고 전체가 회색 placeholder 대상이므로 제외했다. 도넛의 숫자와 그려진 호의 각도가 원본에서 정확히 대응하지 않는 경우 원본 숫자를 유지하고 원본 호의 시작/끝 각도를 재현했다.

## 개별 원본/결과 비교

아래 모든 행은 `comparisons/round1/{deck}-{slide}.jpg`와 `comparisons/round2/{deck}-{slide}.jpg`를 각각 실제 열어 확인했다.

| 슬라이드 | 실제 로드 폰트 | 발견 차이와 수정 | 남는 차이 / placeholder |
|---|---|---|---|
| p16/s09 | Jua 400, Inter 400 | 2019–2023 막대군 폭/군 간격/레이블 중심을 수정; 흑백 3계열/격자 재현 | 원본의 불규칙 손글씨 획은 Jua로 근사; 본문 줄바꿈 유지 |
| p17/s06 | Montserrat Variable 400, Inter 400 | 연간 수입 막대의 너비와 간격, 위 모서리 반경, 제목 박스 높이 수정 | 좌하/우상 복잡한 점 패턴은 회색; Montserrat 자형 미세 차이 |
| p18/s04 | Inter Variable 400/650/700/750 | 제목 박스 높이, 80%·95% 진행 막대, 회사 수익 3행 100% 누적 차트/범례 재현 | 사업 보고서 사진/로고/노이즈 배경 회색; 제목 자형/자간 미세 차이 |
| p19/s08 | Inter Variable 400/750, Poppins 400/700 | 초록 누적 막대 4행, 축, 범례, 두 항목 본문 재현; 마지막 누적 행 간격 국소 수정 | 로고/대각 그래픽 배경 회색; 그래픽 영역과 본문 일부 겹침은 원래 배경 배치에 따름 |
| p20/s07 | Inter Variable 400/800, Poppins 400 | 제목 상단과 자간, 상/하 교차 6개 타임라인 점/틱/본문 배치 재현 | 우상 복잡한 선 그래픽 회색; 원본 이중 원 테두리 일부 단순화 |
| p21/s09 | Montserrat Variable 700/800, Inter Variable 400/750/800, Noto Sans KR 400 | 90%·85% 원형 통계의 호 시작/끝 각도, 하단 4줄 줄바꿈/폰트/높이 수정 | 로고/원형 장식 배경 회색. 원본 본문 양쪽 정렬의 단어 간격은 가까운 명시 줄바꿈으로 근사 |
| p22/s09 | Poppins 700, Inter Variable 400 | 정량 데이터 2계열 막대, 3계열 누적 영역 차트, 좌표·축·범례/하단 설명, 제목 높이 재현 | 영역 차트 채움 및 원본 격자의 겹침 순서 미세 차이 |
| p22/s10 | Poppins 700, Noto Sans KR 400 | 월별 5열×3행 표의 모든 읽히는 문구/줄바꿈 전사; 셀 중앙 배치. 코너 동심 원호를 정확한 1/4원으로 수정 | 제목 폰트 자형, 원본 굵은 표 테두리의 미세 차이 |
| p22/s11 | Poppins 700, Inter Variable 400 | 단일 선 차트 10/20/23/35/36 값, 점/축, 분석 본문, U 모양 원호 재현 | Timmerman 로고 회색; 브랜드 자형 미세 차이 |
| p23/s12 | Poppins 400/600, Inter Variable 400 | Group A–D 두 계열 막대의 군 간격/막대 너비 수정; 제목 박스 높이 확대 | 본문/제목 폰트의 자형 미세 차이; 판독 불가 문구 없음 |
| p24/s10 | Inter Variable 400/550/600/650, Roboto Condensed Variable 400 | burgundy 제안 타임라인 표의 명시 줄바꿈/주차 문구 수정; 제목 위치/자간 보정; 월 chip 중심 검사 | Borcelle 로고 회색. 표 본문의 실제 원본 폰트 이름 불명; 제목 자형 미세 차이 |
| p24/s11 | Inter Variable 400/550/600, Roboto Condensed Variable 400 | 분석 제목 y/박스 높이/자간, 누적 막대·범례·축 재현; 마지막 행 기준선 조정 | 사업 보고서 사진/로고 회색; 본문 굵기/폭 미세 차이 |
| p25/s09 | Bodoni Moda Variable 400, Poppins 400, Inter Variable 400/750 | Result를 얇은 Bodoni Moda로 교체; 막대군 색/간격, 제목 높이 수정. 대학 이름을 좌측 배너 텍스트로 수정 | 원본 세리프 R·s 자형 미세 차이; 대학 이름 최종 통합 캡처 확인 필요 |
| p26/s09 | Inter Variable 400/650, Roboto Condensed Variable 400 | 흰색/분홍 막대, 제목 y/높이, 본문 폰트 수정. 작은 Lucide 표현을 원본 비율의 재사용 SVG 사람 도형 16개로 대체 | **원본 전체 추상 그래픽 배경을 회색으로 처리했으므로 흰 본문 대비가 낮아짐. 원본 텍스트 색은 유지했다.** 빛/반투명 효과를 평면색으로 근사 |
| p26/s12 | Inter Variable 400/650 | 흰색/분홍 선 차트, 원형 점, 86%·62%·70% 진행 막대·오른쪽 본문 폰트 재현 | **그래픽 배경 회색으로 인한 흰 텍스트 대비 감소**; 반투명 패널 평면색 처리 |
| p27/s12 | Inter Variable 400/600/700 | 두 선 차트/표식과 86%·62%·70% 막대/본문 복원, 제목 자간 보정 | 건축/그라데이션 배경 회색. 제목과 본문 실제 원본 폰트 이름 불명 |
| p28/s10 | Tinos 400, Inter Variable 400/650 | 본문 굵은 DM Serif Display를 보통 Tinos로 교체, 이후 너비 맞춤 33 크기/줄간격 보정. chevron·도트·프레임·3계열 선 차트 모두 벡터 구현 | 본문 세리프 자형 미세 차이; 본문 마지막 국소 변경은 통합 최종 캡처에서 확인 |
| p29/s05 | Poppins 400/600/700, Inter Variable 400 | 흰색 범례 복구, placeholder 배경 레이어를 텍스트 뒤로 이동, 제목 높이/군 간격 수정 | 두 코너 그래픽이 원본 크기/범위의 회색 polygon placeholder. 일부 축의 흰색은 연회색 위에서 대비 감소 |
| p29/s11 | Poppins 400/600/700, Inter Variable 400 | 누적 차트 4행, 제목 높이, 범례 흰색, 본문 크기·줄바꿈 수정. 마지막 누적 행 간격 보정 | 코너 그래픽 회색 polygon placeholder; 원본 폰트 폭 미세 차이 |
| p30/s08 | Inter Variable 700, DM Sans Variable 400 | 헤더 폰트를 Inter로 바꾸어 폭 보정, 45/35/20 세 반원 게이지와 본문/푸터 재현 | 오른쪽 복잡한 연결 그래픽은 회색 직사각 placeholder. 게이지 호 분할 미세 차이 |
| p31/s13 | Figtree Variable 400/750/800, Roboto Condensed Variable 700, Inter Variable 400 | 제목 자간/4줄 본문, 두 KPI 패널의 제목/본문 y, 몸체 폰트 폭/줄바꿈 수정. 숫자는 77%·34%, 호는 원본 각도로 재현 | 실제 원본 둥근 본문 폰트 불명, Figtree 근사. 원본 양쪽 정렬 단어 간격 잔차 |
| p32/s05 | Roboto Condensed Variable 400/700, Inter Variable 400 | 5개 20% pie sector를 SVG path로 구현; 제목 높이와 세로 캡션 폰트 폭 수정 | Original Current/market 및 05 자형의 미세 차이. 캡션만 원래 세로 방향 유지 |
| p33/s07 | Inter Variable 400/750, Poppins 400, Pretendard Variable 500 | 3계열 누적 막대, 시장 분석 제목 높이, 본문 원본 4줄 줄바꿈, nav/READ MORE chip 시각 중심 검사 | 원본 제목/본문 폰트 폭 미세 차이; 마지막 행/버튼 잘림 없음 |

## 구현 구조

`columns`, `stackedH`, `lines`, `grid`, `legend`, `arc`, `paintedRing`, `progress`, `person`, `pie`, `kpiPanel`, 월별 표 데이터, 브랜드 헤더를 작은 독립 함수/데이터로 분리했다. 공통 프레임을 직접 수정하지 않고 typed `Element` 데이터를 생성한다. 사진/복잡한 그래픽/로고는 공통 `I`를 통해 연회색 placeholder로 생성한다. 단순 도형·표·차트·인물 pictogram은 벡터/CSS 요소이며 원본 JPEG 파일을 참조하지 않는다.
