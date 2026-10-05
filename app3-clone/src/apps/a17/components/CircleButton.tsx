import type { LucideIcon } from 'lucide-react'
import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export interface CircleButtonProps {
  icon?: LucideIcon
  size?: number
  iconSize?: number
  strokeWidth?: number
  filled?: boolean
  /** Solid glyph with white inner strokes (e.g. a black clock face). */
  inverse?: boolean
  /** Floating white button with soft shadow vs. flat tinted circle. */
  variant?: 'floating' | 'soft' | 'glass'
  className?: string
  children?: ReactNode
}

export function CircleButton({
  icon: Icon,
  size = 42,
  iconSize = 20,
  strokeWidth = 2,
  filled,
  inverse,
  variant = 'soft',
  className,
  children,
}: CircleButtonProps) {
  const look = {
    floating: 'bg-white text-black shadow-[0_2px_12px_rgba(0,0,0,0.10)]',
    soft: 'bg-[#f0f0f0] text-black',
    glass: 'bg-white/15 text-white/80',
  }[variant]
  return (
    <div className={cn(className?.includes('absolute') ? '' : 'relative', 'flex shrink-0 items-center justify-center rounded-full', look, className)} style={{ width: size, height: size }}>
      {Icon && <Icon size={iconSize} strokeWidth={strokeWidth} fill={filled || inverse ? 'currentColor' : 'none'} stroke={inverse ? '#fff' : 'currentColor'} />}
      {children}
    </div>
  )
}
