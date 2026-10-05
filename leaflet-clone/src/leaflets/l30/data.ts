import type { Artwork } from '../shared-3031/components/ArtworkLayer'

export interface AudienceCard {
  key: string
  heading: string[]
  body: string[]
  /** Card box (panel coordinates). */
  box: { x: number; y: number; w: number; h: number }
  /** Text block origin (panel coordinates). */
  text: { x: number; y: number }
  /** Character illustration placeholder (panel coordinates). */
  figure: Artwork
}

/** Panel 1 — who the programme is for. */
export const audience = {
  title: ['이런 분들을 위한', '사업입니다'],
  cards: [
    {
      key: 'ceo',
      heading: ['창업 및 사업 확장을', '준비하는 대표님'],
      body: ['새로운 아이디어를 현실화하고', '성장 기반을 마련하고 싶은 기업', '에게 기회를 제공합니다.'],
      box: { x: 110, y: 320, w: 330, h: 160 },
      text: { x: 221, y: 333 },
      figure: { label: 'business owner illustration', x: 50, y: 275, w: 156, h: 205, radius: '45% 45% 6px 6px / 30% 30% 6px 6px' },
    },
    {
      key: 'owner',
      heading: ['경쟁력 강화를 원하는', '소상공인'],
      body: ['마케팅, 운영 개선, 성장을', '위한 지원이 필요한 분에게', '체계적인 지원을 제공합니다.'],
      box: { x: 70, y: 520, w: 370, h: 167 },
      text: { x: 100, y: 544 },
      figure: { label: 'shop owner illustration', x: 280, y: 507, w: 168, h: 180, radius: '40% 40% 6px 6px / 30% 30% 6px 6px' },
    },
    {
      key: 'founder',
      heading: ['새로운 도전을 준비하는', '예비 창업자'],
      body: ['창업 과정에 필요한 정보와 전문', '지원을 받고 싶은 분에게 전문가', '의 지원을 제공합니다.'],
      box: { x: 110, y: 737, w: 330, h: 160 },
      text: { x: 221, y: 754 },
      figure: { label: 'founder illustration', x: 52, y: 717, w: 156, h: 180, radius: '45% 45% 6px 6px / 30% 30% 6px 6px' },
    },
  ] satisfies AudienceCard[],
}

/** Panel 2 — back cover contact. */
export const contact = {
  heading: '지원센터',
  lines: ['+82-2-1234-5678', 'dream@canvakorea.co.kr', 'www.umchungjoeun.kr'],
}

/** Panel 3 — cover. */
export const cover = {
  badge: '함께 성장하는 기회',
  title: ['지역 성장', '지원사업'],
  intro: ['본 사업은 성장 가능성을 가진 기업', '및 소상공인을 대상으로 경쟁력 강화와', '안정적인 사업 운영을 지원합니다.'],
  /** Office worker + desk illustration (panel coordinates). */
  figure: {
    label: 'office worker at desk illustration',
    x: 0,
    y: 520,
    w: 480,
    h: 498,
    clipPath:
      'polygon(165px 70px, 180px 25px, 215px 3px, 262px 0, 292px 30px, 302px 90px, 290px 145px, 330px 200px, 432px 195px, 420px 330px, 480px 370px, 480px 498px, 0 498px, 0 410px, 38px 380px, 40px 190px, 80px 175px, 130px 140px, 160px 118px)',
  } satisfies Artwork,
}
