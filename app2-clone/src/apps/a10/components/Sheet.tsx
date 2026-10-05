import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'

export interface SheetProps {
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/** White card that floats above the map / globe. Position & radius injected by the caller. */
export function Sheet({ className, style, children }: SheetProps) {
  return (
    <div className={cn('absolute overflow-hidden bg-white', className)} style={style}>
      {children}
    </div>
  )
}
