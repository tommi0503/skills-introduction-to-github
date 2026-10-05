/** Habit-streak app tokens (logical iOS points, 375pt wide). */
export const theme = {
  stage: '#f1eae0',
  ink: '#151518',
  muted: '#8f8f94',
  soft: '#f6f6f6',
  button: '#18171c',
  empty: '#e6e6e9',
} as const

export const screen = { width: 238, height: 516, logicalWidth: 375 } as const

/** Four-corner mesh: colours bleed in from each corner over a white centre. */
export interface MeshGradient {
  tl: string
  tr: string
  bl: string
  br: string
  base?: string
}

export function meshBackground({ tl, tr, bl, br, base = '#fbf6f4' }: MeshGradient): string {
  return [
    `radial-gradient(ellipse 75% 70% at 0% 0%, ${tl}, transparent)`,
    `radial-gradient(ellipse 75% 70% at 100% 0%, ${tr}, transparent)`,
    `radial-gradient(ellipse 75% 70% at 0% 100%, ${bl}, transparent)`,
    `radial-gradient(ellipse 75% 70% at 100% 100%, ${br}, transparent)`,
    base,
  ].join(', ')
}

export const gradients = {
  streak: { tl: '#fdd3bd', tr: '#fcc6db', bl: '#fbeab0', br: '#d4c7fc' },
  mindful: { tl: '#fdd6bf', tr: '#d2c7f6', bl: '#fcc4d8', br: '#cdeedc', base: '#f6eeec' },
  deepWork: { tl: '#d5c9fb', tr: '#c3ddff', bl: '#fdf0ea', br: '#ffdcc8', base: '#f1eaf1' },
} satisfies Record<string, MeshGradient>
