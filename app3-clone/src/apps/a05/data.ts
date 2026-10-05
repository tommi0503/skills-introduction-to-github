import type { LucideIcon } from 'lucide-react'
import {

  Banknote,
  PersonStanding,
  Clock,
  Mail,
  Leaf,
  RotateCw,

  Star,
  Tag,
  Fish,
  Globe,
} from 'lucide-react'

/* ---------- Welcome ---------- */
export interface AuthOption {
  key: string
  label: string
  /** Lucide glyph, or `brand` when the mark is a logo (rendered as placeholder). */
  icon?: LucideIcon
  brand?: boolean
}

export const welcome = {
  title: 'Welcome to Uber Eats',
  phonePrefix: '+1',
  phonePlaceholder: '(201) 555-0123',
  cta: 'Continue',
  or: 'or',
  options: [
    { key: 'apple', label: 'Continue with Apple', brand: true },
    { key: 'google', label: 'Continue with Google', brand: true },
    { key: 'email', label: 'Continue with Email', icon: Mail },
  ] satisfies AuthOption[],
  more: 'Show more options',
  find: 'Find my account',
}

/* ---------- Home ---------- */
export interface Chip {
  key: string
  label: string
  icon?: LucideIcon
  /** emoji-like coloured glyph → placeholder */
  emoji?: boolean
  active?: boolean
}

export interface Category {
  key: string
  label: string
}

export interface Store {
  key: string
  name: string
  perk: string
  eta?: string
  rating: string
  reviews: string
  rank: string
  promo?: string
  starColor: string
}

export const home = {
  location: 'Home',
  verticals: [
    { key: 'all', label: 'All', emoji: true, active: true },
    { key: 'grocery', label: 'Grocery', emoji: true },
    { key: 'convenience', label: 'Convenience', emoji: true },
    { key: 'alcohol', label: 'Alcohol', emoji: true },
  ] satisfies Chip[],
  categories: [
    { key: 'dine', label: 'Dine Out' },
    { key: 'pizza', label: 'Pizza' },
    { key: 'sushi', label: 'Sushi' },
    { key: 'thai', label: 'Thai' },
    { key: 'chinese', label: 'Chinese' },
  ] satisfies Category[],
  filters: [
    { key: 'one', label: 'Uber One', icon: Globe },
    { key: 'pickup', label: 'Pickup', icon: PersonStanding },
    { key: 'offers', label: 'Offers', icon: Tag },
    { key: 'under', label: 'Under 30 min' },
  ] satisfies Chip[],
  featuredTitle: 'Featured on Uber Eats',
  featured: [
    {
      key: 'delfina',
      name: 'Pizzeria Delfina',
      perk: 'Uber One benefits apply',
      eta: '18 min',
      rating: '4.7',
      reviews: '(2,000+)',
      rank: '#1 Italian',
      starColor: '#f5b400',
    },
    {
      key: 'shack',
      name: 'Shake Shack',
      perk: 'Uber One benefits apply',
      eta: '20 min',
      rating: '4.6',
      reviews: '(5,000+)',
      rank: '#3 Fast Food',
      promo: 'Buy 1, get 1',
      starColor: '#000',
    },
  ] satisfies Store[],
  topTitle: 'Top 10 Fast Food spots',
  topSubtitle: 'Most ordered this week',
  searchLabel: 'Search',
}

/* ---------- Store ---------- */
export interface MenuItem {
  title: string
  price: string
  likes: string
  calories: string
  description: string
  promo: string
}

export const store = {
  name: 'Jack in the Box',
  rating: '4.6',
  reviews: '(1,500+)',
  membership: 'Uber One',
  distance: '2.8 mi',
  address: '1401 Willow Rd',
  social: '410+ people reordered',
  modes: ['Delivery', 'Pickup'],
  activeMode: 'Delivery',
  groupOrder: 'Group order',
  perk: ['Uber One benefits apply on', '$15+'],
  eta: '17 min',
  etaLabel: 'Earliest arrival',
  dealTitle: 'Buy 1, get 1 free',
  deal: {
    title: 'Build Your Own Munchie Meal',
    price: '$15.00',
    likes: '89% (29)',
    calories: '1130 - 2010 Cal.',
    description: 'Pick between 1 of 4 different entrees, 2 sides and a drink to create your own meal.',
    promo: 'Buy 1, get 1 free',
  } satisfies MenuItem,
  exploreTitle: 'Explore Menu',
  menuChips: [
    { key: 'featured', label: 'Featured', icon: Star, active: true },
    { key: 'veg', label: 'Vegetarian', icon: Leaf },
    { key: 'pesc', label: 'Pescatarian', icon: Fish },
  ] satisfies Chip[],
  menuBadge: '#1 most liked',
}

/* ---------- Group order ---------- */
export interface SettingRow {
  key: string
  icon: LucideIcon
  title: string
  value: string
}

export const group = {
  title: "Alex's group order",
  from: 'Jack in the Box',
  deliverTo: '1226 University Dr',
  nudge: 'Set a deadline so your guests know when to add items',
  nudgeCta: 'Try it',
  settings: [
    { key: 'pay', icon: Banknote, title: 'Payment option', value: 'Pay for everyone (no limit)' },
    { key: 'deadline', icon: Clock, title: 'Deadline', value: 'No deadline set' },
    { key: 'freq', icon: RotateCw, title: 'Frequency', value: 'Does not repeat' },
  ] satisfies SettingRow[],
  cta: 'Invite people',
}

