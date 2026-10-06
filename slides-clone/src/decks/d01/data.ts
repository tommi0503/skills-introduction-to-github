import { Lightbulb, SlidersVertical, ThumbsUp, type LucideIcon } from 'lucide-react'

export interface Finding { icon: LucideIcon; title: string; body: string }
export const header = { left: 'UDAYANA UNIVERSITY', right: 'FIBRINOSA WILSON' }
export const title = 'CONCLUSION'
export const footer = { left: 'Citations', page: 'PAGE 01' }
const body = 'Lorem ipsum odor amet, consectetuer adipiscing elit.'
export const findings: Finding[] = [
  { icon: ThumbsUp, title: 'Findings', body },
  { icon: Lightbulb, title: 'Findings', body },
  { icon: SlidersVertical, title: 'Findings', body },
]
