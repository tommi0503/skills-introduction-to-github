import { Check, Delete, type LucideIcon } from 'lucide-react'
import type { KeyTone } from './theme'

export const stageCopy = {
  kicker: 'UI/UX Design',
  product: ['Investment', 'App'],
  headline: ['Your Strategy', 'Your Rules'],
  body: ['Banking made simple for everyone Smart tools for', 'smarter spending'],
  bigWord: 'Investment',
}

export const ethereum = { name: 'Ethereum', price: '$360.80', change: '+6.40%' }

export const portfolio = {
  title: 'Starbucks',
  amount: '250k',
  change: '25.6%',
  changeCaption: 'from last month',
  ranges: ['1D', '1W', '4M', '8M'],
  activeRange: '1W',
  tooltip: '$108.00',
  months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
  activeMonth: 'Mar',
  sectionTitle: 'All Transaction',
  filters: ['Today', 'This Week', 'This Mount'],
  activeFilter: 'Today',
  transaction: { merchant: 'Dribbble', kind: 'Payment', amount: '- $24.00', date: '2 Dec 2024 • 3:09 PM' },
}

export type Point = [number, number]

/** Chart layers (logical screen coords), back to front. */
export const chartLayers: Point[][] = [
  [[14, 427], [30, 406], [84, 422], [127, 402], [148, 394], [191, 406], [218, 393], [251, 423], [277, 406], [298, 411], [347, 405], [393, 456]],
  [[14, 438], [57, 427], [111, 444], [154, 422], [202, 438], [234, 454], [277, 438], [320, 449], [352, 427], [393, 461]],
  [[14, 460], [84, 454], [137, 470], [202, 449], [256, 481], [298, 460], [352, 476], [393, 499]],
]
export const chartGrid = { rows: [407, 500, 548], markerX: 253, markerY: 423, bottom: 552 }

export const topUp = {
  title: 'Top Up',
  amount: '28.5k',
  currency: 'USD',
  recipient: { name: 'Anne Smith', card: '**** 1887 2532' },
  presets: ['$10k', '$20k', '$30k', '$40k', '$50k'],
  activePreset: '$20k',
}

export interface KeypadKey {
  key: string
  label?: string
  icon?: LucideIcon
  tone: KeyTone
  /** Grid placement (1-based). */
  col: number
  row: number
  rowSpan?: number
}

const digits: KeypadKey[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9'].map((d, i) => ({
  key: d,
  label: d,
  tone: 'plain',
  col: (i % 3) + 1,
  row: Math.floor(i / 3) + 1,
}))

export const keypad: KeypadKey[] = [
  ...digits,
  { key: '$', label: '$', tone: 'success', col: 1, row: 4 },
  { key: '0', label: '0', tone: 'plain', col: 2, row: 4 },
  { key: '.', label: '.', tone: 'plain', col: 3, row: 4 },
  { key: 'del', icon: Delete, tone: 'warning', col: 4, row: 1 },
  { key: 'clear', label: 'C', tone: 'danger', col: 4, row: 2 },
  { key: 'ok', icon: Check, tone: 'primary', col: 4, row: 3, rowSpan: 2 },
]
