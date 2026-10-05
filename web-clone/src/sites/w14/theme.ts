/** Design tokens for the GitBook clone (w14). */
export const colors = {
  page: '#ffffff',
  ink: '#1c1917',
  body: '#57534d',
  muted: '#79716b',
  mockMuted: '#786b67',
  orange: '#fe551b',
  orangeSoft: 'rgba(254, 85, 27, 0.1)',
  orangeTint: '#fff6f3',
  border: '#efeeed',
  subtle: '#fafaf9',
  chip: '#f5f5f5',
  navButton: '#f4f3f2',
  frame: '#f2f1f1',
  aiChip: '#b1b1b1',
  fadedText: 'rgba(121, 113, 107, 0.8)',
  dots: ['#f0c7c4', '#f3e1bf', '#c6e3c1'],
} as const

/** Font utilities (General Sans → Figtree, Geist Mono → IBM Plex Mono). */
export const fonts = {
  sans: 'font-figtree',
  ui: 'font-inter',
  mono: 'font-plexmono',
} as const

export const shadows = {
  frame: '0 4px 14px rgba(0,0,0,0.06)',
  tile: '0 1px 3px rgba(0,0,0,0.10)',
  popover: '0 6px 24px rgba(0,0,0,0.10)',
} as const
