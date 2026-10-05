import type { PhotoBox } from '../shared-2627/components/Photo'

export interface Paragraph {
  lines: string[]
  x: number
  y: number
  w: number
  h: number
  /** Grey card behind the text (some paragraphs sit on bare paper). */
  card?: boolean
}

export const history = {
  number: '01',
  title: '과거와 미래가 공존하는 도시, 서울',
  photo: { label: 'Bukchon hanok alley photo', x: 38, y: 247, w: 417, h: 520, archRise: 150 } satisfies PhotoBox,
  text: {
    lines: [
      '600년의 역사를 품은 고궁의 고즈넉함과 세계에서 가장 트',
      '렌디한 도심의 활기가 공존하는 곳, 서울에 오신 것을 환영',
      '합니다. 빌딩 숲 사이 숨겨진 골목길을 걷고, 푸른 한강 변',
      '에서 여유를 만끽하며 당신만의 특별한 서울을 발견해 보세',
      '요.',
    ],
    x: 38,
    y: 800,
    w: 417,
    h: 165,
  } satisfies Paragraph,
}

export const tradition = {
  number: '02',
  title: '햇살 아래 빛나는 서울의 전통',
  texts: [
    { lines: ['경복궁 & 한옥마을: 고운 한복을 입고 조선 시대 고궁과 전', '통 한옥 골목을 거닐며 인생 사진을 남겨보세요.'], x: 35, y: 242, w: 420, h: 80 },
    { lines: ['성수동 카페거리: 붉은 벽돌 건물 사이로 감성적인 팝업스', '토어와 트렌디한 카페들이 가득한 서울에서 가장 핫한 동', '네를 탐방합니다.'], x: 35, y: 880, w: 420, h: 92, card: false },
  ] satisfies Paragraph[],
  photos: [
    { label: 'Gyeonghoeru pavilion photo', x: 35, y: 348, w: 420, h: 249 },
    { label: 'hanbok in palace corridor photo', x: 35, y: 612, w: 420, h: 261 },
  ] satisfies PhotoBox[],
}

export const night = {
  number: '03',
  title: '반짝이는 서울의 로맨틱한 밤',
  texts: [
    { lines: ['한강공원 피크닉 & 라면: 노을이 질 때 돗자리를 펴고 앉아,', '강바람을 맞으며 먹는 따끈한 즉석 라면의 매력에 빠져보세', '요.'], x: 33, y: 490, w: 429, h: 108 },
    { lines: ['남산타워 야경: 남산 정상에서 내려다보는 서울 도심의 환', '상적인 파노라마 불빛은 놓칠 수 없는 서울의 하이라이트입', '니다.'], x: 33, y: 607, w: 429, h: 106, card: false },
  ] satisfies Paragraph[],
  photos: [
    { label: 'Han river bridge at night photo', x: 30, y: 52, w: 432, h: 314 },
    { label: 'Namsan at dusk photo', x: 30, y: 720, w: 432, h: 245 },
  ] satisfies PhotoBox[],
}
