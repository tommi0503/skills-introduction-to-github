import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export function PillButton({ children, className, background = '#fff' }: { children: ReactNode; className?: string; background?: string }) {
  return (
    <button
      type="button"
      className={cn('flex h-[52px] w-full items-center justify-center rounded-full text-[14px] font-medium text-black', className)}
      style={{ background }}
    >
      {children}
    </button>
  )
}
