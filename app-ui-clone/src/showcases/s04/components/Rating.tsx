import { Star } from 'lucide-react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export interface RatingProps {
  value: string
  count: string
  size?: number
  className?: string
}

/** Filled star + bold score + muted review count. */
export function Rating({ value, count, size = 14, className }: RatingProps) {
  return (
    <span className={cn('inline-flex items-center gap-[4px]', className)}>
      <Star size={size} fill={theme.star} color={theme.star} strokeWidth={1} />
      <b className="font-semibold text-[#1c1c1c]">{value}</b>
      <span className="text-[#9a9a9a]">{count}</span>
    </span>
  )
}
