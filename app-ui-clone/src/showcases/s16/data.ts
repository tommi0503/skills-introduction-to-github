import { Apple, Bell, BookOpen, SportShoe, House, Salad, Shirt, FileText, User, type LucideIcon } from 'lucide-react'

export type StepState = 'done' | 'current' | 'pending'

export interface FeaturedShipment {
  title: string
  code: string
  status: string
  steps: StepState[]
  facts: { icon: 'pin' | 'calendar'; label: string; value: string }[]
}

export type ChipTone = 'blue' | 'amber' | 'grey'

export interface ShipmentRow {
  id: string
  title: string
  code: string
  status: string
  tone: ChipTone
}

export const locationScreen = {
  title: 'Location',
  place: 'New york, USA',
  search: 'Search',
  notifications: 3,
  segments: [
    { key: 'active', label: 'Active' },
    { key: 'delivered', label: 'Delivered' },
    { key: 'archived', label: 'Archived' },
    { key: 'saved', label: 'Saved' },
  ],
  activeSegment: 'active',
  sectionTitle: 'Current shipment',
  sectionAction: 'See all',
  featured: {
    title: 'MacBook Pro 16"',
    code: 'USPS- 33005282',
    status: 'Transit',
    steps: ['done', 'done', 'current', 'pending'],
    facts: [
      { icon: 'pin', label: 'Location', value: 'Pakistan' },
      { icon: 'pin', label: 'Deliver Date', value: '06 Mar 26' },
    ],
  } satisfies FeaturedShipment,
  rows: [
    { id: 'mbp', title: 'Mac Book Pro 16', code: 'USPS: 33005282', status: 'In Transit', tone: 'blue' },
    { id: 'nike', title: 'Nike Air Max 90', code: 'USPS: 23456784', status: 'Out for Delivery', tone: 'amber' },
  ] satisfies ShipmentRow[],
}

export const deliveryScreen = {
  title: 'Delivery Details',
  place: { label: 'Work', action: 'Edit', address: '500 Terry A Francois Blvd, San Francisco, CA 94158, USA' },
  helpCta: 'Help the Driver Find You (Optional)',
  recipient: {
    title: 'Delivery Recipient',
    action: 'Use my details',
    fields: [
      { key: 'name', label: 'Receiver', placeholder: 'Recipient name' },
      { key: 'phone', label: 'Contact number', placeholder: 'Type phone number' },
    ],
  },
  packageTitle: 'What kind of package?',
  packageKinds: [
    { key: 'food', label: 'Food', icon: Salad },
    { key: 'book', label: 'Book', icon: BookOpen },
    { key: 'doc', label: 'Document', icon: FileText },
  ] satisfies { key: string; label: string; icon: LucideIcon }[],
  save: 'Save',
}

export interface Store {
  key: string
  name: string
  perk: string
  /** lucide glyph, or null when the mark is a brand logo (placeholder). */
  icon: LucideIcon | null
}

export const discoverScreen = {
  title: 'Discover',
  heading: 'Shop Your Way',
  promo: { eyebrow: 'Exclusive Deals', lines: ['Save up to ', '70%', ' on', 'trending items'], cta: 'Active' },
  categoriesTitle: 'Categories',
  categories: [
    { key: 'fashion', label: 'Fashion' },
    { key: 'tech', label: 'Tech' },
    { key: 'home', label: 'Home' },
    { key: 'beauty', label: 'Beauty' },
    { key: 'sports', label: 'Sports' },
  ],
  activeCategory: 'fashion',
  storesTitle: 'Featured Stores',
  stores: [
    { key: 'nike', name: 'Nike Shoes', perk: '15% OFF', icon: SportShoe },
    { key: 'apple', name: 'Apple', perk: 'Free shipping', icon: Apple },
    { key: 'amazon', name: 'Amazon', perk: 'Prime Deals', icon: null },
    { key: 'shein', name: 'Shein', perk: 'Up to 70% OFF', icon: Shirt },
  ] satisfies Store[],
  trendingTitle: 'Trending',
  trending: { title: 'ID: P1873h563830', subtitle: 'JBL Speaker', status: 'On process' },
}

export const navIcons = { House, Bell, User }
