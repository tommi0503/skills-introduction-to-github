import type { ReactNode } from 'react'
import { cn } from '../../../ui'
import { DISPLAY } from '../theme'

export interface SectionTitleProps {
  top: number
  centerX?: number
  className?: string
  children: ReactNode
}

/** Centred rounded heading (체험 프로그램 / 신청 방법 …); colour and size injected. */
export function SectionTitle({ top, centerX = 240, className, children }: SectionTitleProps) {
  return (
    <div className="absolute flex justify-center" style={{ top, left: centerX - 240, width: 480 }}>
      <span className={cn(DISPLAY, 'whitespace-nowrap leading-none', className)}>{children}</span>
    </div>
  )
}
