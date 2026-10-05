/** Design tokens of the "2056 도서관 책축제" tri-fold (outside = 17, inside = 18). */
export interface FestivalPalette {
  cream: string
  periwinkle: string
  /** lighter periwinkle tint used for boxes on the inside spread */
  periwinkleSoft: string
  yellow: string
  card: string
  cardBorder: string
  accent: string
  /** greyish accent for secondary list text */
  accentMuted: string
  ink: string
  inkSoft: string
  inkMuted: string
  rule: string
  onPeriwinkle: string
  onPeriwinkleSoft: string
}

/** Outside of the brochure as printed (warmer cream, stronger periwinkle). */
export const outsidePalette: FestivalPalette = {
  cream: '#f5f2d0',
  periwinkle: '#93a8de',
  periwinkleSoft: '#9db0e3',
  yellow: '#eeebb8',
  card: '#f4f4f4',
  cardBorder: '#9fb2e2',
  accent: '#8199da',
  accentMuted: '#97a6c8',
  ink: '#4a4a4a',
  inkSoft: '#6b6b6b',
  inkMuted: '#8a8a7c',
  rule: '#d9d9d9',
  onPeriwinkle: '#ffffff',
  onPeriwinkleSoft: '#dfe6f5',
}

/** Inside spread (paler cream, soft periwinkle tint). */
export const insidePalette: FestivalPalette = {
  cream: '#f4f3df',
  periwinkle: '#bccaeb',
  periwinkleSoft: '#b8c5e7',
  yellow: '#eeebb8',
  card: '#f2f2f2',
  cardBorder: '#a9b8e2',
  accent: '#8ba3da',
  accentMuted: '#97a6c8',
  ink: '#4b4f5a',
  inkSoft: '#6e6e6e',
  inkMuted: '#8a8a8a',
  rule: '#d2d4d6',
  onPeriwinkle: '#ffffff',
  onPeriwinkleSoft: '#f2f4f8',
}

export const fonts = {
  body: 'font-gothic-a1',
  display: 'font-blackhan',
} as const
