import {
  Bookmark, Compass, Link, Map, Search, Share, Star, ThumbsDown, ThumbsUp, Smile, UsersRound, type LucideIcon,
} from 'lucide-react'

/* ---------- map (screen 1) ---------- */
export interface MapPinData {
  key: string
  /** centre of the round marker */
  x: number
  y: number
  /** small status dot on the marker */
  dot: string
  /** optional line above the name (e.g. "Beliza liked") */
  kicker?: string
  name: string
  sub: string[]
  /** photo avatar rather than an emoji-style badge */
  avatar?: boolean
}

export const mapPins: MapPinData[] = [
  { key: 'cote550', x: 268, y: 246, dot: '#5fd16f', name: 'COTE 550', sub: ['new eat'] },
  { key: 'culture', x: 195, y: 320, dot: '#f2a12c', name: 'Culture Espresso', sub: ['trending cookie cafe'] },
  { key: 'cotefl', x: 163, y: 402, dot: '#f2a12c', name: 'COTE Flatiron', sub: ['trending korean', 'steakhouse'] },
  { key: 'lily', x: 96, y: 455, dot: '#c9a7f0', kicker: 'Beliza liked', name: 'Lily Pond', sub: ['healthy cafe'], avatar: true },
  { key: 'rhythm', x: 344, y: 486, dot: '#f2a12c', name: 'RHYTHM', sub: ['| GREEN', 'trending'] },
  { key: 'cabra', x: 189, y: 492, dot: '#f3a6d0', name: 'La Cabra Bakery', sub: ['popular scandi pastries'] },
  { key: 'pecora', x: 134, y: 538, dot: '#f2a12c', name: 'La Pecora Bianca SoHo', sub: ['trending italian', 'cafe & wine'] },
  { key: 'deluxe', x: 123, y: 598, dot: '#f2a12c', name: 'Deluxe Green Bo', sub: ['trending shanghai', 'dumplings'] },
  { key: 'antidote', x: 313, y: 608, dot: '#f2a12c', name: 'Antidote', sub: ['trending szechuan', 'cocktails'] },
]

/** small "something here" dots */
export const mapDots: [number, number][] = [
  [248, 237], [245, 258], [92, 353], [200, 363], [240, 364], [206, 308],
  [66, 435], [82, 443], [64, 466], [90, 471], [106, 484], [93, 506], [112, 505], [86, 522],
  [108, 568], [56, 565], [139, 554], [146, 551], [179, 546], [206, 554], [120, 463], [152, 576],
]

export interface Category {
  key: string
  label: string
}
export const categories: Category[] = [
  { key: 'top', label: 'top picks' },
  { key: 'eat', label: 'eat' },
  { key: 'cafes', label: 'cafes' },
  { key: 'bars', label: 'bars' },
  { key: 'events', label: 'events' },
  { key: 'goout', label: 'go out' },
  { key: 'shops', label: 'shops' },
]

export interface NavItem {
  key: string
  icon?: LucideIcon
  /** profile photo slot */
  avatar?: boolean
}
export const navItems: NavItem[] = [
  { key: 'friends', icon: UsersRound },
  { key: 'map', icon: Map },
  { key: 'search', icon: Search },
  { key: 'me', avatar: true },
]

export const mapFilters = [
  { key: 'everyone', label: 'everyone', trailing: 'chevron' as const },
  { key: 'open', label: 'open now', leading: 'dot' as const },
]

/* ---------- place (screens 2-4) ---------- */
export const place = {
  query: 'La Cabra Bakery',
  name: 'La Cabra Bakery',
  saves: '946 SAVES',
  tags: ['scandi pastries', '$'],
  rank: { label: 'POPULAR', detail: '#4 bakery' },
  hours: { state: 'open', range: '7am–6pm' },
  photos: 3,
  sticker: ['POPULAR', '#4', 'bakery'],
  about: {
    meta: ['East Village', '152 2nd Ave'],
    text: 'Scandinavian coffee shop serving the city’s most talked-about cardamom buns...',
  },
}

export interface SaveStat {
  key: string
  icon: LucideIcon
  color: string
  value: string
}
export const saveStats: SaveStat[] = [
  { key: 'saved', icon: Bookmark, color: '#3a7bf2', value: '553' },
  { key: 'fav', icon: Star, color: '#f6c33b', value: '106' },
  { key: 'liked', icon: ThumbsUp, color: '#9cc0ea', value: '278' },
]
export const dislikeStat = { value: '9' }

export interface Saver {
  key: string
  name: string
  badge?: 'bookmark' | 'like'
}
export const savers: Saver[] = [
  { key: 'eliza', name: 'eliza', badge: 'bookmark' },
  { key: 'clin', name: 'clin', badge: 'bookmark' },
  { key: 'junebog', name: 'junebog', badge: 'like' },
  { key: 'andrew', name: 'andrew...', badge: 'bookmark' },
  { key: 'ka', name: 'ka' },
]

export interface Action {
  key: string
  label: string
  icon?: LucideIcon
}
export const placeActions: Action[] = [
  { key: 'share', label: 'share', icon: Share },
  { key: 'directions', label: 'directions', icon: Compass },
  { key: 'site', label: 'site', icon: Link },
  { key: 'ig', label: 'ig' },
]

export const saveSheet = {
  segments: [
    { key: 'want', label: 'want to try', icon: Bookmark },
    { key: 'visited', label: 'visited', icon: undefined },
  ],
  active: 'visited',
  reactions: [
    { key: 'disliked', label: 'disliked', icon: ThumbsDown },
    { key: 'okay', label: 'okay', icon: Smile },
    { key: 'liked', label: 'liked', icon: ThumbsUp },
    { key: 'favorite', label: 'favorite', icon: Star },
  ],
  activeReaction: 'favorite',
  addPhotos: 'add photos',
  thoughtPlaceholder: 'what did you think?',
  addLink: 'add link',
  curation: 'add to a curation',
  save: 'save',
  note: 'add a note',
}

export const share = {
  postcard: { lines: ['LA CABRA BAKERY', '(SCANDI PASTRIES)', '— ALEX'] },
  dmsTitle: 'send via corner dms',
  contacts: [
    { key: 'search', label: 'search', icon: Search },
    { key: 'sam', label: 'Sam' },
  ],
  targets: [
    { key: 'share', label: 'share to..', icon: Share },
    { key: 'copy', label: 'copy link', icon: Link },
    { key: 'messages', label: 'messages' },
  ],
}
