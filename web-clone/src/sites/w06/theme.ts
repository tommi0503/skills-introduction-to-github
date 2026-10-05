/** Design tokens for the x.ai clone. */
export const theme = {
  font: 'font-geist',
  mono: 'font-plexmono',
  page: '#ffffff',
  ink: '#0a0a0a',
  muted: 'rgba(10,10,10,0.6)',
  faint: 'rgba(10,10,10,0.3)',
  soft: '#f2f1ef',
  card: '#f9f8f6',
  rule: '#e6e6e6',
  footerRule: '#d5d9e2',
  darkCard: '#151515',
  orange: 'rgb(255,99,8)',
  /** Left edge / width of the main content column. */
  gutter: 104,
  content: 1232,
} as const

/** Syntax colours of the code sample (GitHub light). */
export const syntax = {
  kw: 'rgb(215,58,73)',
  id: 'rgb(36,41,46)',
  arg: 'rgb(227,98,9)',
  str: 'rgb(3,47,98)',
  fn: 'rgb(0,92,197)',
} as const

export type SyntaxToken = keyof typeof syntax
