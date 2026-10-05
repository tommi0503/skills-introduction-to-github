/** Design tokens for the Giga clone. */
export const theme = {
  font: {
    sans: 'font-geist',
    mono: 'font-plexmono',
    display: 'font-inter',
  },
  /** Stand-in for Geist Pixel Line (thin monospace display face). */
  pixel: { fontFamily: "'IBM Plex Mono', monospace", fontWeight: 200 } as const,
  color: {
    page: '#000000',
    bar: '#464443',
    nav: '#403b33',
    heroArt: '#6f6a66',
    orange: '#f26c25',
    orangeDeep: '#eb641d',
    cream: '#f2f1ec',
    ink: '#1f1d1b',
    text: 'rgb(232, 237, 239)',
    textDim: 'rgba(232, 237, 239, 0.74)',
    panelDark: '#050506',
    panelLight: '#d8d3ce',
    panelLine: '#c4c0bc',
    card: 'rgb(39, 39, 41)',
    field: '#0d0e0f',
    logo: '#3a3a3a',
    imageDark: '#4a4a4c',
    chatBg: '#111214',
    chatFoot: '#2c2c2e',
    rule: '#1d1d1d',
  },
} as const
