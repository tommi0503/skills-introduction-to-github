import { CircleAlert, CircleGauge, CircleUserRound, Globe, LayoutGrid, LockOpen, MonitorSmartphone, Shield, type LucideIcon } from 'lucide-react'

/* ---------- onboarding ---------- */
export const intro = {
  title: 'What is a VPN?',
  body: [
    'Safer browsing with a tap! A VPN boosts your',
    'digital privacy, helps to shield your online activity',
    'from snoopers, and allows you to use public Wi-Fi',
    'more securely.',
  ],
  pages: 3,
  activePage: 0,
  primary: 'Sign Up',
  secondary: 'Log In',
  link: 'Subscription and privacy info',
}

/* ---------- paywall ---------- */
export interface Feature {
  key: string
  label: string
  icon: LucideIcon
  /** Solid (filled) glyph instead of an outline. */
  filled?: boolean
}
export const paywall = {
  title: 'First 12 months: 40% off',
  subtitle: 'Get advanced protection against online threats.',
  monthly: '$7.16/month',
  oldPrice: '$144.98',
  newPrice: '$85.98/year',
  savings: ['Savings from comparing current intro and', 'renewal prices.'],
  features: [
    { key: 'devices', label: 'Connect on 10 devices with one account.', icon: MonitorSmartphone },
    { key: 'speed', label: 'Blazing speeds, safer browsing.', icon: CircleGauge, filled: true },
    { key: 'leak', label: 'Leaked password alerts.', icon: LockOpen },
    { key: 'ads', label: 'Blocked ads and trackers.', icon: CircleAlert, filled: true },
  ] satisfies Feature[],
  cta: 'Start subscription',
  plans: 'See all plans',
  fine: ['Valid for new users only.', 'Subscription renews every year until canceled. You can', 'cancel anytime in your Apple account.'],
  link: 'Subscription and privacy info',
}

/* ---------- home ---------- */
export interface Recent {
  key: string
  lines: string[]
  sub?: string
}
export const home = {
  search: 'Search all locations',
  city: 'Seattle, United States',
  status: 'Secured',
  pause: 'Pause connection',
  promo: { title: 'Get your dedicated IP', body: 'Avoid blocklists, robot checks, and more.' },
  recentsTitle: 'Recents',
  allLocations: 'All locations',
  recents: [
    { key: 'us', lines: ['United States'], sub: 'Fastest' },
    { key: 'id', lines: ['Indonesia'], sub: 'Fastest' },
    { key: 'sf', lines: ['San Francisco', 'United States'] },
  ] satisfies Recent[],
}

/* ---------- locations ---------- */
export interface Country {
  key: string
  name: string
  sub: string
  expandable: boolean
}
export const locations = {
  search: 'Search all locations',
  tabs: [
    { key: 'country', label: 'Country' },
    { key: 'meshnet', label: 'Meshnet' },
    { key: 'double', label: 'Double VPN' },
    { key: 'onion', label: 'Onion Over VPN' },
  ],
  activeTab: 'country',
  sectionTitle: 'Select a location',
  countries: [
    { key: 'us', name: 'United States', sub: '55 cities', expandable: true },
    { key: 'uk', name: 'United Kingdom', sub: '4 cities', expandable: true },
    { key: 'ca', name: 'Canada', sub: '3 cities', expandable: true },
    { key: 'de', name: 'Germany', sub: '3 cities', expandable: true },
    { key: 'fr', name: 'France', sub: '4 cities', expandable: true },
    { key: 'jp', name: 'Japan', sub: '2 cities', expandable: true },
    { key: 'au', name: 'Australia', sub: '5 cities', expandable: true },
    { key: 'nl', name: 'Netherlands', sub: 'Amsterdam', expandable: false },
  ] satisfies Country[],
}

/* ---------- tab bar ---------- */
export interface NavTab {
  key: string
  icon: LucideIcon
  /** Small status dot colour on the icon. */
  dot?: 'green' | 'red'
  /** Draw a bolt inside the icon (the "Threat protection" shield). */
  bolt?: boolean
}
export const navTabs: NavTab[] = [
  { key: 'globe', icon: Globe },
  { key: 'protect', icon: Shield, bolt: true },
  { key: 'apps', icon: LayoutGrid },
  { key: 'profile', icon: CircleUserRound },
]
export const navDots: Record<string, NavTab['dot']> = { globe: 'green', apps: 'red', profile: 'red' }
