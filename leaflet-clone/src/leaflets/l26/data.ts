import type { PhotoBox } from '../shared-2627/components/Photo'

export interface Tip {
  lines: string[]
  y: number
  h: number
}

/** Panel 1 (back flap): 04 travel tips. */
export const tips = {
  number: '04',
  title: '서울 여행자를 위한 안내서',
  items: [
    { lines: ['편리한 대중교통: 서울은 지하철이 매우 잘 되어 있습니다.', '교통관련 카드를 이용하면 버스와 지하철을 편리하게 환승', '할 수 있습니다.'], y: 172, h: 93 },
    { lines: ['공공자전거 : 스마트폰 앱으로 간편하게 대여할 수 있는 따', '릉이를 타고 한강 변이나 도심을 가볍게 달려보세요.'], y: 285, h: 75 },
    { lines: ['도심 속 휴식: 청계천이나 고궁 내부 쉼터는 걷다 지친 다리', '를 쉬어가기에 가장 좋은 장소입니다.'], y: 378, h: 75 },
  ] satisfies Tip[],
  photo: { label: 'subway platform photo', x: 22, y: 480, w: 430, h: 512 } satisfies PhotoBox,
}

/** Panel 2 (middle back): quote + information. */
export const information = {
  quote: ['전통과 현대가 어우러진 매력적인 도시,', '서울에서 잊지 못할 추억을 만들어보세요.'],
  heading: 'INFORMATION',
  photo: { label: 'N Seoul Tower photo', x: 117, y: 436, w: 239, h: 422 } satisfies PhotoBox,
  contacts: ['관광안내 : http://www.umchungjoeun.kr', '관광문의 : 02-1234-5678'],
}

/** Panel 3 (front cover). */
export const cover = {
  title: ['SEOUL:', 'TRAVEL GUIDE'],
  tagline: '"낮에는 여유를, 밤에는 낭만을 만나는 곳"',
  photo: { label: 'Seoul night skyline photo', x: 18, y: 292, w: 462, h: 726 } satisfies PhotoBox,
}
