/** Content for 행궁동 동네한바퀴 (06). */

export interface ReviewLine {
  text: string
  /** Whether the line carries a highlighter stripe. */
  marked?: boolean
}

export interface Review {
  /** Top of the review block in panel px (icon + first line aligned). */
  y: number
  lines: ReviewLine[]
}

export const reviews = {
  heading: '동네한바퀴 이용소감',
  items: [
    {
      y: 191,
      lines: [
        { text: '해설가이드님이 있어서 그런지 더 재밌게 구경했어요!' },
        { text: '역사도 배우면서 다니니까 유익하고 색다른 여행이었어요.', marked: true },
      ],
    },
    {
      y: 285,
      lines: [
        { text: '구경만 하는 게 아니라, 각 장소의 역사와 이야기를 들으며' },
        { text: '다니니까 마치 시간 여행을 하는 듯한 색다른 경험이었어요.' },
        { text: '재미와 배움을 동시에 얻을 수 있어서 정말 유익한 여행이었습니다.', marked: true },
        { text: '앞으로도 이런 해설 투어가 있으면 꼭 다시 참여하고 싶어요.' },
      ],
    },
    {
      y: 409,
      lines: [
        { text: '블로그에도 없던 장소들도 알게 되어 신선했어요.' },
        { text: '한적하고 조용히 즐길 수 있었고, 여행 가이드님 덕분에 명소 알기', marked: true },
        { text: '힘든 현지 이야기까지 깊이 있게 들을 수 있었어요.', marked: true },
      ],
    },
    {
      y: 519,
      lines: [
        { text: '고즈넉하고 해설가이드님의 해설도 너무 재밌어서 즐거웠습니다.' },
        { text: '행궁동을 방문하지 않았다면 행궁동 동네한바퀴를 꼭 추천드리고', marked: true },
        { text: '싶어요! 다음에 또 행궁동 동네한바퀴 올래요!', marked: true },
      ],
    },
  ] satisfies Review[],
}

export interface TransitRoute {
  label: string
  y: number
  lines: string[]
}

export const transit = {
  heading: '행궁역 교통편 안내',
  routes: [
    { label: '※지하철 이용 시', y: 197, lines: ['8호선 행궁역 하차 후', '8번 출구로 나와 500m 도보 약5분 소요.'] },
    { label: '※버스 이용 시', y: 365, lines: ['8번 버스 탑승 후 행궁역 하차 후', '직진 500m 도보 약5분 소요.'] },
    { label: '※KTX이용 시', y: 525, lines: ['서울역에서 KTX탑승 후 행궁역 하차 후', '직진 500m 도보 약5분 소요.'] },
  ] satisfies TransitRoute[],
  contactCaption: '· 교통센터 및 관광센터 안내/문의 ·',
  contacts: [
    { name: '지역관광센터', info: '평일 오전9시 ~ 오후6시 공휴일휴무 | +123-456-7890' },
    { name: '지역교통센터', info: '평일 오전9시 ~ 오후6시 공휴일휴무 | +123-456-7890' },
    { name: '지역관광센터', info: '평일 오전9시 ~ 오후6시 공휴일휴무 | +123-456-7890' },
    { name: '지역교통센터', info: '평일 오전9시 ~ 오후6시 공휴일휴무 | +123-456-7890' },
  ],
}

export interface Box {
  x: number
  y: number
  w: number
  h: number
  rotate?: number
  label: string
}

export const cover = {
  kicker: ['동네', '가이드와', '함께하는'],
  boxed: ['행', '궁', '동'],
  title: '동네한바퀴',
  tagline: ['느리게 걷는 즐거움,', '행궁동에서 찾다.'],
  /** Dashed walking route through the stickers (panel px, SVG path). */
  route: 'M 122 214 V 252 Q 122 268 138 268 H 389 Q 405 268 405 284 V 340 Q 405 356 389 356 H 81 Q 65 356 65 372 V 620 Q 65 636 81 636 H 389 Q 405 636 405 620 V 556',
  stickers: [
    { x: 30, y: 0, w: 210, h: 108, label: 'star and circle stickers' },
    { x: 333, y: 186, w: 108, h: 106, rotate: -6, label: 'food photo' },
    { x: 290, y: 238, w: 98, h: 96, label: 'star sticker' },
    { x: 46, y: 271, w: 102, h: 108, rotate: 6, label: 'palace gate photo' },
    { x: 130, y: 306, w: 100, h: 74, label: 'camera sticker' },
    { x: 44, y: 580, w: 104, h: 108, rotate: 4, label: 'interior photo' },
    { x: 316, y: 578, w: 120, h: 112, label: 'coffee cup sticker' },
    { x: 284, y: 926, w: 196, h: 92, label: 'checkered and circle stickers' },
  ] satisfies Box[],
}

export const groupPhoto = { frame: { x: 58, y: 657, w: 360, h: 286 }, photo: { x: 75, y: 682, w: 330, h: 206 } }
