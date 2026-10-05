import type { CSSProperties } from 'react'
import { cn } from '../core/cn'

export interface DividerProps {
  color?: string
  thickness?: number
  vertical?: boolean
  dashed?: boolean
  className?: string
  style?: CSSProperties
}

export function Divider({ color = 'currentColor', thickness = 1, vertical, dashed, className, style }: DividerProps) {
  const border = `${thickness}px ${dashed ? 'dashed' : 'solid'} ${color}`
  return (
    <div
      className={cn(vertical ? 'self-stretch' : 'w-full', className)}
      style={vertical ? { borderLeft: border, ...style } : { borderTop: border, ...style }}
    />
  )
}
