import type { LucideIcon } from 'lucide-react'
import { Bookmark, Headphones, Share, BookOpen, Layers, Sun, Moon } from 'lucide-react'

export interface Plan {
  key: string
  name: string
  badge?: string
  detail: string
  price: string
  unit: string
  selected?: boolean
}
export const plans: Plan[] = [
  { key: 'weekly', name: 'Weekly', detail: 'SGD 6.98 per week', price: 'SGD 6.98', unit: 'per week' },
  { key: 'annual', name: 'Annually +', badge: 'BIRTH CHART', detail: 'SGD 28.98 per year', price: 'SGD 0.60', unit: 'per week', selected: true },
  { key: 'life', name: 'Lifetime +', badge: 'BIRTH CHART', detail: 'Pay once, enjoy forever', price: 'SGD 59.98', unit: 'one-time' },
]

export interface Included {
  label: string
  emoji?: boolean
}
export const included: Included[][] = [
  [{ label: 'Birth Chart', emoji: true }, { label: '24/7 Astrologer Chat' }],
  [{ label: 'Personal Program' }, { label: 'Dream Readings' }],
  [{ label: 'Daily Horoscope' }, { label: 'Moon Calendar' }],
  [{ label: 'Tarot Readings' }, { label: 'Compatibility' }],
  [{ label: 'Affirmations' }, { label: 'Meditations' }, { label: 'Rituals' }],
]

export interface Day {
  dow: string
  date: number
  star?: boolean
  selected?: boolean
}
export const week: Day[] = [
  { dow: 'SUN', date: 24 },
  { dow: '', date: 25, star: true, selected: true },
  { dow: 'TUE', date: 26 },
  { dow: '', date: 27, star: true },
  { dow: 'THU', date: 28 },
]

export interface Shortcut {
  key: string
  kicker: string
  title: string
}
export const shortcuts: Shortcut[] = [
  { key: 'dream', kicker: 'DREAMER', title: 'Decode Dream' },
  { key: 'tarot', kicker: 'TAROT', title: 'Ask Cards' },
]

export const horoscope = {
  kicker: 'BASED ON YOUR BIRTH CHART',
  title: 'Daily Horoscope',
  date: 'MAY 25',
  focus: 'Protecting your peace is the most productive thing you’ll do all week',
  body: 'You’re feeling pretty solid, and connecting with others feels easy and natural. Big decisions come with a surprising clarity, but don’t fret if work tasks drag their heels a bit.',
  cta: 'When’s my Moon-Blessed date?',
}

export interface Tab {
  key: string
  label: string
  icon: LucideIcon
}
export const tabs: Tab[] = [
  { key: 'calendar', label: 'Calendar', icon: Moon },
  { key: 'practice', label: 'Practice', icon: Layers },
  { key: 'healing', label: 'Healing', icon: Headphones },
  { key: 'learning', label: 'Learning', icon: BookOpen },
  { key: 'you', label: 'You', icon: Sun },
]

export interface ShareAction {
  key: string
  /** Lucide glyph; brand marks (TikTok, Instagram) fall back to a placeholder. */
  icon?: LucideIcon
}
export const shareActions: ShareAction[] = [{ key: 'share', icon: Share }, { key: 'tiktok' }, { key: 'instagram' }]
export const bookmarkIcon = Bookmark

export const article = {
  title: 'Lunar Cycle Nutrition',
  category: 'LIFESTYLE',
  duration: '6 MIN',
  heading: 'Lunar cycle nutrition',
  body: 'Our lifestyle defines the way we feel in this world. Suitable diet, work and rest hours, good sleep, creating a safe space at home — all these things can take our life to a whole new level. To keep balance in the body and mind, it’s better to follow natural rhythms, which includes the Lunar cycle.',
  steps: 14,
  step: 0,
}
