import { Children, type ReactNode } from 'react'
import { BOARD, boardHeight, boardWidth } from './geometry'

export interface ScreenBoardProps {
  /** One <AppScreen> per child, laid out left→right with equal gaps. */
  children: ReactNode
  background?: string
}

/** The render canvas: equal-size screens side by side on a flat background. */
export function ScreenBoard({ children, background = BOARD.background }: ScreenBoardProps) {
  const n = Children.count(children)
  return (
    <div
      data-stage
      className="flex items-start"
      style={{ width: boardWidth(n), height: boardHeight, padding: BOARD.padding, gap: BOARD.gap, background }}
    >
      {children}
    </div>
  )
}
