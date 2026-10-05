import type { LucideIcon } from 'lucide-react'
import { ChartNoAxesColumn, Droplets, Drumstick, House, Settings, Wheat } from 'lucide-react'
import { theme } from './theme'

export interface WeekDay {
  letter: string
  day: number
  state: 'done' | 'today' | 'future'
}

export interface Macro {
  amount: string
  name: string
  color: string
  progress: number
  icon: LucideIcon
}

export interface Tab {
  label: string
  icon: LucideIcon
  active?: boolean
}

export const home = {
  brand: 'Cal AI',
  streak: 1,
  week: [
    { letter: 'W', day: 27, state: 'done' },
    { letter: 'T', day: 28, state: 'done' },
    { letter: 'F', day: 29, state: 'done' },
    { letter: 'S', day: 30, state: 'done' },
    { letter: 'S', day: 31, state: 'done' },
    { letter: 'M', day: 1, state: 'today' },
    { letter: 'T', day: 2, state: 'future' },
  ] as WeekDay[],
  calories: { value: 1505, label: 'Calories left', progress: 0.55 },
  macros: [
    { amount: '129g', name: 'Protein', color: theme.protein, progress: 0.3, icon: Drumstick },
    { amount: '247g', name: 'Carbs', color: theme.carbs, progress: 0.2, icon: Wheat },
    { amount: '7g', name: 'Fat', color: theme.fat, progress: 0.96, icon: Droplets },
  ] as Macro[],
  pages: 3,
  recentTitle: 'Recently uploaded',
  recent: {
    name: 'Fried Chicken...',
    time: '10:10 PM',
    calories: '988 calories',
    macros: ['54g', '39g', '60g'],
  },
  tabs: [
    { label: 'Home', icon: House, active: true },
    { label: 'Progress', icon: ChartNoAxesColumn },
    { label: 'Settings', icon: Settings },
  ] as Tab[],
}

export const profile = {
  title: 'Profile',
  heading: 'Weekly summary',
  activity: {
    title: 'Activity',
    days: [
      { letter: 'M', count: 0 },
      { letter: 'T', count: 0 },
      { letter: 'W', count: 3, current: true },
      { letter: 'T', count: 0 },
      { letter: 'F', count: 0 },
      { letter: 'S', count: 0 },
      { letter: 'S', count: 0 },
    ],
    goal: { title: 'Weekly goal', sub: '3/7 activities completed', progress: 3 / 7 },
    cta: 'Continue learning',
  },
  reviews: {
    title: 'Reviews',
    stats: [
      { label: 'Average score', value: '75%' },
      { label: 'New items', value: '11' },
    ],
    method: 'Review method',
  },
  trial: { prefix: 'Your free trial will end in ', emphasis: '6 days' },
}
