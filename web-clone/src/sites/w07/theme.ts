/** Design tokens for the Mobbin landing page clone. */
export const theme = {
  font: 'font-hanken',
  ink: '#141414',
  muted: '#707070',
  subtle: '#adadad',
  surface: '#f4f4f4',
  softButton: 'rgba(64,64,64,0.08)',
  bubble: '#e9e9e9',
  banner: '#404040',
  divider: '#f0f0f0',
  white: '#ffffff',
  /** Left edge of the 1045px content column. */
  gutter: 198,
  contentWidth: 1045,
} as const

/** Text styles taken from the reference DOM (size / line-height / weight / tracking). */
export const type = {
  nav: { fontSize: 16, lineHeight: '22px', fontWeight: 600, letterSpacing: '0.2px' },
  display: { fontSize: 80, lineHeight: '80px', fontWeight: 652, letterSpacing: '-0.6px' },
  h2: { fontSize: 44, lineHeight: '48px', fontWeight: 652, letterSpacing: '-0.4px' },
  lead: { fontSize: 20, lineHeight: '26px', fontWeight: 440 },
  cardTitle: { fontSize: 20, lineHeight: '26px', fontWeight: 600 },
  small: { fontSize: 14, lineHeight: '20px', fontWeight: 456, letterSpacing: '0.2px' },
  tiny: { fontSize: 12, lineHeight: '16px', fontWeight: 456, letterSpacing: '0.2px' },
} as const
