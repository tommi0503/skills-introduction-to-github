import { Bell, House, ReceiptText, ShoppingCart, type LucideIcon } from 'lucide-react'

export interface CartItem {
  id: string
  title: string
  variant: string
  price: string
  quantity: number
}

export interface StoreCart {
  id: string
  name: string
  rating: string
  reviews: string
  items: CartItem[]
  subtotal?: string
  /** Logo tile tone (black brand mark vs white). */
  logoTone: string
}

export const searchPlaceholder = 'Search'
export const checkoutLabel = 'Continue to checkout'
export const subtotalLabel = 'Subtotal'

export const stores: StoreCart[] = [
  {
    id: 'quince',
    name: 'Quince',
    rating: '4.7',
    reviews: '(1,489)',
    logoTone: '#e5e7eb',
    subtotal: 'US$169.70',
    items: [
      { id: 'cotton', title: 'Lightweight Cotton', variant: 'M / Black', price: 'US$39.90', quantity: 2 },
      { id: 'wool', title: 'Italian Wool Slim Leg', variant: '8 / Black', price: 'US$89.90', quantity: 1 },
    ],
  },
  {
    id: 'sakara',
    name: 'Sakara Life',
    rating: '4.6',
    reviews: '(25,049)',
    logoTone: '#e5e7eb',
    items: [{ id: 'beanie', title: 'The Sakara Beanie', variant: '1 Beanie', price: 'US$20.00', quantity: 1 }],
  },
]

export interface NavTab {
  id: string
  icon?: LucideIcon
  badge?: number
  avatarInitial?: string
}

export const navTabs: NavTab[] = [
  { id: 'home', icon: House },
  { id: 'alerts', icon: Bell },
  { id: 'cart', icon: ShoppingCart, badge: 5 },
  { id: 'orders', icon: ReceiptText },
  { id: 'profile', avatarInitial: 'J' },
]
export const activeTab = 'cart'
