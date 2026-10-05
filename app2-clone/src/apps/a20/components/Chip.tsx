import type { ReactNode } from 'react'
import { cn } from '../../../ui'

/** Rounded action chip (icon + label). */
export function Chip({ children, className }: { children: ReactNode; className?: string }) {
  return <span className={cn('inline-flex items-center gap-[6px] rounded-full', className)}>{children}</span>
}
