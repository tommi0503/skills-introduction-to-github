import { ArrowBigRight } from 'lucide-react'

export interface ArrowBadgeProps {
  size: number
  background: string
  color: string
}

/** Filled circle with a solid block arrow. */
export function ArrowBadge({ size, background, color }: ArrowBadgeProps) {
  return (
    <span className="inline-flex shrink-0 items-center justify-center rounded-full" style={{ width: size, height: size, background }}>
      <ArrowBigRight size={size * 0.62} strokeWidth={1} color={color} fill={color} />
    </span>
  )
}
