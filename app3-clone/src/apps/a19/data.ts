export interface TeamLine {
  name: string
  score?: number
  winner?: boolean
}
export interface Fixture {
  key: string
  time?: string
  status?: string
  league: string
  teams: TeamLine[]
  tone: 'light' | 'mlb' | 'nba'
  /** Position inside the day row (half-width cards sit side by side). */
  x: number
  y: number
  w: number
  h: number
}
export interface DayGroup {
  key: string
  dow: string
  date: number
  today?: boolean
  y: number
}
export const favourites = ['barca', 'ao', 'warriors', 'knicks', 'yankees', 'celtics', 'duke']
export const days: DayGroup[] = [
  { key: 'mon', dow: 'MON', date: 16, today: true, y: 128 },
  { key: 'tue', dow: 'TUE', date: 17, y: 367 },
  { key: 'wed', dow: 'WED', date: 18, y: 769 },
]
export const fixtures: Fixture[] = [
  {
    key: 'gsw', status: 'Final', league: 'NBA', tone: 'light', x: 66, y: 131, w: 151, h: 178,
    teams: [{ name: 'Warriors', score: 125, winner: true }, { name: 'Wizards', score: 117 }],
  },
  {
    key: 'bos', status: 'Final', league: 'NBA', tone: 'light', x: 223, y: 161, w: 152, h: 177,
    teams: [{ name: 'Suns', score: 112 }, { name: 'Celtics', score: 120, winner: true }],
  },
  {
    key: 'tb', time: '3:05 AM', league: 'MLB Spring Training', tone: 'mlb', x: 65, y: 370, w: 310, h: 178,
    teams: [{ name: 'Rays', winner: true }, { name: 'Yankees', winner: true }],
  },
  {
    key: 'ind', time: '6:30 AM', league: 'NBA', tone: 'nba', x: 65, y: 563, w: 310, h: 178,
    teams: [{ name: 'Pacers', winner: true }, { name: 'Knicks', winner: true }],
  },
  {
    key: 'bos2', status: 'Final', league: 'MLB Spring Training', tone: 'light', x: 65, y: 790, w: 152, h: 178,
    teams: [{ name: 'Red Sox', score: 4, winner: true }, { name: 'Twins', score: 2 }],
  },
  {
    key: 'nyy', time: '12:45 AM', league: 'MLB Spring Training', tone: 'mlb', x: 223, y: 811, w: 152, h: 178,
    teams: [{ name: 'Mets', winner: true }, { name: 'Astros', winner: true }],
  },
]

export const paywall = {
  title: 'TRY FIXTURED+',
  subtitle: 'Upgrade to Fixtured+ for smarter schedules and zero limits',
  features: ['Unlimited teams', 'Unlimited competitions', 'Calendar sync', 'Competition granularity', 'Customize notifications', 'Custom app icons'],
  review: 'Dream sports app',
  plans: [
    { key: 'annual', name: 'Annual', price: '$29.99/year', trial: 'Free for 7 days', badge: '38% OFF', selected: true },
    { key: 'monthly', name: 'Monthly', price: '$3.99/month', trial: 'Free for 7 days' },
  ],
  cta: 'Try free for 7 days',
}
export type PaywallPlan = (typeof paywall.plans)[number]

export const match = {
  competition: 'MLB Spring Training',
  stage: 'Regular Season',
  home: 'Rays',
  away: 'Yankees',
  innings: ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'T'],
  lines: [
    { team: 'Yankees', runs: [0, 1, 0, 0, 0, 0, 0, 0, 2, 3] },
    { team: 'Rays', runs: [0, 0, 0, 0, 1, 0, 0, 0, 1, 2] },
  ],
  info: [
    { label: 'Venue', value: 'Charlotte Sports Park' },
    { label: 'Location', value: 'Port Charlotte' },
  ],
}

export const share = {
  title: 'SPORT IS BETTER\nWITH FRIENDS',
  body: 'Share an event with friends to let them know what you’re watching.',
  primary: 'Share Event',
  secondary: 'Copy Link',
}
