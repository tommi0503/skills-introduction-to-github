import type { LucideIcon } from 'lucide-react'
import { FileText, Hourglass, Sparkle, Wallet } from 'lucide-react'

export const nav = {
  menus: [
    { label: 'Product', dropdown: true },
    { label: 'Solutions', dropdown: true },
    { label: 'Resources', dropdown: true },
    { label: 'Pricing', dropdown: false },
  ],
  sales: 'Talk to sales',
  login: 'Log In',
  cta: 'Get started for free',
}

export const hero = {
  title: ['All the work around', 'meetings, handled.'],
  lead: ['From AI-powered scheduling to automated meeting recaps and', 'follow-ups, get the busywork done with fewer tools and less effort.'],
  signups: [
    { label: 'Sign up with Google', provider: 'Google', width: 224 },
    { label: 'Sign up with Microsoft', provider: 'Microsoft', width: 242 },
  ],
  email: 'Sign up with email',
  note: 'No credit card required',
}

export interface FeatureTab {
  icon: LucideIcon
  label: string
  badge?: string
  title: string[]
  body: string[]
}

/** Product tabs; the first one is shown in the captured state. */
export const features: FeatureTab[] = [
  {
    icon: Hourglass,
    label: 'Scheduling',
    title: ['Book meetings with', 'the world’s #1', 'scheduling tool'],
    body: ['Giving you complete control and total', 'customization, Calendly is the easiest and', 'most powerful way to find time to connect.'],
  },
  { icon: Sparkle, label: 'Callie', badge: 'Beta', title: [], body: [] },
  { icon: FileText, label: 'Notetaker', badge: 'New', title: [], body: [] },
  { icon: Wallet, label: 'Payments', badge: 'New', title: [], body: [] },
]
export const activeFeature = 0
export const learnMore = 'Learn more'

export const management = {
  eyebrow: 'AI meeting management',
  title: ['Built for people whose', 'work runs on meetings'],
  lead: [
    'Meetings move you forward, but the work around them can slow',
    'you down. Calendly handles the tasks before, during, and after',
    'meetings, so you have more space for what matters.',
  ],
  cta: 'Start for free',
}

export interface Stage {
  title: string
  width: number
  body?: string[]
  step?: { icon: LucideIcon; text: string }
}

export const stages: Stage[] = [
  {
    title: 'Book',
    width: 384,
    body: ['A client emails asking to meet. Share a booking', 'link or ask Callie, your AI assistant, to find times', 'that work for everyone.'],
    step: { icon: Sparkle, text: 'Callie replies with times to meet' },
  },
  { title: 'Prep', width: 248 },
  { title: 'Capture', width: 248 },
  { title: 'Follow up', width: 248 },
]
