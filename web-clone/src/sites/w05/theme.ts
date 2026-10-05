/** Design tokens for the Monologue clone. */
export const theme = {
  mono: 'font-plexmono',
  serif: 'font-playfair',
  wordmark: 'font-instrument-serif',
  page: '#121212',
  frame: '#282828',
  panel: '#363535',
  feature: 'linear-gradient(to bottom, #353434 0px, #2e2e2e 400px, #282828 700px, #262626 1600px, #242424 2214px)',
  ink: '#f2f0ed',
  text82: 'rgba(255,255,255,0.82)',
  text68: 'rgba(255,255,255,0.68)',
  text62: 'rgba(255,255,255,0.62)',
  text48: 'rgba(255,255,255,0.48)',
  etchDark: '#101010',
  etchLight: '#535353',
  cyan: 'rgb(25,208,232)',
  cream: '#fefdfb',
  buttonInk: '#282828',
  /** Dark flat tone for media placeholders on this dark page. */
  media: '#4a4a4a',
  /** Frame geometry. */
  frameInset: 16,
  columnLeft: 120,
  columnRight: 1320,
} as const

export const accents = {
  dictation: { text: 'rgb(239,138,128)', tile: '#d9473c' },
  notes: { text: 'rgb(110,216,186)', tile: '#20a77f' },
  meetings: { text: 'rgb(220,187,21)', tile: '#c9a20d' },
  api: { text: '#ffffff', tile: '#3f6fd8' },
} as const

export type Accent = keyof typeof accents
