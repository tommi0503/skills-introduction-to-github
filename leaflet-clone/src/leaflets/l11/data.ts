export interface Spot {
  number: string
  tag: string
  desc: string
  info: string[]
  address: string[]
  /** Card left edge inside its panel (cards are not centred on the folds). */
  x: number
  width: number
}

const address = ['123 Anywhere St., Any City,', 'ST 12345']

export const spots: Spot[] = [
  { number: '1', tag: '공원', desc: '일출과 일몰이 아름다운 공원입니다.', info: ['입장료: 무료', '관람 시간: 일출 30분 전 ~ 일몰'], address, x: 47, width: 431 },
  { number: '2', tag: '해변', desc: '드라마 촬영지로 유명한 곳입니다.', info: ['입장료: 무료', '추천 시간대: 오후 3-5시'], address, x: 17, width: 433 },
  { number: '3', tag: '공원', desc: '등산로를 따라 30분정도 걷는 코스 추천', info: ['입장료: 무료', '추천: 봄(유채꽃), 가을(억새)'], address, x: 0, width: 435 },
]

export const footer = { text: '문의 123-456-7890', panel: 1 }
