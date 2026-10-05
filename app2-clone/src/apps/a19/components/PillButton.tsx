import type { ReactNode } from 'react'
import { cn } from '../../../ui'

/** Full-round black/white CTA. */
export function PillButton({ children, className }: { children: ReactNode; className?: string }) {
  return (
    <div className={cn('flex items-center justify-center gap-[8px] rounded-full bg-black text-[15px] font-medium text-white', className)}>
      {children}
    </div>
  )
}
