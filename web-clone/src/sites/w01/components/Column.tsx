import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export interface ColumnProps {
  height: number
  background?: string
  borderBottom?: boolean
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/** One section band: the 1278px inner column between the page's vertical rules. */
export function Column({ height, background, borderBottom, className, style, children }: ColumnProps) {
  return (
    <section
      className="relative w-full"
      style={{ height, borderBottom: borderBottom ? `1px solid ${theme.rule}` : undefined }}
    >
      <div
        className={cn('absolute inset-y-0', className)}
        style={{ left: theme.column.left + 1, width: theme.column.width - 2, background, ...style }}
      >
        {children}
      </div>
    </section>
  )
}
