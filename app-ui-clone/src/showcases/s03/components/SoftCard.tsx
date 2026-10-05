import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'

interface SoftCardProps {
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/** Light-grey rounded surface used for trackers, stats and lists. */
export function SoftCard({ className, style, children }: SoftCardProps) {
  return (
    <div className={cn('rounded-[20px] bg-[#f6f6f6]', className)} style={style}>
      {children}
    </div>
  )
}
