import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export interface BlockButtonProps {
  children: ReactNode
  leading?: ReactNode
  variant?: 'primary' | 'secondary'
  className?: string
}

/** Full-width Uber button (black primary / grey secondary). */
export function BlockButton({ children, leading, variant = 'primary', className }: BlockButtonProps) {
  return (
    <button
      type="button"
      className={cn(
        'flex w-full items-center justify-center gap-[9px] rounded-[8px] text-[15.5px] font-medium',
        variant === 'primary' ? 'bg-black text-white' : 'bg-[#eeeeee] font-normal text-[#111]',
        className,
      )}
    >
      {leading}
      {children}
    </button>
  )
}
