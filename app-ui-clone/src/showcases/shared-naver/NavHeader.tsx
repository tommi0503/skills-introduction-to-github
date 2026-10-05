import type { ReactNode } from 'react'
import { ArrowLeft, X } from 'lucide-react'
import { cn } from '../../ui'

export interface BackTitleHeaderProps {
  title: ReactNode
  /** Vertical centre (logical px from the top of the screen). */
  centerY?: number
  color?: string
  titleSize?: number
  /** Slot rendered on the right edge. */
  right?: ReactNode
  /** Back-arrow icon size. */
  arrowSize?: number
  /** Left edge of the arrow glyph (logical px). */
  arrowLeft?: number
  /** Replace the default back arrow. */
  left?: ReactNode
  className?: string
}

/** "← Title" header, title centred. */
export function BackTitleHeader({
  title,
  centerY = 86,
  color = '#1d1d1d',
  titleSize = 18,
  right,
  left,
  arrowSize = 28,
  arrowLeft = 21.5,
  className,
}: BackTitleHeaderProps) {
  return (
    <div className={cn('absolute inset-x-0', className)} style={{ top: centerY - 20, height: 40, color }}>
      <div className="absolute flex h-full items-center" style={{ left: arrowLeft }}>
        {left ?? <ArrowLeft size={arrowSize} strokeWidth={(1.9 * 24) / arrowSize} style={{ marginLeft: -(arrowSize * 5) / 24 }} />}
      </div>
      <div
        className="absolute inset-x-0 flex h-full items-center justify-center font-semibold"
        style={{ fontSize: titleSize, letterSpacing: -0.2 }}
      >
        {title}
      </div>
      {right && <div className="absolute flex h-full items-center" style={{ right: 17 }}>{right}</div>}
    </div>
  )
}

export interface CloseHeaderProps {
  centerY?: number
  right?: number
  color?: string
  size?: number
}

/** A lone close (×) button on the top-right. */
export function CloseButton({ centerY = 85, right = 17, color = '#1d1d1d', size = 24 }: CloseHeaderProps) {
  return (
    <X
      size={size}
      strokeWidth={1.7}
      className="absolute"
      style={{ top: centerY - size / 2, right: right, color }}
    />
  )
}
