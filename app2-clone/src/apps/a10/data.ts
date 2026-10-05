export interface Leg {
  code: string
  time: string
}

export interface Flight {
  id: string
  /** Big number on the left ("8", "1", "2"). */
  lead: string
  leadUnit: string
  /** Show the leading column (hidden for a continuation leg). */
  airlineMark: 'logo' | 'none'
  number: string
  /** Right side of the meta row: either a status ("Departs" + "On Time") or a date. */
  metaLabel: string
  metaValue?: string
  from: string
  to: string
  dep: Leg
  arr: Leg
}

export const addFlightTabs = ['SFO', 'LAX'] as const
export const addFlightDate = 'Fri, 26 Jun'

const sfoLax = (id: string, number: string, arr: string, mark: Flight['airlineMark'] = 'logo'): Flight => ({
  id,
  lead: '8',
  leadUnit: 'HOURS',
  airlineMark: mark,
  number,
  metaLabel: 'Departs',
  metaValue: 'On Time',
  from: 'San Francisco',
  to: 'Los Angeles',
  dep: { code: 'SFO', time: '6:00 AM' },
  arr: { code: 'LAX', time: arr },
})

export const searchResults: Flight[] = [
  sfoLax('as', 'AS 1620', '7:07 AM'),
  sfoLax('ua', 'UA 2127', '7:37 AM'),
  sfoLax('aa', 'AA 6294', '7:42 AM'),
  sfoLax('at', 'AT 5167', '7:42 AM', 'none'),
  sfoLax('qf', 'QF 4730', '7:42 AM'),
]

export const myFlights: Flight[] = [
  {
    id: 'dl',
    lead: '1',
    leadUnit: 'DAY',
    airlineMark: 'logo',
    number: 'DL 1421',
    metaLabel: 'Mon, Jun 29',
    from: 'San Francisco',
    to: 'Los Angeles',
    dep: { code: 'SFO', time: '10:15 AM' },
    arr: { code: 'LAX', time: '11:40 AM' },
  },
  {
    id: 'cx',
    lead: '2',
    leadUnit: 'DAYS',
    airlineMark: 'logo',
    number: 'CX 7786',
    metaLabel: 'Tue, Jun 30',
    from: 'Los Angeles',
    to: 'Mexico City',
    dep: { code: 'LAX', time: '9:14 AM' },
    arr: { code: 'MEX', time: '2:00 PM' },
  },
  {
    id: 'am',
    lead: '3',
    leadUnit: 'DAYS',
    airlineMark: 'logo',
    number: 'AM 646',
    metaLabel: 'Tue, Jun 2',
    from: 'Mexico City',
    to: 'New York',
    dep: { code: 'MEX', time: '8:40 AM' },
    arr: { code: 'JFK', time: '4:02 PM' },
  },
]

export const layover = { duration: '21h 34m', where: 'at LAX', label: 'Long Layover' }

export const airportFilters = ['All', 'North America', 'Europe'] as const

export const airport = {
  tags: ['CAN', 'ZGGG', '8:21 PM GMT+8'],
  name: 'Guangzhou Baiyun Intl.',
  city: 'GUANGZHOU, CHINA',
}

export type IssueIcon = 'takeoff' | 'landing' | 'weather'
export interface Issue {
  icon: IssueIcon
  title: string
  text: string
}
export const issues: Issue[] = [
  { icon: 'takeoff', title: 'Departures', text: 'Flights are taking off 1h 37m late\non average.' },
  { icon: 'landing', title: 'Arrivals', text: 'Flights are landing 1h 4m late on average.' },
  { icon: 'weather', title: 'Weather', text: 'Light rain and recent storms.' },
]

export interface Stat {
  label: string
  value: string
  count: string
  color: string
  /** share of the segmented bar, 0..1 */
  share: number
}
export const departureStats: Stat[] = [
  { label: 'On Time', value: '38%', count: '12', color: '#4f9a5a', share: 0.355 },
  { label: 'Delayed 15m+', value: '59%', count: '19', color: '#c0432f', share: 0.585 },
  { label: 'Canceled', value: '3%', count: '1', color: '#9e2f22', share: 0.03 },
]

/** Takeoff delay per slot, minutes. `now` marks the highlighted slot. */
export const delayTrend = {
  bars: [52, 69, 62, 72, 81, 88, 90, 85, 88, 99, 100, 99, 97, 97, 92, 88, 88, 89, 82, 80, 87, 82, 79, 77],
  pastFrom: 4,
  now: 12,
  peakLabel: '1h 37m',
  gridlines: [
    { minutes: 120, label: '2h' },
    { minutes: 100, label: '1h 40m' },
    { minutes: 80, label: '1h 20m' },
  ],
}
