/** TADA design tokens (logical iOS points, 390pt-wide screens). */
export const theme = {
  stage: '#16171b',
  navy: '#283163',
  ink: '#2a2d3e',
  text: '#1c1c1e',
  sub: '#6f7280',
  muted: '#9a9fae',
  inputBg: '#f0f7fe',
  inputBorder: '#e2eefb',
  line: '#ececf0',
  band: '#f5f5f7',
  bannerBlue: '#bbe0fd',
  passport: '#3d8fe0',
  dim: 'rgba(20,20,24,0.45)',
} as const

export const device = {
  width: 326,
  height: 706,
  logicalWidth: 390,
  radius: 28,
  top: 37,
} as const
