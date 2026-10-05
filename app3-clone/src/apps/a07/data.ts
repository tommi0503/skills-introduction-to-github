import type { LucideIcon } from 'lucide-react'
import { ArrowLeftRight, Bitcoin, ChartNoAxesColumnIncreasing, Landmark, LayoutGrid, Ellipsis, Plus, Shuffle } from 'lucide-react'

/* ---------- Card picker ---------- */
export interface Swatch {
  key: string
  color: string
}

export const cardPicker = {
  badge: 'Customisable',
  title: 'Premium · Space Grey',
  body: 'Made from plastic with a striking shimmer effect, our beautiful Premium card feels as good as it looks',
  swatches: [
    { key: 'grey', color: '#6c6c70' },
    { key: 'rose', color: '#e9c4c0' },
    { key: 'lilac', color: '#a5a8d4' },
  ] satisfies Swatch[],
  selected: 'grey',
  cta: 'Get card for free',
}

/* ---------- Home ---------- */
export interface QuickAction {
  key: string
  label: string
  icon: LucideIcon
}

export interface Transaction {
  key: string
  title: string
  time: string
  primary: string
  secondary: string
}

export interface NavTab {
  key: string
  label: string
  icon?: LucideIcon
  /** brand letter mark */
  mark?: string
}

export const home = {
  search: 'Search',
  account: 'Personal · All accounts',
  balanceMajor: '$19',
  balanceMinor: '.98',
  accounts: 'Accounts',
  pages: 3,
  page: 2,
  actions: [
    { key: 'add', label: 'Add money', icon: Plus },
    { key: 'move', label: 'Move', icon: Shuffle },
    { key: 'details', label: 'Details', icon: Landmark },
    { key: 'more', label: 'More', icon: Ellipsis },
  ] satisfies QuickAction[],
  transactions: [
    { key: 't1', title: 'SGD → USD', time: 'Today, 23:27', primary: '+US$1.49', secondary: '-$2' },
    { key: 't2', title: 'SGD → USD', time: 'Today, 23:27', primary: '-$2', secondary: '+US$1.49' },
  ] satisfies Transaction[],
  seeAll: 'See all',
  products: 'Products for you',
  tabs: [
    { key: 'home', label: 'Home', mark: 'R' },
    { key: 'invest', label: 'Invest', icon: ChartNoAxesColumnIncreasing },
    { key: 'payments', label: 'Payments', icon: ArrowLeftRight },
    { key: 'crypto', label: 'Crypto', icon: Bitcoin },
    { key: 'lifestyle', label: 'Lifestyle', icon: LayoutGrid },
  ] satisfies NavTab[],
  activeTab: 'home',
}

/* ---------- Add money ---------- */
export const addMoney = {
  title: 'Add money',
  source: { name: 'WISE ASIA-PACIFIC...', detail: 'VISA ··7390', action: 'Change' },
  target: { currency: 'SGD', balance: 'Balance: $0', amount: '$20', fee: 'No fee' },
}

/* ---------- Monthly limit ---------- */
export interface KeyDef {
  key: string
  digit?: string
  letters?: string
  /** rendered without a key cap (e.g. decimal point, delete) */
  bare?: boolean
  kind?: 'digit' | 'decimal' | 'delete'
}

export const keypad: KeyDef[] = [
  { key: '1', digit: '1', letters: '\u00a0' },
  { key: '2', digit: '2', letters: 'ABC' },
  { key: '3', digit: '3', letters: 'DEF' },
  { key: '4', digit: '4', letters: 'GHI' },
  { key: '5', digit: '5', letters: 'JKL' },
  { key: '6', digit: '6', letters: 'MNO' },
  { key: '7', digit: '7', letters: 'PQRS' },
  { key: '8', digit: '8', letters: 'TUV' },
  { key: '9', digit: '9', letters: 'WXYZ' },
  { key: '.', digit: '.', bare: true, kind: 'decimal' },
  { key: '0', digit: '0' },
  { key: 'del', bare: true, kind: 'delete' },
]

export const limit = {
  title: 'Set a monthly limit',
  amount: '$50',
  spent: 'Spent this month: $0',
  cta: 'Set limit',
  operators: ['+', '-', '×', '÷', '='],
}
