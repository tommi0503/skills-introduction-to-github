import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export interface PillProps {
  children: ReactNode
  className?: string
}

/** Fully rounded outline button used across the Cloudflare nav and pricing. */
export function Pill({ children, className }: PillProps) {
  return (
    <span
      className={cn(
        'inline-flex h-[38px] shrink-0 items-center whitespace-nowrap tracking-[-0.3px] justify-center gap-2 rounded-full border border-[#ececec] px-[13px] text-[16px] font-medium text-[#262626]',
        className,
      )}
    >
      {children}
    </span>
  )
}

/** Small bordered tag (pricing feature chips). */
export function Chip({ children }: { children: ReactNode }) {
  return (
    <span className="inline-flex h-[26px] items-center whitespace-nowrap rounded-[4px] border border-[#ececec] px-[10px] text-[14px] tracking-[-0.14px] text-[#262626]/80">
      {children}
    </span>
  )
}
