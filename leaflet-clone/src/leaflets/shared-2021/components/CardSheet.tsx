import type { ReactNode } from 'react'
import { cn } from '../../../ui'
import { theme2021 } from '../theme'

export interface CardInsets {
  left: number
  top: number
  right: number
  bottom: number
}

export interface CardSheetProps {
  insets: CardInsets
  radius?: number
  background?: string
  className?: string
  children?: ReactNode
}

/** The rounded near-white card that sits on the light-blue paper of every panel. */
export function CardSheet({ insets, radius = 30, background = theme2021.card, className, children }: CardSheetProps) {
  return (
    <div
      className={cn('absolute', className)}
      style={{ left: insets.left, top: insets.top, right: insets.right, bottom: insets.bottom, borderRadius: radius, background }}
    >
      {children}
    </div>
  )
}
