import { theme } from './theme'

export interface ProgramButton {
  label: string
  fill: string
}

export const programs = {
  title: '기부 프로그램',
  note: ['*기부금 영수증 발급이 가능하며', '세제 혜택을 받으실 수 있습니다.'],
  buttons: [
    { label: '정기 기부', fill: theme.green },
    { label: '일시 기부', fill: theme.yellow },
    { label: '단체 기부', fill: theme.green },
    { label: '아동 · 청소년 결연 1:1 기부', fill: theme.yellow },
  ] satisfies ProgramButton[],
}

export interface InfoSection {
  heading: string
  lines: string[]
}

export const donationInfo: InfoSection[] = [
  { heading: '기부 방법', lines: ['웹사이트를 통해 정기/일시 기부', '아래 계좌를 통해 직접 후원'] },
  { heading: '계좌번호', lines: ['우영은행 (사) 아동권리실천협회', '1000-888-333333'] },
]

export const message = {
  paragraphs: [
    ['아동·청소년이', '우리의 미래입니다.'],
    ['미래를 키우는', '동행자가 되어주세요.'],
  ],
  cta: '후원하기',
}

export const contacts = [
  { key: 'addr', label: '주소', value: '서울 강남구 삼성로 7 명보빌딩 13층' },
  { key: 'web', label: '웹사이트', value: 'umchungjoeun.kr' },
  { key: 'mail', label: '이메일', value: 'dream@canvakorea.co.kr' },
  { key: 'tel', label: '전화', value: '03-987-1533' },
]

export const cover = {
  kicker: '아동·청소년 동행 기부 캠페인',
  title: ['미래를', '키우는', '특별한', '나눔'],
  org: '아동 권리 실천 협회',
}

/** Decorative bird illustrations (panel 2 coords) → placeholders. */
export const birds = [
  { x: 332, y: 37, w: 68, h: 51 },
  { x: 425, y: 47, w: 50, h: 71 },
  { x: 353, y: 100, w: 97, h: 72 },
  { x: 39, y: 378, w: 67, h: 50 },
]
