export const cover = {
  kicker: 'business proposal 2030',
  title: ['MIRI COMPANY', 'PRESENTATION'] as const,
  info: '서울시 구로구 디지털로31길 12 태평양물산 8층    |    대표전화 : 1544-5000    |    www.miricanvas.com',
}
export const toc = [
  { kind: 'v', items: ['경영성과', '인사말', '비전'], desc: '미리디가 꿈꿀수 있는 세상이 열립니다.' },
  { kind: 'h', items: ['사업전망', '프로젝트 로드맵'], desc: 'IT개발 혁신으로 글로벌 기업으로 성장해나갑니다.' },
  { kind: 'd', items: ['재무재표', '조직도', '회사연혁'], desc: '고객중심의 마케팅으로 노력합니다.' },
] as const

const font18 = '이 폰트는 THE명품고딕R 입니다. 폰트 사이즈는 18포인트 입니다.'
export const vision = {
  label: '비전', page: '05',
  head: ['글로벌 회사의 비전을', '실천해 나가는 미리컴퍼니', '새로운 미래의 미리디로 성장해나갑니다'],
  body: [`내용을 입력해주세요. ${font18}`, '내용을 입력해 주세요. 비전에 관한 상세설명을 적어주세요. 내용을 입력해주세요.', `${font18} 내용을 입력해 주세요.`],
  venn: { top: '소통', left: '책임', right: '창조', center: ['조화와', '성장'] },
  cols: ['Communication', 'Responsibility', 'Creation'].map((title) => ({
    title, lines: ['내용을 입력해주세요. 이 폰트는 THE명품고딕R', '입니다. 폰트 사이즈는 18포인트 입니다. 내용을', '입력해주세요. 이 폰트는 THE명품고딕R 입니다.', '폰트 사이즈는 18포인트 입니다.'],
  })),
}

const greet2 = ['인사말에 관한 상세설명을 적어주세요. 내용을 입력해주세요. 이 폰트는 THE명품', '고딕R 입니다. 폰트 사이즈는 18포인트 입니다. 내용을 입력해 주세요.']
export const greeting = {
  label: '인사말', page: '04',
  head: ['고객 중심 경영', '업계 최고 실적을 통한 만족 경영', '미리디의 약속입니다'],
  p1: ['안녕하세요. 미리디를 아끼고 사랑해주시는 고객 여러분.', '인사말에 관한 상세설명을 적어주세요. 내용을 입력해주세요. 이 폰트는 THE명품', '고딕R 입니다. 폰트 사이즈는 18포인트 입니다. 내용을 입력해 주세요. 인사말에', '관한 상세설명을 적어주세요.'],
  p2: greet2, p3: greet2,
  sign: '대표이사 미리디',
}

export const perf = {
  label: '경영성과', page: '03',
  title: ['BUISINESS', 'PERFORMANCE'],
  side: ['내용을 입력해주세요. 이 폰트는 THE명품고딕R 입니다. 폰트 사이즈는 18', '포인트 입니다. 내용을 입력해 주세요. 경영성과에 관한 상세설명을 적어주', '세요. 내용을 입력해주세요. 이 폰트는 THE명품고딕R 입니다.'],
  p1: ['내용을 입력해주세요. 이 폰트는 THE명품고딕R입니다. 폰트 사이즈는 18', '포인트 입니다. 내용을 입력해 주세요. 경영성과에 관한 상세설명을 적어주', '세요. 내용을 입력해주세요. 이 폰트는 THE명품고딕R 입니다. 폰트 사이즈', '는 18포인트 입니다. 내용을 입력해 주세요.'],
  p2: ['경영성과에 관한 상세설명을 적어주세요. 내용을 입력해주세요. 이 폰트는', 'THE명품고딕R입니다. 폰트 사이즈는 18포인트 입니다. 내용을 입력해 주', '세요. 경영성과에 관한 상세설명을 적어주세요.'],
  unit: '(단위_실억원)',
  charts: [
    { title: '취급액', axis: 650, values: [450, 650, 1300, 2000] },
    { title: '자산총계', axis: 869, values: [450, 650, 950, 1500] },
    { title: '당기순이익', axis: 1089, values: [550, 1200, 1800, 1900] },
  ],
}

export const market = {
  label: '사업전망', page: '06',
  title: ['MARKET', 'PROSPECT'],
  side: ['내용을 입력해주세요. 이 폰트는 THE명품고딕R 입니다. 폰트 사이즈는 18', '포인트 입니다. 내용을 입력해 주세요. 사업전망에 관한 상세설명을 적어주', '세요. 내용을 입력해주세요. 이 폰트는 THE명품고딕R 입니다.'],
  fig1: { label: 'Figure1. 시장점유율', from: ['2028', '45.4'], to: ['2030', '70.5'], growth: '20% 성장' },
  fig2: {
    label: 'Figure2. 판매현황', center: ['2030', 'Sales Status'],
    segs: [[36, '#e3e0d8'], [108, '#cdc7b8'], [72, '#bdb7a7'], [144, '#d4502f']] as [number, string][],
    callouts: [
      { v: '40%', x: 668, cy: 407, red: true, desc: ['판매현황에 대한 상세한', '설명을 적어주세요'], path: [[779, 404], [881, 404], [881, 452]] },
      { v: '10%', vx: 1134, x: 1087, cy: 361, desc: ['판매현황에 대한 상세한', '설명을 적어주세요'], path: [[1099, 363], [991, 363], [991, 416]] },
      { v: '30%', vx: 1134, x: 1087, cy: 500, desc: ['판매현황에 대한 상세한', '설명을 적어주세요'], path: [[1121, 500], [1053, 500]] },
      { v: '20%', vx: 742, x: 697, cy: 610, desc: ['판매현황에 대한 설명을', '적어주세요'], path: [[843, 637], [962, 637], [962, 599]] },
    ] as { v: string; vx?: number; x: number; cy: number; red?: boolean; desc: string[]; path: [number, number][] }[],
  },
}

export type StepIcon = 'bulb' | 'laptop' | 'pen' | 'people'
export const roadmap = {
  label: '프로젝트 로드맵', page: '07',
  steps: [
    { icon: 'bulb', en: 'DISCOVER', kr: '문제점 발견', title: 'STEP.1 사용 문제점을 발견한다', lines: ['프로젝트의 문제점을 분석하여 타', '업체와의 경쟁력에서 어떤 위치에', '있는지 측정합니다.'] },
    { icon: 'laptop', en: 'DEFINE', kr: '분석, 정의', title: 'STEP.2 문제점을 분석, 정의한다', lines: ['문제점을 발견하여 분석하여 왜', '문제점이 발견되었는지 전문적인', '통합 솔루션을 정의합니다.'] },
    { icon: 'pen', en: 'DEVELOP', kr: '프로세스 개발', title: 'STEP.3 프로세스를 개발한다', lines: ['풍부한 인프라와 글로벌 네트워크 기반', '으로 프로세스를 새롭게 정립합니다.'] },
    { icon: 'people', en: 'DELIVER', kr: '가치와 경험 전달', title: 'STEP.4 고객에게 경험을 전달한다', lines: ['문제점을 분석하고 새로운 프로세스를', '개발하여 고객에게 가치와 경험을 전달', '합니다.'] },
  ] as { icon: StepIcon; en: string; kr: string; title: string; lines: string[] }[],
  head: ['가치와 경험을 중심으로', '분석하여 프로세스를 개발하고', '문제점을 해결합니다'],
  side: ['내용을 입력해주세요. 이 폰트는 THE명품고딕R 입니다. 폰트 사이즈는 18포인트', '입니다. 내용을 입력해 주세요. 사업전망에 관한 상세설명을 적어주세요. 내용을', '입력해주세요. 이 폰트는 THE명품고딕R 입니다. 내용을 입력해주세요. 이 폰트는', 'THE명품고딕R 입니다. 폰트 사이즈는 18포인트 입니다.'],
}

export const finance = {
  label: '재무재표', page: '08',
  title: ['BUSINESS', 'PERFORMANCE'],
  charts: [
    { title: '취급액', unit: '(단위_실억원)', x: 72, axis: 107, xs: [133, 175, 219, 260], values: [900, 1500, 2507, 3485], fill: '#f2b5a5', line: '#d4502f', label: '#d4502f' },
    { title: '자산총계', unit: '(단위_실억원)', x: 337, axis: 378, xs: [405, 447, 491, 533], values: [350, 2500, 2800, 3500], fill: '#e5e3df', line: '#b8b3a2', label: '#b8b3a2' },
  ],
  years: ['2030', '2031', '2032', '2033'],
  tableTitle: ['주요재무제표', ' (단위_실억원)'],
  head: ['구분', '2030년', '2031년', '2032년', '2033년', '2034년'],
  rows: [
    ['자산총계', '3,986', '6,805', '15,448', '27,380', '27,520'],
    ['재산총계', '3,820', '6,682', '11,302', '14,205', '24,500'],
    ['자본총계', '4,250', '8,314', '9,736', '8,964', '9,356'],
    ['차입금', '2,367', '5,472', '8,496', '3,652', '4,651'],
    ['당기순이익', '3,487', '4,178', '2,147', '1,379', '7,284'],
    ['ROA', '3,287', '6,298', '1,239', '1,782', '9,123'],
    ['ROE', '3,897', '2,936', '1,687', '1,963', '1,.45'],
    ['EPS', '5,217', '7,321', '6,349', '2,784', '2,746'],
    ['취급액', '5,247', '9,214', '8,369', '9,378', '9,147'],
    ['총회원', '5,2179', '1,786', '7,123', '9,784', '2,351'],
  ],
  circled: [[0, 5], [1, 3], [4, 2], [7, 4]] as [number, number][],
}

export const org = {
  label: '조직도', page: '09',
  title: ['ORGANIZATIONAL', 'CHART'],
  people: [['강미리', '대표이사'], ['김정훈', 'COO']],
  body: ['내용을 입력해주세요. 이 폰트는 THE명품고딕R', '입니다. 폰트 사이즈는 18포인트 입니다. 내용', '을 입력해 주세요. 사업전망에 관한 상세설명을', '적어주세요. 내용을 입력해주세요. 이 폰트는', 'THE명품고딕R 입니다. 내용을 입력해주세요.'],
  depts: [
    ['경영전략본부', '인사팀', '재무팀', '법무팀'],
    ['전략기획실', '관리기획팀', '전략기획팀'],
    ['사업지원본부', '고객서비스팀', '사업지원팀'],
    ['마케팅본부', '마케팅기획팀', '홍보팀', '디자인팀'],
    ['개발본부', '개발팀', '정보보호팀', 'MIC개발팀'],
  ],
}

const bullets = (first: string, dash = false) => [`· ${first}`, '· THE 명품고딕R 18pt입니다.', '· 연혁에 맞는 글을 작성해 주세요.', `${dash ? '-' : '·'} THE 명품고딕R 17pt입니다.`]
export const history = {
  label: '회사연혁', page: '10', title: 'COMPANY HISTORY',
  photos: [
    { cx: 145, label: ['도약기', '업계 1위 기업'] }, { cx: 307 }, { cx: 456 },
    { cx: 618, label: ['성장기', 'AI 기술 개발'] }, { cx: 780 }, { cx: 929 },
    { cx: 1090, label: ['설립기', '창립'] },
  ] as { cx: number; label?: string[] }[],
  cols: [
    { x: 73, dot: 146, title: '글로벌 업계 1위 기업 달성', year: '2030', from: '~2029', lines: bullets('글로벌 업계 1위 달성') },
    { x: 311, dot: 382, title: '새로운 산업, 신사업 구축', year: '2028', from: '~2027', lines: bullets('새로운 산업, 신사업 구축') },
    { x: 549, dot: 619, title: 'AI 기술 개발 혁신', year: '2026', from: '~2025', lines: bullets('AI 기술 개발 혁신') },
    { x: 786, dot: 855, title: '인증획득, 연구소 등록', year: '2024', from: '~2023', lines: bullets('인증획득, 연구소 등록') },
    { x: 1023, dot: 1091, title: '설립기_미리컴퍼니 창립', year: '2023', from: '~2022', lines: bullets('설립기 미리 컴퍼니 창립', true) },
  ],
}

export const closing = ['A world that Miridi can dream of opens.', 'We grow into a global company through development and innovation.', 'We strive for customer-centric marketing.']
