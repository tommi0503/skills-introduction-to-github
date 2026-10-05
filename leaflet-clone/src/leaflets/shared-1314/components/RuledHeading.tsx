import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export interface RuledHeadingProps {
  /** Heading box; the rule runs along its bottom edge to the panel's right edge. */
  x: number
  y: number
  width: number
  ruleY: number
  ruleThickness?: number
  ruleColor: string
  className?: string
  children: ReactNode
}

/** Right-aligned section title with a rule running to the panel edge (참가 안내 / 부스 소개). */
export function RuledHeading({ x, y, width, ruleY, ruleThickness = 2, ruleColor, className, children }: RuledHeadingProps) {
  return (
    <>
      <h2 className={cn('absolute m-0 whitespace-nowrap', className)} style={{ left: x, top: y, width }}>
        {children}
      </h2>
      <div className="absolute right-0" style={{ left: x, top: ruleY, height: ruleThickness, background: ruleColor }} />
    </>
  )
}
