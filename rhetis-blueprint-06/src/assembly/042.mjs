// Library assembly descriptors: semantic blocks on a 12 × 6 grid.
// Trend magnitudes without source axis values are normalized, while their visible numeric labels stay blank.
const entry=(n,title,lead,blocks)=>({id:'slide_'+String(n).padStart(2,'0'),title,kicker:`MIRI COMPANY · 2099 사업성과 보고서 · ${n<10?'주요 성과':n<16?'프로젝트 상세':'향후 계획'}`,lead,cover:false,dark:false,blocks});
const trend=(values)=>values.map((value,i)=>({name:`${i+1}Q`,value,label:' '}));
export default [
 entry(8,'핵심 성과 요약','주요 지표 전년 대비 고른 상승, 참여율 및 콘텐츠 소비 증가가 핵심 동력',[
  {kind:'metrics',at:[1,5,1,3],items:[{name:'MAU',fig:'85만 명'},{name:'참여율',fig:'+34%'}]},
  {kind:'metrics',at:[1,5,4,3],items:[{name:'광고 매출',fig:'30억 원'},{name:'커뮤니티 만족도',fig:'4.5점'}]},
  {kind:'bars',at:[6,7,1,6],max:100,items:trend([58,71,86,100])}
 ]),
 entry(9,'프로젝트별 성과','3개 프로젝트 모두 핵심 지표에서 일정 수준 이상의 개선을 보이며 안정적인 성과 달성',[
  {kind:'cards',at:[1,12,1,4],items:[
   {name:'프로젝트 1',icon:'flag',fig:'+28%',note:'월간 신규 게시글 수와 주간 재방문율 모두 목표 대비 높은 수준으로 상승\n신규 게시글 +28% · 활동 전환율 +7%'},
   {name:'프로젝트 2',icon:'heart-plus',fig:'+14%',note:'댓글·공감 수 증가와 참여 기반 전환율 향상에 기여\n참여 액션 XX만 건 · 참여율 +14%'},
   {name:'프로젝트 3',icon:'megaphone',fig:'XX%',note:'광고 상품 이용률과 제휴 캠페인 수 모두 성장세 유지\n성과 1 XX% · 성과 2 XX%'}]},
  {kind:'lines',at:[1,4,5,2],max:100,items:trend([47,52,83])},
  {kind:'lines',at:[5,4,5,2],max:100,items:trend([48,71,83])},
  {kind:'lines',at:[9,4,5,2],max:100,items:trend([53,55,83])}
 ]),
 entry(10,'세부 프로젝트','세부 프로젝트 추진을 통한 콘텐츠 노출·유입 구조 개선 및 핵심 지표 향상',[
  {kind:'cards',at:[1,8,1,2],variant:'quiet',items:[{name:'목표',note:'콘텐츠 노출 경로 개선\n신규 유입 고객의 소비 경험 강화'},{name:'접근 방식',note:'사용자 행동 기반 추천 구조 개편\n첫 화면 콘텐츠 큐레이션 재설계'}]},
  {kind:'metrics',at:[9,4,1,2],items:[{name:'첫 노출 도달 수',fig:'1,234'},{name:'수치 관련 키워드',fig:'50%'}]},
  {kind:'donuts',at:[1,8,3,4],items:[{name:'추천 기반',value:25},{name:'피드 기반',value:25},{name:'검색 기반',value:40},{name:'관련 키워드',value:10}]},
  {kind:'callout',at:[9,4,3,4],text:'이곳에 그래프가 보여주는 핵심 변화를 입력해 보세요.'}
 ]),
 entry(11,'세부 프로젝트 상세 내용','세부 프로젝트를 통한 콘텐츠 노출 구조 개선 및 초기 소비 경험 강화로 사용자 유입 최적화',[
  {kind:'cards',at:[1,5,1,6],variant:'quiet',items:[{name:'개선 전 화면',image:true,imageHeight:235,note:'개선 전 이미지를 넣어주세요'},{name:'개선 화면',image:true,imageHeight:235,note:'개선 된 이미지를 넣어주세요'}]},
  {kind:'cards',at:[6,7,1,3],variant:'quiet',items:[{name:'사업 개요',note:'콘텐츠 노출 구조 개선을 통해 초기 소비 경험을 강화\n프로젝트가 해결하고자 한 방향을 입력해 보세요.'}]},
  {kind:'cards',at:[6,4,4,3],variant:'quiet',items:[{name:'세부 내용',note:'첫 화면 콘텐츠 큐레이션 방식 재정비\n사용자 행동 기반 추천 알고리즘 적용\n콘텐츠 접근 동선 단축 위한 UI 조정'}]},
  {kind:'bars',at:[10,3,4,3],max:35000,items:[{name:'1Q',value:10000,label:'10,000건'},{name:'4Q',value:35000,label:'35,000건'}]}
 ]),
 entry(12,'프로젝트 성공요인','세부 프로젝트의 문제 분석·노출 전략·실행 구조 유기적 결합으로 핵심 지표 개선 견인',[
  {kind:'cards',at:[1,12,1,4],items:[
   {name:'사용자 행동 분석',icon:'user-round',note:'주요 이탈 지점 분석을 통한 핵심 병목 파악\n사용자 초기 진입 시나리오 기반 개선 포인트 도출'},
   {name:'일관된 콘텐츠 노출 전략',icon:'square-pen',note:'사용자 행동 기반 추천 로직 일괄 적용\n첫 노출 영역의 고정된 큐레이션 규칙 확립'},
   {name:'신속한 실행 및 피드백',icon:'messages-square',note:'배포→측정→보완의 짧은 주기 운영\n지표 기반 개선 방식 정착'}]},
  {kind:'cards',at:[1,12,5,2],variant:'quiet',items:[{name:'행동로그 분석 툴',note:'활용 도구를 입력해 보세요.'},{name:'큐레이션 가이드',note:'활용 도구를 입력해 보세요.'},{name:'주간 리뷰 체계',note:'활용 도구를 입력해 보세요.'}]}
 ]),
 entry(13,'고객 관련 성과','고객 전환율의 경우 신규·기존 사용자의 커뮤니티 참여율 상승으로 3Q 및 4Q에서 큰 폭 개선',[
  {kind:'bars',at:[1,7,1,6],max:100,items:[{name:'1Q 신규',value:25,label:' '},{name:'1Q 기존',value:38,label:' '},{name:'2Q 신규',value:38,label:' '},{name:'2Q 기존',value:50,label:' '},{name:'3Q 신규',value:56,label:' '},{name:'3Q 기존',value:63,label:' '},{name:'4Q 신규',value:82,label:' '},{name:'4Q 기존',value:100,label:' '}]},
  {kind:'list',at:[8,5,1,6],variant:'check',items:[{name:'경로 다변화로 신규 사용자 참여 확대',note:'신규 유입의 주요 경로가 커뮤니티 콘텐츠 → 추천 흐름으로 이동\n콘텐츠 기반 유입 고객의 전환율이 기존 대비 +7%p'},{name:'기존 사용자의 반복 참여가 참여율 향상 견인',note:'기존 고객의 반복 전환 비중이 성장\n이용 빈도 증가가 전환율 개선에 직접 기여'}]}
 ]),
 entry(14,'운영 관련 성과','운영 프로세스의 경우 단절된 업무 체계 연계 개선으로 효율성 및 일관성 향상',[
  {kind:'cards',at:[1,12,1,2],variant:'quiet',items:[{name:'운영 상황',note:'주요 업무에 관한 공유 기회가 적어 정보 전달 지연 및 작업 오류가 자주 발생'},{name:'개선 효과',note:'역할 간 실시간 상호 검증과 정보 교류가 가능해지며 처리 속도 향상과 오류 감소 효과'}]},
  {kind:'cards',at:[1,6,3,4],variant:'quiet',items:[{name:'운영 업무',kick:'기존',icon:'user-round-cog'},{name:'검수 업무',kick:'기존',icon:'user-round-search'}]},
  {kind:'architecture',at:[7,6,3,4],items:[{name:'개선 후',chips:['운영','자동 확인 ↔ 키워드','검수']}]}
 ]),
 entry(15,'핵심 이슈 및 개선','운영 과정에서 확인된 주요 이슈와 이를 해결하기 위한 개선 방향',[
  {kind:'cards',at:[1,2,1,6],column:true,variant:'quiet',items:[{name:'사용자 경험'},{name:'노출 로직'},{name:'콘텐츠 품질'}]},
  {kind:'list',at:[3,5,1,6],variant:'divided',items:[{name:'이슈',note:'초기 진입 시 원하는 콘텐츠를 찾기까지 단계가 많아 이탈 존재'},{name:'이슈',note:'로직이 사용자 패턴을 충분히 반영하지 못해 일관성 낮음'},{name:'이슈',note:'사용자 경험에 부정적 영향을 준 문제를 한 줄로 입력해 보세요.'}]},
  {kind:'list',at:[8,5,1,6],variant:'divided',items:[{name:'개선 포인트',note:'진입 동선을 단순화하고 핵심 콘텐츠 접근성을 높이는 구조 개편 검토 필요'},{name:'개선 포인트',note:'사용자 행동 기반 데이터 반영을 강화하고 추천 기준을 재정비'},{name:'개선 포인트',note:'해결을 위해 향후 추진할 필요가 있는 개선 방향을 작성해 보세요.'}]}
 ]),
 entry(16,'차년도 핵심 전략','차년도는 콘텐츠 소비 중심 성장 구조 강화 및 커뮤니티 활성화 기반 확대에 주력',[
  {kind:'cards',at:[1,4,2,4],variant:'on',items:[{name:'콘텐츠 소비 중심 성장 구조 강화'}]},
  {kind:'list',at:[5,8,1,6],variant:'check',items:[{name:'콘텐츠 노출 고도화',note:'카테고리별 초입 노출 정교화 · 신규 사용자 탐색 동선 최적화'},{name:'커뮤니티 활성화 강화',note:'고품질 게시물 추천 정책 개선 · 상호작용 증가를 위한 UI 개편'},{name:'생태계 성장 인프라 확장',note:'이곳에 해당 전략에 관한 설명을 입력해 보세요. 전략의 세부 추진방안을 넣어보세요.'},{name:'프로세스 효율화',note:'이곳에 해당 전략에 관한 설명을 입력해 보세요. 전략의 세부 추진방안을 넣어보세요.'}]}
 ]),
 entry(17,'차년도 추진 계획','준비·개선·고도화·확산의 단계별 추진을 통해 전략 실행력 강화 예정',[
  {kind:'pills',at:[1,12,1,1],items:[{name:'상반기 → 하반기'}]},
  {kind:'timeline',at:[1,12,2,5],items:[{kick:'2099. 1~3',name:'환경 정비',note:'핵심 지표 구조 재정의\n노출·추천 기준표 재정비\n운영 프로세스 점검'},{kick:'2099. 4~6',name:'UX 개선',note:'초기 진입 동선 개편\n주요 화면 UI 조정\n실험 기반 UX 개선 적용'},{kick:'2099. 7~9',name:'기능 고도화',note:'추천 알고리즘 반영 강화\n콘텐츠 큐레이션 고도화\n실험·검증 루프 정착'},{kick:'2099. 10~12',name:'성과 관리',note:'지표 모니터링 체계 운영\n성과 기반 반복 개선\n개선 요소의 서비스 전면 확산'}]}
 ]),
 entry(18,'요약 및 추후 방향','',[
  {kind:'cards',at:[1,3,1,3],variant:'quiet',items:[{kick:'사업 핵심 지표',name:'요약',icon:'presentation'}]},
  {kind:'list',at:[4,9,1,3],variant:'check',items:[{name:'핵심 지표 전반에서 긍정적인 개선 흐름과 가시적인 성과를 확인했습니다.'},{name:'콘텐츠 노출 및 유입 구조 개편 후 신규 고객 콘텐츠 소비량과 유입 지표가 상승했습니다.'},{name:'MAU 85만 명 · 참여율 34% 증가 · 광고 매출 30억 원 · 커뮤니티 만족도 4.5점'}]},
  {kind:'cards',at:[1,3,4,3],variant:'quiet',items:[{kick:'사업 성장 전략',name:'향후 방향',icon:'scroll-text'}]},
  {kind:'list',at:[4,9,4,3],variant:'check',items:[{name:'안정적인 콘텐츠 소비를 중심으로 사용자 리텐션을 확보하고, 플랫폼의 지속적인 성장 모멘텀을 고도화할 계획입니다.'},{name:'플랫폼 활성화를 위해 커뮤니티 참여 구조를 대폭 강화할 예정입니다.'},{name:'커뮤니티 내 신규 기능 도입과 UI/UX 보완에 대한 구체적인 검토를 진행할 것입니다.'}]}
 ])
];
