import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'

export interface FadeTextProps {
  /** CSS gradient painted through the glyphs. */
  gradient: string
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/** Text whose colour is a horizontal gradient (the reference fades words in/out). */
export function FadeText({ gradient, className, style, children }: FadeTextProps) {
  return (
    <span
      className={cn('inline-block bg-clip-text text-transparent', className)}
      style={{ backgroundImage: gradient, WebkitBackgroundClip: 'text', ...style }}
    >
      {children}
    </span>
  )
}
