import type { ReactNode } from 'react'
import type { DayCell } from '../data'

export interface MonthGridProps {
  cells: DayCell[]
  /** Column centres. */
  colX: number[]
  /** Row centres. */
  rowY: number[]
  renderCell: (cell: DayCell, index: number) => ReactNode
}

/** Positions month cells on explicit column/row centres; the cell look is injected. */
export function MonthGrid({ cells, colX, rowY, renderCell }: MonthGridProps) {
  return (
    <>
      {cells.map((c, i) => (
        <div
          key={i}
          className="absolute flex -translate-x-1/2 -translate-y-1/2 items-center justify-center"
          style={{ left: colX[i % 7], top: rowY[Math.floor(i / 7)] }}
        >
          {renderCell(c, i)}
        </div>
      ))}
    </>
  )
}

export const steps = (start: number, step: number, n: number) => Array.from({ length: n }, (_, i) => start + i * step)
