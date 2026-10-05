/** Tokens for the AI food app (reference 18). */
export const theme = {
  stage: '#dedde3',
  screen: '#ffffff',
  ink: '#111111',
  text: '#3f3f46',
  muted: '#8b8b93',
  soft: '#f3f3f5',
  blue: '#2f7cf6',
  bot: '#7ea4f6',
  botSoft: '#dfe7fb',
  cardBlue: '#c4d7f8',
  cardYellow: '#fde7bd',
  cardPink: '#f6d9d5',
  heart: '#e5322d',
} as const

export type CardTone = 'blue' | 'yellow' | 'pink'
export const cardTones: Record<CardTone, string> = {
  blue: theme.cardBlue,
  yellow: theme.cardYellow,
  pink: theme.cardPink,
}

export const phone = {
  width: 208,
  height: 440,
  logicalWidth: 390,
  radius: 29,
} as const
