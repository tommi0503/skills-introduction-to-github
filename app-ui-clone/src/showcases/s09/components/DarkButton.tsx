import type { ReactNode } from 'react'
import { cn } from '../../../ui'
import { theme } from '../theme'

/** Primary black button. */
export function DarkButton({ children, className }: { children: ReactNode; className?: string }) {
  return (
    <div
      className={cn('flex h-full w-full items-center rounded-[10px] font-poppins text-[13px] font-semibold text-white', className)}
      style={{ background: theme.dark }}
    >
      {children}
    </div>
  )
}
