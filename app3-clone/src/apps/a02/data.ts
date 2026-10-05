import { Clock3, ShieldCheck, type LucideIcon } from 'lucide-react'

export const refund = {
  title: 'Review refund',
  ticket: 'Ticket #4821',
  amount: '$124.00',
  risk: 'Medium risk',
  recipient: 'Refund to Maya Chen · Visa ••4412',
  reasonHeading: 'Why the agent wants this',
  reason: 'Order arrived damaged.',
  policy: 'Policy:  full refund under $150 if photo attached.',
  attachment: { name: 'IMG-3228.jpg', caption: 'Photo evidence', action: 'View' },
  source: { label: 'Source', value: 'RefundPolicyv3.2' },
}

export interface Metric {
  key: string
  icon: LucideIcon
  label: string
  value: string
}

export const metrics: Metric[] = [
  { key: 'match', icon: ShieldCheck, label: 'Policy match', value: '94%' },
  { key: 'waiting', icon: Clock3, label: 'Waiting', value: '2 min' },
]

export const actions = { deny: 'Deny', approve: 'Approve & Send' }

export interface Thumb {
  key: string
  active?: boolean
}

export const evidence = {
  thumbs: [{ key: 'front', active: true }, { key: 'side' }, { key: 'top' }] satisfies Thumb[],
  caption: 'IMG-3228.jpg attached to ticket #4821',
}
