/** Design tokens for the "Scan" document-scanner app (showcase 07). */
export const theme = {
  stageBg: 'radial-gradient(ellipse 75% 70% at 50% 50%, #222a3f 0%, #212739 55%, #1c202d 100%)',
  paper: '#f9f8f4',
  canvas: '#f2efea',
  ink: '#141414',
  muted: '#9a9893',
  hairline: '#e7e4dd',
  accent: '#2d5ff5',
  danger: '#d9534b',
  glass: 'rgba(22,17,13,0.92)',
} as const

/** Shared device geometry (stage px). */
export const device = { width: 202, height: 440, logicalWidth: 375, radius: 16 } as const
