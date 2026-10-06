# group-c 개별 검수 기록

담당 소스는 `src/decks/group-c.ts`이다. 초기 배정은 15개 덱·37개 시트·295개 타일이며, 모든 원본 시트를 각각 열어 배치와 셀 경계를 확인했다. `public/reference/groups/c.json` 및 `review/group-c-crops.py`에 전체 native crop 경계가 있다. 원본 이미지는 UI 배경에 사용하지 않았다. 첨부 자료의 설명 문구는 디자인 참고 내용으로 취급했으며 사용자 작업 지시와 구분했다.

본 담당 구현은 p110 20쪽, p112 31쪽, p119 18쪽, p127 36쪽, p143 20쪽, p145 36쪽, 총 161개의 독립 1280×720 페이지이다. p151/p152/p160/p162/p165/p167/p174/p180/p194 134쪽은 별도 추가 담당으로 분리했으며 그 검수 기록은 `group-c-extra.md`와 `group-c-extra-pages.json`에 있다. 공통 모델·기본 도형·UI 컴포넌트와 덱별 재사용 factory 및 페이지 데이터를 사용했다. 서로 다른 원본 구성을 하나의 통일된 페이지 템플릿으로 대체하지 않았다.

## 실제 브라우저 비교

1차와 2차 모두 Chromium에서 161쪽 전부를 렌더한 뒤 원본 crop과 결과를 나란히 놓고 페이지별로 열어 확인했다. Contact sheet만으로 검수하지 않았다. 두 회차의 322개 페이지 PNG 모두 1280×720이다. `group-c-round2-individual.json`에 직접 열어 검토한 2차 161개 ID가 있으며, `group-c-pages.json`은 각 페이지의 원본 경계·render hash·개별 비교 여부·변경·판독 불가 문구·placeholder 영역·남은 차이를 기록한다.

1차 후에는 제목의 굵기/크기/폭/줄바꿈, 서로 다른 카드·사진 영역 배치, 줄 수와 본문 밀도, 표 머리글 및 수치, 차트 방향/시리즈, 색상 팔레트, 원형·물방울 단순 도형, 초과 영역을 수정했다. 2차 후 및 루트 통합 검수에서 지적된 최종 보정은 아래와 같다.

- p110: 본문 문단과 줄 수, 사진 둥근 모서리, 첫 카드 배경, Milestones 번호 색상과 네 줄 본문, 녹색 원형과 흰색 북서 화살표.
- p112: 원본별 세 줄/네 줄/두 문단 본문, phone placeholder 수직 배치, 사진 회전 방향, 표지 좌표, label 폭·글자 크기·회전, 누락 Lucide badges, 네 쌍 막대와 네 개 선 노드, 0..6/0..4.5 축·세로 격자, Reach 차트 높이, 지도 URL/BRAND 및 작은 아이콘, 사다리꼴/삼각형/어두운 윗면 funnel.
- p119: 모든 18쪽 카드 색상을 개별 row-major 팔레트로 지정, 원본에서 판독되는 Title Here/Your Title Here를 각각 전사, 두 줄 본문.
- p127: 제목/section 간격, outline logotype, guide grid/clearspace, palette 행·hex label, 대형 Aa/AaBb 실제 glyph 영역, 본문 문단과 너비·줄 수. 실제 Inter 문자 폭을 브라우저 Canvas로 측정해 명시적 줄바꿈을 작성했다.
- p143: 실제 Poppins 본문과 Playfair Display normal/italic, 표 머리글·행 폰트, 통계와 버튼 좌표, 두 문단 밀도, 강조 글자 색상, Years 및 작은 typography.
- p145: 실제 Roboto 본문, 부분 셀의 알려진 위치 유지, 사진/지도/device 회색 영역, 물방울 단계 도형, 단순 다중 arc/ring와 needle, 3시리즈 묶음막대·가로 누적막대·축 값·legend/카드 수치, pie sector, 원본별 아이콘·색상·GO/GREEN 굵기, 개별 구성 차이.

## 마지막 소스와 자동 검사

마지막 수정 후 실제 브라우저에서 다시 161쪽을 로드해 DOM·실제 glyph ink·폰트·chip 중심·페이지 크기를 자동 검사했다. unexpected findings는 0이다. 이 무촬영 자동 검사는 추가 full 비교 회차를 만들지 않으며 마지막 데이터 정의를 검증한다. `npm run typecheck`도 통과했다.

p127/s04-05(contents), p127/s05-09(primary3)의 원본에서 의도적으로 잘리는 대형 글자만 `allowClip`와 명시적인 이유가 있다. 나머지 영역에는 초과 경고를 숨기는 예외를 추가하지 않았다. 두 intentional source clips는 자동 기록에서도 구분한다.

2차 PNG는 마지막 통합 수정 이전 데이터이다. 최종 제출은 루트가 최신 소스로 production build 및 신규 캡처를 수행하고, definitionHash·PNG hash가 일치하는지 확인한 산출물이어야 한다. 마지막 변경 화면의 반영 여부를 루트 3차 통합 검수에서 확인한다. 이전 2차 캡처를 최종물로 대체하지 않는다.

## 원본과 남는 차이 및 판독 불가 부분

p127 원본의 Clash Display 파일은 확보하지 못했다. Fontshare API는 network permission 후에도 HTTP403을 반환했고 관련 npm 패키지에는 폰트 파일 없이 외부 CSS 참조만 있었다. 실제 로드된 Inter Variable을 명시적으로 사용했으며 글자 폭·굵기·자간을 조정했지만 glyph 형태 차이가 남는다. 다른 원본의 정확한 폰트명이 시트에 없으면 외형을 맞춘 실제 로드 폰트를 사용했고, Poppins/Manrope/Montserrat/Roboto/Playfair Display normal+italic 등 필요한 굵기가 실제 로드된다.

저해상도 시트의 작은 문장은 판독 가능한 조각을 유지하고 나머지는 보통 Lorem ipsum 또는 brand guideline 문장으로 작성했다. 선이나 가짜 glyph로 표현하지 않았다. 해당 페이지·실제 대체 문자열·좌표·폰트 크기는 `group-c-pages.json`에 기록했다. 일부 연락처/작은 legend/미세 차트 수치는 판독 불가라 정상적인 대체 값이다. 차트는 UI geometry 참고용이며 실제 분석 데이터라는 주장이 아니다.

사진·기기 화면·복잡한 3D 이미지·지도·graphic mockup 등은 원본 경계와 같은 연한 회색 단색 placeholder로 바뀐다. 원본 사진의 내용이나 blur를 재현하지 않는다. 복잡한 배경의 장식 세부, tiny chart legend wording 및 곡선 표본은 작은 원본의 한계로 차이가 남는다. 단순 표·차트·원형·다각형·화살표·텍스트·Lucide 아이콘은 실제 요소로 구현했다.

p145/s02-01..03 상단과 p145/s03-10..12·s04-10..12 하단은 시트에서 실제 타일 일부가 잘려 있다. 같은 시트의 완전한 타일 크기를 기준으로 native reference crop을 만들고 시트 밖은 흰 padding으로 보존했다. crop의 음수/범위초과 좌표와 visibleCrop, incomplete 메타데이터를 그대로 기록했다. 부족한 영역은 인접 덱 스타일에 맞춰 완성했고 추가된 일반 문장·차트 값은 복원 가정이다. 알려진 원본 위치를 바꾸거나 pixels를 늘려 채우지 않았다.

## 최종 3차 통합 보정과 source freeze

2026-10-06 16:38:13 UTC 담당 source SHA256: `37e853b13de62e2a67fe9686dcd7f47a953adc07ee644e2e71671496035afc7c`. 추가 전체 비교 회차 없이 루트가 확인한 8페이지를 보정했습니다. 실제 브라우저 161페이지 글자/폰트/chip/canvas 검사는 예상 밖 finding 0, 원본 의도 잘림 2이며 typecheck가 통과했습니다.

- p112/s02-02: DESIGN & VISUAL unreadable prose replaced by five explicit short lines; actual DOM five lines verified, font/box width retained.
- p112/s02-08: Funnel front and upper faces moved upward 40 design px, upper-face thickness matched source; 01 badge center corrected.
- p127/s04-08: Clearspace prose box narrowed from 419 to 300 design px to retain visible gap before square grid.
- p145/s02-04: Restored Month Data segmented horizontal chart and 0/25/50/75/100% axis, NATURE/PROJECTS/SAVE KPI captions and WEEK badge.
- p145/s02-06: Restored visible STEP01/07 simple shapes and dark numeric labels, sampled smooth curve, 31 x-axis numbers and two highlight circles.
- p145/s03-03: Restored area chart below left circular map placeholder and Jan–Dec labels.
- p145/s04-10: Restored corresponding dark-variant area chart below left circular map placeholder and Jan–Dec labels.
- p145/s04-03: Restored four small white dots and ordinary ECO/WATER/GREEN/AIR metric captions, lower-left prose, right 0–100% axis, bottom 31-node line chart and x-axis numbers.

p127/s05-05 COLORS, s07-07 LETTER, s07-08 BAG 누락 보고는 철회했습니다. 실제 final PNG 파일 픽셀과 독립 crop 확인에서 내용이 존재하므로 해당 페이지는 수정하지 않았습니다. 변경 8페이지의 현재 final marker는 재캡처 대기로 표시하며 최신 production 파일을 실제 개별 열람한 후 hash 증빙을 갱신합니다.

최신 production 보정 8쪽을 각각 실제 개별 열람한 뒤 직접 PNG/원본/comparison SHA256를 갱신했습니다. 수정 없는153쪽도 기존 실제 열람한 세 파일 hash와 동일함을 검증했습니다. 최종161/161 actualFinalIndividuallyViewed=true, 모든1280×720/loaded fonts, 예상밖 finding0, 원본 의도 잘림2.

## 같은 3차의 마지막 native PNG 기반 보정

2026-10-06 17:50:36 UTC source SHA256 `4ce6affdc552baf423593cbc5247bdde223a18ed332b7ab780b242b2a1e27bad`. 실제1280×720 PNG crop 및 원본을 직접 확인한6페이지의 누락/행밀도만 한 배치로 보정했습니다.

- p145/s02-01: Native/source verified: left prose now exactly2 actual lines; Jan–Dec bar and area axes restored; area chart moved down away from bar axis.
- p145/s03-07: Native/source verified absent elements: restored orange +3.2% badge, 1q–4q labels, seven actual body lines upper-right, small ordinary caption below central globe.
- p145/s04-12: Native/source verified: left prose exactly3 lines, moved up/narrowed away from donuts; right graphic map uses flat light-gray placeholder; +380000 badge and two-line prose restored.
- p145/s02-04: Native crop confirmed absent white-panel lower-right explanation; restored4 short ordinary lines.
- p145/s02-06: Native crop confirmed absent7 STEP connectors; restored thin vertical brackets beside alternating above/below prose.
- p145/s04-03: Native crop confirmed absent yellow91% card leaf and caption; restored Leaf Lucide and3 short lines; restored top-right 1 859 260 (57.85%) numeric statistic.

Typecheck 및161페이지 live auto 검사 통과: unexpected0, source-intended clip2. Actual Range lineRect 검증에서 forest2줄/network우상단7줄/air왼쪽3줄이 확인됐습니다. 최신 production을 실제 개별 열람하기 전6페이지 완료 flag는 pending이며155페이지 기존 actual-view SHA 증빙은 유지합니다.

마지막6쪽의 pair/native를 각각 실제 열람했습니다. s04-12 첫줄은 숫자 아래와 닿는 현상이 있어 본문만16px 아래로 이동(y194→214)했습니다. Live screenshot 실제 glyph 기준 제목끝160/본문시작173로 빈 여백12px, 본문끝226으로 도넛시작약257과도 분리됩니다. Range bounding box는 font descent 포함으로 실제 glyph보다 더 크며, 실제 픽셀/crop으로 확인했습니다. source freeze `853b050d200e4174c688ade6077b7142abafe91f6c6a0fde96fe0165292c3a3d`; 다른5쪽 final 완료,155동일픽셀 proof 유지, 최신production s04-12 하나만 pending.

최신 production 최종 본문 위치1쪽을 각각 실제 개별 열람한 뒤 직접 PNG/원본/comparison SHA256를 갱신했습니다. 수정 없는160쪽도 기존 실제 열람한 세 파일 hash와 동일함을 검증했습니다. 최종161/161 actualFinalIndividuallyViewed=true, 모든1280×720/loaded fonts, 예상밖 finding0, 원본 의도 잘림2.
