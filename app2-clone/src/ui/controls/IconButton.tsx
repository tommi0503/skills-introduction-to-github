import type { ButtonHTMLAttributes } from 'react'
import type { LucideIcon } from 'lucide-react'
import { cn } from '../core/cn'

export interface IconButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  icon: LucideIcon
  size?: number
  iconSize?: number
  strokeWidth?: number
  /** Tailwind classes for bg/border/shape. Defaults to a plain circle. */
  className?: string
  iconClassName?: string
}

/** Round/square button that hosts a single lucide icon. */
export function IconButton({
  icon: Icon,
  size = 40,
  iconSize = 20,
  strokeWidth = 1.8,
  className,
  iconClassName,
  ...rest
}: IconButtonProps) {
  return (
    <button
      type="button"
      className={cn('inline-flex shrink-0 items-center justify-center rounded-full', className)}
      style={{ width: size, height: size }}
      {...rest}
    >
      <Icon size={iconSize} strokeWidth={strokeWidth} className={iconClassName} />
    </button>
  )
}
