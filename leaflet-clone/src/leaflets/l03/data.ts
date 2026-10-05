export interface ChecklistItem {
  lines: string[]
  y: number
  textOffset?: number
}

export const checklist = {
  title: ['플리마켓 방문 시', '체크리스트!'],
  /** y = icon top (panel px); textOffset = first-line drop for multi-line items. */
  items: [
    { lines: ['일회용품을 쓰지 않아요'], y: 378 },
    { lines: ['장바구니를 챙겨주세요'], y: 482 },
    { lines: ['애견과 방문 시 목줄을', '꼭 챙겨주세요'], y: 578, textOffset: 32 },
  ] as ChecklistItem[],
}

export const directions = {
  title: '찾아오시는길',
  blocks: [
    ['주소', '서울 마포구 서교동 702-29,', '망원한강공원 자유지구 공터'],
    ['버스 - 137번 마포로 정류장 하차', '지하철 - 망원역 하차 후 도보 10분'],
  ],
  sns: ['우리 마을 플리마켓 SNS를', '구독해주세요!'],
  account: ['인스타그램', '@woorimaeulfleemarket'],
}

export const cover = {
  tag: '우리동네 나눔의 장',
  title: ['동그라미', '플리마켓'],
  info: ['망원한강공원 자유지구 공터', '4월~6월 매주 일요일', '오전 10시~오후 5시'],
  categories: ['의류', '수제 간식', '중고 용품', '무료 나눔'],
}

export interface Box {
  label: string
  x: number
  y: number
  w: number
  h: number
  radius?: string
}

/** Goods illustrations on the cover (panel coords) → placeholders. */
export const goods: Box[] = [
  { label: 'cookies', x: 60, y: 368, w: 130, h: 116, radius: '50%' },
  { label: 'cupcake', x: 197, y: 420, w: 92, h: 112, radius: '40% 40% 12px 12px' },
  { label: 'bag', x: 312, y: 380, w: 100, h: 148, radius: '30% 30% 10px 10px' },
  { label: 'sweater', x: 88, y: 530, w: 164, h: 150, radius: '30px' },
  { label: 'socks', x: 268, y: 548, w: 124, h: 132, radius: '30px' },
]
