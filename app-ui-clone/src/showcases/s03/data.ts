export type DayStatus = 'done' | 'missed' | 'today' | 'upcoming'

export interface WeekDay {
  label: string
  status: DayStatus
  /** Highlight the label (current day). */
  current?: boolean
}

export interface Stat {
  value: string
  label: string
}

export interface Task {
  id: string
  title: string
  meta: string
  done?: boolean
}

/** A mascot placeholder: size and shape only (the character art itself is an image). */
export interface MascotSpec {
  w: number
  h: number
  radius: string
}

export interface Challenge {
  id: string
  title: string
  meta: string
  bg: string
  mascot: MascotSpec & { x: number; y: number }
}

export const mascots = {
  cloud: { w: 41, h: 31, radius: '48% 52% 45% 45% / 60% 60% 40% 40%' },
  flower: { w: 63.5, h: 55, radius: '45%' },
  pebble: { w: 26, h: 31, radius: '50%' },
  bear: { w: 51.5, h: 51, radius: '46%' },
} satisfies Record<string, MascotSpec>

export const progress = {
  title: 'Progress',
  streak: '12',
  streakLabel: 'days in a row',
  streakNote: ['Finish one session a day and the streak', 'keeps growing. Your record is 19.'],
  weekTitle: 'Last 7 days',
  weekCount: '7 of 7',
  cta: 'Share your streak',
}

export const last7: WeekDay[] = [
  { label: 'S', status: 'done' },
  { label: 'S', status: 'missed' },
  { label: 'M', status: 'done' },
  { label: 'T', status: 'done' },
  { label: 'W', status: 'done' },
  { label: 'T', status: 'done' },
  { label: 'F', status: 'missed', current: true },
]

export const stats: Stat[] = [
  { value: '48', label: 'sessions done' },
  { value: '512', label: 'minutes practiced' },
  { value: '2', label: 'challenges finished' },
  { value: '19', label: 'longest streak' },
]

export const morning = {
  date: 'Friday, 28 August',
  greeting: 'Morning, Olivia',
  weekTitle: 'This week',
  weekCount: '3 of 7',
  challenge: {
    tag: 'Day 4 of 21',
    title: 'Mindful Mornings',
    meta: '10 min · breathing & journaling',
    progressLabel: '3 days done',
    progress: 0.14,
  },
  todayTitle: 'Today',
  todayCount: '1 of 3 done',
  cta: "Continue today's session",
}

export const thisWeek: WeekDay[] = [
  { label: 'M', status: 'missed' },
  { label: 'T', status: 'done' },
  { label: 'W', status: 'done' },
  { label: 'T', status: 'done' },
  { label: 'F', status: 'today', current: true },
  { label: 'S', status: 'upcoming' },
  { label: 'S', status: 'upcoming' },
]

export const tasks: Task[] = [
  { id: 'box', title: 'Box breathing', meta: '3 min · done at 7:12', done: true },
  { id: 'pages', title: 'Morning pages', meta: '7 min · write without stopping' },
  { id: 'intent', title: 'Set one intention', meta: '2 min · one sentence is enough' },
]

export const challengesPage = {
  title: 'Challenges',
  subtitle: 'Pick one you can actually keep',
  featured: { tag: 'Most joined', title: 'Deep Work Sprint', meta: '14 days · one 25-min block, no tabs' },
  listTitle: 'All challenges',
}

export const filters = [
  { key: 'all', label: 'All' },
  { key: 'mind', label: 'Mind' },
  { key: 'body', label: 'Body' },
  { key: 'focus', label: 'Focus' },
]

export const challenges: Challenge[] = [
  { id: 'mm', title: 'Mindful Mornings', meta: '21 days · 10 min', bg: '#fdf0f4', mascot: { ...mascots.flower, w: 39, h: 34, x: 22.5, y: 19 } },
  { id: 'move', title: 'Move Every Day', meta: '30 days · 20 min', bg: '#eff8f3', mascot: { w: 32.5, h: 28, radius: '38%', x: 26, y: 24 } },
  { id: 'sunset', title: 'Digital Sunset', meta: '14 days · from 9pm', bg: '#f7f5fe', mascot: { ...mascots.pebble, w: 29, h: 36, x: 27.5, y: 22.5 } },
  { id: 'grat', title: 'Gratitude Notes', meta: '21 days · 3 min', bg: '#fef5ef', mascot: { ...mascots.cloud, w: 42.5, h: 32, x: 21, y: 20 } },
]
