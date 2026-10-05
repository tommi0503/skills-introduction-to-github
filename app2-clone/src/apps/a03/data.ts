import { ArrowDown, ArrowRight, ArrowUp, ArrowUpDown, ChartPie, Heart, QrCode, Repeat2, ScrollText, SendHorizontal, Sparkles, TrendingUp, type LucideIcon } from 'lucide-react'

export type NavKey = 'portfolio' | 'markets' | 'search' | 'inbox' | 'agents'
export const navItems: { key: NavKey; label: string }[] = [
  { key: 'portfolio', label: 'Portfolio' },
  { key: 'markets', label: 'Markets' },
  { key: 'search', label: 'Search' },
  { key: 'inbox', label: 'Inbox' },
  { key: 'agents', label: 'Agents' },
]

/* Onboarding */
export const onboarding = {
  headline: ['Investing for those', 'who take it seriously'],
  features: [
    { key: 'multi', icon: ChartPie, label: 'Multi-asset investing' },
    { key: 'yield', icon: TrendingUp, label: 'Industry-leading yields' },
    { key: 'ai', icon: Sparkles, label: 'AI-powered automation' },
    { key: 'support', icon: Heart, label: 'Award-winning support' },
  ] as { key: string; icon: LucideIcon; label: string }[],
  primary: 'Create account',
  secondary: 'Log in',
}

/* Portfolio */
export const portfolio = {
  account: 'Brokerage',
  value: '$17.16',
  tabs: ['Return', 'Income', 'Account value', 'Allocation'],
  change: '$0.04 (0.23%)',
  ranges: ['1D', '1W', '1M', '3M', '6M', 'YTD', '1Y'],
  marginLabel: 'Margin buying power',
  marginValue: '$11.02',
  promo: {
    title: 'Options trading enabled',
    body: 'Earn a $0.06–$0.18 rebate per stock & ETF contract, based on your monthly trading volume.',
    cta: 'Explore Options',
  },
  pages: 8,
  behindTitle: 'Portfolio',
  behindAction: 'Customize',
}

/* Options strategies */
export interface Strategy {
  key: string
  name: string
  sentiment: 'Bullish' | 'Bearish'
  /** Payoff polyline in the 170×84 chart box. */
  points: [number, number][]
  dot: [number, number]
}
export const options = {
  search: 'NVDA Options',
  tabs: ['Owned', 'Strategies', 'Explore', 'Jul 29', 'Jul 31', 'Aug 1'],
  activeTab: 'Strategies',
  priceNote: 'NVDA is at $197.52',
  title: 'Build an options strategy',
  directions: [
    { key: 'up', icon: ArrowUp, color: '#4f9b2a' },
    { key: 'down', icon: ArrowDown, color: '#d23b3b' },
    { key: 'both', icon: ArrowUpDown, color: '#e2703b' },
    { key: 'flat', icon: ArrowRight, color: '#5b6a84' },
  ] as { key: string; icon: LucideIcon; color: string }[],
  section: 'Fundamentals',
  zeroY: 48,
  strategies: [
    { key: 'lc', name: 'Long Call', sentiment: 'Bullish', points: [[-5, 68], [85, 68], [175, -22]], dot: [85, 68] },
    { key: 'lp', name: 'Long Put', sentiment: 'Bearish', points: [[-5, -22], [86, 68], [175, 68]], dot: [86, 68] },
    { key: 'cc', name: 'Covered Call', sentiment: 'Bullish', points: [[-10, 120], [85, 27], [175, 27]], dot: [85, 27] },
    { key: 'csp', name: 'Cash-Secured Put', sentiment: 'Bullish', points: [[-10, 120], [86, 27], [175, 27]], dot: [86, 27] },
    { key: 'cpc', name: 'Covered Put', sentiment: 'Bearish', points: [[-5, 27], [85, 27], [175, 117]], dot: [85, 27] },
    { key: 'lc2', name: 'Long Call', sentiment: 'Bullish', points: [[-5, 67], [86, 67], [175, -22]], dot: [86, 67] },
  ] as Strategy[],
  currentPrice: 'Current price: $197.52',
}

/* Bitcoin */
export interface Quote {
  price: string
  change: string
}
export const bitcoin = {
  ticker: 'BTC',
  name: 'Bitcoin',
  ranges: ['24H', '1W', '1M', '3M', '6M', 'YTD', '1Y', '5Y'],
  about: 'About',
  buyingPowerLabel: 'BTC buying power',
  buyingPower: '$21.00',
  trade: 'Trade',
  explore: 'Explore this asset',
  quotes: {
    detail: { price: '$63,797.67', change: '$461.01 (0.73%)' },
    menu: { price: '$63,664.58', change: '$455.05 (0.72%)' },
  } as Record<'detail' | 'menu', Quote>,
  position: {
    title: 'Your position',
    action: 'History',
    rows: [
      { key: 'today', label: '1D return', value: '-$0.12 (-0.56%)', negative: true },
      { key: 'cost', label: 'Cost basis', value: '$20.00' },
      { key: 'total', label: 'Total value', value: '$21.49' },
      { key: 'unreal', label: 'Unrealized return', value: '-$0.51 (-2.4%)', negative: true },
    ],
  },
  menu: {
    groups: [
      [
        { key: 'send', icon: SendHorizontal, label: 'Send' },
        { key: 'receive', icon: QrCode, label: 'Receive' },
        { key: 'hub', icon: ScrollText, label: 'Options hub' },
      ],
      [{ key: 'recurring', icon: Repeat2, label: 'Recurring buy' }],
    ] as { key: string; icon: LucideIcon; label: string }[][],
    buy: 'Buy',
    sell: 'Sell',
  },
}
