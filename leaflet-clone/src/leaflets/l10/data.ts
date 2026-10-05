import { BusFront, Ticket, type LucideIcon } from 'lucide-react'
import type { ShapeSpec } from '../shared-0812'

export interface InfoSection {
  title: string
  icon?: LucideIcon
  lead?: string[]
  rows?: { label: string; value: string }[]
  notes: string[]
}

export const greeting = {
  title: '인사말',
  paragraphs: [
    ['나무섬 전망대에 오신', '여러분 환영합니다.', '높은 곳에서 자연의', '아름다움과 섬의 풍경을', '만끽해 보세요.'],
    ['감사합니다.'],
    ['나무섬전망대'],
  ],
}

export const guide: InfoSection[] = [
  {
    title: '오시는 길',
    icon: BusFront,
    lead: ['강원도 강릉시 주문진읍 해안로 2733-9'],
    notes: ['지하철 나무섬역 2번 출구 앞', '무료 셔틀버스 운영'],
  },
  {
    title: '입장료',
    icon: Ticket,
    rows: [
      { label: '유아', value: '3,000원' },
      { label: '청소년', value: '6,000원' },
      { label: '성인', value: '12,000원' },
    ],
    notes: ['(전화 및 온라인 사전 예약시 2000원 할인)'],
  },
  {
    title: '예약 문의',
    lead: ['03-987-1533', 'www.umchungjoeun.kr'],
    notes: ['10인 이상 방문의 경우, 사전 예약이 필수입니다.', '전화 또는 웹사이트로 예약 부탁드립니다.'],
  },
]

export const cover = {
  booking: '온라인 예약',
  kicker: '하늘과 땅을 한 눈에',
  title: ['나무섬', '전망대'],
  closed: '매주 일요일 정기휴관',
  hours: ['10:00 - 17:00', '(입장마감 16:00)'],
}

/** Sheet-level artwork (clouds, tree) in sheet coordinates. */
export const sheetArt: ShapeSpec[] = [
  { x: 0, y: 20, w: 272, h: 80, radius: '40px 60px 30px 20px', label: 'cloud' },
  { x: 393, y: 18, w: 197, h: 78, radius: '40px', label: 'cloud' },
  { x: 850, y: 60, w: 190, h: 58, radius: '30px', label: 'cloud' },
  { x: 222, y: 497, w: 230, h: 120, radius: '115px 115px 40px 40px', label: 'tree crown' },
  { x: 335, y: 600, w: 34, h: 160, label: 'tree trunk' },
]

export const coverArt: ShapeSpec[] = [
  { x: 380, y: 40, w: 55, h: 55, label: 'QR code' },
  { x: 335, y: 306, w: 145, h: 50, radius: '25px 0 0 25px', tone: '#5a6a98', label: 'cloud' },
  { x: 0, y: 84, w: 80, h: 32, radius: '0 16px 16px 0', tone: '#5a6a98', label: 'cloud' },
  { x: 0, y: 466, w: 480, h: 552, tone: '#c9ccd1', label: 'ocean telescope photo' },
]

/** Wave band geometry across the two inner panels (sheet px). */
export const waves = { x: 0, width: 960, top: 736, bottom: 782, period: 162, crestX: 145 }
