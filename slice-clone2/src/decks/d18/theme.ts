/** d18 — folder-tab SWOT deck tokens. */
export const t = {
  navy: '#1c364b',
  red: '#b0322a',
  pink: '#f5a9a3',
  brown: '#bb7c4f',
  beige: '#ebd6c0',
  teal: '#b4d1d0',
  orange: '#f5ba71',
  cream: '#fff8eb',
  text: '#2a2a2a',
  display: 'font-bagel',
  body: 'font-nanumgothic',
  /** Panel right edge (tab strip lies beyond it). */
  edge: 1236,
  cx: 618,
} as const
export type Chapter = 'pink' | 'brown' | 'beige' | 'teal' | 'orange'
export const tabOrder: Chapter[] = ['pink', 'brown', 'beige', 'teal', 'orange']
