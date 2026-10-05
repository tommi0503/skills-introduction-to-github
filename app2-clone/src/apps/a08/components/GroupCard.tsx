import { Children, type ReactNode } from 'react'
import { cn } from '../../../ui'

/** Rounded white card; rows are separated by inset hairlines. */
export function GroupCard({ children, inset = 58, className }: { children: ReactNode; inset?: number; className?: string }) {
  return (
    <div className={cn('overflow-hidden rounded-[16px] bg-white', className)}>
      {Children.toArray(children).map((child, i) => (
        <div key={i} className="relative">
          {i > 0 && <div className="absolute top-0 right-0 h-px bg-[#ebebed]" style={{ left: inset }} />}
          {child}
        </div>
      ))}
    </div>
  )
}
