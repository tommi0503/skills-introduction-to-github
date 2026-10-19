export default [
 {id:'slide_01',title:'MIRI COMPANY',kicker:'20XX.12.17',lead:'영업 성장 전략 및 로드맵',cover:true},
 {id:'slide_02',title:'Contents',lead:'이곳에 프레젠테이션의 핵심 주제나 슬로건을 입력해 보세요.',blocks:[
  {kind:'agenda',at:[1,9,1,6],items:[
   {mark:'01',name:'현황 진단 및 분석',note:'목적 및 목표 · 영업 성과 리뷰 · 영업 환경 분석'},
   {mark:'02',name:'영업 전략 수립',note:'핵심 이슈 및 과제 도출 · 영업 목표 · 차별화 전략'},
   {mark:'03',name:'세부 실행 계획',note:'채널별 영업 전략 · 지원 체계 · 분기별 로드맵'},
   {mark:'04',name:'리스크 관리 및 성과 측정',note:'성과 측정 방법 · 잠재적 리스크 및 대응 방안'},
   {mark:'05',name:'결론 및 제안',note:'결론 및 주요 제안 사항'}]},
  {kind:'image',at:[10,3,1,6]}]},
 {id:'slide_03',kicker:'01 · 현황 진단 및 분석',title:'목적 및 목표',lead:'고객 중심의 영업 프로세스 혁신을 통해 시장 경쟁력을 강화합니다.',blocks:[
  {kind:'callout',at:[1,12,1,1],text:'급변하는 시장 환경 속에서 지속 가능한 성장을 위한 체계적인 영업 전략을 수립합니다.'},
  {kind:'cards',at:[1,12,2,5],items:[
   {icon:'chart-no-axes-combined',name:'매출 성장 달성',note:'전년 대비 매출 XX% 증가\n신규 고객 발굴을 통한 고객 기반 확대\n기존 고객 심화 영업으로 객단가 XX% 향상'},
   {icon:'chart-pie',name:'시장 점유율 확대',note:'이곳에 영업 전략의 두 번째 주요 목적을 명시해 주세요.\n경쟁력 강화 방안을 구체적인 지표와 함께 작성합니다.'},
   {icon:'network',name:'영업 조직 역량 강화',note:'이곳에 영업 전략의 세 번째 주요 목적을 명시해 주세요.\n내부 체계와 관련된 목표를 구체적으로 작성합니다.'}]}]},
 {id:'slide_04',kicker:'01 · 현황 진단 및 분석',title:'20XX 영업 성과 리뷰',lead:'신규 고객 확보와 디지털 채널 강화로 목표 대비 105% 달성',blocks:[
  {kind:'list',at:[1,6,1,3],variant:'check',items:[{name:'전체 매출 XXX억원 달성',note:'목표 대비 105%'},{name:'신규 고객 127개사 확보',note:'전년 대비 34% 증가'},{name:'디지털 채널 매출 비중 28% 달성'}]},
  {kind:'venn',at:[1,6,4,3],items:[{name:'디지털 채널 강화'},{name:'신규 시장 진출'},{name:'기존 고객 심화 영업'}]},
  {kind:'bars',at:[7,6,1,6],max:1500,items:[{value:1000,name:'20X1'},{value:1100,name:'20X2'},{value:1250,name:'20X3'},{value:1130,name:'20X4'},{value:1260,name:'20X5'}]}]}
];
