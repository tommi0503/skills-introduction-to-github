import type { ReactNode } from 'react'
import { cn } from '../../../ui'
import type { CtaLink } from '../data'

const variants: Record<CtaLink['variant'], string> = {
  primary: 'bg-[#309d4b] text-[#f9f9f8] border border-[#309d4b]',
  outline: 'bg-[#fefefe] text-[#1e1c1a] border border-[#e4e3db]',
  ghost: 'text-[#1e1c1a] border border-transparent',
}

const sizes = {
  md: 'h-10 px-[17px] text-[14px] leading-5 font-medium',
  sm: 'h-8 px-[11px] text-[13px] leading-[18px]',
} as const

export interface ButtonProps {
  variant: CtaLink['variant']
  size?: keyof typeof sizes
  className?: string
  children: ReactNode
}

/** Rounded rectangular button used across the page. */
export function Button({ variant, size = 'md', className, children }: ButtonProps) {
  return (
    <span
      className={cn(
        'inline-flex shrink-0 items-center justify-center rounded-[8px] whitespace-nowrap',
        sizes[size],
        variant === 'ghost' ? '!px-0' : '',
        variants[variant],
        className,
      )}
    >
      {children}
    </span>
  )
}
