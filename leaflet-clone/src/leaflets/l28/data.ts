import type { Artwork } from '../shared-2829/components/ArtworkLayer'
import { autumn } from '../shared-2829/theme'

export interface InfoRow {
  tag: string
  lines: string[]
}

/** Panel 1 — festival overview. */
export const overview = {
  kicker: '주차 및 셔틀버스',
  title: '가을 꽃 축제',
  paragraph: [
    '가을 꽃 축제는 튤립동에서 열리며, 다양한 음악 공연과 예',
    '술 퍼포먼스로 모든 연령대가 즐길 수 있는 특별한 경험을',
    '제공합니다. 튤립 해안공원의 버스킹 무대는 자연과 음악',
    '이 어우러져 환상적인 분위기를 자아내며, 방문객들에게',
    '잊지 못할 추억을 선사합니다.',
  ],
  rows: [
    { tag: '일시', lines: ['2079. 10. 18~10.21 (금~일)', '14:00 - 20:00'] },
    { tag: '장소', lines: ['튤립동 튤립광장 야외무대 및', '튤립 해안공원 일대 버스킹 무대'] },
    { tag: '관람료', lines: ['무료'] },
    { tag: '장르', lines: ['어쿠스틱, 밴드, 보컬, 퍼포먼스 종합'] },
  ] satisfies InfoRow[],
}

export interface Booth {
  label: string
  x: number
  y: number
  w: number
  h: number
  fill: string
  text: string
  size: number
}

/** Booth layout diagram (coordinates inside the white card). */
export const boothMap = {
  title: '부스 배치도',
  booths: [
    { label: '무대', x: 95, y: 37, w: 162, h: 58, fill: '#ecd377', text: '#4d3b2c', size: 20 },
    { label: '전시부스', x: 22, y: 114, w: 78, h: 54, fill: '#e2dcab', text: '#3f3a2e', size: 15 },
    { label: '전시부스', x: 22, y: 189, w: 78, h: 54, fill: '#e2dcab', text: '#3f3a2e', size: 15 },
    { label: '관람객석', x: 120, y: 112, w: 115, h: 130, fill: '#eec7c1', text: '#4c3f63', size: 22 },
    { label: '푸드트럭', x: 253, y: 114, w: 78, h: 54, fill: '#eea547', text: '#5a3a1e', size: 15 },
    { label: '운영본부', x: 253, y: 189, w: 78, h: 54, fill: '#56a062', text: '#ffffff', size: 15 },
  ] satisfies Booth[],
}

export interface Road {
  x: number
  y: number
  w: number
  h: number
}

/** Panel 2 — simple road diagram made of rounded bars (panel coordinates). */
export const directions = {
  title: '오시는 길',
  roads: [
    { x: 57, y: 167, w: 363, h: 18 },
    { x: 95, y: 175, w: 11, h: 185 },
    { x: 191, y: 175, w: 11, h: 185 },
    { x: 324, y: 175, w: 11, h: 185 },
    { x: 381, y: 175, w: 11, h: 185 },
    { x: 95, y: 232, w: 240, h: 9 },
    { x: 324, y: 272, w: 68, h: 10 },
    { x: 95, y: 319, w: 240, h: 11 },
  ] satisfies Road[],
  marker: { x: 286, y: 262, label: '가을 꽃 축제장', labelX: 317, labelY: 302 },
  transit: [
    { icon: 'bus', lines: ['버스 31, 49, 100-1, 1003', '튤립 정류장 (031400) 하차 / 도보 3분 소요'] },
    { icon: 'subway', lines: ['지하철 튤립역 2번 출구 / 도보 8분'] },
  ] as const,
  rows: [
    { tag: '셔틀버스', lines: ['11:00 12:00 13:00 14:00', '15:00 16:00 17:00 18:00'] },
    { tag: '주차안내', lines: ['공연장 근처 공영 주차장', '10분 2000원 (문의. 02-1234-5678)'] },
    { tag: '문의', lines: ['콘서트 운영 사무국', '02-1234-5678  /', 'dream@canvakorea.co.kr'] },
  ] satisfies InfoRow[],
  credits: [
    { label: '주최, 주관', lines: ['(주)심플앤클리어 광고기획'] },
    { label: '후원', lines: ['더 니플라스 호텔, 메아리 편의점, 이쿠자', '지혜 생명 보험, 햄버거 애비뉴'] },
  ],
}

/** Panel 3 — cover. */
export const cover = {
  edition: '제14회',
  words: ['가을', '꽃', '축제'],
  dates: [
    { date: '10. 18.', day: '금' },
    { date: '10. 21.', day: '일' },
  ],
  address: '튤립시 튤립구 튤립동 00번지 일원',
}

const leaf = '45% 55% 50% 50% / 55% 45% 55% 45%'

/** Artwork in sheet coordinates (hills, leaves, acorns, people) → placeholders. */
export const artwork: Artwork[] = [
  {
    label: 'autumn hills',
    x: 0,
    y: 728,
    w: 1440,
    h: 290,
    clipPath:
      'polygon(0 2px, 80px 0, 440px 30px, 560px 50px, 660px 69px, 880px 125px, 960px 142px, 1100px 152px, 1200px 150px, 1300px 138px, 1440px 136px, 1440px 290px, 0 290px)',
  },
  { label: 'leaf top-left', x: 14, y: 0, w: 72, h: 80, radius: leaf, rotate: -20 },
  { label: 'leaves top cluster', x: 905, y: 0, w: 108, h: 190, radius: '40% 50% 45% 55%' },
  { label: 'leaves top cluster 2', x: 1010, y: 10, w: 105, h: 180, radius: '45% 50% 50% 45%' },
  { label: 'acorns', x: 1310, y: 35, w: 92, h: 85, radius: '45%' },
  { label: 'blue leaf', x: 963, y: 342, w: 88, h: 94, radius: leaf, rotate: 20 },
  { label: 'flower', x: 1125, y: 318, w: 162, h: 152, radius: '46%' },
  { label: 'leaf branch right', x: 1338, y: 432, w: 102, h: 118, radius: '45% 0 0 50%' },
  { label: 'big orange leaf', x: 880, y: 780, w: 120, h: 238, radius: '50% 50% 0 0' },
  { label: 'big red leaf', x: 1012, y: 878, w: 170, h: 140, radius: '50% 50% 0 0' },
  { label: 'family walking', x: 1247, y: 797, w: 155, h: 165, radius: '40% 40% 8px 8px' },
]

export const colors = { pill: autumn.olive, tag: autumn.orange }
