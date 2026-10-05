/** Laundrygo design tokens (logical iOS points, 390pt wide screens). */
export const theme = {
  stage: '#16171b',
  lime: '#d8fa68',
  limeLine: '#daf978',
  ink: '#1c1c1c',
  text: '#2a2a2a',
  sub: '#7a7a7a',
  muted: '#9e9e9e',
  tabLine: '#e6e6e6',
  placeholderOnDark: '#b9bcc2',
} as const

/** Device geometry measured in the reference (stage px). */
export const device = {
  width: 326,
  height: 707,
  logicalWidth: 390,
  radius: 22,
  top: 42,
} as const
