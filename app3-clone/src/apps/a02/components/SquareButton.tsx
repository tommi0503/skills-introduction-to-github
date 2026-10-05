import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export interface SquareButtonProps {
  size?: number
  radius?: number
  className?: string
  children: ReactNode
}

/** Rounded-square outlined button used for back/close/edit. */
export function SquareButton({ size = 53, radius = 14, className, children }: SquareButtonProps) {
  return (
    <span
      className={cn('flex shrink-0 items-center justify-center border border-[#ecebe8]', className)}
      style={{ width: size, height: size, borderRadius: radius }}
    >
      {children}
    </span>
  )
}
