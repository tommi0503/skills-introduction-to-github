import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export interface SpeechBubbleProps {
  /** Which side the tail points out of. */
  tail: 'left' | 'right'
  width: number
  height: number
  color?: string
  radius?: number
  /** Distance of the tail tip from the bubble bottom. */
  tailBottom?: number
  tailSize?: number
  className?: string
  children: ReactNode
}

/** Rounded rectangle with a small triangular tail on one side. */
export function SpeechBubble({
  tail,
  width,
  height,
  color = '#d5e3f1',
  radius = 14,
  tailBottom = 22,
  tailSize = 12,
  className,
  children,
}: SpeechBubbleProps) {
  const tailStyle =
    tail === 'right'
      ? { right: -tailSize + 1, borderLeft: `${tailSize}px solid ${color}`, borderBottom: `${tailSize}px solid transparent` }
      : { left: -tailSize + 1, borderRight: `${tailSize}px solid ${color}`, borderBottom: `${tailSize}px solid transparent` }
  return (
    <div className={cn('relative', className)} style={{ width, height, background: color, borderRadius: radius }}>
      <span className="absolute h-0 w-0" style={{ bottom: tailBottom, ...tailStyle }} />
      {children}
    </div>
  )
}
