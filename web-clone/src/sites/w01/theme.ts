/** Design tokens for the Cartesia clone. */
export const theme = {
  page: '#fefefe',
  ink: '#1e1c1a',
  muted: '#525150',
  faded: 'rgba(30, 28, 26, 0.7)',
  rule: '#e4e3db',
  panel: '#f9f9f8',
  card: '#f3f2ef',
  green: '#309d4b',
  greenDark: '#004e23',
  onGreen: '#f9f9f8',
  tick: '#f6f6f4',
  tickBand: '#fafaf9',
  column: { left: 80, width: 1280, gutter: 48 },
  fonts: {
    sans: 'font-archivo',
    serif: 'font-times',
  },
} as const

/**
 * PP Kyoto (the reference serif) is not bundled; Tinos is used instead, scaled
 * up and slightly tracked so that line widths and cap heights match.
 */
export const serifStyle = (size: number, lineHeight = size * 1.3) => ({
  fontSize: size * 1.1,
  lineHeight: `${lineHeight}px`,
  letterSpacing: `${size * 0.04}px`,
})
