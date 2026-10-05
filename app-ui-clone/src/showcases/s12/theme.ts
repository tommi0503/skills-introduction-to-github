/** Tokens for the "blastup" growth app (showcase 12). */
export const theme = {
  stage: '#563cf3',
  brand: '#563cf5',
  pink: '#ff74cb',
  blue: '#3b7df0',
  ink: '#111111',
  surface: '#f7f7f7',
  chipGrey: '#efefef',
} as const

export const device = {
  width: 153,
  height: 320,
  logicalWidth: 393,
  screenRadius: 19,
  bezel: { thickness: 4.5, color: '#020202' },
} as const

/** Headline typography shared by every screen. */
export const headline = 'text-[28px] leading-[33px] font-medium tracking-[-0.035em]'
