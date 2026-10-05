import type { LetterBlock } from './components/LetterBlocks'
import { ClipboardList, Heart, Pentagon, UserRound, type LucideIcon } from 'lucide-react'

export interface Category {
  key: string
  label: string
}

export interface Restaurant {
  key: string
  name: string
  rating: string
  reviews: string
  price: string
  kind: string
  promo: string
}

export interface NavItem {
  key: string
  label: string
  icon?: LucideIcon
}

export interface Offer {
  key: string
  title: string
  description: string
  icon: 'badge' | 'crown'
}

export interface Product {
  key: string
  name: string
  price: string
  oldPrice?: string
}

export const welcome = {
  ribbon: 'Earn Crowns - Join Now',
  titleLines: ['Welcome to', 'Food Zone'],
  primaryCta: 'Continue with Email',
  secondaryCta: 'Order Delivery',
  legal: {
    prefix: 'By tapping Search Nearby or Continue with Email, Google, Facebook, or Apple, you agree to DoorDash’s ',
    terms: 'Terms & Conditions',
    joiner: ' and ',
    privacy: 'Privacy Policy.',
  },
}

export const home = {
  locationLabel: 'Delivery location',
  address: '351 Maison Street, NY',
  promoValue: '15%',
  promoLines: ['EXTRA', 'DISCOUNT'],
  promoCopy: ['Get your first order', 'delivery free!'],
  searchPlaceholder: 'Search by name & restaurant',
  sectionTitle: 'Popular Restaurants',
}

export const categories: Category[] = [
  { key: 'burger', label: 'Burger' },
  { key: 'steak', label: 'Steak' },
  { key: 'seafood', label: 'Sea Food' },
  { key: 'desserts', label: 'Desserts' },
  { key: 'pizza', label: 'Pizza' },
  { key: 'bbq', label: 'BBQ' },
]

export const restaurants: Restaurant[] = [
  { key: 'mcd', name: 'McDonald’s', rating: '4.8', reviews: '(1,652)', price: '$$', kind: 'Pizza Joint', promo: '15% off: NEW15' },
  { key: 'ny', name: 'New York Pizza', rating: '4.6', reviews: '(980)', price: '$$', kind: 'Pizza Joint', promo: '15% off: NEW15' },
]

export const navItems: NavItem[] = [
  { key: 'home', label: 'Home', icon: Pentagon },
  { key: 'saved', label: 'Saved', icon: Heart },
  { key: 'cart', label: 'Cart' },
  { key: 'orders', label: 'Orders', icon: ClipboardList },
  { key: 'profile', label: 'Profile', icon: UserRound },
]

export const restaurantDetail = {
  name: 'McDonald’s Maison',
  rating: '4.8',
  reviews: '(1,652)',
  tier: 'FoodyPro+',
  distance: '0.1 mi',
  deliveryTitle: 'Delivery Time: 10-20 min',
  deliveryMeta: ['Charge: 3.5$', 'Min. Order: 27$'],
}

export const offers: Offer[] = [
  { key: '50', title: '50% off', description: 'Minimum order $20. Valid for all items. Auto-applied.', icon: 'badge' },
  { key: '30', title: '30% off', description: 'Minimum order $15. Valid for all items. Auto-applied.', icon: 'crown' },
]

export const menuTabs = ['Popular', 'Appetizer', 'Burger', 'Steak', 'Pizza']

export const products: Product[] = [
  { key: 'bigmac', name: 'Big Mac Burger', price: '$4.50', oldPrice: '$6.50' },
  { key: 'surf', name: 'Surf Cheeseburgers', price: '$10', oldPrice: '$12.50' },
  { key: 'meal', name: 'McDo Meal', price: '$8', oldPrice: '$9.50' },
  { key: 'nuggets', name: 'Chicken Nuggets', price: '$5', oldPrice: '$6' },
]

export const letterBlocks: LetterBlock[] = [
  { key: 'f', x: 230, slotX: 63 },
  { key: 'o1', x: 377, slotX: 63 },
  { key: 'o2', x: 526, slotX: 63 },
  { key: 'd', x: 675, slotX: 63, radius: '22px 46px 22px 22px' },
]

export const captions = { left: 'Vislume Studio', right: 'Let’s discuss your crazy idea?' }
