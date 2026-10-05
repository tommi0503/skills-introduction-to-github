import { CalendarDays, House, ShoppingBag, UsersRound, type LucideIcon } from 'lucide-react'

export type DayState = 'open' | 'blocked' | 'hatched' | 'selected'

export interface CalendarDay {
  day: number
  state: DayState
}

export const weekdays = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
export const highlightedWeekday = 'Tue'

const blocked = [1, 3, 21, 22, 29, 30]
const hatched = [8, 13, 14, 17]
const selected = 11

export const septemberDays: CalendarDay[] = Array.from({ length: 30 }, (_, i) => {
  const day = i + 1
  const state: DayState =
    day === selected ? 'selected' : blocked.includes(day) ? 'blocked' : hatched.includes(day) ? 'hatched' : 'open'
  return { day, state }
})

export const rangeTabs = ['Day', 'Week', 'Month', 'Years']
export const activeRange = 'Month'

export interface NavItem {
  key: string
  icon: LucideIcon
}

export const navItems: NavItem[] = [
  { key: 'home', icon: House },
  { key: 'calendar', icon: CalendarDays },
  { key: 'people', icon: UsersRound },
  { key: 'shop', icon: ShoppingBag },
]

export const nextAppointment = {
  title: 'Your Next Appointment',
  barber: 'Liron Israelov’s',
  address: 'f20 se’ - 100BI',
  service: 'Haircut + Beard Styling',
  time: '09:00 - 09:30 AM',
  date: '18 Sep 2026',
}

export const timeSlot = {
  label: 'Select a time slot',
  start: { caption: 'Start', value: '09 : 00 AM' },
  end: { caption: 'End', value: '09 : 30 AM' },
}

export interface ScheduleEntry {
  name: string
  time: string
  status: 'Done' | 'Active'
}

export const scheduleTimes = [
  { time: '9:00', meridiem: 'AM' },
  { time: '9:30', meridiem: 'AM' },
]

export const schedule: ScheduleEntry[] = [
  { name: 'David Madar', time: '09:00 - 09:30 AM', status: 'Done' },
  { name: 'Alex Smith', time: '09:15 - 09:44 AM', status: 'Active' },
]

export const copy = {
  splashTitle: ['Your Next Beauty', 'Appointment Is Just', 'A Tap Away.'],
  splashCta: 'Book an Appointment',
  poweredBy: 'Powered by',
  greeting: 'Hello! David',
  homeTitle: ['Give Your Look the', 'Upgrade It Deserves.'],
  bookCta: 'Book A New Appointment',
  sectionPeek: 'Some',
  bookingTitle: ['Book Your', 'Preferred Time'],
  month: 'September',
  save: 'Save',
  scheduleTitle: 'Today Schedule',
}
