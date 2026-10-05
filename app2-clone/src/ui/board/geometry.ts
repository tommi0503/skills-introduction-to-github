/**
 * Single source of truth for screen geometry: every screen of every app is
 * exactly SCREEN.width × SCREEN.height (iPhone logical points), upright, never tilted.
 */
export const SCREEN = { width: 390, height: 844, radius: 44 } as const
export const BOARD = { gap: 40, padding: 40, background: '#111111' } as const

export function boardWidth(screens: number): number {
  return BOARD.padding * 2 + screens * SCREEN.width + (screens - 1) * BOARD.gap
}
export const boardHeight = BOARD.padding * 2 + SCREEN.height
