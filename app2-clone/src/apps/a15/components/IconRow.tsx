import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export interface IconRowProps {
  icon: ReactNode
  title: ReactNode
  sub?: ReactNode
  trailing?: ReactNode
  /** Horizontal gap from the icon column's left edge to the text. */
  textLeft: number
  className?: string
  titleClassName?: string
  subClassName?: string
}

/** Leading icon + title/subtitle (+ trailing) list row. */
export function IconRow({ icon, title, sub, trailing, textLeft, className, titleClassName, subClassName }: IconRowProps) {
  return (
    <div className={cn('relative flex items-center', className)}>
      <div className="absolute left-0 flex items-center justify-center">{icon}</div>
      <div className="min-w-0 flex-1" style={{ marginLeft: textLeft }}>
        <div className={titleClassName}>{title}</div>
        {sub && <div className={subClassName}>{sub}</div>}
      </div>
      {trailing}
    </div>
  )
}
