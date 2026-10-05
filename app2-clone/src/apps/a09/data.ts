import { ClipboardList, CircleUserRound, House, Mail, Search, type LucideIcon } from 'lucide-react'

/* ---------- tab bar ---------- */
export interface FiverrTab {
  key: string
  icon: LucideIcon
  badge?: number
}
export const tabs: FiverrTab[] = [
  { key: 'home', icon: House },
  { key: 'inbox', icon: Mail },
  { key: 'search', icon: Search },
  { key: 'orders', icon: ClipboardList },
  { key: 'profile', icon: CircleUserRound, badge: 1 },
]

/* ---------- home ---------- */
export const home = {
  search: 'Search services',
  popular: { title: 'Popular services', items: ['Logo Design', 'AI Artists', 'Logo Animation'] },
  offers: {
    title: 'My custom offers',
    items: [
      {
        seller: 'Alex Smith',
        title: 'design stunning mobile app UI UX in figma',
        price: '$5',
        delivery: '7 delivery days',
        expires: 'Offer expires on Jun 9, 2026 at 3:39:21 PM',
      },
      {
        seller: 'Alex Smith',
        title: 'design stunning mobile app UI UX in figma',
        price: '$20',
        delivery: '7 delivery days',
        expires: 'Offer expires on Jun 9, 2026 at 3:39:21 PM',
      },
    ],
  },
  orders: { title: 'My active orders', items: [{ price: '$8.78', title: 'Design stunning mobile app ui ux in figma' }] },
  seeAll: 'See All',
}

/* ---------- category ---------- */
export interface FilterChip {
  label: string
  selected?: boolean
  withIcon?: boolean
}
export interface Gig {
  rating: string
  reviews: string
  title: string
  price: string
  badge?: string
}
export const category = {
  title: 'Fashion Design',
  filters: [
    { label: 'All', withIcon: true },
    { label: 'Service type', selected: true },
    { label: 'Seller Level' },
    { label: 'Delivery time' },
  ] as FilterChip[],
  subcategories: ['Technical Drawing & Tech Pack', 'Fashion Illustration', '3D Garment Design'],
  gigs: [
    { rating: '4.7', reviews: '(80)', title: 'Create fashion tech pack and clothing tech pack designs', price: '$5' },
    {
      rating: '4.9',
      reviews: '(787)',
      title: 'Make your professional fashion tech pack for production',
      price: '$20',
      badge: 'FIVERR’S CHOICE',
    },
    { rating: '4.9', reviews: '(119)', title: 'Custom tech pack services for your creative apparel', price: '$10' },
    { rating: '5.0', reviews: '(42)', title: 'Design a tech pack for your clothing brand', price: '$15' },
  ] as Gig[],
}

/* ---------- gig ---------- */
export interface PackageFact {
  label: string
  value?: string
}
export const gig = {
  imageCounter: '1 of 3',
  seller: 'Alex Smith',
  title: 'Design stunning mobile app UI UX in figma',
  description:
    'Hi! Im Alex Smith, an award-winning Senior Product Designer with over 7 years of professional experience crafting high-converting digital products for mobile apps (iOS & Android)...',
  more: 'More',
  packages: ['$495', '$250', '$50'],
  activePackage: 1,
  packageName: 'MVP Mobile App Design',
  packageText: 'Up to 5 screens UI/UX design. Includes user flow optimization, custom assets, and source file.',
  facts: [
    { label: 'Delivery days', value: '7 Days' },
    { label: 'Revisions' },
    { label: 'Number of pages or screens', value: '5' },
  ] as PackageFact[],
  chat: 'Chat',
}

/* ---------- seller profile ---------- */
export const seller = {
  name: 'Bhavik C',
  handle: '@mewindson',
  badge: 'Vetted Pro',
  rating: '4.8',
  reviews: '(16,690)',
  level: 'Top Rated',
  save: 'Save',
  contact: 'Contact',
  tabs: ['About', 'Gigs', 'Reviews', 'Portfolio', 'Clients'],
  vettedTitle: 'Vetted by Fiverr Pro',
  vettedText: 'Bhavik C was selected by the Fiverr Pro team for their expertise.',
  vettedForTitle: 'Vetted for',
  vettedFor: ['Logo Animation', 'Brand Style Guides', 'Logo Design'],
  hourly: 'Offers hourly rates',
  infoTitle: 'User information',
  bio: 'Hi, I’m Windson (Bhavik Chauhan), a graphic and web designer from India. I’ve worked with 50,000+ businesses worldwide and successfully...',
  more: 'More',
  from: { label: 'From', value: 'India (Mon 9:23 AM)' },
}
