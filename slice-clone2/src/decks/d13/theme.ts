/** d13 — beige notebook with coloured index tabs. */
export const t = {
  bg: '#fcefea',
  shadow: '#a8a79e',
  tan: '#e6c5b5',
  pink: '#e888a2',
  blue: '#90b5c9',
  green: '#437b56',
  ink: '#111',
  text: '#222',
  soft: '#f3f2f4',
  sans: 'font-notosans',
} as const

/** Accent palette keyed by name; `bg` is the pale card fill, `fg` the accent. */
export const tone = {
  pink: { fg: '#e888a2', bg: '#fbeeee', text: '#e888a2' },
  blue: { fg: '#90b5c9', bg: '#eef3f9', text: '#90b5c9' },
  green: { fg: '#437b56', bg: '#f2f8f6', text: '#437b56' },
} as const
export type Tone = keyof typeof tone
