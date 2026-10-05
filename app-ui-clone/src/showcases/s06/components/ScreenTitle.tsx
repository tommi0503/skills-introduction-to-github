import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export interface ScreenTitleProps {
  title: string
  trailing?: ReactNode
  className?: string
}

/** Large page title with trailing actions on the same row. */
export function ScreenTitle({ title, trailing, className }: ScreenTitleProps) {
  return (
    <div className={cn('flex items-center justify-between', className)}>
      <h1 className="text-[22px] font-semibold tracking-[-0.4px] text-[#111]">{title}</h1>
      <div className="flex items-center gap-[10px]">{trailing}</div>
    </div>
  )
}
