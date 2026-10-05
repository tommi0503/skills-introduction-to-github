import type { CSSProperties, ReactNode } from 'react'
import { ArrowRight } from 'lucide-react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export interface MonoButtonProps {
  children: ReactNode
  variant?: 'light' | 'dark' | 'ghost'
  arrow?: boolean
  className?: string
  style?: CSSProperties
}

const variants = {
  light: 'bg-white text-black font-medium',
  dark: 'bg-[#1c1c1c] text-white font-medium',
  ghost: 'text-white',
} as const

/** Uppercase monospace button / nav pill. */
export function MonoButton({ children, variant = 'light', arrow, className, style }: MonoButtonProps) {
  return (
    <span
      className={cn(
        theme.fonts.mono,
        'inline-flex items-center justify-center gap-[5px] rounded-[6px] text-[12px] uppercase tracking-[0.25px] whitespace-nowrap',
        variants[variant],
        className,
      )}
      style={style}
    >
      {children}
      {arrow && <ArrowRight size={13} strokeWidth={1.75} />}
    </span>
  )
}
