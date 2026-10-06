import { theme } from './theme'
export interface Step { label: string; title: string; text?: string; bullets?: string[]; chips: string[]; chipY: number }
export const tag = 'HOW IT WORKS'
export const steps: Step[] = [
  { label: 'Step 1', title: 'Submit a recording', text: 'to the daily challenge prompt in the language of your choice', chips: [theme.blue], chipY: 416 },
  { label: 'Step 2', title: 'Compete & get ranked', text: 'on global or local leaderboards for bragging rights and prize eligibility', chips: [theme.coral, theme.sand], chipY: 416 },
  { label: 'Step 3', title: 'Earn badges', bullets: ["Proficiency badges (e.g. 'best pronunciation')", "User-voted badges (e.g. 'funniest response')"], chips: [theme.coral, theme.sand], chipY: 453 },
  { label: 'Step 4', title: 'Rinse, repeat', text: 'Extend your streaks to track your consistency and show off to friends', chips: [theme.blue, theme.coral, theme.sand], chipY: 416 },
]
export const legend = [
  { color: theme.blue, text: 'Low barrier to entry' },
  { color: theme.coral, text: 'Socially engaging' },
  { color: theme.sand, text: 'Incentives and rewards' },
]
