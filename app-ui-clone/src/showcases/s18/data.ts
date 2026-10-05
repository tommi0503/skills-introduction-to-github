import { House, Sparkles, UserRound, type LucideIcon } from 'lucide-react'
import type { CardTone } from './theme'

export interface TabEntry {
  key: string
  label?: string
  icon: LucideIcon | 'explore'
}

export const tabs: TabEntry[] = [
  { key: 'home', label: 'Home', icon: House },
  { key: 'explore', label: 'Explore', icon: 'explore' },
  { key: 'ai', label: 'Ask AI', icon: Sparkles },
  { key: 'profile', icon: UserRound },
]

export interface FanCard {
  dx: number
  top: number
  w: number
  h: number
  rotate: number
}

export interface Pick {
  key: string
  tone: CardTone
  badge: string
  title: string
  price: string
  cta: string
}

export const homeScreen = {
  greeting: 'Good Morning',
  name: 'Juliette Amara',
  headline: ['Personalized to your', 'taste & weather'],
  /** Fanned dish photos: horizontal offset from centre, top, size and tilt (logical pt / deg). */
  fan: [
    { dx: -113, top: 40, w: 58, h: 72, rotate: -22 },
    { dx: -64, top: 14, w: 62, h: 86, rotate: -8 },
    { dx: 67, top: 14, w: 62, h: 86, rotate: 8 },
    { dx: 126, top: 40, w: 58, h: 72, rotate: 22 },
    { dx: 0, top: 0, w: 66, h: 92, rotate: 0 },
  ] satisfies FanCard[],
  hint: "It's warm today, so I picked something light and refreshing",
  picks: [
    { key: 'left', tone: 'pink', badge: 'AI pick for you', title: 'Spicy Ramen Bowl', price: '$14.99', cta: 'Add to order' },
    { key: 'main', tone: 'blue', badge: 'AI pick for you', title: 'Grilled Chicken Bowl', price: '$14.99', cta: 'Add to order' },
    { key: 'right', tone: 'yellow', badge: 'AI pick for you', title: 'Shoyu Chicken', price: '$12.49', cta: 'Add to order' },
  ] satisfies Pick[],
}

export interface Trending {
  key: string
  tone: CardTone
  name: string
  rating: string
}

export const exploreScreen = {
  title: 'Explore',
  search: 'Search dishes,restaurants,cuisines...',
  askTitle: 'Ask AI what to eat',
  askThumbs: 3,
  askText: "Use these recipes you liked to suggest a full day's healthy meal plan for under $25.",
  askPlaceholder: 'Ask anything about food...',
  trendingTitle: 'Trending near you',
  trendingAction: 'See more',
  trending: [
    { key: 'hermitage', tone: 'yellow', name: 'Hermitage Bistro', rating: '4.8' },
    { key: 'rustic', tone: 'blue', name: 'The Rustic Patty', rating: '4.8' },
  ] satisfies Trending[],
}

export type ChatMessage =
  | { key: string; from: 'user' | 'bot'; lines: string[] }
  | { key: string; from: 'matches' }

export const askScreen = {
  title: 'Ask AI',
  messages: [
    { key: 'u1', from: 'user', lines: ["I'm craving something spicy", 'but not too heavy.'] },
    { key: 'b1', from: 'bot', lines: ['3 matches found. Best pick:', 'Spicy Chicken Bowl.'] },
    { key: 'm', from: 'matches' },
    { key: 'u2', from: 'user', lines: ["I'm craving something spicy", 'but not too heavy.'] },
  ] satisfies ChatMessage[],
  match: { name: 'Hermitage Bistro', note: 'High protein food', score: '90% mass' },
  pages: 3,
  input: "Tell me what you're craving...",
}
