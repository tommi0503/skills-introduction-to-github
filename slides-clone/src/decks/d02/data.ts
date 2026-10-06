import { theme } from './theme'
export interface Feature { title: string; color: string; bullets: string[] }
export const tag = 'KEY FEATURES'
export const title = ["We've designed a comprehensive suite of features to", 'facilitate our unique experience']
export const features: Feature[] = [
  { title: 'Dynamic Context', color: theme.blue, bullets: ['Practical learning scenarios, unique conversations that users can access on-demand through AI'] },
  { title: 'Authentic Community', color: theme.coral, bullets: ['Gives creators space to engage with and build their following', 'Allows audience to interact with their favorite creators and sharpen their skills alongside their learners'] },
  { title: 'Gamified Experience', color: theme.sand, bullets: ['Community and global leaderboards to incentivize progress and even monetary prizes'] },
]
