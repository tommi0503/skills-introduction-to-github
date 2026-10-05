import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'

/** Modal card sheet presented over a dimmed backdrop (starts below the status bar). */
export function Sheet({ children, className, style, top = 59 }: { children: ReactNode; className?: string; style?: CSSProperties; top?: number }) {
  return (
    <div className={cn('absolute inset-x-0 bottom-0 overflow-hidden rounded-t-[24px]', className)} style={{ top, ...style }}>
      {children}
    </div>
  )
}
