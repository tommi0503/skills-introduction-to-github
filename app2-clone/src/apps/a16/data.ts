import type { LucideIcon } from 'lucide-react'
import {
  Book,
  Clock3,
  Earth,
  Globe,
  Headphones,
  House,
  LibraryBig,
  NotebookTabs,
  Plus,
  ScanText,
  Type,
  UserCheck,
} from 'lucide-react'

export interface AuthOption {
  key: string
  label: string
  /** Brand mark rendered as a placeholder before the label. */
  brand?: 'apple' | 'google'
  variant: 'dark' | 'soft' | 'outline'
}

export const welcome = {
  brand: 'ElevenReader',
  headline: 'Discover the perfect voice for every story.',
  body: 'Listen to your favorite books, articles, and PDFs with stunningly natural voice AI.',
  options: [
    { key: 'apple', label: 'Continue with Apple', brand: 'apple', variant: 'dark' },
    { key: 'google', label: 'Continue with Google', brand: 'google', variant: 'soft' },
    { key: 'create', label: 'Create an account', variant: 'outline' },
    { key: 'signin', label: 'Sign in', variant: 'soft' },
  ] satisfies AuthOption[],
}

export interface Plan {
  key: string
  name: string
  detail: string
  price: string
  selected?: boolean
  badge?: string
}

export const paywall = {
  title: 'Listen to anything without limits',
  rating: { stars: 5, label: '4.7 stars from 50,000+ listeners' },
  features: [
    { label: 'Listen with unlimited hours', highlight: true },
    { label: '1,000+ studio-quality, lifelike voices' },
    { label: 'Create custom voices' },
    { label: 'Download to listen offline' },
  ],
  plans: [
    {
      key: 'annual',
      name: 'Annual',
      detail: '3 days free, billed as S$ 149.98/yr',
      price: '$2.87/week',
      selected: true,
      badge: 'OUR BEST VALUE • SAVE 17%',
    },
    { key: 'monthly', name: 'Monthly', detail: 'S$ 14.98/mo', price: '$3.44/week' },
  ] satisfies Plan[],
  cta: 'Try Unlimited for $0.00',
  footnote: '3 days free. We’ll remind you before it ends —\ncancel anytime.',
}

export interface IconItem {
  key: string
  label: string
  icon: LucideIcon
  /** Solid glyph (filled with currentColor). */
  filled?: boolean
}

export interface Collection {
  key: string
  label: string
  title: string
  description: string
  tone: string
}

export interface MiniBook {
  key: string
  title: string
}

export const home = {
  title: 'Home',
  filters: [
    { key: 'foryou', label: 'For you', icon: LibraryBig },
    { key: 'following', label: 'Following', icon: UserCheck, filled: true },
    { key: 'recents', label: 'Recents', icon: Clock3, filled: true },
  ] satisfies IconItem[],
  activeFilter: 'foryou',
  uploadTitle: 'Upload & listen',
  uploads: [
    { key: 'write', label: 'Write\ntext', icon: Type },
    { key: 'upload', label: 'Upload\na file', icon: NotebookTabs },
    { key: 'scan', label: 'Scan\ntext', icon: ScanText },
    { key: 'paste', label: 'Paste\na link', icon: Globe },
  ] satisfies IconItem[],
  collectionsTitle: 'Recommended collections',
  collections: [
    {
      key: 'scifi',
      label: 'Sci-fi',
      title: 'Science Fiction',
      description: 'Futuristic scenes, high stake worlds, and mind-bending ideas',
      tone: '#6fb9b2',
    },
    {
      key: 'dystopia',
      label: '',
      title: 'Dystopia',
      description: 'Bleak futures and the fight for survival',
      tone: '#b9c4bf',
    },
  ] satisfies Collection[],
  mini: [
    { key: 'unscripted', title: 'Unscripted' },
    { key: 'operation', title: 'Operation\nShadowstrike' },
    { key: 'stars', title: 'The Stargazers:\nNew World Or...' },
    { key: 'lost', title: 'The Lost C...\nSymphony' },
  ] satisfies MiniBook[],
  tabs: [
    { key: 'home', label: 'Home', icon: House, filled: true },
    { key: 'explore', label: 'Explore', icon: Book, filled: true },
    { key: 'import', label: 'Import', icon: Plus },
    { key: 'library', label: 'Library', icon: Headphones },
    { key: 'voices', label: 'Voices', icon: Earth, filled: true },
  ] satisfies IconItem[],
  activeTab: 'home',
}

export interface Book {
  key: string
  title: string
  author: string
  duration?: string
  price?: string
  ultra?: boolean
}

export const travel = {
  title: 'Travel',
  description: 'Journeys across cultures, landscapes, and destinations',
  meta: '14 books · Updated 9 hours ago',
  books: [
    { key: 'china', title: 'China Travel Guide', author: 'Dan Marson', duration: '1h 25m', price: 'S$3.85' },
    { key: 'zhob', title: 'Zhob', author: 'Saraban K. K.', duration: '43m', ultra: true },
    { key: 'wander', title: 'Wanderlust and the Hidden Paths', author: '' },
    { key: 'between', title: 'Between Sky and Moon', author: '' },
  ] satisfies Book[],
}
