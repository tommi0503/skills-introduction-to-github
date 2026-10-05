import { Activity, MapPin, PawPrint } from 'lucide-react'
import type { LucideIcon } from 'lucide-react'

export interface DeviceStatus {
  battery: string
  online: string
  updated: string
}

export const pet = { name: 'Tilda', breed: 'SCOTTISH FOLD' }

export const homeStatus: DeviceStatus = { battery: '67%', online: 'Online', updated: 'Now' }
export const lostStatus: DeviceStatus = { battery: '64%', online: 'Online', updated: 'Now' }

export const home = {
  place: 'Mobbin House for 12 min',
  todayLabel: 'Today',
  todayDate: 'Tuesday, Feb 10',
  rest: { title: 'Rest', lines: ['No sleep', 'data collected'] },
  activity: { title: 'Activity', caption: 'ACTIVE TIME', value: '0 min' },
  /** bar heights (px) + fills of the activity mini chart */
  activityBars: [
    { h: 3, c: '#e6f6ec' },
    { h: 13, c: '#d2f0dd' },
    { h: 21, c: '#bfe9cf' },
    { h: 32, c: '#ade3c2' },
    { h: 40, c: '#92d7af' },
  ],
  outsideTitle: 'Last time outside',
  outsideLink: 'Timeline',
  outsideText: ['Your cat’s time outside of the', 'safe zone will show up here.'],
}

export interface FiTab {
  key: string
  label: string
  icon?: LucideIcon
  avatar?: boolean
}
export const tabs: FiTab[] = [
  { key: 'live', label: 'Live', icon: MapPin },
  { key: 'health', label: 'Health', icon: Activity },
  { key: 'community', label: 'Community', icon: PawPrint },
  { key: 'tilda', label: 'Tilda', avatar: true },
]

export interface Step {
  label: [string, string]
  done: boolean
}
export const order = {
  title: 'Your order was placed',
  number: 'Order #: 3980665',
  steps: [
    { label: ['Order', 'Placed'], done: true },
    { label: ['Order', 'Shipped'], done: false },
    { label: ['Order', 'Delivered'], done: false },
  ] as Step[],
  tracking: 'Tracking information will become available when your order ships.',
  help: 'Need help? Chat live ›',
  earnTitle: 'Earn free months',
  promo: {
    title: 'Refer a friend, get 1 month FREE',
    body: ['Share Fi and give your', 'friends 1 month free, get 1', 'month free when they join.'],
    cta: 'Share referral link',
  },
  setup: 'Start setup',
}

export const lost = {
  place: 'Mobbin House',
  duration: 'for 2d 17hr',
  city: 'Aurora, IL',
  share: 'Share',
  lostMode: 'Start Lost Mode',
}

export const rest = {
  title: 'Rest',
  periods: ['Day', 'Week', 'Month', 'Year'],
  /** spacing after each period tab (px) */
  periodGaps: [31, 33, 33, 0],
  date: 'Thu, Feb 12',
  label: 'Rest',
  total: '5hr 4m',
  split: [
    { label: 'Sleep', value: '5h', tone: 'strong' as const },
    { label: 'Naps', value: '0m', tone: 'light' as const },
  ],
  timelineTitle: 'Timeline',
  /** Segments on a 0..1 day axis */
  timeline: [
    { from: 0, to: 0.178 },
    { from: 0.75, to: 0.756 },
    { from: 0.917, to: 0.946 },
  ],
  axis: ['12AM', '6AM', '12PM', '6PM', '12AM'],
  night: {
    title: 'Night Summary',
    date: 'Feb 11',
    start: '8:00 PM',
    end: '6:01 PM',
    /** interruption marks as x offsets (px) from the bar start */
    marks: [19, 22, 50, 58],
    stats: [
      { label: 'Asleep', value: '9hr 39m', tone: 'blue' as const },
      { label: 'Interruptions', value: '5', tone: 'red' as const },
    ],
  },
  comparison: 'Comparison',
}
