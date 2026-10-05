import type { ReactNode } from 'react'
import { cn } from '../../../ui'

/** Soft white floating control used by the in-app browser chrome. */
export function FloatingCircle({ children, className }: { children: ReactNode; className?: string }) {
  return (
    <div
      className={cn('flex items-center justify-center rounded-full bg-white', className)}
      style={{ boxShadow: '0 2px 14px rgba(0,0,0,0.07)' }}
    >
      {children}
    </div>
  )
}
