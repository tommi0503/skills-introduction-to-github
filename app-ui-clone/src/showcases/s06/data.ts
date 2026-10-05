import { Briefcase, CalendarClock, Send, type LucideIcon } from 'lucide-react'

export interface QuickStartItem {
  key: string
  title: string
  subtitle: string
  icon: LucideIcon
}

export const inbox = {
  title: 'Inbox',
  priorityLabel: 'AI Priority',
  count: '12',
  countLabel: 'Need Attention',
  sectionLabel: 'Next Up',
  mail: { subject: 'Design Proposal', from: 'Daniel Smith', time: '9:30 AM', preview: 'Let’s move forward.' },
  suggestion: { label: 'AI suggest a reply', timer: '18s' },
}

export const create = {
  title: 'Create',
  prompt: 'What should this email say?',
  placeholder: 'Describe your email in a few words..',
  generate: 'Generate',
  counter: '0/300',
  quickStart: 'Quick Start',
  cta: 'Generate Draft',
}

export const quickStart: QuickStartItem[] = [
  { key: 'meeting', title: 'Meeting', subtitle: 'Meetings, organized by AI.', icon: CalendarClock },
  { key: 'proposal', title: 'Proposal', subtitle: 'Prepared by AI.', icon: Briefcase },
  { key: 'followup', title: 'Follow- up', subtitle: 'Send a quick follow-up.', icon: Send },
]

export const draft = {
  title: 'Draft Ready',
  subtitle: 'Your email is ready to send.',
  score: 98,
  scoreLabel: 'Clarity Score',
  tipTitle: 'Smart Tip',
  tipBody: 'Add a clear CTA to increase response',
  tipAction: 'Add CTA',
  cta: 'Sent Email',
}
