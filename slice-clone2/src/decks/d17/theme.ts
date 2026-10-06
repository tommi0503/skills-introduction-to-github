/** d17 — sky-blue simple business manual tokens. */
export const t = {
  bg: '#93b5c5',
  ink: '#224b6b',
  text: '#3a4651',
  grey: '#efeef1',
  blue: '#dce5ef',
  mid: '#94aec1',
  strip: '#dee6ec',
  light: '#9cb9cb',
  faint: '#c9d5de',
  font: 'font-notosans',
  /** Inter for Latin digits, Noto Sans KR for Hangul. */
  family: "'Inter Variable', 'Noto Sans KR', sans-serif",
  /** Hangul width correction vs. reference face. */
  fs: 1.05,
  panel: { x: 40, y: 40, w: 1200, h: 630, border: 2 },
  rule: { y: 643, x: 57, w: 1166 },
} as const
export type Tone = 'grey' | 'blue' | 'mid' | 'dark'
export const tone = (k: Tone) => ({ grey: t.grey, blue: t.blue, mid: t.mid, dark: t.ink })[k]
