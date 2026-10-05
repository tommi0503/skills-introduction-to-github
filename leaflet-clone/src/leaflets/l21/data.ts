import type { CardInsets } from '../shared-2021/components/CardSheet'

export const cards: CardInsets[] = [
  { left: 34, top: 24, right: 29, bottom: 29 },
  { left: 41, top: 24, right: 36, bottom: 29 },
  { left: 47, top: 24, right: 37, bottom: 29 },
]

export interface CourseSession {
  period: string
  deadline: string
}

export interface CourseRow {
  id: string
  name: string
  sessions: CourseSession[]
}

const session: CourseSession = { period: '9.4~10.15', deadline: '(접수마감 ~8.31)' }

export interface InfoItem {
  label: string
  value: string
}

export const curriculumPanel = {
  heading: '교육과정',
  tableTitle: '2046년 하반기 강좌',
  rows: [
    { id: 'phone', name: '스마트폰 기초', sessions: [session, session] },
    { id: 'video', name: '영상 편집 기초', sessions: [session, session] },
    { id: 'kiosk', name: '키오스크 정복', sessions: [session, session] },
    { id: 'ai', name: 'AI활용 기초', sessions: [session, session] },
    { id: 'pc', name: '컴퓨터 기초', sessions: [session, session] },
  ] satisfies CourseRow[],
  info: [
    { label: '신청 대상', value: '튤립구 거주중인 50대 이상 주민' },
    { label: '비용', value: '전액 무료' },
    { label: '준비물', value: '개인 스마트폰, 필기구' },
    { label: '신청 마감', value: '각 강좌별 선착순 20명' },
  ] satisfies InfoItem[],
  notice: '문의 사항은 뒷장을 참고해주십시오',
}

export interface AudienceWish {
  id: string
  /** Side the bubble sits on; the illustration takes the other side. */
  side: 'left' | 'right'
  lines: string[]
  illustration: string
}

export const audiencePanel = {
  heading: '수강대상',
  wishes: [
    { id: 'phone', side: 'left', lines: ['스마트폰을 조금 더', '잘 사용하고 싶어요.'], illustration: 'woman taking a photo' },
    { id: 'kiosk', side: 'right', lines: ['무인 키오스크 사용,', '너무 어려워요!'], illustration: 'kiosk' },
    { id: 'video', side: 'left', lines: ['영상을 찍어서', '편집도 해보고 싶어요'], illustration: 'man filming with phone' },
    { id: 'ai', side: 'right', lines: ['요즘은 AI가 대세?', '시니어도 배울래요!'], illustration: 'robot' },
    { id: 'pc', side: 'left', lines: ['컴퓨터를 기초부터', '차근차근 배워보기!'], illustration: 'desktop computer' },
  ] satisfies AudienceWish[],
}

export interface CourseDetail {
  id: string
  title: string
  rows: InfoItem[]
}

const detailRows = (): InfoItem[] => [
  { label: '[대상]', value: '스마트폰 사용 초보이신 분' },
  { label: '[과정]', value: '스마트폰 기본 조작법\n전화 통화 및 사진 찍기\n메신저 사용 및 기타' },
]

export const detailPanel = {
  heading: '상세안내',
  courses: [
    { id: 'phone', title: '스마트폰 기초 강좌', rows: detailRows() },
    { id: 'video', title: '영상 편집 기초', rows: detailRows() },
    { id: 'kiosk', title: '키오스크 정복', rows: detailRows() },
    { id: 'ai', title: 'AI 활용 기초', rows: detailRows() },
  ] satisfies CourseDetail[],
}
