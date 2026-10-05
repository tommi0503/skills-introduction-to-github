import { ChartNoAxesColumn, Circle, Hexagon, House, Square, Van, type LucideIcon } from 'lucide-react'

export interface StatCardData {
  key: string
  title: string
  value: string
  delta: string
  tone: 'green' | 'purple'
  bars: number[]
  /** Index of the highlighted bar. */
  highlight: number
}

export interface DayItem {
  key: string
  weekday: string
  day: string
}

export interface ScheduleEvent {
  key: string
  time: string
  title: string
  window: string
  place: string
}

export interface NavEntry {
  key: string
  icon: LucideIcon
  /** Smaller glyph centred inside the main icon (e.g. the bars inside a square). */
  detail?: LucideIcon
  detailSize?: number
}

export interface Metric {
  key: string
  label: string
  value: string
  color: string
}

export const planner = {
  title: 'Maintenance Planner',
  subtitle: 'Maintain regularly to prevent downtime.',
  date: 'Wed, 16 June 2026',
  count: '4 Schedule',
  activeDay: '08',
}

export const statCards: StatCardData[] = [
  { key: 'today', title: 'Scheduled Today', value: '24', delta: '+6 added', tone: 'green', bars: [17, 46, 27, 53, 27, 39], highlight: 3 },
  { key: 'service', title: 'Under Service', value: '12', delta: '-5%', tone: 'purple', bars: [15, 46, 27, 53, 27, 39], highlight: 3 },
]

export const days: DayItem[] = [
  { key: 'mon', weekday: 'Mon', day: '06' },
  { key: 'tue', weekday: 'Tue', day: '07' },
  { key: 'wed', weekday: 'Wed', day: '08' },
  { key: 'thu', weekday: 'Thu', day: '09' },
  { key: 'fri', weekday: 'Fri', day: '10' },
]

export const events: ScheduleEvent[] = [
  { key: 'oil', time: '08:00', title: 'Oil Change', window: '8 AM - 9 AM', place: 'Newcastle upon Tyne' },
  { key: 'brake', time: '11:30', title: 'Break Inspection', window: '11:30 AM - 12 PM', place: 'FleetCare Workshop' },
  { key: 'tire', time: '02:00', title: 'Tire Rotation', window: '2:00 PM - 3:00 PM', place: 'Main Workshop' },
  { key: 'wash', time: '05:00', title: 'Wash & Detail', window: '5:00 PM - 6:00 PM', place: 'Main Workshop' },
]

export const navEntries: NavEntry[] = [
  { key: 'home', icon: House },
  { key: 'fleet', icon: Van },
  { key: 'service', icon: Hexagon, detail: Circle, detailSize: 8 },
  { key: 'analytics', icon: Square, detail: ChartNoAxesColumn, detailSize: 12 },
]

export const analytics = {
  title: 'Fleet Analytics',
  subtitle: 'Monitor analyze improve performance.',
  vehicle: 'PRADO - TRK-104',
  status: 'Active',
  nextService: 'Next Service  in 12 days',
  breakdown: 'Maintenance Cost Breakdown',
}

export const metrics: Metric[] = [
  { key: 'health', label: 'Health Score', value: '92%', color: '#2f8a4e' },
  { key: 'compliance', label: 'Compliance', value: '48,720', color: '#111' },
  { key: 'fuel', label: 'Fuel Level', value: '58%', color: '#f2a443' },
]
