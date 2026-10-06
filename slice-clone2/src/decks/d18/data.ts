
export const team = { no: '3', suffix: '조', line: '미리대학교 경영학과 12345678 강미리' }
export const cover = { title: ['SWOT 분석 및 조사', '[ 브랜드네임 ]'], kicker: 'BRANDNAME' }
export const closing = { title: '감사합니다', kicker: 'BRANDNAME' }

const cardBody = ['세부사항을 입력해주세요.', '폰트는 나눔스퀘어라운드', 'Regular입니다. 폰트 크기는', '18사이즈입니다. 내용은', '다섯줄 정도가 보기좋습니다.']
export type TocIcon = 'pen' | 'net' | 'rings' | 'hands'
export const toc = {
  title: 'CONTENTS', chapter: 'CHAPTER 01',
  items: ([['PLAN', 'pen'], ['ASSIGN', 'net'], ['IMPLEMENT', 'rings'], ['FEEDBACK', 'hands']] as [string, TocIcon][]).map(([label, icon]) => ({ label, icon, lines: cardBody })),
}

const swotBody = ['세부사항을 입력해주세요.', '폰트는 나눔스퀘어라운드 Regular입니다.', '폰트 크기는  18사이즈입니다. 내용은', '네줄 정도가 보기좋습니다.']
export const swot = {
  title: 'SWOT 브랜드네임', chapter: 'CHAPTER 01',
  quads: [
    { label: 'STRENGTH', right: true, cy: 218 },
    { label: 'WEAKNESS', right: false, cy: 218 },
    { label: 'OPPORTUNITY', right: true, cy: 515 },
    { label: 'THREAT', right: false, cy: 515 },
  ].map((q) => ({ ...q, lines: swotBody })),
  pieces: [
    { ch: 'S', x: 511, y: 302, k: 'pink' },
    { ch: 'W', x: 622, y: 302, k: 'navy' },
    { ch: 'O', x: 511, y: 415, k: 'navy' },
    { ch: 'T', x: 622, y: 415, k: 'pink' },
  ] as { ch: string; x: number; y: number; k: 'pink' | 'navy' }[],
  /** puzzle knobs [cx, cy, colour] */
  knobs: [
    [677, 286, 'navy'], [750, 359, 'navy'], [498, 470, 'navy'], [566, 538, 'navy'], [601, 470, 'navy'], [677, 432, 'navy'],
    [646, 358, 'pink'], [566, 432, 'pink'],
    [566, 316, 'white'], [513, 358, 'white'], [720, 470, 'white'], [677, 510, 'white'],
  ] as [number, number, 'navy' | 'pink' | 'white'][],
}

export const strength = {
  title: 'S/W 내부환경 – 강점', kicker: 'STRENGTH', chapter: 'CHAPTER 02',
  notes: [
    { label: '강점 01', x: 141, tx: 244, lines: ['세부사항을 입력해주세요. 사용한 서체는', '나눔스퀘어라운드 Regular입니다.', '폰트 크기는  20사이즈입니다.'] },
    { label: '강점 02', x: 620, tx: 726, lines: ['세부사항을 입력해주세요. 사용한 서체는', '나눔스퀘어라운드 Regular입니다.', '폰트 크기는  20사이즈입니다'] },
  ],
  points: [[132, 567, 20], [371, 523, 40], [611, 458, 70], [851, 436, 80], [1091, 393, 100]] as [number, number, number][],
  caption: '그래프 제목을 적어주세요',
}

const weakBody = ['관련된 세부사항을 입력해주세요.', '폰트는 배달의민족 주아체이며,', '22사이즈입니다. 자간은-5, 행간은 40입니다.', '내용은 세줄에서 네줄 정도가 보기좋습니다.']
export const weakness = {
  title: 'S/W 내부환경 – 약점', kicker: 'WEAKNESS', chapter: 'CHAPTER 02',
  head: '브랜드의 최대 약점은 무엇인가?',
  points: [[158, 545, 20], [294, 479, 40], [431, 378, 70], [568, 445, 50], [704, 462, 45]] as [number, number, number][],
  tag: '매출 20%감소',
  blocks: [{ label: '브랜드의 약점', cy: 324, lines: weakBody }, { label: '보완하기 위한 전략', cy: 502, lines: weakBody }],
}

const anal = ['세부사항을 입력해주세요. 사용한 서체는 나눔스퀘어라', '운드 Regular입니다. 폰트 크기는  20사이즈입니다', '그래프에 관한 상세한 내용을 입력해주셔도 좋습니다.', '이 폰트는 나눔스퀘어라운드 Regular입니다.']
export const opportunity = {
  title: 'O/T 외부환경 – 기회요인', kicker: 'OPPORTUNITY', chapter: 'CHAPTER 02',
  heads: ['주제 A에 대한 그래프', '그래프에 대한 분석'],
  note: ['2030년 기준 (단위:%)', '자료출처 : 미리대학교 정보학술관'],
  bars: [
    { label: '비교01', v: 7, top: 533, c: 'orange' },
    { label: '비교02', v: 12, top: 487, c: 'pink' },
    { label: '비교03', v: 16, top: 448, c: 'teal' },
    { label: '주제 A', v: 23, top: 382, c: 'navy' },
  ] as { label: string; v: number; top: number; c: 'orange' | 'pink' | 'teal' | 'navy' }[],
  heading: '핵심 문구를 써주세요',
  lines: [...anal, ...anal],
}

export const threat = {
  title: 'O/T 외부환경 – 위협요인', kicker: 'THREAT', chapter: 'CHAPTER 02',
  cols: ['', 'A', 'B', 'C'],
  rows: Array.from({ length: 4 }, () => ['텍스트', '텍스트를 입력하세요', '텍스트를 입력하세요', '텍스트를 입력하세요']),
  donut: [{ label: 'A업체 50%', deg: 180, c: 'navy' }, { label: 'B업체 30%', deg: 108, c: 'pink' }, { label: 'C업체 20%', deg: 72, c: 'teal' }] as { label: string; deg: number; c: 'navy' | 'pink' | 'teal' }[],
  banner: ['경쟁업체의 점유율이 작년도에 비해 ', '2배', '가 되었다.'] as const,
}

const juaLines = ['관련된 세부사항을 입력해주세요.', '그래프에 관한 상세한 내용을 입력해주셔도 좋습니다.', '이 폰트는 배달의민족 주아체이며, 사이즈는 20입니다.']
export const fourP = {
  title: '4P 전략', label: 'PLACE / PROMOTION', chapter: 'CHAPTER 03',
  blocks: [{ head: '서브타이틀을 써주세요', cy: 264, lines: juaLines }, { head: '서브타이틀을 써주세요', cy: 451, lines: juaLines }],
  caption: ['관련된 세부사항을 입력해주세요. 상단 이미지에 관한 상세한 내용을', '적어주셔도 좋습니다. 이 폰트는 나눔스퀘어라운드 Regular입니다'],
}

const refRows: [string, string][] = [
  ['단행본', '저자. (발행년). 서명. (판사항). 발행지:발행사'],
  ['학술지', '저자. (발행년). 논문명. 자료(저널)명, 권(호), 수록 면수.'],
  ['학위논문', '저자. (수여년). 논문명(학위명). 수여기관명, 소재지.'],
  ['심포지움\n자료', '저자. (년,월). 논문명. 의장(Chairperson). 심포지움명.\n심포지움 개최기관, 소재지.'],
  ['컨퍼런스\n발표 자료', '저자. (년,월). 컨퍼런스명, 소재지.'],
  ['웹자료', '참고문헌이나 자료의 출처를 적어주세요.\nhttps://miricanvas.com'],
  ['', '참고문헌이나 자료의 출처를 적어주세요.\nhttps://miricanvas.com'],
]
export const references = {
  title: '참고문헌', kicker: 'REFERENCE', chapter: 'CHAPTER 04',
  head: ['해당내용', '문헌 종류', 'REFERENCE'],
  tables: ['01. 내용을 입력하세요', '02. 내용을 입력하세요'].map((heading) => ({ heading, rows: refRows.map(([kind, ref]) => ({ item: '내용을 적어주세요', kind, ref })) })),
}

