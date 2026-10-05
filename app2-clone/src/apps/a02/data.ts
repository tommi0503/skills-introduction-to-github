export type NavKey = 'home' | 'chats' | 'trips' | 'explore' | 'profile'
export interface NavItem {
  key: NavKey
  label: string
}
export const navItems: NavItem[] = [
  { key: 'home', label: 'Home' },
  { key: 'chats', label: 'Chats' },
  { key: 'trips', label: 'Trips' },
  { key: 'explore', label: 'Explore' },
  { key: 'profile', label: 'Profile' },
]
export const profileInitials = 'AS'
export const composerPlaceholder = 'Ask anything...'

/* Welcome */
export interface FloatingCard {
  key: string
  x: number
  y: number
  width: number
}
export const welcome = {
  title: ['Welcome to', 'Mindtrip!'],
  subtitle: 'Your Ultimate Travel Companion',
  next: 'Next',
  skip: 'Skip',
  pages: 5,
  activePage: 0,
  cards: [
    { key: 'a', x: 276, y: 161, width: 130 },
    { key: 'b', x: 78, y: 258, width: 131 },
    { key: 'c', x: 214, y: 350, width: 147 },
  ] as FloatingCard[],
}

/* Home */
export interface Tile {
  key: string
  title: string
  lines?: string[]
  meta?: string
  actions?: boolean
}
export const home = {
  getStarted: 'Get started',
  starters: [
    { key: 'chat', title: 'Start a chat' },
    { key: 'trip', title: 'Create a trip' },
  ] as Tile[],
  forYouPrefix: 'For you in',
  forYouPlace: 'Civic Center',
  explore: 'Explore',
  forYou: [
    { key: 'chambers', title: 'Chambers', meta: 'Contemporary · $$', actions: true },
    { key: 'tour', title: '', lines: ['NYC: Chinatown & Little', 'Italy Food Tour with 7'], meta: 'Activity' },
  ] as Tile[],
  getInspired: 'Get inspired',
}

/* Chat */
export const chat = {
  title: 'NYC Cupcake Recommendations',
  userInitial: 'A',
  question: 'Best cupcakes in NYC?',
  answerLead: 'Cupcake mission in',
  answerPlace: 'NYC',
  answerRest: '? Say less. Here are some top spots to hit (from iconic classics to “wait why is this so good” flavors):',
  place: {
    name: 'Magnolia Bakery',
    rating: '4.2',
    meta: 'American · $',
    body: 'The classic NYC cupcake stop (plus their famous banana pudding if you “accidentally” want more than cupcakes). Great for that nostalgic, fluffy-frosting moment.',
  },
  mapLabel: 'Map',
}

/* Trip planning sheet */
export const planner = {
  behindTitle: 'Los Angeles',
  title: 'Hey Alex, let’s get started on your trip!',
  intro: 'I see that you have shared some details about your trip already, is there anything else you want me to know?',
  photos: ['la', 'sf'],
  chipRows: [
    [{ key: 'la', label: 'Los Angeles', pin: true }],
    [
      { key: 'sf', label: 'San Francisco Bay Area', pin: true },
      { key: 'aug', label: 'August', pin: false },
    ],
  ],
  transcript: ['No. No.', 'Okay, great. So, we’re all set — just tap the Create Trip button below!'],
  speaking: 'Speaking...',
  cta: 'Create trip',
}

/* Trips */
export interface TripCard {
  key: string
  title: string
  subtitle?: string
}
export const trips = {
  title: 'Trips',
  newTrip: 'New Trip',
  bookedOnly: 'Booked only',
  filter: 'All',
  sections: [
    { key: 'up', title: 'Upcoming', card: { key: 'bkk', title: 'Trip to Bangkok, October 2026', subtitle: 'Bangkok · Oct 19–23' } },
    { key: 'un', title: 'Unscheduled', card: { key: 'la', title: 'Trip to Los Angeles and San Francisco', subtitle: 'Los Angeles \u00b7 San Francisco' } },
  ] as { key: string; title: string; card: TripCard }[],
}
