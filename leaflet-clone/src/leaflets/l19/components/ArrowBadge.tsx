import { ArrowRight } from 'lucide-react'

export interface ArrowBadgeProps {
  size: number
  background: string
  color: string
}

/** Filled circle with a bold right arrow. */
export function ArrowBadge({ size, background, color }: ArrowBadgeProps) {
  return (
    <span className="inline-flex shrink-0 items-center justify-center rounded-full" style={{ width: size, height: size, background }}>
      <ArrowRight size={size * 0.62} strokeWidth={3.4} color={color} />
    </span>
  )
}
