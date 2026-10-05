import type { ShapeSpec } from '../shared-0812'

export interface Activity {
  title: string
  desc: string[]
}

export interface InfoRow {
  label: string
  value: string
}

export const joinPanel = {
  title: '함께해 주세요',
  subtitle: '다양한 방법으로 함께재단과 함께할 수 있어요.',
  activities: [
    { title: '참여하기', desc: ['지역 프로그램과 행사에 직접 참여해 보세요.'] },
    { title: '나누기', desc: ['시간과 재능, 물품으로 마음을 나눠주세요.'] },
    { title: '함께하기', desc: ['지역의 다양한 기관과 단체가 되어주세요.'] },
  ] satisfies Activity[],
  firstTime: {
    title: '처음 참여하기',
    desc: ['처음이라 낯설어도 괜찮아요!', '매월 첫째 주 토요일, 오리엔테이션에서', '편하게 안내 해드려요'],
  } satisfies Activity,
  art: [
    { x: 200, y: 100, w: 78, h: 50, radius: '40% 40% 50% 50%', label: 'heart mascot' },
    { x: 0, y: 246, w: 124, h: 96, radius: '0 48px 48px 0', label: 'blue mascot' },
  ] satisfies ShapeSpec[],
}

export const thanksPanel = {
  title: '감사합니다',
  body: [
    '함께재단은 이웃과 이웃 사이의 다정한 연결을 만듭니다.',
    '작은 관심 이 모여 우리 동네를 조금씩, 그러나 꾸준히',
    '따뜻하게 바꾸고 있어 요.',
  ],
  info: [
    { label: '운영시간', value: '평일 09:00~18:00 주말/공휴일 휴무' },
    { label: '주소', value: '서울특별시 다정구 상상로 77 희망빌딩 1층 00031' },
    { label: '전화', value: '02-1234-5678' },
    { label: '이메일', value: 'dream@canvakorea.co.kr' },
    { label: '웹사이트', value: 'http://www.umchungjoeun.kr' },
  ] satisfies InfoRow[],
  cta: { lines: ['지금,', '우리 함께 해요!'], note: 'QR 코드로 모바일 접속하세요!' },
  art: [
    { x: 137, y: 119, w: 84, h: 84, clip: 'polygon(30% 0,70% 0,100% 30%,100% 70%,70% 100%,30% 100%,0 70%,0 30%)', label: 'octagon mascot' },
    { x: 183, y: 95, w: 46, h: 46, radius: '50%', label: 'star mascot' },
    { x: 226, y: 80, w: 112, h: 128, radius: '50% 50% 40% 40%', label: 'yellow mascot' },
    { x: 325, y: 785, w: 132, h: 72, radius: '66px 66px 0 0', label: 'pink mascot' },
  ] satisfies ShapeSpec[],
}

export const coverPanel = {
  handle: '@dreamcanvakorea',
  arc: '함께 만드는 변화',
  title: ['우리동네', '함께재단'],
  tagline: ['이웃과 이웃을 잇는', '다정한 연결을 만들어갑니다.'],
  art: [
    { x: 212, y: 652, w: 60, h: 50, radius: '50% 50% 50% 50% / 40% 40% 60% 60%', label: 'heart' },
    { x: 50, y: 705, w: 138, h: 138, radius: '50%', label: 'blue mascot' },
    { x: 70, y: 840, w: 110, h: 42, radius: 12, label: 'blue mascot legs' },
    { x: 190, y: 736, w: 103, h: 146, label: 'green mascot' },
    { x: 285, y: 670, w: 133, h: 212, clip: 'polygon(20% 8%,62% 0,100% 50%,60% 100%,0 55%)', label: 'orange mascot' },
  ] satisfies ShapeSpec[],
}
