/** Design tokens for the snacks app (showcase 10). */
export const theme = {
  stage: '#dadfe5',
  screen: '#f8f8f8',
  yellow: '#ffcc00',
  yellowSoft: '#ffec96',
  yellowPale: '#fff3c4',
  orange: '#ff9e37',
  orangeSoft: '#fdd5ac',
  ink: '#000000',
  muted: '#8a8a8a',
  chip: '#ffffff',
  tabIdle: '#f2f2f3',
  phoneShadow: '0 14px 40px rgba(70, 80, 100, 0.35), 0 2px 8px rgba(70, 80, 100, 0.2)',
} as const

export const font = 'font-jakarta'

/** Phones are 200 stage px wide and designed at 390pt. */
export const phone = { width: 200, height: 435, logicalWidth: 390, radius: 21 } as const
