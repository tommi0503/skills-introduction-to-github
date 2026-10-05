import type { LucideIcon } from 'lucide-react'
import { Images, LayoutGrid, Plus, Search, Share, SlidersHorizontal, Trash2 } from 'lucide-react'

export interface GridPhoto {
  key: string
}

export const library = {
  avatarInitial: 'S',
  dateChip: 'Wed, Feb 25',
  /** 3 columns × 6 rows, the last row cut off by the screen edge. */
  photos: [
    'tee-front', 'tee-detail', 'tee-front-2',
    'cap-front', 'cap-side', 'cap-back',
    'tote', 'tote-lamp', 'tote-logo',
    'asm', 'as', 'asmob',
    'sl-mobbin', 'slmob', 'slm',
    'gradient', 'room', 'table',
  ].map((key): GridPhoto => ({ key })),
  nav: [
    { key: 'photos', label: 'Photos', icon: Images },
    { key: 'collections', label: 'Collections', icon: LayoutGrid },
    { key: 'create', label: 'Create', icon: Plus },
  ] satisfies NavItem[],
  activeNav: 'photos',
}

export interface NavItem {
  key: string
  label: string
  icon: LucideIcon
}

export const viewer = {
  date: 'Feb 25, 2026',
  time: '4:51 AM',
  actions: [
    { key: 'share', label: 'Share', icon: Share },
    { key: 'edit', label: 'Edit', icon: SlidersHorizontal },
    { key: 'add', label: 'Add to', icon: Plus },
    { key: 'trash', label: 'Trash', icon: Trash2 },
  ] satisfies NavItem[],
}

export interface Suggestion {
  key: string
  label: string
  active?: boolean
}

export const editor = {
  aspect: 'Original',
  hint: 'Tap, circle, or brush to select',
  suggestions: [
    { key: 'enhance', label: 'Enhance' },
    { key: 'dynamic', label: 'Dynamic' },
    { key: 'ai', label: 'AI Enhance', active: true },
  ] satisfies Suggestion[],
  tools: ['Auto', 'Actions', 'Filters', 'Lighting'],
  activeTool: 'Auto',
  searchIcon: Search,
}

export const lens = {
  title: 'Google Lens',
  price: '$337*',
  source: 'GOAT',
  relatedTitle: 'Related search',
  related: [{ key: 'mobbin', label: 'Mobbin T-shirt' }],
  modes: ['Translate', 'Search'],
  activeMode: 'Search',
}
