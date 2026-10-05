import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'

/** Small rectangular badge (e.g. "#1 Italian", "Buy 1, get 1"). */
export function Tag({ children, className, style }: { children: ReactNode; className?: string; style?: CSSProperties }) {
  return (
    <span className={cn('inline-flex items-center rounded-[3px] px-[5px] whitespace-nowrap', className)} style={style}>
      {children}
    </span>
  )
}
