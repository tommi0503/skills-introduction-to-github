import type { ReactNode } from 'react'
import { cn } from '../../../ui'
import { theme } from '../theme'

/** Grey assistant bubble. */
export function MessageBubble({ children, className }: { children: ReactNode; className?: string }) {
  return (
    <div
      className={cn('w-[314px] rounded-[16px] px-[14px] py-[10px] text-[16px] leading-[22px] tracking-[-0.15px] text-[#111]', className)}
      style={{ background: theme.bubble }}
    >
      {children}
    </div>
  )
}
