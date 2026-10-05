import {
  Bookmark,
  Folder,
  Store,
  Users,
} from 'lucide-react'
import type { LucideIcon } from 'lucide-react'

export interface AuthOption {
  key: 'google' | 'apple' | 'microsoft' | 'sso'
  label: string
  dark?: boolean
}
export const signIn = {
  title: 'Sign in to Goodnotes',
  options: [
    { key: 'google', label: 'Continue with Google' },
    { key: 'apple', label: 'Continue with Apple', dark: true },
    { key: 'microsoft', label: 'Continue with Microsoft' },
    { key: 'sso', label: 'Single sign-on (SSO)' },
  ] as AuthOption[],
  remember: 'Remember me',
  trouble: 'Trouble signing in?',
}

export type ThumbKind = 'folder' | 'greenFolder' | 'image' | 'blank'
export interface DocItem {
  title: string[]
  date: string
  thumb: { kind: ThumbKind; x: number; y: number; w: number; h: number; radius?: number }
  /** label block top (px, screen) */
  labelTop: number
  shared?: boolean
  starred?: boolean
  star?: { x: number; y: number }
}

/** Column centres of the 3-up grid. */
export const columns = [72, 194, 316]

export const documents: DocItem[] = [
  { title: ['Chemistry'], date: 'Today', thumb: { kind: 'greenFolder', x: 26, y: 245, w: 92, h: 81 }, labelTop: 333, star: { x: 98, y: 262 } },
  { title: ['Generated', 'Notes'], date: 'Yesterday', thumb: { kind: 'folder', x: 149, y: 245, w: 91, h: 80 }, labelTop: 335, star: { x: 219, y: 272 } },
  { title: ['Mind Map'], date: 'Yesterday', thumb: { kind: 'image', x: 281, y: 233, w: 64, h: 85, radius: 2 }, labelTop: 333, star: { x: 328, y: 249 } },
  { title: ['Mobbin'], date: 'Yesterday', thumb: { kind: 'image', x: 37, y: 432, w: 64, h: 84, radius: 2 }, labelTop: 532, shared: true, starred: true, star: { x: 84, y: 449 } },
  { title: ['Mobbin -', 'Whiteboard'], date: 'Yesterday', thumb: { kind: 'image', x: 149, y: 454, w: 92, h: 71, radius: 6 }, labelTop: 534, star: { x: 223, y: 470 } },
  { title: ['Project', 'Road...urple)'], date: 'Yesterday', thumb: { kind: 'image', x: 271, y: 459, w: 85, h: 56, radius: 4 }, labelTop: 534, star: { x: 339, y: 475 } },
  { title: ['Untitled Text', 'Document'], date: '', thumb: { kind: 'blank', x: 28, y: 632, w: 85, h: 88, radius: 3 }, labelTop: 733, star: { x: 96, y: 649 } },
]

export interface DockTab {
  key: string
  label: string
  icon: LucideIcon
}
export const dockTabs: DockTab[] = [
  { key: 'documents', label: 'Documents', icon: Folder },
  { key: 'favorites', label: 'Favorites', icon: Bookmark },
  { key: 'shared', label: 'Shared', icon: Users },
  { key: 'marketplace', label: 'Marketplace', icon: Store },
]

export const newFolder = {
  title: 'New Folder',
  name: 'Mobbin',
  tabs: ['Color', 'Icon'],
  selected: '1-4',
  swatches: [
    ['#833327', '#8d4225', '#845c20', '#3d6f28', '#475eab', '#62469f', '#843f6b'],
    ['#dd6f70', '#e5a463', '#e9ca50', '#91d96b', '#94baf5', '#c4aaf5', '#e696ca'],
    ['#ecb1b3', '#f1cfa9', '#f3e789', '#c5f0a1', '#d4e4fb', '#e7dafa', '#f0d0e7'],
    ['#1e1c1d', '#5b5b59', '#bebcb8', '#e3e2dd', '#ffffff', 'wheel'],
  ],
}

export const editor = {
  tabs: [
    { label: 'Untitled (D...', active: true, menu: true },
    { label: 'Untitled Text...', active: false, menu: false },
  ],
}

export const audioClip = {
  title: 'Audio Clip 1',
  tabs: ['Summary', 'Transcript'],
  view: 'View generated notes',
  speed: '1.0×',
  elapsed: '00:07',
  total: '00:22',
  progress: 0.32,
  disclaimer: 'AI content may be inaccurate',
}

export const aiChat = {
  prompt: 'map with labels',
  answer:
    'I created a labeled UX design brainstorming map featuring key sections such as user personas, user journey, wireframes, features, pain points, solutions, and design ideas, visually connected to illustrate the brainstorming process.',
  review: 'Review',
  badge: 'AI Content',
  insert: 'Insert into Page 1',
  discard: 'Discard',
  placeholder: 'Start with an idea...',
  create: 'Create',
  disclaimer: 'AI content may be inaccurate',
}
