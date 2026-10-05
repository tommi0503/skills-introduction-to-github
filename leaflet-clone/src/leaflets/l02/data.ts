export interface Rect {
  x: number
  y: number
  w: number
  h: number
}

/* ---------- Panel 1 — cover ---------- */
export const coverPanel = {
  badge: 'Joyful Market',
  wordmark: { strong: 'JOYFUL', light: 'MARKET' },
  /** Upright vertical poem, columns from right to left. */
  poem: ['공간 조이풀', '함께하는', '들어요', '서로의 이야기를', '믿어요', '소통의 힘을'],
  coupon: { caption: 'MART DISCOUNT COUPON', label: '조이풀 마켓' },
}

/* ---------- Panel 2 — artist interview ---------- */
export const interviewPanel = {
  sideTitle: 'ARTIST INTERVIEW',
  sideCaption: ['JOYFULMARKET', "LET'S MAKE IT TOGETHER"],
  badge: 'Artist Interview',
  heading: ['서로의 이야기를 듣고 위로하며', '어떻게 소통하는지 경험하세요.'],
  intro: ['그림으로 세상과 소통하는 발달장애', '천재화가 유빈 작가를 소개합니다.'],
  artist: { name: 'Painter. Yubin', role: 'Developmentally disabled artist.' },
  work: { title: 'Thank You All', year: '(2034 work)' },
  body: ['유빈 작가의 2034년 대표 작품으로', '모두에게 감사합니다란 주제로 그린', '작품이다.'],
}

/* ---------- Panel 3 — testimonials ---------- */
export const testimonialsPanel = {
  heading: ['조이풀 마켓은 단순한', '쇼핑 장소 그 이상입니다.'],
  brand: { pre: 'Joy', script: 'ful', post: ' Market' },
  slogan: ['"Please', 'Join My Family"'],
  schedule: ['Every Saturday', 'From 9 AM to 5 PM'],
  badge: 'Offline',
}

export interface Bubble {
  key: string
  box: Rect
  /** Corner radius (CSS). */
  radius: string
  /** Tail triangle, bubble-local coords. */
  tail: Array<[number, number]>
  lines: string[]
  align: 'left' | 'center'
  textX: number
  textY: number
}

export const bubbles: Bubble[] = [
  {
    key: 'gift',
    box: { x: 52, y: 305, w: 263, h: 115 },
    radius: '30px',
    tail: [[240, 20], [290, 18], [255, 60]],
    lines: ['독특한 선물을 찾고 지역', '예술가를 지원할 수 있는 좋은', '장소입니다.'],
    align: 'left',
    textX: 25,
    textY: 15,
  },
  {
    key: 'shop',
    box: { x: 52, y: 443, w: 204, h: 125 },
    radius: '34px',
    tail: [[60, 100], [100, 110], [70, 150]],
    lines: ['함께 쇼핑하고 즐기는', '모습을 볼 수 있어서', '정말 좋았어요. ~'],
    align: 'left',
    textX: 25,
    textY: 20,
  },
  {
    key: 'gem',
    box: { x: 274, y: 433, w: 158, h: 152 },
    radius: '50%',
    tail: [[20, 100], [50, 130], [-4, 142]],
    lines: ['이 마켓은', '진정한 보석', '입니다. ^^'],
    align: 'center',
    textX: 0,
    textY: 32,
  },
  {
    key: 'food',
    box: { x: 185, y: 610, w: 248, h: 105 },
    radius: '30px',
    tail: [[30, 5], [0, 0], [10, 40]],
    lines: ['신선하고 건강한 음식 이', '가득해서 너무 좋았어요!'],
    align: 'center',
    textX: 0,
    textY: 18,
  },
]

export const faces: Rect[] = [
  { x: 330, y: 333, w: 95, h: 88 },
  { x: 62, y: 610, w: 98, h: 96 },
]

/* ---------- Panel 4 — programme ---------- */
export const programPanel = {
  badge: 'Joyful Market',
  intro: ['시장 입구에 위치한 웰컴 부스에서 스티커를', '받아 모험을 시작해 보세요.'],
  stamp: ['JOYFUL', 'MARKET'],
  chips: [['조이풀 마켓에는', '공연도', '나눔도'], ['웃음까지', '가득합니다.']],
  sections: [
    {
      title: '공연일정',
      highlight: '매주 토요일 12시부터 3시까지',
      lines: ['이곳은 라이브 공연과 매력적인 경험을 즐길', '수 있는 활기찬 커뮤니티 허브입니다.'],
    },
    {
      title: '나눔 이벤트',
      highlight: '공동체의 힘과 나눔의 기쁨을 함께해요!',
      lines: ['따뜻한 마음으로 참여해 주세요.'],
    },
  ],
  contacts: ['문의 : 1533-5678', '이메일 : share@joy.com'],
}

/** 3×2 grid of round thumbnails: photo or stamp. */
export const thumbs: Array<'photo' | 'stamp'> = ['photo', 'photo', 'photo', 'photo', 'stamp', 'stamp']
