/** Design tokens for the "bond" app screens (reference 25). */
export const bond = {
  stage: '#141414',
  screen: '#f6f6f6',
  splash: '#f0f0f0',
  ink: '#0d0d0d',
  text: '#1c1c1c',
  muted: '#8c8c8c',
  faint: '#b5b5b5',
  surface: '#ffffff',
  card: '#fbfbfb',
  chip: '#ececec',
  keyboard: '#e0e1e3',
  softShadow: '0 4px 14px rgba(0,0,0,0.06)',
} as const

/** Device geometry shared by every phone in the stage (stage px). */
export const device = {
  width: 270,
  height: 582,
  logicalWidth: 393,
  screenRadius: 34,
} as const
