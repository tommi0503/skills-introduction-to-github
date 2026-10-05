import { House, Apple, TextSearch, ShoppingCart, BriefcaseBusiness, type LucideIcon } from 'lucide-react'

export type LineTone = 'muted' | 'accent'
export type ActionKind = 'primary' | 'secondary'

export interface BasketLine {
  text: string
  tone?: LineTone
}

export interface BasketAction {
  label: string
  kind: ActionKind
}

export interface Basket {
  id: string
  title: string
  /** Number of stacked avatars (1 = single store logo, 2 = group order). */
  avatars: 1 | 2
  lines: BasketLine[]
  actions: BasketAction[]
  showMore: boolean
}

export interface NavItem {
  key: string
  label: string
  icon: LucideIcon
  badge?: number
}

export const header = { title: 'Baskets', action: 'Orders' }

export const baskets: Basket[] = [
  {
    id: 'mcd',
    title: 'McDonald’s®',
    avatars: 1,
    lines: [{ text: '3 items · US$20.57' }, { text: 'Deliver to 1226 University Dr' }],
    actions: [
      { label: 'View basket', kind: 'primary' },
      { label: 'View shop', kind: 'secondary' },
    ],
    showMore: true,
  },
  {
    id: 'safeway',
    title: 'Safeway',
    avatars: 1,
    lines: [{ text: '5 items · US$22.57' }, { text: 'Deliver by 20:45 on Monday to 1226 University Dr' }],
    actions: [
      { label: 'View basket', kind: 'primary' },
      { label: 'View shop', kind: 'secondary' },
    ],
    showMore: true,
  },
  {
    id: 'group',
    title: '1226 University Dr Group orders',
    avatars: 2,
    lines: [{ text: 'Repeats · Created by Joshua S' }, { text: '2 upcoming orders', tone: 'accent' }],
    actions: [{ label: 'View order', kind: 'primary' }],
    showMore: false,
  },
]

export const navItems: NavItem[] = [
  { key: 'home', label: 'Home', icon: House },
  { key: 'grocery', label: 'Grocery', icon: Apple },
  { key: 'browse', label: 'Browse', icon: TextSearch },
  { key: 'baskets', label: 'Baskets', icon: ShoppingCart, badge: 3 },
  { key: 'account', label: 'Account', icon: BriefcaseBusiness },
]
export const activeNav = 'baskets'
