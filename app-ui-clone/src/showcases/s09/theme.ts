/** Design tokens for TheKitchen~ (showcase 09). */
export const theme = {
  stage: '#e1e2e4',
  dark: '#1f1f1f',
  darkField: '#3d3d3d',
  lime: '#ccff00',
  canvas: '#f5f5f7',
  card: '#ffffff',
  ink: '#111111',
  muted: '#a3a3a3',
  hairline: '#ececee',
  stepper: '#e9e9eb',
} as const

/** Device geometry in stage px. Screens are designed at 375pt wide. */
export const device = { width: 173, logicalWidth: 375, radius: 14, height: 374 } as const
