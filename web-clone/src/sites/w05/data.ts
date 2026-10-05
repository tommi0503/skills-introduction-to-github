import type { Accent } from './theme'

export const nav = {
  wordmarkInitial: 'M',
  wordmarkRest: 'onologue',
  links: ['Dictation', 'Notes', 'Features', 'Pricing', 'Docs'],
  ios: 'Download for iOS',
  mac: 'Download for Mac',
}

export const announcement = { text: 'Introducing mono-1: our first model built for dictation', cta: 'Read more' }

export const hero = {
  pill: 'Start working 3× faster today',
  title: 'Builders think out loud.',
  body: 'Monologue brings voice dictation, voice notes, and bot-free meeting transcription together in one app for Mac, iPhone, iPad, and Apple Watch.',
  cta: 'Download for Mac',
  availableLabel: 'Available for',
  availableLink: 'iPhone, iPad, and Apple Watch',
}

export interface ProductTab {
  label: string
  accent: Accent
  icon: 'mic' | 'notes' | 'api'
}

export const productTabs: ProductTab[] = [
  { label: 'Dictation', accent: 'dictation', icon: 'mic' },
  { label: 'Notes', accent: 'notes', icon: 'notes' },
  { label: 'MCP / API / CLI', accent: 'api', icon: 'api' },
]

export interface Rect {
  x: number
  y: number
  w: number
  h: number
}

export const logos = {
  caption: 'Used by builders at companies including',
  /** Visible customer logos in the captured marquee (x relative to the page, y relative to the strip). */
  items: [
    { x: -49, y: 113, w: 149, h: 34 },
    { x: 185, y: 119, w: 145, h: 22 },
    { x: 428, y: 117, w: 103, h: 26 },
    { x: 640, y: 117, w: 122, h: 26 },
    { x: 853, y: 117, w: 140, h: 25 },
    { x: 1065, y: 120, w: 160, h: 16 },
    { x: 1308, y: 116, w: 118, h: 27 },
  ] as Rect[],
}

export type ManifestoPart = string | { word: string; accent: Accent; icon: ProductTab['icon'] | 'video' }

export const manifesto: { lead: string; body: ManifestoPart[]; close: string } = {
  lead: 'Monologue is what happens when you talk through your work instead of typing it.',
  body: [
    'It starts as ',
    { word: 'dictation', accent: 'dictation', icon: 'mic' },
    ' that writes what you meant. Use it for ',
    { word: 'voice notes', accent: 'notes', icon: 'notes' },
    ' on a walk. Use it for ',
    { word: 'meetings', accent: 'meetings', icon: 'video' },
    ' without a bot. Give the transcript to your agents and keep building.',
  ],
  close: 'It stays with you from Cursor to a walk to a call.',
}

export const dictationFeature = {
  eyebrow: 'Dictation',
  title: ['Use your voice', 'wherever you type'],
  body: 'Draft a coding prompt, share a team update, text a friend, or reply to an email. Monologue turns what you say into clear text that fits the app you’re in.',
  apps: ['Coding', 'Team chat', 'Messages', 'Email'],
}

export interface Showcase {
  /** Top of the mockup frame, relative to the feature block. */
  top: number
  title: string
  body: string
  iconSize: number
}

export const showcases: Showcase[] = [
  {
    top: 321,
    title: 'Give your coding agent the whole task',
    body: 'Monologue uses the code around you to get file names and technical terms right.',
    iconSize: 20,
  },
  {
    top: 1203,
    title: 'Say the list. Skip the formatting.',
    body: 'Speak each item in order. Monologue turns them into a numbered list before you send.',
    iconSize: 14,
  },
  { top: 2085, title: '', body: '', iconSize: 0 },
]
