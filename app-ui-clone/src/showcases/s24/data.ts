import { CalendarCheck, House, PlaneTakeoff, Star, type LucideIcon } from 'lucide-react'

export interface IconLabel {
  icon: LucideIcon
  label: string
}

export const greeting = 'WWIT님 어디로 가시나요?'
export const destinationPlaceholder = '목적지 입력'

export const shortcuts: IconLabel[] = [
  { icon: House, label: '집으로' },
  { icon: Star, label: '강남역' },
]

export const reserve = {
  title: '타다 예약하기',
  actions: [
    { icon: PlaneTakeoff, label: '공항 이동' },
    { icon: CalendarCheck, label: '시간 대절' },
  ] as IconLabel[],
}

export interface PromoBanner {
  lines: string[]
  background: string
}

export const friendBanner: PromoBanner = {
  lines: ['편안한 이동이 필요한', '친구가 있다면'],
  background: '#bbe0fd',
}

export const nextBanner: PromoBanner = {
  lines: ['타다 NEXT 출시 기념', '탈 때마다 50% 할인'],
  background: 'linear-gradient(90deg,#c3dbf9 0%,#bcd5f6 60%,#a9c3ec 100%)',
}

export interface Notice {
  /** Plain prefix then bold part. */
  text: string
  bold: string
}

export const homeNotice: Notice = { text: '타다 NEXT ', bold: '무제한 50% 할인' }
export const feedNotice: Notice = { text: '타다 NEXT 출시 기념 ', bold: '선착순 혜택' }

export interface StoryCardItem {
  id: string
  title: string
  subtitle: string
  imageHeight: number
}

export const storyCards: StoryCardItem[] = [
  { id: 'call', title: '부르는 게 전부는 아니니까', subtitle: '더 편하게 타다 이용하는 방법', imageHeight: 152 },
  { id: 'waaay', title: '일상 속 이동에 대한 이야기', subtitle: '타다와 쏘카의 인터뷰 프로젝트 WaaaY', imageHeight: 152 },
]

export const profile = { name: 'WWIT', phone: '010-', credit: '0 크레딧' }

export const drawerPromo = { title: '횟수 제한없이 10% 할인', link: '쿠폰 확인하기' }

export interface MenuItem {
  label: string
  caption?: string
}

export const primaryMenu: MenuItem[] = [
  { label: '공지 및 이벤트' },
  { label: '패스포트', caption: '바로 70,000원 혜택 받으세요.' },
  { label: '쿠폰' },
  { label: '탑승 내역' },
  { label: '결제 관리' },
  { label: '친구초대' },
]

export const secondaryMenu: string[] = ['고객센터', '설정']
