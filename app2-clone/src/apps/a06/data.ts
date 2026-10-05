import {
  ClipboardList, Heart, House, ShoppingBag, Smile, type LucideIcon,
} from 'lucide-react'

/* ---------- shared ---------- */
export interface NavItem {
  key: string
  label: string
  icon: LucideIcon
}
export const navItems: NavItem[] = [
  { key: 'home', label: '홈', icon: House },
  { key: 'shop', label: '장보기·쇼핑', icon: ShoppingBag },
  { key: 'like', label: '찜', icon: Heart },
  { key: 'orders', label: '주문내역', icon: ClipboardList },
  { key: 'my', label: '마이배민', icon: Smile },
]

export type TagKind = 'mint' | 'club' | 'grey' | 'new' | 'greyMuted'
export interface TagData {
  label: string
  kind: TagKind
}

/* ---------- home ---------- */
export const home = {
  searchPlaceholder: '배민클럽은 배달팁 0원에 쿠폰까지!',
  promo: { lines: ['배민클럽 먹을복 제대로 터졌다!', '총 219,500원 할인 받아요'], cta: '쿠폰받고 주문하기' },
  tabs: ['음식배달', '픽업', '장보기·쇼핑', '선물하기', '혜택모아보기'],
  more: { strong: '음식배달', rest: '에서 더보기' },
  sectionTitle: '금방 도착하는 가게',
}

export interface GridItem {
  key: string
  label: string
  badge?: string
}
export const serviceGrid: GridItem[][] = [
  [
    { key: 'fest', label: '먹을복페스타' },
    { key: 'meet', label: '만나서결제' },
    { key: 'one', label: '한그릇' },
    { key: 'pick', label: '바로 픽업', badge: '기다림없이' },
    { key: 'point', label: '포인트모으기' },
  ],
  [
    { key: 'jokbal', label: '족발·보쌈' },
    { key: 'katsu', label: '돈까스·회' },
    { key: 'pizza', label: '피자' },
    { key: 'jjim', label: '찜·탕' },
    { key: 'chinese', label: '중식' },
  ],
]

export interface StoreBrand {
  key: string
  label: string
  badge?: string
}
export const brands: StoreBrand[] = [
  { key: 'bmart', label: 'B마트', badge: '무료배달' },
  { key: 'cu', label: 'CU', badge: '무료배달' },
  { key: 'emart', label: '이마트', badge: '최대15%' },
  { key: 'everyday', label: '이마트슈퍼' },
  { key: 'nobrand', label: '노브랜드' },
  { key: 'gs', label: 'GS더프레시', badge: '최대20%' },
]

/* ---------- search ---------- */
export const search = {
  query: '김치찜',
  relatedLabel: '연관',
  related: ['묵은지김치찜', '갈비찜', '등갈비김치찜', '곱도리탕', '두루치기'],
  tabs: ['전체', '배달 99+', '픽업 61', '장보기·쇼핑 22', '전시'],
  section: '배달',
  sort: '기본순',
}

export interface ResultData {
  key: string
  name: string
  /** description split into runs; `hit` runs are the matched keyword */
  desc: { text: string; hit?: boolean }[]
  rating: string
  reviews: string
  minOrder: string
  eta: string
  etaIcon: 'blue' | 'teal'
  thumb: { caption: string; price: string; discount: string }
  tags: TagData[][]
  ad?: boolean
}

const hit = (text: string) => ({ text, hit: true })
const fest: TagData = { label: '먹을복페스타', kind: 'mint' }
const club: TagData = { label: '배민클럽', kind: 'club' }
const relief: TagData = { label: '고유가 피해지원금', kind: 'grey' }
const pickup: TagData = { label: '픽업가능', kind: 'grey' }
const reserve: TagData = { label: '예약가능', kind: 'grey' }

export const results: ResultData[] = [
  {
    key: 'r1', name: '귀한김치찜 마포점',
    desc: [{ text: '1.5인 ' }, hit('김치찜'), { text: ' 백반, 2~3인 삼겹2배 ' }, hit('김치찜'), { text: ' 세트' }],
    rating: '5.0', reviews: '(341)', minOrder: '5,000원', eta: '약 22분', etaIcon: 'blue',
    thumb: { caption: '1.5인 김치찜 백반', price: '16,400원', discount: '2,000원 즉시할인' },
    tags: [[fest, club, relief], [pickup]], ad: true,
  },
  {
    key: 'r2', name: '김치찜만 30년 홍대점',
    desc: [{ text: '[1인분] 30년 전통 한돈 ' }, hit('김치찜'), { text: ' 세트, [2~3인분] 30년 전통' }],
    rating: '4.8', reviews: '(320)', minOrder: '5,000원', eta: '약 17분', etaIcon: 'teal',
    thumb: { caption: '[1인분] 30년 전통 한돈 김치찜', price: '18,900원', discount: '2,000원 즉시할인' },
    tags: [[fest, club, relief], [pickup, reserve]],
  },
  {
    key: 'r3', name: '영원김치찜',
    desc: [{ text: '[]신선 한돈[]양많은 1인 한돈 고기가득 ' }, hit('김치찜')],
    rating: '5.0', reviews: '(521)', minOrder: '5,000원', eta: '약 17분', etaIcon: 'teal',
    thumb: { caption: '[]신선 한돈[]양많은 1인', price: '17,900원', discount: '3,000원 즉시할인' },
    tags: [[fest, club]], ad: true,
  },
  {
    key: 'r4', name: '김치돼학교 홍대점',
    desc: [{ text: '[++오픈E벤트++] 직화 삼겹 ' }, hit('김치찜'), { text: ', [100% 국내산]' }],
    rating: '5.0', reviews: '(1,575)', minOrder: '5,000원', eta: '약 24분', etaIcon: 'teal',
    thumb: { caption: '[++오픈E벤트++] 직화', price: '18,900원', discount: '2,000원 즉시할인' },
    tags: [[fest, club]],
  },
]

/* ---------- category list ---------- */
export const category = {
  title: '음식배달',
  cartCount: '1',
  tabs: ['분식', '중식', '찜·탕', '돈까스·회', '피자', '아시안'],
  active: '돈까스·회',
  sortLabel: '기본순 외',
  coupon: '지금 바로 사용할 수 있는 쿠폰은?',
}

export interface MenuItem {
  key: string
  caption: string
  price: string
  was: string
}
export interface ShopBlock {
  key: string
  name: string
  rating: string
  reviews: string
  menus: MenuItem[]
  discount: string
  eta: string
  distance: string
  minOrder: string
  tags: TagData[]
}
export const shops: ShopBlock[] = [
  {
    key: 'barun', name: '바른카츠 본점', rating: '4.9', reviews: '(2,150)',
    menus: [
      { key: 'm1', caption: '[혼밥] 쫄면 정식세트', price: '11,900원', was: '14,900원' },
      { key: 'm2', caption: '[시그니처] 생모짜 치즈카츠', price: '11,900원', was: '14,900원' },
      { key: 'm3', caption: '[추천] 크림 김치 볶음밥', price: '13,900원', was: '16,900원' },
    ],
    discount: '3,000원 즉시할인', eta: '약 29분', distance: '2.0km', minOrder: '11,900원',
    tags: [
      { label: '먹을복페스타', kind: 'greyMuted' }, club, { label: '신규', kind: 'new' }, relief, pickup, reserve,
    ],
  },
  {
    key: 'sushi', name: '스시 히바치', rating: '4.9', reviews: '(1,024)',
    menus: [
      { key: 'm1', caption: '스테셜 초밥(14p)', price: '20,000원', was: '21,000원' },
      { key: 'm2', caption: '나만의 초밥세트', price: '16,500원', was: '17,500원' },
      { key: 'm3', caption: '특선 초밥(12pcs)', price: '16,000원', was: '17,000원' },
    ],
    discount: '1,000원 즉시할인', eta: '약 31분', distance: '1.6km', minOrder: '15,000원',
    tags: [],
  },
]
