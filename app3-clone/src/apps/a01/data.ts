import {
  Bookmark,
  CircleUserRound,
  Heart,
  House,
  MessageCircle,
  Repeat,
  Search,
  Send,
  SquarePlay,
  type LucideIcon,
} from 'lucide-react'

export interface Story {
  key: string
  label: string
  /** "own" = your story (no ring, plus badge). */
  kind: 'own' | 'ring'
}

export const stories: Story[] = [
  { key: 'you', label: 'Your story', kind: 'own' },
  { key: 'welcome', label: 'Welcome', kind: 'ring' },
  { key: 'instagram', label: 'instagram', kind: 'ring' },
  { key: 'igforbusiness', label: 'instagramforbusiness', kind: 'ring' },
]

export interface NavTab {
  key: string
  icon: LucideIcon
}

export const navTabs: NavTab[] = [
  { key: 'home', icon: House },
  { key: 'reels', icon: SquarePlay },
  { key: 'messages', icon: Send },
  { key: 'search', icon: Search },
  { key: 'profile', icon: CircleUserRound },
]

export const feedPost = {
  authors: 'dwellmagazine',
  coAuthor: 'wrongmarfa',
  counter: '2/5',
}

export interface PostAction {
  key: string
  icon: LucideIcon
  count: string
}

export const reelPost = {
  author: 'instagram',
  audio: 'Johnny Cash · Ring of Fire',
  caption: 'lenticular art rings that move with you...',
  time: '1 day ago',
  actions: [
    { key: 'like', icon: Heart, count: '220K' },
    { key: 'comment', icon: MessageCircle, count: '3,778' },
    { key: 'repost', icon: Repeat, count: '2,213' },
    { key: 'share', icon: Send, count: '7,187' },
  ] satisfies PostAction[],
  saveIcon: Bookmark,
}

export const cameraModes = ['POST', 'STORY', 'REEL'] as const
export const activeCameraMode = 'STORY'

export interface GalleryTile {
  key: string
  /** Selection order badge, if picked. */
  order?: number
  camera?: boolean
}

export const galleryTiles: GalleryTile[] = [
  { key: 'camera', camera: true },
  { key: 'sea-rocks', order: 1 },
  { key: 'sand', order: 2 },
  { key: 'tower' },
  { key: 'blue-light' },
  { key: 'white-arch' },
  { key: 'city-night' },
  { key: 'blue-stairs' },
  { key: 'rocks' },
  { key: 'building' },
  { key: 'people' },
  { key: 'cups' },
]

export const newPost = { title: 'New post', next: 'Next', album: 'Stocks' }
