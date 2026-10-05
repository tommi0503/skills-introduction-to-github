/** Design tokens for the Rentique fashion-rental app (logical iOS points). */
export const theme = {
  font: 'font-jakarta',
  ink: '#1c1c1c',
  muted: '#8f8f8f',
  line: '#ececec',
  chipBg: '#f4f4f5',
  cardCream: '#f6f3ee',
  dark: '#222222',
  brand: '#4f5bff',
  pro: '#f5d000',
} as const

/** Device geometry shared by both phones (measured from the reference). */
export const device = {
  width: 314,
  height: 681,
  logicalWidth: 375,
  radius: 30,
} as const
