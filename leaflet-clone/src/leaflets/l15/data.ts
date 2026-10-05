import type { Artist } from '../shared-1516/components/ArtistCard'

export const artists = {
  eyebrow: 'ARTISTS',
  title: '함께하는 사람들',
  list: [
    { role: '지휘', name: '한아름', notes: ['예술대학교 지휘과 교수', '전 시립교향악단 부지휘자'], side: 'left', y: 186, textX: 211 },
    { role: '바이올린', name: '서도윤', notes: ['국제콩쿠르 우승', '음대 최고연주자 과정'], side: 'right', y: 414, textX: 71 },
    { role: '첼로', name: '민하늘', notes: ['수석 첼리스트', '유럽 3개국 리사이틀 투어'], side: 'left', y: 639, textX: 220 },
  ] satisfies Artist[],
  closing: ['2015년 창단 이후 매년 두 차례,', '정기연주회로 관객을 만나고 있습니다.'],
}

export interface TicketRow {
  seat: string
  price: string
  note: string
}

export const ticket = {
  eyebrow: 'TICKET',
  title: '티켓 안내',
  columns: { seat: '좌석', price: '가격', note: '비고' },
  rows: [
    { seat: 'R석', price: '50,000원', note: '1층 중앙' },
    { seat: 'S석', price: '30,000원', note: '1층 사이드·2층' },
    { seat: 'A석', price: '20,000원', note: '3층' },
  ] satisfies TicketRow[],
  footnote: '* 학생·경로 30% 할인 (신분증 지참) / 단체 10인 이상 20% 할인',
  purchaseTitle: '예매 방법',
  purchase: [
    { label: '온라인', value: '인터파크 티켓 · 예스24 공연' },
    { label: '전화', value: '02-567-8901 (평일 10:00~17:00)' },
    { label: '현장', value: '공연 당일 1시간 전부터 (잔여석)' },
  ],
  mapTitle: '오시는 길',
  venueLabel: '라라나아트센터 콘서트홀',
  access: [
    { label: '지하철', value: '서울역 2번 출구 도보 5분' },
    { label: '주 차', value: '아트센터 지하주차장 (공연 관람 3시간 무료)' },
  ],
}

export const cover = {
  edition: '제12회 정기연주회',
  titleLines: ['특별한', '음악회'],
  date: '2080. 10. 24 (토) 오후 7시 30분',
  venue: '라라나아트센터 콘서트홀',
  credits: [
    { label: '주최', value: '달빛 챔버 오케스트라' },
    { label: '후원', value: '라라나문화재단' },
  ],
}
