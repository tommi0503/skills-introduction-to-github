import type { LucideIcon } from 'lucide-react'
import { Bus, Clock3, Link2, MapPin, Phone, TrainFront } from 'lucide-react'
import type { CardInsets } from '../shared-2021/components/CardSheet'

export interface ApplyMethod {
  id: string
  icon: LucideIcon
  /** Render the glyph solid (phone handset). */
  iconFilled?: boolean
  title: string
  /** Grey explanatory lines. */
  notes: string[]
  /** Highlighted blue line (phone / place / url). */
  highlight: string
  highlightClassName: string
  /** Optional trailing grey line with a QR icon box beside it. */
  qrCaption?: string
  /** Vertical gap between the title row and the notes (px). */
  notesGap: number
  /** Vertical gap between the notes and the highlight (px). */
  highlightGap: number
}

export interface TransitRoute {
  id: string
  icon: LucideIcon
  lines: string[]
}

export interface ContactLine {
  id: string
  icon: LucideIcon
  filled?: boolean
  text: string
}

export const cards: CardInsets[] = [
  { left: 30, top: 30, right: 29, bottom: 26 },
  { left: 35, top: 30, right: 31, bottom: 26 },
  { left: 35, top: 30, right: 30, bottom: 26 },
]

export const applyPanel = {
  heading: '신청하는 방법',
  methods: [
    {
      id: 'phone',
      icon: Phone,
      iconFilled: true,
      title: '전화 신청',
      notes: ['[튤립구 평생 학습센터 교육과]'],
      highlight: '02-1234-5678',
      highlightClassName: 'text-[24.5px] font-semibold tracking-[0.01em]',
      notesGap: 26,
      highlightGap: 7,
    },
    {
      id: 'visit',
      icon: MapPin,
      title: '방문 신청',
      notes: ['[튤립구 평생 학습센터 교육과]'],
      highlight: '1층 접수센터 혹은 안내 문의',
      highlightClassName: 'text-[24.5px] font-bold tracking-[-0.01em]',
      notesGap: 26,
      highlightGap: 12,
    },
    {
      id: 'online',
      icon: Link2,
      title: '온라인 신청',
      notes: ['[하단 QR코드을 촬영하시면', '사이트에 접속하실 수 있습니다]'],
      highlight: 'http://www.umchungjoeun.kr',
      highlightClassName: 'text-[18px] font-medium',
      notesGap: 16,
      highlightGap: 4,
      qrCaption: '홈>교육신청>세부사항',
    },
  ] satisfies ApplyMethod[],
  prepHeading: '신청시 준비물',
  prepNote: '방문 신청시 신분증 지참 필수',
}

export const directionsPanel = {
  heading: '오시는 길',
  place: '튤립구 평생 학습센터',
  address: ['서울특별시 다정구 상상로 77', '희망빌딩 1층 00031'],
  routes: [
    { id: 'bus', icon: Bus, lines: ['버스 31, 49, 100-1, 1003', '튤립 정류장 (031400) 하차', '도보 3분 소요'] },
    { id: 'subway', icon: TrainFront, lines: ['지하철 튤립역 2번 출구', '도보 8분'] },
  ] satisfies TransitRoute[],
  contactHeading: '연락처',
  contacts: [
    { id: 'tel1', icon: Phone, filled: true, text: '02-1234-5678' },
    { id: 'tel2', icon: Phone, filled: true, text: '02-1234-5678' },
    { id: 'hours', icon: Clock3, text: '9:00 ~ 18:00' },
  ] satisfies ContactLine[],
}

export const coverPanel = {
  kicker: '시니어를 위한',
  title: '디지털&AI',
  subtitle: '첫걸음교실',
  tagline: '생활에 필요한 IT를 쉽게!',
  courses: ['스마트폰', '키오스크', 'AI 활용'],
  inquiryLabel: '문의',
  inquiryPlace: '튤립구 평생학습센터',
  inquiryPhone: '02-1234-5678',
}
