import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export interface PillProps {
  active?: boolean
  className?: string
  children: ReactNode
}

/** Outlined chip; solid near-black when active. */
export function Pill({ active, className, children }: PillProps) {
  return (
    <span
      className={cn(
        'flex shrink-0 items-center justify-center rounded-full border',
        active ? 'border-[#1c1c1e] bg-[#1c1c1e] text-white' : 'border-[#9a9aa0] text-[#3a3a3c]',
        className,
      )}
    >
      {children}
    </span>
  )
}
