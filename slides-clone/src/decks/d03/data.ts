import { Flame, Plus, Zap, type LucideIcon } from 'lucide-react'
export const tag = 'UNIQUE SELLING PROPOSITION'
export const title = ['...with a focus on practical application in a socially', 'rewarding way']
export const lead = ['Generating usage momentum', 'through engaging features']
export const bullets = [
  { bold: 'Daily speaking challenges', text: ': low barrier to incentivize initial engagement' },
  { bold: 'Challenge streaks', text: ': competitive-element to encourage recurring usage' },
  { bold: 'Badges', text: ': community-driven recognition and social validation for users to build depth with other users and app' },
]
export interface Perk { label: string; text: string; icon: LucideIcon; color: string; x: number; y: number }
export const perks: Perk[] = [
  { label: 'Challenges', text: 'Daily bragging rights', icon: Plus, color: '#5b9bf5', x: 940, y: 238 },
  { label: 'Streaks', text: 'Showoff your consistency', icon: Zap, color: '#e0b878', x: 915, y: 395 },
  { label: 'Badges', text: 'Challenge for fame!', icon: Flame, color: '#f08a84', x: 940, y: 551 },
]
