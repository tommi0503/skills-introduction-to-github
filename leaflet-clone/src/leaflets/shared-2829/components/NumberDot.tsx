import { cn } from '../../../ui'

export interface NumberDotProps {
  label: string
  color: string
  size?: number
  className?: string
}

/** Small filled circle with a number (map legend bullets). */
export function NumberDot({ label, color, size = 15, className }: NumberDotProps) {
  return (
    <span
      className={cn('inline-flex shrink-0 items-center justify-center rounded-full font-bold leading-none text-white', className)}
      style={{ width: size, height: size, background: color, fontSize: size * 0.62 }}
    >
      {label}
    </span>
  )
}
