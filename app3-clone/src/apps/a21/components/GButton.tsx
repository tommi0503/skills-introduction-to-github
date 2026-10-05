import type { ReactNode } from 'react'
import { cn } from '../../../ui'
import { theme } from '../theme'

/** Google flat blue raised button. */
export function GButton({ children, className }: { children: ReactNode; className?: string }) {
  return (
    <div
      className={cn('absolute flex items-center justify-center rounded-[3px] text-[14px] font-medium text-white', className)}
      style={{ background: theme.blue, boxShadow: '0 1px 3px rgba(0,0,0,.25)' }}
    >
      {children}
    </div>
  )
}
