import type { LucideIcon } from 'lucide-react'
import { Home, Library, Plus, Search } from 'lucide-react'

export interface NavItem {
  key: string
  label: string
  icon?: LucideIcon
  /** brand mark (Spotify logo) → placeholder */
  brand?: boolean
}

export const nav: Record<string, NavItem> = {
  home: { key: 'home', label: 'Home', icon: Home },
  search: { key: 'search', label: 'Search', icon: Search },
  library: { key: 'library', label: 'Your Library', icon: Library },
  premium: { key: 'premium', label: 'Premium', brand: true },
  create: { key: 'create', label: 'Create', icon: Plus },
}

/* ---------- Premium plans ---------- */
export interface Plan {
  key: string
  tag: string
  tagColor: string
  name: string
  price: string
  after: string
  features: string[]
  cta: string
  legal: string
  legalLink: string
  legalTail: string
}

export const premium = {
  header: '$0 for 4 months of Premium I...',
  title: 'Available plans',
  brand: 'Premium',
  plans: [
    {
      key: 'individual',
      tag: 'US$0 for 4 months',
      tagColor: '#ffd2d7',
      name: 'Individual',
      price: 'US$0 for 4 months',
      after: 'US$11.99/month after',
      features: ['1 Premium account', '15 hours/month of listening time from our audiobooks subscriber catalogue', 'Cancel anytime'],
      cta: 'Try 4 months for US$0',
      legal:
        "By clicking this button, you'll be taken to our website. Premium Individual only. Free for 4 months, then $11.99 per month after. Offer only available if you haven't tried Premium before.",
      legalLink: 'Terms apply',
      legalTail: '. Offer ends December 31, 2025.',
    },
  ] satisfies Plan[],
  nextTag: { label: 'US$0 for 1 month', color: '#d7c5f5' },
  nowPlaying: { title: 'WILDFLOWER', artist: 'Billie Eilish', progress: 0.05 },
  tabs: ['home', 'search', 'library', 'premium', 'create'],
  activeTab: 'premium',
}

/* ---------- Home (offline) ---------- */
export interface Shortcut {
  key: string
  title: string
  /** artist without artwork → icon tile */
  iconOnly?: boolean
  playing?: boolean
  unread?: boolean
}

export interface MediaCardData {
  key: string
  overline: string
  title: string
  subtitle: string
}

export const home = {
  filters: ['All', 'Music', 'Podcasts', 'Audiobooks'],
  activeFilter: 'All',
  shortcuts: [
    { key: 'ophelia', title: 'The Fate of Ophelia Radio' },
    { key: 'gracie', title: 'Gracie Abrams', iconOnly: true },
    { key: 'dj', title: 'DJ', playing: true },
    { key: 'hang', title: 'Good Hang with Amy Poehler', unread: true },
    { key: 'true', title: 'That’s So True Radio' },
  ] satisfies Shortcut[],
  offlineTitle: 'While you’re offline',
  offlineBody: 'Your downloads, including songs and episodes, will appear here.',
  showsTitle: 'Your shows',
  shows: [
    { key: 'hang', overline: 'Comedy', title: 'Good Hang with Amy Poehler', subtitle: 'The Ringer' },
    { key: 'tpw', overline: 'Comedy', title: 'This Past Weekend w/ Theo Von', subtitle: 'Theo Von' },
    { key: 'shawn', overline: 'Society & Culture', title: 'The Shawn Ryan Show', subtitle: 'Shawn Ryan' },
  ] satisfies MediaCardData[],
  stationsTitle: 'Recommended Stations',
  stations: ['#e0705f', '#8fd4a6', '#9ed8cf'],
  stationLabel: 'RADIO',
  tabs: ['home', 'search', 'library', 'create'],
  activeTab: 'home',
  offline: 'Offline mode',
}

/* ---------- Now playing ---------- */
export const player = {
  context: 'That’s So True Radio',
  title: 'That’s So True',
  artist: 'Gracie Abrams',
  elapsed: '0:04',
  remaining: '-2:42',
  progress: 0.03,
  lyrics: 'Lyrics',
}

/* ---------- Artist ---------- */
export interface Track {
  key: string
  title: string
  plays: string
  video?: boolean
}

export const artist = {
  name: 'Laufey',
  listeners: '36.2M monthly listeners',
  follow: 'Follow',
  tabs: ['Music', 'Clips', 'Events', 'Merch'],
  activeTab: 'Music',
  popular: 'Popular',
  tracks: [
    { key: 'start', title: 'From The Start', plays: '937,554,546' },
    { key: 'winter', title: 'Winter Wonderland', plays: '172,661,391' },
    { key: 'lover', title: 'Lover Girl', plays: '126,318,780', video: true },
    { key: 'falling', title: 'Falling Behind', plays: '454,892,464' },
    { key: 'santa', title: 'Santa Baby', plays: '98,112,402' },
  ] satisfies Track[],
  navTabs: ['home', 'search', 'library', 'create'],
  activeNav: 'search',
}
