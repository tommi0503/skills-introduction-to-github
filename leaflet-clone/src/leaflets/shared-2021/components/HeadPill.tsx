import type { ReactNode } from 'react'
import { cn } from '../../../ui'
import { DISPLAY } from '../theme'

export interface HeadPillProps {
  /** Variant: 'solid' = dark blue pill with light text, 'soft' = pale blue pill with navy text. */
  variant?: 'solid' | 'soft'
  className?: string
  children: ReactNode
}

const VARIANTS = {
  solid: 'bg-[#4677ae] text-[#f2f6fb]',
  soft: 'bg-[#d5e3f1] text-[#2f4f78]',
} as const

/** Capsule section header (신청하는 방법 / 교육과정 …). Size/padding injected through className. */
export function HeadPill({ variant = 'solid', className, children }: HeadPillProps) {
  return (
    <span className={cn('inline-flex items-center justify-center whitespace-nowrap rounded-full leading-none tracking-[0.03em]', DISPLAY, VARIANTS[variant], className)}>
      {children}
    </span>
  )
}
