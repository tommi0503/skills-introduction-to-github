import type { ReactNode } from 'react'
import { cn } from '../../../ui'

interface RuledHeadingProps {
  children: ReactNode
  color?: string
  className?: string
}

/** Text framed by a rule above and below (campaign kicker). */
export function RuledHeading({ children, color = '#1f1f1f', className }: RuledHeadingProps) {
  return (
    <div className={cn('flex items-center justify-center', className)} style={{ borderTop: `1.5px solid ${color}`, borderBottom: `1.5px solid ${color}` }}>
      {children}
    </div>
  )
}
