/** Facts shared by both sides of the festival brochure. */
export const festival = {
  name: ['2056', '도서관', '책축제'],
  tagline: '책으로 만나는 즐겁고 다정한 하루',
  arcTagline: '책과 만나는 즐겁고 다정한 하루',
  date: '2056.10.17(토) 10:00-17:00',
  place: '다정구 도서관 앞 광장',
  phoneDots: '02.1234.5678',
  phoneDashes: '02-1234-5678',
  website: 'www.umchungjoeun.kr',
} as const

export interface LabeledValue {
  label: string
  value: string
}
