/** Design tokens shared by the Naver Pay showcases (19–22). Values sampled from the references. */
export const naver = {
  stageBg: '#16171b',
  /** Phone geometry in stage px (all references share the same capture size). */
  phoneWidth: 378,
  phoneHeight: 819,
  logicalWidth: 390,
  screenRadius: 24,

  green: '#03c75a',
  greenButton: '#5bdb64',
  greenDeep: '#43a94e',
  greenText: '#00a854',
  greenSoftBg: '#e7f6ea',

  text: '#1d1d1d',
  textStrong: '#111111',
  textSub: '#666666',
  textMuted: '#9a9a9a',
  textFaint: '#c4c4c4',
  link: '#2f7de1',

  line: '#ececec',
  lineStrong: '#dddddd',
  surface: '#f5f6f8',
  toolbarBg: '#f8f8f8',
} as const

export type NaverTheme = typeof naver
