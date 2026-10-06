import json
from pathlib import Path
p=Path('review')
assignment=json.loads((p/'assignment-c.json').read_text())
observations={
'd38-s010':'주황 단색 배경, 왼쪽 흰색 2줄 대제목과 3줄 부제, 오른쪽 3개 곡선 그래픽, 하단 웹사이트.',
'd39-s001':'상단 초대형 CORPORATE와 중앙 짧은 선, 가운데 긴 둥근 사진, 하단 발표자와 작은 2줄 문단; 사진으로 된 전체 배경.',
'd40-s004':'크림색 격자 배경, 큰 둥근 사진 프레임 위 왼쪽 흰색 Budgeting Basics, 크림 칩과 5줄 문단.',
'd40-s006':'상단 넓은 둥근 사진과 하단 좌측 Investing 101, 우측 칩과 5줄 문단, 격자 장식.',
'd40-s008':'좌측 큰 사진, 우측 Protecting Your Wealth 2줄 제목과 칩 및 6줄 문단, 전체 둥근 프레임.',
'd40-s009':'우측 저금통 사진, 좌측 겹친 둥근 큰 제목 상자와 작은 휴식 안내 상자, 격자 장식.',
'd40-s010':'우측 계산기 사진, 좌측 겹친 둥근 Thank You 상자와 Finance = Freedom 안내 상자.',
'd41-s001':'오래된 종이 배경과 빈티지 소품, 중앙 굵은 세리프 HISTORY PROJECT 2줄, 다이아몬드 선 장식과 저자.',
'd42-s007':'흰 배경과 좌측 세로 테두리, 도시 파노라마, Methodology와 긴 본문, 우측 동일한 2개 이탤릭 본문 카드.',
'd43-s001':'크림색 배경의 Psychology Project 세리프 제목, 작은 대학 로고, 밑줄과 손글씨 본문, 우측 복잡한 뇌 일러스트.',
'd43-s003':'좌측 Introduction/Problem Statement 및 8줄 본문, 오른쪽 곡선으로 잘린 상담 사진.',
'd43-s007':'좌측 작은 뇌 일러스트와 Research Questions, 손글씨 본문; 우측 위 큰 사분원 상담 사진.',
'd43-s008':'상단 좌측 둥근 가로 사진, Applied Methodology, 넓은 줄간격의 6줄 본문; 오른쪽 큰 뇌 일러스트.',
'd44-s008':'좌측 계단 사진 위 흰색 Hypotheses 카드, 오른쪽 파란 Significance of the Study와 짧은 선 및 문단.',
'd45-s001':'흰 바탕의 빨간 흐림 그래픽, 왼쪽 대학 로고와 Thesis Defense 2줄 제목, 저자 및 학번.',
'd46-s004':'크림 배경의 검은 2줄 제목, 우측 세로 사진과 라임 막대, 하단 좌측 6줄 본문 및 페이지 번호.',
'd46-s008':'상단 왼쪽 Growth Pathways와 우측 긴 문단, 하단 넓은 건물 사진과 라임 세로 막대.',
'd46-s010':'전체 건물 사진 배경, 좌측 작은 회사명과 라임 막대, 우측 초대형 THANK YOU, 하단 날짜와 연도.',
'd47-s002':'빨강 배경의 압축 산세리프 질문 제목, 좌측/중앙 짧은 흰 본문, 우측 사진, 왼쪽 연결 원 4개.',
'd47-s006':'빨강 배경의 상단 좌우 설명과 중앙 사진, 하단 TARGET AUDIENCE와 양쪽 연결 원.',
'd47-s007':'빨강 배경의 상단 왼쪽 설명과 오른쪽 사진, 중앙 Brand Positioning 2줄 제목, 하단 교차 도형.',
'd47-s009':'왼쪽 Brand Voice & Messaging 3줄 제목, 중앙 설명, 오른쪽 연결 원과 아래 사진.',
'd47-s010':'중앙 Visual Identity 2줄 제목, 왼쪽 큰 사진, 오른쪽 본문과 작은 사진, 두 교차 도형.',
'd47-s011':'왼쪽 상단 본문 및 작은 사진, 중앙 Brand Experience, 오른쪽 큰 사진과 꽃 모양 도형.',
'd47-s012':'왼쪽 Measuring Brand Success 3줄, 오른쪽 위/아래 본문, 중앙 작은 사진과 양쪽 연결 원.',
'd48-s003':'흰 배경, 왼쪽 상단 테이프가 붙은 둥근 사진, 큰 02., Investment/노란 Planning, 두 본문 영역.',
'd48-s004':'Risk Management 세리프 제목과 노란 강조, 하단 왼쪽 사진/테이프, 중앙 본문과 큰 03.',
'd49-s003':'얇은 상하 구분선과 작은 머리말/꼬리말, 왼쪽 Introduction과 작은 본문, 오른쪽 사진 3개.',
'd49-s005':'얇은 상하 구분선과 작은 머리말/꼬리말, 왼쪽 Brand Value와 작은 본문, 오른쪽 사진 3개.',
'd49-s006':'왼쪽 Target Audience 2줄 세리프 제목 및 본문, 오른쪽 62.5/25/12.5% 회색 원형 차트.',
'd49-s007':'상단 긴 사진, 중앙 Brand Voice & Tone 2줄 제목, 하단 작은 3줄 본문, 얇은 머리말/꼬리말.',
'd49-s008':'중앙 Visual Direction 제목, 왼쪽 2개 작은 문단, 오른쪽 큰 사진, 얇은 머리말/꼬리말.',
'd49-s010':'왼쪽 Timeline 제목과 세로 사진, 오른쪽 6개 일정 행과 구분선 및 날짜.',
'd49-s011':'중앙 Case Studies 제목, 왼쪽 작은 본문과 오른쪽 세로 사진, 얇은 머리말/꼬리말.',
'd50-s001':'짙은 초록 배경과 사분원 장식, 왼쪽 The Creative Process 흰색/라임 제목 및 작은 문단, 오른쪽 큰 그림과 별.',
'd50-s006':'Time Allocation 제목, 30/20/40/10% 둥근 카드 4개가 계단 형태로 배치, 길쭉한 그림 사진 2개.',
'd50-s008':'왼쪽 Building Depth와 작은 문단, 중앙 세로 그림 사진, 오른쪽 작은 그림과 4개 라임 점 목록.',
'd50-s009':'상단 Color Impact, 왼쪽 따뜻한 그림 사진과 3행 색상 영향 표, 오른쪽 큰 시원한 그림 사진.',
'd50-s010':'사분면 구성: 왼쪽 위 Knowing When To Stop, 오른쪽 위 그림, 왼쪽 아래 팔레트, 오른쪽 아래 6줄 문단.',
'd50-s011':'왼쪽 라임 배경띠와 둥근 꽃 그림 및 큰 8갈래 도형, 오른쪽 Art Meets The Audience와 작은 본문.',
'd51-s001':'보라색 배경과 겹친 빈티지 TV 사진, 중앙 분홍색 Brand Strategy 2줄을 약간 회전, 상단 노란 로고.',
'd51-s006':'보라색 배경, 왼쪽 분홍 Creating a Distinct Market Presence 4줄과 하단 본문, 오른쪽 큰 노트 사진.',
'd52-s002':'짙은 남색, 왼쪽 What is Banking와 주황 칩, 오른쪽 사진과 겹친 데이터 카드, 작은 설명/목록 및 로고.',
'd52-s005':'상단 좌측 패널과 우측 현금 사진, 아래 오른쪽 How Banks Make Money와 주황 칩, 왼쪽 3개 설명 영역.',
'd52-s006':'중앙 Role in the Economy 제목과 주황 칩, 양쪽 사진, 중앙 작은 설명 패널 및 하단 로고.',
'd52-s009':'상단 왼쪽 로고/세로 패널, 하단 큰 현금 사진, 오른쪽 Financial Literacy & Banking와 칩 및 2개 목록.',
'd52-s010':'상단 왼쪽 로고와 Thank You, 주황 칩, 오른쪽 큰 사진, 하단 좌측 감사 패널과 우측 연락처.',
'd53-s002':'노란 배경과 빨강 작은 스튜디오 머리말, 중앙 대문자 설명, 하단 Target Audience와 매우 큰 Identify, 우상단 흰 물결.',
'd53-s005':'노란 배경, 왼쪽 흰색 기둥 2개 안 중앙 문단, 오른쪽 Develop/Brand Positioning 및 흰 물결 장식.',
'd53-s007':'빨강 배경, 오른쪽 위 노란 둥근 패널 안 설명, 왼쪽 흰 물결, 하단 Design/Visual Identity 흰 제목.',
'd53-s010':'빨강 배경, 상단 오른쪽 Social Media, 중앙 매우 큰 Leverage, 하단 왼쪽 3줄 설명과 오른쪽 노란 물결.',
'd53-s011':'노란 배경, 상단 초대형 Implement, 왼쪽 흰 리본, 오른쪽 설명, 하단 Brand Guidelines.',
'd53-s014':'노란 배경, 상단 Innovate와 Continuously, 왼쪽 아래 흰 리본, 오른쪽 아래 4줄 설명.'}
fixes={
'd38':['Poppins 실제 300/400 굵기를 로드하고 제목 크기와 y 위치, 부제 y 위치를 조정.'],
'd39':['CORPORATE를 League Spartan 800으로 변경하고 크기·자간·가로 비율을 조정.'],
'd40':['제목을 League Spartan 700, 문단/칩을 실제 Barlow 300/500으로 변경.','마무리 2장 제목 중앙 정렬과 두 카드 모서리 반경 수정.'],
'd41':['과도한 장식이 있던 Cinzel Decorative를 Bodoni Moda 900으로 교체하고 제목 폭/높이를 조정.'],
'd42':['Methodology 제목과 Barlow 본문/카드 좌표를 조정.'],
'd43':['제목 Forum 크기와 손글씨 Comic Neue 실제 글꼴 크기·줄간격을 조정.'],
'd44':['Significance 제목 y 위치와 실제 Barlow 문단 크기·줄바꿈을 조정.'],
'd45':['Thesis Defense를 DM Sans 600 136px로 조정하고 대학 로고를 Lucide로 구현.'],
'd46':['본문의 실제 DM Sans 크기와 명시적 줄바꿈, 페이지 번호 글꼴을 조정.'],
'd47':['압축 제목을 실제 Bebas Neue로 변경하고 가로 비율·행간을 조정.','본문을 DM Sans로 교체, 누락 머리말과 일부 y 위치를 수정.'],
'd48':['Tinos/Poppins 실제 굵기 사용, Risk Management 본문 영역 폭을 늘려 원본 줄바꿈 유지.'],
'd49':['제목을 Tinos 400, 본문을 Poppins 300으로 조정하고 줄바꿈 재구성.'],
'd50':['제목을 실제 League Spartan 700으로 조정, 카드 수치를 chip 광학 중앙 정렬로 구현.'],
'd51':['분홍색 제목 폰트·굵기·자간 및 원본의 작은 텍스트 회전각을 조정.'],
'd52':['제목을 실제 Manrope 400으로 변경해 g의 모양을 가깝게 조정.','일부 제목 자간, 패널 크기, 목록의 다중 줄 높이를 조정.'],
'd53':['주요 제목을 실제 DM Sans 700으로 변경해 i 점과 폭을 조정.','흰 리본/물결을 재사용 가능한 곡선 좌표 데이터로 구현.']}
remaining={
'd38':['그래픽 그라디언트는 사용자 지시에 따라 회색 placeholder. 곡선 마스크의 접점은 근사.'],
'd39':['사진 배경과 건물은 회색 placeholder이므로 흰 텍스트 대비가 원본보다 낮음. League Spartan 글리프는 추정.'],
'd40':['사진은 회색 placeholder. 일부 본문 양끝 정렬과 League Spartan 세부 글리프가 원본과 차이.'],
'd41':['종이 질감과 빈티지 소품은 회색 placeholder. 원본의 H/P 장식 획 및 세리프 형태는 추정 글꼴로 근사.'],
'd42':['도시 사진은 회색 placeholder, 회사 로고는 Lucide 대체. 제목/카드 글꼴은 추정.'],
'd43':['뇌/꽃 일러스트 및 사진은 회색 placeholder. Forum과 Comic Neue는 원본 글꼴 추정이며 일부 장식 획/손글씨 모양이 다름.'],
'd44':['계단 사진과 흐린 배경은 회색 placeholder. 로고 없는 문단 폰트는 Barlow로 근사.'],
'd45':['붉은 흐림 배경을 회색 placeholder로 변경. 졸업 로고는 Lucide 대체, 제목 글리프는 추정.'],
'd46':['흑백 사진은 회색 placeholder. 본문의 양끝 정렬 및 작은 글리프 간격은 근사.'],
'd47':['사진은 회색 placeholder. 원본 제목의 장식적인 압축 획은 Bebas Neue로 근사; 교차/꽃 도형 곡률에 차이.'],
'd48':['사진은 회색 placeholder, 테이프 단순 사각형은 불규칙 경계 없이 근사. Tinos 세리프 글리프는 추정.'],
'd49':['제품/책상 사진은 회색 placeholder. Tinos/Cormorant는 원본 세리프 글꼴 추정; 작은 본문 양끝 정렬에 차이.'],
'd50':['그림 사진/하프톤 그래픽은 회색 placeholder. 그라디언트 사분원은 단색 곡선으로 구현. 별/8갈래 도형의 둥근 끝은 근사.'],
'd51':['TV/노트 사진은 회색 placeholder, 원본 TV의 기울기는 placeholder에 적용하지 않음. 제목 텍스트의 원본 작은 회전만 보존.'],
'd52':['현금/은행 사진은 회색 placeholder, 그래픽 그라디언트 패널은 단색. Manrope 제목과 Lucide Orbit 로고는 추정.'],
'd53':['대형 제목 세부 글리프/행간과 물결·리본의 곡률 및 일부 화면 밖 잘린 도형 방향은 근사.']}
post={
'd42-s007':['2차 검수 후 카드 이탤릭을 실제 Roboto Condensed 400 italic로 변경하여 5줄과 카드 안 높이를 복구.'],
'd49-s007':['2차 검수 후 긴 3줄 본문 크기를 19→18.5 source px로 줄여 추가 줄바꿈을 제거.'],
'd50-s001':['2차 검수 후 기본 작은 본문을 21→20 source px로 조정하여 3줄 유지.'],
'd50-s008':['2차 검수 후 기본 작은 본문 20 source px로 조정하여 긴 bullet의 추가 줄바꿈을 제거.'],
'd50-s010':['2차 검수 후 기본 작은 본문을 20 source px로 조정하여 6줄과 높이를 복구.'],
'd50-s011':['2차 검수 후 기본 작은 본문을 20 source px로 조정.'],
'd52-s009':['2차 검수 후 자간 0→-5 source px로 조정하여 Financial Literacy / & Banking 2줄 유지.'],
'd52-s010':['2차 검수 후 좌상단 누락된 Noble Bank 로고 추가.']}
rows=[]
for deck in assignment:
 d=deck['id']
 for slide in deck['slides']:
  s=slide['id'];key=f'{d}-{s}'
  changes=list(post.get(key,[]))
  if d=='d49':changes.append('2차 검수 후 제목 위치를 source y+18→y+7로 올려 원본 상단 기준선에 맞춤.')
  round_audits=[]
  for r in ['agent-c-1','agent-c-2']:
   meta=json.loads((Path('comparisons')/r/f'{d}.json').read_text())
   audit=next(x for x in meta['slides'] if x['id']==s)
   round_audits.append({'round':r,'unexpectedFindingsAtCapture':len([i for i in audit['findings'] if not i.get('expectedClip')])})
  rows.append({'deck':d,'slide':s,'originalViewed':True,'originalPath':f'public/reference/{d}/{s}.jpg','observedOriginalLayout':observations[key],
   'comparisonRoundsViewed':[{'round':r,'path':f'comparisons/{r}/{key}.jpg','viewedIndividually':True} for r in ['agent-c-1','agent-c-2']],
   'corrections':fixes[d],'postSecondRoundDataChanges':changes,'remainingDifferences':remaining[d],
   'fontGuessesRecorded':True,'unreadableReplacements':[],'unreadableTextNote':'판독 가능한 원본 문구와 원본 Lorem 본문을 보존. 판독 불가 문구로 간주해 새로 만든 텍스트 없음.',
   'intentionalClippingReason':None,'automaticAuditAtComparisonCapture':round_audits,
   'finalCaptureRequired':bool(changes)})
output={'agent':'decks_c','scope':'d38–d53 / 53 pages','originalsIndividuallyViewed':53,'firstComparisonsIndividuallyViewed':53,'secondComparisonsIndividuallyViewed':53,
 'reviewMethod':'각 원본과 각 1·2차 나란히 비교 이미지를 tools.view_image로 개별 열람. 연락처 시트만으로 검수하지 않음.',
 'cycleLimit':'덱별 에이전트 비교·수정 2회; 세 번째 최종 렌더/통합 시각 검수는 주 에이전트 담당.',
 'postfixAutomaticCheck':'review/agent-c-postfix-audit.json: 2차 뒤 마지막 수정의 live browser 자동 검증만 수행, 추가 PNG/비교 이미지 캡처 없음.',
 'sharedToolingCorrection':'d40 chip +2px 경고는 감사 canvas의 normal 자간 초기화 오류로 주 에이전트가 수정. ChipLabel은 실제 글꼴 face를 기다리는 공통 수정도 적용됨.',
 'sourceFiles':['src/decks/group-c.ts','src/decks/c-38-45.ts','src/decks/c-46-49.ts','src/decks/c-50-53.ts'],'pages':rows}
assert len(rows)==53 and len(observations)==53
(p/'agent-c.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
print('Wrote',len(rows),'page records')
