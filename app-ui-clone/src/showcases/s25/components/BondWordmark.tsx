import { cn } from '../../../ui'

export interface BondWordmarkProps {
  text: string
  size: number
  className?: string
}

/** The heavy lowercase "bond" wordmark, set as type. */
export function BondWordmark({ text, size, className }: BondWordmarkProps) {
  return (
    <span
      className={cn('font-poppins font-bold text-black', className)}
      style={{ fontSize: size, lineHeight: 1, letterSpacing: -size * 0.07 }}
    >
      {text}
    </span>
  )
}
