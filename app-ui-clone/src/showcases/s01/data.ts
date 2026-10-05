import { Calendar, House, MessageSquareText, Search, UserRound } from 'lucide-react'
import type { TabItem } from '../../ui'

export interface Swatch {
  color: string
  selected?: boolean
}

export interface CarouselProduct {
  id: string
  name: string
  price: string
  sizes: string[]
  colors: Swatch[]
}

export interface GridProduct {
  id: string
  name: string
  price: string
  colors: Swatch[]
}

export const brand = { name: 'Rentique', badge: 'Pro member' }

export const hero = {
  title: ['The ultimate snkrs', 'Collection!'],
  cta: 'New arrival for Gen Z',
}

const sizes = ['XS', 'S', 'L', 'XL']
const neutralDots: Swatch[] = [{ color: '#e6e6e6' }, { color: '#8a8a8a', selected: true }, { color: '#4a4a4a' }]
const navyDots: Swatch[] = [{ color: '#e6e6e6' }, { color: '#4e5d8f', selected: true }, { color: '#4a4a4a' }]

export const carousel: CarouselProduct[] = [
  { id: 'layered', name: 'Urban Layered Looker', price: '$18.70', sizes, colors: neutralDots },
  { id: 'leather', name: 'Classic Leather Jacket', price: '$21.70', sizes, colors: navyDots },
  { id: 'coat', name: 'Cozy Wool Coat', price: '$24.90', sizes, colors: neutralDots },
]

export const navTabs: TabItem[] = [
  { key: 'home', icon: House, label: 'Home' },
  { key: 'search', icon: Search },
  { key: 'bookings', icon: Calendar },
  { key: 'chat', icon: MessageSquareText },
  { key: 'profile', icon: UserRound },
]

export const search = { placeholder: 'Search dresses...' }

export const promo = {
  title: ['Discount up to 45% on every', 'dress rental for events'],
  subtitle: 'Only for this week',
  cta: 'Book Now',
}

export const styleFilters = [
  { key: 'all', label: 'All Styles' },
  { key: 'birthday', label: 'Birthday' },
  { key: 'wedding', label: 'Wedding' },
  { key: 'party', label: 'Party' },
  { key: 'casual', label: 'Casual' },
]

export const gridProducts: GridProduct[] = [
  {
    id: 'velvet',
    name: 'Velvet Muse Dress',
    price: '$25.50',
    colors: [{ color: '#111111' }, { color: '#f3c9e9' }, { color: '#ece6dc' }],
  },
  {
    id: 'classic',
    name: 'Classic Leather Jacket',
    price: '$21.70',
    colors: [{ color: '#5a2c1c' }, { color: '#9a9a9a', selected: true }, { color: '#1f3bd6' }],
  },
  {
    id: 'fringe',
    name: 'Fringe Black Jacket',
    price: '$32.50',
    colors: [{ color: '#111111' }, { color: '#8a8a8a', selected: true }, { color: '#1a73e8' }],
  },
  {
    id: 'faux',
    name: 'Premium Faux Leather',
    price: '$17.50',
    colors: [{ color: '#1b2350' }, { color: '#a58a8a', selected: true }, { color: '#4f7a4a' }],
  },
]
