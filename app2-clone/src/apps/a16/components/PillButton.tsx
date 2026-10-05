import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export type PillVariant = 'dark' | 'soft' | 'outline'

const variants: Record<PillVariant, string> = {
  dark: 'bg-[#1d1d1f] text-white',
  soft: 'bg-[#efeff1] text-[#111]',
  outline: 'bg-white text-[#111] shadow-[0_0_0_1px_#f3f3f4]',
}

export interface PillButtonProps {
  variant: PillVariant
  leading?: ReactNode
  children: ReactNode
  className?: string
}

/** Full-width capsule button used across onboarding & paywall. */
export function PillButton({ variant, leading, children, className }: PillButtonProps) {
  return (
    <button
      type="button"
      className={cn('flex w-full items-center justify-center gap-[9px] rounded-full text-[16px] font-medium', variants[variant], className)}
    >
      {leading}
      {children}
    </button>
  )
}
