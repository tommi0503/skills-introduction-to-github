/** Every slide is exactly SLIDE size (16:9), flat and upright. Boards lay slides out on a fixed grid. */
export const SLIDE = { width: 1280, height: 720 } as const
export const BOARD = { gap: 40, padding: 40, columns: 2, background: '#d4d4d8' } as const
export function boardSize(count: number) {
  const cols = Math.min(BOARD.columns, count)
  const rows = Math.ceil(count / BOARD.columns)
  return {
    width: BOARD.padding * 2 + cols * SLIDE.width + (cols - 1) * BOARD.gap,
    height: BOARD.padding * 2 + rows * SLIDE.height + (rows - 1) * BOARD.gap,
  }
}
