export const payTabs = ['멤버십', '현장결제', '쿠폰']
export const ACTIVE_PAY_TAB = 1

export const pointMoney = {
  title: '포인트•머니',
  balanceLabel: '보유잔액',
  balance: '9,789원',
  accountLabel: '출금계좌',
  account: '미래에셋 4520',
  promo: { text: '포인트 뽑기가 ', highlight: '총 3번!' },
}

export interface EventCardData {
  color: string
  caption: string
}

export const eventsA: EventCardData[] = [
  { color: '#3e26d2', caption: 'T로밍하고 결제하면' },
  { color: '#6b3314', caption: '매주 카페에서' },
  { color: '#2b44e6', caption: '' },
]

export const eventsB: EventCardData[] = [
  { color: '#3367d8', caption: '' },
  { color: '#3367d8', caption: '' },
  { color: '#3b9ea6', caption: '' },
]

export interface WalletCard {
  /** Top edge inside the stack (logical px). */
  top: number
  badge: string
  /** Placeholder tone so overlapping card images stay distinguishable. */
  tone: string
  /** Badge top offset from the card top. */
  badgeTop: number
}

export const walletCards: WalletCard[] = [
  { top: 329, badge: '신한 5699', tone: '#d4d6db', badgeTop: 20 },
  { top: 486.5, badge: '비씨 7892', tone: '#e5e7eb', badgeTop: 20 },
  { top: 641.5, badge: '국민 2095', tone: '#dcdee3', badgeTop: 20 },
]

export interface NavItem {
  label: string
  icon: 'asset' | 'benefit' | 'stock' | 'estate'
  x: number
}

export const navItems: NavItem[] = [
  { label: '자산·송금', icon: 'asset', x: 40.7 },
  { label: '혜택', icon: 'benefit', x: 116.5 },
  { label: '증권', icon: 'stock', x: 272.9 },
  { label: '부동산', icon: 'estate', x: 351.3 },
]

export interface PayMethod {
  name: string
  region: string
  selected?: boolean
  event?: boolean
  /** Logo placeholder tone (brand logos are not drawn). */
  tone: string
  outlined?: boolean
}

export const payMethods: PayMethod[] = [
  { name: '네이버페이', region: '국내', selected: true, tone: '#e5e7eb' },
  { name: '알리페이 플러스', region: '해외', event: true, tone: '#e5e7eb' },
  { name: '유니온페이', region: '해외', event: true, tone: '#eef0f2', outlined: true },
  { name: 'GLN', region: '해외', event: true, tone: '#e5e7eb' },
]
