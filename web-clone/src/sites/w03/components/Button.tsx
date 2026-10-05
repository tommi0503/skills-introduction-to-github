import type { ReactNode } from 'react'
import { cn } from '../../../ui'

type Variant = 'dark' | 'light' | 'outline'

const variants: Record<Variant, string> = {
  dark: 'bg-[#0f0e0d] text-[#fafaf9]',
  light: 'bg-[#fafaf9] text-[#0f0e0d]',
  outline: 'border border-[#fafaf9]/80 text-[#fafaf9]',
}

export interface ButtonProps {
  children: ReactNode
  variant?: Variant
  className?: string
}

/** Rectangular Harvey CTA. Size is controlled by className. */
export function Button({ children, variant = 'dark', className }: ButtonProps) {
  return (
    <a className={cn('inline-flex items-center justify-center rounded-[4px] font-medium', variants[variant], className)}>
      {children}
    </a>
  )
}
