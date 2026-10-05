/** Design tokens for the Cosmos clone. */
export const theme = {
  font: 'font-dm',
  color: {
    canvas: '#f7f5f3',
    page: '#ffffff',
    ink: '#0e0e0e',
    muted: '#6b6866',
    navText: '#6b6866',
    hint: '#9a9795',
    searchBg: '#fcfbfa',
    searchBorder: '#e9e6e3',
    panel: '#a4a38f',
    redCard: '#d1543e',
    tanCard: '#e8c8a0',
    chip: 'rgba(120, 30, 20, 0.55)',
    chipDot: '#bc361b',
    overlayPill: 'rgba(255,255,255,0.25)',
    searchPill: 'rgba(40, 40, 30, 0.22)',
  },
  /** Width of the scrollable content column (page minus the 10px scrollbar gutter). */
  contentWidth: 1430,
  cardRadius: 10,
} as const

export type Theme = typeof theme
