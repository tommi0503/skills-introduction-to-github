import { Building2, Flag, Globe, Mountain, type LucideIcon } from 'lucide-react'

export interface Category {
  key: string
  icon: LucideIcon
  /** Centre position inside the cluster (logical points). */
  x: number
  y: number
  size: number
  bg: string
  fg: string
}

export interface ChatEntry {
  id: string
  from: 'user' | 'ai'
  lines: string[]
  time: string
}

export type DayState = 'default' | 'selected' | 'photo' | 'pending' | 'faded'

export interface MonthSpec {
  title: string
  /** Weekday index (0 = Sun) of the 1st. */
  offset: number
  days: number
  states: Record<number, DayState>
}

export const steps = { total: 5 }

export const whereTo = {
  title: 'Where to next?',
  subtitle: 'Country region or city pick anything',
  search: 'Search a destination',
  emptyTitle: 'Start typing',
  emptySubtitle: 'The best destinations will appear here',
}

/** Destination photo bubbles fanned along the arc (centre x/y, diameter). */
export const arcPhotos = [
  { x: 71, y: 293, d: 51 },
  { x: 107, y: 268, d: 51 },
  { x: 161, y: 250, d: 51 },
  { x: 215, y: 250, d: 51 },
  { x: 266, y: 268, d: 51 },
  { x: 305, y: 293, d: 51 },
]

/** Globe-search sits in the middle of the cluster; others orbit around it. */
export const categories: Category[] = [
  { key: 'search', icon: Globe, x: 187.5, y: 55, size: 50, bg: '#ececec', fg: '#2a2a2a' },
  { key: 'world', icon: Globe, x: 115, y: 74, size: 43, bg: '#ebe7fd', fg: '#8b5cf6' },
  { key: 'nature', icon: Mountain, x: 260, y: 74, size: 43, bg: '#fde8d3', fg: '#ea6a2a' },
  { key: 'city', icon: Building2, x: 153, y: 128, size: 43, bg: '#d3f5e5', fg: '#1aa26c' },
  { key: 'culture', icon: Flag, x: 222, y: 128, size: 43, bg: '#fdefbf', fg: '#de9b12' },
]

export const chat = {
  title: 'Travio AI',
  dayLabel: 'Today',
  composer: 'Ask me anything...',
  typing: 'AI is planning your trip',
}

export const messages: ChatEntry[] = [
  { id: 'm1', from: 'user', lines: ["I'm planning a 7-day trip to Bali", 'around August 28th.'], time: '10:28 AM' },
  {
    id: 'm2',
    from: 'ai',
    lines: ['Great choice! I can help you plan the', 'best of Bali, from beaches and temples', 'to local food and hidden gems.'],
    time: '10:29 AM',
  },
]

export const trip = { dates: '28 aug - 03 sep', title: 'Trip to Bali', place: 'Bali, Indonesia' }

export const dates = {
  eyebrow: 'Plan your journey',
  title: 'When are you leaving?',
  cta: 'Continue',
}

export const durations = [
  { key: 'weekend', label: 'Weekend' },
  { key: '3n', label: '3 Nights' },
  { key: '1w', label: '1 Week' },
  { key: '2w', label: '2 Weeks' },
]

export const weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

export const months: MonthSpec[] = [
  { title: 'August 2026', offset: 4, days: 31, states: { 28: 'photo', 29: 'selected', 30: 'selected', 31: 'selected' } },
  { title: 'September 2026', offset: 4, days: 17, states: { 1: 'pending', 2: 'pending', 3: 'photo' } },
]
