import type { ReactNode } from 'react'
import { cn } from '../../../ui'
import { theme } from '../theme'

/** Condensed terracotta price. */
export function Price({ children, className }: { children: ReactNode; className?: string }) {
  return (
    <div className={cn('font-condensed font-normal tracking-[-0.03em]', className)} style={{ color: theme.price }}>
      {children}
    </div>
  )
}
