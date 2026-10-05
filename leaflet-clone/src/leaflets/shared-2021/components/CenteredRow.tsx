import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export interface CenteredRowProps {
  top: number
  /** Horizontal centre in panel px (default panel centre). */
  centerX?: number
  className?: string
  children: ReactNode
}

/** Places its content horizontally centred on centerX at a given top. */
export function CenteredRow({ top, centerX = 240, className, children }: CenteredRowProps) {
  return (
    <div className={cn('absolute flex justify-center', className)} style={{ top, left: centerX - 240, width: 480 }}>
      {children}
    </div>
  )
}
