export type NavKey = 'home' | 'stats' | 'journal' | 'season' | 'friends' | 'more'
export const navOrder: NavKey[] = ['home', 'stats', 'journal', 'season', 'friends', 'more']

export const headerStats = [
  { key: 'streak', icon: 'flame' as const, value: '0' },
  { key: 'trophy', icon: 'trophy' as const, value: '1', dot: true },
  { key: 'xp', icon: 'sparkle' as const, value: '348' },
]

export const today = {
  day: 'Day 1/66',
  motto: "It's your first day. Don't screw it.",
  tabs: [
    { key: 'todo', label: 'To-dos', count: 5 },
    { key: 'done', label: 'Done', count: 0 },
    { key: 'skipped', label: 'Skipped', count: 0 },
  ],
}

export interface Habit {
  id: string
  title: string
  badge: { kind: 'welcome' | 'streak'; label: string }
  highlight?: boolean
  infoDim?: boolean
  /** flat placeholder tone of the illustration */
  tone: string
}

export const habits: Habit[] = [
  { id: 'breaths', title: '2 Deep Breaths', badge: { kind: 'welcome', label: 'Day 1 Welcoming Task' }, highlight: true, tone: '#5d5a4a' },
  { id: 'water', title: 'Drink 2 L water', badge: { kind: 'streak', label: '1d' }, infoDim: true, tone: '#3a3434' },
  { id: 'social', title: 'No more than 4 hours social media', badge: { kind: 'streak', label: '1d' }, tone: '#3b3330' },
]

export const momentum = {
  intro: 'You have started a Life Reset for',
  timer: [
    { value: '14', unit: 'hr' },
    { value: '53', unit: 'm' },
    { value: '03', unit: 's' },
  ],
  level: 'WEAK',
  note: { strong: '1 day active,', rest: ' 29% done. Let’s boost your momentum!' },
  cta: 'Learn how habits form',
}

export const improvementFilters = ['All', 'Physical exercise', 'Learning and reflection', 'Mindfulness']

export const improvements = [
  { id: 'wake', title: 'Wake up at 10 AM', text: 'Rise before everyone, seize the day.', tone: '#3d3a36' },
  { id: 'journal', title: 'Journaling', text: 'Record and reflect your day.', tone: '#36392f', procrastinating: true },
]

export type TaskIcon = 'meditate' | 'notebook' | 'phone' | 'glass' | 'wind' | 'book' | 'sunrise'
export interface TaskTile {
  icon: TaskIcon
  active?: boolean
}

export const journeyDays = [
  {
    id: 'd1',
    date: '5 Jun 2026',
    title: 'Day 1',
    current: true,
    mood: { title: 'Today’s MoodV5', label: 'Happy' },
    tasks: [
      { icon: 'meditate' },
      { icon: 'notebook' },
      { icon: 'phone' },
      { icon: 'glass' },
      { icon: 'wind', active: true },
      { icon: 'book', active: true },
    ] as TaskTile[],
    journal: ['Three things I’m grateful', 'for today:', '- The quality time I got to', 'spend with my friends...'],
  },
  {
    id: 'd2',
    date: '6 Jun 2026',
    title: 'Day 2',
    current: false,
    question: ['How are you', 'feeling today?'],
    tasks: [{ icon: 'glass' }, { icon: 'phone' }, { icon: 'sunrise' }] as TaskTile[],
  },
]

export const season = {
  header: 'Season',
  title: 'Season Unlimited',
  chip: 'Season 7',
  stats: [
    { label: 'Start on', value: 'May 22' },
    { label: 'Time left', value: '25d 13h' },
  ],
  text: 'Complete your daily habit tasks to gain XP and climb the ladder. Grow together and earn rewards.',
  cta: 'Join Challenge',
  joined: '932 joined',
  duo: {
    title: 'Season Duo',
    chip: 'Duo Season 0',
    banner: 'DUO PUSH-UPS',
    status: 'Duo challenge has ended',
    note: 'Stay tuned for the next duo season!',
  },
}
