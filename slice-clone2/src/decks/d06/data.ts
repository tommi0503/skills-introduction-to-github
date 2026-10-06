export const brand = 'MIRICANVAS'

const para8 = [
  '올바른 페이지 레이아웃을 선택하는 것은 모든 디자인',
  '프로젝트에서 중요한 요소이며 최종 결과물의 시각적',
  '매력, 가독성 및 사용성에 큰 영향을 미칠 수 있습니다.',
  '디자인의 목적과 대상에 따라 페이지 크기, 방향, 여백,',
  '열 너비, 이미지 및 기타 요소의 배치와 같은 요소를 고려',
  '해야 할 수 있습니다. 또한 정보의 계층 구조와 독자의',
  '시선을 콘텐츠에 어떻게 유도할 것인지도 고려하는 것이',
  '중요합니다.',
]
const sub = '제목을 입력해주세요.'
const extra = { title: '부가범주를 입력하세요.', lines: ['부가 설명 및 범주 1', '부가 설명 및 범주 2'] }

export const cover = { title: ['BUSINESS', 'PRESENTATION'], sub: '프리젠테이션의 소제목을 입력해주세요.', date: '2081. 5. 3' }
export const about = { title: 'About us', sub, body: para8, note: '페이지내 인물사진은 샘플 이미지입니다.', page: '02' }
export const mission = { title: 'Mission & Vision', sub, cols: [para8, para8, para8], page: '03' }

const d2 = ['연혁과 해당 부가 설명을', '공간에 입력해주세요.']
const d1 = ['연혁과 해당 부가 설명']
const d5 = ['회사가 미리캔버스를 통해', '제공하는 모든 콘텐츠 및', "'편집기'에 대한 저작권은", '국제 저작권협약에 보호받고', '있습니다.']
const e = (cy: number, desc: string[]) => ({ cy, title: '해당년도의 내용', desc })
export const timeline = {
  title: 'The Timeline',
  intro: [
    '올바른 페이지 레이아웃을 선택하는 것은 모든 디자인 프로젝트에서',
    '중요한 요소이며 최종 결과물의 시각적 매력, 가독성 및 사용성에 큰',
    '영향을 미칠 수 있습니다. 디자인의 목적과 대상에 따라 페이지 크기,',
    '방향, 여백, 열 너비, 이미지 및 기타 요소의 배치와 같은 요소를 고려해',
    '야 할 수 있습니다. 또한 정보의 계층 구조와 독자의 시선을 콘텐츠에',
    '어떻게 유도할 것인지도 고려하는 것이 중요합니다.',
  ],
  years: [
    { x: 212, year: '2081', entries: [e(443, d5)] },
    { x: 399, year: '2085', entries: [e(301, d2), e(384, d1)] },
    { x: 586, year: '2090', entries: [e(301, d2), e(384, d5), e(498, d5)] },
    { x: 772, year: '2095', entries: [e(301, d5), e(412, d2), e(497, d1)] },
    { x: 959, year: '2098', entries: [e(301, d2), e(384, d5), e(497, d2), e(582, d1)] },
  ],
  page: '04',
}

export const product = {
  title: 'Our Product',
  intro: [
    '올바른 페이지 레이아웃을 선택하는 것은 모든 디자인 프로젝트에서 중요',
    '한 요소이며 최종 결과물의 시각적 매력, 가독성 및 사용성에 큰 영향을 미',
    '칠 수 있습니다. 디자인의 목적과 대상에 따라 페이지 크기, 방향, 여백, 열',
    '너비, 이미지 및 기타 요소의 배치와 같은 요소를 고려해야 할 수 있습니다.',
    '또한 정보의 계층 구조와 독자의 시선을 콘텐츠에 어떻게 유도할 것인지도',
    '고려하는 것이 중요합니다.',
  ],
  items: [0, 1].map(() => ({ title: '제목을 입력해주세요.', desc: ['이미지에 대한 설명 또는 기타 내용을 자유롭게', '입력해주세요!'] })),
  page: '05',
}

export const pie = {
  title: ['Pie Chart', 'Content 01'],
  sub, body: para8, extra,
  chartTitle: '그래픽의 제목을 입력하세요.',
  caption: '그래픽의 부제목을 입력하세요.',
  /** clockwise from 12 o'clock, degrees */
  slices: [
    { from: 0, to: 116, c: '#383838' },
    { from: 116, to: 190, c: '#585858' },
    { from: 190, to: 252, c: '#787878' },
    { from: 252, to: 298, c: '#c2c2c2' },
    { from: 298, to: 338, c: '#dddddd' },
    { from: 338, to: 360, c: '#eeeeee' },
  ],
  bigLabels: [
    { x: 1017, cy: 321, v: '32%', d: ['해당내용과 수치를', '입력하세요.'] },
    { x: 978, cy: 466, v: '27%', d: ['해당내용과 수치를', '입력하세요.'] },
  ],
  smallLabels: [
    { x: 797, cy: 353, c: '#333' },
    { x: 826, cy: 469, c: '#eee' },
    { x: 838, cy: 268, c: '#333' },
    { x: 836, cy: 181, c: '#999' },
  ].map((l) => ({ ...l, v: '27%', d: '부가설명' })),
  page: '06',
}

export const line = {
  title: ['Line Graph', 'Content 02'],
  sub, body: para8, extra,
  chartTitle: '그래픽의 제목을 입력하세요.',
  years: ['2081', '2090', '2092', '2095', '2098', '2099'],
  xs: [735, 814, 892, 970, 1049, 1127],
  ticks: [0, 100, 200, 300, 400],
  series: [
    { c: '#555', values: [30, 70, 130, 250, 350, 400], labelC: '#555' },
    { c: '#c4c4c4', values: [30, 70, 100, 150, 190, 210], labelC: '#c4c4c4' },
  ],
  page: '07',
}

export const team = {
  title: ['Meet', 'Our Team'],
  members: [
    { x: 175, name: '김대표', role: '대표이사', en: 'Managing Director', duties: ['미리캔버스 창립', '국제 저작권협약 담당', '사진, 아이콘 개발', '미리캔버스 서비스 런칭'], motto: ['진정한 의미를 찾아', '쫓는 모험가'] },
    { x: 373, name: '김개발', role: '기술연구개발 총괄', en: 'Technology Director', duties: ['국제 저작권협약 담당', '사진, 아이콘 개발', '미리캔버스 서비스 런칭', '미리캔버스 설립'], motto: ['호기심을 잃지 않는', '마음으로', '차근차근 끝까지'] },
    { x: 571, name: '김재무', role: '재무총괄', en: 'Finance Director', duties: ['사진, 아이콘 개발', '미리캔버스 서비스 런칭', '위기관리 담당'], motto: ['사고련으로 무장한', '창의적 경영'] },
  ],
  rows: [
    { cy: 130, dept: '기획 / 개발', en: ['Development', 'Planning', 'Research'], lead: '김미리 총괄', desc: ["회사가 미리캔버스를 통해 제공하는 모든 콘텐츠 및 '편집기'에 대한 저작", '권은 회사에게 있으며저작권 법과 국제 저작권협약에 보호받고 있습니다.'] },
    { cy: 283, dept: '디자인', en: ['Branding Design', 'Product Design'], lead: '강미리 총괄', desc: ['다만 사진, 아이콘 및 텍스트의 일부는 타 저작권사로부터 미리캔버스 서', '비스에서만 사용이 가능토록 허가를 받아 제공하고 있습니다. 사용자는 회', "사의 허락없이 미리캔버스의 '편집기' 소프트웨어를 이용하여, 상업적 활", '동을 할 수 없습니다.'] },
    { cy: 430, dept: '마케팅', en: ['Marketing', 'PR'], lead: '박미리 총괄', desc: ["회사가 미리캔버스를 통해 제공하는 모든 콘텐츠 및 '편집기'에 대한 저작권", '은 회사에게 있으며저작권 법과 국제 저작권협약에 보호받고 있습니다.'] },
    { cy: 571, dept: '경영 / 투자', en: ['Business Support', 'Investment'], lead: '고미리 총괄', desc: ["사용자는 회사의 허락없이 미리캔버스의 '편집기' 소프트웨어를 이용하여,", '상업적 활동을 할 수 없습니다. 사용자는 미리캔버스에서 제공하는 템플릿', '복제 활동을 할 수 없습니다.'] },
  ],
  staff: ['홍미리', '홍미리', '홍미리', '홍미리'],
  dividers: [240, 389, 537],
  note: '* 페이지내 인물사진은 샘플 이미지입니다.',
  page: '08',
}

export const company = { name: '(주)회사명', lines: ['www.miricanvas.com', '서울 구로구 디지털로33길 27 삼성IT밸리 303호', 'miricanvas@miridih.com'], copy: '©MIRIDIH ALL RIGHTS RESERVED.' }
export const qna = { title: 'Q & A' }
export const quote = { lines: ['사람은 자본이 없어도 산을 옮길 수 있으나,', '사람이 없는 자본은 아무런 쓸 데가 없다.'], author: 'Peter Drucker' }
