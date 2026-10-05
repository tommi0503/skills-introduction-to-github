/** Design tokens for the "Delivery" app family (reference 16). */
export const theme = {
  stage: '#e5e5e5',
  screen: '#f6f6f6',
  surface: '#ffffff',
  ink: '#1f1f1f',
  inkSoft: '#3a3a3a',
  muted: '#9b9b9b',
  subtle: '#b4b4b4',
  field: '#f3f3f3',
  hairline: '#e4e4e4',
  dark: '#212121',
  orange: '#fa6b29',
  orangeFrom: '#f8723f',
  orangeTo: '#fd903f',
  blue: '#3b82f6',
  amber: '#e9a23b',
} as const

export const orangeGradient = `linear-gradient(90deg, ${theme.orangeFrom}, ${theme.orangeTo})`

/** Geometry shared by the three phones (stage px). */
export const phone = {
  width: 211,
  height: 459,
  logicalWidth: 390,
  radius: 20,
} as const
