import { Compass, Heart, House, ShoppingCart, type LucideIcon } from 'lucide-react'
import { theme } from './theme'

export interface NavItem {
  key: string
  icon: LucideIcon
  label: string
  /** Solid glyph (heart, house) vs outlined (cart). */
  filled?: boolean
}

export const navItems: NavItem[] = [
  { key: 'home', icon: House, label: 'Home', filled: true },
  { key: 'explore', icon: Compass, label: 'Explore' },
  { key: 'cart', icon: ShoppingCart, label: 'Cart' },
  { key: 'saved', icon: Heart, label: 'Saved', filled: true },
]

export interface Product {
  title: string[]
  price: string
  /** Inner (image) card colour and outer frame colour. */
  tone: string
  frame: string
  heartBg: string
}

export const potatoChips: Product = {
  title: ['Potato', 'Chips'],
  price: '$2.00 USD',
  tone: theme.yellow,
  frame: theme.yellowSoft,
  heartBg: '#f6c300',
}

export const cheetos: Product = {
  title: [],
  price: '$1.80 USD',
  tone: theme.orange,
  frame: theme.orangeSoft,
  heartBg: '#ff9213',
}

export const homeCategories = ['All', 'Chips', 'Chocolate', 'Cookies']
export const exploreFilters = ['All', 'Recent', 'Offers', 'Trending']

export interface PhotoBox {
  left: number
  top: number
  width: number
}

export interface Collection {
  title: string
  tags: string[]
  color: string
  /** Loose snacks photo (left) and stacked bags photo (right); both run to the card bottom. */
  snacks: PhotoBox
  bags: PhotoBox
}

export const collections: Collection[] = [
  {
    title: 'Crunchy Chips',
    tags: ['Crispy', 'salty', 'fun'],
    color: '#ffdd94',
    snacks: { left: 6, top: 62, width: 190 },
    bags: { left: 182, top: 20, width: 150 },
  },
  {
    title: 'Cheese Laius Chips',
    tags: ['Cheesy', 'crunchy', 'bold'],
    color: '#fdd3a5',
    snacks: { left: 2, top: 90, width: 192 },
    bags: { left: 180, top: 17, width: 160 },
  },
  {
    title: 'Onion Rings Funyuns',
    tags: ['Crispy', 'salty', 'tasty'],
    color: '#fff7ac',
    snacks: { left: 40, top: 84, width: 132 },
    bags: { left: 196, top: 33, width: 136 },
  },
  {
    title: 'Mixed Nuts',
    tags: ['Natural', 'crunchy', 'energizing'],
    color: '#f9cd96',
    snacks: { left: 6, top: 90, width: 150 },
    bags: { left: 222, top: 30, width: 110 },
  },
]

export const user = { greeting: 'Hi, Jack.L', subtitle: 'Best Snacks For you' }

export const onboarding = {
  titleBold: ['Your Favorite', 'Treats,'],
  titleLight: 'Anytime',
  subtitle: 'Snacks delivered fast, fresh, anytime.',
  cta: 'Get Start',
}
