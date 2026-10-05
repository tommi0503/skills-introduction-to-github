import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'

export interface PillProps {
  children: ReactNode
  variant?: 'solid' | 'outline' | 'plain'
  className?: string
  style?: CSSProperties
}

const variants = {
  solid: 'bg-[#e9ebdf] text-[#151515]',
  outline: 'border border-[#e9ebdf]/80 text-[#e9ebdf]',
  plain: 'text-[#e9ebdf]',
} as const

/** Rounded 40px nav/CTA pill. */
export function Pill({ children, variant = 'solid', className, style }: PillProps) {
  return (
    <span
      className={cn('inline-flex h-[40px] items-center justify-center rounded-full font-geist text-[14px] whitespace-nowrap', variants[variant], className)}
      style={style}
    >
      {children}
    </span>
  )
}
