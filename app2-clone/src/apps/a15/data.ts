import { BriefcaseBusiness, House, Plus, type LucideIcon } from 'lucide-react'

export interface Chip {
  key: string
  label: string
  icon: 'calendar' | 'rider'
}
export const chips: Chip[] = [
  { key: 'schedule', label: 'Schedule ahead', icon: 'calendar' },
  { key: 'rider', label: 'Change rider', icon: 'rider' },
]

/* ---------- home ---------- */
export interface Shortcut {
  key: string
  title: string
  sub?: string
  icon: LucideIcon
  /** Filled glyph (home / work) vs outline (+). */
  filled?: boolean
}
export interface Reward {
  key: string
  title: string[]
  sub: string[]
}
export const home = {
  greeting: 'Rise and shine, Alex',
  promo: ['50% off your next 2 rides. Restrictions', 'apply. through 05/14/2026'],
  search: 'Where are you going?',
  shortcuts: [
    { key: 'home', title: 'Home', sub: 'Add shortcut', icon: House, filled: true },
    { key: 'work', title: 'Work', sub: 'Add shortcut', icon: BriefcaseBusiness, filled: true },
  ] satisfies Shortcut[],
  earnTitle: 'Earn as you ride',
  rewards: [
    { key: 'united', title: ['United MileagePlus'], sub: ['Earn 1–4 miles per $1 on qualifying rides'] },
    { key: 'hilton', title: ['Hilton Honors'], sub: ['Earn 3 points for every $1 spent on rides'] },
    { key: 'atmos', title: ['Atmos Rewards by Alaska and', 'Hawaiian Airlines'], sub: ['Earn 2–3 points per $1 on', 'qualifying rides'] },
  ] satisfies Reward[],
  peek: 'You and Lyft',
}

/* ---------- destination ---------- */
export interface Place {
  key: string
  title: string
  address: string
}
export const destination = {
  title: 'Destination',
  startLabel: 'Start',
  start: 'Current location',
  destPlaceholder: 'Destination',
  shortcuts: [
    { key: 'home', title: 'Add home', icon: House, filled: true },
    { key: 'work', title: 'Add work', icon: BriefcaseBusiness, filled: true },
    { key: 'custom', title: 'Add custom shortcut', icon: Plus },
  ] satisfies Shortcut[],
  places: [
    { key: 'ohare', title: "O'Hare Int'l Airport", address: 'Chicago, IL' },
    { key: 'midway', title: 'Chicago Midway Airport', address: '5700 S Cicero Ave, Chicago' },
    { key: 'mccormick', title: 'McCormick Place', address: '252 E 23rd St, Chicago' },
    { key: 'navy', title: 'Navy Pier', address: '776 E Grand Ave, Chicago' },
    { key: 'union', title: 'Union Station', address: '225 S Canal St, Chicago' },
    { key: 'wrigley', title: 'Wrigley Field', address: '1060 W Addison St Chicago' },
  ] satisfies Place[],
}

/* ---------- ride options ---------- */
export const rides = {
  tapToEdit: 'Tap to edit locations',
  arrive: 'Arrive 4:56 PM',
  saving: "You're saving 50%, up to $10. + 1 more",
  option: { name: 'Standard', seats: '4', price: '$9.94', discount: '52% off', was: '$20.92', eta: 'in 4 min · 4:56 PM' },
  cash: 'Lyft Cash: $13.22 + Promo',
  schedule: 'Schedule',
  cta: 'Select Standard',
  /** Route polyline in screen coordinates. */
  route: [
    [171, 151], [171, 172], [164, 175], [164, 229], [107, 233], [126, 281], [131, 296], [150, 326],
    [190, 371], [196, 396], [196, 451], [281, 453],
  ] as Array<[number, number]>,
}

/* ---------- upsell ---------- */
export const upsell = {
  title: 'Get going faster?',
  body: ['A Black ride is available to pick you up', 'sooner. Go ahead and get the VIP treatment', '($28.92 total).'],
  primary: 'Upgrade for $18.05 more',
  secondary: 'Keep waiting',
  /** 0..1 progress of the auto-dismiss timer on "Keep waiting". */
  progress: 0.06,
}
