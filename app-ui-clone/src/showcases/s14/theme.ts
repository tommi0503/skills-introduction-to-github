/** Per-mood colour theme: every screen of the app is skinned through this shape. */
export interface MoodTheme {
  key: string
  /** Screen background (solid or gradient). */
  background: string
  /** Translucent colour of the stacked "previous albums" behind the cover. */
  stackTint: string
}

export const moodThemes = {
  blue: { key: 'blue', background: '#5078db', stackTint: 'rgba(255,255,255,0.55)' },
  teal: { key: 'teal', background: 'linear-gradient(180deg,#56b68d 0%,#48a584 35%,#3a957d 60%,#2a8577 85%,#237c72 100%)', stackTint: 'rgba(255,255,255,0.55)' },
  red: { key: 'red', background: '#e72721', stackTint: 'rgba(255,255,255,0.6)' },
} satisfies Record<string, MoodTheme>

export const palette = {
  stage: '#e9e9e9',
  playerCard: '#101415',
  ink: '#111111',
  muted: '#444444',
  navAccent: '#4f7be0',
}
