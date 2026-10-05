/** Design tokens for leaflet 03 (green flea market). */
export const theme = {
  green: '#099a55',
  cream: '#f8f5f0',
  yellow: '#fdd20e',
  ink: '#1b1b1b',
  clip: '#c0504d',
} as const

/** Irregular "torn paper" / wavy blob silhouettes approximated with border-radius. */
export const blobs = {
  note: '14px 22px 18px 26px / 20px 14px 28px 18px',
  /** Bean-shaped map outline in a 316×254 box. */
  mapPath:
    "path('M 32 44 C 62 2 128 6 152 48 C 176 78 204 26 252 14 C 300 4 324 56 312 130 C 300 204 262 254 160 254 C 70 254 18 228 6 160 C -4 110 4 74 32 44 Z')",
} as const
