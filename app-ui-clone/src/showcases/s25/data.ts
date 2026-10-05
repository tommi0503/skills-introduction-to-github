import type { LucideIcon } from 'lucide-react'
import { ArrowBigUp, Cloud, CornerDownLeft, Delete, House, Inbox } from 'lucide-react'

/* ---------- Splash ---------- */
export const splash = {
  brand: 'bond',
  legal: { lead: 'By tapping Continue you accept our', links: ['Privacy Policy', 'Terms of Service'] as const },
  cta: 'Continue',
}

/* ---------- Home ---------- */
export type StoryVisual = 'add' | 'stack' | 'card' | 'photo'

export interface Story {
  id: string
  name: string
  time?: string
  visual: StoryVisual
  /** Seen stories render their name in grey. */
  seen?: boolean
  /** Avatar badge tone (photo placeholder). */
  badge?: 'photo' | 'brand'
}

export const stories: Story[] = [
  { id: 'add', name: 'Add Story', visual: 'add', seen: true },
  { id: 'alex', name: 'Alex Smithh', time: 'Just now', visual: 'stack', badge: 'photo' },
  { id: 'bond', name: 'Bond', time: '3 wk ago', visual: 'card', seen: true, badge: 'brand' },
  { id: 'sam', name: 'Sam Lee', time: '6 min ago', visual: 'photo', badge: 'photo' },
]

export const home = {
  friendsTitle: 'Friends you may know',
  discoverPlaceholder: 'Discover using your memories',
  memoryCount: '1',
}

export interface BondTab {
  key: string
  icon: LucideIcon
}

export const bondTabs: BondTab[] = [
  { key: 'memories', icon: Cloud },
  { key: 'home', icon: House },
  { key: 'inbox', icon: Inbox },
]

/* ---------- Discover ---------- */
export interface Suggestion {
  emoji: string
  text: string
}

export const suggestions: Suggestion[] = [
  { emoji: '🍽️', text: 'Best food to get right now' },
  { emoji: '🌇', text: 'Perfect place to go out on Friday' },
  { emoji: '🎬', text: 'TV show that I will love' },
]

export const discover = {
  title: 'Discover',
  memoryCount: '0',
  participant: 'SA',
  query: 'Best matcha place in New York',
}

/* ---------- Keyboard ---------- */
export interface KeySpec {
  label?: string
  icon?: LucideIcon
  /** Width in pt; letters default to the keyboard's key width. */
  width?: number
  /** Extra left margin in pt (beyond the normal gap). */
  offset?: number
  /** Light-grey function key face (shift/delete/123/return). */
  fn?: boolean
}

const letters = (s: string): KeySpec[] => s.split('').map((label) => ({ label }))

export const qwertyRows: KeySpec[][] = [
  letters('qwertyuiop'),
  letters('asdfghjkl'),
  [
    { icon: ArrowBigUp, width: 43 },
    ...letters('zxcvbnm').map((k, i) => (i === 0 ? { ...k, offset: 6.5 } : k)),
    { icon: Delete, width: 43, offset: 8 },
  ],
  [
    { label: '123', width: 89 },
    { label: '', width: 186.5 },
    { icon: CornerDownLeft, width: 89 },
  ],
]

/* ---------- Place detail ---------- */
export const place = {
  query: 'Best matcha place in New York',
  photos: [56, 90, 178] as const,
  name: 'Plentea Matcha (Served in Neighbors Café) Matcha La...',
  category: 'Cafe',
  rating: '4.7',
  address: '60 Furman St, Brooklyn, NY 11201, USA',
  summary: [
    { text: "If you're looking for the best-rated spot, you have to try " },
    { text: 'Plentea Matcha', bold: true },
    {
      text:
        ' inside Neighbors Café. It’s highly praised for its smooth, nutty flavor and lack of bitterness, which makes it a favorite for both matcha lovers and former coffee addicts. Plus, the location at Pier 1 offers some great views while you enjoy your drink!',
    },
  ],
  less: 'less',
  memories: 'No related memories available',
  actions: { secondary: 'Finalize', primary: 'Regenerate' },
}

/* ---------- Detail / members ---------- */
export const detail = {
  title: 'Detail',
  emoji: '🍽️',
  heading: 'Best matcha place in New York',
  meta: ['Best rated', 'New York City'],
  membersLabel: 'Members (2)',
}

export interface Member {
  id: string
  name: string
  kind: 'photo' | 'initials' | 'invite'
  initials?: string
  action?: string
}

export const members: Member[] = [
  { id: 'alex', name: 'Alex Smith', kind: 'photo' },
  { id: 'sam', name: 'Samsam', kind: 'initials', initials: 'SA', action: 'Connect' },
  { id: 'add', name: 'Add friends', kind: 'invite' },
]
