/** A tide high/low. `hour` may lie outside 0..24 (previous / next day) to extend the curve. */
export interface Extreme {
  hour: number
  height: number
  /** Time label; omitted for unlabeled off-screen extremes. */
  time?: string
}

export interface StationCard {
  id: string
  name: string
  level: string
  rising: boolean
  nowHour: number
  /** card background (sky) gradient stops, top → bottom */
  sky: [string, string]
  extremes: Extreme[]
}

const hm = (t: string) => {
  const [h, m] = t.split(':').map(Number)
  return h + m / 60
}
const ex = (t: string, height: number, dayOffset = 0): Extreme => ({ hour: hm(t) + dayOffset * 24, height, time: t })

export const stations: StationCard[] = [
  {
    id: 'bahia',
    name: 'Bahia Los Angeles',
    level: '0.7m',
    rising: false,
    nowHour: 6.5,
    sky: ['#4a5a80', '#2c3a5c'],
    extremes: [{ hour: -4.4, height: 1.2 }, ex('01:59', 2.5), ex('08:28', 0.3), ex('15:32', 3.5), ex('21:54', 1.4), { hour: 28.3, height: 3.3 }],
  },
  {
    id: 'moku',
    name: 'Moku o Loe, Kaneohe Bay, Oahu Island, Hawaii',
    level: '0.2m',
    rising: false,
    nowHour: 3.5,
    sky: ['#1b2238', '#0f1424'],
    extremes: [{ hour: -0.9, height: 0.3 }, ex('01:44', 0.3), ex('08:50', -0.2), ex('16:46', 0.8), { hour: 23.5, height: 0.2 }],
  },
  {
    id: 'laie',
    name: 'Laie Bay, Oahu Island',
    level: '0.2m',
    rising: false,
    nowHour: 3.5,
    sky: ['#161a2c', '#0e1220'],
    extremes: [{ hour: -1.3, height: 0.25 }, ex('01:22', 0.3), ex('08:18', -0.2), ex('16:25', 0.8), ex('23:24', 0.2), { hour: 30, height: 0.7 }],
  },
  {
    id: 'peniche',
    name: 'Peniche',
    level: '2.7m',
    rising: true,
    nowHour: 14.5,
    sky: ['#3d424e', '#2c313b'],
    extremes: [{ hour: -2, height: 0.4 }, ex('04:12', 3.1), ex('10:14', 0.4), ex('16:32', 3.4), ex('22:54', 0.3), { hour: 29, height: 3.2 }],
  },
]

export interface Pin {
  id: string
  x: number
  y: number
  label?: string[]
  /** label centre x when it is not under the pin */
  labelX?: number
  labelY?: number
  size?: 'sm' | 'lg'
}

/** Station Map (overview) annotations — screen coordinates. */
export const overviewPins: Pin[] = [
  { id: 'laie', x: 205, y: 356.5, label: ['Laie Bay, Oahu', 'Island, Hawaii'] },
  { id: 'haleiwa', x: 105, y: 388.5, label: ['Haleiwa, Waialua Bay,', 'Oahu Island, Hawaii'] },
  { id: 'kahana', x: 251.5, y: 448.5 },
  { id: 'waianae', x: 57.5, y: 482, label: ['Waianae, Oahu', 'Island, Hawaii'] },
  { id: 'moku', x: 285.5, y: 490, label: ['Moku o Loe, Kaneohe Bay,', 'Oahu Island, Hawaii'] },
  { id: 'pearl', x: 185, y: 552.5 },
  { id: 'honolulu', x: 242, y: 567, label: ['Honolulu, Honolulu', 'Harbor, Oahu', 'Island, Hawaii'] },
  { id: 'hanauma', x: 338.5, y: 586, label: ['Hanauma Bay, Oahu', 'Island, Hawaii'] },
]

/** Station Map (zoomed, Moku selected). */
export const zoomedPins: Pin[] = [
  { id: 'laie', x: 206, y: 251.5, label: ['Laie Bay, Oahu', 'Island, Hawaii'] },
  { id: 'haleiwa', x: 116.5, y: 281, label: ['Haleiwa, Waialua Bay,', 'Oahu Island, Hawaii'] },
  { id: 'kahana', x: 245, y: 334 },
  { id: 'waianae', x: 74, y: 365, label: ['Waianae, Oahu', 'Island, Hawaii'] },
  { id: 'pearl', x: 189, y: 429.5 },
  { id: 'honolulu', x: 240.5, y: 441, label: ['Honolulu, Honolulu', 'Harbor, Oahu', 'Island, Hawaii'] },
  { id: 'hanauma', x: 326, y: 457, label: ['Hanauma Bay, Oahu', 'Island, Hawaii'] },
  { id: 'moku', x: 278.5, y: 341.5, size: 'lg', label: ['Moku o Loe, Kaneohe Bay,', 'Oahu Island, Hawaii'], labelX: 279, labelY: 396 },
]

export const selectedStation = {
  name: 'Moku o Loe, Kaneohe Bay, Oahu Island, Hawaii',
  place: 'Kaneohe, Hawaii',
  nowHour: 3.5,
  extremes: [{ hour: -4, height: 0.7 }, ex('23:06', 0.3, -1), ex('01:44', 0.3), ex('08:50', -0.2), ex('16:46', 0.8)],
}

export type ConditionIcon = 'sun' | 'water' | 'wind' | 'swell' | 'wave'
export interface Condition {
  icon: ConditionIcon
  value: string
  unit?: string
}

export const summaryConditions: Condition[] = [
  { icon: 'sun', value: '20°' },
  { icon: 'water', value: '30°' },
  { icon: 'wave', value: '0.9m' },
  { icon: 'sun', value: '4' },
]

export const windConditions: Condition[] = [
  { icon: 'sun', value: '32°' },
  { icon: 'water', value: '25°' },
  { icon: 'wind', value: '4', unit: 'WNW' },
  { icon: 'swell', value: '3', unit: 's' },
]

export const tideConditions: Condition[] = [
  { icon: 'sun', value: '23°' },
  { icon: 'water', value: '26°' },
  { icon: 'wind', value: '5', unit: 'W' },
  { icon: 'swell', value: '3', unit: 's' },
]

export const currentStation = 'Bahia Los Angeles'

export const wind = { speed: '7', direction: 'W', gusts: 'Gusts: 15 km/h', badge: '7', swell: '0.2m' }

export const windDayCurve: Extreme[] = [ex('08:28', 0.3), ex('15:32', 2.7), ex('21:54', 0.6), { hour: 28.3, height: 3.3 }]

export const fallingTide = {
  level: '0.7m',
  title: 'Falling Tide',
  subtitle: 'Low in 2 hr, 1 min',
  sun: [
    { kind: 'sunrise' as const, time: '05:35' },
    { kind: 'sunset' as const, time: '19:34' },
    { kind: 'moonrise' as const, time: '07:05' },
    { kind: 'moonset' as const, time: '21:40' },
  ],
  tides: [
    { rising: true, time: '01:59', height: '2.5m', past: true },
    { rising: false, time: '08:28', height: '0.3m' },
    { rising: true, time: '15:32', height: '3.5m' },
    { rising: false, time: '21:54', height: '1.4m' },
  ],
  curve: [{ hour: -4.4, height: 1.2 }, ex('01:59', 2.5), ex('08:28', 0.3), ex('15:32', 3.5), ex('21:54', 1.4)] as Extreme[],
  scrub: { hour: 14.9, value: '3.4m', time: '14:55', day: 'Today' },
}

export type TabKey = 'today' | 'charts' | 'tables' | 'solunar'
export const tabs: { key: TabKey; label: string }[] = [
  { key: 'today', label: 'Today' },
  { key: 'charts', label: 'Charts' },
  { key: 'tables', label: 'Tables' },
  { key: 'solunar', label: 'Solunar' },
]
