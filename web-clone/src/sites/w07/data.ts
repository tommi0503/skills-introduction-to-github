import type { LucideIcon } from 'lucide-react'
import { ChevronsUpDown, Focus, Inbox, Search, Star } from 'lucide-react'

export interface Rect { x: number; y: number; w: number; h: number; radius?: number | string }

export const nav = {
  links: ['MCP', 'Customers', 'Pricing'],
  login: 'Log in',
  socials: [
    { label: 'YouTube', x: 1085 },
    { label: 'X', x: 1129 },
  ],
}

/** Each headline line: text before the inline app icon, then after it. */
export const hero = {
  lines: [
    { before: 'Where', after: 'teams', icon: 'Airbnb icon' },
    { before: 'and agents', after: 'find', icon: 'Agent app icon' },
    { before: 'designs', after: 'that work', icon: 'OpenAI icon' },
  ],
  lead: ['The design reference library for apps and sites.', '621,500 shipped screens, new every week.'],
  primary: 'Join for free',
  secondary: 'See plans',
}

export const cookie = { text: 'We use cookies.', link: 'Read more', accept: 'Accept', deny: 'Deny' }

export const trusted = {
  caption: 'Trusted by teams and agents at',
  logos: [
    { label: 'Harvey', x: 419, w: 80 },
    { label: 'Uber', x: 547, w: 66 },
    { label: 'Spotify', x: 661, w: 94 },
    { label: 'Metalab', x: 803, w: 88 },
    { label: 'Wise', x: 939, w: 83 },
  ],
}

export const story = {
  primary: ['Design research took hours.', "Now, it's one search."],
  secondary: ['Every designer has that folder.', 'Hundreds of screenshots saved for later,', 'yet somehow never the right one.'],
  feature: 'AI chat & search',
}

/** Horizontal showcase cards (landscape web shots and portrait phone shots). */
export type ShotKind = 'web' | 'phone'
export const carousel: { x: number; kind: ShotKind; label: string }[] = [
  { x: -264, kind: 'web', label: 'Perplexity academic screen' },
  { x: 332, kind: 'phone', label: 'Assistant chat screen' },
  { x: 656, kind: 'web', label: 'Template picker screen' },
  { x: 1252, kind: 'phone', label: 'Agent inbox screen' },
]

export const library = {
  title: ['One library', 'for all your needs.'],
  cards: ['Apps', 'Sites', 'Screens', 'Flows', 'Animations', 'UI Elements'] as const,
}
export type LibraryCard = (typeof library.cards)[number]

/** Media regions inside each library card, relative to the card's top-left. */
export const libraryMedia: Record<LibraryCard, Rect[]> = {
  Apps: [
    { x: 61, y: 144, w: 74, h: 74, radius: '30%' },
    { x: 200, y: 144, w: 74, h: 74, radius: '30%' },
    { x: 121, y: 131, w: 92, h: 92, radius: '30%' },
  ],
  Sites: [{ x: 40, y: 82, w: 333, h: 208, radius: 4 }],
  Screens: [{ x: 87, y: 82, w: 160, h: 347, radius: 24 }],
  Flows: [
    { x: -111, y: 82, w: 160, h: 347, radius: 18 },
    { x: 61, y: 82, w: 160, h: 347, radius: 18 },
    { x: 233, y: 82, w: 160, h: 347, radius: 18 },
  ],
  Animations: [{ x: 87, y: 82, w: 160, h: 347, radius: 18 }],
  'UI Elements': [],
}

export const toolbar: { icon: LucideIcon; active?: boolean }[] = [
  { icon: Inbox },
  { icon: Focus },
  { icon: Star, active: true },
  { icon: ChevronsUpDown },
]
export const toolbarSearch = Search

export const mcp = {
  title: ['Give your AI agents', 'access to Mobbin.'],
  cta: 'Connect MCP',
  note: 'Available on Pro & Team plans',
  clients: [
    { label: 'Cursor', w: 35 },
    { label: 'ChatGPT', w: 40 },
    { label: 'Claude', w: 40 },
    { label: 'Figma', w: 40 },
    { label: 'Grok', w: 42 },
  ],
  prompt: { before: 'Show me how top apps design ', strong: 'paywalls', after: ' that make upgrading feel worth it' },
  result: 'Found 5 apps',
}
