import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'

export interface NeoBoxProps {
  className?: string
  style?: CSSProperties
  /** offset shadow colour (neo-brutalist drop) */
  shadow?: string
  offset?: number
  children?: ReactNode
}

/** Bordered box with a hard offset shadow — the app's signature button/chip style. */
export function NeoBox({ className, style, shadow = '#111', offset = 3, children }: NeoBoxProps) {
  return (
    <div
      className={cn('flex items-center justify-center border-[1.5px] border-[#111]', className)}
      style={{ boxShadow: `${offset}px ${offset}px 0 ${shadow}`, ...style }}
    >
      {children}
    </div>
  )
}
