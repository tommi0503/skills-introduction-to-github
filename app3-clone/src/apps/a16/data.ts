import { Dumbbell, type LucideIcon } from 'lucide-react'

export interface Token {
  word: string
  /** Already placed in the answer → rendered as an empty grey slot. */
  used?: boolean
}

export interface Badge {
  label: string
  color: string
  /** lucide glyph on a filled circle, or null → illustrated badge (placeholder). */
  icon: LucideIcon | null
}

export interface PromptWord {
  text: string
  bold?: boolean
}

export interface Exercise {
  id: string
  progress: number
  progressColor: string
  badge: Badge
  title: string
  /** Character illustration box. */
  character: { x: number; y: number; w: number; h: number }
  bubble: { y: number; speaker: boolean; words: PromptWord[] }
  /** Top of the answer area (first rule line). */
  answerTop: number
  answer: Token[]
  bankTop: number
  bank: Token[][]
  layout: { badgeY: number; titleY: number }
}

export const exercises: Exercise[] = [
  {
    id: 'new-word',
    progress: 0.31,
    progressColor: '#58cc02',
    badge: { label: 'NEW WORD', color: '#c46fe6', icon: null },
    title: 'Translate this sentence',
    character: { x: 40, y: 205, w: 76, h: 178 },
    bubble: {
      y: 271,
      speaker: true,
      words: [{ text: 'Le' }, { text: 'parc' }, { text: 'est' }, { text: 'petit', bold: true }],
    },
    answerTop: 443,
    answer: [{ word: 'The' }],
    bankTop: 572,
    bank: [
      [{ word: 'bread' }, { word: 'French' }, { word: 'fun' }, { word: 'is' }, { word: 'lives' }],
      [{ word: 'park' }, { word: 'small' }, { word: 'The', used: true }],
    ],
    layout: { badgeY: 128, titleY: 171 },
  },
  {
    id: 'hard',
    progress: 0.94,
    progressColor: '#f49c1c',
    badge: { label: 'HARD EXERCISE', color: '#e0474c', icon: Dumbbell },
    title: 'Translate this sentence',
    character: { x: 18, y: 205, w: 114, h: 160 },
    bubble: {
      y: 263,
      speaker: false,
      words: [{ text: 'The' }, { text: 'stores' }, { text: 'are' }, { text: 'small' }],
    },
    answerTop: 434,
    answer: [{ word: 'Les' }, { word: 'magasins' }, { word: 'sont' }, { word: 'petits' }],
    bankTop: 568,
    bank: [
      [{ word: 'bonne soirée' }, { word: 'elles' }, { word: 'homme' }, { word: 'il' }],
      [
        { word: 'Les', used: true },
        { word: 'magasins', used: true },
        { word: 'sont', used: true },
        { word: 'petits', used: true },
      ],
    ],
    layout: { badgeY: 124, titleY: 163 },
  },
]

export const checkLabel = 'CHECK'
