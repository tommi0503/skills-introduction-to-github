import {
  CircleUserRound,
  Heart,
  MessageSquare,
  Navigation,
  Search,
  type LucideIcon,
} from 'lucide-react'

/* ---------- shared ---------- */
export interface Vertical {
  key: string
  label: string
  isNew?: boolean
}
export const verticals: Vertical[] = [
  { key: 'homes', label: 'Homes' },
  { key: 'experiences', label: 'Experiences', isNew: true },
  { key: 'services', label: 'Services', isNew: true },
]
export const activeVertical = 'homes'

export interface NavTab {
  key: string
  label: string
  /** null → brand mark (placeholder). */
  icon: LucideIcon | null
  dot?: boolean
}
export const navTabs: NavTab[] = [
  { key: 'explore', label: 'Explore', icon: Search },
  { key: 'wishlists', label: 'Wishlists', icon: Heart },
  { key: 'trips', label: 'Trips', icon: null },
  { key: 'messages', label: 'Messages', icon: MessageSquare },
  { key: 'profile', label: 'Profile', icon: CircleUserRound, dot: true },
]

/* ---------- screen 1 · home feed ---------- */
export interface Stay {
  id: string
  title: string
  price: string
  rating: string
  guestFavorite: boolean
}
export interface StayRow {
  id: string
  title: string
  stays: Stay[]
}
export const feed = {
  searchLabel: 'Start your search',
  rows: [
    {
      id: 'philly',
      title: 'Popular homes in Philadelphia',
      stays: [
        { id: 'a', title: 'Apartment in Center City', price: '$228 for 2 nights', rating: '4.97', guestFavorite: true },
        { id: 'b', title: 'Place to stay in Strawberry Mansion', price: '$122 for 2 nights', rating: '4.8', guestFavorite: false },
        { id: 'c', title: 'Apartment in Fishtown', price: '$240 for 2 nights', rating: '4.9', guestFavorite: false },
      ],
    },
    {
      id: 'miami',
      title: 'Available next month in Miami',
      stays: [
        { id: 'd', title: 'Apartment in Brickell', price: '$381 for 2 nights', rating: '5.0', guestFavorite: true },
        { id: 'e', title: 'Condo in Miami Beach', price: '$112 for 2 nights', rating: '4.99', guestFavorite: true },
        { id: 'f', title: 'Room in Wynwood', price: '$140 for 2 nights', rating: '4.9', guestFavorite: false },
      ],
    },
  ] satisfies StayRow[],
  toast: 'Prices include all fees',
}

/* ---------- screen 2 · where? ---------- */
export interface Suggestion {
  id: string
  title: string
  lines: string[]
  /** lucide glyph on a tinted tile, or null → illustration placeholder. */
  icon: LucideIcon | null
}
export const where = {
  title: 'Where?',
  placeholder: 'Search destinations',
  suggestedLabel: 'Suggested destinations',
  suggestions: [
    { id: 'nearby', title: 'Nearby', lines: ['Find what’s around you'], icon: Navigation },
    { id: 'pocono', title: 'Pocono Mountains, PA', lines: ['Popular lake destination'], icon: null },
    { id: 'orlando', title: 'Orlando, FL', lines: ['For sights like', 'Walt Disney World Resort'], icon: null },
    { id: 'philly', title: 'Philadelphia, PA', lines: ['For its top-notch dining'], icon: null },
  ] satisfies Suggestion[],
  fields: [
    { label: 'When', value: 'Add dates' },
    { label: 'Who', value: 'Add guests' },
  ],
  clear: 'Clear all',
  search: 'Search',
}

/* ---------- screen 3 · listing ---------- */
export const listing = {
  counter: '1 / 27',
  title: ['Private bedroom in', 'Manhattan Upper East Side'],
  subtitle: ['Room in New York, United States', '1 queen bed · Shared bathroom'],
  rating: '4.96',
  badge: ['Guest', 'favorite'],
  reviews: '298',
  reviewsLabel: 'Reviews',
  host: { title: 'Stay with Allison', sub: 'Superhost · 7 years hosting' },
  rare: 'Rare find! This place is usually booked',
  price: '$356',
  priceSub: 'For 2 nights · Sep 5 – 7',
  freeCancel: 'Free cancellation',
  cta: 'Reserve',
}

/* ---------- screen 4 · review & continue ---------- */
export interface ReviewSection {
  title: string
  lines: { text: string; link?: string }[]
  action?: string
}
export const review = {
  title: 'Review and continue',
  stay: { title: 'Private bedroom in Manhattan Upper East Side', rating: '4.96 (298)', badge: 'Guest favorite' },
  sections: [
    { title: 'Trip details', lines: [{ text: 'Sep 5 – 6, 2025' }, { text: '1 adult' }], action: 'Change' },
    { title: 'Total price', lines: [{ text: '$201.54 including taxes', link: 'USD' }], action: 'Details' },
    { title: 'Free cancellation', lines: [{ text: 'Cancel before Sep 4 for a full refund.', link: 'Full policy' }] },
  ] satisfies ReviewSection[],
  payTitle: 'Choose when to pay',
  payOptions: [
    { key: 'now', title: 'Pay $201.54 now' },
    {
      key: 'part',
      title: 'Pay part now, part later',
      sub: '$40.31 now,  $161.23 charged on Aug 27. No extra fees.',
      link: 'More info',
    },
  ],
  payChoice: 'now',
  steps: 4,
  step: 1,
  cta: 'Next',
}
