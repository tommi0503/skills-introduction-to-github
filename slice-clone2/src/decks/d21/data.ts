export const brief = ['PLEASE ENTER A BRIEF', 'DESCRIPTION FOR THIS PART.']
export const brief3 = ['PLEASE ENTER A', 'BRIEF DESCRIPTION', 'FOR THIS PART.']
export const byline = '2080.05.01  |  기획팀 김미리'

export const cover = { kicker: 'Company Report', light: '꼭 넣어야 하는', bold: '회사 소개서 양식' }

const descs = ['소개할 내용을 입력해 보세요. 포함되는 내용을 나열해 보세요.', '항목으로 깔끔하게 정리해요. 핵심 키워드만 제시해도 좋아요.', '주제에서 말하는 바를 요약해요. 주제의 핵심내용을 입력해요.']
export const toc = {
  kicker: 'CONTENTS', title: ['목차', '페이지'],
  items: Array.from({ length: 6 }, (_, i) => ({ n: `0${i + 1}`, title: '목차 쓰는 곳', desc: descs[i % 3] })),
  gridDesc: ['소개할 내용을 입력해 보세요.', '포함되는 내용을 나열해 보세요.'],
}

export const chapter = {
  kicker: 'CHAPTER. 01', title: '회사 소개',
  lines: ['이곳에는 큼지막한 제목을 보완할 상세한 항목들을 적어보세요.', '긴 문장으로 써도 좋지만, 보기 좋으려면 키워드만 나열해도 좋아요.', '위 혹은 옆의 제목과 길이를 맞추면 좀 더 예쁘게 만들 수 있어요.'],
}
export const section = { n: '01', title: '회사 소개', lines: ['목차에 대해 소개할 내용을 입력해 보세요.', '목차에 포함되는 내용을 나열해 보세요.'] }

export const ceo = {
  title: '글로벌 기업으로 성장하겠습니다.',
  lines: ['이 페이지는 회사 CEO 인사말을 입력하는 페이지 입니다.', '우측에 CEO 대표 사진을 넣어주시고, 텍스트 박스를 더블 클릭하신 후 대표님 인사말을 기입', '해주시길 바랍니다.  사용 폰트는 프리텐다드 Light이며, 사이즈는 18 포인트 입니다.', '문단이나 내용은 자유롭게 변형해주시면 됩니다.', '꾸밈 요소를 배제한 심플한 디자인을 지향하는 프레젠테이션 레이아웃입니다.'],
  sign: '미리 컴퍼니 대표이사', foot: '*페이지 내 인물사진은 샘플이미지입니다.',
}

export const result = {
  kicker: 'RESULT', title: '주요 사업 성과', band: '이곳에 사업 성과를 요약해 주세요.',
  stats: [['117', '억', '분기매출'], ['200', '만명', '가입자 수'], ['12', '%', '성장률']],
  lead: '결론에 해당하는이미지를 넣고 이곳에는 결론에 대한 설명을 간단하게 넣어주세요.',
  lines: ['결론은 전체 내용을 요약하고, 보고에서 핵심이 되는 포인트를 강조합니다. 간결한 문장이 중요해요.', '보고할 땐 결론을 먼저 제시해 보세요. 구체적인 보고보다 앞 부분에 배치하는게 좋습니다.'],
}

export const vision = {
  kicker: 'VISION', title: '회사 비전 및 가치',
  cards: [1, 2, 3].map((n) => ({ title: `키워드 0${n}`, lines: ['키워드에 대한 내용을 입력하세요.', '키워드에 대한 내용을 입력하세요.'] })),
  quote: ['이곳에 회사의 비전이나 가치를 요약해 주세요.', '긴 문장이라면 가장 핵심이 되는 단어들을 나열해도 좋아요.'],
}

export const history = {
  kicker: 'HISTORY', title: '회사 연혁',
  cols: ['2060년', '2070년', '2080년', '2090년'].map((year, i) => ({
    year, title: `키워드${i + 1}`,
    bullets: [['이곳에는 회사의 설립부터', '현재까지 있었던 주요 사항', '들을 입력해 주세요.'], ['시간의 흐름을 녹여내 보다', '자연스러운 전개를 완성해', '보세요.']],
  })),
}

export const brief10 = {
  kicker: 'ABOUT COMPANY', light: '미리컴퍼니', bold: '간략한 연혁 페이지',
  rows: [['2070', 480, 382], ['2080', 544, 492], ['2090', 608, 595]].map(([year, x, y]) => ({ year: year as string, x: x as number, y: y as number, lines: ['이곳에는 연도별 회사 주요 사항들을 간략하게 입력해주세', '요. 주목하기 좋은 성과도 좋아요.'] })),
}

export const areas = {
  kicker: 'KEYWORD', title: '주요 사업 영역',
  cards: [1, 2, 3].map((n) => ({ title: `키워드 0${n}`, lines: ['한눈에 보고 파악할 수 있도록', '이곳에 자사 사업 영역을', '간략히 요약해 주세요.'] })),
}

export const share = {
  kicker: 'BACKGROUND', title: '사업별 비중',
  pie: [{ label: '프로젝트 1', v: 30, c: '#4870b0', x: 399, y: 361, white: true }, { label: '프로젝트 2', v: 40, c: '#bdc8d3', x: 342, y: 474 }, { label: '프로젝트 3', v: 30, c: '#ffffff', x: 285, y: 361 }],
  caption: '[ 사진이나 그래프를 넣을 공간]',
  items: [
    { n: '01', title: '비중 관련 간단 소개', bullets: [['사업별 비중을 입력하는 페이지입니다. 매출비중, 이익 비', '중 등 다양한 용도로 활용하세요.'], ['왼쪽의 사진이나 그래프를 추가로 설명해 배경의 내용을', '완성해 보세요.']] },
    { n: '02', title: '비중 관련 간단 소개', bullets: [['사업별 비중을 입력하는 페이지입니다. 매출비중, 이익 비', '중 등 다양한 용도로 활용하세요.'], ['또한 연구 목적이나 범위를 나타내 배경의 당위를 나타내', '보세요.']] },
  ],
}

const trendBul = [['연간 실적 등의 추이를 소개하는 페이지입니', '다. 흐름을 간단히 알려주세요.'], ['왼쪽의 사진이나 그래프를 추가로 설명해 배', '경의 내용을 완성해 보세요.']]
export const trend = {
  kicker: 'TRANSITION', title: '연간 실적 추이',
  ticks: [80, 60, 40, 20, 0],
  points: [[232, 37], [375, 45], [518, 65], [660, 75]] as [number, number][],
  labels: [['항목 01', 232], ['항목 02', 375]] as [string, number][],
  items: [{ n: '01', title: '실적 관련 간단 소개', bullets: trendBul }, { n: '02', title: '실적 관련 간단 소개', bullets: trendBul }],
}

export type FactorIcon = 'calendar' | 'org' | 'doc'
export const compare = {
  kicker: 'COMPARISON', title: '분기별 실적 비교',
  legend: ['TYPE 01', 'TYPE 02'],
  bars: [[167, 36, 394, 'blue'], [228, 40, 454, 'grey'], [332, 36, 364, 'blue'], [392, 40, 305, 'grey']] as [number, number, number, 'blue' | 'grey'][],
  caption: '[ 사진이나 그래프를 넣을 공간]',
  items: (['첫번째 요인', '두번째 요인', '세번째 요인'] as const).map((title, i) => ({ n: `0${i + 1}`, title, icon: (['calendar', 'org', 'doc'] as FactorIcon[])[i], lines: ['배경 요인을 입력하는 페이지입니다. 현상이 일어나게 된 원인을 입', '력하세요. 오른쪽 그래프를 설명해 배경의 내용을 완성해 보세요.'] })),
}

export const partners = { kicker: 'PARTNER', title: '주요 협력사', cards: [1, 2].map((n) => ({ title: `협력사 0${n}`, lines: ['이곳에는 해당 협력사에 관한', '간단한 소개를 입력해 주세요.'] })) }

export const analysis = {
  kicker: 'ANALYSIS', title: '내부 역량 분석', band: '이 곳에는 분석한 세부 내용을',
  quote: ['이 곳에는 분석한 내용을 요약해', '입력해 주시기 바랍니다.', '분석한 결과에 관한 담당자의', '의견도 함께 남겨주세요.'],
  stepsA: [
    { n: '1', box: [1063, 257], right: 1036, cy: 263, lines: ['분석에 사용된 데이터의 종류, 출처,', '수집 방법 등을 설명합니다. 데이터의', '신뢰성과 정확성을 강조하는 부분입니다.'] },
    { n: '2', box: [1007, 418], right: 980, cy: 422, lines: ['실제로 어떻게 분석을 수행했는지,', '어떤 단계들을 거쳤는지와 데이터 전처리,', '모델 학습, 평가 등의 단계를 포함합니다.'] },
    { n: '3', box: [955, 570], right: 932, cy: 576, lines: ['분석결과와 그 해석을 설명합니다. 어떤 지표를', '사용하여 어떻게 결과를 해석했는지를 명시합니다.'] },
  ],
  stepsB: [
    ['분석에 사용된 데이터의 종류, 출처,수집 방법 등을 설명합니다.', '데이터의 신뢰성과 정확성을 강조하는 부분입니다.'],
    ['실제로 어떻게 분석을 수행했는지, 어떤 단계들을 거쳤는지와 데이터', '전처리, 모델 학습, 평가 등의 단계를 포함합니다.'],
    ['분석결과와 그 해석을 설명합니다. 어떤 지표를  사용하여 어떻게', '결과를 해석했는지를 명시합니다.'],
  ],
}

export const perf = {
  kicker: 'RESULT', title: '성과 페이지',
  lines: ['이 페이지는 성과에 대한 간략한 소개를 하는 페이지 입니다.', '성과에 대한 간략한 설명을 입력해주세요.'],
  a: ['48%', '성과 항목 A'], b: ['15%', '성과 항목 B'],
}

const kpiText = ['이 곳에 위 키워드에 대한 내용을 입력해주세요.', '텍스트 박스를 더블클릭하여 내용을 수정할 수 있', '습니다. 명확한 상승 수치나 증거를 제시하면 설', '득력이 높아져요.']
export const kpis = {
  kicker: 'RESULT', title: '성과 페이지',
  first: { n: '01', label: '분기매출', v: '117', unit: '억', lines: ['이 곳에 위 키워드에 대한 내용을', '입력해주세요. 텍스트 박스를 더블', '클릭하여 내용을 수정할 수 있습니', '다.'] },
  rows: [{ n: '02', label: '가입자 수', v: '200', unit: '만명', lines: kpiText }, { n: '03', label: '성장률', v: '10.8', unit: '%', lines: kpiText }],
}

export const conclusion = {
  kicker: 'CONCLUSION', title: '결론 페이지', band: '이 곳에는 보고서의 결론을 기재해 주세요.',
  items: [
    ['보고할 땐 결론을 먼저 제시해 보세요.', '배경,현황, 수치 등의 구체적인 보고보다 앞 부분에 배치하는게 좋습니다.'],
    ['결론은 전체 내용을 요약하고, 보고에서 핵심이 되는 포인트를 강조합니다.', '명확하고 간결한 문장이 중요해요.'],
    ['결과를 보여주는 것 외에도, 견해나 방안을 제시하는 것 또한 잊지 마세요.', '결론에서 쓸 가장 중요한 내용입니다.'],
  ],
}

const p1 = ['이곳에 프로필을 입력해 주세요. 이곳에 프', '로필을 입력해주세요.']
const p2 = ['이곳에 프로필을 입력해', '주세요. 이곳에 프로필을', '입력해주세요.']
export const team = {
  kicker: 'PROFILE', title: '팀원 프로필',
  rows: [
    [{ name: 'CEO 준미리', lines: p1 }, { name: '김미리', lines: p2 }, { name: '최미리', lines: p2 }],
    [{ name: '팀장 최미리', lines: p1 }, { name: '이미리', lines: p2 }, { name: '성미리', lines: p2 }],
  ],
  company: 'MIRI COMPANY', foot: '*페이지 내 인물사진은 샘플이미지입니다.',
}

export const info = {
  kicker: 'ABOUT COMPANY', title: '회사 기본 정보', pin: 'MIRICOMPANY',
  items: [
    { head: 'OFFICE HOUR', lines: ['월 - 금. 10:00 - 19:00 / 토-일. 11:00 - 2:00'] },
    { head: 'COMMUNICATION', lines: ['전화. 02-123-4567 / 이메일. MIRI@COMPANY.COM', '홈페이지. MIRICOMPANY.COM / FAX. 02-123-4567'] },
    { head: 'ADDRESS', lines: ['서울특별시 미리동 미리로 미리길 12-4, 5층'] },
  ],
}

export const closing = { en: 'Thank you.', kr: '감사합니다.', mail: 'mirikim@miricanvas.com' }
