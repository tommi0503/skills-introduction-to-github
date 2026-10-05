import type { LucideIcon } from 'lucide-react'
import { Plus, Layers, SquarePen } from 'lucide-react'

export const nav = {
  brand: 'Aside',
  links: ['Features', 'Use cases', 'Resources', 'Pricing'],
  cta: 'Download',
}

export const hero = {
  badge: 'Backed by Y Combinator',
  title: ['The most intelligent AI assistant,', 'but it’s a browser.'],
  cta: 'Download',
}

/** Sidebar rows of the browser mockup. `icon` = lucide glyph; `logo` = brand mark placeholder. */
export interface SidebarItem {
  label: string
  icon?: LucideIcon
  logo?: boolean
  muted?: boolean
  selected?: boolean
  trailing?: 'spinner' | 'dot' | 'count'
  indent?: boolean
}

export interface SidebarGroup { title: string; items: SidebarItem[] }

export const mockup = {
  tiles: 6,
  sidebar: [
    {
      title: 'Bookmarks',
      items: [
        { label: 'Notion', logo: true },
        { label: 'Figma', logo: true },
        { label: 'GitHub', logo: true },
      ],
    },
    {
      title: 'Chats',
      items: [
        { label: 'New Chat', icon: SquarePen, muted: true },
        { label: 'Cancel subscription and request refunds', selected: true, indent: false },
        { label: 'Finding website design example', trailing: 'spinner', indent: false },
        { label: 'San Francisco Largest Park', trailing: 'dot', indent: false },
        { label: 'Show all', muted: true, indent: false },
      ],
    },
    {
      title: 'Tabs',
      items: [
        { label: 'New Tab', icon: Plus, muted: true },
        { label: 'Agent tabs', icon: Layers, muted: true, trailing: 'count' },
        { label: 'Instagram', logo: true, muted: true },
        { label: 'Aside Browser | Notion', logo: true, muted: true },
        { label: 'Y Combinator', logo: true, muted: true },
      ],
    },
  ] satisfies SidebarGroup[],
  address: { site: 'Aside', title: 'Cancel subscription and request refunds ⋅ Chats' },
  chatTitle: 'Cancel subscription and request refunds',
  prompt: 'cancel all unused subscriptions and request refunds',
  reply: 'First, I’ll check your credit card statement to find subscriptions from last month.',
  search: { lead: 'Searched browsing history and memory for', term: 'Credit card' },
  results: [
    { title: 'Card Overview  |  Chase', detail: 'chase.com', meta: '3d ago', logo: true },
    { title: 'MEMORY.md', detail: 'User’s bank and the credit card is Chase.', meta: '8d ago', logo: true },
    { title: 'Jun’s Chase', detail: 'Passkey', meta: 'Passwords', logo: false },
  ],
  input: 'Reply, @ for context',
}

export const intro = {
  link: 'Introducing Aside',
  paragraphs: [
    {
      strong: 'Today’s AI browsers are broken.',
      rest: 'They never complete a task. They say “I can’t do this” every time. They stop every time the work gets real, and they still lack the basics: speed and usability.',
    },
    {
      strong: 'Aside is a browser rebuilt for people and agents.',
      rest: 'It works across your logged-in websites and handles complex work other agents can’t: messages, payments, internal tools, and everything in between.',
    },
  ],
}

export const capability = {
  link: 'Unlimited capability',
  title: ['Anything you do in a browser,', 'Aside can do for you.'],
  body: 'Unlike other AI agents that rely on integrations, Aside just uses websites and accounts directly, just like you do. That means you can ask any task in your mind anytime you need. The only wall is the imagination.',
  cards: [
    { title: 'Signing in', body: 'Aside signs in and works across your email, dashboards, and internal tools.' },
    { title: 'Communications', body: 'Aside handles comments, replies, and follow-ups for you.' },
    { title: 'Docs and Spreadsheets', body: 'Aside can work with files directly on your computer.' },
  ],
}

export const benchmark = {
  title: { before: 'The', faint: 'SOTA', after: 'browser agent.' },
  body: 'Aside ranked #1 on three browser agent benchmarks: Online-Mind2Web, BU-Bench-V1, and Odysseys, surpassing OpenAI, Anthropic, and Browser Use.',
  more: 'Learn more',
  rows: [
    { name: 'Aside', score: 99.0, highlight: true },
    { name: 'Browser Use', score: 97.7 },
    { name: 'GPT-5.4', score: 92.8 },
    { name: 'Claude Opus 4.8', score: 84.0 },
    { name: 'ChatGPT Atlas', score: 70.0 },
  ],
  /** Bar scale: score → width fraction of the 610px track. */
  scale: { min: 66.1, max: 99.0 },
  tabs: ['Online-Mind2Web', 'BU Bench v1', 'Odyssey'],
  activeTab: 0,
}

export const memory = {
  title: { faint: 'Memory', rest: 'that knows what you’re working on.' },
  body: 'Aside knows which sites to use for which work. It turns your browsing history into memory, so you don’t have to repeat context every time. All memory stays local on your device and is never shared with anyone.',
  more: 'Learn more',
  prompt: 'Find the candidate I opened yesterday and prep interview notes',
}

export const passwords = {
  link: 'Password Manager',
  title: 'Password that works with AI.',
  body: ['AI agents stop at login screen and ask you to log in every time.', 'Aside lets agents sign in through autofill, without ever exposing your credentials to the AI.'],
  cards: 3,
}
