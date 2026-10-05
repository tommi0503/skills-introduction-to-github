import type { LucideIcon } from 'lucide-react'
import { CircleEllipsis, Gift, HandHeart, House, Store, Tag, User } from 'lucide-react'

/* ---------- Tab bar ---------- */
export type CuTabKey = 'home' | 'stock' | 'pay' | 'my' | 'more'

export interface CuTab {
  key: CuTabKey
  label: string
  icon?: LucideIcon
  /** Centre FAB (QR) instead of an icon. */
  fab?: boolean
}

export const cuTabs: CuTab[] = [
  { key: 'home', label: '홈', icon: House },
  { key: 'stock', label: '재고조회' },
  { key: 'pay', label: '결제·적립·무인', fab: true },
  { key: 'my', label: 'MY CU', icon: User },
  { key: 'more', label: '전체보기', icon: CircleEllipsis },
]

/** Later app build: same tabs, the centre label uses spaced bullets. */
export const cuTabsSpaced: CuTab[] = cuTabs.map((t) => (t.fab ? { ...t, label: '결제 • 적립 • 무인' } : t))

/* ---------- Home ---------- */
export const homeHeader = {
  promoTitle: '⏰BBANG HOUR⏰',
  promoBody: '하루 2번 빵 할인쿠폰 받자!',
  benefitBadge: '혜택',
}

export const searchSuggestion = { rank: '5', keyword: '카다이프', trend: '–' }

export const popupTeaser = {
  caption: '플래시팝업에서 만나고 싶은 상품을 남겨주세요!',
  title: '이거 팔면 살 사람?🙋🏻‍♀️',
}

export const heroBanner = {
  title: ['이거 팔면', '살 사람?'],
  body: ['다음 플래시팝업 상품은?', '2주 한정 참여 이벤트'],
  page: '1 / 11',
}

export interface ServiceTile {
  key: string
  label: string
  /** Large tiles carry the title inside; small ones put it underneath. */
  size: 'large' | 'small'
  bold?: boolean
}

export const serviceTiles: ServiceTile[] = [
  { key: 'pickup', label: '픽업', size: 'large' },
  { key: 'delivery', label: '배달', size: 'large' },
  { key: 'reserve', label: '예약', size: 'small' },
  { key: 'bar', label: 'CU BAR', size: 'small', bold: true },
  { key: 'home', label: '홈배송', size: 'small' },
]

export const keepingTile = { title: '키핑 보관함', caption: '지금은 비어 있어요' }

export const homeSections = {
  favoriteStore: '자주 가는 점포가 있나요?',
  favoriteCta: '단골점포 등록하기',
  services: '찾는 서비스가 있나요?',
}

/* ---------- Product ---------- */
export const product = {
  name: '롯데)빼빼로초코필드',
  price: '2,000',
  currency: '원',
  methods: ['픽업', '배달'],
  cta: '구매하기',
}

/* ---------- Cart ---------- */
export const cart = {
  title: '장바구니',
  tab: { label: '배달', count: 3 },
  address: { name: '우리집', detail: '서울 마포구 (으)로 배달', action: '변경' },
  store: { name: '마포제일점', suffix: ' 에서 배달', autoMatch: '자동매칭' },
  selectAll: '전체 선택',
  bulkActions: ['픽업 담기', '선택 삭제'],
  coupon: { title: '[배달] 무료배달(3천원) + 2천원 할인(2만원 이상 구매)', caption: '쿠폰 자동 발행' },
  promo: { emoji: '🎉', highlight: '2+1', text: ' 행사가 적용되었습니다.' },
  gift: { caption: '증정상품을 담았어요', order: 3, keep: 0 },
  cta: '16,400원 배달 주문하기',
}

export interface CartItem {
  id: string
  name: string
  stock: string
  qty: number
  listPrice?: string
  price: string
  /** Gift summary row under the item. */
  withGift?: boolean
}

export const cartItems: CartItem[] = [
  { id: 'rice', name: 'CJ)큰햇반300g', stock: '10개 남았어요!', qty: 3, listPrice: '8,700원', price: '5,800원', withGift: true },
  { id: 'noodle', name: '농심)육개장사발면', stock: '31개 남았어요!', qty: 3, price: '2,000원' },
]

/* ---------- Keeping box ---------- */
export const keeping = {
  title: '키핑 보관함',
  item: '웅진)오곡누룽지P500ml',
  badge: '증정',
  until: '2026.06.11 까지',
  remaining: '59일 남음',
  since: '보관 시작일 : 2026.04.13',
  barcode: { first: '9', last: '1' },
}

export interface InfoRow {
  icon: LucideIcon
  label: string
  lines: string[]
}

export const keepingInfo: InfoRow[] = [
  { icon: Store, label: '사용처', lines: ['CU 전체 점포', '포켓CU 온라인 구매 (픽업, 배달)'] },
  { icon: Gift, label: '혜택', lines: ['아래 상품 중 1개 교환 가능'] },
  { icon: Tag, label: '사용조건', lines: ['최대 1개 교환', '발행일로부터 60일 사용가능'] },
  { icon: HandHeart, label: '사용방법', lines: ['포켓CU QR화면에서 선택하거나', '키핑 보관함의 바코드를 보여주세요'] },
]
