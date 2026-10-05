import type { ReactNode } from 'react'
import { cn } from '../../../ui'

/** Full-width capsule button; `variant` swaps black primary for grey secondary. */
export function CapsuleButton({
  children,
  top,
  variant = 'primary',
  className,
}: {
  children: ReactNode
  top: number
  variant?: 'primary' | 'secondary'
  className?: string
}) {
  return (
    <div
      className={cn(
        'absolute flex items-center justify-center rounded-full text-[16px]',
        variant === 'primary' ? 'bg-black text-white' : 'bg-[#efefef] text-black',
        className,
      )}
      style={{ top }}
    >
      {children}
    </div>
  )
}
