/** Design tokens for the Calendly landing page clone. */
export const theme = {
  body: 'font-geist',
  display: 'font-archivo',
  ink: '#071a31',
  muted: '#5f6d77',
  chip: '#3d464e',
  page: '#fcfbf8',
  panel: '#f5f3ee',
  white: '#ffffff',
  tabIdle: '#dcdfe5',
  tabActive: '#6aaef5',
} as const

export const type = {
  nav: { fontSize: 14, lineHeight: '19.6px', fontWeight: 500 },
  h1: { fontSize: 72, lineHeight: '79.2px', fontWeight: 500, letterSpacing: '-2.3px' },
  h2: { fontSize: 60, lineHeight: '66px', fontWeight: 500, letterSpacing: '-2.2px' },
  featureTitle: { fontSize: 36, lineHeight: '39.6px', fontWeight: 500, letterSpacing: '-1px' },
  h3: { fontSize: 28, lineHeight: '33.6px', fontWeight: 500 },
  lead: { fontSize: 18, lineHeight: '25.2px', fontWeight: 400 },
  body: { fontSize: 16, lineHeight: '22.4px', fontWeight: 400 },
  button: { fontSize: 16, lineHeight: '22.4px', fontWeight: 500 },
  small: { fontSize: 14, lineHeight: '19.6px', fontWeight: 400 },
  label: { fontSize: 16, lineHeight: '16px', fontWeight: 500 },
  micro: { fontSize: 12, lineHeight: '16.8px', fontWeight: 500 },
  eyebrow: { fontSize: 12, lineHeight: '12px', fontWeight: 600, letterSpacing: '1px' },
} as const
