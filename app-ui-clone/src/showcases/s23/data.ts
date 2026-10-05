import { House, NotepadText, UserRound, type LucideIcon } from 'lucide-react'

export interface ServiceItem {
  id: string
  name: string
  /** Lines under the name. */
  details: string[]
  price: string
  /** Suffix after the price (e.g. "원 부터"). */
  unit: string
  /** Card surface gradient (plain UI surface behind the product photo). */
  surface: string
  /** Product photo area inside the card (card-relative logical px). */
  photo: { x: number; y: number; w: number; h: number; radius: string }
}

const beige = 'linear-gradient(90deg,#f1ece6 0%,#efeae4 45%,#dcdad5 100%)'
const grey = 'linear-gradient(100deg,#dad8d5 0%,#e6e3df 55%,#e4e1dd 100%)'
const rack = { x: 178, y: 20, w: 142, h: 135.5, radius: '16px 16px 0 0' }
const flat = { x: 181, y: 56, w: 137, h: 85, radius: '2px' }

export const services: Record<string, ServiceItem> = {
  allInOne: {
    id: 'allInOne',
    name: '올인원',
    details: ['생활빨래, 와이셔츠,', '개별클리닝'],
    price: '64,200',
    unit: '원 부터',
    surface: beige,
    photo: rack,
  },
  shirtsDry: {
    id: 'shirtsDry',
    name: '와이셔츠&드라이',
    details: ['와이셔츠,', '개별클리닝'],
    price: '43,500',
    unit: '원 부터',
    surface: beige,
    photo: rack,
  },
  dryOnly: {
    id: 'dryOnly',
    name: '드라이온리',
    details: ['개별클리닝'],
    price: '58,600',
    unit: '원 부터',
    surface: 'linear-gradient(180deg,#ecebe8 0%,#e5e3e0 100%)',
    photo: rack,
  },
  laundryDry: {
    id: 'laundryDry',
    name: '런드리&드라이',
    details: ['생활빨래,', '개별클리닝'],
    price: '47,400',
    unit: '원 부터',
    surface: 'linear-gradient(90deg,#e4e1de 0%,#e1dedb 100%)',
    photo: rack,
  },
  laundryOnly: {
    id: 'laundryOnly',
    name: '런드리온리',
    details: ['생활빨래'],
    price: '38,700',
    unit: '원 부터',
    surface: grey,
    photo: flat,
  },
  beddingOnly: {
    id: 'beddingOnly',
    name: '베딩온리',
    details: ['이불'],
    price: '28,700',
    unit: '원',
    surface: 'linear-gradient(100deg,#cfcdcb 0%,#e1dedb 60%,#e4e1de 100%)',
    photo: flat,
  },
}

export const monthlyIntro = {
  title: '월정액 서비스',
  subtitle: '주기적인 세탁이 필요할 때 합리적인 가격으로 이용하세요',
}

export const topTabs = ['월정액', '자유이용']
export const guideLabel = '가이드'

export const hero = {
  eyebrow: 'EVERYDAY ESSENTIAL',
  headline: 'MEET',
  brand: [
    { text: 'LIFE', script: false },
    { text: 'goes', script: true },
    { text: 'ON', script: false },
  ],
  body: ['매일 마주하는 일상을', '특별하게 만들어 줄 라이프 어메니티'],
  pager: '2 / 8',
}

export const areaCheck = '서비스 가능 지역 확인'

export const event = {
  kicker: '친구 초대 이벤트',
  before: '친구도 나도 ',
  highlight: '5,000원',
  after: ' 지급',
}

export interface StoryItem {
  id: string
  label: string
  title: string[]
  isNew?: boolean
}

export const storyIntro = { title: '런드리고의 재발견', subtitle: '우리가 몰랐던 런드리고 이야기' }

export const stories: StoryItem[] = [
  { id: 's10', label: 'STORY.10', title: ['드라이클리닝의', '오해와 진실'], isNew: true },
  { id: 's09', label: 'STORY.09', title: ['일상의 불편함을', '함께 수선하세요'] },
]

export interface FooterLine {
  text: string
  /** Trailing underlined link text. */
  link?: string
  /** Whole line value underlined after label. */
  underlined?: string
}

export const footerLines: FooterLine[] = [
  { text: '(주) 의식주컴퍼니' },
  { text: '대표: 조성우  사업자 등록번호: 561-87-00957 ', link: '[사업자 정보 확인]' },
  { text: '통신판매업신고 : 제 2018-서울강서-2052호' },
  { text: '주소: 서울시 강서구 양천로60길 40 (우편번호: 07566)' },
  { text: '개인정보담당자 : 김상재  이메일: privacy@lifegoeson.kr' },
  { text: '고객센터 : ', underlined: '1833-3429' },
  { text: 'Copyright 2018 © Lifegoeson All rights reserved.' },
]
export const footerButton = '이용약관 및 개인정보취급방침'

export interface NavItem {
  key: string
  label: string
  icon?: LucideIcon
  /** Brand mark rendered as placeholder. */
  logo?: boolean
}

export const navItems: NavItem[] = [
  { key: 'home', label: '홈', icon: House },
  { key: 'pickup', label: '수거요청', logo: true },
  { key: 'history', label: '이용내역', icon: NotepadText },
  { key: 'my', label: 'MY', icon: UserRound },
]
