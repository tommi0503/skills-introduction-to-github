export const nav = [['Miri Electronics'], ['Company', 'Introduction'], ['Business', 'Performance'], ['Performance', 'by field'], ['Environment'], ['Contact']]
export const cover = { title: ['A JOURNEY TOWARDS', 'A SUSTAINABLE', 'FUTURE'], sub: '(주)미리전자 지속가능경영보고서 2039' }

const tocBody = ['해당 목차에 관련된 내용을 간략하게', '작성해주세요. 폰트는 프리텐다드', 'Light입니다. 폰트 크기는 14pt이고', '행간은 1.5로 설정해주시면 좋습니다.']
export const toc = {
  label: 'Sustainability Report', title: ['Table of', 'Contents'],
  cols: [
    { n: '01', label: ['Company', 'Introduction'], bottom: 522 },
    { n: '02', label: ['Business', 'Performance'], bottom: 468 },
    { n: '03', label: ['Performance', 'by field'], bottom: 468 },
    { n: '04', label: ['-', 'Environment'], bottom: 413 },
    { n: '05', label: ['-', 'Contact'], bottom: 359 },
  ].map((c) => ({ ...c, body: tocBody })),
  xs: [40, 281, 520, 760, 999, 1238],
}

export const intro = { label: 'Company Introduction', no: '01', name: 'Miri Electronics', sub: '기업 소개에 관련된 내용을 간략하게 작성해주세요. 폰트는 Noto Sans CJK KR Thin이고 폰트 크기는 22pt입니다.' }

export const ceo = {
  title: ['CEO', '인사말'], quote: '" 인사말에 관련된 한마디를 작성해주세요. "',
  body: [
    '인사말에 관련된 내용 및 자유롭게 작성해주세요. 폰트는 프리텐다드 Light 입니다. 폰트 크기는 18pt',
    '이고 행간은 1.6으로 맞춰 설정해주시면 좋습니다. 인사말에 관련된 내용 및 자유롭게 작성해 주세요.',
    '폰트는 프리텐다드 Light입니다. 폰트 크기는 18pt이고 행간은1.6로 맞춰 설정해주시면 좋습니다.',
    '인사말에 관련된 내용 및 자유롭게 작성해주세요. 폰트는 프리텐다드 Light 입니다. 폰트 크기는 18pt',
    '이고 행간은 1.6로 맞춰 설정해주시면 좋습니다.',
  ],
  sign: ['미리전자', '대표이사'],
  goals: ['01', '02', '03'].map((n) => ({ n, head: ['사업 목표나 강조하고 싶은', '주제를 작성해주세요.'], body: ['해당 관련된 내용 및 자유롭게', '작성해 주세요. 폰트는 프리텐', '다드 Light입니다.'] })),
}

export const company = {
  title: ['회사', '소개'],
  rows: [['회사명', '미리전자'], ['대표이사', '강미리 회장, 정미리 사장'], ['자본금', '000,000,000 원'], ['임직원수', '000 명'], ['본사', '본사시 본사구 본사동 12길 34'], ['설립일', '20XX.00.00'], ['사업내용', '사업내용에 대해 작성해주세요.'], ['생산제품', '생산제품에 대해 작성해주세요.']],
  quote: '" 비전이나 핵심가치에 대한 내용을 간략하게 작성해주세요. "',
  keywords: ['Keyword 01', 'Keyword 02', 'Keyword 03'],
  philosophy: '경영이념에 대한 내용을 간략하게 작성해주세요.',
  body: ['회사 소개 관련된 내용 및 자유롭게 작성해주세요. 폰트는 프리텐다드 Light입니다.', '폰트 크기는 18pt이고 행간은 1.7로 맞춰 설정해주시면 좋습니다. 회사 소개 관련된', '내용 및 자유롭게 작성해주세요. 폰트는 프리텐다드 Light입니다. 폰트 크기는 18pt', '이고 행간은 1.7로 맞춰 설정해주시면 좋습니다.'],
  last: '회사 소개 관련된 내용 및 자유롭게 작성해주세요. 폰트는 프리텐다드 Light입니다.',
}

const amt = (light: boolean) => (light ? '12,345,678' : '24,691,356')
export const sales = {
  title: ['사업부문별', '현황'], sub: '2039 글로벌 매출현황', unit: '(단위 : 백만 원, 연결재무제표기준)',
  share: [['국내64%', 144, 415], ['국내36%', 415, 568]] as [string, number, number][],
  groups: [{ label: '매출액', cy: 327 }, { label: '영업 이익', cy: 420 }].map((g) => ({ ...g, rows: [{ year: '2020년도', w: 147, v: amt(true), light: true }, { year: '2039년도', w: 295, v: amt(false), light: false }] })),
  divisions: [['CE부문', '생활가전 사업'], ['IM부문', '네트워크 사업'], ['DS부문', '반도체 사업']],
  product: '해당 주요 제품군을 작성해주세요.',
  table: {
    head: '매출액 (단위 : 백만 원, 연결재무제표기준)',
    rows: ['한국 (KOREA)', '일본 (JAPAN)', '중국 (CHAINA)', '유럽 (EUROPE)', '미국 (USA)', '멕시코 (MEXICO)', '중남미 (LATIN AMERICA)', '아프리카 (AFRICA)', '동남아시아 (SOUTHEAST ASIA)'].map((r) => [r, '12,345,678', '34,567,890']),
    total: ['합계', '111,111,102', '311,111,010'],
  },
}

type Region = { name: string; x: number; cy: number; values: number[]; path: [number, number][] }
export const network = {
  title: ['비즈니스', '네트워크'],
  table: { head: ['구분', '합계'], a: [['판매거점', '48'], ['생산거점', '26'], ['R&D 센터', '28'], ['디자인 센터', '9'], ['기타', '111']], b: [['임직원', '246,820 명'], ['협력회사', '16750 개'], ['진출국가', '52개국'], ['연구개발비', '18.5조 원']] },
  kinds: ['판매거점 .........', '생산거점 .........', 'R&D센터 .........', '디자인 센터 ......'],
  regions: [
    { name: '북미', x: 305, cy: 261, values: [8, 2, 4, 2], path: [[343, 261], [443, 261], [443, 352]] },
    { name: '유럽', x: 714, cy: 261, values: [7, 1, 5, 1], path: [[706, 261], [688, 261], [688, 328]] },
    { name: '중국', x: 920, cy: 261, values: [6, 5, 4, 1], path: [[912, 261], [893, 261], [893, 352]] },
    { name: '한국', x: 1125, cy: 261, values: [12, 2, 3, 2], path: [[1117, 261], [1049, 261], [1049, 357]] },
    { name: '일본', x: 1125, cy: 413, values: [4, 1, 3, 1], path: [[1117, 413], [1072, 413], [1072, 377]] },
    { name: '중남미', x: 305, cy: 566, values: [4, 4, 3, 1], path: [[357, 566], [448, 566], [448, 540], [538, 540]] },
    { name: '아프리카', x: 714, cy: 566, values: [2, 5, 1, 0], path: [[706, 566], [677, 566], [677, 470]] },
    { name: '서남아시아', x: 920, cy: 566, values: [2, 2, 2, 1], path: [[912, 566], [905, 566], [905, 437]] },
    { name: '동남아시아', x: 1125, cy: 566, values: [3, 4, 3, 0], path: [[1117, 566], [1053, 566], [1053, 530], [990, 530], [990, 480]] },
  ] as Region[],
  pins: [[443, 362], [688, 337], [893, 362], [1049, 367], [1072, 367], [677, 457], [905, 424], [990, 468], [552, 540]] as [number, number][],
}

export const field = {
  title: ['분야별', '실적'], sub: '사업부문별 매출실적', unit: '(단위 : 백만 원, 연결재무제표기준)',
  big: '12,345,678+', bigDesc: ['CE부문 매출현황에 대해 간략하게 작성해 주세요. 폰트는 프리텐다드 Medium입니다. 폰트 크기는 15', 'pt이고 행간은 1.5로 맞춰 설정해주시면 좋습니다. CE부문 매출현황에 대해 간략하게 작성해 주세요.'],
  rows: [{ v: '1,234,567+', cy: 513, desc: ['IM부문 매출현황에 대해 간략하게 작성해', '주세요. 폰트는 프리텐다드 Medium입니다.'] }, { v: '2,345,678+', cy: 641, desc: ['DS부문 매출현황에 대해 간략하게 작성해', '주세요. 폰트는 프리텐다드 Medium입니다.'] }],
  kpis: [
    { label: 'KPI', v: '57', unit: '%', x: 666, y: 215, w: 275 },
    { label: '신상품', v: '62', x: 961, y: 215, w: 276 },
    { label: '협력사', v: '45', x: 666, y: 374, w: 275, navy: true },
    { label: '매출 증가', v: '70', unit: '%', x: 961, y: 374, w: 276 },
    { label: '총 고객수', v: '5,000,000', x: 666, y: 533, w: 571 },
  ] as { label: string; v: string; unit?: string; x: number; y: number; w: number; navy?: boolean }[],
}

export const env = {
  title: '환경',
  cols: [
    { head: '에너지 효율', x: 42, lines: ['에너지 효율과 관련된 내용을 작성해 주세요. 폰트는 프리텐다드', 'Medium입니다. 폰트 크기는 16pt이고 행간은 1.5입니다. 에너지', '효율과 관련된 내용을 작성해 주세요. 폰트는 프리텐다드 Medium', '입니다. 폰트 크기는 16pt이고 행간은 1.5입니다.'], note: '(에너지 효율과 관련된 부가 설명을 간략하게 작성해 주세요.)' },
    { head: '관리 체계', x: 457, lines: ['관리 체계와 관련된 내용을 작성해 주세요. 폰트는 프리텐다드', 'Medium입니다. 폰트 크기는 16pt이고 행간은 1.5입니다. 관리', '체계와 관련된 내용을 작성해 주세요. 폰트는 프리텐다드 Medium', '입니다. 폰트 크기는 16pt이고 행간은 1.5입니다. 관리체계와', '관련된 내용을 작성해 주세요. 폰트는 프리텐다드 Medium입니다.'] },
  ],
  tech: { head: '환경 보호 기술 현황', sub: '온실가스 누적 감축량', unit: '(단위 : 백만 톤, CO₂eq)', bars: [{ year: '2020년', a: 27, b: 254, w: 214, cy: 288 }, { year: '2039년', a: 35, b: 320, w: 298, cy: 327 }] },
  strategy: {
    head: '대응전략',
    p1: ['대응 전략과 관련된 내용을 작성해 주세요. 폰트는 프리텐다드', 'Medium입니다. 폰트 크기는 16pt이고 행간은 1.5입니다. 대응', '전략과 관련된 내용을 작성해 주세요. 폰트는 프리텐다드 Medium', '입니다. 폰트 크기는 16pt이고 행간은 1.5입니다. 대응 전략과', '관련된 내용을 작성해 주세요. 폰트는 프리텐다드 Medium입니다.', '대응 전략과 관련된 내용을 작성해 주세요. 폰트는 프리텐다드', 'Medium입니다. 폰트 크기는 16pt이고 행간은 1.5입니다.'],
    p2: ['대응 전략과 관련된 내용을 작성해 주세요. 폰트는 프리텐다드', 'Medium입니다. 폰트 크기는 16pt이고 행간은 1.5입니다. 대응', '전략과 관련된 내용을 작성해 주세요.'],
    note: '(대응 전략과 관련된 부가 설명을 간략하게 작성해 주세요.)',
  },
  ring: '관리체계',
  keywords: [1, 2, 3].map((n) => ({ title: `Keyword 0${n}`, lines: ['해당 키워드와 관련된 내용을 작성해 주세요. 폰트는 프리텐다드', 'Medium입니다. 폰트 크기는 16pt이고 행간은 1.45입니다.'] })),
}

export type ContactIcon = 'mail' | 'phone' | 'home'
export const contact = {
  title: 'Thank you',
  rows: [{ icon: 'mail', lines: ['mirielectronics@dih.com'], cy: 556 }, { icon: 'phone', lines: ['02.1234.5678'], cy: 596 }, { icon: 'home', lines: ['https://www.mirielectronics.com', '미리시 미리구 미리로 12길 34 미리전자'], cy: 634 }] as { icon: ContactIcon; lines: string[]; cy: number }[],
}
