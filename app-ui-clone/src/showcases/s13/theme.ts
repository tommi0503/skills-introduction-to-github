/** Colour + surface tokens for the "Branja" barber booking app. */
export const theme = {
  ink: '#0b0b0b',
  muted: '#8f8e8a',
  stageTone: '#c3c3bc',
  card: '#ffffff',
  glass: 'rgba(255,255,255,0.42)',
  glassBorder: 'rgba(255,255,255,0.7)',
  cellBlocked: 'rgba(70,60,45,0.075)',
  cellHatchA: 'rgba(70,60,45,0.08)',
  cellHatchB: 'rgba(255,255,255,0.10)',
  fieldBg: 'rgba(60,55,45,0.13)',
  doneChip: '#e6fbac',
  activeChip: '#a9d1f7',
  /** Frosted screen surface (light at top, darker band in the middle, light bottom). */
  screenHome:
    'linear-gradient(180deg,#f5f4f2 0%,#f3f2f0 5%,#e9e8e5 9%,#d6d5d0 14%,#cdccc7 20%,#c0bdb5 34%,#bbb8b0 42%,#c4c4bd 47%,#dcdcd6 52%,#e2e2dc 56%,#dededa 100%)',
  screenBooking:
    'linear-gradient(180deg,#f5f4f2 0%,#f3f2f0 4%,#e9e8e4 9%,#d8d7d2 14%,#cfcecb 19%,#d6d6d1 26%,#d3d2cb 35%,#c9c7bf 44%,#bdbbb3 52%,#bebdb5 64%,#cfd0ca 72%,#e7e6e3 82%,#f2f1f0 100%)',
  /** Keeps the white status bar legible over the photo placeholder. */
  splashTopScrim: 'linear-gradient(180deg,rgba(13,18,21,0.55) 0%,rgba(13,18,21,0) 100%)',
  splashScrim:
    'linear-gradient(180deg,rgba(18,28,40,0) 0%,rgba(40,58,80,0.55) 22%,rgba(24,35,48,0.92) 45%,#121a20 70%,#0d1215 100%)',
} as const
