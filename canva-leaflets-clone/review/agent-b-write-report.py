import json,hashlib,datetime
from pathlib import Path
from PIL import Image
root=Path('.')
source=Path('src/data/group-b.ts')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
audit=json.loads(Path('review/agent-b-audit-latest.json').read_text())
assert sha(source)==audit['sourceFileSha256']
byAudit={(r['brochure'],r['page']):r for r in audit['pages']}
observations={
'l06-s01-p1':['크림색 바탕, 노란 물결 띠, 대칭 렌즈형 메뉴 6개, 두 주황 별, 검은 점선 쿠폰 곡선, 왼쪽 scallop과 굵은 한글 3줄을 확인했습니다.'],
'l06-s01-p2':['청록 소개 색면 위아래의 크림 타원, 소개사 카드 장식, 3줄 소개 문단, 3개 흰 꽃, 오시는 길과 오른쪽 물결선을 확인했습니다.'],
'l06-s01-p3':['아래 오른쪽이 둥근 노란 표지 면, 주황/흰색 제목 4행, 겹친 주황 스티커, 2035년 및 10/10-11 토-일, 시청 앞 광장을 확인했습니다.'],
'l06-s02-p1':['페스타 게임맵 2행 제목과 노란 4방향 곡선, 주사위, Start 아래 화살표, 세 시설 상자와 세 게임 상자, 주황 동선을 확인했습니다.'],
'l06-s02-p2':['청록 테두리 푸드트럭 존, 9개 연결 꽃, 휴게 공간, 주황 원형 체험 부스와 여섯 하단 체험 상자의 접지면 연결을 확인했습니다.'],
'l06-s02-p3':['노란 다엽형 상점 영역, Finish 위 화살표 및 말, 5개 상점 상자, 하단 체험 상자와 꺾인 위 화살표를 확인했습니다.'],
'l07-s01-p1':['연회색 단색면, INSPIRATION 영문, 큰 사진과 작은 사진, 3행 한국어 영감 문단의 위치와 줄바꿈을 확인했습니다.'],
'l07-s01-p2':['원형 NATURAL INGREDIENTS 이미지 배지, 2행 굵은 한국어 슬로건, 두 가로선, CONTACT US와 3행 연락처를 확인했습니다.'],
'l07-s01-p3':['PUREDERM 타이틀, 세로 제품 사진, 타원 모서리 ESSENTIAL LINE 버튼의 시각적 중앙 정렬을 확인했습니다.'],
'l07-s02-p1':['상단 가로선, DAILY SUN DEFENSE 타이틀, 제품 사진, 제품명/효능/성분/사용감 문단과 하단 3개 사진 및 선을 확인했습니다.'],
'l07-s02-p2':['상단 커튼/크림 사진의 별도 높이, REPAIRING CREAM, 제품 사진과 6행 설명을 확인했습니다.'],
'l07-s02-p3':['HYDRATING AMPOULE, 제품 사진, 6행 설명, 오른쪽 하단 사진을 확인했습니다.'],
'l08-s01-p1':['1236px 높이, 진한 파란 면, 통계/2025년 기준, 세 하늘색 육각형과 4,000/12/58 중앙 숫자 및 설명을 확인했습니다.'],
'l08-s01-p2':['상단 팀 사진, 파란 분리선, 흰 연락처 영역과 말풍선 및 3행 연락처를 확인했습니다.'],
'l08-s01-p3':['파란 타이틀 영역, 하늘색/보라색/흰색 다각형 마크, 아람 테크/슬로건, 여성 사진과 하단 흰 주소를 확인했습니다.'],
'l08-s02-p1':['상단 접지 경계의 잘린 다각형 마크, 역사/사명/비전 반복 3행 본문, 하단 파란 서비스 영역을 확인했습니다.'],
'l08-s02-p2':['보라색 리더십 면, 3개 육각 인물 사진, MARTHA BLEVINS/THOMAS LARSON/김지연 이름과 직책을 확인했습니다.'],
'l08-s02-p3':['요금 제목, 학생/직업/단체 패키지 소제목, 60/85/70달러, 1~2행 요금 설명과 원문의 굵기 차이를 확인했습니다.'],
'l09-s01-p1':['전통 종이 질감 배경과 흰 둥근 초대 카드, 매듭, 손글씨 초대 2행, 작은 선과 일시/장소/프로그램을 확인했습니다. 원문의 5일간을 보존했습니다.'],
'l09-s01-p2':['크림색 넓은 여백, 은행잎 이미지 아이콘, 오른쪽에서 시작하는 한복 인물 삽화, 자간을 둔 웹주소와 접지 경계를 확인했습니다.'],
'l09-s01-p3':['거친 달 그래픽, 한가위 대축제 세로쓰기, 작은 풍성한 추석 보내세요 문구, 큰 한복 남녀 삽화를 확인했습니다.'],
'l09-s02-p1':['한가위 유래 제목과 얇은 선, 역사와 유래/한가위의 의미 손글씨 소제목, 각 4행 본문과 강강술래 삽화를 확인했습니다.'],
'l09-s02-p2':['축제 프로그램 소개 제목, 4개 둥근 사진, 전통 문화 및 음식 체험/전통 놀이 체험과 각 2행 본문을 확인했습니다.'],
'l09-s02-p3':['상단 누각/감나무 삽화, 큰 사진과 두 작은 사진, 문화 공연 소제목과 2행 본문을 확인했습니다.'],
'l10-s01-p1':['남색 면, 두 4방향 곡선 별, 걸어서 만나는 서울의 밤 명조 제목, 5행 안내와 웹주소를 확인했습니다.'],
'l10-s01-p2':['크림 면, 타원 야경코스, 세 코스와 얇은 분리선, QR코드 라벨 및 연락처 하단 남색 면을 확인했습니다.'],
'l10-s01-p3':['남색 표지, 서울 야경가이드 명조 2행 제목, SEOUL NIGHT WALK, 아치형 야경 사진을 확인했습니다.'],
'l10-s02-p1':['코스 안내 타원과 굵은 선, 계절/예매/분수 3행 본문, A/B/C의 시작/1시간 표와 세 빨간 지도 핀을 확인했습니다.'],
'l10-s02-p2':['편의 시설 타원과 굵은 선, 6행 두 열 안내, 작은 촬영 캐릭터, 테두리 촬영 꿀팁과 본문 좌우 정렬을 확인했습니다.'],
'l10-s02-p3':['즐길거리 타원, 큰 골목 사진과 두 작은 사진, 달빛 포토존 3 곳/기념 촬영, 3행 장소, 스카이라인 및 두 구름 윤곽을 확인했습니다.']}
fixes={
'l06-s01-p1':['실제 서체를 비교했습니다. 2차의 Gasoek One은 과도하게 붙는 획으로 판단해 마지막 소스에서 Black Han Sans 400으로 복원했습니다.','푸드트럭 존/쿠폰의 원본 글폭에 맞춘 크기 조정, 검은 곡선 점선과 하단 scallop 확장.'],
'l06-s01-p2':['소개 본문22→20px 및 줄간격1.15로 원래3행 복원.','Lucide 윤곽 꽃을 흰 단순 SVG 꽃잎으로 변경하고 크기/위치 보정.','소개사 및 오시는 길 제목 크기 보정 및 최종 Black Han Sans 복원.'],
'l06-s01-p3':['겹친 주황/흰 제목 요소를 색상별 4개의 단일 행으로 분리해 겹침 제거.','노란 표지 아래 오른쪽 둥근 모서리 복원.','최종 Black Han Sans와 제목 줄 위치/글폭 보정.','날짜61px 및 원문 토-일의 구분 기호 보정.'],
'l06-s02-p1':['주황 체험 동선의 왼쪽 직선 연결 면 보완.','둥근 Lucide 화살표를 단순 채운 다각형으로 바꾸고 원본 굵기/크기로 보정.','최종 Black Han Sans로 제목/Start 복원하고 게임맵 행간과 글폭 보정.'],
'l06-s02-p2':['연결 꽃 SVG 테두리를 보완해 큰 크림 틈을 줄였습니다.'],
'l06-s02-p3':['Finish가 나무 말 회색영역에 가려지던 paint order 수정 및 말 높이/위치 보정.','최종 Finish 서체/글폭 및 오른쪽 하단 꺾인 위 화살표 방향 보정.'],
'l07-s01-p1':['본문24→23px, 줄간격1.36으로 중간 한 글자가 독립 행에 감기는 오류를 없애고3행 복원.'],
'l07-s01-p2':['CONTACT US48→45px로 원본 글폭에 맞춤.'],
'l07-s01-p3':['PUREDERM67→65px로 원본 글폭에 맞춤.'],
'l07-s02-p1':['상단 가로선 y20→52, 시작 x30→0으로 수정.','설명 계속 행 앞 불필요한 bullet 제거.','마지막 원문 판독에서 알로아를 알로에로 보정.'],
'l07-s02-p2':['상단 이미지 y59,h191→y90,h159로 원본 경계 맞춤.'],
'l07-s02-p3':[],
'l08-s01-p1':['4,000과58의 글폭을 맞춰64px/80px로 보정. 중앙 ink 정렬 확인.'],
'l08-s01-p2':[], 'l08-s01-p3':[],
'l08-s02-p1':['본문 폭/굵기22px/600으로 보정.','마지막 소스에 상단 오른쪽 파란 삼각 면 추가.'],
'l08-s02-p2':[],
'l08-s02-p3':['가격을 실제 Pretendard500,72px,-2px자간으로 맞추고 기준선을11px 위로 올림.'],
'l09-s01-p1':['Nanum Brush Script→Gaegu700 실제 비교 후, 원본의 좁은 글폭과 획에 더 가까운 실제 Nanum Pen Script400으로 최종 소스 변경. 초대 문구는 2줄, 높이86px로 유지하며 마지막 자동감사 통과.'],
'l09-s01-p2':['웹주소26px/3px자간→23px/1.5px자간으로 원본 글폭에 맞춤.'],
'l09-s01-p3':['원본에 더 가까운 실제 Nanum Pen Script400으로 최종 세로쓰기 서체 변경.'],
'l09-s02-p1':['본문20px/1.28행간으로 원문 줄바꿈 복원.','손글씨를 최종 Nanum Pen Script400으로 변경.'],
'l09-s02-p2':['본문20px/1.28행간으로 맞춤 및 손글씨를 최종 Nanum Pen Script400으로 변경.'],
'l09-s02-p3':['본문 문화공연 끝 한 글자가 추가행에 감기던 문제를20px로 해결.','손글씨를 최종 Nanum Pen Script400으로 변경.'],
'l10-s01-p1':['Noto Serif KR→실제 Nanum Myeongjo400 본문/700 제목으로 최종 보정.','웹주소를 실제 Noto Sans KR300으로 보정.'],
'l10-s01-p2':['명조 타원 라벨을 실제 Nanum Myeongjo700으로 최종 보정.','QR 안내21px/700→20px/최종500으로 원본 글폭과 굵기에 맞춤.'],
'l10-s01-p3':['명조 제목을 실제 Nanum Myeongjo700 및 y113으로 최종 보정.','영문31→28px로 원본 글폭 보정.'],
'l10-s02-p1':['코스 A/B/C 기준 위치를9px 위로 이동.','타원 명조 라벨을 최종 Nanum Myeongjo700으로 변경.'],
'l10-s02-p2':['편의시설 표 위치7px 위로 이동.','촬영 꿀팁 제목과 본문을 분리해 본문을 왼쪽 정렬하고 행 기준선 보정.','타원 명조 라벨을 최종 Nanum Myeongjo700으로 변경.'],
'l10-s02-p3':['Lucide가 사각 아이콘비로 축소되던 구름을 실제 너비의 단순 SVG 윤곽으로 구현.','타원 명조 라벨을 최종 Nanum Myeongjo700으로 변경.']}
placeholders={
'l06-s01-p1':[], 'l06-s01-p2':['보드게임 카드 이미지 아이콘','지도 및 나무 말의 복합 이미지'], 'l06-s01-p3':[],
'l06-s02-p1':['입체 주사위 이미지 아이콘'], 'l06-s02-p2':['나무 게임판 이미지 아이콘'], 'l06-s02-p3':['나무 보드게임 말/퍼즐 이미지 아이콘'],
'l07-s01-p1':['스킨케어 사진2개'], 'l07-s01-p2':['NATURAL INGREDIENTS 이미지 배지'], 'l07-s01-p3':['앰플 제품 사진'],
'l07-s02-p1':['제품 사진 및 하단 상세 사진3개'], 'l07-s02-p2':['크림/커튼 사진 및 크림제품 사진'], 'l07-s02-p3':['앰플 제품 및 은박 튜브 사진'],
'l08-s01-p1':[], 'l08-s01-p2':['팀 사진'], 'l08-s01-p3':['여성 스마트폰 사진'], 'l08-s02-p1':[], 'l08-s02-p2':['리더 인물 사진3개; 육각 clipPath 유지'], 'l08-s02-p3':[],
'l09-s01-p1':['전통 종이 질감 그래픽 배경','전통 매듭 이미지 아이콘'], 'l09-s01-p2':['은행잎 이미지 아이콘','오른쪽 접지면에서 이어지는 한복 인물 복잡 삽화'], 'l09-s01-p3':['거친 붓 질감 달 그래픽','한복 남녀 복잡 삽화'],
'l09-s02-p1':['전통 종이 질감 배경','강강술래 인물 복잡 삽화'], 'l09-s02-p2':['전통 종이 질감 배경','전통 행사 사진4개'], 'l09-s02-p3':['전통 종이 질감 배경','누각/감나무 복잡 삽화','행사 사진3개'],
'l10-s01-p1':[], 'l10-s01-p2':[], 'l10-s01-p3':['야경 사진; 아치 clip 유지'], 'l10-s02-p1':[], 'l10-s02-p2':['촬영 팁 캐릭터 이미지 아이콘'], 'l10-s02-p3':['골목/음식/방문객 사진3개','타워/건물의 복잡 스카이라인 삽화']}
diffs={
'l06-s01-p1':['원본의 복잡한 점무늬 질감 생략; 색면과 곡선 보존.','실제 Black Han Sans를 사용하지만 원본의 장식 숫자 절개/일부 자형은 다릅니다.','메뉴 렌즈형 도형의 곡선이 미세하게 다릅니다.'],
'l06-s01-p2':['원본의 복잡한 점무늬 질감 생략; 색면 보존.','큰 타원 접점과 지도 옆 물결 곡선에 소폭 차이가 있습니다.','사진/이미지 아이콘을 회색으로 치환했습니다.'],
'l06-s01-p3':['겹친 스티커와 파란 별의 작은 곡선 차이.','점무늬 texture 생략 및 원본 장식 숫자의 절개 형태 차이.'],
'l06-s02-p1':['원본의 복잡한 점 texture 생략.','제목/영문의 일부 자형 차이가 남습니다.'],
'l06-s02-p2':['연결 꽃의 연결점/크림 빈공간 곡선은 근사이며 texture를 생략했습니다.'],
'l06-s02-p3':['노란 다엽 색면의 개별 곡선 위치가 근사입니다.','원본의 점 texture와 나무 이미지 세부는 없습니다.'],
'l07-s01-p1':['영문은 실제 Inter Variable로 근사하여 일부 글자 폭이 다릅니다.','사진 영역의 내용은 회색입니다.'], 'l07-s01-p2':['원본 이미지 배지를 회색 원으로 치환했습니다.','전화 앞/문자 사이 공백과 일부 글자 폭에 소폭 차이가 있습니다.'], 'l07-s01-p3':['영문 Inter Variable의 미세한 획/자폭 차이가 있습니다.','제품 사진을 회색으로 치환했습니다.'],
'l07-s02-p1':['영문 Inter Variable의 미세한 자형 차이.','하단 상세 사진3개의 인접 회색 면이 시각적으로 합쳐 보입니다.'], 'l07-s02-p2':['한글 문단의 실제 Noto Sans KR 글자 폭에 소폭 차이.','사진을 회색으로 치환했습니다.'], 'l07-s02-p3':['한글 문단의 실제 Noto Sans KR 글자 폭에 소폭 차이.','사진을 회색으로 치환했습니다.'],
'l08-s01-p1':['실제 Noto Sans KR/Roboto Condensed 사용; 원본의 일부 숫자/본문 자형 및 기준선에 소폭 차이.'], 'l08-s01-p2':['말풍선의 작은 모서리 및 dot 모양에 소폭 차이.','팀 사진을 회색으로 치환했습니다.'], 'l08-s01-p3':['브랜드 마크는 단순 다각형으로 근사하여 모서리/작은 간격에 차이가 있습니다.','원본 흰 주소를 보존했으며 회색 사진 placeholder 위에서 대비가 낮아집니다.'],
'l08-s02-p1':['마크는 단순 다각형이며 본문 기준선에 소폭 차이가 있습니다.'], 'l08-s02-p2':['원본 인물 사진을 육각 회색으로 치환했습니다.','영문과 한국어 직책의 작은 자형/기준선 차이.'], 'l08-s02-p3':['가격의 일부 글자 형태와 영문/Korean 조합폭 차이가 있습니다.'],
'l09-s01-p1':['종이 질감은 요청에 따라 회색이며 매듭도 회색입니다.','실제 Nanum Pen Script400으로 근사해 원본 손글씨의 일부 자형이 다를 수 있습니다.'], 'l09-s01-p2':['은행잎과 인물 삽화는 회색입니다.','웹주소의 일부 영문 자폭 차이가 있습니다.'], 'l09-s01-p3':['달/한복 삽화는 회색이며 세로 손글씨는 실제 Nanum Pen Script400 근사입니다.'],
'l09-s02-p1':['종이/인물 삽화 회색 면이 합쳐져 보입니다; 같은 #e5e5e5 규칙을 준수한 결과입니다.','본문의 일부 자간/기준선과 손글씨 자형 차이.'], 'l09-s02-p2':['종이 배경과 사진 회색 면이 합쳐져 보입니다; 같은 #e5e5e5 규칙을 준수한 결과입니다.','손글씨와 작은 본문 자형 차이.'], 'l09-s02-p3':['종이/사진/삽화 회색 면이 합쳐져 보입니다; 같은 #e5e5e5 규칙을 준수한 결과입니다.','손글씨와 작은 본문 자형 차이.'],
'l10-s01-p1':['별 곡선의 미세한 폭 차이 및 명조/URL 일부 자형 차이.'], 'l10-s01-p2':['타원 윤곽의 작은 높이 차이 및 코스 본문 글자 폭 차이.'], 'l10-s01-p3':['실제 Nanum Myeongjo를 사용하였으나 일부 명조 자형/기준선 차이가 남을 수 있습니다.','야경 사진은 아치형 회색입니다.'],
'l10-s02-p1':['코스 표의 얇은 글자 및 핀 곡선에 소폭 차이.'], 'l10-s02-p2':['캐릭터를 회색으로 치환했습니다.','촬영 꿀팁의 작은 글자 자폭 차이가 있습니다.'], 'l10-s02-p3':['사진/스카이라인은 회색입니다.','구름 윤곽의 각 봉우리 모양이 근사입니다.']}
# All rows in the two captured rounds were individually inspected by this agent.
pages=[];checkedPngs=[]
for num in range(6,11):
 b=f'l{num:02d}';r1=json.loads(Path(f'comparisons/agent-b-r1/{b}.json').read_text());r2=json.loads(Path(f'comparisons/agent-b-r2/{b}.json').read_text());by1={r['id']:r for r in r1['panels']+r1['sides']}
 for row in r2['panels']+r2['sides']:
  key=f"{b}-{row['id']}";side=row['id'][:3];mode='panel' if '-p' in row['id'] else 'unfolded';panelKeys=[f'{b}-{side}-p{i}' for i in range(1,4)]
  def vals(table):return table.get(key, sum((table[k] for k in panelKeys),[]))
  for r in [by1[row['id']],row]:
   p=Path(r['file']);assert Image.open(p).size==(1280,720);assert sha(p)==r['pngSha256'];checkedPngs.append(str(p))
  a=byAudit[(b,row['id'])];changed=r2['definitionHash']!=a['definitionHash']
  records={}
  for rn,meta,rr in [('agent-b-r1',r1,by1[row['id']]),('agent-b-r2',r2,row)]:
   records[rn]={'comparison':f'comparisons/{rn}/{key}.jpg','viewedIndividually':True,'png':rr['file'],'pngSha256':rr['pngSha256'],'definitionHash':meta['definitionHash'],'rendererHash':meta['rendererHash'],'capturedAt':meta['capturedAt'],'unexpectedFindings':[x for x in rr['findings'] if not x.get('expectedClip')]}
  pages.append({'brochure':b,'page':row['id'],'side':side,'mode':mode,'originalViewed':True,'originalFullImageViewed':f'public/reference/{b}/{side}.png','originalSourceSha256':row['referenceSha256'],'sourceObservations':vals(observations),'comparisonRoundsViewed':['agent-b-r1','agent-b-r2'],'comparisons':records,'corrections':vals(fixes),'remainingDifferences':vals(diffs),'remainingPlaceholderReasons':vals(placeholders),'unreadableReplacements':[],'replacementCount':0,'latestSourceAudit':{'definitionHash':a['definitionHash'],'canvas':a['audit']['size'],'unexpectedFindings':[x for x in a['audit']['issues'] if not x.get('expectedClip')],'fontChecks':a['audit']['fontChecks']},'intentionalClipReasons':list({x.get('reason','원본 접지/페이지 경계에서 의도적 장식 잘림') for x in a['audit']['issues'] if x.get('expectedClip')}),'lastSourceChangesAfterRound2':changed,'finalRecaptureRequired':changed,'lastSourceChangesReflectedInFinalPng':'pending-primary-third-round' if changed else 'confirmed-in-agent-b-r2'})
assert len(pages)==40
assert len(checkedPngs)==80
assert all(not p['latestSourceAudit']['unexpectedFindings'] for p in pages)
report={'agent':'B','scope':['l06','l07','l08','l09','l10'],'nativeOriginalCount':10,'reviewedScreenCountPerRound':40,'agentVisualComparisonRoundCount':2,'allOriginalsViewedIndividually':True,'allRound1ScreensViewedIndividually':True,'allRound2ScreensViewedIndividually':True,'allPanelsAndUnfoldedScreensIncluded':True,'reviewMethod':'각 페이지 원본/브라우저 결과를 나란히 놓은 개별 비교 이미지를 view_image로 모두 열람했습니다. 연락처 시트로 검수를 대신하지 않았습니다. 3차 에이전트 비교 캡처는 하지 않았습니다. 두 번째 비교 뒤 최종 소스 보정은 마지막 브라우저 자동감사로 검사했고 주 에이전트의 세 번째 최종 캡처/개별 검수가 필요합니다.','unreadableReplacements':[],'textPolicy':'모든 확인 가능한 본문/제목을 실제 한국어/영문 텍스트로 옮겼습니다. 판독불가 문구를 선으로 대체하지 않았으며 이번 10장에서는 임의 대체 문구를 사용하지 않았습니다.','sourceInstructionsPolicy':'첨부된 인쇄물의 안내/광고 문구는 재현 대상 콘텐츠로 취급하고 작업 지시로 실행하지 않았습니다.','fontsSelected':{'l06':'Black Han Sans400/Pretendard 실제; Gasoek One400 및 Bagel Fat One400 실제 glyph specimen과 비교, 원본의 일부 장식 숫자는 근사','l07':'Noto Sans KR400/700/Inter Variable(Arial 별칭)400/600/700 실제','l08':'Noto Sans KR400/500/600/700, Roboto Condensed Variable400, Pretendard Variable500 실제','l09':'Nanum Pen Script400/Noto Sans KR400/700/Inter Variable 실제; Nanum Brush Script400/Gaegu700/Single Day400 glyph specimen 비교','l10':'Nanum Myeongjo400/700,Noto Sans KR300/700,Pretendard Variable300/400/500/600/700 실제'},'sourceFile':'src/data/group-b.ts','sourceFrozen':True,'sourceFileSha256':sha(source),'latestAuditArtifact':'review/agent-b-audit-latest.json','latestBrowserAuditScreens':40,'latestBrowserAuditUnexpected':0,'latestAuditPerformedAfterLastSourceChange':True,'typecheckPassedAfterLastSourceChange':True,'pngIntegrity':{'verifiedCount':80,'allDimensions':[1280,720],'sha256MatchesAllCapturedMetadata':True},'primaryFinalCaptureRequired':True,'pages':pages,'reportedAt':datetime.datetime.now(datetime.timezone.utc).isoformat()}
Path('review/agent-b.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'pages':len(pages),'nativeOriginals':10,'checkedPngs':len(checkedPngs),'latestAuditUnexpected':0,'sourceSha256':report['sourceFileSha256'],'primaryRecapturePages':sum(p['finalRecaptureRequired'] for p in pages)},ensure_ascii=False))
