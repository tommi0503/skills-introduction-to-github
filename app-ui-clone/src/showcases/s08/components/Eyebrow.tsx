import type { ReactNode } from 'react'
import { cn } from '../../../ui'
import { theme } from '../theme'

/** Small tracked uppercase label ("VINTAGE · BERLIN"). */
export function Eyebrow({ children, className, color = theme.muted }: { children: ReactNode; className?: string; color?: string }) {
  return (
    <div className={cn('font-dm text-[8.8px] leading-[12px] font-normal tracking-[0.2em] whitespace-nowrap', className)} style={{ color }}>
      {children}
    </div>
  )
}
