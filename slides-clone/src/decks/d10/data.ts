import { Dumbbell, Shirt, Tv, type LucideIcon } from 'lucide-react'
export const tagline = ['EMPOWERING', 'YOUR FINANCIAL', 'FUTURE']
export const categories: { label: string; icon: LucideIcon; w: number; active?: boolean; y: number }[] = [
  { label: 'Food', icon: Tv, w: 268, y: 160 },
  { label: 'Cloth', icon: Shirt, w: 352, y: 205, active: true },
  { label: 'Entertainment', icon: Tv, w: 237, y: 252 },
  { label: 'Sport', icon: Dumbbell, w: 172, y: 298 },
]
export const activity = { heading: [['TRACK YOUR'], ['FINANCIAL'], ['ACTIVITY']], right: ['WE PRIORITIZE', 'THE SECURITY OF', 'YOUR', 'INVESTMENTS'] }
export const trust = ['YOUR', 'TRUST IS', 'PARAMO', 'UNT TO US.']
export const future = { heading: ['ENSURING', 'OUR', 'FINANCIAL', 'FUTURE'], body: ['WE BELIEVE IN', 'FOSTERING', 'ENDURING', 'RELATIONSHIPS'] }
export const record = {
  saving: ['SAVING FOR A', 'MAJOR', 'PURCHASE, OR', 'BUILDING', 'WEALTH'],
  heading: ['OUR TRACK', 'RECORD SPEAKS', 'FOR ITSELF'],
  uncertainty: ['UNCERTAINTY IN', 'FINANCIAL', 'MARKETS'],
  stats: ['41K+', '182K+'],
  cols: ['SECURITY AND TRUST: YOUR TRUST IS PARAMOUNT TO US. WE PRIORITIZE THE SECURITY OF YOUR INVESTMENTS AND ADHERE TO THE HIGHEST STANDARDS.', 'LONG-TERM FOCUS: WE BELIEVE IN FOSTERING ENDURING RELATIONSHIPS WITH OUR CLIENTS. OUR INVESTMENT STRATEGIES ARE BUILT FOR THE LONG RUN.'],
}
