import type { LucideIcon } from 'lucide-react'
import {
  PhoneIncoming,
  Signature,
  Sun,
  SearchCode,
  ShieldHalf,
  Infinity as InfinityIcon,
  Settings,
  MessageCircle,
  Share,
  Clock,
  Inbox,
  Phone,
  Grip,
  Cog,
} from 'lucide-react'

export interface Feature {
  icon: LucideIcon
  label: string
}
export const features: Feature[] = [
  { icon: PhoneIncoming, label: 'Virtual receptionist for calls' },
  { icon: Signature, label: 'Note-taking on phone calls' },
  { icon: Sun, label: 'Daily recap listing to-dos' },
  { icon: SearchCode, label: 'Search conversations with AI' },
  { icon: ShieldHalf, label: 'Spam calls filter' },
  { icon: InfinityIcon, label: 'Unlimited texts & calls (US & CA)' },
]

export interface Plan {
  key: string
  name: string
  price: string
  perWeek: string
  badge?: string
  selected?: boolean
}
export const plans: Plan[] = [
  { key: 'yearly', name: 'Yearly', price: '$199.99/year', perWeek: '$3.85/week', badge: '45% DISCOUNT', selected: true },
  { key: 'monthly', name: 'Monthly', price: '$29.99', perWeek: '$6.92/week' },
]
export const paywallLinks = ['Terms', 'Restore Purchase', 'Privacy']

export const inboxChips = [
  { key: 'all', label: 'All' },
  { key: 'unread', label: 'Unread' },
  { key: 'ask', label: 'Ask Beside AI' },
  { key: 'memo', label: 'Memo' },
  { key: 'd', label: 'Drafts' },
]

export type AvatarKind = 'number' | 'orb' | 'gift' | 'photo' | 'sun' | 'red'
export interface InboxItem {
  key: string
  avatar: AvatarKind
  /** Blurred/hidden title rendered as a grey bar when absent. */
  title?: string
  meta?: string
  subtitle: string
  action?: LucideIcon
  actionFilled?: boolean
  actionInverse?: boolean
}
export const pinnedItems: InboxItem[] = [
  { key: 'number', avatar: 'number', subtitle: 'Customize your number', action: Settings },
  { key: 'ask', avatar: 'orb', title: 'Ask Beside AI', subtitle: 'Ask your calls & chats anything', action: MessageCircle, actionFilled: true },
  { key: 'gift', avatar: 'gift', title: 'Gift Beside, Earn $50', subtitle: '14 days free for your contacts', action: Share },
]
export const threadItems: InboxItem[] = [
  { key: 'mobbin', avatar: 'photo', title: 'Mobbin team', meta: 'just now', subtitle: 'You: What’s up team!' },
  { key: 'recap', avatar: 'sun', title: 'Daily Recap', meta: '23h', subtitle: 'Wed, Feb 11', action: Clock, actionInverse: true },
  { key: 'hours', avatar: 'orb', title: 'Preferred Hours Inquiry', meta: '2d', subtitle: 'As your Beside assistant, I’m here to help you' },
  { key: 'fin', avatar: 'red', title: 'Financial Objective Discussion', meta: '2d', subtitle: 'Let’s talk about your goals', action: Clock, actionInverse: true },
]

export interface Tab {
  key: string
  label: string
  icon?: LucideIcon
}
export const tabs: Tab[] = [
  { key: 'inbox', label: 'Inbox', icon: Inbox },
  { key: 'calls', label: 'Calls', icon: Phone },
  { key: 'ai', label: 'AI' },
  { key: 'dial', label: 'Dial', icon: Grip },
  { key: 'settings', label: 'Settings', icon: Cog },
]

export interface Suggestion {
  key: string
  label: string
}
export const suggestionRows: Suggestion[][] = [
  [
    { key: 's1', label: 'How could I have better handled my last call?' },
    { key: 's2', label: 'What did I promise to do?' },
  ],
  [
    { key: 's3', label: 'Show me missed calls' },
    { key: 's4', label: 'Help me draft the perfect reply' },
  ],
]

export const keyboard = {
  suggestions: ['I', 'The', 'I’m'],
  rows: ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM'],
}
