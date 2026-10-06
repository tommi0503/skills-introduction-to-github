import { BOARD, boardSize } from './geometry'
import type { DeckDefinition } from './deck'

/** Renders every slide of a deck on a flat grid (the render target). */
export function Board({ deck }: { deck: DeckDefinition }) {
  const { width, height } = boardSize(deck.slides.length)
  return (
    <div
      data-stage
      className="grid content-start"
      style={{
        width,
        height,
        padding: BOARD.padding,
        gap: BOARD.gap,
        background: BOARD.background,
        gridTemplateColumns: `repeat(${Math.min(BOARD.columns, deck.slides.length)}, max-content)`,
      }}
    >
      {deck.slides.map((S, i) => (
        <S key={i} />
      ))}
    </div>
  )
}
