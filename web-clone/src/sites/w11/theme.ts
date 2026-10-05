/** Design tokens for the Origin clone. */
export const theme = {
  colors: {
    page: '#050505',
    heading: '#fafafa',
    white: '#ffffff',
    muted: 'rgba(255,255,255,0.6)',
    faint: 'rgba(255,255,255,0.32)',
    panel: '#0e0e0e',
    card: '#0e0e0e',
    cardBorder: 'rgba(255,255,255,0.09)',
    control: '#181818',
    pill: '#232424',
    pillBack1: '#141515',
    pillBack2: '#0d0e0e',
    green: '#10b06a',
  },
  /** Flat stand-in tones for imagery (one colour each). */
  tones: {
    sky: '#1c6799',
    phone: '#3a7099',
    darkMedia: '#1c1c1d',
    logo: '#2a2a2b',
    award: '#23282c',
    glow: '#3b4e5c',
    canvas: '#070707',
    photo: '#886621',
    mock: '#161717',
  },
  /** Extra tracking (em) applied to the serif stand-in so widths match Lyon Display. */
  serifTracking: -0.017,
  fonts: {
    serif: 'font-times',
    mono: 'font-plexmono',
    sans: 'font-inter',
  },
} as const
